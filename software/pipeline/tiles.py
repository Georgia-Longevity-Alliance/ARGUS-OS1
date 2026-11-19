"""ARGUS-OS1 — tile IO + translation-only registration.

Why not plain phase correlation?
--------------------------------
The peer-reviewed OpenFlexure range-of-motion measurement (Chisholm et al. 2026,
doi:10.1111/jmi.70192) registers consecutive images by correlation, which is the
right idea — but global Fourier phase correlation is only unambiguous for shifts
smaller than half a field, and our scan steps are 0.65 of a field (overlap 0.35).
Measured on the phantom: `cv2.phaseCorrelate` returned 124 px for a true 260 px
step, and equal-size normalised cross-correlation returned ~0 (the non-overlapping
part of the tile dominates the score). Both failures are documented here so the
next person does not repeat them.

Single-edge strip matching looked good (15/15 exact links at 0.35 overlap) until
it met a 0.70 overlap traverse, where the *perpendicular* band scored 0.944 at a
completely wrong shift — a wide band after a large shift no longer fits inside
the target, and repeated texture supplies a plausible false peak.

What works: **patch voting**. Nine small patches (3x3 grid, 22 % of the field) are
searched independently of each other in the other tile
(`cv2.matchTemplate`, TM_CCOEFF_NORMED); the displacements are clustered and the
cluster with the largest total score wins, giving a shift, a mean score and a
support count. Measured: 15/15 exact links at 0.35 overlap (phantom) and 59/59 at
0.70 (traverse). Chain placement then accumulates drift, which a global
least-squares refinement (translation-only bundle adjustment over all overlapping
pairs) distributes.
"""

from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass, field
from typing import Iterable

import cv2
import numpy as np

IMG_EXT = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp")


def natural_key(path: str):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", os.path.basename(path))]


@dataclass
class Tile:
    path: str
    image: np.ndarray            # float32 0..1, HxWxC
    pos: np.ndarray = field(default_factory=lambda: np.zeros(2, float))
    focus: np.ndarray | None = None

    @property
    def h(self) -> int:
        return self.image.shape[0]

    @property
    def w(self) -> int:
        return self.image.shape[1]

    def box(self) -> tuple[int, int, int, int]:
        x, y = self.pos
        return int(round(x)), int(round(y)), self.w, self.h


def load_tiles(directory: str, limit: int | None = None) -> list[Tile]:
    files = sorted(
        (
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(IMG_EXT) and not f.startswith(("_", "."))
        ),
        key=natural_key,
    )
    if limit:
        files = files[:limit]
    if not files:
        raise FileNotFoundError(f"no images in {directory}")
    tiles = []
    for path in files:
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise IOError(f"cannot read {path}")
        img = img.astype(np.float32) / (65535.0 if img.dtype == np.uint16 else 255.0)
        if img.ndim == 2:
            img = img[..., None]
        tiles.append(Tile(path=path, image=img))
    return tiles


def to_gray(img: np.ndarray) -> np.ndarray:
    if img.shape[2] == 1:
        return img[..., 0]
    return cv2.cvtColor(img.astype(np.float32), cv2.COLOR_BGR2GRAY)


def overlap_fraction(dx: float, dy: float, w: int, h: int) -> float:
    return max(0.0, 1.0 - abs(dx) / w) * max(0.0, 1.0 - abs(dy) / h)


#: patch grid positions and patch size, as fractions of the field
PATCH_GRID = (0.18, 0.50, 0.82)
PATCH_SIZE = 0.22
#: fallback grid for low overlap: corners + centre, small patches
DENSE_GRID = (0.08, 0.30, 0.50, 0.70, 0.92)
MIN_PATCH_SCORE = 0.50
CLUSTER_TOL_PX = 2.0


def _vote(cands: list[tuple[float, np.ndarray]]) -> tuple[np.ndarray, float, int]:
    if not cands:
        return np.zeros(2), 0.0, 0
    cands = sorted(cands, key=lambda c: -c[0])
    clusters: list[dict] = []
    for score, shift in cands:
        for cl in clusters:
            if np.linalg.norm(cl["shift"] - shift) <= CLUSTER_TOL_PX:
                cl["members"].append((score, shift))
                cl["shift"] = np.mean([m[1] for m in cl["members"]], axis=0)
                break
        else:
            clusters.append({"shift": shift, "members": [(score, shift)]})
    best = max(clusters, key=lambda c: sum(m[0] for m in c["members"]))
    wsum = sum(m[0] for m in best["members"])
    shift = sum(m[0] * m[1] for m in best["members"]) / wsum
    return np.round(shift), float(wsum / len(best["members"])), len(best["members"])


