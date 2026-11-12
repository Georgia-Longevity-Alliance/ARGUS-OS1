# DESIGN — ARGUS-OS1

**Version:** 2.1
**Date:** 2026-10-14

## Geometry (fixed 2026-11-12)

**All stages are inverted. Upright variants are withdrawn.** The specimen vessel is closed, opaque and never moved; the objective looks up from below, **dry**, through a No. 1.5H coverslip into aqueous medium. No immersion of any kind (no oil, no water film). The humid warm volume is the vessel, not the enclosure.

Consequences: fixed specimen (identity is assigned by position), objective-only XYZ, maximum dry NA 0.95 (PSF 0.33 µm) — sub-0.3 µm readout requires structured illumination, for which the OET DMD is reused (extension slot). Binocular viewing is realised as a two-camera head. See `docs/ARGUS_EngineeringNote_InvertedOptics_DualCamera_2026-11-12.md` and `docs/ARGUS_EngineeringNote_TwoZoneContainment_2026-11-12.md` (both preliminary PI drafts).

## Architecture

ARGUS-OS1 is built on OpenFlexure v6.1.5 with local AI compute.

| Stage | Hardware | Software | Budget |
|:---:|------|------|:---:|
| **OS1 (V6)** | OpenFlexure + Jetson Orin NX + Dry 40× | CellPose + tracking + lineage | $3-5K |
| **OS2 (V7)** | 40×/0.95 dry (corr.) + sCMOS + microfluidic + SIM slot | Jetson AGX | ~$70K HW / ~$307K full |
| **OS3 (V8)** | Light-sheet + fs-laser + tweezers | Full platform | +$141K |

## Key Design Decisions

### 1. Inverted geometry, dry objectives
The objective works dry from below through a 170 µm coverslip; the vessel never moves and only the objective carriage translates in XYZ. The 40×/0.95 dry correction-collar objective sets the resolution floor (0.33 µm PSF); a 60×/1.2 water objective is not used — no immersion is permitted over a months-long campaign.

### 2. Local edge-AI (no cloud dependency)
Jetson Orin NX (OS1) / Jetson AGX Orin (OS2) runs all AI inference locally. No cloud dependency means: (a) no latency for real-time tracking, (b) no bandwidth constraint for 100-embryo overnight runs, (c) data privacy for unpublished research.

### 3. Motor release via Sangaboard API
WilliamW (2026) implemented a motor release feature in the Sangaboard firmware. This allows the microscope stage to be disengaged for manual positioning, then re-engaged for automated scanning — critical for the "survey → target" workflow.

### 4. Transparent embryo as the primary validation model
- Transparent → no sectioning needed
- Fully mapped invariant lineage (Sulston 1983) → known cell identities
- Short embryogenesis (~3 h) → overnight protocols feasible
- 7 fluorescent markers available
- Centriole biology conserved with mammals

> **📌 Specimen scope:** the platform is a general autonomous fluorescence microscope: development from the zygote onward in transparent embryos, plus **cell cultures** (hPSC-derived/primary cardiomyocytes, RPE1), organoids and other transparent specimens. Only the AI module (segmentation/tracking) needs training per specimen type — consistent with the platform's "easily trainable" principle.

### 5. Blind protocol
AI tracks centrioles → human classifies fate (retained/eliminated) without seeing pedigree → pedigree computed last. This prevents confirmation bias in fate classification.

### 6. Energy architecture
```
Jetson inference: ~5-15 W (continuous)
Laser illumination: ~1-3 W (intermittent)
Camera acquisition: ~2-5 W (burst)
Total overnight run: ~200 Wh (≪ 1 kWh)
```

## AIS Integration

ARGUS-OS1 is the first physical instantiation of the AIS (Autonomous Intelligence Socket) protocol:

| AIS Component | ARGUS-OS1 Instantiation |
|---------------|------------------------|
| Passport | 17 capabilities, 9 forbidden actions, 650+ lines JSON |
| Body Law | Laser safety, temp ≤37°C, phototoxicity ceiling |
| Flight Recorder | Centriole tracking log (coordinates, intensities, divisions) |
| LLM Bridge | Anomaly detection → diagnosis → safe restart or pause |
| Trace Network | Solved anomalies shared across all ARGUS devices |
| Knowledge Field | Published findings → Aletheia claims with provenance |

## References
- OpenFlexure: https://openflexure.org
- Sangaboard: https://github.com/rwb27/sangaboard
- Sulston 1983: PMID 6684600
- WilliamW motor release: OpenFlexure forum (2026)
