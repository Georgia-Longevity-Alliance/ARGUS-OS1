# CONCEPT — ARGUS-OS1

**Version:** 175.0
**Date:** 2026-07-22

---

## 0. Hypothesis

### What is KNOWN (literature)

1. ~88% of cells eliminate centrioles by the **comma stage** of C. elegans embryogenesis. ~68 cells retain them at that stage (Kalbfuss & Gönczy 2023, PMID 37256957). **Timing gap:** our imaging window (zygote→~100 cells, ~3h) ends BEFORE comma stage. Cells classified as "retained" at 100-cell stage may eliminate centrioles later. **We measure "retained at 100-cell window" — a snapshot, not final fate.**
2. Centriole segregation is STOCHASTIC at the 4-cell stage (Gönczy & Balestra 2023, PMID 36988082) and ABpr lineage (Erpf & Mikeladze-Dvali 2020). Full-embryogenesis stochasticity is TESTED in Pilot P1 (NOT assumed).
3. E-lineage (intestinal) cells lose centrioles during post-embryonic endoreduplication (Lu & Roy 2014, PMID 25360893). **EXCLUDED from primary analysis** (different elimination mechanism). Separate secondary analysis on E-lineage only.
4. ~17% (113/671 cells) undergo programmed cell death (Sulston 1983). **EXCLUDED via CED-3::mKate2 (588nm)** (competing risk in Cause-Specific Hazards model).
5. Centriole elimination in oogenesis initiates with SAS-1 central tube loss (Magescas et al. 2023, PMID 37987153). **SAS-1::miRFP670 (670nm, far-red, NO GFP overlap) serves as an early marker** — SAS-1 disappearance precedes SAS-4 loss, providing an early signal of impending elimination. **Caveat:** Magescas (2023) studied primarily oocytes; somatic applicability tested in Pilot P6.
6. Based on OToole (2003) centriole ultrastructure and Magescas (2023) SAS-1 dynamics, we HYPOTHESIZE PCM disassembles before the core. Tested via SPD-2::mCherry (PCM). Note: Fu & Glover (2012, Drosophila) place SPD-2 at centriole-PCM interface — C. elegans localization may differ. SPD-5 as alternative PCM marker in 5 embryos., PMID 14610052). SAS-4::GFP visualizes the core but NOT PCM. A "GFP-positive, PCM-negative" centriole is a ZOMBIE — structurally present, biologically dead. **Primary outcome: composite fate = (SAS-4+ AND SPD-2+). Loss of EITHER for >30 min = eliminated (Bobinnec (1998): centriole disassembly possible in vivo (HeLa cells, 12h timescale). 30-min threshold is empirically chosen: >2 imaging intervals ensures loss is NOT a transient focal plane artifact. Validated in Pilot P3.).** This eliminates misclassification of zombie centrioles as "retained." SPD-2::mCherry tracked in ALL N=100. Exploratory: AIR-1::GFP in 20 embryos (Plourde 2025 — direct centrosome asymmetry measure). embryos.
7. PAR proteins (PAR-2, PAR-3, PAR-6) establish cortical asymmetry and influence spindle orientation in early C. elegans embryos. **PAR-2::GFP + PAR-3::mCherry** quantify both posterior and anterior cytoplasmic asymmetry at each division.

### What is TESTED here (ARGUS hypothesis)

**H₀ (null):** Pedigree Score does NOT predict centriole fate beyond cell type, cytoplasm asymmetry, and age.

**H₁ (alternative):** Pedigree Score — a PCA composite of 5 division-orientation metrics — independently predicts whether a centriole is retained or eliminated at the 100-cell window.

**Pedigree Score (PCA):** (a) fraction ∥ divisions, (b) mean 3D angle change, (c) angle variance, (d) orientation switches, (e) cumulative angular path → first principal component.
**Operational definitions:** (a) fraction ∥ = count(∥ divisions)/total divisions, where ∥ = angle between division axis and A-P axis <30°. (b) Mean 3D angle = mean(arccos(|v₁·v₂|)) between consecutive divisions. (c) Angle variance = var(angles). (d) Orientation switches = count of ∥→⟂ or ⟂→∥ transitions. (e) Cumulative angular path = Σ arccos(|vᵢ·vᵢ₊₁|). All computed in embryo-centered coordinates. **PCA:** first principal component across 5 standardized metrics, computed per-embryo then pooled.

