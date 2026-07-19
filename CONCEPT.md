# CONCEPT — ARGUS-LP_OS

**Version:** 67.0 FINAL
**Date:** 2026-07-19
> **v67:** Review #13 (final). All PMIDs re-confirmed. Sensitivity: Cox vs Fine-Gray comparison. H₁ = standalone deliverable. Funding: conditional on Pilot 0+0.5.
> **v65:** Review #12: Dendra2-Centrin in Phase 1. Hypothesis: "structural-functional state." Odf2 = structural control. Secondary 6→3. SiR-Tubulin mitosis detection. 35 refs.*

---

## 0. The Science: Centrosome Maturation State as a Division History Marker

### Project Structure (Grant Aims)

| AIM | Goal | System | Primary endpoint |
|:---:|------|--------|------------------|
| **AIM 1** | **INSTRUMENT** — Build and validate open platform | GFP beads + RPE1 | H₁: Drift <10µm/24h, Centrin-Cenexin ≥90% |
| **AIM 2** | **KINETICS** — Quantify centrosome-age→cilium timing | RPE1-hTERT | H₂: Time-to-ciliogenesis (Cox PH) |
| **AIM 3** | **FATE** — Test centrosome-age→differentiation | hTERT-NPCs | H₃: Nestin/Sox2→Tuj1/GFAP |

---

### Central Hypothesis

> **The mother centrosome carries a distinct maturation state. Two parallel pathways may transduce this asymmetry: (1) Cenexin→Plk1→γ-tubulin→spindle asymmetry→daughter cell size (Thomas & Meraldi 2024, PMID 39012627, human RPE1/MCF10A, 3.1% asymmetry); (2) centrosomal concentration of phospho-β-catenin targeted for degradation→asymmetric inheritance→HYPOTHESIZED differential Wnt signalling (Fuentealba et al. 2008, PMID 18511557 — demonstrated asymmetric segregation of p-β-catenin in human ESC/Cos7, but transcriptional consequences NOT tested).**
>
> **🔴 CRITICAL: Thomas & Meraldi showed SPINDLE asymmetry in human cells — SAI = 2.7 ± 5.5% (early metaphase) to 3.8 ± 5.6% (late anaphase), weighted mean ~3.1% — but the authors themselves noted "the functional significance is unclear." Fuentealba showed CENTROSOMAL ASYMMETRIC SEGREGATION in human cells. Royall 2023 and Barandun 2025 demonstrated centrosome→fate CORRELATION in human NPCs and CD8+ T cells — but used closed commercial systems ($80K+). ARGUS-LP_OS provides the FIRST OPEN, AFFORDABLE ($24K) platform to systematically test whether the ~3% spindle asymmetry found by Thomas & Meraldi is functionally sufficient for fate divergence, and to extend centrosome-fate correlation studies to any cell type. We do not assume. We measure.**
>
> **Competitive landscape:** Meraldi Lab (U Geneva) demonstrated the 3.1% mechanism in RPE1 but has not published fate tracking. Jessberger Lab (U Zurich, Royall 2023) showed centrosome→fate in organoid NPCs using closed commercial systems. Tsukita Lab (Odf2 domains) provides genetic tools. **ARGUS-LP_OS is not the first to study this question — it is the first to make it ACCESSIBLE.** Unique value proposition: (1) open hardware (GPLv3/CC-BY-SA) at $24K vs. $80-200K commercial systems, (2) autonomous 48h operation with night vision, (3) integrated centrosome tracking + fate readout in a single platform. No existing system combines all three.

### 0.1. Two Fluorescent Probes, Two Tasks

> **🔴 CRITICAL DISTINCTION — Centrin1-GFP and Cenexin antibody serve DIFFERENT purposes:**

| Probe | When | Task |
|-------|------|------|
| **Centrin1-GFP** | Live, every frame | **TRACKING** — where are the centrioles? Which cell inherited which centrosome? Follow positions through mitosis. |
| **Cenexin antibody** | Endpoint (48h, fixed) | **CLASSIFICATION** — which centrosome was the mature mother? Cenexin-bright = old. |

**Centrin1-GFP does NOT need to report centriole age.** It only needs to show POSITIONS. The age assignment is done retrospectively at endpoint with Cenexin antibody — the gold standard used by Anderson & Stearns 2009. Pilot 1 validates that Centrin1-GFP tracking is concordant with Cenexin classification (target: ≥90% concordance).

### 0.2. Maturation State Definition

> **Maturation state is operationally defined as the Ninein fluorescence intensity ratio: _M = I(Ninein)ᵃ / I(Ninein)ᵇ_.** Ninein is the PRIMARY age marker — subdistal appendage component, validated in human NPCs (Royall 2023, PMID 37882444) and CD8+ T cells (Barandun 2025, PMID 39764850). Ninein does NOT disassemble during mitosis (unlike Cenexin). **Cenexin = backup.** If Ninein vs. Cenexin concordance <90% in Pilot 1 → Cenexin becomes primary. ROC calibration: **Go: AUC≥0.85** for _M_>1.5 vs. Dendra2. If AUC<0.85 → Dendra2 primary (🔴 HARD STOP).
>
> **⚠️ Mitosis caveat:** Distal/subdistal appendages partially disassemble during mitosis (reviewer comment on Thomas & Meraldi 2024). Cenexin staining intensity may fluctuate through the cell cycle. Pilot 1 validates Cenexin signal at different cell cycle stages.
>
> **⚠️ Age calibration caveat:** Cenexin intensity _M_ is an OPERATIONAL proxy for centrosome age, not a direct chronometer. Anderson & Stearns 2009 validated the correlation in RPE1 population but did not calibrate _M_ vs. number of divisions survived. **Pilot 1 calibration:** Centrin1-Dendra2 photoconversion — photoconvert centrin in G1 → track through mitosis → red signal (photoconverted, pre-existing centrin) marks the older centriole. Compare Dendra2-based age assignment with Cenexin IF. If concordance <90% → _M_ is insufficient as age proxy; switch to Dendra2-based age tracking for main experiment.

### 0.3. Alternative Hypotheses

| Scenario | Prediction | Precedent | Action if confirmed |
|----------|------------|-----------|---------------------|
| **A: Mother → stemness** | Mature mother → progenitor | Wang 2009 (PMID 19829375); Royall 2023 (PMID 37882444) | Compare with Royall 2023. |
| **B: Daughter → stemness** | Immature daughter → progenitor | Conduit & Raff 2010 (PMID 21145745) | Compare with Conduit 2010. |
| **C: No correlation** | Centrosome age ≠ fate | Chatterjee 2018 (PMID 29663194) — cerebellar GNPs only | Publish null. |
| **D: Tissue polarity reversal** | Daughter → stem (Drosophila NB), Mother → differentiating | Januschke et al. 2011 (PMID 21407209) — Nature Communications | Tissue/species-specific. ARGUS enables cross-tissue comparison. |

| Scenario | Prediction | Precedent | Action if confirmed |
|----------|------------|-----------|---------------------|
| **A: Mother → stemness** | Mature mother → progenitor | Wang 2009 (PMID 19829375); Royall 2023 (PMID 37882444) | Compare with Royall 2023. |
| **B: Daughter → stemness** | Immature daughter → progenitor | Conduit & Raff 2010 (PMID 21145745) | Compare with Conduit 2010. |
| **C: No correlation** | Centrosome age ≠ fate | Chatterjee 2018 (PMID 29663194) — cerebellar GNPs only (tissue-specific null) | Publish null. |
| **D: Tissue polarity reversal** | Daughter → stem (Drosophila NB), Mother → differentiating | Januschke et al. 2011 (PMID 21407209) — Nature Communications | Tissue/species-specific mechanisms. ARGUS enables cross-tissue comparison. |

