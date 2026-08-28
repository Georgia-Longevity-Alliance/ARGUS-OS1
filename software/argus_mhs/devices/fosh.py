"""FOSH micromanipulator driver (OS3) — MHS-style.

Positioning of microinjection capillaries / cell-manipulation tools inside the
enclosure. Shares the same NEMA17 + TMC2209 stack. Body Law limits enforced
via Safety Layer; collisions with V9-HANDS are avoided by a no-go zone map
checked before any move.
"""
from __future__ import annotations

from typing import Any, Optional

from argus_mhs.driver import MHSDriver, Tag

FOSH_TAG = Tag(
    description="FOSH 3-5 DOF micromanipulator (OS3), inside enclosure",
    weight_kg=5.0,
    read=["tip_xyz", "speed", "force"],
    write=["move_tip", "set_speed", "home"],
    safety_limits={
        "move_tip": {"min": [-50, -50, -50],
                     "max": [50, 50, 50],
                     "confirm": True},   # near-object manipulation
        "force":   {"max": 4.0},
        "set_speed": {"min": 0.1, "max": 100.0},
    },
    units={"tip_xyz": "um", "speed": "um/s", "force": "mN"},
)


class FoshDriver(MHSDriver):
    def __init__(self, manip, no_go: Optional[list] = None):
        super().__init__("argus/fosh", FOSH_TAG)
        self.manip = manip
        self.no_go = no_go or []          # no-go zones (list of [min,max] boxes)

    def _collision_check(self, target):
        for box in self.no_go:
            lo, hi = box
            if all(lo[i] <= target[i] <= hi[i] for i in range(len(target))):
                raise PermissionError(f"collision: target {target} inside no-go zone {box}")

    def _read_impl(self, qty: str) -> Any:
        if qty == "tip_xyz":
            return self.manip.position()
        if qty == "speed":
            return self.manip.speed()
        if qty == "force":
            return self.manip.force_mN()
        return None

    def _write_impl(self, qty: str, value: Any) -> Any:
        if qty == "move_tip":
            self._collision_check(value)
            self.manip.move(value)
            return self.manip.position()
        if qty == "set_speed":
            self.manip.set_speed(value)
            return value
        if qty == "home":
            self.manip.home()
            return "ok"
        return None
