# CONCEPT — ARGUS-OS1

**Version:** 118.0
**Date:** 2026-07-21
> **v118:** Anderson 2009 confirmed EXPERIMENTAL. +Erpf 2020, +Balestra 2015. 12 refs.

---

## 0. Hypothesis

**Centriole pedigree (∥/⟂) → centriole fate (retained/eliminated).**

In C. elegans, ~88% of cells eliminate centrioles during differentiation. ~68 cells retain them (Kalbfuss & Gönczy 2023, PMID 37256957). Centrioles segregate STOCHASTICALLY (Gönczy & Balestra 2023, PMID 36988082; Erpf & Mikeladze-Dvali 2020).

**Stochastic segregation STRENGTHENS the hypothesis.** If which centriole (old/young) goes to which daughter is random, then age cannot explain any pedigree↔fate correlation. Pedigree (= division orientation) is INDEPENDENT of which centriole goes where. The orientation determines the tissue context → cell fate (Kalbfuss 2023). The centriole is a passenger — but its pedigree records the journey. Randomness of passenger assignment eliminates age as confound.

**Age measurement in C. elegans:** via Dendra2::SAS-4 photoconversion (Erpf & Mikeladze-Dvali 2020). Alternatively, computed from known lineage. Age is a CONTROL variable — not the primary test. Pedigree is the primary predictor. Anderson 2009 (NIH/3T3 mouse cells) demonstrates the principle that age affects function, not a direct C. elegans measurement.

**Question:** does centriole pedigree independently predict fate after controlling for age and cell type? **Null hypothesis:** pedigree does NOT predict fate. Rejecting H₀ = breakthrough.

**Возможный механизм (MCARA/DID):** на центриоли ассоциированы дифференцировочно-индуцирующие факторы (DID). При прохождении узлов траектории DID отщепляются → включение генных сетей → дифференцировка. Centriole pedigree определяет момент и порядок отщепления.

---

## 1. Why C. elegans

| | C. elegans |
|---|:---:|
| Cell lineage | ✅ Complete (959 cells) |
| Division axes | ✅ Fixed (A/P, D/V) |
| ∥/⟂ defined | ✅ Relative to body axis |
| Fates known | ✅ For every cell |

---

## 2. Prediction

**Pedigree (∥/⟂) → centriole fate (retained/eliminated).**

Control: age → function quality (Anderson 2009).

---

## 3. Experiment

| Step | Action |
|:---:|--------|
| 1 | C. elegans embryo, Centrin1-GFP + histone::GFP |
| 2 | Immobilization: microfluidic chip or agarose pad |
| 3 | 3D time-lapse from zygote to ~100 cells (~3h, 30°C) |
| 4 | **Pedigree: continuous 3D angle (not binary).** Full history per centriole. Pilot: validate angle measurement on 5 embryos. |
| 5 | Centriole fate — retained or eliminated |
| 6 | **Mixed-effects logistic regression.** fate ~ angle_3d + age + cell_type + (1|embryo). **VIF test for multicollinearity (age vs angle).** |

---

## 4. Budget