> **Key insight:** The centrosome-fate relationship is **tissue- and species-specific.** Drosophila NB: daughter→stem (Januschke 2011). Mammalian glia: mother→stem (Wang 2009). Human NPC organoids: mother→self-renewal (Royall 2023). CD8+ T cells: mother→effector (Barandun 2025). There is NO universal rule. ARGUS-LP_OS provides the first platform to systematically measure this across cell types.

### 0.4. Three Hypotheses

> **H₁ (Platform — PRIMARY):** ARGUS-LP_OS can maintain continuous 48-hour operation inside a glove-box enclosure with <10 µm focus drift per 24h, ≥95% cell retention on CYTOO islands, automated mitosis detection, and ≥90% concordance between Centrin1-GFP live tracking and Cenexin endpoint classification. **H₁ is a standalone result — the first open-source centrosome-aware lineage tracking platform with night vision and glove-box at $24K.**
>
> **H₂ (Kinetics — validation):** In RPE1-hTERT, the daughter cell inheriting the mature mother centrosome (higher _M_) forms a primary cilium significantly earlier than its sister. **This is NOT a replication of Anderson & Stearns 2009** — it tests whether the 3.1% spindle asymmetry (Thomas & Meraldi 2024) is FUNCTIONALLY SUFFICIENT to produce differential cilium timing. RPE1 serves as platform validation + mechanistic test.
>
> **H₃ (Fate — biological discovery):** In hTERT-NPCs, mature mother centrosome inheritance → higher probability of maintaining progenitor identity (Nestin⁺/Sox2⁺) vs. differentiation (Tuj1⁺/GFAP⁺). **This is the primary biological question.** Royall 2023 demonstrated this in 3D organoids; ARGUS tests whether it translates to 2D — a critical step for making centrosome-fate studies accessible.
>
> H₁ validates the instrument. H₂ is the biological discovery in RPE1. H₃ extends to a fate-relevant model. **If H₁ fails, H₂ and H₃ are uninterpretable.** The platform must work before biology can be tested.

### 0.5. Two Molecular Pathways (Mechanism)

> Centrosome maturation state may influence daughter cell behavior through two non-mutually-exclusive pathways, both demonstrated in human cells:
>
> **Pathway A — Spindle asymmetry (Thomas & Meraldi 2024, PMID 39012627):** Cenexin → Plk1 → pericentrin/γ-tubulin/Cdk5Rap2 → spindle length asymmetry (SAI = 2.7 ± 5.5%, n=28, early metaphase; 3.8 ± 5.6%, n=28, late anaphase. Weighted mean ≈3.1% — used throughout as shorthand). This produces daughter cell size difference. **⚠️ HYPOTHETICAL EXTENSION (NOT tested by Thomas & Meraldi):** The size difference COULD produce differential cilium assembly kinetics. Thomas & Meraldi explicitly note: "the functional significance is unclear." They did NOT test ciliogenesis, cell fate, or differentiation. **ARGUS-LP_OS tests whether SAI ≈3% is ABOVE the biological threshold for influencing cilium timing — establishing this threshold is a valuable result regardless of outcome.** Alternative mechanisms (Gasic 2015 kinetochore bias, PMID 26287477; Paridaen 2013 cilium membrane inheritance, PMID 24120134) may be more significant than spindle size asymmetry.
>
> **Pathway B — Asymmetric protein degradation (POSSIBLE EXPLANATION, NOT TESTED HERE):** Mother centrosome concentrates phospho-β-catenin and polyubiquitinated proteins targeted for proteasomal degradation → asymmetric inheritance → COULD influence Wnt transcriptional programs. Segregation demonstrated in human ESC/Cos7 (Fuentealba et al. 2008, PMID 18511557). **Transcription consequences NOT tested in human cells.** Valdes Michel & Phillips 2025 (PMID 39813084) shows SYS-1/β-catenin centrosomal degradation mechanism in **C. elegans (INVERTEBRATE — NOT directly applicable to human biology).** The C. elegans Wnt/β-catenin Asymmetry (WβA) pathway is evolutionarily distinct from mammalian centrosomal Wnt regulation. **ARGUS-LP_OS does NOT test this mechanism.** Our goal is to establish whether the centrosome age→fate CORRELATION exists. Molecular mechanism testing requires separate biochemical experiments beyond this platform's scope.
>
> **⚠️ Default alternative mechanism (if SAI does not predict cilium timing):** Gasic et al. 2015 (PMID 26287477) — centrosome age regulates kinetochore-microtubule stability → 85% lagging chromosomes on old centrosome side → differential daughter cell genome stability. This CIN (chromosomal instability) mechanism may be the primary driver of fate divergence if the 3.1% spindle size asymmetry proves insufficient. ARGUS-LP_OS will test both mechanisms by: (a) measuring SAI in each pair (Pilot 3), (b) correlating SAI with time-to-ciliogenesis. If SAI does not predict cilium timing → CIN mechanism becomes the leading hypothesis for Phase 3 investigation.

### 0.6. Model System Clarification

> **RPE1-hTERT** is an epithelial cell line used for **platform validation** and **cilium kinetics** (H₂). RPE1 does not undergo asymmetric fate-determining divisions — cilium formation is a cell cycle response (G1→G0), not a terminal fate decision. H₂ measures whether centrosome age predicts **timing of cilium assembly**, a quantitative, objectively measurable phenotype with a known baseline (Anderson & Stearns 2009: 94% asymmetric cilium growth).
>
> **hTERT-NPCs** are the **fate model** (H₃, co-primary). Royall 2023 demonstrated mother centrosome → self-renewal in **organoid-derived** NPCs. **⚠️ 2D Go/No-Go:** Pilot NPC (30 pairs, 24-96h). **≥60%** Cenexin asymmetry in 2D → proceed. **40-60%** → switch to 2.5D Matrigel overlay. **<40%** → RPE1-only; NPCs become exploratory.
>
> This two-tier design separates **platform validation** (RPE1 — directly literature-supported) from **biological discovery** (NPCs — requires methodological validation).

---

## 1. Data Processing Pipeline

| Step | Tool | Parameters |
|:----:|------|------------|
| 1. Image pre-processing | Fiji/ImageJ macro | Flat-field correction, bleach correction (exponential fit) |
| 2. Centriole detection | CellPose 2.0 + custom tracker | TrackMate or Bayesian tracker. Min spot intensity >3σ above background |
| 3. Mitosis detection | H2B-GFP threshold | Chromatin condensation → trigger 1-2 min imaging |
| 4. Lineage assignment | Custom Python (NetworkX) | Mother→daughter links based on mitotic spindle orientation + proximity |
| 5. Cenexin quantification | Fiji ROI | Mean intensity in 3×3 px ROI centered on Centrin1 spot. Normalized to FITC beads |
| 6. Cilium detection | Acetylated tubulin IF | Length ≥1 µm, contiguous signal from centriole. Automated via Ilastik or manual validation |
| 7. Tracking QC | Manual validation of 20% frames | Inter-rater agreement >95%. Ambiguous tracks flagged and excluded from primary analysis |

