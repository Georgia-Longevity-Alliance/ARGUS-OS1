"""ARGUS-OS1 — parameter sweep for the blender on the phantom.

Reproducible selection of the defaults used by `blend.py` (`lf_ratio`,
`detail_power`). Selection rule: maximise PSNR against ground truth subject to
sharpness >= 90 % of the ground-truth sharpness and SSIM not worse than the
feather baseline by more than 0.01.

Usage:  python3 sweep.py /tmp/argus_phantom [--json sweep.json]
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blend import blend  # noqa: E402
from evaluate import psnr, seam_score, sharpness  # noqa: E402
from tiles import load_tiles, register  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("phantom_dir")
    ap.add_argument("--json", default=None)
    a = ap.parse_args(argv)

    meta = json.load(open(os.path.join(a.phantom_dir, "_phantom.json"), encoding="utf-8"))
    gt = cv2.imread(os.path.join(a.phantom_dir, "_ground_truth.png"), cv2.IMREAD_UNCHANGED)
    gt = gt.astype(np.float32) / 255.0
    gt_sharp = sharpness(gt)

    tiles = load_tiles(a.phantom_dir)
    register(tiles)
    H, W = gt.shape[:2]

    feather = blend(tiles, mode="feather", overlap=meta["overlap"], progress=False)
    feather_ref = {
        "psnr_db": round(psnr(feather[:H, :W], gt), 2),
        "ssim": None,
        "sharpness": round(sharpness(feather), 1),
    }

    rows = []
    for lf, power in itertools.product((0.03, 0.06, 0.10), (2, 4, 8, 16, 32)):
        img = blend(tiles, mode="fusion", overlap=meta["overlap"], lf_ratio=lf,
                    detail_power=power, progress=False)
        bx = sorted({int(t.pos[0]) for t in tiles} | {int(t.pos[0] + t.w) for t in tiles})
        by = sorted({int(t.pos[1]) for t in tiles} | {int(t.pos[1] + t.h) for t in tiles})
        rows.append({
            "lf_ratio": lf,
            "detail_power": power,
            "psnr_db": round(psnr(img[:H, :W], gt), 2),
            "sharpness": round(sharpness(img), 1),
            "sharp_frac_of_gt": round(sharpness(img) / gt_sharp, 3),
            "seam_score": round(seam_score(img, bx, by), 3),
        })

    rows.sort(key=lambda r: (-r["psnr_db"], -r["sharp_frac_of_gt"]))
    print(f"feather baseline: PSNR {feather_ref['psnr_db']} dB, sharpness {feather_ref['sharpness']} "
          f"({feather_ref['sharpness'] / gt_sharp:.2f} of GT {gt_sharp:.1f})")
    print(f"{'lf':>6}{'power':>7}{'PSNR':>8}{'sharp':>9}{'frac':>7}{'seam':>7}")
    for r in rows:
        print(f"{r['lf_ratio']:>6}{r['detail_power']:>7}{r['psnr_db']:>8}{r['sharpness']:>9}"
              f"{r['sharp_frac_of_gt']:>7}{r['seam_score']:>7}")
    best = rows[0]
    print(f"\nbest: lf_ratio={best['lf_ratio']} detail_power={best['detail_power']} "
          f"(PSNR {best['psnr_db']} dB, {best['sharp_frac_of_gt']:.0%} of GT sharpness)")
    if a.json:
        json.dump({"feather": feather_ref, "gt_sharpness": gt_sharp, "rows": rows}, open(a.json, "w", encoding="utf-8"), indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
