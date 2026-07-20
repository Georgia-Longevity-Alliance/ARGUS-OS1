# PARAMETERS — ARGUS-OS1

**Version:** 61.0 — Synchronised with CONCEPT v97
**Date:** 2026-07-21

## Platform

| Parameter | Value |
|-----------|-------|
| Microscope | OpenFlexure v6.1.5, ASA |
| Objective | 60×/1.2 NA WI |
| Camera | RasPi Camera HQ |
| Markers | Centrin1-GFP + SiR-Tubulin (live), Arl13B (endpoint) |
| Spindle orientation pedigreey | Binary: ∥ (along) or ⟂ (perpendicular) per division |
| Age | Number of divisions survived |

## Experiment

| Parameter | Value |
|-----------|-------|
| Cell line | RPE1-hTERT + hTERT-NPCs |
| N | 600 pairs (RPE1), 150 pairs (NPCs) |
| Primary endpoint | Time-to-ciliogenesis (Cox PH) |
| Power | 82% at HR≥1.35, ICC ρ=0.3 |
| Duration | 48h continuous |
| Budget | ~$23,000 |

## OS1 → OS2 → OS3

OS1 collects spindle orientation pedigreey + fate data → OS2 tests convergence → OS3 builds progenitor maps.
