"""Demo: wire the V9 24/7 operating cycle through the MHS-style orchestrator.

Triggers:
  1. Medium replenishment  -> every 6 h  -> pipette capability
  2. Objective cleaning    -> SNR drop >10% -> arm 'wipe' capability
  3. Sample exchange       -> 'mitosis complete' Vision event -> arm pick-and-place
  4. Waste removal         -> per cadence -> transfer box

Escalation: any task whose handler confidence < 0.7 is queued for a human.
Run briefly with max_events to see the loop; in production tick down to ~1s
and let it run unattended.
"""
from __future__ import annotations

from argus_mhs.orchestrator import Orchestrator


def build_orchestrator() -> Orchestrator:
    o = Orchestrator()

    # -- capabilities (execute through Tool Bridge / drivers) --
    def pipette_medium(orch, payload=None):
        print("[cap] pipette medium replenishment")
        return orch.stack["pipette"](orch, payload)

    def wipe_objective(orch, payload=None):
        print("[cap] arm wipe objective (immersion, lens)")
        return "ok"

    def exchange_sample(orch, payload=None):
        print("[cap] arm pick-and-place sample exchange")
        return "ok"

    def remove_waste(orch, payload=None):
        print("[cap] transfer-box waste out (tray full)")
        return "ok"

    o.stack_capability("pipette", lambda o2, p=None: (print("[cap] pipette")))
    o.stack_capability("wipe", wipe_objective)
    o.stack_capability("exchange", exchange_sample)
    o.stack_capability("waste", remove_waste)

    # -- tasks --
    o.every("medium_replenish", 6 * 3600, lambda o2: o2.cap("pipette"),
            min_conf=0.95)
    # objective cleaning on SNR drop is normally Vision-triggered; demo as event:
    o.on_event("sample_exchange", lambda o2: o2.cap("exchange"), min_conf=0.9)
    o.on_event("waste_removal", lambda o2: o2.cap("waste"), min_conf=0.6)

    # mark the sample-exchange handler as low-confidence to demo escalation
    def low_conf(orch, payload=None): return "risky step"
    low_conf.confidence = 0.5
    o.on_event("manual_confirm_step", low_conf, min_conf=0.7)

    return o


if __name__ == "__main__":
    orch = build_orchestrator()
    orch.run(tick=0.2, max_events=6)
    print("\nEscalations (human queue):", orch.escalations)
    print("Task statuses:")
    for t in orch._heap if hasattr(orch, "_heap") else []:
        pass
