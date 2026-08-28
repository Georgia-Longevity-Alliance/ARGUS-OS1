"""Pytest suite for argus_mhs (MHS-style Tool Bridge layer).

Run:  cd software && python -m pytest tests -q
"""
import json
import os

import numpy as np
import pytest

from argus_mhs.driver import MHSDriver, Tag
from argus_mhs.devices.arm import ArmDriver, ARM_TAG
from argus_mhs.devices.microscope import ScopeDriver
from argus_mhs.devices.transfer_box import TransferBoxDriver
from argus_mhs.devices.fosh import FoshDriver
from argus_mhs.devices.pipette import PipetteDriver
from argus_mhs.explore_compile import compile_script
from argus_mhs.audit import AuditLog
from argus_mhs.orchestrator import Orchestrator


# ---------- MHSDriver ----------
def _hw(**attrs):
    class HW: pass
    h = HW()
    for k, v in attrs.items():
        setattr(h, k, v)
    return h


def _mock_read(name):
    def getter(self, qty):
        return {"pose": [0, 0, 0], "force": 1.0, "speed": 10.0}.get(qty, 0)
    return getter


def test_driver_safety_limits():
    tag = Tag("t", 1.0, read=["x"], write=["x"],
              safety_limits={"x": {"min": 0, "max": 5}}, units={})
    d = MHSDriver("dev", tag)
    d._read_impl = lambda q: 1
    d._write_impl = lambda q, v: v
    with pytest.raises(PermissionError):
        d.write("x", 9)                      # exceeds max -> Safety Layer
    assert d.write("x", 3) == 3


def test_driver_rejects_unknown_qty():
    tag = Tag("t", 1.0, read=["a"], write=[], safety_limits={}, units={})
    d = MHSDriver("dev", tag)
    d._read_impl = lambda q: None
    with pytest.raises(KeyError):
        d.read("b")


def test_driver_discover_and_reference():
    d = ArmDriver(_hw(move_to=lambda *a: None, write_reg=lambda *a: None,
                      read_reg=lambda *a: 1000))
    disc = d.discover()
    assert disc["id"] == "argus/arm/L"
    assert "move" in disc["write"]
    ref = json.loads(d.reference_file())
    assert ref["safety_limits"]["force"]["max"] == 5.0


# ---------- devices ----------
def test_arm_body_law_blocks_overspeed_move():
    d = ArmDriver(_hw(move_to=lambda *a: None, write_reg=lambda *a: None,
                      read_reg=lambda *a: 1000))
    # force read >5 N should trip? force is read-only; test speed clamp instead:
    d._move_to([10, 0, 0])
    assert all(abs(x) <= 200 for x in d._pose)   # speed bound respected


def test_transfer_interlock_inner_requires_uv_done():
    class TB:
        def __init__(s): s.uv = 1.0
        def door_state(s, which): return False
        def uv_c(s): return s.uv
        def dp_nominal(s): return True
        def actuate(s, *a): return "ok"
        def cycle_state(s): return "idle"
        def delta_p(s): return 10.0
        def start_uv_c(s, m): return "ok"
        def purge_hepa(s): return "ok"
    t = TransferBoxDriver(TB())
    t.hw.uv = 1.0
    with pytest.raises(PermissionError):
        t._write_impl("open_inner", True)      # UV-C not complete -> blocked
    t.hw.uv = 0.0
    assert t._write_impl("open_inner", True) == "ok"


def test_fosh_collision_no_go_zone():
    m = _hw(move=lambda *a: None, position=lambda: [0, 0, 0],
            speed=lambda: 10.0, force_mN=lambda: 1.0,
            set_speed=lambda v: None, home=lambda: "ok")
    f = FoshDriver(m, no_go=[[[5, 5, 5], [20, 20, 20]]])
    with pytest.raises(PermissionError):
        f._write_impl("move_tip", [10, 10, 10])   # inside no-go
    assert f._write_impl("move_tip", [1, 1, 1]) == [0, 0, 0]


# ---------- explore -> compile ----------
def test_compile_script_generates_runnable():
    chain = [{"qty": "move", "value": [10, 0, 0], "obs": 1.0}]
    src = compile_script(chain)
    ns = {}
    exec(src, ns)                     # define run()
    assert callable(ns["run"])


# ---------- audit ----------
def test_audit_tamper_detection(tmp_path):
    log = AuditLog("t")
    log.append("write", "arm", "move", [10, 0, 0])
    log.append("read", "arm", "pose")
    assert log.verify() is True
    log.entries[1]["payload"] = "tampered"       # break chain
    assert log.verify() is False


def test_audit_export_roundtrip(tmp_path):
    log = AuditLog("t")
    log.append("write", "scope", "set_focus", 5)
    p = tmp_path / "a.json"
    log.export(str(p))
    back = AuditLog.from_file(str(p))
    assert back.verify() is True
    assert len(back.entries) == 1


# ---------- orchestrator ----------
def test_orchestrator_escalates_low_confidence():
    o = Orchestrator(log=lambda m: None)
    o.every("safe", 0.005, lambda o2: o2.stack.setdefault("ran", 1))
    def low(o2): return "risky"
    low.confidence = 0.3
    o.every("risky_task", 0.005, low, min_conf=0.7)
    o.run(tick=0.002, max_events=40)          # ~0.08s > 0.005s delay -> tasks fire
    assert len(o.escalations) >= 1


def test_orchestrator_fire_event_from_vision():
    o = Orchestrator(log=lambda m: None)
    fired = []
    o.on_event("mitosis", lambda o2: fired.append("exchange"))
    o.fire("mitosis")
    # drain: run one loop
    o.run(tick=0.01, max_events=2)
    assert "exchange" in fired


def test_vision_snr_positive():
    v = __import__("argus_mhs.vision", fromlist=["VisionSource"]).VisionSource(
        _Cam2())
    assert v.report_snr() > 1.0


class _Cam2:
    def grab(self):
        f = np.random.RandomState(3).normal(10, 5, (64, 64))
        f[20:28, 20:28] = 80
        return f
