# PARAMETERS — ARGUS-OS1

**Version:** 154.0  
**Date:** 2026-07-22

## Model

| Parameter | Value |
|-----------|-------|
| Organism | C. elegans (N2 Bristol, hermaphrodite) |
| Stage | Embryo, zygote → ~100 cells (~3h at 25°C) |
| Cells retaining centrioles | 41 proliferating + 20 intestinal + 7 terminally differentiated = **68 total** |
| Cells eliminating centrioles | ~490 (~88%) |
| Pedigree | Pedigree Score (PCA of 5 metrics): fraction ∥, mean angle, angle variance, switches, cumulative path |

## Platform

| Parameter | Value |
|-----------|-------|
| Version | ARGUS V7 |
| Objective | 60×/1.2 NA WI (new) |
| Camera | sCMOS (Hamamatsu ORCA-Fusion BT) |
| Lasers | 405 nm (Dendra2) + 488 nm + 561 nm |
| Second modality | Phase contrast (cell boundary tracking) |
| Immobilization | Microfluidic chip |
| AI agent | Jetson AGX Orin 64GB (275 TOPS) — local tracking, blind pedigree computation |
| Night vision | IR LED 850nm + 2× NoIR cameras |
| Enclosure | Glove-box isolator (acrylic, HEPA H13, neoprene gloves) |
| Markers | SAS-4::GFP + Centrin1::mCherry + Histone::BFP + PAR-2::GFP + Dendra2::SAS-4 |

## Experiment

| Parameter | Value |
|-----------|-------|
| Pilot N | 10 embryos (stochasticity + phototoxicity + marker validation + pair quantification + ciliogenesis) |
| Main N | 100 embryos (intermediate analysis at 50; expand to 200 if BF<3) |
| Duration | ~3h per embryo |
| Temperature | 25°C |
| Design | Sequential 3-stage: (1) collect all, (2) sister pairs, (3) within-type permutation (10K shuffles) |
| Primary evidence | Bayes Factor > 10 for H₁ vs H₀ |
| Supplementary | Permutation test p < 0.05 after Bonferroni + FDR |
| Controls | Negative: RNAi-PLK-4. Positive: spd-2(or165)/plk-1(RNAi) mutants. Dark: parallel embryos. |
| Cytoplasm control | PAR-2::GFP (posterior cortex asymmetry) |
| Blind protocol | AI tracks → human classifies fate → pedigree computed last |
| Pre-registration | OSF |
| Budget | ~$128,500 (HW: ~$48,500 + personnel: $50,000 + contingency 30%: $30,000) |
