# CONCEPT — ARGUS-OS1

**Version:** 143.0
**Date:** 2026-07-21
> **v143:** V7 $81K. Sister-cell primary. All synced.

---

## 0. Hypothesis

**Centriole pedigree (∥/⟂) → centriole fate (retained/eliminated).**

In C. elegans, ~88% of cells eliminate centrioles during embryogenesis. ~68 cells retain them: 41 proliferating + 20 intestinal + 7 terminally differentiated (Kalbfuss & Gönczy 2023, PMID 37256957; EM confirmation in Croisier et al. 2025, PMID 40475707). **Note:** intestinal cells later lose centrioles during endoreduplication (Lu & Roy 2014). Centrioles segregate STOCHASTICALLY at 4-cell stage (Gönczy & Balestra 2023, PMID 36988082) and in ABpr lineage (Erpf & Mikeladze-Dvali 2020). Extrapolated to full embryogenesis — testable in this project.

**Stochastic segregation makes age ORTHOGONAL to pedigree.** If which centriole goes where is random, age and pedigree are statistically independent. This eliminates age as a confound — any observed pedigree↔fate effect must come from the pedigree itself.

**Pedigree definition:** time-ordered sequence of division orientations (3D angles) of all cells the centriole has passed through. Measured via SAS-4::GFP tracking. Age measured via Dendra2::SAS-4 photoconversion (Erpf & Mikeladze-Dvali 2020).

**Two nested hypotheses:**
- **H₁ (known, Kalbfuss 2023):** pedigree correlates with centriole fate THROUGH cell type.
- **H₂ (tested here):** pedigree adds predictive power BEYOND cell type. **Primary test: sister-cell pairs.** When a cell divides symmetrically (same-type daughters — rare in C. elegans, exact frequency to be determined in Pilot), one gets the older centriole, one gets the younger. If their centriole fates diverge, pedigree is the explanation. **Caveat:** most C. elegans divisions are asymmetric (different daughter types). Pilot will quantify available same-type sister pairs.


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
| 3 | 3D time-lapse from zygote to ~100 cells (~3h, **25°C standard**). **Adaptive illumination — not continuous. Dark control: parallel embryos, lasers OFF.** |
| 4 | **Pedigree: continuous 3D angle (not binary).** Full history per centriole. Pilot: validate angle measurement on 5 embryos. |
| 5 | Centriole fate — retained or eliminated |
| 6 | **Primary test: sister-cell pairs.** Compare centriole fate in sister cells — same type, different centriole age/pedigree. Mixed-effects logistic regression. Plan B (whole-population): fate ~ angle_3d + age + cell_type + (1|embryo). |

---

## 4. Budget (ARGUS V7)

| Item | $ |
|------|--:|
| 60×/1.2 NA WI objective (Nikon CFI Plan Apo, new) | 12,000 |
| sCMOS camera (Hamamatsu ORCA-Fusion BT, new) | 15,000 |
| 488 nm LED | 500 |
| Microfluidic chip + pressure system | 2,500 |
| Frame + stage: Aluminum 7075 + thermal stabilization | 4,000 |
| AI: RasPi 5 + Hailo-8L (local tracking) | 350 |
| Night vision: IR LED 850nm + NoIR camera + notch filters | 500 |
| C. elegans strains + reagents + consumables | 1,500 |
| PI salary (25% FTE, 12 months) | 15,000 |
| Engineer salary (50% FTE, 12 months) | 25,000 |
| Lab space rental (Abastumani, 12 months) | 5,000 |
| Contingency (20%) | 16,400 |
| **Total (ARGUS V7)** | **~98,000** |

| 3-axis micromanipulator ×2 + injector — AI-controlled | 8,000 |
| **Total (Phase 3 equipment)** | **~71,000** |
| **Grand total (all phases)** | **~197,000** |

### Comparison with equivalent systems

| System | Type | 3D time-lapse | Centriole tracking | Open | Price |
|--------|------|:---:|:---:|:---:|--:|
| **ARGUS V0 (Alex)** | OpenFlexure | ❌ | ❌ | ✅ | **$930** |
| **ARGUS V6** | OpenFlexure | ❌ | ❌ | ✅ | **$3-4K** |
| **ARGUS V7** | OpenFlexure + WI + sCMOS + AI | ✅ | ✅ | ✅ | **$35K** |

---

## 5. Key References

| # | Reference | PMID |
|---|-----------|------|
| 1 | Sulston & Horvitz (1977) — post-embryonic lineage | 838129 |
| 2 | Sulston et al. (1983) — embryonic lineage | 6684600 |
| 2 | Kalbfuss & Gönczy (2023) — 88% eliminate, cell fate→centriole fate, Sci Adv | 37256957 |
| 3 | Kalbfuss, Berger & Gönczy (2023) — centriolar protein mapping, Dev Biol | 37414202 |
| 4 | Gönczy & Balestra (2023) — stochastic segregation | 36988082 |
| 5 | Anderson & Stearns (2009) — age → cilium timing (EXPERIMENTAL, NIH/3T3) | 19682908 |
| 6 | Erpf & Mikeladze-Dvali (2020) — Dendra2::SAS-4 centriole tracking | microPublication |
| 7 | Balestra et al. (2015) — SAS-4::GFP stability in embryos, Cell Research | 25892868 |
| 7 | Yamashita et al. (2007) — Drosophila mGSC | 17255513 |
| 8 | Januschke et al. (2011) — Drosophila NB | 21407209 |
| 9 | Wang et al. (2009) — mouse radial glia | 19829375 |
| 10 | Coffman et al. (2016) — MT asymmetry in C. elegans, MBoC | 27733624 |
| 11 | Kalbfuss & Gönczy (2023) — centriole elimination review, Open Biol | 37963546 |
| 12 | Croisier et al. (2025) — EM confirms centrioles in rectal cells, microPublication | 40475707 |

> **Marker note:** SAS-4::GFP (Gönczy lab) is validated for centriole tracking in C. elegans. Centrin1-GFP is the alternative. Pilot will compare both.

---

*C. elegans only. Pedigree = 3D angle. V7. $35K HW. 15 refs.*
