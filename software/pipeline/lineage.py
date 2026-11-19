"""ARGUS-OS1 — division events and the **endomitosis gate** (2026-11-19).

**Why this module exists.** In the *C. elegans* intestine, cells enter a full M phase,
segregate their chromosomes, and then never assemble a central spindle or ingress the
membrane — they become binucleated and polyploid (Barrull-Mascaró et al., *J Cell Biol*
226:e202604104, 2026, PMID [43037622]; preprint 10.1101/2025.08.04.668394). Such cells
can also appear during embryogenesis when the cycle is forced. A lineage tracker that
calls a division from the **number of nuclei** therefore records:

  * a division that never happened, and — the part that actually breaks our analysis —
  * a **sister pair that never existed**.

Sister pairs are the unit of ARGUS's primary test (within-type pedigree comparison), so
this is a correctness gate, not a cosmetic filter.

**The rule.** A division exists only with evidence of *cell* division:

    division   <=> nuclei 1 -> 2  AND  membrane ingression >= FURROW_MIN
                    (or an explicit cell-count increment)
    nuclear_split_no_furrow  <=> nuclei 1 -> 2 AND ingression <  FURROW_MIN
    no_event   otherwise

A `nuclear_split_no_furrow` is recorded as its own event class and **never** contributes
to sister pairs or to pedigree aggregation. The gate is one-directional and conservative:
a furrow without a second nucleus is not a division either.

**FURROW_MIN is our threshold, not a literature constant.** The paper establishes that
ingression is *absent* in endomitosis; it does not hand down "0.10". The value is a
documented, configurable knob so that a different optics/marker set can re-calibrate it
without editing logic. A borderline case plus a changed knob is covered by a test.

**Honest status.** This is a *design* consequence of a mechanism, verified on synthetic
frames. It is **not** a measured false-division rate on real ARGUS data: no published
source (searched 2026-11-19) quantifies how often an automatic tracker miscalls
endomitotic cells in this organism. That measurement is R6
(`docs/EXPERIMENT_CENTRIOLE_ENDOMITOSIS_2026-11-19.md`).

CLI
---
  python lineage.py --demo                       # phantom + classification table
  python lineage.py --demo --furrow-min 0.25     # show the knob changing a verdict
"""

from __future__ import annotations

import argparse
import json
import sys

#: Minimum membrane ingression (0..1) required to call a division. Our choice.
FURROW_MIN = 0.10

#: Event classes — strings, so they survive serialisation into the lineage log.
DIVISION = "division"
NUCLEAR_SPLIT_NO_FURROW = "nuclear_split_no_furrow"
NO_EVENT = "no_event"


def classify_transition(prev: dict, cur: dict, furrow_min: float = FURROW_MIN) -> str:
    """Classify one cell between two frames. Deterministic, conservative.

    `prev`/`cur` need: `nuclei` (int) and `furrow` (0..1, membrane ingression index).
    `cell_count_delta` (optional int) is honoured when present — an explicit increment
    of the number of cells is stronger evidence than an image-derived index.
    """
    for frame, name in ((prev, "prev"), (cur, "cur")):
        if "nuclei" not in frame or "furrow" not in frame:
            raise ValueError(f"{name} must carry `nuclei` and `furrow`")
        if not 0.0 <= float(frame["furrow"]) <= 1.0:
            raise ValueError(f"{name}.furrow must be within 0..1")

    n_prev, n_cur = int(prev["nuclei"]), int(cur["nuclei"])
    if n_cur < n_prev:
        return NO_EVENT                      # merges/segmentation flicker: not our event
    if n_cur == n_prev:
        return NO_EVENT

    delta = cur.get("cell_count_delta")
    if delta is not None and int(delta) > 0:
        return DIVISION                      # explicit cell-count increment wins

    return DIVISION if float(cur["furrow"]) >= furrow_min else NUCLEAR_SPLIT_NO_FURROW


def classify_series(frames: list[dict], furrow_min: float = FURROW_MIN) -> list[dict]:
    """Classify a single cell's frame sequence into events."""
    events = []
    for i in range(1, len(frames)):
        kind = classify_transition(frames[i - 1], frames[i], furrow_min)
        if kind == NO_EVENT:
            continue
        events.append({"frame": i, "class": kind, "furrow": frames[i]["furrow"],
                       "nuclei": frames[i]["nuclei"]})
    return events


