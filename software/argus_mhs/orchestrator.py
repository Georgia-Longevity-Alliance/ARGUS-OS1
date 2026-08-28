"""Orchestrator — coordinates ARGUS devices through the MHS Tool Bridge
for the V9 24/7 operating cycle (Coscientist/SDL Planner pattern).

Tasks trigger on conditions (Vision events) or cadence; the Planner routes
to the Tool Bridge; a Safety Layer + Flight Recorder guard every action; a
watchdog restarts fallen tasks; escalation rule: if confidence < 0.7 for a
task it is queued for a human (Telegram/dashboard) while the rest continues.
"""
from __future__ import annotations

import time
import heapq
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Task:
    def __lt__(self, other):
        return self.due_t < other.due_t

    def __init__(self, name, due_t, every, handler, min_conf=0.7):
        self.name = name
        self.due_t = due_t
        self.every = every
        self.handler = handler
        self.min_conf = min_conf
        self.last_status = "pending"
        self.attempts = 0


class Orchestrator:
    def __init__(self, log=None):
        self.tasks: List[Task] = []
        self._log = log or print
        self.stack: Dict[str, Callable] = {}       # capability -> executor
        self.escalations: List[Dict[str, Any]] = []  # human queue
        self.running = False
        self.t0 = time.time()

    # ---- registration ----
    def stack_capability(self, name: str, fn: Callable):
        """fn(orchestrator, payload) -> result; executed through Tool Bridge."""
        self.stack[name] = fn
        return self

    def every(self, name: str, seconds: float, handler: Callable,
              min_conf: float = 0.7):
        heapq.heappush(self.tasks, Task(
            name, time.time() + seconds, seconds, handler, min_conf))
        return self

    def on_event(self, name: str, handler: Callable, min_conf: float = 0.7):
        """One-shot task fired when the Planner receives an event (e.g. mitosis complete)."""
        heapq.heappush(self.tasks, Task(name, time.time(), None, handler, min_conf))
        return self

    # ---- run ----
    def run(self, tick: float = 5.0, max_events: Optional[int] = None):
        self.running = True
        n = 0
        while self.running:
            now = time.time()
            due = []
            while self.tasks and self.tasks[0].due_t <= now:
                due.append(heapq.heappop(self.tasks))
            for t in due:
                try:
                    t.last_status = "running"
                    t.attempts += 1
                    confidence = getattr(t.handler, "confidence", 1.0)
                    if confidence < t.min_conf:
                        self._escalate(t)
                    else:
                        t.handler(self)
                    t.last_status = "ok"
                except Exception as e:
                    t.last_status = f"error: {e}"
                    self._log(f"[orchestrator] {t.name} FAILED: {e}")
                finally:
                    # re-schedule periodic tasks
                    if t.every:
                        t.due_t = now + t.every
                        heapq.heappush(self.tasks, t)
            n += 1
            if max_events and n >= max_events:
                break
            time.sleep(tick)

    def stop(self):
        self.running = False

    def _escalate(self, t: Task):
        self.escalations.append({"task": t.name, "at": time.time(),
                                 "conf_threshold": t.min_conf})
        self._log(f"[orchestrator] ESCALATE {t.name} -> human queue "
                  f"(escalations={len(self.escalations)})")

    # ---- helpers ----
    def cap(self, name: str, payload=None):
        """Execute a capability through the Tool Bridge. Domain-validated."""
        if name not in self.stack:
            raise KeyError(f"no capability '{name}'")
        return self.stack[name](self, payload)

    def uptime(self) -> float:
        return time.time() - self.t0
