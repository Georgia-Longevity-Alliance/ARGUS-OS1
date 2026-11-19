"""ARGUS-OS1 — measure the usable travel (range of motion) of a stage.

Method follows the peer-reviewed low-cost approach for the OpenFlexure
(Chisholm et al. 2026, doi:10.1111/jmi.70192): image the same field while
stepping the stage, and recover the displacement from image correlation instead
of trusting a calibrated stage. Our registration is strip-based (see tiles.py)
because the per-frame step is large relative to the field.

Input is a directory of frames captured during a slow traverse of one axis
(`--axis x|y`). Output: measured travel in µm and mm, per-link match scores, and
the measured step per frame — which converts stage steps to µm and therefore
also calibrates the stage for scan planning.

Usage:
  python3 measure_rom.py FRAMES_DIR --mpp-um 0.0388 --axis x [--step-um 50]
"""

from __future__ import annotations

import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tiles import load_tiles, strip_match  # noqa: E402


def measure(frames_dir: str, mpp_um: float, axis: str = "x", min_score: float = 0.30) -> dict:
    tiles = load_tiles(frames_dir)
    if len(tiles) < 3:
        raise ValueError("need at least 3 frames of a traverse")
    ax = 0 if axis == "x" else 1
    steps, scores = [], []
    total = 0.0
    for prev, cur in zip(tiles[:-1], tiles[1:]):
        shift, score, edge = strip_match(prev.image, cur.image)
        scores.append(score)
        if score < min_score:
            continue
        step = abs(float(shift[ax]))
        if step < 1e-9:
            continue
        steps.append(step)
        total += step
    if not steps:
        raise RuntimeError("no reliable frame-to-frame links — traverse too coarse or no texture")
    field_um = (tiles[0].w if axis == "x" else tiles[0].h) * mpp_um
    return {
        "frames": len(tiles),
        "axis": axis,
        "links_used": len(steps),
        "links_total": len(scores),
        "median_score": round(float(np.median(scores)), 3),
        "min_score": round(float(min(scores)), 3),
        "field_um": round(field_um, 1),
        "median_step_px": round(float(np.median(steps)), 2),
        "median_step_um": round(float(np.median(steps)) * mpp_um, 2),
        "measured_travel_um": round(total * mpp_um, 1),
        "measured_travel_mm": round(total * mpp_um / 1000.0, 3),
        "travel_in_fields": round(float(total) / (tiles[0].w if axis == "x" else tiles[0].h), 2),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("frames_dir")
    ap.add_argument("--mpp-um", type=float, required=True)
    ap.add_argument("--axis", default="x", choices=["x", "y"])
    ap.add_argument("--step-um", type=float, default=None,
                    help="commanded step per frame, to print the measured/commanded ratio")
    a = ap.parse_args(argv)
    res = measure(a.frames_dir, a.mpp_um, a.axis)
    for k, v in res.items():
        print(f"{k:>18}: {v}")
    if a.step_um:
        ratio = res["median_step_um"] / a.step_um
        print(f"{'measured/commanded':>18}: {ratio:.4f}  "
              f"(commanded {a.step_um} µm/frame -> measured {res['median_step_um']} µm/frame)")
        print(f"{'frame count for 10 mm':>18}: {10000.0 / res['median_step_um']:.0f} frames "
              f"at this step; travel limit {res['measured_travel_mm']} mm")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
