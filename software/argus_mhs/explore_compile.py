"""Exploration -> compile pattern (MHS): learn a procedure, then run it
deterministically as a single command. Application: closed-loop autofocus /
fluid-dynamics optimization with Vision (camera) as ground truth."""
from __future__ import annotations

from typing import Any, Callable, Dict, List


def explore_and_compile(driver, goal: str, callback, max_steps: int = 20) -> str:
    """Iteratively tune a device, observe result, compile a deterministic script."""
    chain: List[Dict[str, Any]] = []
    for _ in range(max_steps):
        action = callback.pick_next_action(goal, chain)   # agent decides -> write()
        result = driver.write(action["qty"], action["value"])
        obs = callback.observe(result)                    # camera / Vision snapshot
        chain.append({"qty": action["qty"], "value": action["value"], "obs": obs})
        if callback.is_done(obs):
            return compile_script(chain)
    raise TimeoutError("not converged")


def compile_script(chain: List[Dict[str, Any]]) -> str:
    """Package the chain into a deterministic code file (single command)."""
    lines = ["def run(driver):"]
    for i, c in enumerate(chain):
        lines.append(f"    r{i} = driver.write({c['qty']!r}, {c['value']!r})")
    lines.append("    return locals()")
    src = "\n".join(lines)
    with open("compiled_procedure.py", "w") as f:
        f.write(src)
    return src