| Item | $ |
|------|--:|
| 60×/1.2 NA WI objective (new) | 8,000 |
| sCMOS camera (Hamamatsu ORCA) | 8,000 |
| 488 nm laser (single-mode) | 2,000 |
| 561 nm laser | 2,000 |
| Light-sheet optics (cyl. lens, scanning mirror, tube lens, dichroics, filters) | 5,000 |
| 3-axis motorized stage + controller | 2,500 |
| Anti-vibration optical table | 3,000 |
| Temperature-controlled enclosure (PID) | 2,000 |
| Microfluidic chip + pressure system | 2,500 |
| **Optical bench: Invar (Fe-36Ni, TER 1.2 — zero drift)** | 3,000 |
| **Frame + stage: Aluminum 7075 (aerospace grade, CNC milled)** | 3,500 |
| **AI agent: Jetson AGX Orin 64GB (275 TOPS) — autonomous control of microscope, manipulators, laser, data pipeline** | 2,500 |
| **Night vision: IR LED 850nm + 2× NoIR cameras** | 500 |
| **Internal surveillance: 2× cameras + LED lighting** | 400 |
| **Glove-box isolator (acrylic, HEPA H13, neoprene gloves)** | 5,000 |
| **Neoprene gloves (spare set) + mounting rings** | 200 |
| **Femtosecond laser NIR 800 nm (Phase 3, optional)** | 15,000 |
| **405 nm laser (Dendra2 photoconversion)** | 800 |
| **Optical tweezers: 2× 1064 nm CW traps (AOD-split) — dual manipulation** | 22,000 |
| **3-axis micromanipulator ×2 + microcapillaries + pneumatic injector — AI-controlled (Jetson AGX)** | 8,000 |
| **Internal shelves (reagents, tools) + UV-C sterilization lamp** | 1,000 |
| C. elegans strains + reagents + consumables | 1,500 |
| Data analysis (compute + software) | 5,000 |
| Contingency (20%) | 15,200 |
| **Total (Phase 1 — Core)** | **~91,000** |
| Femtosecond laser (Phase 3, optional) | +18,000 |
| **Total (all phases)** | **~109,000** |

### Comparison with equivalent systems

| System | Type | 3D time-lapse | Centriole tracking | Open | Price |
|--------|------|:---:|:---:|:---:|--:|
| **LLSM (Betzig)** | Lattice light-sheet | ✅ | ✅ | ❌ | $500K-1M |
| **OpenSPIM** | Light-sheet | ✅ | ❌ | ✅ | $15-25K |
| **Nikon Ti2-E** | Confocal | ✅ | ❌ | ❌ | $80-200K |
| **IncuCyte S3** | Wide-field | ✅ | ❌ | ❌ | $50K |
| **ARGUS V0 (Alex)** | OpenFlexure | ❌ | ❌ | ✅ | **$930** |
| **ARGUS V6** | OpenFlexure | ❌ | ❌ | ✅ | **$3-4K** |
| **ARGUS V7** | OpenFlexure + WI | ✅ | ❌ | ✅ | **$15K** |
| **ARGUS V8** | **Light-sheet + AI** | ✅ | ✅ | ✅ | **$61K** |

> **ARGUS V8 — only open system with 3D time-lapse + centriole tracking. 9× cheaper than LLSM.**

---

## 5. Key References

| # | Reference | PMID |
|---|-----------|------|
| 1 | Sulston & Horvitz (1977) — post-embryonic lineage | 838129 |
| 2 | Sulston et al. (1983) — embryonic lineage | 6684600 |
| 2 | Kalbfuss & Gönczy (2023) — 88% eliminate, Science Advances | 37256957 |
| 3 | Kalbfuss, Berger & Gönczy (2023) — cell fate determines centriole fate, Dev Biol | 37414202 |
| 4 | Gönczy & Balestra (2023) — stochastic segregation | 36988082 |
| 5 | Anderson & Stearns (2009) — age → cilium timing (EXPERIMENTAL, NIH/3T3) | 19682908 |
| 6 | Erpf & Mikeladze-Dvali (2020) — Dendra2::SAS-4 centriole tracking | microPublication |
| 7 | Balestra et al. (2015) — SAS-4::GFP stability in embryos, Cell Research | 25892868 |
| 7 | Yamashita et al. (2007) — Drosophila mGSC | 17255513 |
| 8 | Januschke et al. (2011) — Drosophila NB | 21407209 |
| 9 | Wang et al. (2009) — mouse radial glia | 19829375 |
| 10 | Coffman et al. (2016) — MT asymmetry in C. elegans | — |

> **Marker note:** SAS-4::GFP (Gönczy lab) is validated for centriole tracking in C. elegans. Centrin1-GFP is the alternative. Pilot will compare both.

---

*C. elegans only. Pedigree = ∥/⟂. V8 light-sheet. $35K. 10 refs.*
