# CONCEPT — ARGUS-OS1

****Version:** 154.0
**Date:** 2026-07-22
> **v143:** V7 $81K. Sister-cell primary. All synced.

---

## 0. Hypothesis

### What is KNOWN (literature)

1. ~88% of cells eliminate centrioles during C. elegans embryogenesis. ~68 cells retain them: 41 proliferating + 20 intestinal + 7 terminally differentiated (Kalbfuss & Gönczy 2023, PMID 37256957). EM confirmation: Croisier et al. 2025 (PMID 40475707). **Note:** intestinal cells later lose centrioles during endoreduplication (Lu & Roy 2014, PMID 25360893) — this is post-embryonic loss, distinct from embryonic elimination.
2. Centriole segregation is STOCHASTIC at the 4-cell stage (Gönczy & Balestra 2023, PMID 36988082) and in the ABpr lineage (Erpf & Mikeladze-Dvali 2020). **Whether stochasticity extends to ALL embryonic stages is UNKNOWN** — Pilot P1 tests this directly.
3. Centrioles retained in terminally differentiated cells of the adult somatic gonad likely serve a functional purpose (Gönczy, pers. comm., 21 Jul 2026). **Alternative hypothesis:** retention may reflect ciliary function rather than pedigree — we test this by cross-referencing the 68 retained-cell list against WormAtlas cilial neuron inventory.
4. Centriole elimination in oogenesis initiates with SAS-1 central tube loss (Magescas, Kalbfuss & Gönczy 2023, PMID 37987153) — a potential mechanistic link.

### What is TESTED here (ARGUS hypothesis)

**H₀ (null):** Pedigree does NOT predict centriole fate beyond cell type.

**H₁ (alternative):** Centriole pedigree — the time-ordered sequence of 3D division orientations — predicts centriole fate (retained vs eliminated) independently of cell type.

**Pedigree definition:** 5 quantitative metrics per centriole: (a) fraction of ∥ divisions, (b) mean 3D angle change, (c) angle variance, (d) orientation switches count, (e) cumulative angular path. Reduced to **Pedigree Score** via PCA (first principal component).

**Critical assumption — tested in Pilot P1:** If centriole segregation is stochastic at ALL stages, age and pedigree are orthogonal (Spearman ρ < 0.1). If ρ ≥ 0.1 at any stage, age enters the model as a mandatory covariate and stochasticity is NOT assumed.

**Primary test — sequential 3-stage design:**
- **Stage 1 (all 100 embryos):** Collect pedigree + fate data for ALL cells.
- **Stage 2 (sister pairs):** If ≥40 same-type sister pairs exist → direct test of pedigree effect within identical cell types. **This is the cleanest causal test.**
- **Stage 3 (within-type permutation):** For each cell type with ≥5 cells → **permutation test** (10,000 shuffles): is the observed association between Pedigree Score and centriole fate stronger than random? This avoids distributional assumptions.

**Age measurement:** Dendra2::SAS-4 photoconversion (Erpf & Mikeladze-Dvali 2020). **Requires 405 nm laser** — included in budget. Pilot P1 validates photoconversion efficiency.


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

**H₀:** Pedigree Score does NOT predict centriole fate (retained/eliminated).

**H₁:** Pedigree Score predicts centriole fate independently of cell type, cytoplasm volume (PAR-2 asymmetry), and centriole age.

**Statistical model (Bayesian primary):**
```
fate ~ PedigreeScore + age + PAR2_asymmetry + (1|embryo) + (1|cell_type)
```
**Evidence threshold:** Bayes Factor (BF) > 10 for H₁ vs H₀.
**Frequentist supplement:** Permutation test (10,000 shuffles), α = 0.05 with Bonferroni correction.
**Intermediate analysis:** After 50 embryos. If BF < 3 → increase N to 200. If BF > 10 → stop early (efficiency).

---

## 3. Experiment

### Markers and Strains

