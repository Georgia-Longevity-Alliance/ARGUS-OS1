# PARAMETERS — ARGUS-LP_OS

**Version:** 54.0 — Synchronised with CONCEPT v58
**Date:** 2026-07-19
> **v54:** Materials: ASA primary (Tg 95-105°C), PET fallback. Motor drivers: TMC2209 with GPIO MOSFET de-energising → 3% duty → 0.6W avg. O'Toole bioRxiv (Malcolm 2026) ref. OpenFlexure Forum (WilliamW) pers. comm.

## Phase 1 (v1.0) — Sister Tracking (RPE1-hTERT)

| Parameter | Value |
|-----------|-------|
| **Microscope** | OpenFlexure v6.1.5, **ASA filament (primary, Tg 95-105°C, O'Toole-validated). PET fallback.** 60×/1.2 NA WI |
| **Camera** | RasPi Camera HQ (pilot) → ZWO ASI183MM Pro cooled (+$1,018 net) SNR fallback |
| **IR 850 nm safety** | Pilot 0.5: 72h continuous IR + WI + medium (no cells). ROS, apoptosis, proliferation, ΔT_medium. ⚠️ Kiepas 2020 (PMID 31988150) — general phototoxicity methodology, NOT 850 nm 48h-specific. Pilot 0.5 generates original data. |
| **Incubator** | New CO₂ (Benchmark MyTemp / Binder CB 60), 37°C, 5% CO₂, HEPA H13 |
| **O₂** | 5% via N₂ purge + LuminOx sensor |
| **Cell line (primary)** | RPE1-hTERT (ATCC CRL-4000) |
| **Cell line (Phase 3 / v2.0)** | hTERT-NPCs (ReNcell/Lonza) |
| **Markers (live)** | Centrin1-GFP + H2B-GFP (stable lentiviral) — TRACKING only |
| **Markers (endpoint)** | Cenexin antibody — CLASSIFICATION + acetylated tubulin (cilium) |
| **Sister isolation** | CYTOO 2-cell islands (fibronectin, PEG borders). Optional: 3-axis micromanipulator (FOSH-adapted) +$1,200. |
| **Motor drivers** | 🔴 **TMC2209 UART (StealthChop + CoolStep) + GPIO MOSFET (IRLZ44N) on Vmot.** De-energise motors between imaging cycles. Duty: 3% (18s per 10min). Avg heat: 0.6W. DS18B20 temperature monitoring on motor housings. |
| **Imaging interval** | 10 min (interphase) / 1 min (mitosis trigger) |
| **Duration** | 72h continuous + 8h overnight dark recovery |
| **N** | 300 pairs. Adaptive: if Pilot 3 ICC>0.4 → N=600 (CYTOO reserve covers +$600). Pilot: 50 pairs → effect size + ICC → final N. |
| **Primary endpoint** | Time-to-ciliogenesis (hours from cytokinesis to cilium ≥1 µm). Kaplan-Meier + Cox PH. |
| **Secondary endpoints** | Cilium presence at 72h (binary, McNemar). Ki67 status (binary, McNemar). |
| **Tertiary (NPCs)** | Differentiation: Nestin/Sox2 → Tuj1/GFAP (Fisher exact). |
| **Lineage** | Full tree: mother→daughters→granddaughters→great-granddaughters (~3 cell cycles in 72h). |
| **Statistics** | Primary: Fine-Gray subdistribution hazard with frailty terms (R `frailtypack` — supports random effects for PlateID/IslandID/MotherID). Sensitivity: cause-specific hazards + cluster-robust SE vs. Cox with censoring. Secondary: Cox PH (no competing risks). Binary: McNemar + glmer. Interim: O'Brien-Fleming, conditional power via R `rpact`/`gsDesign`. CP<20% → futility stop. CP 20-50% → adaptive N increase (Cui-Hung-Wang). |
| **Power** | Primary: 82% at HR≥1.35 with N=300 pairs, ICC ρ=0.3, 20% attrition, 30% competing risk. If Pilot 3 ICC>0.4 → N=600 → power >85%. Secondary: 80% at 15 pp difference (65:35 split). |
| **Maturation state** | Cenexin ratio _M_ — continuous predictor. Binary _M>1.5_ calibrated via ROC in pilot. |

## Go/No-Go Gates

| Gate | Criterion | Fail → Action |
|------|-----------|---------------|
| Pilot 0 | Drift <5 µm/24h, 7 days, **60×/1.2 NA dry** | Heated enclosure |
| **Pilot 0.5** | 🔴 **Drift <10 µm/24h WITH water immersion + medium + IR, 72h. CO₂ leak <5%/h. ASA extract viability ≥90%. IR ΔT_medium <1°C. Motor housings <45°C at 3% duty. Serum: ≥70% ciliogenesis AND ≥20% division at chosen FBS condition (test 0.5/1/2/5/10%).** | Active autofocus (Knapper 2022) / parylene-C / reduce IR duty cycle / cell cycle synchronisation / add Peltier cooling |
| **Proof-of-Concept** | 🔴 **≥8/10 pairs Centrin-Cenexin concordance, applicant's lab, 48h, 60×/1.2 NA WI** | Re-evaluate Centrin1-GFP line; consider Dendra2-primary strategy |
| Pilot 1 | Centrin-Cenexin concordance ≥90% **+ PCM/appendage integrity vs. M + ≤20% cells with Centrin1-GFP >2× endogenous + Cenexin vs. age r²≥0.7 + Ninein vs. Cenexin concordance ≥90% + Shh-dependence (Cyclopamine)** | Cenexin-mCherry line / Dendra2 primary / Ninein backup / re-clone Centrin1-GFP |
| Pilot 2 | CYTOO cell retention ≥80%, 72h | Gridded microwells |
| **Pilot 2b** | 🟡 **Cilium asynchrony on CYTOO ≥70% of standard coverslip level (20 pairs each, 48h)** | **Switch to standard coverslips + micromanipulator** |
| Pilot 3 | Effect size + ICC measured (50 pairs) | Adjust N (ICC>0.4 → N=600) |
| Pilot NPC | ≥60% Cenexin asymmetry in 2D **+ Mib1/PCM1 asymmetric localization** | 2.5D Matrigel / RPE1-only |
| SNR | ≥5 at ≤5% LED, ≤200 ms | Cooled sCMOS (+$1,800) |

## Budget — v1.0

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA, motors, bearings, fasteners) | 600 |
| **TMC2209 UART stepper drivers ×4 + GPIO MOSFET (IRLZ44N) + DS18B20 ×4 + BME280** | **80** |
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
| **CYTOO coverslips ×10 (резерв для адаптивного N, если ICC>0.4 → N=600)** | **600** |
| Tetraspeck beads | 250 |
| IF antibodies (acetyl-tubulin, PCM: pericentrin/γ-tubulin/Cdk5Rap2, appendages: Ninein/Cep164, Mib1/PCM1/Notch1, centrin-2, secondary, DAPI) | 700 |
| Transfection reagents | 250 |
| Consumables (plastic, tips, tubes, PFA, Triton X-100) | 600 |
| Cables, connectors, power supplies, misc | 200 |
| Shipping, customs (Georgia) | 500 |
| **Subtotal v1.0** | **23,160** |
| **+25% contingency** | **5,790** |
| **SNR fallback (sCMOS, net)** | **1,018** |
| **TOTAL v1.0 (max)** | **$29,968** |

