# ARGUS-OS1 — tile pipeline (scan QC, stitching, sampling gates)

Status: 🟢 **working prototype, verified on a synthetic phantom** (no hardware needed).
Origin: the OpenFlexure community threads of 2026-11-15…18 (`docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`),
formalised and self-tested. Literature basis is recorded in `../../EVIDENCE.md`.

## Tools

| File | Purpose | Gate / metric |
|---|---|---|
| `qc.py scan DIR` | F2: validates a scan directory against `scan_data.json` (declared vs actual field resolution, capture mode, overlap, extent in mm, estimated scan time) | exit 1 on ERROR → usable as a pipeline gate |
| `qc.py gate --mpp-um X --binning N` | F6: pre-registered sampling rule (≤100 nm/px, no binning >2×2) | exit 1 on FAIL |
| `qc.py colour DIR --out DIR2` | F6: per-field illumination / white-balance normalisation + provenance JSON | — |
| `blend.py DIR --out stitched.tif` | F4: stitching + fusion (feather low band, detail from sharpest field), optional `--dzsave` | — |
| `measure_rom.py FRAMES --mpp-um X --axis x` | F5: measures usable stage travel from image correlation (Chisholm et al. 2026 method) | measured mm vs commanded |
| `phantom.py OUTDIR` | synthetic ground-truth dataset with illumination drift, per-field defocus, sub-diffraction pairs | — |
| `evaluate.py DIR` | PSNR / SSIM / sharpness / seam score vs ground truth for `hard` / `feather` / `fusion` | — |
| `sweep.py DIR` | reproducible selection of blender defaults | — |

## Measured performance (phantom, 1080 px mosaic, 400 px fields, overlap 0.35)

| mode | PSNR dB | SSIM | sharpness | sharpness vs GT | seam score |
|---|---|---|---|---|---|
| `hard` (paste, no blending) | 22.19 | 0.904 | 493 | 0.96 | **1.67** (visible) |
| `feather` (average only) | 25.76 | **0.942** | 299 | 0.58 | 0.97 |
| `fusion` (this pipeline) | **26.81** | 0.938 | 473 | **0.92** | 0.99 |
| ground truth | — | 1.0 | 512 | 1.00 | 1.00 |

Reading: averaging is accurate but soft (58 % of ground-truth sharpness — exactly the
"averaging makes everything soft" the forum reported); taking detail from the sharpest
field restores 92 % of sharpness and is *more* accurate in PSNR, at a 0.004 SSIM cost.

Low overlap (0.15, the setting the forum recommends for flat slides) also registers
exactly (0 px error) thanks to the dense-patch fallback; fusion keeps 97 % of ground-truth
sharpness there (PSNR 24.61 vs 24.28 for averaging).

Registration accuracy: 0 px error on all tested layouts (0.35 and 0.15 overlap, snake scan;
59/59 exact links on a 0.70-overlap traverse).

## Two dead ends, kept in the code comments

1. **Global phase correlation** (`cv2.phaseCorrelate`) — the method used in the peer-reviewed
   OpenFlexure ROM paper — is ambiguous for steps > half a field; it returned 124 px for a
   true 260 px step. Equal-size NCC returned ≈0 because the non-overlapping part dominates.
2. **Single-edge strip matching** — 15/15 exact at 0.35 overlap, but at 0.70 overlap the
   perpendicular band scored 0.944 at a completely wrong shift (the band no longer fits
   inside the target after a large step, and repeated texture supplies a false peak).

What survives is **patch voting**: 9 patches (22 % of field) matched independently, clustered,
best cluster wins (shift, mean score, vote count). Fallback to a dense corner grid when votes
are low.

## Usage on real scan data

```bash
cd software/pipeline
python3 qc.py scan ~/scan_2026-11-20 --seconds-per-field 3   # F2 — must print PASS
python3 qc.py gate --mpp-um 0.0388 --binning 1               # F6 — must print PASS
python3 qc.py colour ~/scan_2026-11-20 --out ~/scan_norm      # F6 — before any ML
python3 blend.py ~/scan_norm --out embryo.tif --overlap 0.35 --dzsave embryo_dz
```

Notes
* Defaults (`lf_ratio=0.03`, `detail_power=8`) were selected by `sweep.py` on the phantom
  (best PSNR subject to ≥90 % of ground-truth sharpness); re-run the sweep on real data.
* `--mode feather` gives the reference the pipeline must beat; `--mode hard` reproduces the
  naive paste so seams can be shown to a reviewer.
* Memory: the whole mosaic is held in RAM (fine for OS1 scan sizes, revisit for OS2).

## Tests

```bash
cd software && python3 -m pytest tests/test_pipeline.py -q      # 7 passed
```
