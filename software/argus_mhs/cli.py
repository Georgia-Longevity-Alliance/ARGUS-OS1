"""CLI transport (MHS: read / write / discover) for registered ARGUS drivers.

Usage:
    python -m argus_mhs.cli list
    python -m argus_mhs.cli read <device> <qty>
    python -m argus_mhs.cli write <device> <qty> <json-value>
    python -m argus_mhs.cli reference <device>
"""
from __future__ import annotations

import argparse
import json
import sys

from argus_mhs.mcp_server import _devices, register
from argus_mhs.devices.arm import ArmDriver
from argus_mhs.devices.microscope import ScopeDriver
from argus_mhs.devices.pipette import PipetteDriver
from argus_mhs.devices.transfer_box import TransferBoxDriver
from argus_mhs.devices.fosh import FoshDriver


class _HW:
    """Stub hardware for demoing the CLI without real actuators."""
    def __getattr__(self, name):
        if name in ("position", "focus_position", "temp", "report_snr"):
            return lambda *a, **k: (0 if name == "temp" else [0, 0, 0])
        if name in ("volume", "plunger_pos", "pressure_kpa", "door_state",
                    "uv_c", "delta_p", "cycle_state", "speed", "force_mN"):
            return lambda *a, **k: 0
        if name in ("move_abs", "focus_abs", "capture", "set_led", "set_flow",
                    "aspirate", "dispense", "home", "actuate", "start_uv_c",
                    "purge_hepa", "move", "set_speed", "move_to", "write_reg",
                    "read_reg"):
            return lambda *a, **k: None
        raise AttributeError(name)


def _build_default_registry():
    register(ScopeDriver(_HW(), vision=None))
    register(ArmDriver(_HW(), "L", 0x11))
    register(ArmDriver(_HW(), "R", 0x12))
    register(FoshDriver(_HW()))
    register(PipetteDriver(_HW()))
    register(TransferBoxDriver(_HW()))
    return _devices


def main(argv=None):
    p = argparse.ArgumentParser(prog="argus-cli")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list")
    sub.add_parser("reference").add_argument("device")
    r = sub.add_parser("read"); r.add_argument("device"); r.add_argument("qty")
    w = sub.add_parser("write")
    w.add_argument("device"); w.add_argument("qty"); w.add_argument("value")

    args = p.parse_args(argv)
    devs = _build_default_registry()

    if args.cmd == "list":
        for d in devs.values():
            print(json.dumps(d.discover()))
    elif args.cmd == "reference":
        print(devs[args.device].reference_file())
    elif args.cmd == "read":
        print(json.dumps(devs[args.device].read(args.qty)))
    elif args.cmd == "write":
        val = json.loads(args.value)
        print(json.dumps(devs[args.device].write(args.qty, val)))


if __name__ == "__main__":
    main()