| Marker | Purpose |
|--------|--------|
| SAS-4::GFP | Centriole tracking (validated, Gönczy lab) |
| Centrin1::mCherry | Orthogonal centriole marker (cross-validation in P4) |
| Histone::BFP | Nucleus segmentation, cell counting |
| **PAR-2::GFP** | **Cytoplasm asymmetry control.** PAR-2 marks posterior cortex — quantifies cytoplasmic volume asymmetry at each division. Covariate in regression. |
| Dendra2::SAS-4 | Age measurement via photoconversion (Pilot P1). **Requires 405 nm laser.** |
| **spd-2(or165) / plk-1(RNAi)** | **Positive control:** mutants with known centriole loss (spd-2) or duplication failure (plk-1). Replaces gut lineage control. |

> **Idea (Jaba Tqemaladze, 2026-07-21):** Heidenhain's iron haematoxylin — the method Boveri used to discover centrioles in 1900 (Scheer 2014, PMID 25047623). Unlike GFP, it does not require transgenic lines. The centriole retains iron after differentiation, when surrounding structures are already destained.

**Why this matters for ARGUS:**
1. **Routine histological method** — no transgenic constructs required
2. **Stains the entire centriole** — not only proteins (SAS-4, Centrin1) but also the iron-binding core
3. **Independent of GFP** — can verify GFP data with an orthogonal method
4. **$5-10 per sample** — vs $500+ for transgenic lines

**Protocol (adapted for C. elegans whole-mount):**
| Step | Action | Time |
|:---:|---------|:----:|
| 1 | Fixation: Bouin's fluid or 4% PFA + 2.5% glutaraldehyde | 30 min |
| 2 | Permeabilization: freeze-crack or acetone | 10 min |
| 3 | Mordant: 2.5% iron-ammonium alum | 1-12 h |
| 4 | Staining: 0.5% haematoxylin | 1-12 h |
| 5 | Differentiation: 2.5% iron-ammonium alum (microscope control) | 5-30 min |
| 6 | Dehydration + mounting | 30 min |

**Prediction:** Centrioles visible as black dots even in cells where GFP signal of SAS-4/Centrin1 is lost.

**Reference:** Scheer 2014 (PMID 25047623), Fig. 7b.

---

### Pilot Phase (3 months) — Before Main Experiment

| Step | Action |
|:---:|--------|
| P1 | **Stochasticity validation.** Dendra2::SAS-4 photoconversion at 8-, 16-, 32-, 64-cell stages. 10 embryos. **Requires 405 nm laser.** **Go/No-Go:** if Spearman ρ(age, pedigree) ≥ 0.1 at any stage (p < 0.05) → stochasticity NOT assumed → age enters model as mandatory covariate. If ρ ≥ 0.3 → age becomes primary predictor; re-evaluate entire hypothesis. |
| P2 | **Phototoxicity ceiling.** Determine max imaging duration without viability loss. Metrics: division rate, morphology score, hatching rate. Test 488nm + 561nm with 60×/1.2 NA WI at 5-min Z-stack intervals. Find safe duty cycle. |
| P3 | **Photobleaching assay.** Measure SAS-4::GFP signal decay over 3h. If >30% loss → switch to sparse temporal sampling or increase laser power budget. |
| P4 | **Marker cross-validation.** Double transgenic line: Centrin1-GFP + SAS-4::mCherry in same embryos. Confirm both markers track same centrioles. 5 embryos. |
| P5 | **Same-type sister pair quantification.** From Sulston 1983 lineage map: count divisions where both daughters have identical cell type at hatching. If <40 pairs in 100 embryos → switch to Plan C (within-type pedigree comparison, see Analysis). |
| P7 | **Ciliogenesis cross-check.** Compare Kalbfuss (2023) 68 retained-centriole cells against WormAtlas cilial neuron list. If >50% overlap → alternative hypothesis (ciliary retention) cannot be excluded. |

**Pilot Go/No-Go criteria:**
- **P1 (stochasticity):** Spearman ρ(age, pedigree) < 0.1 at ALL stages → age ≈ orthogonal ✅. ρ ≥ 0.1 → age is mandatory covariate ⚠️. ρ ≥ 0.3 → re-evaluate hypothesis 🔴.
- **P2 (phototoxicity):** division rate drop >10% vs dark control → reduce duty cycle or switch to HyD (GaAsP) detector.
- **P3 (photobleaching):** SAS-4::GFP signal decay >30% over 3h → sparse temporal sampling.
- **P5 (sister pairs):** <40 same-type pairs in 100 embryos → Stage 3 (permutation within-type) becomes primary.
- **P7 (ciliogenesis):** >50% overlap with WormAtlas cilial neurons → flag alternative hypothesis; test ciliary marker co-localization.

