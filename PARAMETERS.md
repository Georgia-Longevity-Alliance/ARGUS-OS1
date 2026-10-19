# PARAMETERS — ARGUS-OS1

**Version:** 186.0
**Date:** 2026-07-23

## OS Stages

| Stage | Hardware | Budget | Status |
|:---:|------|:---:|:---:|
| **OS1** | V6 — OpenFlexure + Jetson Orin NX + Dry 40× | ~$3-5K | 🔵 Alex building |
| **OS2** | V7 — 60×/1.2 WI + sCMOS + phase contrast + Jetson AGX + microfluidic | ~$126K | 🟡 Planning |
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
| Budget | ~$282,000 (HW: ~$59.7K + AIS Dedicated Server 10yr: $18K + personnel: $50K + contingency: $33K) |

## Engineering Platform (Axio Observer benchmark, 2026-10-19)

> Из `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. Параметры коммерческого эталона vs план ARGUS.

| Параметр | Эталон (Zeiss Axio Observer 7) | ARGUS план | Статус |
|----------|-------------------------------|------------|:---:|
| Аппаратный автофокус | Definite Focus 3 (NIR 835 нм) | Fiducial/LED-автофокус (PMID 42274973, 42525498) | ⚠️ разрыв → P0 |
| Освещение | Colibri 7 (7 каналов LED) | 4-канальный LED (DAPI/FITC/TRITC/Cy5) | ⚠️ P1 |
| Среда (CO₂/temp/влажн.) | Axio Observer live (Glass Lid heated, Controller, Plate K) | Stage-top модуль (дизайн OS2) | ⚠️ P1 |
| Z-точность | Piezo Z (нано-шаг) | Степпер Z (1–2 мкм) → piezo | ⚠️ P2 |
| Детектор | pco.edge 4.2 sCMOS + Axiocam 208 | sCMOS (pco.edge/ORCA-класс) | ⚠️ P2 |
| Опт. сечение | Apotome 3 (SIM) | SIM/HiLo-модуль (OS2/OS3) | ⚠️ P2 |
| Автоиммерсия | Autoimmersion module | Дозатор иммерсии (60× WI) | ⚠️ P2 |
| Автономная смена образцов | ❌ нет | ✅ V9-руки (уникально) | 🟢 |
| ПО | ZEN 3.3 | Micro-Manager + Mastodon + OpenFlexure | 🟢 план |
| Локальный compute | Z8 + RTX A4000 (~200 Вт) | Jetson Orin NX (~5–15 Вт) | 🟢 |

*Помечено ⚠️ — разрывы, закрываемые открытыми решениями (см. TODO.md 🔧).*
