# PARAMETERS — ARGUS-LP_OS

**Version:** 51.0 — Synchronised with CONCEPT v51
**Date:** 2026-07-19

## Phase 1 (v1.0) — Sister Tracking (RPE1-hTERT)

| Parameter | Value |
|-----------|-------|
| **Microscope** | OpenFlexure v6.1.5, 60×/1.2 NA WI |
| **Camera** | RasPi Camera HQ (pilot) → ZWO ASI183MM Pro cooled (+$1,018 net) SNR fallback |
| **Night vision** | IR LED 850 nm + Camera NoIR — standard |
| **Incubator** | New CO₂ (Benchmark MyTemp / Binder CB 60), 37°C, 5% CO₂, HEPA H13 |
| **O₂** | 5% via N₂ purge + LuminOx sensor |
| **Cell line (primary)** | RPE1-hTERT (ATCC CRL-4000) |
| **Cell line (Phase 3 / v2.0)** | hTERT-NPCs (ReNcell/Lonza) |
| **Markers (live)** | Centrin1-GFP + H2B-GFP (stable lentiviral) — TRACKING only |
| **Markers (endpoint)** | Cenexin antibody — CLASSIFICATION + acetylated tubulin (cilium) |
| **Sister isolation** | CYTOO 2-cell islands (fibronectin, PEG borders). Optional: 3-axis micromanipulator (FOSH-adapted) +$1,200. |
| **Microinjection** | Optional: pneumatic microinjector (apoptosis factors, dyes, siRNA) |
| **Imaging interval** | 10 min (interphase) / 1 min (mitosis trigger) |
| **Duration** | 72h continuous + 8h overnight dark recovery |
| **N** | 200 pairs (Pilot: 50 pairs → effect size → final N) |
| **Primary endpoint** | Time-to-ciliogenesis (hours from cytokinesis to cilium ≥1 µm). Kaplan-Meier + Cox PH. |
| **Secondary endpoints** | Cilium presence at 72h (binary, McNemar). Ki67 status (binary, McNemar). |
| **Tertiary (NPCs)** | Differentiation: Nestin/Sox2 → Tuj1/GFAP (Fisher exact). |
| **Lineage** | Full tree: mother→daughters→granddaughters→great-granddaughters (~3 cell cycles in 72h). |
| **Statistics** | Primary: Fine-Gray subdistribution hazard (competing risk: division). Secondary: Cox PH (no competing risks). Binary: McNemar + glmer. |
| **Power** | Primary: 80% at HR≥1.35 with N=200 pairs, ICC ρ=0.3, 20% attrition. Secondary: 80% at 15 pp difference (65:35 split). |
| **Maturation state** | Cenexin ratio _M_ — continuous predictor. Binary _M>1.5_ calibrated via ROC in pilot. |

## Go/No-Go Gates

| Gate | Criterion | Fail → Action |
|------|-----------|---------------|
| Pilot 0 | Drift <5 µm/24h, 7 days | Heated enclosure |
| Pilot 1 | Centrin-Cenexin concordance ≥90% | Cenexin-mCherry line |
| Pilot 2 | CYTOO cell retention ≥80%, 72h | Gridded microwells |
| Pilot 3 | Effect size measured (50 pairs) | Adjust N |
| SNR | ≥5 at ≤5% LED, ≤200 ms | Cooled sCMOS (+$1,800) |

## Budget — v1.0

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA, motors, bearings, fasteners) | 600 |
| RasPi 5 (8GB) + 1TB NVMe SSD | 250 |
| Camera HQ + C-mount RMS adapter | 150 |
| Objective 60×/1.2 NA WI (Olympus/Nikon, tested used) | 3,500 |
| LED 488 nm + excitation/emission/dichroic filter cube (Thorlabs) | 900 |
| IR LED 850 nm + Camera NoIR (night vision) | 50 |
| Incubator CO₂ (new, Benchmark MyTemp / Binder CB 60) | 7,500 |
| O₂ control (N₂ cylinder + regulator + LuminOx + solenoid) | 500 |
| Jetson Orin NX 16GB + carrier board | 700 |
| RasPi 5 (4GB) + Hailo-8L | 180 |
| Centrin1-GFP RPE1-hTERT (lentiviral transduction, commercial) | 1,500 |
| Cenexin antibody (100 µg) | 350 |
| RPE1-hTERT + ReNcell NPCs (1 vial) | 1,800 |
| Culture media, FBS, supplements, antibiotics | 500 |
| CYTOO coverslips ×20 | 1,500 |
| Tetraspeck beads | 250 |
| IF antibodies (acetyl-tubulin + secondary + DAPI) | 400 |
| Transfection reagents | 250 |
| Consumables (plastic, tips, tubes, PFA, Triton X-100) | 600 |
| Cables, connectors, power supplies, misc | 200 |
| Shipping, customs (Georgia) | 500 |
| **Subtotal v1.0** | **22,180** |
| **+15% contingency** | **3,327** |
| **SNR fallback (sCMOS, net)** | **1,018** |
| **TOTAL v1.0 (max)** | **$26,525** |

### Optional: Micromanipulator Module (+$1,208)

| Line item | $ |
|-----------|--:|
| 3-axis micromanipulator (FOSH v2.0 adapted) | 400 |
| Pneumatic microinjector | 500 |
| Glass capillaries (box of 100) | 60 |
| Mounting bracket (3D-printed, OF-compatible) | 40 |
| Tubing, connectors, syringe | 50 |
| +15% contingency | 158 |
| **TOTAL v1.0+ (with micromanipulator)** | **$27,733** |

## Results Strategy

| Outcome | Action |
|---------|--------|
| p<0.05, Scenario A or B | Platform paper + biology paper |
| p≥0.05, Scenario C | Platform paper + null result («centrosome maturation state does not predict cilium fate in RPE1») |
| Platform failure | Technical report |

**We publish regardless.**

## Phase 2 (v1.5) — Causality

| Experiment | System | Cost |
|------------|--------|-----:|
| Odf2 KO + HDAC6i rescue | RPE1-hTERT | $3,000 |
| Cenexin domain-specific KO | RPE1-hTERT (Phase 3 / v2.0) | $3,000 |

## Phase 3 (v2.0) — Progenitor Map

| System | Markers |
|--------|---------|
| hTERT-NPCs | Nestin/Sox2 → Tuj1/GFAP |
| MSCs | Oil Red O / Alizarin Red / Alcian Blue |
| CD34+ HSPCs | CD34/CD38/CD45RA/CD90 |
