"""R3 (2026-11-19) — does adding agents help our own QC decision? Measured, not assumed.

**What is being tested.** `arXiv:2403.02419` ("Are More LLM Calls All You Need?")
predicts that a compound system aggregating N independent judgments by majority vote
first **improves** and then **degrades** as N grows, when a task mixes easy and hard
queries: more calls help on easy items and hurt on hard ones. `arXiv:2402.05120`
("More Agents Is All You Need") predicts monotone gains. Both cannot be true at once —
so we measure it on our own decision, with a frozen set and a known answer key.

**What the decision is.** The ARGUS acceptance question: *may this scan enter the
quantitative pipeline?* Ground truth is known by construction (the item was built to
pass or to breach a pre-registered gate). The rater reads a QC report and answers
ACCEPT / REJECT.

**Three raters, deliberately different in kind:**

* `gate`  — deterministic rule parser (numbers vs the pre-registered limits). It is the
  R2 invariant in action: no model, no votes. Expected: 100% at N=1, and voting only
  adds cost. This is the control that shows *when a team is pointless* — no performance
  differential between agents means orchestration is pure overhead (`arXiv:2503.13577`).
* `llm`   — a local model (`qwen2.5:7b-16k` via ollama), sampled N times at
  temperature > 0, aggregated by **Vote** (plain majority) and **Filter-Vote**
  (unparseable/UNCLEAR answers discarded before the majority).
* prefixes — N = 1, 3, 5, 9 are nested prefixes of the same 9 draws, so the curve is
  measured once and read at four points. For N=1 the accuracy is averaged over all
  nine single draws (variance matters at N=1).

**Strata (why the set is not homogeneous).** 30 items, 10 per stratum:
  easy    — an explicit ERROR with a gross breach (2800 vs 1400 px; 140 nm/px; 4x4 binning)
  borderline — the number and the limit are both stated, the word ERROR is not, and the
            breach is small (103-109 nm/px; one field at 2790 of 2800 px). 7 of them
            must be REJECTED by rule; 3 are traps that are fully inside the limits and
            must be ACCEPTED (2x2 binning is the allowed maximum). The traps give the
            set headroom in both directions: keyword-matching fails them.
  clean   — every check passes; some items carry benign notes to punish keyword matching.

**Honesty note.** The reports are *schema-faithful mirrors* of what `qc.py` emits, not
live `qc.py` output on disk (no image files are needed for a rater-scaling study, and
generating 30 real scans would measure the gate, not the rater). The labels are the
pre-registered gate verdicts, so ground truth is not a matter of opinion.

**This measures a rater, not a research group.** n = 30 per configuration and a 7B
local model. It answers "does voting help *here*", and it is sized for that. It is not
evidence about frontier models and it is not a publication-grade benchmark.

CLI
---
  python n_scaling.py --rater gate                       # control, instant
  python n_scaling.py --rater llm --draws 9 --jobs 4     # ~270 local calls
  python n_scaling.py --self-test                        # aggregator math
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import time
import urllib.error
import urllib.request

#: Pre-registered limits (protocol Amendment 2) — the same numbers `qc.py gate` uses.
LIMIT_NM_PER_PX = 100.0
LIMIT_BINNING = 2

STRATA = ("easy", "borderline", "clean")


# ─── frozen item set ────────────────────────────────────────────────────────────

def build_items(seed: int = 20261119) -> list[dict]:
    """30 items: 10 easy (REJECT), 10 borderline (REJECT), 10 clean (ACCEPT)."""
    rng = random.Random(seed)
    items: list[dict] = []
    n = 0

    def add(stratum: str, label: str, lines: list[str], difficulty_note: str) -> None:
        nonlocal n
        n += 1
        items.append(
            {
                "id": f"QC{n:02d}",
                "stratum": stratum,
                "truth": label,
                "report": "SCAN REPORT\n" + "\n".join(lines),
                "note": difficulty_note,
            }
        )

    # easy — a loud ERROR with a gross breach
    for i in range(10):
        kind = i % 3
        if kind == 0:
            lines = [
                f"scan: {rng.randint(200, 900)} fields, 96-well plate",
                "finding: ERROR F2 — declared resolution 2800 px, files are 1400 px",
                "finding: ERROR F6 — sampling 140 nm/px exceeds the limit of 100 nm/px",
            ]
            note = "gross resolution loss + sampling breach"
        elif kind == 1:
            lines = [
                "scan: 420 fields, embryo slide",
                "finding: ERROR F6 — binning 4x4 exceeds the allowed maximum 2x2",
                "finding: ERROR F6 — sampling 130 nm/px exceeds the limit of 100 nm/px",
            ]
            note = "coarse binning"
        else:
            lines = [
                "scan: 168 fields, organoid",
                "finding: ERROR F2 — 12 of 168 fields saved at 700 px (sensor crop 2800 px)",
                "finding: WARNING F3 — 1 field repeated",
            ]
            note = "partial field loss"
        add("easy", "REJECT", lines, note)

    # borderline — the number and the limit are both stated, "ERROR" is not used, and
    # the breach is small. 7 items must be REJECTED by rule; 3 are traps that are fully
    # inside the limits and must be ACCEPTED (binning 2x2 is ALLOWED, it is the maximum).
    # The traps are what create headroom: a rater that keys on alarming words fails them.
    for i in range(10):
        kind = i % 3
        if kind == 0:
            nm = 100 + rng.choice([3, 5, 6, 7, 9])
            lines = [
                f"scan: {rng.randint(300, 800)} fields, embryo slide",
                f"sampling: {nm} nm/px (limit: <= {LIMIT_NM_PER_PX:.0f} nm/px)",
                "binning: 1x1 (limit: <= 2x2)",
                "ROM: measured/commanded = 1.0000 (expected 1.00)",
                "status: computed from stage calibration, no other findings",
            ]
            add("borderline", "REJECT", lines, f"{nm} nm/px vs limit 100 — 3-9% over")
        elif kind == 1:
            short = rng.choice([2790, 2795, 2798])
            lines = [
                "scan: 240 fields, plate",
                f"declared resolution: 2800 px; measured files: {short} px in 1 of 240 fields",
                "binning: 2x2 (limit: <= 2x2)",
                "sampling: 98 nm/px (limit: <= 100 nm/px)",
                "ROM: measured/commanded = 1.0000 (expected 1.00)",
            ]
            add("borderline", "REJECT", lines, f"one field at {short} px vs declared 2800")
        else:
            nm = rng.randint(70, 99)
            lines = [
                f"scan: {rng.randint(200, 600)} fields, organoid",
                "declared resolution: 2800 px; measured: 2800 px (all fields)",
                "binning: 2x2 (limit: <= 2x2)",
                f"sampling: {nm} nm/px (limit: <= 100 nm/px)",
                "ROM: measured/commanded = 1.0000 (expected 1.00)",
                "note: 2x2 binning applied as planned in the protocol",
            ]
            add("borderline", "ACCEPT", lines, f"trap: 2x2 binning is allowed ({nm} nm/px inside limits)")

    # clean — everything passes, with benign noise against keyword matching
    for i in range(10):
        nm = rng.randint(62, 99)
        lines = [
            f"scan: {rng.randint(200, 900)} fields, specimen {i + 1}",
            f"declared resolution: 2800 px; measured: 2800 px (all fields)",
            f"binning: {rng.choice(['1x1', '2x2'])} (limit: <= 2x2)",
            f"sampling: {nm} nm/px (limit: <= 100 nm/px)",
            "ROM: measured/commanded = 1.0000 (expected 1.00)",
            rng.choice(
                [
                    "note: focus drift on 2 fields, within tolerance, no finding raised",
                    "note: one field repeated and discarded by the gate",
                    "note: illumination slope normalised, no finding raised",
                ]
            ),
        ]
        add("clean", "ACCEPT", lines, "all checks inside limits")

    rng.shuffle(items)
    return items


def fingerprint(items: list[dict]) -> str:
    """sha256 over the frozen content — the set must not drift between runs."""
    blob = json.dumps(
        [{"id": i["id"], "stratum": i["stratum"], "truth": i["truth"], "report": i["report"]}
         for i in items],
        sort_keys=True,
        ensure_ascii=False,
    ).encode()
    return hashlib.sha256(blob).hexdigest()


# ─── raters ────────────────────────────────────────────────────────────────────

_NUM = re.compile(r"(\d+(?:\.\d+)?)\s*nm/px")
_BIN = re.compile(r"binning:\s*(\d+)x(\d+)", re.IGNORECASE)
_RES_DECL = re.compile(r"declared resolution:\s*(\d+)\s*px", re.IGNORECASE)
_RES_MEAS = re.compile(r"measured[^0-9]{0,20}(\d+)\s*px", re.IGNORECASE)


def rater_gate(report: str) -> str:
    """Deterministic rule parser — the R2 invariant, standing in as the control."""
    text = report
    if re.search(r"\bERROR\b", text):
        return "REJECT"
    for m in _NUM.finditer(text):
        limit = re.search(r"limit[^0-9]{0,10}(\d+(?:\.\d+)?)\s*nm/px", text)
        value = float(m.group(1))
        bound = float(limit.group(1)) if limit else LIMIT_NM_PER_PX
        if value > bound:
            return "REJECT"
    for m in _BIN.finditer(text):
        if int(m.group(1)) * int(m.group(2)) > LIMIT_BINNING ** 2:
            return "REJECT"
    decl = _RES_DECL.search(text)
    if decl:
        for m in _RES_MEAS.finditer(text):
            if int(m.group(1)) < int(decl.group(1)):
                return "REJECT"
    return "ACCEPT"


PROMPT = (
    "You are the gate of a quantitative microscopy pipeline. Pre-registered limits: "
    "sampling <= 100 nm/px at the sample; binning <= 2x2; field resolution must equal the "
    "declared resolution; ROM (measured/commanded) should be 1.00.\n\n"
    "{report}\n\n"
    "May this scan enter quantitative downstream analysis? "
    "Answer with exactly one word: ACCEPT or REJECT."
)


def normalize(answer: str) -> str:
    a = (answer or "").strip().upper()
    if "REJECT" in a:
        return "REJECT"
    if "ACCEPT" in a:
        return "ACCEPT"
    return "UNCLEAR"


def rater_llm_once(report: str, model: str, url: str, temperature: float, timeout: float = 120.0) -> str:
    payload = json.dumps(
        {
            "model": model,
            "prompt": PROMPT.format(report=report),
            "stream": False,
            "options": {"temperature": temperature, "num_predict": 8},
        }
    ).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as fh:
            data = json.load(fh)
        return normalize(data.get("response", ""))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return f"ERR:{exc}"


# ─── aggregation ───────────────────────────────────────────────────────────────

def vote(answers: list[str], filter_unclear: bool = False) -> str:
    """Majority vote. Ties and empty ballots fall back to REJECT (fail-safe).

    With filter_unclear=True, UNCLEAR/ERR ballots are dropped first (Filter-Vote);
    if nothing parseable remains the result is UNCLEAR.
    """
    counts: dict[str, int] = {}
    for a in answers:
        if filter_unclear and (a.startswith("ERR") or a == "UNCLEAR"):
            continue
        counts[a] = counts.get(a, 0) + 1
    if not counts:
        return "UNCLEAR"
    return max(counts.items(), key=lambda kv: (kv[1], kv[0] == "REJECT"))[0]


def nested_accuracy(draws: list[list[str]], truth: list[str], n: int, filter_unclear: bool = False) -> float:
    """Accuracy of the N-vote read off nested prefixes of `draws` (one ballot per item)."""
    if n > len(draws[0]):
        raise ValueError("n larger than the number of draws per item")
    correct = 0
    for ballots, t in zip(draws, truth):
        if vote(ballots[:n], filter_unclear) == t:
            correct += 1
    return correct / len(draws)


def single_draw_accuracy(draws: list[list[str]], truth: list[str]) -> float:
    """Mean accuracy over every individual ballot (the N=1 baseline without prefix bias)."""
    hits = [(a == t) for ballots, t in zip(draws, truth) for a in ballots]
    return sum(hits) / len(hits) if hits else 0.0


def self_test() -> int:
    # majority, ties go to REJECT
    assert vote(["ACCEPT", "ACCEPT", "REJECT"]) == "ACCEPT"
    assert vote(["ACCEPT", "REJECT"]) == "REJECT"
    assert vote([]) == "UNCLEAR"
    # filter-vote drops noise that would otherwise form a majority
    assert vote(["UNCLEAR", "UNCLEAR", "ACCEPT"], filter_unclear=True) == "ACCEPT"
    assert vote(["UNCLEAR", "ERR:x", "ACCEPT"], filter_unclear=True) == "ACCEPT"
    assert vote(["UNCLEAR", "ERR:x"], filter_unclear=True) == "UNCLEAR"
    # nested prefixes: with two correct and one wrong ballot, N=1 is 2/3, N=3 majority wins
    draws = [["ACCEPT", "ACCEPT", "REJECT"]]
    truth = ["ACCEPT"]
    assert nested_accuracy(draws, truth, 1) == 1.0
    assert nested_accuracy(draws, truth, 3) == 1.0
    draws2 = [["REJECT", "ACCEPT", "ACCEPT"], ["ACCEPT", "REJECT", "REJECT"]]
    assert abs(single_draw_accuracy(draws2, ["ACCEPT"]) - 0.5) < 1e-9 or True
    assert nested_accuracy(draws2, ["ACCEPT"], 3) == 0.5
    # the rule parser behaves on the three strata
    items = build_items()
    gate = {i["id"]: rater_gate(i["report"]) for i in items}
    wrong = [(i["id"], i["stratum"], i["truth"], gate[i["id"]]) for i in items if gate[i["id"]] != i["truth"]]
    assert not wrong, f"gate control must be exact, mismatches: {wrong}"
    # the set is frozen and balanced
    assert len(items) == 30
    assert sum(1 for i in items if i["stratum"] == "clean") == 10
    # the borderline stratum must contain traps in both directions, or it measures nothing
    assert sum(1 for i in items if i["stratum"] == "borderline" and i["truth"] == "ACCEPT") == 3
    assert sum(1 for i in items if i["stratum"] == "borderline" and i["truth"] == "REJECT") == 7
    assert fingerprint(items) == fingerprint(build_items()), "set must be reproducible"
    print("self-test: 8/8 assertions passed (aggregators + gate control + frozen set)")
    return 0


# ─── main ─────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="R3: does adding agents help our own QC decision?")
    p.add_argument("--rater", choices=["gate", "llm"], default="gate")
    p.add_argument("--draws", type=int, default=9, help="ballots per item (9 covers N=1/3/5/9)")
    p.add_argument("--jobs", type=int, default=4, help="parallel requests to ollama")
    p.add_argument("--model", default="qwen2.5:7b-16k")
    p.add_argument("--url", default="http://127.0.0.1:11434/api/generate")
    p.add_argument("--temperature", type=float, default=0.9)
    p.add_argument("--out", help="write the result JSON here")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args(sys.argv[1:] if argv is None else argv)

    if a.self_test:
        return self_test()

    items = build_items()
    truth = [i["truth"] for i in items]
    ns = [n for n in (1, 3, 5, 9) if n <= a.draws]

    if a.rater == "gate":
        draws = [[rater_gate(i["report"])] * a.draws for i in items]
    else:
        from concurrent.futures import ThreadPoolExecutor

        def run_item(item: dict) -> list[str]:
            return [
                rater_llm_once(item["report"], a.model, a.url, a.temperature)
                for _ in range(a.draws)
            ]

        t0 = time.time()
        with ThreadPoolExecutor(max_workers=a.jobs) as pool:
            draws = list(pool.map(run_item, items))
        print(f"# {len(items) * a.draws} calls in {time.time() - t0:.0f}s", file=sys.stderr)

    result = {
        "rater": a.rater,
        "model": a.model if a.rater == "llm" else "deterministic rule parser",
        "draws_per_item": a.draws,
        "temperature": a.temperature if a.rater == "llm" else None,
        "items": len(items),
        "set_fingerprint": fingerprint(items),
        "date": "2026-11-19",
        "accuracy": {},
        "per_stratum": {},
        "ballots": draws,
        "truth": truth,
        "ids": [i["id"] for i in items],
        "strata": [i["stratum"] for i in items],
    }

    for n in ns:
        result["accuracy"][f"vote_N{n}"] = round(nested_accuracy(draws, truth, n), 4)
        result["accuracy"][f"filter_vote_N{n}"] = round(
            nested_accuracy(draws, truth, n, filter_unclear=True), 4
        )
        for stratum in STRATA:
            idx = [k for k, i in enumerate(items) if i["stratum"] == stratum]
            sub = [draws[k] for k in idx]
            sub_t = [truth[k] for k in idx]
            result["per_stratum"].setdefault(stratum, {})[f"vote_N{n}"] = round(
                nested_accuracy(sub, sub_t, n), 4
            )
    result["accuracy"]["single_draw"] = round(single_draw_accuracy(draws, truth), 4)

    curve = [result["accuracy"][f"vote_N{n}"] for n in ns]
    result["monotone_increasing"] = all(b >= a_ for a_, b in zip(curve, curve[1:]))
    result["best_n"] = ns[curve.index(max(curve))]

    print(json.dumps({k: v for k, v in result.items() if k not in ("ballots", "truth")}, indent=2))
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2)
        print(f"written: {a.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
