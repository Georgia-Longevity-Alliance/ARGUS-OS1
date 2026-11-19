"""ARGUS-OS1 — synthetic intra-operative phantom for the tile pipeline.

Produces a ground-truth mosaic plus overlapping fields with the failure modes
that the OpenFlexure community thread (2026-11-18) described:
  * per-field illumination gain differences (vignetting / colour drift),
  * per-field defocus (blur) of varying strength,
  * sensor noise,
  * centriole-like sub-diffraction *pairs* whose separation must survive the
    fusion step (our 100 nm/px acceptance criterion in physical units).

Usage:  python3 phantom.py OUTDIR [--size 1440] [--tile 400] [--overlap 0.35]
"""

from __future__ import annotations

import argparse
import json
import os

import cv2
import numpy as np


def make_ground_truth(size: int, seed: int = 7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    img = np.full((size, size, 3), 0.88, np.float32)  # brightfield background

    # cell bodies (soft, dark blobs)
    for _ in range(140):
        cx, cy = rng.integers(0, size, 2)
        ax, ay = rng.integers(10, 34, 2)
        cv2.ellipse(
            img,
            (int(cx), int(cy)),
            (int(ax), int(ay)),
            float(rng.integers(0, 180)),
            0,
            360,
            tuple(float(v) for v in rng.normal(0.55, 0.08, 3)),
            -1,
        )
    img = cv2.GaussianBlur(img, (0, 0), 1.2)

    # high-frequency texture (chromatin-like)
    tex = rng.normal(0, 1, (size, size)).astype(np.float32)
    tex = cv2.GaussianBlur(tex, (0, 0), 0.8)
    tex = 0.06 * tex / (np.abs(tex).max() + 1e-9)
    img += tex[..., None]

    # centriole-like pairs: 2 dark dots, 4 px apart (sub-diffraction at field scale)
    for _ in range(90):
        cx, cy = rng.integers(20, size - 20, 2)
        ang = rng.uniform(0, np.pi)
        d = 4
        for s in (-0.5, 0.5):
            px = int(cx + s * d * np.cos(ang))
            py = int(cy + s * d * np.sin(ang))
            cv2.circle(img, (px, py), 2, (0.15, 0.15, 0.18), -1)
    img = cv2.GaussianBlur(img, (0, 0), 0.6)

    # bright specks (debris) to make seams visible
    for _ in range(60):
        cx, cy = rng.integers(0, size, 2)
        cv2.circle(img, (int(cx), int(cy)), 1, (0.99, 0.99, 0.99), -1)
    return np.clip(img, 0.0, 1.0)


def degrade(tile: np.ndarray, rng: np.random.Generator, idx: int) -> np.ndarray:
    out = tile.astype(np.float32).copy()
    # illumination gain (smooth gradient + per-channel offset)
    gx = np.linspace(0.88, 1.12, tile.shape[1], dtype=np.float32)[None, :]
    gy = np.linspace(0.92, 1.08, tile.shape[0], dtype=np.float32)[:, None]
    gain = gx * gy
    offset = rng.normal(0, 0.02, 3).astype(np.float32)
    out = out * gain[..., None] + offset
    # defocus: cycle through 0, 0.6, 1.2, 1.8 px so a third of the fields are soft
    sigmas = [0.0, 0.6, 1.2, 1.8]
    s = sigmas[idx % len(sigmas)]
    if s > 0:
        out = cv2.GaussianBlur(out, (0, 0), s)
    out += rng.normal(0, 0.008, out.shape).astype(np.float32)
    return np.clip(out, 0.0, 1.0)


def build(outdir: str, size: int = 1440, tile: int = 400, overlap: float = 0.35, seed: int = 7) -> dict:
    os.makedirs(outdir, exist_ok=True)
    gt = make_ground_truth(size, seed)
    rng = np.random.default_rng(seed + 1)
    step = int(round(tile * (1.0 - overlap)))
    coords = list(range(0, size - tile + 1, step))
    if coords[-1] + tile < size:
        coords.append(size - tile)
    meta = {"size": size, "tile": tile, "overlap": overlap, "step": step, "grid": len(coords), "fields": []}
    idx = 0
    for r, y in enumerate(coords):
        xs = coords if r % 2 == 0 else coords[::-1]  # snake scan, as OFM does
        for x in xs:
            patch = gt[y:y + tile, x:x + tile]
            out = degrade(patch, rng, idx)
            name = f"field_{idx:03d}.png"
            cv2.imwrite(os.path.join(outdir, name), (out * 255 + 0.5).astype(np.uint8))
            meta["fields"].append({"img": name, "x": int(x), "y": int(y), "defocus_sigma": [0.0, 0.6, 1.2, 1.8][idx % 4]})
            idx += 1
    cv2.imwrite(os.path.join(outdir, "_ground_truth.png"), (gt * 255 + 0.5).astype(np.uint8))
    with open(os.path.join(outdir, "_phantom.json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
    return meta


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir")
    ap.add_argument("--size", type=int, default=1440)
    ap.add_argument("--tile", type=int, default=400)
    ap.add_argument("--overlap", type=float, default=0.35)
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args(argv)
    meta = build(a.outdir, a.size, a.tile, a.overlap, a.seed)
    print(f"{len(meta['fields'])} fields ({meta['grid']}x{meta['grid']}), tile {meta['tile']} px, "
          f"overlap {meta['overlap']}, step {meta['step']} px -> {a.outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