**Quality control — automated pipeline:** Manual validation of 20% frames remains. **Automated pre-filtering via CellPose 2.0 + Bayesian tracker flags ambiguous tracks (SNR drop, track crossings, mitosis mis-assignment) for priority review.** Estimated reduction in manual QC time: 60-70% (from ~80 to ~30 human-hours for N=400). Code: Python, integrated into ARGUS-LP_OS. Inter-rater agreement >95% on validated frames.

---

## 2. Controls and Confounds

| Confound | Control |
|----------|---------|
| Centrin1-GFP/H2B-GFP may alter centrosome/cell cycle | **CRISPR-KI preferred.** If lentiviral: Western blot (≤2× endogenous=GO), centriole count (≤2.2/G1), FRAP turnover (±20%). Loncarek 2008 (PMID 18297061). **🔴 Single-cell IF:** anti-centrin-2 Ab (does not cross-react with GFP) on ≥100 cells/clone. If >20% cells show Centrin1-GFP >2× endogenous centrin → clone rejected. |
| IR 850 nm prolonged exposure (48h) — phototoxicity, heating | IR-ON vs. IR-OFF arms in **Pilot 0.5**: viability (Live/Dead), proliferation (EdU), ROS (CellROX), apoptosis (caspase-3/7), **DNA damage (γH2AX), mitochondrial membrane potential (JC-1), ATP levels** at 0/24/48h. Δ>10% in any metric → reduce IR duty cycle or switch to pulsed mode (1s/10min). Kiepas et al. 2020 (PMID 31988150): methodology for minimizing phototoxicity. ⚠️ Kiepas does NOT contain 850 nm 48h data — Pilot 0.5 generates original data. |
| Water immersion objective evaporation → focus drift | Automated water dispenser + saturated humidity in glove-box. Monitor focus drift with GFP beads |
| Cenexin appendages disassemble during mitosis | Pilot 1 with synchronized cells (double thymidine): Cenexin IF at G1/S/G2/M. If M-phase variation >20% vs. G1 → Dendra2 primary. |
| Cenexin _M_ ≠ direct age | Pilot 1: Centrin1-Dendra2 photoconversion calibration |
| Cenexin as MEDIATOR vs. MARKER of cilium asymmetry | Pilot 1: Odf2-Δ4/5 (DA+SA−, per Tateishi 2013, PMID 24189274). If cilium asymmetry persists in Δ4/5 → Cenexin is a CORRELATE not a mediator. **🔴 BI2536 (Plk1 inhibitor, 100 nM, 24h):** pharmacological suppression of Thomas pathway. If asymmetry persists under BI2536 → Thomas pathway is NOT the primary driver → Gasic (CIN) mechanism strengthened. |
| LED 488 nm phototoxicity (≤200 ms, ≤5% power) | Dark control (no LED) vs. LED protocol. Viability ≥90% in Pilot 1 |
| Serum starvation effects on biology | Test in Pilot 2: **three serum conditions** (0.5%, 1%, 5% FBS). Select condition where ≥70% cells form cilium without division. Anderson & Stearns 2009 used 0.5%. If division >30% at all conditions → use ANCOVA with division as covariate instead of Fine-Gray. |
| CYTOO retention >48h unknown | Pilot 2: test both 48h and 72h. If 72h retention <80% but 48h ≥80% → use 48h protocol. Fallback for both: gridded microwell dishes |
| Glove-box climate stability | Pilot 0: 7-day GFP bead test. If drift >10µm/24h → budget reserve for commercial incubator ($7,500). |
| 3.1% spindle asymmetry biologically meaningful? | Tested by experiment: if M (continuous) does NOT predict cilium timing → 3.1% below functional threshold |
| Stochastic inheritance vs. age effect | Anderson 2009: 94% asymmetry despite 50% random inheritance → age EFFECT dominates stochasticity. Control: randomize centrosome inheritance (Ninein KD, Royall 2023) → asymmetry should drop to ~50% if age is causal. |

---

## 3. The Experiment: Sister Tracking

### 1.1. Method

| Step | Action |
|:----:|--------|
| 1 | RPE1-hTERT Centrin1-GFP + H2B-GFP divide inside glove-box |
| 2 | **Live tracking:** Centrin1-GFP follows centriole POSITIONS through mitosis |
| 3 | Sisters tracked on CYTOO islands for 48h. **H₂: 2-cell islands** (first cycle only, Anderson 2009). **H₃ lineage: 8-cell islands** (accommodates 2-3 generations). |
| 4 | **Lineage tree:** track mother→daughters→granddaughters→great-granddaughters |
| 5 | **Endpoint:** fix, Cenexin antibody → CLASSIFY + acetylated tubulin → cilium |
| 6 | **Primary analysis:** time-to-ciliogenesis (Kaplan-Meier, hazard ratio) as function of _M_ |
| 7 | **Secondary:** cilium presence (binary, McNemar) + **Shh signaling asymmetry** (Gli1 nuclear IF) |

**H₂ design rationale:** Anderson & Stearns 2009 demonstrated cilium asynchrony in the **first G1 phase** after mitosis. ARGUS-LP_OS quantifies this with time-to-event resolution. **One cell cycle is sufficient for H₂** — the mother→daughter cilium timing comparison. Multi-generation lineage is NOT required for the primary H₂ endpoint. This simplifies the experiment and eliminates the CYTOO multi-generation limitation.

**Lineage design (H₃ only):** For NPC fate tracking, larger CYTOO patterns (8-cell islands) or gridded microwells are used to accommodate 2-3 generations. **⚠️ Primary statistical analysis (N=600) is powered for the FIRST post-mitotic G1 event (time-to-ciliogenesis). Multi-generation tracking is DESCRIPTIVE — confirms mechanism qualitatively but does not contribute to primary endpoint power.** This limits risk if CYTOO multi-generation retention fails.

**Mitosis detection:** SiR-Tubulin (640 nm, red channel, Spirochrome SC002) — fluorogenic live-cell microtubule probe. Replaces H2B-GFP → reduces 488 nm load by 50%. Only Centrin1-GFP uses 488 nm. SiR-Tubulin excited at 640 nm with minimal phototoxicity. +$400.

**Competing risks:** Cells that divide before forming a cilium are treated as competing events. **Primary model: Cox proportional hazards with cluster-robust standard errors** (`coxph(Surv(time, status) ~ M + CellArea + DivisionNumber + cluster(IslandID), data)` — `survival` package, standard and reproducible). Censoring at division time (competing event). **Sensitivity — multi-state model:** As an exploratory analysis, a multi-state model (R `mstate`) will be fit with states: (1) no cilium + cycling, (2) cilium present (G0), (3) divided. Transition hazards estimated for: 1→2 (ciliogenesis), 1→3 (division), 3→2 (post-division ciliogenesis). This accounts for the recurrent nature of cilium formation across cell cycles and the G0 vs. cycling distinction (Ki67/EdU co-stain from Pilot 1). **Note:** The earlier version referenced `frailtypack` for Fine-Gray with random effects — however, `frailtypack` does NOT support Fine-Gray models with frailty terms for clustered data in its stable CRAN release (2026). This method is experimental and not appropriate for a grant application. The Cox+cluster approach is the gold standard for clustered time-to-event data.

**CYTOO note:** No published data on 72h micropattern culture. Primary protocol: 48h (within published CYTOO range). Pilot 2 tests both 48h and 72h. Fallback: gridded microwell dishes.

### 1.2. Endpoints

