# ARGUS-OS1 V6 — acceptance report

Verdict: **INCOMPLETE**

| # | Check | Status | Detail |
|---|---|---|---|
| A1 | firmware version reported by server | UNKNOWN | no --url given |
| A2 | motor_release exposed | UNKNOWN | no --url given |
| A3 | scan passes QC gate | PASS | scan_data consistent with files |
| A4 | field size / capture mode as declared | PASS | declared resolution == actual, capture_mode full |
| A5 | measured stage travel | UNKNOWN | not measured yet — run measure_rom.py, then pass --rom-mm |
| A6 | sampling gate | PASS | 38.8 nm/px, binning 1x1 (protocol Amendment 2: <=100 nm/px, binning <=2x2) |
| A7 | stitching sanity | PASS | seam score 0.989 (<1.05 pass), registration 0.984 median match score |

## Inputs
* server URL: `—`
* API probe: —
* scan directory: `/tmp/argus_demo.uaoOP1/mosaic`
* mpp: 0.0388 µm/px, binning 1, overlap 0.35
* ROM: None mm

Copy the table into `hardware/PROVENANCE_V6.md`; keep this file as the evidence pack.
