# PARAMETERS — ARGUS-OS1

**Version:** 186.0
**Date:** 2026-07-23

## OS Stages

| Stage | Hardware | Budget | Status |
|:---:|------|:---:|:---:|
| **OS1** | V6 — OpenFlexure + Jetson Orin NX + Dry 40× | ~$3-5K | 🔵 Alex building |
| **OS2** | V7 — 60×/1.2 WI + sCMOS + phase contrast + Jetson AGX + microfluidic | ~$70K HW / ~$307K full | 🟡 Planning |
| **OS3** | V8 — OS2 + light-sheet + fs-laser + tweezers | +$141K | ⚪ Future |

## Model

| Parameter | Value |
|-----------|-------|
| Specimen | Transparent embryos (development from zygote onward); cell cultures (hPSC-CM, RPE1); organoids |
| Imaging window | Zygote → ~100 cells (~3h at 25°C). **Snapshot at 100-cell, NOT comma stage.** |
| Cells with centrioles at 100-cell | ~68 (41 proliferating + 20 intestinal + 7 terminally differentiated) |
| E-lineage (gut) | INCLUDED as factor analysis (post-embryonic centriole loss) |
| Apoptotic cells | EXCLUDED via CED-3::mCherry (~12% of cells) |
| Pedigree | Pedigree Score (PCA): fraction ∥, mean angle, angle variance, switches, cumulative path |

## Platform

| Parameter | Value |
|-----------|-------|
| Version | OS2 = ARGUS V7 (+ OS3 light-sheet recommended) |
| Objective | 60×/1.2 NA WI |
| Camera | sCMOS (Hamamatsu ORCA-Fusion BT) |
| Lasers | 405 nm + 488 nm + 561 nm + 640 nm |
| Light-sheet | OS3 (V8) module — 10× lower phototoxicity vs widefield |
| Interval | 2-min (5-min fallback per Pilot P2) |
| AI | Jetson AGX Orin 64GB (blind pedigree computation) |
| Markers (7) | SAS-4::GFP, SAS-1::mCherry, Centrin1::BFP, Dendra2::SAS-4, PAR-2::GFP, PAR-3::mCherry, CED-3::mCherry, Histone::CFP |

## Experiment

| Parameter | Value |
|-----------|-------|
| Primary test | Bootstrap Mixed Model: fate ~ PedigreeScore + age + PAR2 + PAR3 + (1\|embryo) + (1\|lineage) |
| Bootstrap | 1,000 embryo resamples |
| Power | OR≥1.2, BF>10, β<0.1 with N=100 embryos (~6,800 centrioles after exclusions) |
| Sensitivity | Sister-cell pairs (Stage 3, secondary) |
| Outcomes | (a) SAS-4 retention, (b) SAS-1 retention (earlier decision point) |
| Exclusions | E-lineage, CED-3(+) apoptotic, <3 timepoints |
| Intermediate | After 50 embryos: BF<3→N=200, BF>10→stop |
| Controls | Negative: RNAi-PLK-4. Positive: spd-2(or165)/plk-1(RNAi) |
| Blind protocol | AI tracks → human classifies fate → pedigree computed last |
| Budget | ~$307K full OS2-stage project (platform HW ~$70K: objective/sCMOS/spinning-disk/lasers/microfluidic/frame/AGX/phase; biology+consumables ~$37K; dissemination ~$8K; personnel ~$130K; contingency $44K; AIS server $18K) — breakdown in CONCEPT §4. Version-table "~$126K" = hardware-only figure (superseded by ~$70K hardware in CONCEPT §4) |

## Engineering Platform (Axio Observer benchmark, 2026-10-19)