### Main Experiment — Sequential 3-Stage Design

**Blind protocol:** AI tracker (Jetson AGX Orin) extracts centriole coordinates + cell boundaries + division angles. Pedigree computation is DELAYED — raw trajectory data stored. Human expert classifies centriole fate (retained/eliminated) from final frame WITHOUT access to pedigree data. Pedigree Score computed ONLY after fate classification is locked. Pre-registered on OSF.

| Stage | Action | N |
|:---:|--------|:---:|
| **1** | **Collect ALL data:** 3D time-lapse (zygote→~100 cells, ~3h at 25°C). Adaptive illumination: 2-min interval, Z-stack 21 slices × 0.4 μm. Dark control: parallel embryos, lasers OFF. PAR-2::GFP channel for cytoplasm asymmetry. Phase contrast for cell boundaries. **Negative control:** RNAi-PLK-4 (no centrioles). **Positive control:** spd-2(or165) mutants (known centriole loss). | 100 embryos |
| **2** | **Sister-pair analysis:** If ≥40 same-type pairs → direct test of pedigree effect in genetically+cytoplasmically identical backgrounds. Mixed-effects Bayesian logistic regression. | Subset of Stage 1 |
| **3** | **Within-type permutation test:** For each cell type with ≥5 cells → 10,000 random shuffles of Pedigree Score vs fate. Compute empirical p-value: fraction of shuffled datasets where association ≥ observed. Bonferroni correction across cell types. | All cells from Stage 1 |

**Intermediate analysis:** After 50 embryos. If BF < 3 for H₁ vs H₀ → increase total N to 200. If BF > 10 → stop early. **Primary evidence:** Bayes Factor > 10. **Supplementary:** permutation p < 0.05 after correction.

---

## 4. Budget (ARGUS V7)

| Item | $ |
|------|--:|
| 60×/1.2 NA WI objective (Nikon CFI Plan Apo, new) | 13,500 |
| sCMOS camera (Hamamatsu ORCA-Fusion BT, new) | 18,500 |
| 488 nm LED + 561 nm LED | 800 |
| **405 nm laser (Dendra2 photoconversion, Pilot P1)** | **1,200** |
| Phase contrast condenser + objectives | 2,500 |
| Microfluidic chip + pressure system | 2,500 |
| Frame + stage: Aluminum 7075 + thermal stabilization | 4,000 |
| AI: Jetson AGX Orin 64GB (275 TOPS, local tracking) | 2,000 |
| Night vision: IR LED 850nm + NoIR camera + notch filters | 500 |
| C. elegans strains (PAR-2::GFP, Dendra2::SAS-4, spd-2, RNAi) + reagents | 4,000 |
| PI salary (25% FTE, 12 months) | 15,000 |
| Engineer salary (50% FTE, 12 months) | 30,000 |
| Lab space rental (Abastumani, 12 months) | 5,000 |
| Contingency (30%) | 30,000 |
| **Hardware subtotal** | **~48,500** | |
| Personnel + lab | 50,000 |
| Contingency (30%) | 30,000 |
| **Total (ARGUS V7)** | **~128,500** |

| 3-axis micromanipulator ×2 + injector — AI-controlled | 8,000 |
| **Total (Phase 3 equipment)** | **~71,000** |
| **Grand total (all phases)** | **~225,000** |

### Comparison with equivalent systems

| System | Type | 3D time-lapse | Centriole tracking | Open | Price |
|--------|------|:---:|:---:|:---:|--:|
| **ARGUS V0 (Alex)** | OpenFlexure | ❌ | ❌ | ✅ | **$930** |
| **ARGUS V6** | OpenFlexure | ❌ | ❌ | ✅ | **$3-4K** |
| **ARGUS V7** | OpenFlexure + WI + sCMOS + AI + phase | ✅ | ✅ | ✅ | **$47K (HW)** |

---

## 5. Key References

