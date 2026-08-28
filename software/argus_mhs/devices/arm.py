"""V9-HANDS cable-driven arm driver (MHS-style) with Body Law limits."""
from __future__ import annotations

import time
from typing import Any

from argus_mhs.driver import MHSDriver, Tag

ARM_TAG = Tag(
    description="Cable-driven 6-DOF arm through glove-port sleeve (V9-HANDS)",
    weight_kg=2.5,
    read=["pose", "force", "speed", "current", "gripper"],
    write=["move", "gripper", "speed_limit", "force_limit"],
    safety_limits={
        "force": {"max": 5.0},              # Body Law: F <= 5 N
        "speed": {"max": 200.0},            # Body Law: v <= 200 mm/s
        "move":  {"min": [-200, -200, -200],
                  "max": [200, 200, 200],
                  "confirm": True},         # irreversible -> human-in-the-loop
    },
    units={"pose": "mm", "force": "N", "speed": "mm/s"},
)


class ArmDriver(MHSDriver):
    def __init__(self, bus, arm="L", node_id=0x11):
        super().__init__(f"argus/arm/{arm}", ARM_TAG)
        self.bus = bus
        self.node_id = node_id
        self._pose = [0, 0, 0]

    def _read_impl(self, qty: str) -> Any:
        if qty == "pose":
            return self._pose
        if qty == "force":
            return self.bus.read_reg(self.node_id, 0x30) / 1000.0
        if qty == "speed":
            return self.bus.read_reg(self.node_id, 0x32)
        return 0

    def _write_impl(self, qty: str, value: Any) -> Any:
        if qty == "gripper":
            self.bus.write_reg(self.node_id, 0x40, 1 if value else 0)
            return "ok"
        if qty == "move":
            self._move_to(value)
            return self._pose
        return None

    def _move_to(self, target):
        vmax = self.tag.safety_limits["speed"]["max"]
        steps = int(vmax ** 0.5) or 1
        for k in range(1, steps + 1):
            step = [self._pose[i] + (target[i] - self._pose[i]) * k / steps
                    for i in range(3)]
            dt = 0.05
            for i in range(3):  # clamp per-tick velocity to Body Law
                d = abs(step[i] - self._pose[i])
                if d / dt > vmax:
                    sgn = 1 if step[i] > self._pose[i] else -1
                    step[i] = self._pose[i] + sgn * vmax * dt
            self.bus.move_to(self.node_id, step)
            self._pose = step
            time.sleep(dt)
