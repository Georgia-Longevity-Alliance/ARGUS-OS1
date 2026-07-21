# PARAMETERS — ARGUS-OS1

**Version:** 63.0 — sync with CONCEPT v112
**Date:** 2026-07-21

## Model

| Parameter | Value |
|-----------|-------|
| Organism | C. elegans (N2 Bristol, hermaphrodite) |
| Stage | Embryo, zygote → ~100 cells (~3h at 30°C) |
| Cells retaining centrioles | 41 proliferating + 20 intestinal + 7 terminally differentiated = **68 total** |
| Cells eliminating centrioles | ~490 (~88%) |
| Pedigree | ∥/⟂ relative to A/P axis at anaphase. Full history per centriole. |

## Platform

| Parameter | Value |
|-----------|-------|
| Version | ARGUS V8 (light-sheet) |
| Objective | 60×/1.2 NA WI (new) |
| Camera | sCMOS (Hamamatsu ORCA) |
| Lasers | 488 nm + 561 nm |
| Immobilization | Microfluidic chip |
| AI agent | Jetson AGX Orin 64GB (275 TOPS) — local, autonomous |
| Night vision | IR LED 850nm + 2× NoIR cameras |
| Surveillance | 2× internal cameras + LED lighting |
| Enclosure | Glove-box isolator (acrylic, HEPA H13, neoprene gloves) |
| Markers | **SAS-4::GFP (primary, validated).** Centrin1-GFP (alternative). + histone::GFP. |

## Experiment

| Parameter | Value |
|-----------|-------|
| N | 30-50 embryos |
| Duration | ~3h per embryo |
| Temperature | 30°C |
| Analysis | Mixed-effects logistic regression: fate ~ pedigree + age + (1|embryo) |
| Budget | ~$177,000 (Core Phase 1), ~$225,000 (all phases) |
