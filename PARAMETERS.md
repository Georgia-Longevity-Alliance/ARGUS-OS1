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
