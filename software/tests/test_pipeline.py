"""Pytest suite for the ARGUS-OS1 tile pipeline (phantom-based, no hardware).

Run:  cd software && python -m pytest tests/test_pipeline.py -q

The phantom is generated once per session (session-scoped fixture) in a temp dir,
so the numbers asserted below are reproducible from source, not from stored data.
"""

from __future__ import annotations

import json
import os
import sys

import cv2
import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
PIPELINE = os.path.abspath(os.path.join(HERE, "..", "pipeline"))
sys.path.insert(0, PIPELINE)

import phantom  # noqa: E402
from blend import blend  # noqa: E402
from evaluate import psnr, seam_score, sharpness  # noqa: E402
from measure_rom import measure  # noqa: E402
from qc import gate, scan  # noqa: E402
from tiles import load_tiles, register  # noqa: E402


def _truth(phantom_dir: str) -> dict:
    meta = json.load(open(os.path.join(phantom_dir, "_phantom.json"), encoding="utf-8"))
    return {f["img"]: np.array([f["x"], f["y"]], float) for f in meta["fields"]}


@pytest.fixture(scope="session")
def ph(tmp_path_factory):
    d = str(tmp_path_factory.mktemp("phantom"))
    phantom.build(d, size=1080, tile=400, overlap=0.35)
    return d


@pytest.fixture(scope="session")
def tiles(ph):
    t = load_tiles(ph)
    register(t)
    return t


def test_registration_is_exact(ph, tiles):
    truth = _truth(ph)
    err = np.array([np.abs(t.pos - truth[os.path.basename(t.path)]).max() for t in tiles])
    assert err.max() <= 1.0, f"registration error max {err.max()} px"