**Primary test — Sister-cell pairs (eliminates ICC):**
When a cell divides, one daughter gets the older centriole, one the younger. Both inherit identical cell type, cytoplasm, and lineage. **Pedigree difference IS the only systematic difference.** This is the cleanest causal design.

**ICC power calculation:** For N=100 embryos with ~68 centrioles each, ICC≈0.3 → N_eff = 100/(1+67×0.3) ≈ 4.7. **Within-embryo mixed models have <20% power for OR=1.2.** Sister-pair design eliminates ICC. PAR-2/PAR-3 ratio included as within-pair covariate (daughters are not cytoplasmically identical)..

**Secondary — Bootstrap Mixed Model (all cells):**
```
fate ~ PedigreeScore + age + time_since_last_division + mother_daughter + PAR2 + PAR3 + (1|embryo/lineage)
```
Exploratory. ICC-adjusted confidence intervals reported.

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

**Statistical model — Joint Model (longitudinal + survival):**
```
Longitudinal: SAS4_intensity(t) ~ PedigreeScore + age + time + (1+time|embryo)
Survival:    time_to_composite_loss ~ PedigreeScore + age + PAR_ratio + frailty(embryo)
```
**Composite fate:** loss of SAS-4::GFP OR SPD-2::mCherry below threshold. Eliminates zombie misclassification.
**Joint model** uses ALL intensity data (not just binary endpoint), increasing power ~2× vs Cox alone.
**Fine-Gray** for competing risk of apoptosis (CED-3+).
**Package:** `JMbayes2` (R). Priors: Normal(0,1) fixed, Half-Cauchy(0,2.5) random.
**Power:** N=100, ~50 cells/embryo, joint model → >80% power for HR≥1.3 at α=0.05.
**Evidence:** BF > 10 (α=0.05 threshold equivalent) for H₁ vs H₀ (primary: SAS-4 outcome). **Secondary (SAS-1):** FDR (Benjamini-Hochberg, q<0.05).
**Fixed N=100. NO intermediate stopping.**

---

## 3. Experiment

### Markers and Strains

| Marker | Purpose |
|--------|--------|
| SAS-4::GFP | Centriole core tracking (validated, Gönczy lab) |
| **SAS-1::miRFP670 (670nm, far-red, NO GFP overlap)** | **Early marker: central tube loss precedes SAS-4 loss (Magescas 2023, oocytes; somatic validation in P6)** |
| Centrin1::BFP | Orthogonal centriole marker (cross-validation P4) |
| Dendra2::SAS-4 | Age measurement via photoconversion (Pilot P1). **405 nm laser required.** |
| **PAR-2/PAR-3 ratio** (PAR-2::GFP + PAR-3::mCherry) | Cortical asymmetry index |
| **CED-3::mKate2 (588nm)** | Apoptosis: competing risk in Cause-Specific Hazards model |
| **SPD-2::mCherry** (561nm) | PCM marker: functional vs zombie. ALL N=100 embryos. Distinct λ from SAS-4::GFP (488nm). |
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
| P1 | **Stochasticity + depth.** Ratiometric normalization: SAS-4::GFP / Histone::CFP per cell. Eliminates depth×lineage confounding. Dendra2::SAS-4 photoconversion at 8-, 16-, 32-, 64-cell stages. 10 embryos. **Z-depth calibration:** brightness vs depth (μm). If depth >20% variance → covariate. **Non-UV control:** 5 embryos, NO 405nm. ρ < 0.1 ✅ | ρ ≥ 0.1 ⚠️ | ρ ≥ 0.3 🔴 |
| P2 | **Phototoxicity ceiling.** Test 488/561/405nm at 2-min vs 5-min intervals. Metrics: division rate, morphology, hatching rate. **Go/No-Go:** if division rate drops >10% at 2-min interval → switch to 5-min interval OR upgrade to light-sheet (V8). |
| P3 | **Photobleaching assay.** SAS-4::GFP + SAS-1::miRFP670 (670nm, far-red, NO GFP overlap) signal decay over 3h. >30% loss → sparse sampling or light-sheet. |
| P4 | **Marker cross-validation.** SAS-4::GFP + SAS-1::miRFP670 (670nm, far-red, NO GFP overlap) + Centrin1::BFP in same embryos. Confirm co-localization. 5 embryos. |
| P5 | **Sister-pair quantification.** From Sulston 1983: count same-type sister pairs. **This is PRIMARY test candidate pool.** |
| P6 | **SAS-1→SAS-4 latency + oogenesis comparison.** Compare somatic latency with published oogenesis data (Pierron 2023: SAS-1 lost in -10 oocyte). Test SPD-5 as alternative early PCM marker. In 10 embryos, measure time (min) between SAS-1::miRFP670 (670nm, far-red, NO GFP overlap) loss and SAS-4::GFP loss for ≥50 centrioles. **Validity thresholds:** (a) mean latency <15 min, (b) variance <30% of mean, (c) latency predicts SAS-4 loss in >80% of cells. If ALL three met → SAS-1 is valid surrogate. Otherwise → descriptive only. |
| P7 | **Ciliogenesis cross-check + exclusion validation.** Compare Kalbfuss 68 vs WormAtlas cilial neurons. >50% overlap → flag. Also validate CED-3::mKate2 (588nm) + histone::CFP morphology against Sulston 1983 apoptosis map. |
| P8 | **Mother/daughter identification.** Validate Dendra2::SAS-4 signal ratio: older centriole = dimmer (diluted photoconverted protein). Compare with lineage-based age prediction. 5 embryos. |

