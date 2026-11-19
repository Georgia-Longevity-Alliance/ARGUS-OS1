"""Pytest suite for the ARGUS-OS1 tile pipeline (phantom-based, no hardware).

Run:  cd software && python -m pytest tests/test_pipeline.py -q

The phantom is generated once per session (session-scoped fixture) in a temp dir,
so the numbers asserted below are reproducible from source, not from stored data.
"""

from __future__ import annotations

import json
import os
import sys

import cv2
import numpy as np
import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
PIPELINE = os.path.abspath(os.path.join(HERE, "..", "pipeline"))
sys.path.insert(0, PIPELINE)

import phantom  # noqa: E402
from blend import blend  # noqa: E402
from evaluate import psnr, seam_score, sharpness  # noqa: E402
from measure_rom import measure  # noqa: E402
from qc import gate, scan  # noqa: E402
from tiles import load_tiles, register  # noqa: E402


def _truth(phantom_dir: str) -> dict:
    meta = json.load(open(os.path.join(phantom_dir, "_phantom.json"), encoding="utf-8"))
    return {f["img"]: np.array([f["x"], f["y"]], float) for f in meta["fields"]}


@pytest.fixture(scope="session")
def ph(tmp_path_factory):
    d = str(tmp_path_factory.mktemp("phantom"))
    phantom.build(d, size=1080, tile=400, overlap=0.35)
    return d


@pytest.fixture(scope="session")
def tiles(ph):
    t = load_tiles(ph)
    register(t)
    return t


def test_registration_is_exact(ph, tiles):
    truth = _truth(ph)
    err = np.array([np.abs(t.pos - truth[os.path.basename(t.path)]).max() for t in tiles])
    assert err.max() <= 1.0, f"registration error max {err.max()} px"


def test_fusion_keeps_sharpness_at_least_85pct_of_ground_truth(ph, tiles):
    gt = cv2.imread(os.path.join(ph, "_ground_truth.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0
    img = blend(tiles, mode="fusion", progress=False)
    frac = sharpness(img) / sharpness(gt)
    assert frac >= 0.85, f"fusion sharpness only {frac:.2f} of ground truth"


def test_fusion_beats_plain_averaging_on_psnr(ph, tiles):
    gt = cv2.imread(os.path.join(ph, "_ground_truth.png"), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255.0
    H, W = gt.shape[:2]
    fus = blend(tiles, mode="fusion", progress=False)[:H, :W]
    fea = blend(tiles, mode="feather", progress=False)[:H, :W]
    assert psnr(fus, gt) > psnr(fea, gt), "fusion must not be less accurate than averaging"


def test_seams_are_invisible(ph, tiles):
    bx = sorted({int(t.pos[0]) for t in tiles} | {int(t.pos[0] + t.w) for t in tiles})
    by = sorted({int(t.pos[1]) for t in tiles} | {int(t.pos[1] + t.h) for t in tiles})
    img = blend(tiles, mode="fusion", progress=False)
    assert seam_score(img, bx, by) < 1.05, "visible seams at tile borders"


def test_scan_qc_catches_half_resolution_gotcha(ph):
    meta = json.load(open(os.path.join(ph, "_phantom.json"), encoding="utf-8"))
    bad = {
        "image_count": len(meta["fields"]),
        "capture_mode": "standard",
        "full_resolution": [2800, 2800],
        "overlaps_xy": [0.35, 0.35],
        "pixel_size_um": 0.0388,
    }
    with open(os.path.join(ph, "scan_data.json"), "w", encoding="utf-8") as fh:
        json.dump(bad, fh)
    assert scan(ph) == 1, "QC must fail when declared resolution != actual"

    bad["capture_mode"], bad["full_resolution"] = "full", [400, 400]
    with open(os.path.join(ph, "scan_data.json"), "w", encoding="utf-8") as fh:
        json.dump(bad, fh)
    assert scan(ph) == 0, "QC must pass on a consistent scan"


def test_sampling_gate_matches_protocol_amendment_2():
    assert gate(0.0388, binning=2) == 0        # 40x/0.75 + 1.55 um pitch
    assert gate(0.100, binning=2) == 0         # exactly on the limit
    assert gate(0.155, binning=4) == 1         # merged centriole pairs


def test_rom_measurement_recovers_known_traverse(tmp_path):
    gt = phantom.make_ground_truth(8200, seed=11)
    rng = np.random.default_rng(3)
    step, tile, n = 120, 400, 12
    for i in range(n):
        patch = gt[2000:2000 + tile, i * step:i * step + tile].copy()
        gain = np.linspace(0.9, 1.1, tile, dtype=np.float32)[None, :, None]
        out = np.clip(patch * gain + rng.normal(0, 0.006, patch.shape), 0, 1)
        cv2.imwrite(str(tmp_path / f"frame_{i:03d}.png"), (out * 255).astype(np.uint8))
    res = measure(str(tmp_path), mpp_um=0.0388, axis="x")
    assert res["links_used"] == n - 1
    assert abs(res["median_step_px"] - step) <= 1.0
    assert abs(res["measured_travel_um"] - (n - 1) * step * 0.0388) < 0.05 * (n - 1) * step * 0.0388
