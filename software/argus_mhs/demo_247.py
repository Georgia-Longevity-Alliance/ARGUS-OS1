"""Demo: wire the V9 24/7 operating cycle through the MHS-style orchestrator.

Triggers:
  1. Medium replenishment -> every 6 h -> pipette capability
  2. Sample exchange      -> Vision 'mitosis' event -> arm pick-and-place
  3. Waste removal        -> 'waste' event -> transfer box
Escalation: any handler whose confidence < 0.7 is queued for a human.
After the loop, Flight Recorder is flushed into a tamper-evident AuditLog,
exported to JSON, and verified.

Run:  python -m argus_mhs.demo_247   (from software/)
"""
from __future__ import annotations

import numpy as np

from argus_mhs.orchestrator import Orchestrator
from argus_mhs.vision import VisionSource
from argus_mhs.audit import AuditLog, collect_drivers


class _Cam:
    def grab(self):
        # frame with a bright blob -> high SNR + a "mitosis-like" detection marker
        import numpy as _np
        f = _np.random.RandomState(7).normal(10, 2, (64, 64))
        f[30:34, 30:34] = 90
        return f


class _VisionEvents:
    """Wraps VisionSource and reports a 'mitosis' event when a mitosis fires."""
    def __init__(self):
        self.v = VisionSource(_Cam())
        self.detections = 2

    def poll(self):
        # Normally: self.v.mitosis(...) returns detections. Here 1 event first tick.
        if self.detections > 0:
            self.detections -= 1
            return ["mitosis"]
        return []


def build() -> Orchestrator:
    o = Orchestrator()
    o.stack_capability("pipette", lambda o2, p=None: print("[cap] pipette medium"))
    o.stack_capability("exchange", lambda o2, p=None: print("[cap] arm exchange sample"))
    o.stack_capability("waste", lambda o2, p=None: print("[cap] transfer-box waste out"))

    o.every("medium_replenish", 6 * 3600, lambda o2: o2.cap("pipette"), min_conf=0.95)
    o.on_event("mitosis", lambda o2: o2.cap("exchange"), 0.9)
    o.on_event("waste", lambda o2: o2.cap("waste"), 0.6)

    # demo escalation: low-confidence step
    def risky(o): return "needs human"
    risky.confidence = 0.5
    o.on_event("manual_confirm", lambda o2: risky(o2), min_conf=0.7)  # min_conf unused for events

    # attach vision event source -> schedules 'mitosis' handler
    o.attach_event_source(_VisionEvents().poll)
    return o


if __name__ == "__main__":
    orch = build()
    orch.run(tick=0.2, max_events=5)

    # escalate demo: fire a low-confidence event directly
    orch.fire("manual_confirm")

    # (b) Flight Recorder -> tamper-evident audit log
    audit = AuditLog("argus-demo")
    collect_drivers([], audit)     # no real drivers registered in demo, keep for parity
    for e in orch.escalations:
        audit.append("escalate", "orchestrator", e["task"], e)
    audit.export("/tmp/argus_audit.json")

    print("\nAudit entries:", len(audit.entries), "root_hash:", audit._prev)
    print("Audit verified (chain intact):", audit.verify())