**Go/No-Go criteria:**
- P1: ρ < 0.1 ✅ | ρ ≥ 0.1 ⚠️ | ρ ≥ 0.3 🔴
- P2: division rate >90% of dark control at chosen interval ✅ | <90% → 5-min interval or light-sheet
- P3: signal decay <30% over 3h ✅
- P5: ≥40 same-type pairs → sensitivity analysis viable
- P6: ≥2 of 3 validity criteria met → SAS-1 valid surrogate | <2 criteria → descriptive only 🔴
- P7: CED-3 + histone morphology correctly identifies apoptotic cells ✅ | >50% WormAtlas overlap → flag ciliogenesis alternative
- P8: Dendra2 ratio correctly identifies mother in >90% of divisions ✅

---

### Main Experiment — Bootstrap Mixed Model Design

**Blind protocol:** AI tracker extracts coordinates + tracks centrioles across frames. Pedigree Score computation DELAYED until human classification complete. Human classifies centriole fate from FULL time series (all frames) but WITHOUT Pedigree Score overlay. Pedigree Score computed only after fate classification locked. Pedigree Score computed only after classification locked. OSF pre-registered.

| Stage | Action | N |
|:---:|--------|:---:|
| **1** | **Collect ALL data.** 3D time-lapse: zygote→~100 cells, ~3h at 25°C. Adaptive illumination: 1-min intervals for primary (capture fast elimination events). 5-min fallback if phototoxicity exceeds threshold (Pilot P2).. Z-stack 21 slices × 0.4 μm. **Light-sheet (V8) strongly recommended** — reduces phototoxicity ×10 vs widefield. PAR-2 + PAR-3 channels. CED-3 channel. Phase contrast for boundaries. **Negative control:** RNAi-PLK-4. **Positive control:** spd-2(or165). | 100 embryos |
| **2** | **Bootstrap Mixed Model (PRIMARY).** Fate ~ PedigreeScore + age + PAR2 + PAR3 + (1|embryo/lineage). 1,000 bootstrap resamples of embryos. **Bayesian BF>10.** **Exclusion:** E-lineage cells, CED-3(+) apoptotic cells, cells with <3 timepoints. **Outcome variables:** (a) SAS-4 retention, (b) SAS-1 retention (early signal of impending elimination). | ~6,800 centrioles after exclusions |
| **3** | **Sister-pair sensitivity analysis.** If ≥40 same-type pairs → within-pair comparison. Secondary, not required for conclusions. | Subset of Stage 1 |
| **4** | **E-lineage secondary analysis.** Intestinal cells separately: does Pedigree Score predict which cells lose centrioles during endoreduplication? Post-embryonic follow-up (additional 2h imaging at L1 stage). | E-lineage cells only |
| **5** | **SAS-1 vs SAS-4 discordance.** Cells where SAS-1 is lost but SAS-4 persists → "centriole committed to elimination." Test whether Pedigree Score predicts SAS-1 loss EARLIER than SAS-4 loss. | All cells |

