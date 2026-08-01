# DESIGN — ARGUS-OS1

**Version:** 2.0
**Date:** 2026-08-01

## Architecture

ARGUS-OS1 is built on OpenFlexure v6.1.5 with local AI compute.

| Stage | Hardware | Software | Budget |
|:---:|------|------|:---:|
| **OS1 (V6)** | OpenFlexure + Jetson Orin NX + Dry 40× | CellPose + tracking + lineage | $3-5K |
| **OS2 (V7)** | 60×/1.2 WI + sCMOS + microfluidic | Jetson AGX | ~$126K |
| **OS3 (V8)** | Light-sheet + fs-laser + tweezers | Full platform | +$141K |

## Key Design Decisions

### 1. Upright geometry for water immersion
Inverted scopes are standard for live-cell imaging, but water immersion objectives require upright geometry. The OpenFlexure frame was modified to support this. The 60×/1.2 NA WI objective in OS2 provides the resolution needed for centriole-level tracking.

### 2. Local edge-AI (no cloud dependency)
Jetson Orin NX (OS1) / Jetson AGX Orin (OS2) runs all AI inference locally. No cloud dependency means: (a) no latency for real-time tracking, (b) no bandwidth constraint for 100-embryo overnight runs, (c) data privacy for unpublished research.

### 3. Motor release via Sangaboard API
WilliamW (2026) implemented a motor release feature in the Sangaboard firmware. This allows the microscope stage to be disengaged for manual positioning, then re-engaged for automated scanning — critical for the "survey → target" workflow.

### 4. C. elegans as model organism
- Transparent embryo → no sectioning needed
- Invariant lineage (Sulston 1983) → known cell identities
- 3-hour embryogenesis → overnight protocol feasible
- 7 fluorescent markers available
- Centriole biology conserved with mammals

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
| Knowledge Field | Published findings → Noepedia claims with provenance |

## References
- OpenFlexure: https://openflexure.org
- Sangaboard: https://github.com/rwb27/sangaboard
- Sulston 1983: PMID 6684600
- WilliamW motor release: OpenFlexure forum (2026)
