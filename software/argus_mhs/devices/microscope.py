"""OpenFlexure microscope driver (ARGUS-OS1) — MHS-style."""
from __future__ import annotations

from typing import Any

from argus_mhs.driver import MHSDriver, Tag

SCOPE_TAG = Tag(
    description="OpenFlexure microscope (ARGUS-OS1), 40x/0.75 dry",
    weight_kg=4.0,
    read=["stage_xyz", "focus", "temperature", "snr"],
    write=["move_stage", "set_focus", "capture", "led"],
    safety_limits={
        "move_stage": {"min": [0, 0, 0], "max": [30, 30, 15]},
        "set_focus":  {"min": 0, "max": 20},
        "led":        {"min": 0, "max": 100},
    },
    units={"stage_xyz": "mm", "focus": "mm", "temperature": "C"},
)


class ScopeDriver(MHSDriver):
    def __init__(self, hw):
        """hw = OpenFlexure control / Motor Release API."""
        super().__init__("argus/scope", SCOPE_TAG)
        self.hw = hw

    def _read_impl(self, qty: str) -> Any:
        if qty == "stage_xyz":
            return self.hw.position()
        if qty == "focus":
            return self.hw.focus_position()
        if qty == "temperature":
            return self.hw.temp()
        if qty == "snr":
            return self.hw.report_snr()          # from Vision (YOLO/CellPose)
        return None

    def _write_impl(self, qty: str, value: Any) -> Any:
        if qty == "move_stage":
            self.hw.move_abs(value)
            return self.hw.position()
        if qty == "set_focus":
            self.hw.focus_abs(value)
            return self.hw.focus_position()
        if qty == "capture":
            return self.hw.capture(value)
        if qty == "led":
            self.hw.set_led(value)
            return "ok"
        return None