**Intermediate analysis:** After 50 embryos. BF<3 → N=200. BF>10 → stop.

---

## 4. Budget (ARGUS V7, 24 months)

**Platform:** Spinning disk confocal (CSU-W1) + sCMOS. V8 light-sheet deferred to OS2 (separate proposal).

| Item | $ |
|------|--:|
| 60×/1.2 NA WI objective (Nikon CFI Plan Apo) | 13,500 |
| sCMOS camera (Hamamatsu ORCA-Fusion BT) | 22,000 |
| Spinning disk unit (Yokogawa CSU-W1) | 18,000 |
| 405 nm + 488 nm + 561 nm + 640 nm lasers | 2,500 |
| Microfluidic chip + pressure system | 5,000 |
| Frame + stage: Aluminum 7075 + thermal stabilization | 4,000 |
| AI: Jetson AGX Orin 64GB (275 TOPS) | 3,000 |
| Night vision + phase contrast | 2,000 |
| C. elegans strains (8 markers + RNAi + mutants) + reagents | 10,000 |
| Equipment maintenance (2 years) | 8,000 |
| Consumables (coverslips, agarose, plates) | 4,000 |
| Conference travel | 3,000 |
| Open Access fees | 5,000 |
| PI salary (25% FTE, 24 months) | 30,000 |
| Engineer salary (50% FTE, 24 months) | 60,000 |
| Lab space (Abastumani, 24 months) | 10,000 |
| Contingency (20%) | 32,000 |
| **Total** | **~192,000** |

---

## 4b. Causality Test (OS2 Preview)

If Pedigree Score correlates with fate in OS1, OS2 tests causality via **centriole transplantation**: transplant a centriole with "bad" pedigree into a cell with "good" pedigree (or vice versa). If fate follows the centriole, not the cell → causality proven. Design pre-registered now for credibility.

## 4c. Sensitivity Analyses

- **Lineage stratification:** neurons vs hypodermis vs muscle. Tests whether Pedigree Score effect is universal or lineage-restricted.

- **Temperature calibration (Pilot P0):** Compare 20°C (Sulston standard) vs 25°C. If elimination pattern differs → use 20°C.

- **Spectral unmixing:** SPD-2::mCherry + SAS-4::GFP + CED-3::mKate2 (588nm) channels unmixed to prevent cross-excitation.

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
| 25 | **Delattre, Canard & Gönczy (2006)** — sequential protein recruitment in C. elegans centriole formation, Curr Biol | 16979563 |
| 26 | **Dammermann et al. (2004)** — centriole assembly requires centriolar and PCM proteins, Dev Cell | 15572125 |
| 27 | **Pintard & Bowerman (2019)** — mitotic cell division in C. elegans, Genetics | 30626640 |
| 28 | **Fu & Glover (2012)** — centriole-PCM interface (Drosophila), Open Biol | 22977736 |
| 29 | **Plourde et al. (2025)** — AIR-1 centrosome asymmetry, C. elegans embryo, Sci Rep | 40082489 |

---

**Exclusion criteria:** E-lineage (gut) + CED-3(+) apoptotic cells + <3 timepoints.
**Primary:** Bootstrap Mixed Model, BF>10.
**Sensitivity:** Sister pairs. **Surrogate:** SAS-1 loss before SAS-4.
**Timing note:** 100-cell window snapshot — NOT comma stage. Late eliminators flagged.
**V8 light-sheet strongly recommended** for phototoxicity ceiling.
*33 refs. Sister-pairs PRIMARY. Joint model (JMbayes2). Composite fate (SAS-4+SPD-2). $192K.*

---

**Limitations:** (1) 100-cell window ≠ comma stage — Pilot P0 validates dynamics specifically in 0→100-cell window. (2) E-lineage EXCLUDED (post-embryonic elimination mechanism differs). (3) CED-3 for apoptosis exclusion. (4) SAS-1 somatic applicability tested in P6; secondary outcome until validated. (5) V7 spinning disk with adaptive illumination; V8 light-sheet deferred to OS2. (6) PCM loss before core (O'Toole 2003). (7) SPD-2::mCherry composite fate in ALL N=100 embryos. (8) Temperature control ±0.1°C. (9) Sister-pair count: Sulston (1983) → ~5 same-type pairs/embryo → ~500 total pairs across 100 embryos. Power >80% for OR≥1.5 with paired design.