def _patches(ga: np.ndarray, gb: np.ndarray, grid: tuple, size: float) -> list[tuple[float, np.ndarray]]:
    h, w = ga.shape
    ps = max(12, int(size * min(w, h)))
    out: list[tuple[float, np.ndarray]] = []
    for fx in grid:
        for fy in grid:
            px = min(max(int(fx * w - ps / 2), 0), w - ps)
            py = min(max(int(fy * h - ps / 2), 0), h - ps)
            tmpl = ga[py:py + ps, px:px + ps]
            res = cv2.matchTemplate(gb.astype(np.float32), tmpl.astype(np.float32), cv2.TM_CCOEFF_NORMED)
            _, mx, _, ml = cv2.minMaxLoc(res)
            if mx >= MIN_PATCH_SCORE:
                out.append((float(mx), np.array([px - ml[0], py - ml[1]], float)))
    return out


def match_shift(a: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, float, str]:
    """Position of tile `b` in the frame of tile `a` (px), score, support label.

    Pass 1 uses a sparse 3x3 patch grid (good for overlap >= ~0.30). If it yields
    fewer than two agreeing patches — which is what happens at the low overlap the
    forum recommended for flat slides (0.15) — pass 2 adds a dense grid of small
    patches near the field corners, where the sliver of shared content lives.
    """
    ga = to_gray(a) * 255.0
    gb = to_gray(b) * 255.0
    cands = _patches(ga, gb, PATCH_GRID, PATCH_SIZE)
    shift, score, votes = _vote(cands)
    if votes < 2 or score < 0.65:
        dense = DENSE_GRID
        cands += _patches(ga, gb, dense, 0.12)
        cands += _patches(ga, gb, dense, 0.08)
        shift, score, votes = _vote(cands)
    return shift, score, f"votes:{votes}"


strip_match = match_shift   # backwards-compatible alias


def initial_layout(tiles: list[Tile], min_score: float = 0.30) -> np.ndarray:
    """Chain placement in acquisition order (handles snake/raster scans)."""
    pos = [np.zeros(2)]
    last_step = np.zeros(2)
    for i in range(1, len(tiles)):
        shift, score, _ = strip_match(tiles[i - 1].image, tiles[i].image)
        if score < min_score:
            shift = last_step          # low-confidence link -> reuse previous step
        else:
            last_step = shift
        pos.append(pos[-1] + shift)
    return np.asarray(pos, float)


@dataclass
class Registration:
    shifts: list[tuple[int, int, np.ndarray, float]] = field(default_factory=list)
    positions: np.ndarray | None = None

    def summary(self) -> dict:
        if self.positions is None or len(self.positions) == 0:
            return {}
        resp = np.array([s[3] for s in self.shifts]) if self.shifts else np.array([0.0])
        return {
            "pairs": len(self.shifts),
            "median_score": round(float(np.median(resp)), 3),
            "min_score": round(float(resp.min()), 3),
            "extent_px": [float(np.ptp(self.positions[:, 0])), float(np.ptp(self.positions[:, 1]))],
        }


def _candidate_pairs(pos: np.ndarray, w: int, h: int, k: int = 8) -> Iterable[tuple[int, int]]:
    """Only *axial* neighbours (pure row / pure column steps).

    Diagonal neighbours share just a corner, which a single strip template
    cannot lock onto — measured on the phantom: 17 of 17 diagonal links were
    wrong (off by a whole step) while all 15 chain links were exact. The raster
    grid is fully connected through axial links alone, so diagonal ones are
    dropped rather than repaired.
    """
    n = len(pos)
    seen = set()
    for i in range(n):
        d = np.linalg.norm(pos - pos[i], axis=1)
        d[i] = np.inf
        for j in np.argsort(d)[:k]:
            j = int(j)
            if j == i:
                continue
            key = (min(i, j), max(i, j))
            if key in seen:
                continue
            seen.add(key)
            step = pos[j] - pos[i]
            big, small = float(np.abs(step).max()), float(np.abs(step).min())
            if big < 0.05 * max(w, h):
                continue
            if small / big > 0.30:            # not an axial neighbour
                continue
            if overlap_fraction(*step, w, h) > 0.02:
                yield i, j


