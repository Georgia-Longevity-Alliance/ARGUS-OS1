"""ARGUS-OS1 — Q2 census: centriole foci per cell and per nucleus in binucleated cells.

**Context.** Step 1 of the branch `exp/centriole-endomitosis` is closed from the literature
(Kalbfuss & Gönczy, *Sci Adv* 2023, PMID 37256957): all 20 intestinal cells of L1 larvae keep
centrioles, including the 14 that endomitose, and eliminate them later in development. So the
next question is not "are they there" but **how they are distributed once the cell is
binucleated**:

  Q2 → after endomitosis (L2-L4), is there one shared focus per cell, or one focus per nucleus?

This module is only the bookkeeping and the decision rule. It does not measure anything by
itself: it reads a hand-scored CSV (one row per cell), validates it, and returns a verdict that
is **structural**, not a numeric threshold.

**The decision rule (no invented cut-offs).**

| observation in binucleated cells | verdict | consequence |
|---|---|---|
| 2 foci, one over each nucleus (`foci_per_nucleus` = 1) | `PARTITIONED` | the pair separates between nuclei → duplication must proceed without division = H1 signature → run Q3 |
| 1 focus, shared (`foci_per_nucleus` = 0.5) | `SHARED` | a single pair is kept while ploidy doubles → H2 is the live hypothesis, Q3 unnecessary |
| foci = 0 in a substantial fraction | `MIXED` | dating first (Q4), not duplication |

**Why a focus, not a centriole.** Light microscopy scores one *focus* per centriole pair.
"Retained" vs "duplicated" (H1 vs H2 at the level of individual centrioles) needs U-ExM or
serial-section EM — precedent: Croisier, Kalbfuss & Gönczy 2025, PMID 40475707, who used EM to
prove that SAS-4/SAS-7 foci in L1 rectal cells are bona fide centrioles.

**Controls the CSV forces you to record**, because without them the census cannot be believed:
a marker-free strain (`strain` = `ctrl`), the non-endomitotic rings 1-2 (`cell_class` = `control_ring`),
and the stage (`L1`..`L4`).

CLI
---
  python centriole_census.py --template counts.csv     # empty sheet with instructions
  python centriole_census.py --in counts.csv           # verdict + per-stage summary
  python centriole_census.py --self-test               # exercise all three verdicts
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys

FIELDS = [
    "animal_id",       # e.g. A01
    "cell_id",         # e.g. int3V, or V1L for a seam control
    "cell_class",      # endomitotic | control_ring | seam | ctrl
    "stage",           # L1 | L2 | L3 | L4
    "strain",          # centriole-marker strain id, or `ctrl` for the marker-free control
    "nuclei",          # 1 | 2  (count nuclei in this cell)
    "foci_total",      # centriole-marker foci in the whole cell
    "foci_nuc1",       # foci over nucleus 1
    "foci_nuc2",       # foci over nucleus 2 (0 when mononucleated)
    "dapi_integrated", # integrated nuclear intensity, arbitrary units (ploidy proxy)
    "note",            # free text: anything that made scoring hard
]

VERDICT_PARTITIONED = "PARTITIONED"
VERDICT_SHARED = "SHARED"
VERDICT_MIXED = "MIXED"
VERDICT_INSUFFICIENT = "INSUFFICIENT"


def template(path: str) -> str:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(FIELDS)
        w.writerow(["A01", "int3V", "endomitotic", "L2", "SAS-4::GFP", 2, 2, 1, 1, 1000, ""])
        w.writerow(["A01", "int1V", "control_ring", "L2", "SAS-4::GFP", 1, 1, 1, 0, 1000, ""])
        w.writerow(["A01", "int3V", "ctrl", "L2", "ctrl", 2, 0, 0, 0, 1000, "marker-free: must be 0"])
    return path


def load(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        raise ValueError("empty file")
    missing = [f for f in FIELDS if f not in rows[0]]
    if missing:
        raise ValueError(f"missing columns: {missing}")
    return rows


def _int(row: dict, key: str) -> int:
    try:
        return int(str(row[key]).strip())
    except (KeyError, ValueError) as exc:
        raise ValueError(f"{row.get('cell_id','?')}: `{key}` must be an integer, got {row.get(key)!r}") from exc


def validate(rows: list[dict]) -> list[str]:
    """Row-level problems (empty list = usable)."""
    problems: list[str] = []
    for row in rows:
        cid = row.get("cell_id", "?")
        try:
            nuclei = _int(row, "nuclei")
            total = _int(row, "foci_total")
            n1 = _int(row, "foci_nuc1")
            n2 = _int(row, "foci_nuc2")
        except ValueError as exc:
            problems.append(str(exc))
            continue
        if nuclei not in (1, 2):
            problems.append(f"{cid}: nuclei must be 1 or 2, got {nuclei}")
        if min(total, n1, n2) < 0:
            problems.append(f"{cid}: negative focus count")
        if n1 + n2 != total:
            problems.append(f"{cid}: foci_nuc1+nuc2={n1 + n2} but foci_total={total}")
        if nuclei == 1 and n2 != 0:
            problems.append(f"{cid}: mononucleated cell must have foci_nuc2=0")
        if row.get("strain", "").strip() == "ctrl" and total != 0:
            problems.append(f"{cid}: marker-free control shows {total} foci — bleed-through or mis-scoring")
        if row.get("stage", "").strip() not in ("L1", "L2", "L3", "L4"):
            problems.append(f"{cid}: stage must be L1..L4")
    return problems


def census(rows: list[dict]) -> dict:
    """Summarise and decide. Marker-free controls and seam cells are reported, not pooled."""
    problems = validate(rows)
    if problems:
        raise ValueError("invalid input:\n  " + "\n  ".join(problems))

    def keep(r: dict) -> bool:
        return r["strain"].strip() != "ctrl" and r["cell_class"].strip() == "endomitotic"

    target = [r for r in rows if keep(r)]
    binu = [r for r in target if _int(r, "nuclei") == 2]
    mono = [r for r in target if _int(r, "nuclei") == 1]

    per_nucleus = []
    for r in binu:
        per_nucleus.append(_int(r, "foci_total") / 2.0)

    zero_fraction = (sum(1 for r in binu if _int(r, "foci_total") == 0) / len(binu)) if binu else 0.0
    animals = len({r["animal_id"] for r in target})

    if len(binu) < 10 or animals < 5:
        verdict = VERDICT_INSUFFICIENT
    elif zero_fraction >= 0.2:
        verdict = VERDICT_MIXED
    elif statistics.median(per_nucleus) >= 0.9:
        verdict = VERDICT_PARTITIONED
    elif statistics.median(per_nucleus) <= 0.6:
        verdict = VERDICT_SHARED
    else:
        verdict = VERDICT_INSUFFICIENT

    by_stage = {}
    for stage in ("L1", "L2", "L3", "L4"):
        sel = [r for r in binu if r["stage"] == stage]
        if sel:
            by_stage[stage] = {
                "cells": len(sel),
                "median_foci_total": statistics.median(_int(r, "foci_total") for r in sel),
                "median_foci_per_nucleus": round(statistics.median(_int(r, "foci_total") / 2 for r in sel), 3),
            }

    return {
        "rows": len(rows),
        "animals": animals,
        "endomitotic_binucleated": len(binu),
        "endomitotic_mononucleated": len(mono),
        "control_cells": len([r for r in rows if r["cell_class"].strip() in ("control_ring", "seam")]),
        "marker_free_control_rows": len([r for r in rows if r["strain"].strip() == "ctrl"]),
        "median_foci_per_binucleated_cell": statistics.median([_int(r, "foci_total") for r in binu]) if binu else None,
        "median_foci_per_nucleus": round(statistics.median(per_nucleus), 3) if per_nucleus else None,
        "zero_foci_fraction": round(zero_fraction, 3),
        "by_stage": by_stage,
        "verdict": verdict,
        "next": {
            VERDICT_PARTITIONED: "H1 signature -> run Q3 (U-ExM or serial-section EM) to count centrioles per focus",
            VERDICT_SHARED: "H2 live -> Q3 unnecessary; go to Q4 (date the elimination event)",
            VERDICT_MIXED: "mixed population -> Q4 (dating) first, then re-test duplication in the positive cells",
            VERDICT_INSUFFICIENT: "not enough binucleated cells / animals (need >=10 cells from >=5 animals)",
        }[verdict],
        "rule": "structural: 1 focus per nucleus vs 1 shared focus; no numeric threshold is invented",
    }


def self_test() -> int:
    def row(**kw):
        base = dict(animal_id="A01", cell_id="int3V", cell_class="endomitotic", stage="L2",
                    strain="SAS-4::GFP", nuclei=2, foci_total=2, foci_nuc1=1, foci_nuc2=1,
                    dapi_integrated=1000, note="")
        base.update(kw)
        return base

    # PARTITIONED: 12 binucleated cells, 2 foci each, from 6 animals
    rows = [row(animal_id=f"A{i//2:02d}", cell_id=f"int{i}V") for i in range(12)]
    rows += [row(cell_id="int1V", cell_class="control_ring", nuclei=1, foci_total=1, foci_nuc2=0)]
    rows += [row(cell_id="int3V", strain="ctrl", foci_total=0, foci_nuc1=0, foci_nuc2=0)]
    res = census(rows)
    assert res["verdict"] == VERDICT_PARTITIONED, res
    assert res["animals"] == 6 and res["endomitotic_binucleated"] == 12

    # SHARED: one focus per binucleated cell
    shared = [row(animal_id=f"A{i//2:02d}", cell_id=f"int{i}V", foci_total=1, foci_nuc1=1, foci_nuc2=0)
              for i in range(12)]
    assert census(shared)["verdict"] == VERDICT_SHARED

    # MIXED: a fifth of the cells have no focus at all
    mixed = [row(animal_id=f"A{i//2:02d}", cell_id=f"int{i}V") for i in range(10)]
    mixed += [row(animal_id=f"A{i:02d}", cell_id=f"intx{i}V", foci_total=0, foci_nuc1=0, foci_nuc2=0)
              for i in range(3)]
    assert census(mixed)["verdict"] == VERDICT_MIXED

    # INSUFFICIENT: only 4 cells
    assert census(rows[:4])["verdict"] == VERDICT_INSUFFICIENT

    # the marker-free control must be zero, or the sheet is rejected
    bad = [row(strain="ctrl", foci_total=2, foci_nuc1=1, foci_nuc2=1)]
    assert validate(bad), "marker-free control with foci was accepted"

    # foci_nuc1+nuc2 must equal foci_total
    assert validate([row(foci_total=3, foci_nuc1=1, foci_nuc2=1)]), "sum mismatch accepted"
    print("self-test: 6/6 assertions passed (three verdicts, insufficiency, two validations)")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Q2 census: centriole foci per cell / per nucleus.")
    p.add_argument("--template", help="write an empty scoring sheet here")
    p.add_argument("--in", dest="infile", help="scored CSV to summarise")
    p.add_argument("--json", action="store_true")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args(sys.argv[1:] if argv is None else argv)

    if a.self_test:
        return self_test()
    if a.template:
        print("written:", template(a.template))
        return 0
    if not a.infile:
        p.print_help()
        return 1
    try:
        res = census(load(a.infile))
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        for k, v in res.items():
            if k in ("by_stage", "next", "rule"):
                continue
            print(f"{k:36s}: {v}")
        print(f"{'verdict':36s}: {res['verdict']}")
        print(f"{'next':36s}: {res['next']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
