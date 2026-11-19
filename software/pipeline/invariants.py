"""R2 (2026-11-19) — verification invariants: a gate is deterministic, not a vote.

**The invariant.** Anything that decides whether ARGUS data is accepted must be a
deterministic, inspectable check. No language model may sit inside the verification
path, and no model may veto or overrule a gate verdict. Where a model is used at all,
it may only *propose*; the gate decides.

**Why (evidence, verified 2026-11-19):**

* Mieczkowski, Collins, Sucholutsky, Velez & Griffiths, "Language model teams as
  distributed systems", *PNAS* 123(47), 2026, doi:10.1073/pnas.2612825123 —
  centralized and decentralized team architectures have *asymmetric* vulnerabilities;
  the paper's frame is that each architecture fails differently, so the failure we
  accept must be named, not wished away.
* Kim et al., "Towards a Science of Scaling Agent Systems", arXiv:2512.08296 —
  across 260 configurations: "architectures without centralized verification tend to
  propagate errors more than those with centralized coordination".
* Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet",
  arXiv:2310.01798 — intrinsic self-correction without external feedback does not
  reliably work, so "the model checks itself" is not a verification strategy.
* Pappu, El, Cao et al., "Multi-Agent Teams Hold Experts Back", arXiv:2602.01011 —
  averaging expert with non-expert opinions loses up to 41.1% and the loss grows with
  team size; consensus is not a quality mechanism.

**The vulnerability we accept (named rather than hidden).** Centralized verification
creates a single point of failure: if `qc.py`/`acceptance.py` is wrong, every scan
inherits the error, and there is no second opinion to catch it. That is the trade we
choose, because the alternative — distributed judgment by models — trades a loud,
local, reproducible failure for a quiet, global, unmeasurable one. The single point is
mitigated by tests, by `--demo` dry runs and by the bundle's `sha256sum -c`, not by
adding a second opinion.

**How the invariant is enforced.** This module is the enforcement, and it is itself
tested (`tests/test_pipeline.py`): it reads the verification modules and fails if a
model dependency appears, or if a pure gate module grows a network dependency.

Run standalone:  python -m invariants [pipeline_dir]
Exit code 0 = invariant holds, 1 = violation.
"""

from __future__ import annotations

import os
import re
import sys

#: Imports that mean "a model has entered the verification path".
FORBIDDEN_MODEL_IMPORTS = (
    "openai",
    "anthropic",
    "transformers",
    "torch",
    "tensorflow",
    "keras",
    "onnxruntime",
    "sentence_transformers",
    "llama_cpp",
    "llama_index",
    "langchain",
    "vllm",
    "ollama",
    "google.generativeai",
    "mistralai",
    "cohere",
    "litellm",
    "cellpose",
    "stardist",
    "ultralytics",
    "sam2",
    "segment_anything",
)

#: Imports that mean "this module talks to the network". A gate that *decides* must
#: not depend on a remote answer, so these are forbidden in GATE_MODULES.
FORBIDDEN_NETWORK_IMPORTS = (
    "urllib",
    "requests",
    "httpx",
    "socket",
    "http.client",
    "aiohttp",
)

#: Modules that decide acceptance. Model-free AND network-free.
GATE_MODULES = (
    "qc.py",
    "blend.py",
    "evaluate.py",
    "tiles.py",
    "measure_rom.py",
    # 2026-11-19: the lineage/endomitosis gate decides whether an event counts as a
    # division, so it must be as inspectable as the scan gates (R3).
    "lineage.py",
    # Q2 census: turns hand scoring into a verdict, so it must be inspectable too.
    "centriole_census.py",
)

#: Modules that may talk to hardware (the microscope HTTP API) but still must not
#: contain a model dependency.
TOOL_MODULES = ("acceptance.py",)

_IMPORT_RE = re.compile(
    r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_.]*)", re.MULTILINE
)


def imported_roots(path: str) -> list[str]:
    """Top-level module names imported by a Python source file."""
    with open(path, "r", encoding="utf-8") as fh:
        src = fh.read()
    return [m.group(1) for m in _IMPORT_RE.finditer(src)]


def violations(path: str, forbidden: tuple[str, ...]) -> list[str]:
    """Imports of `forbidden` roots found in `path` (matches dotted prefixes)."""
    hits = []
    for name in imported_roots(path):
        for bad in forbidden:
            if name == bad or name.startswith(bad + "."):
                hits.append(f"{os.path.basename(path)}: imports `{name}` (forbidden `{bad}`)")
    return hits


def check_all(pipeline_dir: str | None = None) -> list[str]:
    """Return every violation of the verification invariant (empty = OK)."""
    if pipeline_dir is None:
        pipeline_dir = os.path.dirname(os.path.abspath(__file__))
    problems: list[str] = []

    for name in GATE_MODULES:
        path = os.path.join(pipeline_dir, name)
        if not os.path.exists(path):
            problems.append(f"{name}: gate module is missing")
            continue
        problems += violations(path, FORBIDDEN_MODEL_IMPORTS)
        problems += violations(path, FORBIDDEN_NETWORK_IMPORTS)

    for name in TOOL_MODULES:
        path = os.path.join(pipeline_dir, name)
        if not os.path.exists(path):
            problems.append(f"{name}: tool module is missing")
            continue
        problems += violations(path, FORBIDDEN_MODEL_IMPORTS)

    return problems


def accepted_failure_mode() -> dict[str, str]:
    """The trade we accept, in machine-readable form (used by reports and grants)."""
    return {
        "architecture": "centralized verification",
        "accepted_risk": "single point of failure in the gate",
        "mitigation": "tests + --demo dry run + bundle sha256sum -c",
        "rejected_alternative": "distributed judgment by language models",
        "rejected_because": "propagates errors undetected (arXiv:2512.08296) and "
        "averages expert with non-expert (arXiv:2602.01011, up to -41.1%)",
        "evidence": "PNAS 123(47) 2026 doi:10.1073/pnas.2612825123; arXiv:2512.08296; "
        "arXiv:2310.01798; arXiv:2602.01011",
        "date": "2026-11-19",
    }


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    directory = argv[0] if argv else None
    problems = check_all(directory)
    if problems:
        print("R2 INVARIANT VIOLATED — a model or network dependency entered the gate:")
        for p in problems:
            print("  -", p)
        return 1
    print(
        "R2 invariant holds: "
        f"{len(GATE_MODULES)} gate modules are model-free and network-free; "
        f"{len(TOOL_MODULES)} tool modules are model-free."
    )
    risk = accepted_failure_mode()
    print(f"accepted risk: {risk['accepted_risk']} (mitigation: {risk['mitigation']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