def register(tiles: list[Tile], refine: bool = True, min_score: float = 0.30) -> Registration:
    """Chain layout + pairwise measurements + global least-squares refinement."""
    pos0 = initial_layout(tiles, min_score)
    w, h = tiles[0].w, tiles[0].h

    reg = Registration()
    rows, rhs = [], []
    n = len(tiles)
    for i, j in _candidate_pairs(pos0, w, h):
        shift, score, _ = strip_match(tiles[i].image, tiles[j].image)
        reg.shifts.append((i, j, shift, score))
        if score < min_score:
            continue
        for axis in (0, 1):
            row = np.zeros(2 * n)
            row[2 * j + axis] += 1.0
            row[2 * i + axis] -= 1.0
            rows.append(row)
            rhs.append(shift[axis])

    if refine and rows:
        from scipy.sparse import csr_matrix
        from scipy.sparse.linalg import lsqr

        A = np.asarray(rows, float)
        b = np.asarray(rhs, float)
        # anchor tile 0 at the origin (2 equations, weight 1) — anchoring *every*
        # coordinate instead would bias the whole mosaic towards zero.
        anchor = np.zeros((2, 2 * n))
        anchor[0, 0] = 1.0
        anchor[1, 1] = 1.0
        A = np.vstack([A, anchor])
        b = np.concatenate([b, np.zeros(2)])
        sol = lsqr(csr_matrix(A), b, atol=1e-10, btol=1e-10, iter_lim=20000)[0]
        pos = sol.reshape(-1, 2)
    else:
        pos = pos0

    pos = np.round(pos)
    pos -= pos.min(axis=0)
    for t, p in zip(tiles, pos):
        t.pos = p.astype(float)
    reg.positions = pos
    return reg


def canvas_shape(tiles: list[Tile]) -> tuple[int, int]:
    xs = max(t.pos[0] + t.w for t in tiles)
    ys = max(t.pos[1] + t.h for t in tiles)
    return int(math.ceil(ys)), int(math.ceil(xs))


def make_weights(tile: Tile, feather: float) -> np.ndarray:
    h, w = tile.h, tile.w
    fy, fx = np.ones(h), np.ones(w)
    k = max(1, int(round(feather)))
    ramp = np.linspace(0.0, 1.0, k + 2)[1:-1]
    fx[:k] = np.minimum(fx[:k], ramp)
    fx[-k:] = np.minimum(fx[-k:], ramp[::-1])
    fy[:k] = np.minimum(fy[:k], ramp)
    fy[-k:] = np.minimum(fy[-k:], ramp[::-1])
    return np.outer(fy, fx).astype(np.float32)


def focus_map(tile: Tile, sigma: float = 2.0) -> np.ndarray:
    """Local focus measure: box-filtered squared Laplacian of luminance."""
    g = to_gray(tile.image)
    lap = cv2.Laplacian(g, cv2.CV_32F, ksize=3)
    energy = cv2.boxFilter(lap * lap, -1, (7, 7), normalize=True)
    return cv2.GaussianBlur(energy, (0, 0), sigma).astype(np.float32)


def save_scan_data_like(path: str, tiles: list[Tile], mpp_um: float, overlap: float) -> None:
    """Write a fixture mimicking the OpenFlexure `scan_data.json` layout."""
    import time

    data = {
        "instrument": "ARGUS-OS1 phantom",
        "created": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "image_count": len(tiles),
        "capture_mode": "full",
        "full_resolution": [tiles[0].w, tiles[0].h],
        "overlaps_xy": [overlap, overlap],
        "pixel_size_um": mpp_um,
        "positions": [
            {"x": float(t.pos[0]), "y": float(t.pos[1]), "img": os.path.basename(t.path)} for t in tiles
        ],
    }
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=1)