### Optional: Micromanipulator Module (+$1,208)

| Line item | $ |
|-----------|--:|
| 3-axis micromanipulator (FOSH v2.0 adapted) | 400 |
| Pneumatic microinjector | 500 |
| Glass capillaries (box of 100) | 60 |
| Mounting bracket (3D-printed, OF-compatible) | 40 |
| Tubing, connectors, syringe | 50 |
| +15% contingency | 158 |
| **TOTAL v1.0+ (with micromanipulator)** | **$31,176** |

## Results Strategy

| Outcome | Action |
|---------|--------|
| p<0.05, Scenario A or B | Platform paper + biology paper |
| p≥0.05, Scenario C | Platform paper + null result («centrosome maturation state does not predict cilium fate in RPE1») |
| Platform failure | Technical report |

**We publish regardless.**

## Phase 2 (v2.0) — Causality

| Experiment | System | Cost |
|------------|--------|-----:|
| Odf2 KO + Odf2(FL) rescue (positive control) | RPE1-hTERT | $1,500 |
| Odf2 KO + Odf2(Δ188-806) — distal only, subdistal absent | RPE1-hTERT | $1,500 |
| Odf2 KO + Odf2(Δ1-59) — no recruitment, no cilia (negative control per Tateishi 2013) | RPE1-hTERT | $1,500 |
| Odf2 KO + Odf2(ΔC) — binds centrosome, no appendages (pharmacological control) | RPE1-hTERT | $1,500 |

## Phase 3 (v2.0) — Progenitor Map

| System | Markers |
|--------|---------|
| hTERT-NPCs | Nestin/Sox2 → Tuj1/GFAP |
| MSCs | Oil Red O / Alizarin Red / Alcian Blue |
| CD34+ HSPCs | CD34/CD38/CD45RA/CD90 |
