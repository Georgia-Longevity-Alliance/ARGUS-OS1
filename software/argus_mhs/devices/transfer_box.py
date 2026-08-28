"""Pass-through transfer box driver (V9-TRANSFER) — MHS-style.

Hardware interlock: outer and inner doors can NEVER both be open. The inner
door opens only when UV-C cycle is complete (UV=0) and pressure differential
is nominal, and only by the robot hand (never manually).
"""
from __future__ import annotations

from typing import Any

from argus_mhs.driver import MHSDriver, Tag

TRANSFER_TAG = Tag(
    description="Pass-through airlock transfer box (V9-TRANSFER) for consumables",
    weight_kg=12.0,
    read=["door_outer", "door_inner", "uv_c", "delta_p", "cycle_state"],
    write=["open_outer", "open_inner", "start_uv_c", "purge"],
    safety_limits={
        "open_inner": {"confirm": True},   # irreversible containment action
        "open_outer": {"confirm": True},
    },
    units={"delta_p": "Pa", "uv_c": "uW/cm^2"},
)


class TransferBoxDriver(MHSDriver):
    def __init__(self, hw, box="A"):
        super().__init__(f"argus/transfer/{box}", TRANSFER_TAG)
        self.hw = hw                       # interlock controller + sensors

    # -- interlock invariant enforced in logic --
    def _interlock_ok(self, which: str) -> bool:
        other = "open_outer" if which == "open_inner" else "open_inner"
        if self.hw.door_state(other):
            raise PermissionError("interlock: other door open")
        if which == "open_inner":
            # inner door only after UV-C=0 and DP nominal
            if self.hw.uv_c() > 0:
                raise PermissionError("interlock: UV-C not complete")
            if not self.hw.dp_nominal():
                raise PermissionError("interlock: pressure differential off")
        return True

    def _read_impl(self, qty: str) -> Any:
        if qty == "door_outer":
            return self.hw.door_state("open_outer")
        if qty == "door_inner":
            return self.hw.door_state("open_inner")
        if qty == "uv_c":
            return self.hw.uv_c()
        if qty == "delta_p":
            return self.hw.delta_p()
        if qty == "cycle_state":
            return self.hw.cycle_state()
        return None

    def _write_impl(self, qty: str, value: Any) -> Any:
        if qty in ("open_outer", "open_inner"):
            self._interlock_ok(qty)
            return self.hw.actuate(qty, bool(value))
        if qty == "start_uv_c":
            return self.hw.start_uv_c(float(value))   # minutes
        if qty == "purge":
            self.hw.purge_hepa()
            return "ok"
        return None
