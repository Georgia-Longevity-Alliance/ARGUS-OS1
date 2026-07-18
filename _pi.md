# _pi.md — ARGUS-LP_OS

**Parent:** Marketing
**GitHub:** https://github.com/Georgia-Longevity-Alliance/ARGUS-LP

> RULE: before any action, read MAP.md, MEMORY.md, CONCEPT.md.

## Summary
ARGUS-LP_OS is an autonomous robotic platform for 24/7 centrosome-aware lineage tracking. Based on OpenFlexure v6.1.5. Fully open (GPLv3/CC-BY-SA). Primary system: RPE1-hTERT. v1.0: no laser, no ablation, sister tracking on CYTOO islands, night vision (IR 850 nm) standard. v2.0: adds glove-box (HEPA H13, UV-C), femtosecond laser.

> RULE: CONCEPT.md and all core files — ENGLISH only. Any non-English text → translate immediately.

## Directory Structure
- `hardware/` — 3D models, STL, schematics (KiCad)
- `software/` — control, AI, analysis (Python/Rust), night vision
- `firmware/` — microcontroller firmware (RasPi Pico, Hailo)
- `docs/` — documentation, protocols, peer reviews, audit reports
- `letters/` — outreach correspondence
- `grants/` — grant applications
- `refs/` — scientific references

## Rules
- All hardware — CC-BY-SA 4.0
- All code — GPLv3
- All data — CC0
- Do not duplicate scientific materials from LC/MCARA/CEDAR
- Engineering here (hardware, software, firmware); science there (theory, grants, articles)
- Minimum 2 commits/week (activity for OSC)

## Current Status (v51)
- CONCEPT.md v51 — 9 peer reviews. Fuentealba 2008 (human) mechanism. Odf2 domain deletions. Barandun corrected. Fine-Gray competing risks.
- 28 verified PMIDs. Budget $24,053.
- RPE1 = kinetics (H₂). NPCs = fate (H₃). Platform versions: v1.0/v2.0/v3.0.
