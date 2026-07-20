# CONCEPT — ARGUS-OS1

**Version:** 97.1
**Date:** 2026-07-21
> **v97.1:** Возраст = количество делений (не длина в пикселях). N=400→600. SiR-Tubulin calibration. Valdes Michel уже исправлена в v96.
> **v97:** Радикальное упрощение. Только 3 маркера.
> **v96:** OS1 очищен от Odf2/Phase2.
> **v95:** ARGUS-OS1 = наблюдение.

---

## 0. What ARGUS-OS1 Is

ARGUS-OS1 — открытая платформа для 3D-трекинга центриолей в живых клетках. Измеряет траекторию каждой центриоли (XYZ spindle vector каждого деления) и судьбу клетки. Данные передаются в ARGUS-OS2 для проверки гипотезы lineage-памяти.

### Project Structure

| AIM | Goal | System | Primary endpoint |
|:---:|------|--------|------------------|
| **AIM 1** | **INSTRUMENT** — Build + record centriole trajectories | GFP beads + RPE1 | Drift <10µm/24h, tracking ≥90% |
| **AIM 2** | **KINETICS** — Trajectory length → cilium timing | RPE1-hTERT | Time-to-ciliogenesis (Cox PH) |
| **AIM 3** | **FATE** — Trajectory → differentiation | hTERT-NPCs | Nestin/Sox2→Tuj1/GFAP |

> **🔗 OS1 → OS2 → OS3:** OS1 собирает траектории. OS2 проверяет конвергенцию. OS3 строит прогениторные карты.

---

## 1. Data Processing Pipeline

| Step | Tool | Parameters |
|:----:|------|------------|
| 1. Image pre-processing | Fiji/ImageJ macro | Flat-field correction, bleach correction |
| 2. Centriole detection | CellPose 2.0 + Bayesian tracker | Min spot intensity >3σ above background. **Records XYZ position + frame number.** |
| 3. Mitosis + spindle | SiR-Tubulin (640 nm) | Chromatin condensation trigger. **Record spindle vector (XY — primary, Z — secondary, ~1 µm precision).** |
| 4. Lineage assignment | Python (NetworkX) | Mother→daughter links. **Каждый узел: траектория = последовательность XY-векторов + n_divisions.** |
| 5. Cilium detection | Arl13B IF (endpoint) | Length ≥1 µm. |
| 6. Tracking QC | Confidence-based (CellPose score) | <5% manual review, ~10-15 human-hours for N=400. |

> **Минимальный набор маркеров:** Centrin1-GFP + SiR-Tubulin + Arl13B. **Возраст = количество делений. Траектория = последовательность ОРИЕНТАЦИЙ делений** (в C. elegans: меридиональное/экваториальное — только 2 варианта. В RPE1: угол θ в плоскости XY). Судьба = Arl13B⁺.

---

## 2. Controls and Confounds

| Confound | Control |
|----------|---------|
| Centrin1-GFP may alter cell cycle | CRISPR-KI preferred. WB ≤2× endogenous. Δ>10% cilium timing vs WT → clone rejected. Bouhlel 2017: Sfi1/Centrin control. |
| 488 nm + 640 nm phototoxicity | Pilot 0.5: 72h, viability, ROS, γH2AX, JC-1. Δ>10% → reduce duty cycle. |
| Serum starvation effects | Pilot 0.5: test 0.5%/1%/5% FBS. Select condition with ≥70% ciliogenesis. |
| Glove-box stability | Pilot 0: 7-day GFP beads, drift <10µm/24h. |

---

## 3. The Experiment

### 3.1. Method

| Step | Action |
|:----:|--------|
| 1 | RPE1-hTERT Centrin1-GFP, 3D time-lapse |
| 2 | **Live tracking:** Centrin1-GFP → позиции центриолей. SiR-Tubulin → **XY spindle vector.** |
| 3 | **Траектория:** последовательность XY-векторов делений + количество делений для каждой центриоли. |
| 4 | 48h наблюдение, 2-3 поколения. |
| 5 | Endpoint: Arl13B IF → cilium. |
| 6 | Primary analysis: time-to-ciliogenesis (Cox PH) vs длина траектории. |
| 7 | **Данные передаются в OS2:** траектория + судьба для проверки конвергенции. |

### 3.2. Endpoints

| Endpoint | Type | Analysis |
|----------|:----:|----------|
| Time-to-ciliogenesis | 🎯 Primary | Cox PH: hazard ratio per additional division survived |
| Cilium presence at 48h | Secondary | McNemar (paired) |
| Дифференцировка (NPCs) | Tertiary | Nestin→Tuj1 (Fisher exact) |

### 3.3. Cell Strategy

| Stage | Duration | Go/No-Go |
|:-----|:--------:|----------|
| Pilot 0 (GFP beads) | 1 week | Drift <10µm/24h |
| Pilot 0.5 (phototoxicity) | 1 week | Viability ≥90%, ROS<20% |
| Pilot 1 (Centrin1 validation) | 2 weeks | Tracking ≥90% concordance with manual |
| Main RPE1 (N=400 pairs) | 4 weeks | Primary: time-to-ciliogenesis |
| Main NPCs (N=150 pairs) | 4 weeks | Primary: differentiation |

> **🔗 После OS1:** данные траекторий → OS2 (конвергенция). После OS2 → OS3 (прогениторные карты).

### 3.4. Statistical Design

| Parameter | Value |
|-----------|-------|
| Primary test | Cox PH: Surv(time_to_cilium) ~ n_divisions + strata(generation) |
| N | 600 pairs (interim at 300, O'Brien-Fleming). Увеличено с 400 для мощности при конкурирующих рисках (Fine-Gray). |
| Power | 82% at HR≥1.35, ICC ρ=0.3, 30% competing risk (division before cilium) |

---

## 4. Budget (Simplified)

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA) + motors | 600 |
| RasPi 5 + SSD + Camera HQ | 400 |
| 60×/1.2 NA WI objective | 3,000 |
| LED 488 nm + SiR-LED 640 nm + filters | 600 |
| Incubator CO₂ + glove-box + HEPA | 11,000 |
| Jetson Orin NX | 500 |
| Centrin1-GFP RPE1 + NPCs + media | 2,000 |
| Arl13B antibody + secondary | 300 |
| Consumables + contingency (25%) | 4,700 |
| **Total** | **~23,000** |
