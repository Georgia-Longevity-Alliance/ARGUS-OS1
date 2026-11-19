"""ARGUS-OS1 — verification of the tile pipeline against a known phantom.

Metrics
-------
* PSNR / SSIM vs ground truth mosaic
* sharpness (variance of Laplacian) vs the ground truth -> "did fusion keep detail?"
* seam score: mean |dI/dx| on tile borders divided by the global mean |dI/dx|
  (1.0 = invisible seams)
* registration error vs the phantom's true positions

Usage:  python3 evaluate.py /tmp/argus_phantom [--json report.json]
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blend import blend  # noqa: E402
from tiles import load_tiles, register, to_gray  # noqa: E402


def sharpness(img: np.ndarray) -> float:
    g = to_gray(img) * 255.0
    return float(cv2.Laplacian(g.astype(np.float32), cv2.CV_32F, ksize=3).var())


def psnr(a: np.ndarray, b: np.ndarray) -> float:
    mse = float(np.mean((a.astype(np.float32) - b.astype(np.float32)) ** 2))
    return float("inf") if mse == 0 else float(10 * np.log10(1.0 / mse))


def seam_score(img: np.ndarray, borders_x: list[int], borders_y: list[int], band: int = 2) -> float:
    g = to_gray(img).astype(np.float32)
    dx = np.abs(np.diff(g, axis=1)).mean()
    dy = np.abs(np.diff(g, axis=0)).mean()
    vals = []
    for x in borders_x:
        x = min(max(x, band), g.shape[1] - band - 1)
        vals.append(np.abs(np.diff(g[:, x - band:x + band + 1], axis=1)).mean())
    for y in borders_y:
        y = min(max(y, band), g.shape[0] - band - 1)
        vals.append(np.abs(np.diff(g[y - band:y + band + 1, :], axis=0)).mean())
    ref = 0.5 * (dx + dy)
    return float(np.mean(vals) / max(ref, 1e-9))


def run(phantom_dir: str, verbose: bool = True) -> dict:
    with open(os.path.join(phantom_dir, "_phantom.json"), encoding="utf-8") as fh:
        meta = json.load(fh)
    gt = cv2.imread(os.path.join(phantom_dir, "_ground_truth.png"), cv2.IMREAD_UNCHANGED)
    gt = gt.astype(np.float32) / 255.0
    truth = {f["img"]: np.array([f["x"], f["y"]], float) for f in meta["fields"]}

    tiles = load_tiles(phantom_dir)
    reg = register(tiles)
    true_pos = np.array([truth[os.path.basename(t.path)] for t in tiles], float)
    reg_err = np.abs(np.asarray([t.pos for t in tiles], float) - true_pos)

    results: dict = {
        "tiles": len(tiles),
        "registration": reg.summary(),
        "reg_error_median_px": float(np.median(np.abs(reg_err - np.median(reg_err)))),
        "reg_error_max_px": float(reg_err.max()),
    }

    out = {}
    for mode in ("hard", "feather", "fusion"):
        img = blend(tiles, mode=mode, overlap=meta["overlap"], progress=False)
        H = min(img.shape[0], gt.shape[0])
        W = min(img.shape[1], gt.shape[1])
        a, b = img[:H, :W], gt[:H, :W]
        bx = sorted({int(t.pos[0]) for t in tiles} | {int(t.pos[0] + t.w) for t in tiles})
        by = sorted({int(t.pos[1]) for t in tiles} | {int(t.pos[1] + t.h) for t in tiles})
        out[mode] = {
            "psnr_db": round(psnr(a, b), 2),
            "ssim": round(float(ssim(b, a, channel_axis=2, data_range=1.0)), 4),
            "sharpness": round(sharpness(img), 1),
            "seam_score": round(seam_score(img, bx, by), 3),
        }
    out["ground_truth"] = {"sharpness": round(sharpness(gt), 1), "seam_score": 1.0}
    results["modes"] = out

    if verbose:
        print(f"tiles: {results['tiles']}  reg: {results['registration']}")
        print(f"registration error: median |dev| {results['reg_error_median_px']:.2f} px, "
              f"max {results['reg_error_max_px']:.2f} px")
        print(f"{'mode':<10}{'PSNR dB':>9}{'SSIM':>8}{'sharp':>9}{'seam':>7}")
        for mode in ("hard", "feather", "fusion"):
            m = out[mode]
            print(f"{mode:<10}{m['psnr_db']:>9}{m['ssim']:>8}{m['sharpness']:>9}{m['seam_score']:>7}")
        print(f"{'GT':<10}{'--':>9}{'--':>8}{out['ground_truth']['sharpness']:>9}{1.0:>7}")
    return results


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("phantom_dir")
    ap.add_argument("--json", default=None)
    a = ap.parse_args(argv)
    res = run(a.phantom_dir)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1)
        print("json ->", a.json)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
