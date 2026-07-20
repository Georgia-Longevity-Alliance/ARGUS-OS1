# CONCEPT — ARGUS-OS1

**Version:** 97.5
**Date:** 2026-07-21
> **v97.5:** XYZ→position. SiR-Tubulin 100 nM. Controls expanded (SiR toxicity, Z-drift autofocus, alternative mechanisms).
> **v97.4:** Binary trajectory (∥/⟂).
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
| 2. Centriole detection | CellPose 2.0 + Bayesian tracker | Min spot intensity >3σ above background. **Records position + frame number.** |
| 3. Mitosis + spindle | SiR-Tubulin (640 nm) | Chromatin condensation trigger. **Record spindle vector (XY — primary, Z — secondary, ~1 µm precision).** |
| 4. Lineage assignment | Python (NetworkX) | Mother→daughter links. **Каждый узел: траектория = последовательность XY-векторов + n_divisions.** |
| 5. Cilium detection | Arl13B IF (endpoint) | Length ≥1 µm. |
| 6. Tracking QC | Confidence-based (CellPose score) | <5% manual review, ~10-15 human-hours for N=400. |

> **Минимальный набор маркеров:** Centrin1-GFP + SiR-Tubulin + Arl13B. **Возраст = количество делений. Траектория:** в C. elegans — бинарная (∥/⟂, меридиональное/экваториальное). В RPE1 — **угол θ** (0-180°, непрерывная переменная относительно предыдущего деления). Судьба = Arl13B⁺.

---

## 2. Controls and Confounds

| Confound | Control |
|----------|---------|
| Centrin1-GFP may alter cell cycle | CRISPR-KI preferred. WB ≤2× endogenous. Δ>10% cilium timing vs WT → clone rejected. |
| 488 nm + 640 nm phototoxicity | Pilot 0.5: 72h. SiR-Tubulin at **100 nM** (validated non-toxic at ≤100 nM). Measurements: viability, ROS, γH2AX, JC-1. Δ>10% → reduce duty cycle. |
| SiR-Tubulin may affect MT dynamics (docetaxel-based) | Control: cells without SiR-Tubulin. Compare division frequency + spindle orientation. |
| Serum starvation effects | Pilot 0.5: test 0.5%/1%/5% FBS. Select ≥70% ciliogenesis. |
| Z-drift during 48h | Autofocus (Knapper 2022) + reference GFP beads. Pilot 0 validates drift <10µm/24h. |
| Alternative mechanisms (cytoplasmic, epigenetic) | **Acknowledged.** This study tests the centriolar hypothesis. OS2/OS3 designed to rule out alternatives. |

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

## 4. Budget

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA) + motors + bearings | 800 |
| RasPi 5 (8GB) + 1TB NVMe SSD + Camera HQ | 500 |
| 60×/1.2 NA WI objective (**новый**, Nikon/Olympus) | 6,500 |
| LED 488 nm + LED 640 nm + excitation/emission filters | 800 |
| Incubator CO₂ (Benchmark MyTemp) + glove-box + HEPA H13 | 12,000 |
| Jetson Orin NX 16GB | 700 |
| Centrin1-GFP RPE1-hTERT (CRISPR-KI or lentiviral) | 2,500 |
| hTERT-NPCs + culture media + FBS + supplements | 1,500 |
| Arl13B antibody + secondary + DAPI | 400 |
| SiR-Tubulin (Spirochrome, 5 × 35 nmol) | 500 |
| Consumables (plastic, tips, PFA, Triton) | 800 |
| Contingency (25%) | 6,800 |
| **Total** | **~34,000** |

---

## 5. Key References

| # | Reference | PMID | Topic |
|---|-----------|------|-------|
| 1 | Anderson & Stearns (2009) | 19682908 | Centriole age → cilium asymmetry |
| 2 | Paridaen et al. (2013) | 24120134 | Cilium membrane → asymmetric inheritance |
| 3 | Reina & Gonzalez (2014) | 25047620 | Fate follows age — review |
| 4 | Thomas & Meraldi (2024) | 39012627 | Cenexin→Plk1→SAI 3.1% |
| 5 | Gasic et al. (2015) | 26287477 | 85% CIN via Cenexin |
| 6 | Gaudin et al. (2021) | 34402855 | DISCO complex — centriole maturation |
| 7 | Hall & Hehnly (2021) | 33561384 | Subdistal appendages — review |
| 8 | Kumar et al. (2020) | — | 3-cycle centriole maturation, Cells 9(6):1429 |
| 9 | Azimzadeh (2020) | — | Centrosomes in asymmetric division, Curr Opin Cell Biol 67:149 |
| 10 | Chai et al. (2024) | — | Multi-SpinX spindle tracking (bioRxiv) |
| 11 | Malcolm et al. (2026) | — | OpenFlexure live-cell validation (bioRxiv) |
| 12 | Knapper et al. (2022) | 34625963 | Autofocus for OpenFlexure |
| 13 | Stringer et al. (2021) | 33318659 | CellPose 2.0 |
| 14 | Sulston & Horvitz (1977) | 838129 | C. elegans complete lineage |

---

*Version 97.8 — OS1→OS2→OS3. 3 markers. Trajectory: C. elegans = ∥/⟂, RPE1 = angle θ. $34K.*

> **Объектив:** $3,500 — б/у Olympus/Nikon с проверкой. Новый: $5,000-8,000. Заложена проверка б/у перед покупкой.