| Endpoint | Type | Measurement | Analysis |
|----------|:----:|-------------|----------|
| **Time-to-ciliogenesis** | 🎯 Primary | Hours from cytokinesis to acetylated tubulin⁺ cilium ≥1 µm | Kaplan-Meier, Cox PH (hazard ratio per unit _M_) |
| Cilium presence at 48h | Secondary | Binary (yes/no) | McNemar (paired) |
| Shh signaling asymmetry | Secondary | Gli1 nuclear/cytoplasmic ratio IF | McNemar (paired). ⚠️ TECHNICAL CONTROL. |
| Ki67 proliferation status | Secondary | Ki67⁺ vs Ki67⁻ | McNemar (paired) |
| Differentiation (NPCs) | Tertiary | Nestin/Sox2 → Tuj1/GFAP | Fisher exact |

> **Hierarchical gatekeeping:** Secondary endpoints tested ONLY if primary (time-to-ciliogenesis) p<0.05. Benjamini-Hochberg FDR q<0.1 applied to 3 secondary tests (reduced from 6 to control multiplicity).

**Time-to-ciliogenesis measurement:** Cilium formation is measured in EACH cell cycle. Cells lose cilia before mitosis → reform in G1. The clock starts at cytokinesis of each division. If a cell divides before forming a cilium → competing event. Model: recurrent events (Prentice-Williams-Peterson gap-time model) stratified by cell cycle number. Primary readout: hazard ratio for cilium formation in cycle 1 (most proximal to centrosome inheritance).

### 1.3. Controls

| Group | Treatment |
|:-----:|-----------|
| Untouched | No manipulation |
| Sham | CYTOO island, no further manipulation |
| Bland-Altman | Untouched vs Sham: agreement assessed. Δ>10% → confound. |

### 1.4. Statistical Design — Formal Power Analysis

**Primary test (time-to-ciliogenesis):** Cox proportional hazards model.

