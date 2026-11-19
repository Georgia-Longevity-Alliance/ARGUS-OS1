"""ARGUS-OS1 — tile blending: feather low band + best-focus detail.

Recept (forum practice, 2026-11-18) formalised with the textbook basis:
  * low spatial frequencies (illumination / colour) -> feather-weighted average
    over a wide overlap (Burt & Adelson 1983, doi:10.1145/245.247);
  * detail band -> *not averaged*: take it from the sharpest field at each
    location (multi-focus fusion; Ballesteros & Garzón 2026, doi:10.1111/jmi.70161
    shows wavelet/focus-selective fusion beats plain averaging for sharpness).
  * optional deep-zoom pyramid export via `vips dzsave` when available.

Defaults (lf_ratio=0.03, detail_power=8) come from `sweep.py` on the phantom:
92 % of ground-truth sharpness, PSNR within 0.03 dB of the best value found,
seam score 0.99 (i.e. invisible).
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tiles import (  # noqa: E402
    Tile,
    canvas_shape,
    focus_map,
    load_tiles,
    make_weights,
    register,
    to_gray,
)


def _bands(tile: Tile, sigma_lf: float) -> tuple[np.ndarray, np.ndarray]:
    img = tile.image
    low = np.empty_like(img)
    for c in range(img.shape[2]):
        low[..., c] = cv2.GaussianBlur(img[..., c], (0, 0), sigma_lf)
    return low, img - low


def _affine_from_low(lows: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    """Per-tile, per-channel gain/offset that maps a field onto the mosaic median.
    Computed from the low band (illumination is a low-frequency phenomenon) and
    then applied to the *whole* field, so the detail band is corrected too."""
    means = np.array([[l[..., c].mean() for c in range(lows[0].shape[2])] for l in lows])
    stds = np.array([[l[..., c].std() for c in range(lows[0].shape[2])] for l in lows])
    m_ref, s_ref = np.median(means, axis=0), np.median(stds, axis=0)
    gain = np.where(stds > 1e-6, s_ref / np.maximum(stds, 1e-6), 1.0)
    offset = m_ref - means * gain
    return gain, offset


def blend(
    tiles: list[Tile],
    mode: str = "fusion",
    lf_ratio: float = 0.03,
    detail_power: float = 8.0,
    feather_ratio: float = 0.85,
    overlap: float = 0.35,
    progress: bool = True,
) -> np.ndarray:
    """mode: fusion (default) | feather (average only) | hard (no blending)."""
    if not tiles:
        raise ValueError("no tiles")
    tiles.sort(key=lambda t: tuple(t.pos))
    ch = tiles[0].image.shape[2]
    H, W = canvas_shape(tiles)
    sigma_lf = max(2.0, lf_ratio * min(tiles[0].w, tiles[0].h))
    feather = max(2.0, feather_ratio * overlap * min(tiles[0].w, tiles[0].h))

    acc_w = np.zeros((H, W, 1), np.float32)
    acc = np.zeros((H, W, ch), np.float32)
    if mode == "fusion":
        acc_low = np.zeros((H, W, ch), np.float32)
        focus_best = np.zeros((H, W, 1), np.float32)

    lows: list[np.ndarray | None] = [None] * len(tiles)
    details: list[np.ndarray | None] = [None] * len(tiles)
    if mode == "fusion":
        raw_lows = [_bands(t, sigma_lf)[0] for t in tiles]
        gain, offset = _affine_from_low(raw_lows)
        for k, t in enumerate(tiles):
            img = t.image * gain[k] + offset[k]
            low = np.empty_like(img)
            for c in range(img.shape[2]):
                low[..., c] = cv2.GaussianBlur(img[..., c], (0, 0), sigma_lf)
            lows[k] = low
            details[k] = img - low

    for k, t in enumerate(tiles):
        x, y, w, h = t.box()
        sl = (slice(y, y + h), slice(x, x + w))
        wt = make_weights(t, feather)[..., None]
        if mode == "hard":
            acc[sl] = t.image
            acc_w[sl] = 1.0
        elif mode == "feather":
            acc[sl] += t.image * wt
            acc_w[sl] += wt
        else:
            low = lows[k]
            acc_low[sl] += low * wt
            acc_w[sl] += wt
            f = focus_map(t)[..., None]
            acc[sl] = np.maximum(acc[sl], f)  # reuse acc as focus container
        if progress and (k + 1) % 10 == 0:
            print(f"  pass1 {k + 1}/{len(tiles)}", file=sys.stderr)

    if mode == "hard":
        return np.clip(acc, 0.0, 1.0)
    if mode == "feather":
        return np.clip(acc / np.maximum(acc_w, 1e-6), 0.0, 1.0)

    focus_best = acc  # focus maps were accumulated here
    low_comp = acc_low / np.maximum(acc_w, 1e-6)

    # pass 2: detail from the sharpest field, soft-selected
    d_acc = np.zeros((H, W, ch), np.float32)
    d_w = np.zeros((H, W, 1), np.float32)
    for k, t in enumerate(tiles):
        x, y, w, h = t.box()
        sl = (slice(y, y + h), slice(x, x + w))
        fb = focus_best[sl]
        rel = focus_map(t)[..., None] / np.maximum(fb, 1e-9)
        wt = make_weights(t, feather)[..., None] * np.power(np.clip(rel, 0.0, 1.0), detail_power)
        d_acc[sl] += details[k] * wt
        d_w[sl] += wt[:, :, :1]
    detail = d_acc / np.maximum(d_w, 1e-6)
    return np.clip(low_comp + detail, 0.0, 1.0)


def save_tiff(path: str, img: np.ndarray) -> None:
    out = (np.clip(img, 0, 1) * 255.0 + 0.5).astype(np.uint8)
    if out.shape[2] == 1:
        out = out[..., 0]
    cv2.imwrite(path, out)


def dzsave(path: str, outdir: str) -> bool:
    exe = shutil.which("vips")
    if not exe:
        return False
    subprocess.run([exe, "dzsave", path, outdir], check=False)
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ARGUS-OS1 tile blending")
    ap.add_argument("input", help="directory with scan fields")
    ap.add_argument("--out", default="stitched.tif")
    ap.add_argument("--mode", default="fusion", choices=["fusion", "feather", "hard"])
    ap.add_argument("--overlap", type=float, default=0.35)
    ap.add_argument("--lf-ratio", type=float, default=0.03)
    ap.add_argument("--detail-power", type=float, default=8.0)
    ap.add_argument("--dzsave", metavar="DIR", default=None)
    args = ap.parse_args(argv)

    tiles = load_tiles(args.input)
    reg = register(tiles)
    print(f"tiles: {len(tiles)}  registration: {reg.summary()}", file=sys.stderr)
    out = blend(tiles, mode=args.mode, overlap=args.overlap,
                lf_ratio=args.lf_ratio, detail_power=args.detail_power)
    save_tiff(args.out, out)
    print(f"written {args.out}  {out.shape[1]}x{out.shape[0]}", file=sys.stderr)
    if args.dzsave:
        print("dzsave:", "ok" if dzsave(args.out, args.dzsave) else "skipped (vips not installed)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