> From `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. Commercial benchmark parameters vs ARGUS plan.

| Parameter | Benchmark (Zeiss Axio Observer 7) | ARGUS plan | Status |
|-----------|----------------------------------|------------|:---:|
| Hardware autofocus | Definite Focus 3 (NIR 835 nm) | Fiducial/LED autofocus (PMID 42274973, 42525498) | ⚠️ gap → P0 |
| Illumination | Colibri 7 (7-channel LED) | 4-channel LED (DAPI/FITC/TRITC/Cy5) | ⚠️ P1 |
| Environment (CO₂/temp/humidity) | Axio Observer live (Glass Lid heated, Controller, Plate K) | Stage-top module (OS2 design) | ⚠️ P1 |
| Z precision | Piezo Z (nm step) | Stepper Z (1–2 µm) → piezo | ⚠️ P2 |
| Detector | pco.edge 4.2 sCMOS + Axiocam 208 | sCMOS (pco.edge/ORCA class) | ⚠️ P2 |
| Optical sectioning | Apotome 3 (SIM) | SIM/HiLo module (OS2/OS3) | ⚠️ P2 |
| Auto-immersion | Autoimmersion module | Immersion dispenser (60× WI) | ⚠️ P2 |
| Autonomous sample change | ❌ none | ✅ V9 hands (unique) | 🟢 |
| Software | ZEN 3.3 | Micro-Manager + Mastodon + OpenFlexure | 🟢 plan |
| Local compute | Z8 + RTX A4000 (~200 W) | Jetson Orin NX (~5–15 W) | 🟢 |

*⚠️ marks gaps closable by open solutions (see TODO.md 🔧).*

## Dark state / photon leakage (2026-11-12, NFR-13)

> From `docs/ARGUS_EngineeringNote_DarkState_2026-11-12.md`. The imaging path is reversible — light entering the objective/camera side reaches the specimen.

| Parameter | Value |
|-----------|-------|
| Specimen-plane leakage, dark state | ≤ 0.5 µW/cm² (400–700 nm); ≤ 0.1 µW/cm² (400–500 nm); ≤ 0.043 J/cm²/day |
| Attenuation of each non-imaging path | OD ≥ 4 |
| Optical apertures into the vessel | 1 permanent (170 µm glass bottom) + 1 shuttered top window for transmitted light |
| Shutters | Normally closed (spring-closed solenoid) + independent driver enable + TTL; block flag in park |
| Objective carriage | Inside a light-tight dark cell, opaque bellows on the XYZ travel |
| Camera / binocular / spare ports | Light-tight mini-box; flock-lined M42 adapter with O-ring; binocular tube capped |
| Light piping | Vessel walls/lid opaque (black POM/PEEK); capillary shanks blackened except last 2–3 mm; perfusion lines opaque |
| NIR (awareness cameras, autofocus) | Gated, baffled from the vessel, 940 nm (awareness) / 850 nm (autofocus, ≤1–10 µW), never continuous |
| Dose monitor | Photodiode at specimen plane, 10 s logging, alarm; open shutter outside exposure = Flight Recorder anomaly |
| Verification | V8e dark test (leak map, reciprocity, power-cut, 24 h log, 14-day stability) |
| BOM delta | ≈ $350–720 |

*Applies to OS1–OS4. OS4 adds a sixth source: the OET projector path during manipulation (deliberate, must be inside the light budget).*

## Geometry & containment (2026-11-12, two-zone)

> From `docs/ARGUS_EngineeringNote_TwoZoneContainment_2026-11-12.md`. Humid warm volume = the closed vessel; the enclosure is dry.

| Parameter | Value |
|-----------|-------|
| Containment locus | Closed perfusion chamber (170 µm glass bottom, opaque walls, lid with 10–12 mm window, 2 septum + 2 Luer ports) |
| Only permanent optical boundary | 170 µm coverslip (wet → dry). No wall window |
| Specimen | Never moved; identity is assigned by position (FR-12) |
| Moving element | Objective + 2 Fi epi reflector on an XYZ carriage (X/Y closed-loop ±6–8 mm, step ≤100 nm; piezo Z 100 µm) |
| IM35 property exploited | Focus already moves the nosepiece carriage, stage fixed; finite 160 mm tube → transverse shift does not change focus or magnification |
| Epi light delivery | Light guide / bundle to the moving reflector (illumination path only; never in the imaging path) |
| Heating | Sides + lid, never under the coverslip (thermal bow → focus drift). Thermistor in the medium |
| Dry zone | 24–30 °C, RH < 40 %, desiccant, opaque (NFR-13) |
| Immersion over months | Silicone oil 40×/1.25 (does not evaporate or creep); dry 40×/0.85–0.95 on the same nosepiece for survey |
| CO₂ | Optional CO₂-free HEPES/L-15 medium + perfusion (V6 decides); humidity control then not required |
| Image-side NA at M42 port | ≈0.027 (f/18) → a 1 mm window there costs ≈λ/10 |
| Verification | V8f (14-day closed-vessel stability), V8g (objective-scanning invariance) |
| BOM delta (minimum viable) | ≈ $1,100–2,900 |

## Inverted optics, dual camera, awareness cameras (2026-11-12)

> From `docs/ARGUS_EngineeringNote_InvertedOptics_DualCamera_2026-11-12.md`. **Preliminary draft prepared by PI — engineering review required.**

| Parameter | Value |
|-----------|-------|
| Geometry | **Inverted for all stages** (OS1–OS4). Upright variants withdrawn |
| Objective | Dry, correction collar (0.11–0.23 mm), against a No. 1.5H coverslip; **no immersion anywhere** |
| Max dry NA / PSF | 0.95 → 0.33 µm @520 nm (0.17 µm with SIM via the OET DMD — extension slot) |
| Objective ladder | 4×/0.13, 10×/0.30, 20×/0.75, 40×/0.95 (corr.) |
| Binocular viewing | Two camera ports (no eyepieces): motorised flip mirror (100 % A / split) + dichroic 560 LP; 1:1 relay on port B; parfocality ≤ ±2 µm by shims |
| What stereo is not | A compound head has no parallax; depth comes from a Z-stack (piezo Z, 0.1–0.3 µm steps), not from a stereo pair |
| Awareness cameras | ≥2 visible general view (1/1.8", 16 mm lens ≈ 100 mm field at 300 mm) + ≥2 NIR night vision (IR-cut removed, 850/940 nm, ≤0.001 lux) |
| Dark-state seals | Black silicone septa and O-rings; opaque flap over the lid window (NFR-13.3) |
| Verification | V8h (dual-port parfocality, channel registration), V8i (coverage, NIR leakage) |
| BOM delta | ≈ $5.2–16.1K |

*Applies to OS1–OS4. All of it is a preliminary PI draft: the engineer reviews before purchase.*