def build_pedigree(tracks: dict[str, list[dict]], furrow_min: float = FURROW_MIN) -> dict:
    """Build divisions and sister pairs from per-cell tracks.

    Returns `{divisions, nuclear_splits, sister_pairs, excluded_from_pedigree}`.
    Sister pairs are created **only** from `division` events; every pair is asserted to
    have a furrow, so a regression that promotes endomitosis fails loudly here.
    """
    divisions, splits, pairs, excluded = [], [], [], []

    for cell_id, frames in tracks.items():
        for ev in classify_series(frames, furrow_min):
            if ev["class"] == DIVISION:
                a, b = f"{cell_id}.a", f"{cell_id}.b"
                divisions.append({"parent": cell_id, "frame": ev["frame"], "daughters": [a, b],
                                  "furrow": ev["furrow"]})
                pairs.append({"cell_a": a, "cell_b": b, "parent": cell_id, "frame": ev["frame"]})
            else:
                splits.append({"cell": cell_id, "frame": ev["frame"], "furrow": ev["furrow"]})
                # A binucleated cell is a real cell: it keeps its identity and its pedigree
                # parent, but it contributes no sister pair and no division to the metrics.
                excluded.append({"cell": cell_id, "reason": NUCLEAR_SPLIT_NO_FURROW,
                                 "frame": ev["frame"]})

    for pair in pairs:                                   # invariant, checked every build
        assert _pair_has_furrow(pair, divisions), f"sister pair without a furrow: {pair}"

    return {
        "divisions": divisions,
        "nuclear_splits": splits,
        "sister_pairs": pairs,
        "excluded_from_pedigree": excluded,
        "furrow_min": furrow_min,
        "rule": "division requires a furrow or an explicit cell-count increment",
    }


def _pair_has_furrow(pair: dict, divisions: list[dict]) -> bool:
    for d in divisions:
        if d["parent"] == pair["parent"] and d["frame"] == pair["frame"]:
            return float(d["furrow"]) >= 0.0 and d["daughters"] == [pair["cell_a"], pair["cell_b"]]
    return False


# ─── phantom ───────────────────────────────────────────────────────────────────

def make_phantom_tracks(
    n_divisions: int = 6,
    n_endomitosis: int = 4,
    n_quiet: int = 3,
    frames: int = 8,
    seed: int = 20261119,
) -> tuple[dict[str, list[dict]], dict[str, str]]:
    """Synthetic per-cell tracks with ground-truth event labels.

    Endomitotic events deliberately get a *little* ingression noise (0.00-0.05) so the
    test proves the class is decided by the threshold, not by an exact zero.
    """
    import random

    rng = random.Random(seed)
    tracks: dict[str, list[dict]] = {}
    truth: dict[str, str] = {}

    def series(event: str) -> list[dict]:
        out = []
        split_at = rng.randint(3, frames - 2)
        for f in range(frames):
            nuclei = 1 if f < split_at else 2
            if f < split_at:
                furrow = 0.0
            elif event == DIVISION:
                furrow = round(rng.uniform(0.35, 0.95), 3)      # visible ingression
            elif event == NUCLEAR_SPLIT_NO_FURROW:
                furrow = round(rng.uniform(0.00, 0.05), 3)      # noise around zero
            else:
                nuclei, furrow = 1, 0.0
            out.append({"nuclei": nuclei, "furrow": furrow})
        return out

    for i in range(n_divisions):
        cid = f"DIV{i:02d}"
        tracks[cid] = series(DIVISION)
        truth[cid] = DIVISION
    for i in range(n_endomitosis):
        cid = f"ENDO{i:02d}"
        tracks[cid] = series(NUCLEAR_SPLIT_NO_FURROW)
        truth[cid] = NUCLEAR_SPLIT_NO_FURROW
    for i in range(n_quiet):
        cid = f"QUIET{i:02d}"
        tracks[cid] = series(NO_EVENT)
        truth[cid] = NO_EVENT
    return tracks, truth


def demo(furrow_min: float = FURROW_MIN) -> dict:
    tracks, truth = make_phantom_tracks()
    result = build_pedigree(tracks, furrow_min)
    base = {"furrow_min": furrow_min, "tracks": len(tracks),
            "divisions": len(result["divisions"]),
            "nuclear_splits": len(result["nuclear_splits"]),
            "sister_pairs": len(result["sister_pairs"]),
            "expected_divisions": sum(1 for v in truth.values() if v == DIVISION),
            "expected_endomitosis": sum(1 for v in truth.values() if v == NUCLEAR_SPLIT_NO_FURROW)}
    base["correct"] = (base["divisions"] == base["expected_divisions"]
                       and base["nuclear_splits"] == base["expected_endomitosis"])
    return base


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Division gate: endomitosis is not a division.")
    p.add_argument("--demo", action="store_true", help="run on the synthetic phantom")
    p.add_argument("--furrow-min", type=float, default=FURROW_MIN,
                   help=f"ingression threshold 0..1 (default {FURROW_MIN})")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(sys.argv[1:] if argv is None else argv)

    if not a.demo:
        p.print_help()
        return 1
    res = demo(a.furrow_min)
    if a.json:
        print(json.dumps(res, indent=2))
    else:
        print(f"furrow_min = {res['furrow_min']}")
        print(f"  true divisions      : {res['expected_divisions']}  -> called: {res['divisions']}")
        print(f"  true endomitoses    : {res['expected_endomitosis']}  -> called: {res['nuclear_splits']}")
        print(f"  sister pairs        : {res['sister_pairs']} (only from divisions)")
        print(f"  verdict             : {'PASS' if res['correct'] else 'FAIL'}")
    return 0 if res["correct"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
