# STATE — ARGUS-LP_OS

**Date:** 2026-07-20
**Status:** 🟡 v54 — v1.0 (V0+V6): наблюдение. v2.0 (V7): поиск причин (водная иммерсия 60×, локальный AI). v3.0: абляция + манипуляторы. Научная платформа: CONCEPT.md. Инженерные: docs/VERSIONS.md.

## Current Design (v50 / Platform v1.0)

| Parameter | Value |
|-----------|-------|
| **Grant type** | INSTRUMENT (H₁) + BIOLOGY (H₂ + H₃) |
| **H₁ — Platform** | Standalone result: first open-source centrosome-aware lineage tracker |
| **H₂ — Biology (RPE1)** | Mature mother → shorter time-to-ciliogenesis |
| **H₃ — Fate (NPCs)** | Mature mother → progenitor maintenance (Nestin⁺/Sox2⁺) |
| **Cell models** | RPE1-hTERT + hTERT-NPCs (both in Phase 1) |
| **Primary endpoint** | Time-to-ciliogenesis (Kaplan-Meier, Cox PH) |
| **Secondary** | Cilium binary + Ki67 |
| **Lineage** | Full tree: 3 generations (~72h, 3 cell cycles) |
| **Mechanism** | Pathway A: spindle asymmetry (Thomas 2024). Pathway B: β-catenin/Wnt (Valdes Michel 2025). |
| **Markers** | Centrin1-GFP (live TRACKING) + Cenexin antibody (endpoint CLASSIFICATION) |
| **Sister isolation** | CYTOO 2-cell islands (fibronectin, PEG borders) |
| **Design** | Natural sister comparison. NO laser. NO ablation. NO micropipette. |
| **Night vision** | IR LED 850 nm + Camera NoIR — standard |
| **Primary endpoint** | Cilium presence (acetylated tubulin) — single endpoint |
| **Statistics** | McNemar + glmer. N=200 pairs. 80% power at 15 pp with ICC ρ=0.3. |
| **Objective** | 60×/1.2 NA WI |
| **Budget** | $19,092 (max with all fallbacks) |
| **Timeline** | Pilots: 4 weeks. Main: 4 weeks. Total: ~12 weeks. |
| **References** | 26 verified PMIDs |

## Platform Versions

| Version | Hardware | Experiment | Laser |
|:-------:|----------|------------|:-----:|
| **v1.0** | OF v6.1.5, 60×/1.2 NA WI, night vision, HEPA H13 | Phase 1 — RPE1 observation | ❌ |
| **v1.5** | Same as v1.0 + Odf2 KO reagents | Phase 2 — Causality | ❌ |
| **v2.0** | Glove-box (HEPA H13, UV-C), fs laser, multi-camera NV | Phase 3 — NPC + ablation | ✅ |

## Key Decisions (2026-07-19)

- **v50:** Time-to-ciliogenesis primary endpoint (Kaplan-Meier). β-catenin/Wnt mechanism (Valdes Michel 2025, PMID 39813084). hTERT-NPCs added to Phase 1. Lineage tree (3 generations). H₁ strengthened as standalone platform result.
- **v49:** Platform versions unified (v1.0/v2.0/v3.0). Night vision standard. HEPA H13 in glove-box. Real budgets.
- **v48:** Spindle≠Fate gap explicitly acknowledged in Central Hypothesis
- **v47:** Centrin1-GFP = TRACKING ≠ Cenexin antibody = CLASSIFICATION
- **v46:** 60×/1.2 NA WI primary. CYTOO primary. Micropipette removed.
- **v45:** Alternative hypotheses (A/B/C). HDAC6i rescue. N=200 pairs. Continuous M.

## Core Files Status

| File | Version | Sync |
|------|:-------:|:----:|
| CONCEPT.md | v49 | ✅ |
| README.md | v49 | ✅ |
| PARAMETERS.md | v49 | ✅ |
| TODO.md | v49 | ✅ |
| STATE.md | v49 | ✅ |
| MEMORY.md | v49 | ✅ |
| _pi.md | v49 | ✅ |
| MAP.md | v49 | ✅ |
| hardware/README.md | v49 | ✅ |
| software/README.md | v49 | ✅ |

## Next Actions

1. Pilot 0: 7-day incubator stability test
2. Pilot 1: Centrin-Cenexin concordance
3. Install night vision (IR LED + Camera NoIR)
4. Submit INSTRUMENT grant (v1.0)
5. OSC resubmit

## 7 Peer Reviews Processed

All major criticisms addressed. Design is minimal sufficient — platform validation + single biological question.