**Reproducibility:** All code, protocols, and raw data on GitHub + Zenodo (CC-BY). Protocol on bioRxiv before data collection. **Data:** Raw images → BioImage Archive. Processed → Zenodo. Code → GitHub. **Independent replication:** N2 strain (baseline) + CB4856 (Hawaiian) for cross-strain validation. **Timeline:** Pilot (2 months) → Main (4 months) → Analysis (2 months). **Biosafety:** BSL-1. C. elegans — non-pathogenic. 488nm LED — class 1 laser product.

**Limitations:** (1) Stochasticity NOT assumed — Pilot P1 tests all stages; ρ ≥ 0.1 → age mandatory covariate. (2) Sister-cell pairs rare (~5%) — Stage 2 quantifies; Stage 3 (permutation) is primary if <40 pairs. (3) Ciliogenesis alternative: Pilot P7 cross-references WormAtlas cilial neurons; >50% overlap flags retention-for-cilia hypothesis. (4) C. elegans-specific — requires cross-species validation. (5) Multicollinearity: Pedigree Score (PCA) reduces 5 metrics → 1 dimension; VIF monitored. (6) Phototoxicity: Pilot P2 determines safe duty cycle; HyD (GaAsP) detector recommended for 10× lower laser power. (7) Heidenhain haematoxylin: Pilot validates with anti-SAS-4 co-stain + RNAi-PLK-4 negative control (no centrioles = no black dots). (8) Multiple testing: Bonferroni correction (α/N_cell_types) + FDR (Benjamini-Hochberg, q < 0.05). (9) Positive control: spd-2(or165)/plk-1(RNAi) mutants replace gut lineage (endomitosis ≠ embryonic elimination). Pre-registered: OSF.

| # | Reference | PMID |
|---|-----------|------|
| 1 | Sulston & Horvitz (1977) — post-embryonic lineage | 838129 |
| 2 | Sulston et al. (1983) — embryonic lineage | 6684600 |
| 3 | Kalbfuss & Gönczy (2023) — 88% eliminate, cell fate→centriole fate, Sci Adv | 37256957 |
| 4 | Kalbfuss, Berger & Gönczy (2023) — centriolar protein mapping, Dev Biol | 37414202 |
| 5 | Gönczy & Balestra (2023) — stochastic segregation | 36988082 |
| 6 | Anderson & Stearns (2009) — age → cilium timing (EXPERIMENTAL, NIH/3T3) | 19682908 |
| 7 | Erpf & Mikeladze-Dvali (2020) — Dendra2::SAS-4 centriole tracking | DOI:10.17912/micropub.biology.000286 |
| 8 | Balestra et al. (2015) — paternal centrioles persist in C. elegans embryos, Cell Research | 25906994 |
| 9 | Yamashita et al. (2007) — Drosophila mGSC | 17255513 |
| 10 | Januschke et al. (2011) — Drosophila NB | 21407209 |
| 11 | Wang et al. (2009) — mouse radial glia | 19829375 |
| 12 | Coffman et al. (2016) — MT asymmetry in C. elegans, MBoC | 27733624 |
| 13 | Kalbfuss & Gönczy (2023) — centriole elimination review, Open Biol | 37963546 |
| 14 | Croisier et al. (2025) — EM confirms centrioles in rectal cells, microPublication | 40475707 |
| 15 | Lu & Roy (2014) — centriole loss in intestine during endoreduplication | 25360893 |
| 16 | Magescas, Kalbfuss & Gönczy (2023) — centriole elimination in oogenesis: SAS-1 loss initiates, EMBO J | 37987153 |
| 17 | Woglar, Gönczy et al. (2022) — molecular architecture of C. elegans centriole, PLoS Biol | 36107993 |
| 18 | Serwas, Gönczy et al. (2025) — SAS-1 ensures centriole integrity, PLoS Genet | 41124206 |

> **Marker note:** SAS-4::GFP (Gönczy lab) validated for centriole tracking. Centrin1-GFP alternative. Pilot compares both. Balestra (2015, PMID 25906994) confirms paternal centrioles persist — GFP signal stable through embryogenesis. Magescas (2023, PMID 37987153): centriole elimination initiates with SAS-1 loss — potential mechanistic link to pedigree.

---

*C. elegans only. Pedigree Score (PCA). V7. $128.5K. 18 refs. Bayesian primary (BF>10). Sequential 3-stage design. Pilot with Go/No-Go.*