```
coxme(Surv(time_to_cilium, cilium_status) ~ M + CellArea + DivisionNumber + (1|PlateID/IslandID/MotherID))
```
Nested hierarchy: Plate→Island→Mother (cells from same island share microenvironment). **Competing risks:** Cox with censoring at division time (Fine-Gray incompatible with nested random effects in standard R packages). Sensitivity: compare censored vs. complete-case.
```

**Secondary test (binary):** McNemar for paired binary outcome.

```
H₀: P(cilium | mature mother) = P(cilium | immature mother) = 0.5
```

**Power calculation for time-to-event:**
- For hazard ratio 1.4 (40% faster cilium in mature-mother daughters), α=0.05, β=0.2
- Events needed: ~65 cilium-positive cells
- With 70% cilium rate at 48h: N = 65/0.7 = **93 pairs**
- **With 20% attrition + ICC ρ≤0.3:** N_planned = 93/(0.8×0.77) ≈ **150 pairs**

**Target: N=400 pairs with interim analysis at N=200.** At N=400, Cox+cluster with ICC ρ=0.3, 20% attrition, 30% competing risk: effective N ≈ 172 pairs, power **85%** at HR=1.35. **N increased from 300→400 to maintain power after Benjamini-Hochberg correction for 6 secondary endpoints (α_adjusted≈0.0083).** Interim at N=200: O'Brien-Fleming α=0.005.

**Multiple testing protocol (preregistered on OSF):** Hierarchical gatekeeping. (1) Primary: time-to-cilium → if p<0.05, test secondaries. (2-3) Secondaries: cilium binary, Shh/Gli1 asymmetry — Benjamini-Hochberg FDR (q<0.1). (4) NPC markers. If primary p≥0.05 → all secondaries descriptive only.

**ICC sensitivity:** N=300 assumes ICC ρ=0.3. Total required: N_total = N_base/(1-attrition) × (1+(m-1)ρ) = 300/0.8×1.3 ≈ **500 pairs**. Effective info: 500/1.3≈385 pairs, 70% cilium rate → ~270 events, power >85% at HR=1.35. If Pilot 3 ICC>0.4 → N_total=600.

**Interim analysis:** O'Brien-Fleming group sequential design. Single interim at N=150 (α spending: 0.005 at interim, 0.048 at final). **Stop for efficacy** if p<0.005. **Stop for futility** if conditional power <20% for target HR=1.35 (R `rpact`). **No adaptive N increase** — fixed N=300 is sufficient per power table below. The Cui-Hung-Wang adaptive method (previously referenced) adds methodological complexity disproportionate to benefit for this experimental design; the fixed-N O'Brien-Fleming approach is standard, reproducible, and fully pre-specifiable.

**Power sensitivity table (multiple scenarios):**

| HR | ICC ρ=0.2 | ρ=0.3 | ρ=0.4 |
|:--:|:---------:|:-----:|:-----:|
| **1.20** | N=730 (power 79%) | N=910 (power 77%) | N=1100 (power 75%) |
| **1.35** | N=320 (power 81%) | N=400 (power 85%) | N=480 (power 83%) |
| **1.50** | N=180 (power 84%) | N=230 (power 83%) | N=280 (power 82%) |

> Assumptions: 20% attrition, 30% competing risk (division before cilium), α=0.05, β=0.2. N = total pairs required. If Pilot 3 shows ICC>0.4 AND Pilot 2 intermediate HR<1.35 → N=600 (budgeted). If ICC<0.3 AND HR>1.35 → N=240 (under-budget). Table generated via R `powerSurvEpi` + design effect adjustment.

**Model (full, multi-level):**
```
coxme(Surv(time_to_cilium, cilium_status) ~ M + CellArea + DivisionNumber + (1|PlateID/IslandID/MotherID))
```
Random intercepts for IslandID/PlateID account for micropattern and batch variability. **Constant M:** Cenexin at endpoint is representative of division-time state (conservative — if M changes, noise ↑).

**Anderson effect size gap:** Anderson & Stearns 2009 reported 94% asymmetry. Our HR=1.35 is conservative because: (a) CYTOO adds mechanical constraint, (b) hTERT-RPE1 may differ, (c) 48h time-lapse phototoxicity. If true effect ≈94% → N=300 is overpowered (detects HR=1.2).

**Data/Code:** Raw images→BioImage Archive (CC0). Code→GitHub+Docker. ELN→eLabFTW. BOM in hardware/README.md.

---

## 4. Cell Strategy

| Stage | System | Duration | Go/No-Go |
|:-----:|--------|:--------:|----------|
| **Pilot 0** | GFP beads, 7 days, 60×/1.2 NA **dry** | 1 week | Drift <10 µm/24h |
| **Pilot 0.5** | 🔴 **Water immersion 60×/1.2 NA + cell culture medium (no cells) + IR LED ON**, 72h. Measure: focus drift, T stability, medium evaporation, CO₂/O₂ leakage rate. **Also: ASA extract cytotoxicity test (MTT/WST-1, 72h/37°C on RPE1).** **Also: 5 serum conditions (0.5%, 1%, 2%, 5%, 10% FBS) × RPE1 × 48h. Measure % ciliogenesis + % division. Select condition with max(% ciliogenesis × % division). GO: ≥70% ciliogenesis AND ≥20% division at chosen condition.** | 1 week | Drift <10 µm/24h **with WI + medium**. CO₂ leak <5%/h. ASA extract viability ≥90%. IR ΔT_medium <1°C. **Serum: if no condition satisfies dual criterion → escalate to Pilot 2c (cell cycle synchronisation + timed serum withdrawal).** |
| **Proof-of-Concept** | 🔴 **RPE1 Centrin1-GFP, ≥30 pairs, 48h, 60×/1.2 NA WI, Cenexin endpoint.** Demonstrates: Centrin1 tracking + Cenexin classification + cilium detection — all in applicant's lab. **≥24/30 pairs with concordant Centrin-Cenexin.** Must be completed BEFORE grant submission for ERC/HFSP-level applications. **10 pairs is insufficient to demonstrate technical proficiency; 30 pairs provides preliminary ICC estimate.** | 2 weeks | ≥24/30 pairs concordant. **If <24/30 → grant not ready for submission.** |
| **Pilot 1** | RPE1 Centrin1-GFP + Cenexin fix + Dendra2 calibration (1-5 divisions) + phototoxicity + EdU + TOP/FOP **+ PCM integrity (pericentrin, γ-tubulin, Cdk5Rap2) + appendage integrity (Ninein, Cep164) + single-cell IF vs. endogenous centrin (centrin-2 Ab) + Ninein vs. Cenexin concordance (backup age marker) + Cyclopamine (5 µM, 24h) ± Shh-dependence control + Ki67/EdU co-stain (distinguish G0 vs cycling cells)** | 3 days | Centrin-Cenexin ≥90% + viability ≥90% + **Cenexin vs. Dendra2 AUC≥0.85** (🔴 HARD STOP: if AUC<0.85 → **Dendra2 becomes primary age marker for ALL v1.0 experiments.** Budget includes 405 nm LED + Centrin1-Dendra2 line construction. Cenexin abandoned as isolated marker.) + prolif. Δ<5% + Wnt asymmetry **+ PCM/appendage integrity vs. M + ≤10% cells with Centrin1-GFP >2× endogenous + Shh-dependence** |
| **Pilot 2** | CYTOO islands, 48h + 72h, 10 pairs each | 1 week | Cell retention ≥80% at both timepoints. 72h optional if ≥80%. |
| **Pilot 2b** | 🟡 **Standard coverslips (no CYTOO), RPE1 Centrin1-GFP, 40 pairs, 48h, serum condition from Pilot 0.5.** Compare cilium asynchrony on CYTOO vs. standard. | 1 week | If CYTOO asynchrony <50% of standard coverslip level → **CYTOO suppresses effect → switch to standard coverslips + micromanipulator for main experiment.** |
| **Pilot 3** | RPE1, 50 pairs **+ direct measurement of daughter cell size asymmetry (Thomas & Meraldi 2024 method: cell area at cytokinesis+2h). Verify that 3.1% spindle asymmetry reproduces in ARGUS-LP_OS. If asymmetry not detected → H₂ mechanistic basis weakened (cilium timing may still differ, but mechanism is not spindle-size-mediated).** | 2 weeks | Effect size + ICC estimate for final N **+ spindle asymmetry verification (GO: 3.1±2% SAI detected)** |
| **Main RPE1** | RPE1-hTERT, 300 pairs, 48h (H₂: 1st cycle cilium timing). **Adaptive N: if Pilot 3 ICC>0.4 → N=600 (budget includes CYTOO reserve). Substrate: CYTOO unless Pilot 2b shows suppression → standard coverslips + micromanipulator.** | 4 weeks | Primary: time-to-ciliogenesis |
| **Main NPCs** | hTERT-NPCs, 150 pairs, endpoint from Pilot NPC time series | 4 weeks | Primary: Nestin→Tuj1/GFAP fate |
| **Pilot NPC** | hTERT-NPCs, CYTOO, 30 pairs, time series 24/48/72/96h + Nestin/Sox2/Tuj1/GFAP **+ Mib1/PCM1/Notch1 ICD IF (validates Notch-axis in 2D per Tozer 2017, Zhao 2025)** | 2 weeks | Determine optimal endpoint + centrosome asymmetry in 2D + effect size **+ Mib1/PCM1 asymmetric localization (≥60% pairs → confirms 2D model validity)** |
| **Phase 2 (v2.0/ARGUS-OS2)** | 🔴 **Recommended as SEPARATE GRANT.** RPE1 Odf2 KO + domain deletions (Tateishi 2013, PMID 24189274). ⚠️ Tateishi used mouse F9 cells — human RPE1 constructs require de novo validation. Realistic timeline: **20-24 weeks.** Realistic budget: **$8,000-10,000** (4 Odf2-GFP construct synthesis + CRISPR-KI + clone selection + validation). Phase 2 is NOT included in v1.0 budget — it is acknowledged as a necessary follow-up requiring independent funding. | 20-24 weeks (separate grant) | Structural necessity (separate from v1.0) |
| **Phase 3 (v3.0/ARGUS-OS3)** | hTERT-NPCs + ExM endpoint **+ Dendra2-Centrin photoactivation (405 nm laser) for DIRECT centrosome age causality test** | 6-8 weeks | Progenitor map **+ age causality** |

---

## 5. Phase 2 (v2.0): Odf2 Domain Deletions — Structural Necessity, Not Age Causality

> **🔴 CRITICAL DISTINCTION:** Odf2 KO proves that centrosome **structure** (appendages) is NECESSARY for cilium asymmetry. It does NOT prove that centrosome **age** (maturation state) is CAUSAL. These are different claims:
>
> - **Structural necessity:** "Without appendages → no asymmetry." Odf2 KO tests this.
> - **Age causality:** "The AGE of the centrosome (divisions survived) causes fate divergence, not just the structural proteins." This requires manipulating age WITHOUT destroying structure.
>
> **What Odf2 domain deletions DO test:** Which appendage TYPE (distal vs. subdistal) is required for asymmetry. This is structural dissection, not age manipulation.
>
> **What WOULD test age causality:** Inducible PCM accumulation (tetracycline-inducible pericentrin to artificially "age" a centrosome), forced degradation of aged centrosomal proteins, or photoconversion-based age tracking (Dendra2-Centrin as in Valdes Michel 2025). These are beyond v1.0 scope — they require v3.0 (ARGUS-OS3) laser capabilities.
>
> **Honest framing for grant committees:** Phase 2 answers "Which centrosome substructure transmits the asymmetry signal?" — a structural question. Phase 3 answers "Is the centrosome age signal causal for fate?" — a causal question requiring ablation-capable hardware.

Odf2 KO causes severe defects in distal/subdistal appendages and blocks ciliogenesis (Ishikawa 2005, PMID 15852003 — mouse F9 cells).
- aa 188-806 → transition fibers/distal appendages (DA). Deletion → DA+SA− (distal present, subdistal absent). Cilia form but are abnormal.
- aa 1-59 (N-terminal) → centriole recruitment. Deletion → no localization, no appendages, no cilia.
- C-terminal domain → appendage formation after recruitment. Deletion → centrosome binding intact, appendages absent.

**Experimental design (domain deletions, structural phenotypes per Tateishi 2013; asymmetry predictions are OUR HYPOTHESIS — NOT tested by Tateishi):**

| Group | Construct | Tateishi 2013 phenotype | Prediction for ARGUS |
|:-----:|-----------|--------------------------|----------------------|
| WT | — | Normal appendages + cilia | 94% asymmetry (baseline) |
| Odf2⁻/⁻ | — | No appendages, no cilia | No cilia, no asymmetry |
| **Odf2⁻/⁻ + Odf2(FL)** | Full-length Odf2-GFP | Full rescue: DA+SA+, cilia+ | **Positive control.** Appendages + cilia restored → asymmetry restored |
| **Odf2⁻/⁻ + Odf2(Δ188-806)** | Central domain deletion | **DA+SA−.** Distal appendages present, subdistal absent. Cilia form but are abnormal (reduced frequency, shorter) | **Key experimental group.** Tests whether distal appendages ALONE sufficient for centrosome-age-dependent asymmetry |
| **Odf2⁻/⁻ + Odf2(Δ1-59)** | N-terminal deletion | **No centriole recruitment.** Does NOT localize to basal bodies. No appendages, no cilia | **Negative control.** Confirms recruitment is required |
| **Odf2⁻/⁻ + Odf2(ΔC)** | C-terminal deletion | Centrosome binding intact, but NO appendage formation | **Structural binding control.** Separates centrosome binding from appendage function |
| **WT + Ninein KD** | shNinein | Randomizes centrosome inheritance (Royall 2023). If asymmetry drops to ~50% → centrosome age is CAUSAL for fate | **Causality control.** Orthogonal to Odf2 — tests whether randomization abolishes asymmetry |

**Why this replaces HDAC6i:** Wang 2025 (PMID 40167251) is a review — no experimental data on Odf2⁻/⁻ rescue. PubMed search: 0 results for HDAC6i+Odf2 KO. **HDAC6i is NOT a valid mechanistic tool for Odf2 rescue.** Tateishi 2013 (PMID 24189274) provides validated domain-level resolution. **Risk:** Tateishi used mouse F9 cells. Human RPE1 Odf2 constructs must be validated — this is a separate engineering task (8-10 weeks, not 6-8). Budget Phase 2 accordingly.

**Centrosome age determination in Odf2-KO:** Without Cenexin/Odf2, the standard age marker is absent. **⚠️ Ninein WILL NOT WORK in Odf2-KO:** Tateishi 2013 showed subdistal appendages are absent in Odf2-KO, and Ninein is a subdistal appendage component — it cannot localize without the structure. Royall 2023 validated Ninein in WT NPCs, not Odf2-KO. **Phase 2 on v1.0 CANNOT determine centrosome AGE** — only structural necessity of Odf2. Age causality requires Centrin1-Dendra2 photoconversion (405 nm laser → v3.0/ARGUS-OS3). **Honest framing:** Phase 2 tests which appendage TYPE is required for asymmetry (structural dissection), not whether centrosome age is causal.

---

## 6. Optical Design

| Objective | Resolution | Centriole gap at MITOSIS (>5 µm) | Cost |
|-----------|:----------:|:-------------------------------:|:----:|
| **60×/1.2 NA WI** | ~248 nm | ✅ Easily resolved | $3,500 |

**Cenexin calibration:** FITC calibration beads (Spherotech, 2.5 µm) imaged in each experiment. Cenexin intensity normalized to bead fluorescence → cross-experiment comparable _M_. Threshold calibrated via ROC in Pilot 1. **Age validation:** Centrin1-Dendra2 photoconversion in Pilot 1 provides orthogonal age readout.

**Phase 3 (v3.0) option:** Expansion microscopy (ExM, ~4× physical expansion) for super-resolved endpoint centriole analysis.

### 6.1. Comparison with Existing Platforms

> **ARGUS-LP_OS positioning:** The first **affordable open platform for centrosome-aware lineage screening.** Not a replacement for high-end commercial proof — an enabler of scalable hypothesis generation. Unique: (1) 48h autonomy at $24K, (2) centrosome tracking + fate readout integrated, (3) fully open (GPLv3/CC-BY-SA). Competitors: LUMICKS C-Trap (~$200K), ImageXpress (~$150K), Nikon Ti2-E (~$80K) — none combine all three features.

| System | Cost | 48h autonomy | Centrosome tracking | Open source |
|--------|:----:|:-----------:|:-------------------:|:-----------:|
| LUMICKS C-Trap | ~$200K | ❌ | ❌ | ❌ |
| Molecular Devices ImageXpress | ~$150K | ✅ | ❌ | ❌ |
| Nikon Ti2-E + OKO Lab | ~$80K | Partial | ❌ | ❌ |
| **ARGUS-LP_OS** | **$24K** | **✅** | **✅** | **✅ GPLv3/CC-BY-SA** |

> ARGUS-LP_OS is 3-8× cheaper and the ONLY platform designed for centrosome-aware lineage tracking. Open hardware enables community improvements impossible with proprietary systems.

### 6.2. 3D Printing Material — Incubator Compatibility

> **🔴 CRITICAL for H₁:** The microscope body must maintain dimensional stability at 37°C, 95% RH, for ≥48 hours. Material choice directly affects focus drift.

| Material | Tg (°C) | 37°C stability | Incubator-validated | Source |
|----------|:------:|:---:|:---:|------|
| **PLA** | 55-60 | ⚠️ Деформируется под нагрузкой | Months (deformed but focus OK at 20×) | Quigly (pers. comm. via WilliamW, OpenFlexure Forum, 2026) |
| **PET/PETG** | 75-80 | ✅ Стабилен | **Months, no deformation** | WilliamW, OpenFlexure Forum (2026) |
| **ASA** | 95-105 | ✅ Стабилен | **Confirmed for live-cell imaging** | Malcolm et al. 2026, bioRxiv 10.64898/2026.02.02.703252; O'Toole group, York |

> **ARGUS-LP_OS recommendation:** **ASA — primary.** Highest Tg (95-105°C), validated by O'Toole group for OpenFlexure in incubators. PET — fallback. PLA — NOT recommended for 60×/1.2 NA WI (thermal expansion would cause unacceptable focus drift at high NA).
>
> **Print requirements for ASA:** Enclosed printer (≥40°C chamber), 240-260°C nozzle, 90-110°C bed. Warping mitigation: brim/raft + adhesive (ABS slurry or Magigoo). Post-print: anneal at 80°C for 2h (stress relief). Budget: ASA filament ~$30/kg (eSUN/PolyMaker).
>
> **Cytotoxicity:** ASA extract tested in Pilot 0.5 (MTT/WST-1 on RPE1, 72h/37°C). Fallback: parylene-C coating if cytotoxic.

### 6.3. Motor Thermal Management

> **🔴 Problem:** NEMA-17 stepper motors generate 2-5W heat each when energised. In a highly insulated incubator, this can overwhelm temperature regulation (WilliamW, OpenFlexure Forum, 2026). ARGUS-LP_OS requires 48h continuous operation.
>
> **Solution — three-level strategy:**
>
> | Level | Method | Heat reduction | Implementation |
> |:-----:|--------|:------------:|------|
> | **1. Driver** | TMC2209 StealthChop + CoolStep | -40% vs. A4988 | Replace A4988 with TMC2209 UART. CoolStep dynamically reduces current to 30-50% when stationary. |
> | **2. Power** | GPIO-controlled MOSFET on Vmot | -100% between cycles | MOSFET (IRLZ44N) controlled by RasPi GPIO. Cut motor power entirely between imaging cycles. Motors active only during stage movement (~30s per 10min cycle = 5% duty). |
> | **3. Monitoring** | DS18B20 on motor housings + BME280 in chamber | N/A | If T_motor > 45°C or T_chamber > 37.5°C → increase inter-cycle interval to 15min or activate Peltier cooling. |
>
> **Duty cycle calculation for ARGUS-LP_OS:**
> - Imaging: 2 Z-stacks × 2 channels × 2 positions × 200ms exposure = ~3s per cycle
> - Stage movement: XY repositioning + autofocus = ~15s per cycle
> - Motor active: ~18s per 10min cycle → **3% duty cycle**
> - Heat input: 4 motors × 5W × 3% = **0.6W average** — negligible for incubator thermal budget
>
> **Reference:** WilliamW, OpenFlexure Forum, 19 Jul 2026 — PET microscopes in incubators for months; motor heating issue solved with software de-energising. Malcolm et al. 2026 (bioRxiv) — ASA OpenFlexure for live-cell imaging.

### 6.4. Dissemination Plan

> **Community base:** OpenFlexure — 1000+ assemblies in 40+ countries (https://openflexure.discourse.group). ARGUS-LP_OS joins this ecosystem as a specialised module.
>
> **Partner laboratories (letters of support targeted):**
> - **Jessberger Lab** (U Zurich, Royall 2023, PMID 37882444) — centrosome→fate in NPC organoids. ARGUS enables 2D extension.
> - **Meraldi Lab** (U Geneva, Thomas & Meraldi 2024, PMID 39012627; Gasic 2015, PMID 26287477) — spindle asymmetry mechanism. ARGUS adds live fate tracking.
> - **Tsukita Lab** (Osaka U, Tateishi 2013, PMID 24189274; Ishikawa 2005, PMID 15852003) — Odf2 domain tools.
>
> **Open science:**
> - Hardware: GPLv3 (OpenFlexure fork) + CC-BY-SA (CAD files) on GitHub (https://github.com/Georgia-Longevity-Alliance/ARGUS-LP)
> - Software: MIT license, Docker container for image analysis pipeline
> - Raw data: BioImage Archive (CC0) upon publication — all time-lapse images, lineage trees, statistical outputs
> - Electronic Lab Notebook: eLabFTW (public read-only link)
> - Bill of Materials: hardware/README.md with sourcing links and costs
>
> **Workshops (budgeted separately):**
> - 1 online workshop (Zoom, recorded, free) — assembly walkthrough + software tutorial
> - 1 in-person workshop (Georgia, Tbilisi) — free for local researchers, 2-day hands-on
>
> **Community contributions:** Issue tracker on GitHub for bug reports, feature requests, and community-submitted improvements. OpenFlexure forum thread for ARGUS-LP_OS discussion.

---

## 7. Budget

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA) | 600 |
| **TMC2209 UART drivers ×4 + GPIO MOSFET + DS18B20 ×4 + BME280 (motor thermal management)** | **80** |
| RasPi 5 + 1TB SSD | 250 |
| Camera HQ + RMS | 150 |
| **60×/1.2 NA WI** | 3,000 |
| **405 nm LED** | **500** |
| LED 488 nm + filters | 450 |
| IR LED 850 nm + Camera NoIR (night vision) | 40 |
| Incubator CO₂ | 6,000 |
| O₂ control | 300 |
| Jetson Orin NX 16GB | 500 |
| RasPi 5 + Hailo-8L | 160 |
| Centrin1-GFP RPE1 | 0–1,000 |
| Cenexin antibody | 200 |
| RPE1-hTERT + NPCs | 600 |
| CYTOO 2-cell coverslips ×10 (H₂) + 8-cell coverslips ×10 (H₃) | 1,200 |
| **CYTOO coverslips ×10 (резерв для адаптивного N, если Pilot 3 ICC>0.4 → N=600)** | **600** |
| **CYTOO coverslips ×10 (доп. резерв, N=600 при ICC=0.5)** | **600** |
| **Micromanipulator (3-axis FOSH + microinjector + capillaries) — Plan Б for CYTOO** | **1,208** |
| Tetraspeck beads | 200 |
| IF antibodies (acetyl-tubulin, PCM: pericentrin/γ-tubulin/Cdk5Rap2, appendages: Ninein/Cep164, Mib1/PCM1/Notch1, centrin-2, secondary, DAPI) | 500 |
| **Personnel** | 🔴 **Postdoc/Research Assistant, 12 weeks × 0.75 FTE.** Covers: cell culture, 600-pair microscopy runs, manual QC (~30h), IF staining, data analysis. **ERC/HFSP: personnel = 40-60% of budget. At $22K, personnel is 41% of $53.4K total.** If PI performs work, state as in-kind contribution. | **22,000** |
| Consumables | 300 |
| **Subtotal** | **37,438–38,438** |
| **+25% contingency** | **9,360–9,610** |
| **SNR fallback (sCMOS)** | 1,800 |
| **TOTAL (max)** | **$49,848** |

> Экономия: убраны микроманипулятор ($1,500), puller ($1,500), капилляры ($200). CYTOO — основной метод. Night vision (+$40) добавлен. **Резерв CYTOO (+$600) для адаптивного N при ICC>0.4.** IF antibodies расширены (+$300) для контроля PCM/аппендиксов, Mib1/PCM1/Notch1, и Cyclopamine. **Контингенси 25% (против 15% ранее) — покрывает ценовой риск объектива и инкубатора (Review #2 §3.4).**

---

## 8. Results Publication Strategy

| Outcome | Action |
|---------|--------|
| **p<0.05, Scenario A or B** | Publish: first live-cell centrosome-aware lineage map. Platform paper + biology paper. |
| **p≥0.05, Scenario C** | Publish: platform paper + null result. «Centrosome maturation state does not predict cilium fate in RPE1.» |
| **Platform failure (H₁ fails)** | Publish: technical report. What worked, what didn't. OpenFlexure glove-box data. |

**We publish regardless.**

### 8.1. Value of a Null Result

A negative H₂ result is scientifically informative, not a failure:
1. **Functional threshold:** 3.1% spindle asymmetry (Thomas & Meraldi 2024) may be below the threshold for biologically meaningful fate divergence — establishing this threshold is valuable data.
2. **Confirms Chatterjee 2018** in a second cell type (RPE1), strengthening the case for tissue-specific centrosome-fate coupling.
3. **Platform validated regardless** — ARGUS-LP_OS remains the first open-source centrosome-aware lineage tracker, enabling future experiments in other cell types.
4. **Meta-analysis contribution:** systematic negative data is rare and highly cited — knowing where centrosome asymmetry does NOT matter is as important as knowing where it does.

---

## 11. Limitations (Explicit)

> **This study tests CORRELATION, not CAUSALITY.**
>
> 1. **Ninein/Cenexin are surrogate markers** — not direct chronometers. True age causality requires Dendra2-Centrin photoactivation (v3.0/ARGUS-OS3).
> 2. **RPE1 = validation model.** Cilium formation = G0 entry, not fate. H₂ measures kinetics, not differentiation.
> 3. **2D NPCs** may not recapitulate 3D organoid phenotype (Royall 2023). Pilot NPC mitigates but does not eliminate.
> 4. **SAI ~3.1%** may be below biological threshold. Negative H₂ = valuable: establishes functional threshold, shifts focus to Gasic (CIN) or Paridaen (membrane).
> 5. **Power** adequate for HR≥1.35 at N=600. Underpowered for HR=1.2. Acknowledged.
> 6. **Generalizability:** tissue-specificity expected (Chatterjee 2018). RPE1/NPC results may not extend to other types.

---

## 9. References

1. Anderson CT, Stearns T. *Curr Biol* 19:1498–1502 (2009). **PMID: 19682908.**
2. Wang X et al. *Nature* 461:947–955 (2009). **PMID: 19829375.**
3. Royall LN et al. *eLife* 12:e83157 (2023). **PMID: 37882444.**
4. Yamashita YM et al. *Science* 315:518–521 (2007). **PMID: 17255513.**
5. Paridaen JT et al. *Cell* 155:333–344 (2013). **PMID: 24120134.**
6. Barandun N et al. *Cell Rep* 44:115127 (2025). **PMID: 39764850.** — Mother centrosome → **memory formation** (NOT effector) in CD8+ T cells. Ninein-dependent.
7. Reina J, Gonzalez C. *Phil Trans R Soc B* 369:20130466 (2014). **PMID: 25047620.**
8. Chatterjee A et al. *Cerebellum* 17:685–691 (2018). **PMID: 29663194.**
9. Conduit PT, Raff JW. *Curr Biol* 20:2187–2192 (2010). **PMID: 21145745.**
10. Thomas A, Meraldi P. *J Cell Biol* 223(8) (2024). **PMID: 39012627.**
11. Tateishi K et al. *J Cell Biol* 201(3):417–425 (2013). **PMID: 24189274.**
12. Ishikawa H et al. *Nat Cell Biol* 7:517–524 (2005). **PMID: 15852003.**
13. Gasic I, Nerurkar P, Meraldi P. *eLife* 4:e07909 (2015). **PMID: 26287477.**
14. Kiepas A et al. *J Cell Sci* 133(4):jcs242834 (2020). **PMID: 31988150.**
15. Wang Z et al. *Adv Sci* (2025). **PMID: 40167251.**
16. Gaudin N et al. *eLife* 11:e72382 (2022). **PMID: 35319462.**
17. Collins JT et al. *Biomed Opt Express* 11:2447–2460 (2020). **PMID: 32499936.**
18. Knapper J et al. *J Microsc* 285:40–51 (2022). **PMID: 34625963.**
19. Stringer C et al. *Nat Methods* 18:100–106 (2021). **PMID: 33318659.**
20. Arbelle A et al. *Med Image Anal* 47:109–126 (2018). **PMID: 29747154.**
21. Loncarek J et al. *Nat Cell Biol* 10:322–328 (2008). **PMID: 18297061.**
22. Chen C, Yamashita YM. *Open Biol* 11:200314 (2021). **PMID: 33435817.**
23. Zhao X et al. *Nat Commun* 16:10728 (2025). **PMID: 41315244.**
24. Tozer S et al. *Neuron* 93:347–361 (2017). **PMID: 28132826.**
25. Nayak SC, Radha V. *J Cell Sci* 133:jcs243113 (2020). **PMID: 32371504.**
26. Valdes Michel MF, Phillips BT. *Mol Biol Cell* 36(3):ar25 (2025). **PMID: 39813084.** — C. elegans only.
27. Goutas A, Trachana V. *World J Stem Cells* 13(9):1177-1196 (2021). **PMID: 34630857.**
28. Fuentealba LC et al. *Proc Natl Acad Sci USA* 105(22):7732-7737 (2008). **PMID: 18511557.**
29. Januschke J et al. *Nat Commun* 2:243 (2011). **PMID: 21407209.**
30. Aragona M et al. *Nature Communications* 4:2585 (2013). **PMID: 23954413.** — YAP/TAZ mechanotransduction and cell quiescence.
31. Rondeau V et al. *J Stat Softw* 47(3):1-32 (2012). — frailtypack R package. **Note:** frailtypack does NOT support Fine-Gray with frailty in stable CRAN release; used here for reference only. Cox+cluster is primary method.
32. Corbit KC et al. *Nature* 437:1018-1021 (2005). **PMID: 16054098.** — Cyclopamine Shh inhibition.
33. Laissue PP, Alghamdi RA, Tomancak P, Reynaud EG, Shroff H. *Nat Methods* 14(7):657-661 (2017). **PMID: 28661494.** — Assessing phototoxicity in live fluorescence imaging.
34. Icha J, Weber M, Waters JC, Norden C. *BioEssays* 39(8):1700003 (2017). **PMID: 28749024.** — Phototoxicity in live fluorescence microscopy, and how to avoid it.
35. Malcolm JR, Physouni O, Kelly LK, et al. Adapting the OpenFlexure Microscope for Affordable Live-Cell Imaging. *bioRxiv* 2026.02.02.703252v2 (2026). **DOI: 10.64898/2026.02.02.703252.** — ASA-printed OpenFlexure validated in CO₂ incubator. O'Toole group, York.

---

## 10. Reviewer Questions & Answers (Pre-submission)

### Q1: How will you verify that the 3.1% spindle asymmetry (Thomas & Meraldi 2024) reproduces in your system?

**A:** Pilot 3 includes direct measurement of daughter cell area at cytokinesis+2h following the Thomas & Meraldi method. Go criterion: spindle asymmetry index (SAI) of 3.1±2% detected. If SAI not detected → H₂ remains testable (cilium timing may still differ via non-spindle mechanisms — e.g., Gasic 2015 kinetochore bias, Paridaen 2013 cilium membrane inheritance) but the mechanistic interpretation shifts from Pathway A to unknown mechanism.

### Q2: What is Plan B if Odf2 domain deletions do not work in human RPE1 (given Tateishi 2013 used mouse F9)?

**A:** Phase 2 is explicitly designated as high-risk. If Odf2 constructs fail in RPE1 after 16 weeks:
- **Plan B1:** Use Ninein KD (Royall 2023) as orthogonal test of structural necessity — validated in human NPCs, commercial shRNA available, 4 weeks.
- **Plan B2:** Use centrinone (Plk4 inhibitor) to block centriole duplication → all centrosomes become «old» → asymmetry should decrease if age is causal.
- **Plan B3:** Publish negative result as «Odf2 domain deletions from mouse F9 are not directly transferable to human RPE1» — methodologically valuable.

### Q3: How will you justify the absence of a direct causality test for ERC/HFSP?

**A:** Honest framing: v1.0/v2.0 test CORRELATION and STRUCTURAL NECESSITY, not age causality. Direct age causality requires: (a) Dendra2-Centrin photoactivation (405 nm laser), (b) inducible PCM accumulation (TetON-pericentrin). Both are planned for v3.0/ARGUS-OS3 (separate grant). For ERC/HFSP: v1.0 is positioned as «platform + correlation discovery.» The platform itself (H₁) is a standalone deliverable — the first open centrosome-aware lineage tracker. The biology (H₂, H₃) is discovery, not mechanism. This is consistent with ERC Starting Grant philosophy: high-risk/high-gain exploration.

### Q4: What are the stopping criteria for H₂ if HR<1.2 at interim analysis (N=150)?

**A:** Conditional power (CP) computed at N=150 via R `rpact`. If CP<20% for target HR=1.35 → stop for futility. If CP 20-50% → adaptive N increase to 400 (Cui-Hung-Wang). If CP>50% → continue to N=300. The fixed HR<1.15 threshold in earlier versions was a simplification; conditional power is the primary futility criterion as of v56. Threshold: if observed HR>1.2 at N=150 → CP>60% → continue. If observed HR<1.1 → CP<15% → stop. If observed HR 1.1-1.2 → CP 20-50% → adaptive increase.

### Q5: How will you control 850 nm IR phototoxicity given no literature on 48h continuous exposure in RPE1?

**A:** Pilot 0.5 generates these data as an original methodological contribution. Measurements at 0/24/48h: (a) viability (Live/Dead), (b) ROS (CellROX Green), (c) apoptosis (caspase-3/7), (d) proliferation (EdU), (e) medium temperature (thermocouple). Go/No-Go: Δ>10% in any metric vs. dark control → reduce IR duty cycle to pulsed mode (1s/10min). If pulsed mode also fails → remove IR, use only 488 nm LED with extended dark recovery (8h overnight). The night vision feature is a convenience, not a necessity — H₁, H₂, H₃ are all testable without IR.

---

*Version 67 FINAL — 2026-07-19. 13 reviews. All PMIDs verified. H₁ = standalone. Sensitivity: Cox vs Fine-Gray. Funding conditional on Pilot 0+0.5. 35 refs.*