def test_fusion_keeps_sharpness_at_least_85pct_of_ground_truth(ph, tiles):
    gt = cv2.imread(os.path.join(ph, "_ground_truth.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0
    img = blend(tiles, mode="fusion", progress=False)
    frac = sharpness(img) / sharpness(gt)
    assert frac >= 0.85, f"fusion sharpness only {frac:.2f} of ground truth"


def test_fusion_beats_plain_averaging_on_psnr(ph, tiles):
    gt = cv2.imread(os.path.join(ph, "_ground_truth.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0
    H, W = gt.shape[:2]
    fus = blend(tiles, mode="fusion", progress=False)[:H, :W]
    fea = blend(tiles, mode="feather", progress=False)[:H, :W]
    assert psnr(fus, gt) > psnr(fea, gt), "fusion must not be less accurate than averaging"


def test_seams_are_invisible(ph, tiles):
    bx = sorted({int(t.pos[0]) for t in tiles} | {int(t.pos[0] + t.w) for t in tiles})
    by = sorted({int(t.pos[1]) for t in tiles} | {int(t.pos[1] + t.h) for t in tiles})
    img = blend(tiles, mode="fusion", progress=False)
    assert seam_score(img, bx, by) < 1.05, "visible seams at tile borders"


def test_scan_qc_catches_half_resolution_gotcha(ph):
    meta = json.load(open(os.path.join(ph, "_phantom.json"), encoding="utf-8"))
    bad = {
        "image_count": len(meta["fields"]),
        "capture_mode": "standard",
        "full_resolution": [2800, 2800],
        "overlaps_xy": [0.35, 0.35],
        "pixel_size_um": 0.0388,
    }
    with open(os.path.join(ph, "scan_data.json"), "w", encoding="utf-8") as fh:
        json.dump(bad, fh)
    assert scan(ph) == 1, "QC must fail when declared resolution != actual"

    bad["capture_mode"], bad["full_resolution"] = "full", [400, 400]
    with open(os.path.join(ph, "scan_data.json"), "w", encoding="utf-8") as fh:
        json.dump(bad, fh)
    assert scan(ph) == 0, "QC must pass on a consistent scan"


def test_sampling_gate_matches_protocol_amendment_2():
    assert gate(0.0388, binning=2) == 0        # 40x/0.75 + 1.55 um pitch
    assert gate(0.100, binning=2) == 0         # exactly on the limit
    assert gate(0.155, binning=4) == 1         # merged centriole pairs


def test_rom_measurement_recovers_known_traverse(tmp_path):
    gt = phantom.make_ground_truth(8200, seed=11)
    rng = np.random.default_rng(3)
    step, tile, n = 120, 400, 12
    for i in range(n):
        patch = gt[2000:2000 + tile, i * step:i * step + tile].copy()
        gain = np.linspace(0.9, 1.1, tile, dtype=np.float32)[None, :, None]
        out = np.clip(patch * gain + rng.normal(0, 0.006, patch.shape), 0, 1)
        cv2.imwrite(str(tmp_path / f"frame_{i:03d}.png"), (out * 255).astype(np.uint8))
    res = measure(str(tmp_path), mpp_um=0.0388, axis="x")
    assert res["links_used"] == n - 1
    assert abs(res["median_step_px"] - step) <= 1.0
    assert abs(res["measured_travel_um"] - (n - 1) * step * 0.0388) < 0.05 * (n - 1) * step * 0.0388


# ---------- acceptance runner (A1/A2) against a mock OpenFlexure server ----------
def _serve(payloads: dict[str, dict]):
    import http.server
    import json as _json
    import threading

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            body = payloads.get(self.path)
            if body is None:
                self.send_response(404)
                self.end_headers()
                return
            data = _json.dumps(body).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, *exc):  # silence
            return

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def test_acceptance_flags_healthy_server():
    import acceptance

    payloads = {
        "/api/v2/instrument/": {"status": "ok", "firmware": {"name": "Sangaboard", "version": "v1.0.4"}},
        "/api/v2/actions": {"actions": ["move", "motor_release", "autofocus"]},
    }
    srv, url = _serve(payloads)
    try:
        a1, a2, _ = acceptance.check_a1_a2(acceptance.probe(url))
    finally:
        srv.shutdown()
    assert a1["status"] == "PASS", a1
    assert a2["status"] == "PASS", a2


def test_acceptance_flags_firmware_mismatch_and_missing_motor_release():
    import acceptance

    payloads = {
        "/api/v2/instrument/": {"firmware": {"version": "unknown"}, "warning": "firmware mismatch"},
        "/api/v2/actions": {"actions": ["move"]},
    }
    srv, url = _serve(payloads)
    try:
        a1, a2, _ = acceptance.check_a1_a2(acceptance.probe(url))
    finally:
        srv.shutdown()
    assert a1["status"] == "FAIL", a1
    assert a2["status"] == "UNKNOWN", a2          # silence is not consent


def test_acceptance_is_unknown_without_server():
    import acceptance

    a1, a2, log = acceptance.check_a1_a2({"/api/v2/": (0, "unreachable")})
    assert a1["status"] == "UNKNOWN" and a2["status"] == "UNKNOWN"
    assert "not reachable" in log


# ─── R2 (2026-11-19): verification is a deterministic gate, not a vote ───────────

def test_r2_verification_path_is_model_free():
    """No model dependency may enter the gate modules."""
    import invariants

    problems = invariants.check_all(PIPELINE)
    assert problems == [], "R2 invariant violated:\n" + "\n".join(problems)


def test_r2_checker_catches_a_planted_model_import(tmp_path):
    """The checker must actually fail on a violation, or it proves nothing."""
    import invariants

    gate = tmp_path / "qc.py"
    gate.write_text("import openai\n")
    problems = invariants.check_all(str(tmp_path))
    assert any("openai" in p for p in problems), problems


def test_r2_gate_must_not_depend_on_the_network(tmp_path):
    import invariants

    gate = tmp_path / "qc.py"
    gate.write_text("import urllib.request\n")
    problems = invariants.check_all(str(tmp_path))
    assert any("urllib" in p for p in problems), problems


def test_r2_accepted_risk_is_named():
    """We choose centralization and its single point of failure on purpose."""
    import invariants

    risk = invariants.accepted_failure_mode()
    assert risk["architecture"] == "centralized verification"
    assert "single point of failure" in risk["accepted_risk"]
    assert "2512.08296" in risk["evidence"]


# ─── R8 (2026-11-19): light-dose budget ─────────────────────────────────────────

def test_r8_exposure_and_total_dose():
    import light_dose as L

    # 1 mW/cm^2 for 1000 ms = 1e-3 W/cm^2 * 1 s = 1e-3 J/cm^2
    assert L.exposure_j_cm2(1.0, 1000.0) == pytest.approx(1e-3)
    total = L.total_dose_j_cm2(0.5, 50, frames=400, z_slices=5)
    assert total == pytest.approx(0.5e-3 * 0.050 * 400 * 5)  # = 5e-2 J/cm^2
    assert total == pytest.approx(5e-2)


def test_r8_unit_conventions_do_not_drift():
    """1 W/m^2 == 0.1 mW/cm^2 == 1 uW/mm^2 — the 10x datasheet trap."""
    import light_dose as L

    assert L.to_mw_cm2(1.0, "w/m2") == pytest.approx(0.1)
    assert L.to_mw_cm2(0.1, "mw/cm2") == pytest.approx(0.1)
    assert L.to_mw_cm2(1.0, "uw/mm2") == pytest.approx(0.1)
    assert L.to_mw_cm2(1.0, "w/cm2") == pytest.approx(1000.0)
    with pytest.raises(ValueError):
        L.to_mw_cm2(1.0, "candela")


def test_r8_no_threshold_is_invented():
    import light_dose as L

    res = L.budget(0.5, 50, frames=400, z_slices=5)
    assert res["verdict"] == "reported_only"          # no limit -> no verdict
    over = L.budget(0.5, 50, frames=400, z_slices=5, max_j_cm2=0.01)
    assert over["verdict"] == "exceeded"
    under = L.budget(0.5, 50, frames=400, z_slices=5, max_j_cm2=1.0)
    assert under["verdict"] == "pass"
    with pytest.raises(ValueError):
        L.budget(0.5, 50, frames=1, max_j_cm2=0)


# ─── R3 (2026-11-19): N-scaling harness on the frozen QC set ─────────────────────

def test_r3_harness_self_test():
    """Aggregators, gate control and the frozen set must all hold."""
    import n_scaling

    assert n_scaling.self_test() == 0


def test_r3_frozen_set_is_reproducible_and_balanced():
    import n_scaling

    items = n_scaling.build_items()
    assert len(items) == 30
    assert n_scaling.fingerprint(items) == n_scaling.fingerprint(n_scaling.build_items())
    # a gate (deterministic rater) must be exact on every item, traps included
    wrong = [i["id"] for i in items if n_scaling.rater_gate(i["report"]) != i["truth"]]
    assert wrong == [], f"gate control mismatched on {wrong}"
    # and voting must not change a perfect single rater
    truth = [i["truth"] for i in items]
    draws = [[n_scaling.rater_gate(i["report"])] * 9 for i in items]
    for n in (1, 3, 5, 9):
        assert n_scaling.nested_accuracy(draws, truth, n) == 1.0


# ─── R3 (2026-11-19): endomitosis gate — a division needs a furrow ───────────────

def test_r3_endomitosis_is_not_a_division():
    """Nuclear split without ingression must never become a division or a sister pair."""
    import lineage

    res = lineage.demo()
    assert res["correct"] is True, res
    assert res["divisions"] == res["expected_divisions"] == 6
    assert res["nuclear_splits"] == res["expected_endomitosis"] == 4
    assert res["sister_pairs"] == 6            # one pair per true division, none for endomitosis


def test_r3_sister_pairs_only_from_divisions():
    import lineage

    tracks, truth = lineage.make_phantom_tracks()
    ped = lineage.build_pedigree(tracks)
    assert len(ped["sister_pairs"]) == sum(1 for v in truth.values() if v == lineage.DIVISION)
    # every endomitotic track is excluded from pedigree aggregation and keeps no pair
    excluded = {e["cell"] for e in ped["excluded_from_pedigree"]}
    endo = {k for k, v in truth.items() if v == lineage.NUCLEAR_SPLIT_NO_FURROW}
    assert endo <= excluded
    for pair in ped["sister_pairs"]:
        assert pair["parent"] not in endo


def test_r3_furrow_threshold_is_the_only_knob_and_it_flips_a_borderline_case():
    """A borderline cell (ingression 0.15) must be decided by the documented threshold."""
    import lineage

    frames = [{"nuclei": 1, "furrow": 0.0}, {"nuclei": 2, "furrow": 0.15}]
    assert lineage.classify_transition(*frames, furrow_min=0.10) == lineage.DIVISION
    assert lineage.classify_transition(*frames, furrow_min=0.25) == lineage.NUCLEAR_SPLIT_NO_FURROW


def test_r3_explicit_cell_count_wins_over_the_image_index():
    import lineage

    prev = {"nuclei": 1, "furrow": 0.0}
    cur = {"nuclei": 2, "furrow": 0.0, "cell_count_delta": 1}
    assert lineage.classify_transition(prev, cur) == lineage.DIVISION


def test_r3_merge_and_flicker_are_not_events():
    import lineage

    assert lineage.classify_transition({"nuclei": 2, "furrow": 0.5},
                                       {"nuclei": 1, "furrow": 0.0}) == lineage.NO_EVENT
    assert lineage.classify_transition({"nuclei": 1, "furrow": 0.0},
                                       {"nuclei": 1, "furrow": 0.0}) == lineage.NO_EVENT
    with pytest.raises(ValueError):
        lineage.classify_transition({"nuclei": 1}, {"nuclei": 2, "furrow": 0.4})
    with pytest.raises(ValueError):
        lineage.classify_transition({"nuclei": 1, "furrow": 0.0},
                                    {"nuclei": 2, "furrow": 1.4})


def test_r3_pedigree_build_is_deterministic():
    import lineage

    tracks, _ = lineage.make_phantom_tracks()
    assert lineage.build_pedigree(tracks) == lineage.build_pedigree(tracks)
