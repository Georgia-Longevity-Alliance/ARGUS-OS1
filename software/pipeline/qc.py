"""ARGUS-OS1 — gates that must pass before scan data enters the pipeline.

`scan`   (F2) validates a scan directory against its `scan_data.json`:
         the OpenFlexure gotcha reported on the forum (2026-11-18) is that fields
         are saved at 1400 px while the sensor crop is 2800 px, unless
         `histo scan capture mode = full`. A silent 2x loss of field causes a 2x
         increase of tile count and hides inside a "successful" scan, so the
         declared resolution is compared with the real file resolution here.
`gate`   (F6) enforces the pre-registered sampling rule (protocol Amendment 2):
         <= 100 nm/px at the sample and no binning above 2x2.
`colour` (F6) removes per-field illumination / white-balance differences by
         mapping every field onto the mosaic median (low-frequency affine),
         which is what the OFM-vs-Aperio comparison required before any ML
         (Corrielus et al. 2026, doi:10.1016/j.ijgc.2026.104993).

Exit code is 0 on pass, 1 if any ERROR-level finding is raised, so the module
can be used as a pipeline gate or in CI.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from blend import _affine_from_low  # noqa: E402
from tiles import IMG_EXT, load_tiles, to_gray  # noqa: E402


def _find_key(data: dict, *names, default=None):
    for n in names:
        if n in data:
            return data[n]
    for v in data.values():
        if isinstance(v, dict):
            for n in names:
                if n in v:
                    return v[n]
    return default


def scan(dirpath: str, seconds_per_field: float | None = None, as_json: bool = False) -> int:
    findings: list[tuple[str, str]] = []

    def add(level: str, msg: str) -> None:
        findings.append((level, msg))

    meta_path = os.path.join(dirpath, "scan_data.json")
    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path, encoding="utf-8") as fh:
            meta = json.load(fh)
    else:
        add("WARN", "scan_data.json absent — positions must be re-derived by registration")

    files = sorted(f for f in os.listdir(dirpath) if f.lower().endswith(IMG_EXT) and not f.startswith(("_", ".")))
    if not files:
        add("ERROR", "no image files")
        _report(findings, as_json, dirpath)
        return 1

    sizes = set()
    for f in files:
        img = cv2.imread(os.path.join(dirpath, f), cv2.IMREAD_UNCHANGED)
        if img is None:
            add("ERROR", f"unreadable: {f}")
            continue
        sizes.add((img.shape[1], img.shape[0]))
    if len(sizes) > 1:
        add("ERROR", f"inconsistent field sizes across the scan: {sorted(sizes)}")
    w, h = sorted(sizes)[-1]

    declared_count = _find_key(meta, "image_count", "n_images", "count")
    if isinstance(declared_count, int) and declared_count != len(files):
        add("ERROR", f"scan_data declares {declared_count} fields, {len(files)} on disk")

    declared_res = _find_key(meta, "full_resolution", "capture_resolution", "resolution")
    if isinstance(declared_res, (list, tuple)) and len(declared_res) == 2:
        dw, dh = int(declared_res[0]), int(declared_res[1])
        if (dw, dh) != (w, h):
            add("ERROR", f"declared resolution {dw}x{dh} != actual {w}x{h} — "
                         "the 1400/2800 px gotcha: set histo scan capture mode = full "
                         "and check things/autofocus.py hardcoded capture mode")
    capture_mode = _find_key(meta, "capture_mode")
    if capture_mode is not None and str(capture_mode).lower() not in ("full", "full_resolution"):
        add("WARN", f"capture_mode={capture_mode!r} — expected 'full' for maximum field")

    overlap = _find_key(meta, "overlaps_xy", "overlap", "overlaps")
    ov = None
    if isinstance(overlap, (list, tuple)) and overlap:
        ov = float(np.mean([float(v) for v in overlap]))
        if ov < 0.12:
            add("WARN", f"overlap {ov:.2f} too small for reliable blending/registration "
                        "(forum practice: 0.15 flat slides, 0.35-0.50 uneven)")

    mpp = _find_key(meta, "pixel_size_um", "pixel_size", "mpp")
    extent = None
    positions = _find_key(meta, "positions", "stage_positions", "fields")
    if isinstance(positions, list) and positions and isinstance(positions[0], dict):
        xs = [float(p.get("x", 0)) for p in positions]
        ys = [float(p.get("y", 0)) for p in positions]
        extent_px = (max(xs) - min(xs) + w, max(ys) - min(ys) + h)
        if mpp:
            extent = (extent_px[0] * float(mpp) / 1000.0, extent_px[1] * float(mpp) / 1000.0)
        add("INFO", f"scanned extent ≈ {extent_px[0]:.0f}×{extent_px[1]:.0f} px"
                    + (f" = {extent[0]:.2f}×{extent[1]:.2f} mm" if extent else ""))

    if mpp:
        add("INFO", f"field {w}×{h} px = {w * float(mpp):.1f}×{h * float(mpp):.1f} µm, "
                    f"{float(mpp) * 1000:.1f} nm/px")
    if seconds_per_field:
        total = len(files) * seconds_per_field
        add("INFO", f"estimated acquisition time at {seconds_per_field:.1f} s/field: "
                    f"{total / 3600:.1f} h for {len(files)} fields")

    _report(findings, as_json, dirpath)
    return 1 if any(lvl == "ERROR" for lvl, _ in findings) else 0


def _report(findings: list[tuple[str, str]], as_json: bool, target: str) -> None:
    if as_json:
        print(json.dumps({"target": target, "findings": findings}, ensure_ascii=False, indent=1))
        return
    print(f"QC {target}")
    for lvl, msg in findings:
        print(f"  [{lvl:5}] {msg}")
    errors = sum(1 for lvl, _ in findings if lvl == "ERROR")
    print(f"  -> {'FAIL' if errors else 'PASS'} ({errors} error(s))")


def gate(mpp_um: float, binning: int = 1, limit_um: float = 0.100, max_binning: int = 2) -> int:
    ok = True
    print(f"sampling at the sample: {mpp_um * 1000:.1f} nm/px (limit {limit_um * 1000:.0f} nm/px)")
    if mpp_um > limit_um:
        print("  [FAIL] sampling coarser than the pre-registered limit "
              "(protocol Amendment 2: pairs merge above ~150 nm/px)")
        ok = False
    print(f"binning: {binning}x{binning} (max {max_binning}x{max_binning})")
    if binning > max_binning:
        print("  [FAIL] binning above the pre-registered maximum")
        ok = False
    print("  ->", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def colour(dirpath: str, outdir: str) -> int:
    tiles = load_tiles(dirpath)
    os.makedirs(outdir, exist_ok=True)
    lows = []
    for t in tiles:
        low = np.empty_like(t.image)
        for c in range(t.image.shape[2]):
            low[..., c] = cv2.GaussianBlur(t.image[..., c], (0, 0), 0.03 * min(t.w, t.h))
        lows.append(low)
    gain, offset = _affine_from_low(lows)
    report = []
    for k, t in enumerate(tiles):
        out = np.clip(t.image * gain[k] + offset[k], 0.0, 1.0)
        name = os.path.basename(t.path)
        cv2.imwrite(os.path.join(outdir, name), (out * 255 + 0.5).astype(np.uint8))
        report.append({"img": name, "gain": [round(float(v), 4) for v in gain[k]],
                       "offset": [round(float(v), 4) for v in offset[k]]})
    with open(os.path.join(outdir, "colour_report.json"), "w", encoding="utf-8") as fh:
        json.dump({"fields": report}, fh, indent=1)
    print(f"normalised {len(tiles)} fields -> {outdir} (provenance in colour_report.json)")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="ARGUS-OS1 QC gates")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="validate a scan directory (F2)")
    s.add_argument("dirpath")
    s.add_argument("--seconds-per-field", type=float, default=None)
    s.add_argument("--json", action="store_true")
    g = sub.add_parser("gate", help="sampling/binning gate (F6)")
    g.add_argument("--mpp-um", type=float, required=True)
    g.add_argument("--binning", type=int, default=1)
    c = sub.add_parser("colour", help="per-field illumination/colour normalisation (F6)")
    c.add_argument("dirpath")
    c.add_argument("--out", required=True)
    a = ap.parse_args(argv)

    if a.cmd == "scan":
        return scan(a.dirpath, a.seconds_per_field, a.json)
    if a.cmd == "gate":
        return gate(a.mpp_um, a.binning)
    return colour(a.dirpath, a.out)


if __name__ == "__main__":
    raise SystemExit(main())
