# PARAMETERS — ARGUS-OS1

**Version:** 158.0
**Date:** 2026-07-22

## Model

| Parameter | Value |
|-----------|-------|
| Organism | C. elegans (N2 Bristol, hermaphrodite) |
| Imaging window | Zygote → ~100 cells (~3h at 25°C). **Snapshot at 100-cell, NOT comma stage.** |
| Cells with centrioles at 100-cell | ~68 (41 proliferating + 20 intestinal + 7 terminally differentiated) |
| E-lineage (gut) | INCLUDED as factor analysis (post-embryonic centriole loss) |
| Apoptotic cells | EXCLUDED via CED-3::mCherry (~12% of cells) |
| Pedigree | Pedigree Score (PCA): fraction ∥, mean angle, angle variance, switches, cumulative path |

## Platform

| Parameter | Value |
|-----------|-------|
| Version | ARGUS V7 + V8 light-sheet (MANDATORY) |
| Objective | 60×/1.2 NA WI |
| Camera | sCMOS (Hamamatsu ORCA-Fusion BT) |
| Lasers | 405 nm + 488 nm + 561 nm + 640 nm |
| Light-sheet | V8 module — 10× lower phototoxicity vs widefield |
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
| Budget | ~$140000 (HW: ~$59.7K + personnel: $50K + contingency: $33K) |
