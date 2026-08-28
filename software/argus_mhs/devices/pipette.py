"""Pipette / liquid handling driver (MHS-style).

Purposes: medium replenishment (DMEM/agarose), waste removal, microinjection
capillaries. Fluid dynamics matter — bubble formation is a physical failure
mode (MHS Genentech lesson): use gentle flow for viscous samples and a
human-in-the-loop confirm for aspiration/dispense of critical volumes.
"""
from __future__ import annotations

from typing import Any

from argus_mhs.driver import MHSDriver, Tag

PIPETTE_TAG = Tag(
    description="Syringe-pump pipette / medium replenishment tool (exchangeable end-effector)",
    weight_kg=0.8,
    read=["volume", "flow_rate", "plunger_pos", "pressure"],
    write=["aspirate", "dispense", "set_flow", "home"],
    safety_limits={
        "dispense": {"min": 0.0, "max": 1000.0, "confirm": True},   # uL, irreversible
        "aspirate": {"min": 0.0, "max": 1000.0, "confirm": True},
        "set_flow": {"min": 1.0, "max": 200.0},                     # uL/s, gentle for viscous
    },
    units={"volume": "uL", "flow_rate": "uL/s", "pressure": "kPa"},
)


class PipetteDriver(MHSDriver):
    def __init__(self, pump, tool="pipette"):
        super().__init__(f"argus/tool/{tool}", PIPETTE_TAG)
        self.pump = pump
        self._flow = 140.0            # uL/s default (aqueous)

    def _read_impl(self, qty: str) -> Any:
        if qty == "flow_rate":
            return self._flow
        if qty == "volume":
            return self.pump.volume()
        if qty == "plunger_pos":
            return self.pump.plunger_pos()
        if qty == "pressure":
            return self.pump.pressure_kpa()
        return None

    def _write_impl(self, qty: str, value: Any) -> Any:
        if qty == "set_flow":
            self._flow = float(value)
            self.pump.set_flow(self._flow)
            return self._flow
        if qty == "aspirate":
            self.pump.aspirate(float(value), self._flow)
            return self.pump.volume()
        if qty == "dispense":
            self.pump.dispense(float(value), self._flow)
            return self.pump.volume()
        if qty == "home":
            self.pump.home()
            return "ok"
        return None
