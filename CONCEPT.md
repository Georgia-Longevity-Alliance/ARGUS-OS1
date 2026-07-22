# CONCEPT — ARGUS-OS1

**Version:** 158.0
**Date:** 2026-07-22

---

## 0. Hypothesis

### What is KNOWN (literature)

1. ~88% of cells eliminate centrioles by the **comma stage** of C. elegans embryogenesis. ~68 cells retain them at that stage (Kalbfuss & Gönczy 2023, PMID 37256957). **Timing gap:** our imaging window (zygote→~100 cells, ~3h) ends BEFORE comma stage. Cells classified as "retained" at 100-cell stage may eliminate centrioles later. **We measure "retained at 100-cell window" — a snapshot, not final fate.**
2. Centriole segregation is STOCHASTIC at the 4-cell stage (Gönczy & Balestra 2023, PMID 36988082) and ABpr lineage (Erpf & Mikeladze-Dvali 2020). Full-embryogenesis stochasticity is TESTED in Pilot P1 (NOT assumed).
3. E-lineage (intestinal) cells lose centrioles during post-embryonic endoreduplication (Lu & Roy 2014, PMID 25360893). These cells RETAIN centrioles throughout our imaging window. **They are EXCLUDED from the primary analysis.** A secondary analysis examines them separately.
4. ~12% of embryonic cells undergo programmed cell death (Sulston 1983 lineage). Apoptotic centriole loss is passive degradation, NOT pedigree-driven elimination. **Apoptotic cells are EXCLUDED** via CED-3::mCherry marker.
5. Centriole elimination in oogenesis initiates with SAS-1 central tube loss (Magescas et al. 2023, PMID 37987153). **SAS-1::mCherry serves as an early marker** — SAS-1 disappearance precedes SAS-4 loss, providing an early signal of impending elimination. **Caveat:** Magescas (2023) studied primarily oocytes; somatic applicability tested in Pilot P6.
6. PCM (pericentriolar material) disassembles BEFORE the centriole core disappears (O'Toole et al. 2003, PMID 14610052). SAS-4::GFP visualizes the core but NOT PCM. A "GFP-positive" centriole may be biologically inactive. **We track both SAS-4 (core) and SAS-1 (tube integrity) as complementary fate markers.**
7. PAR proteins (PAR-2, PAR-3, PAR-6) establish cortical asymmetry and influence spindle orientation in early C. elegans embryos. **PAR-2::GFP + PAR-3::mCherry** quantify both posterior and anterior cytoplasmic asymmetry at each division.

### What is TESTED here (ARGUS hypothesis)

**H₀ (null):** Pedigree Score does NOT predict centriole fate beyond cell type, cytoplasm asymmetry, and age.

**H₁ (alternative):** Pedigree Score — a PCA composite of 5 division-orientation metrics — independently predicts whether a centriole is retained or eliminated at the 100-cell window.

**Pedigree Score (PCA):** (a) fraction ∥ divisions, (b) mean 3D angle change, (c) angle variance, (d) orientation switches, (e) cumulative angular path → first principal component.

**Primary test — Bootstrap Mixed Model (fixed N=100 embryos):**
```
fate ~ PedigreeScore + age + time_since_last_division + mother_daughter + lineage(E_vs_nonE) + PAR2 + PAR3 + (1|embryo) + (1|cell_lineage)
```
Bootstrap: 1,000 embryo resamples. **Power: recalculated with ICC.** BF>10, β<0.1.
**Priors:** Student-t(3,0,1) fixed effects (regularizing). Half-Student-t(3,0,2.5) random.
**NO intermediate stopping.** Fixed N=100.

**Comma-stage validation (N=20 embryos):** Extended imaging (+2h, ~200→350 cells) for a subset to verify that 100-cell PedigreeScore predicts final comma-stage elimination. **Critical for surrogate endpoint validation.**

**Inter-rater reliability:** Two independent classifiers (human + AI). **Cohen's Kappa ≥ 0.85 required.** Below threshold → third arbitrator.

**E-lineage strategy:** INCLUDED as factor `lineage(E_vs_nonE)`, NOT excluded. Test PedigreeScore × lineage interaction. If significant → lineage-specific models.

**Fate classification (3 categories):**
- **Early eliminators:** centriole lost ≤100-cell window
- **Late eliminators:** centriole retained at 100 cells, lost by extended imaging (+2h, ~200 cells)
- **Permanent retainers:** centriole present at 200+ cells
**Primary outcome:** binary (retained vs eliminated at 100 cells). **Secondary:** 3-category ordinal model.

**Mother/daughter centriole tracking:** In each division, the older (mother) centriole is identified by Dendra2::SAS-4 signal ratio (older = dimmer, more photoconverted protein diluted). **Mother/daughter status added as fixed effect.**

**Sensitivity — Sister pairs:** If ≥40 same-type pairs → within-pair comparison (secondary).

---

## 1. Why C. elegans

| Feature | Value |
|---------|-------|
| Cell lineage | Complete (959 cells), every division axis known |
| Division axes | Fixed (A/P, D/V) — ∥/⟂ objectively defined |
| Fates known | For every cell (Sulston 1983, PMID 6684600) |
| Apoptosis map | Known (Sulston 1983) — excludable a priori |
| Centriole fate map | ~88% eliminate by comma stage (Kalbfuss 2023) |

---

## 2. Prediction

**H₀:** Pedigree Score does NOT predict centriole fate.

**H₁:** Pedigree Score predicts centriole fate independently of cell type, lineage (E vs non-E), cytoplasm asymmetry (PAR-2, PAR-3), centriole age, and mother/daughter status.

**Statistical model (Bayesian, brms with weakly informative priors):**
```
fate ~ PedigreeScore + age + mother_daughter + lineage(E_vs_nonE) + PAR2 + PAR3 + (1|embryo) + (1|cell_lineage)
```
**Priors (brms, pre-registered):** Fixed effects ~ **Student-t(3, 0, 1)** (regularizing — avoids OR inflation of Normal(0,1)). Random effects ~ Half-Student-t(3, 0, 2.5). **ICC:** intra-class correlation for lineage random effect reported; power recalculated accounting for ICC.
**Evidence:** BF > 10 (α=0.05 threshold equivalent) for H₁ vs H₀ (primary: SAS-4 outcome). **Secondary (SAS-1):** FDR (Benjamini-Hochberg, q<0.05).
**Fixed N=100. NO intermediate stopping.**

---

## 3. Experiment

### Markers and Strains

| Marker | Purpose |
|--------|--------|
| SAS-4::GFP | Centriole core tracking (validated, Gönczy lab) |
| **SAS-1::mCherry** | **Early marker: central tube loss precedes SAS-4 loss (Magescas 2023, oocytes; somatic validation in P6)** |
| Centrin1::BFP | Orthogonal centriole marker (cross-validation P4) |
| Dendra2::SAS-4 | Age measurement via photoconversion (Pilot P1). **405 nm laser required.** |
| PAR-2::GFP + **PAR-3::mCherry** | Cytoplasm asymmetry: posterior + anterior cortex |
| **CED-3::mCherry** | **Apoptosis marker: exclude dying cells** |
| Histone::CFP | Nucleus segmentation |
| spd-2(or165) / plk-1(RNAi) | Positive control: centriole loss mutants |

### Iron-Based Centriole Detection (Heidenhain's Haematoxylin)

> **Idea (Jaba Tqemaladze, 2026-07-21):** Heidenhain's iron haematoxylin — the method Boveri used to discover centrioles in 1900 (Scheer 2014, PMID 25047623). Serves as **endpoint validation**, NOT live tracking. Fixed embryos at 100-cell stage → stain → compare with final GFP frame. Confirms that GFP-positive structures are centrioles, not aggregates.

**Protocol (C. elegans whole-mount):**
| Step | Action | Time |
|:---:|---------|:----:|
| 1 | Fixation: 4% PFA + 2.5% glutaraldehyde | 30 min |
| 2 | Permeabilization: freeze-crack | 10 min |
| 3 | Mordant: 2.5% iron-ammonium alum | 1-12 h |
| 4 | Staining: 0.5% haematoxylin | 1-12 h |
| 5 | Differentiation: 2.5% iron-ammonium alum (microscope control until background clear) | 5-30 min |
| 6 | Dehydration + mounting | 30 min |

**Negative control:** RNAi-PLK-4 embryos (no centrioles → no black dots). **Reference:** Scheer 2014 (PMID 25047623).

---

### Pilot Phase (3 months)

| Step | Action |
|:---:|--------|
| P1 | **Stochasticity validation.** Dendra2::SAS-4 photoconversion at 8-, 16-, 32-, 64-cell stages. 10 embryos. **405 nm laser.** **Non-photoconverted control:** 5 embryos with Dendra2 but NO 405nm exposure — same imaging otherwise. If aberrant divisions >5% in photoconverted vs control → method invalid. **Go/No-Go:** Spearman ρ(age, pedigree) < 0.1 at ALL stages → age≈orthogonal ✅. ρ ≥ 0.1 → age mandatory covariate ⚠️. ρ ≥ 0.3 → re-evaluate hypothesis 🔴. |
| P2 | **Phototoxicity ceiling.** Test 488/561/405nm at 2-min vs 5-min intervals. Metrics: division rate, morphology, hatching rate. **Go/No-Go:** if division rate drops >10% at 2-min interval → switch to 5-min interval OR upgrade to light-sheet (V8). |
| P3 | **Photobleaching assay.** SAS-4::GFP + SAS-1::mCherry signal decay over 3h. >30% loss → sparse sampling or light-sheet. |
| P4 | **Marker cross-validation.** SAS-4::GFP + SAS-1::mCherry + Centrin1::BFP in same embryos. Confirm co-localization. 5 embryos. |
| P5 | **Sister-pair quantification.** From Sulston 1983: count same-type sister pairs. **This is sensitivity analysis, not primary test.** |
| P6 | **SAS-1→SAS-4 latency measurement.** In 10 embryos, measure time (minutes) between SAS-1::mCherry loss and SAS-4::GFP loss for ≥50 centrioles across cell types. **Go/No-Go:** if latency variance across cell types >2-fold → latency must be modeled as cell-type-specific. If mean latency <5 min → SAS-1 and SAS-4 loss are near-simultaneous (surrogate invalid). |
| P7 | **Ciliogenesis cross-check + exclusion validation.** Compare Kalbfuss 68 vs WormAtlas cilial neurons. >50% overlap → flag. Also validate CED-3::mCherry + histone::CFP morphology against Sulston 1983 apoptosis map. |
| P8 | **Mother/daughter identification.** Validate Dendra2::SAS-4 signal ratio: older centriole = dimmer (diluted photoconverted protein). Compare with lineage-based age prediction. 5 embryos. |

**Go/No-Go criteria:**
- P1: ρ < 0.1 ✅ | ρ ≥ 0.1 ⚠️ | ρ ≥ 0.3 🔴
- P2: division rate >90% of dark control at chosen interval ✅ | <90% → 5-min interval or light-sheet
- P3: signal decay <30% over 3h ✅
- P5: ≥40 same-type pairs → sensitivity analysis viable
- P6: mean SAS-1→SAS-4 latency <30 min across cell types ✅ | >30 min or >2-fold variance → cell-type-specific model | <5 min → surrogate invalid 🔴
- P7: CED-3 + histone morphology correctly identifies apoptotic cells ✅ | >50% WormAtlas overlap → flag ciliogenesis alternative
- P8: Dendra2 ratio correctly identifies mother in >90% of divisions ✅

---

### Main Experiment — Bootstrap Mixed Model Design

**Blind protocol:** AI tracker extracts coordinates + boundaries + angles. Pedigree computation DELAYED. Human classifies centriole fate (SAS-4 retained/lost, SAS-1 retained/lost — TWO binary outcomes) from final frame WITHOUT pedigree data. Pedigree Score computed only after classification locked. OSF pre-registered.

| Stage | Action | N |
|:---:|--------|:---:|
| **1** | **Collect ALL data.** 3D time-lapse: zygote→~100 cells, ~3h at 25°C. Adaptive illumination: 2-min intervals (5-min if P2 fails). Z-stack 21 slices × 0.4 μm. **Light-sheet (V8) strongly recommended** — reduces phototoxicity ×10 vs widefield. PAR-2 + PAR-3 channels. CED-3 channel. Phase contrast for boundaries. **Negative control:** RNAi-PLK-4. **Positive control:** spd-2(or165). | 100 embryos |
| **2** | **Bootstrap Mixed Model (PRIMARY).** Fate ~ PedigreeScore + age + PAR2 + PAR3 + (1|embryo) + (1|lineage). 1,000 bootstrap resamples of embryos. **Bayesian BF>10.** **Exclusion:** E-lineage cells, CED-3(+) apoptotic cells, cells with <3 timepoints. **Outcome variables:** (a) SAS-4 retention, (b) SAS-1 retention (early signal of impending elimination). | ~6,800 centrioles after exclusions |
| **3** | **Sister-pair sensitivity analysis.** If ≥40 same-type pairs → within-pair comparison. Secondary, not required for conclusions. | Subset of Stage 1 |
| **4** | **E-lineage secondary analysis.** Intestinal cells separately: does Pedigree Score predict which cells lose centrioles during endoreduplication? Post-embryonic follow-up (additional 2h imaging at L1 stage). | E-lineage cells only |
| **5** | **SAS-1 vs SAS-4 discordance.** Cells where SAS-1 is lost but SAS-4 persists → "centriole committed to elimination." Test whether Pedigree Score predicts SAS-1 loss EARLIER than SAS-4 loss. | All cells |

**Intermediate analysis:** After 50 embryos. BF<3 → N=200. BF>10 → stop.

---

## 4. Budget (ARGUS V7 + V8 light-sheet)

| Item | $ |
|------|--:|
| 60×/1.2 NA WI objective (Nikon CFI Plan Apo) | 13,500 |
| sCMOS camera (Hamamatsu ORCA-Fusion BT) | 18,500 |
| 405 nm laser (Dendra2 photoconversion) | 1,200 |
| 488 nm + 561 nm + 640 nm LED/lasers | 1,500 |
| **Light-sheet module (V8) — MANDATORY** (Keller et al. 2008, PMID 18845710: 10-100× lower phototoxicity) | 8,000 |
| **Light-sheet delivery + installation + calibration** | 3,000 |
| Phase contrast condenser + objectives | 2,500 |
| Microfluidic chip + pressure system | 2,500 |
| Frame + stage: Aluminum 7075 + thermal stabilization | 4,000 |
| AI: Jetson AGX Orin 64GB (275 TOPS) | 2,000 |
| Night vision: IR LED + NoIR + notch filters | 500 |
| C. elegans strains (7 markers + RNAi + mutants) + reagents | 5,500 |
| PI salary (25% FTE, 12 months) | 15,000 |
| Engineer salary (50% FTE, 12 months) | 30,000 |
| Lab space rental (Abastumani, 12 months) | 5,000 |
| Contingency (25%) | 27,000 |
| **Hardware subtotal** | **~62,700** |
| Personnel + lab | 50,000 |
| Contingency (25%) | 27,000 |
| **Total (ARGUS V7+V8)** | **~140,000** |

---

## 5. Key References

| # | Reference | PMID |
|---|-----------|------|
| 1 | Sulston & Horvitz (1977) — post-embryonic lineage | 838129 |
| 2 | Sulston et al. (1983) — embryonic lineage + apoptosis map | 6684600 |
| 3 | Kalbfuss & Gönczy (2023) — 88% eliminate, cell fate→centriole fate, Sci Adv | 37256957 |
| 4 | Kalbfuss, Berger & Gönczy (2023) — centriolar protein mapping, Dev Biol | 37414202 |
| 5 | Gönczy & Balestra (2023) — stochastic segregation at 4-cell stage | 36988082 |
| 6 | Anderson & Stearns (2009) — centriole age → cilium timing (NIH/3T3) | 19682908 |
| 7 | Erpf & Mikeladze-Dvali (2020) — Dendra2::SAS-4 tracking, ABpr lineage | DOI:10.17912/micropub.biology.000286 |
| 8 | Balestra et al. (2015) — paternal centrioles persist, Cell Research | 25906994 |
| 9 | Yamashita et al. (2007) — Drosophila mGSC asymmetric inheritance | 17255513 |
| 10 | Januschke et al. (2011) — Drosophila NB daughter centrosome | 21407209 |
| 11 | Wang et al. (2009) — mouse radial glia asymmetric inheritance | 19829375 |
| 12 | Coffman et al. (2016) — MT asymmetry in C. elegans, MBoC | 27733624 |
| 13 | Kalbfuss & Gönczy (2023) — centriole elimination review, Open Biol | 37963546 |
| 14 | Croisier et al. (2025) — EM confirms centrioles in rectal cells | 40475707 |
| 15 | Lu & Roy (2014) — centriole loss in gut endoreduplication | 25360893 |
| 16 | Magescas, Kalbfuss & Gönczy (2023) — SAS-1 loss initiates elimination, EMBO J | 37987153 |
| 17 | Woglar, Gönczy et al. (2022) — centriole molecular architecture, PLoS Biol | 36107993 |
| 18 | Serwas, Gönczy et al. (2025) — SAS-1 integrity, PLoS Genet | 41124206 |
| 19 | **O'Toole et al. (2003)** — MT ends in mitotic centrosome of C. elegans, J Cell Biol | 14610052 |
| 20 | Weaver et al. (2017) — miRNAs in apoptosis, C. elegans development, Genes Dev | 28167500 |
| 21 | **Keller et al. (2008)** — light-sheet microscopy for embryo development, Science | 18845710 |
| 22 | **Feldman & Priess (2012)** — centrosome + PAR-3 in MTOC hand-off, epithelial polarization, Curr Biol | 22425160 |
| 23 | **Mikeladze-Dvali et al. (2012)** — centriole elimination during C. elegans oogenesis, Development | 22492357 |
| 24 | **Cabernard & Doe (2009)** — spindle orientation in Drosophila neuroblast homeostasis, Dev Cell | 19619498 |

---

**Exclusion criteria:** E-lineage (gut) + CED-3(+) apoptotic cells + <3 timepoints.
**Primary:** Bootstrap Mixed Model, BF>10.
**Sensitivity:** Sister pairs. **Surrogate:** SAS-1 loss before SAS-4.
**Timing note:** 100-cell window snapshot — NOT comma stage. Late eliminators flagged.
**V8 light-sheet strongly recommended** for phototoxicity ceiling.
*24 refs. V7+V8 mandatory. $140K. Student-t priors. Comma-stage validation (N=20). Cohen's Kappa ≥0.85.*

---

**Limitations:** (1) 100-cell window ≠ comma stage — 3-category fate (early/late/permanent) as secondary analysis. (2) E-lineage INCLUDED as factor with interaction test, not excluded. (3) CED-3 + histone morphology for apoptosis exclusion. (4) SAS-1 latency measured in Pilot P6; <5 min invalidates surrogate. (5) V8 light-sheet MANDATORY (Keller 2008: 10-100× lower phototoxicity vs widefield). (6) PCM loss before core (O'Toole 2003) — some GFP+ centrioles may be inactive. (7) Mother/daughter identified via Dendra2 ratio (Pilot P8). (8) Multiple testing: BF>10 for SAS-4 (primary), FDR (q<0.05) for SAS-1 (secondary). Fixed N=100, NO sequential stopping. Pre-registered: OSF (brms priors specified).
