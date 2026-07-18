# CONCEPT — ARGUS-LP_OS

**Version:** 53.0
**Date:** 2026-07-19

---

## 0. The Science: Centrosome Maturation State as a Division History Marker

### Central Hypothesis

> **The mother centrosome carries a distinct maturation state. Two parallel pathways may transduce this asymmetry: (1) Cenexin→Plk1→γ-tubulin→spindle asymmetry→daughter cell size (Thomas & Meraldi 2024, PMID 39012627, human RPE1/MCF10A, 3.1% asymmetry); (2) centrosomal concentration of phospho-β-catenin targeted for degradation→asymmetric inheritance→HYPOTHESIZED differential Wnt signalling (Fuentealba et al. 2008, PMID 18511557 — demonstrated asymmetric segregation of p-β-catenin in human ESC/Cos7, but transcriptional consequences NOT tested).**
>
> **🔴 CRITICAL: Thomas & Meraldi showed SPINDLE asymmetry (3.1%) in human cells — but the authors themselves noted "the functional significance is unclear." Fuentealba showed CENTROSOMAL ASYMMETRIC SEGREGATION in human cells. Neither tested FATE. ARGUS-LP_OS is the FIRST direct test of whether these mechanisms produce biologically meaningful fate divergence. We do not assume. We measure.**
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

> **Maturation state is operationally defined as the Cenexin fluorescence intensity ratio: _M = I(Cenexin)ᵃ / I(Cenexin)ᵇ_.** _M_ is a continuous variable in all primary analyses. A binary threshold (_M > 1.5_) is calibrated via ROC analysis in Pilot 1.
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

> **H₁ (Platform — PRIMARY):** ARGUS-LP_OS can maintain continuous 48-hour operation inside a glove-box enclosure with <5 µm focus drift per 24h, ≥95% cell retention on CYTOO islands, automated mitosis detection, and ≥90% concordance between Centrin1-GFP live tracking and Cenexin endpoint classification. **H₁ is a standalone result — the first open-source centrosome-aware lineage tracking platform with night vision and glove-box at $24K.**
>
> **H₂ (Biology — SECONDARY):** In RPE1-hTERT, the daughter cell inheriting the mature mother centrosome (higher _M_) forms a primary cilium significantly earlier than its sister (shorter time-to-ciliogenesis within 48h), after controlling for cell size.
>
> **H₃ (Fate — TERTIARY, NPCs):** In hTERT-NPCs, mature mother centrosome inheritance → higher probability of maintaining progenitor identity (Nestin⁺/Sox2⁺) vs. differentiation (Tuj1⁺/GFAP⁺).
>
> H₁ validates the instrument. H₂ is the biological discovery in RPE1. H₃ extends to a fate-relevant model. **If H₁ fails, H₂ and H₃ are uninterpretable.** The platform must work before biology can be tested.

### 0.5. Two Molecular Pathways (Mechanism)

> Centrosome maturation state may influence daughter cell behavior through two non-mutually-exclusive pathways, both demonstrated in human cells:
>
> **Pathway A — Spindle asymmetry (Thomas & Meraldi 2024, PMID 39012627):** Cenexin → Plk1 → pericentrin/γ-tubulin/Cdk5Rap2 → 3.1% spindle length asymmetry → daughter cell size difference → differential cilium assembly kinetics. Demonstrated in human RPE1 and MCF10A cells.
>
> **Pathway B — Asymmetric protein degradation (POSSIBLE EXPLANATION, NOT TESTED HERE):** Mother centrosome concentrates phospho-β-catenin and polyubiquitinated proteins targeted for proteasomal degradation → asymmetric inheritance → COULD influence Wnt transcriptional programs. Segregation demonstrated in human ESC/Cos7 (Fuentealba et al. 2008, PMID 18511557). **Transcription consequences NOT tested in human cells.** Valdes Michel & Phillips 2025 (PMID 39813084) shows analogous mechanism in C. elegans (SYS-1/β-catenin at centrosome). **ARGUS-LP_OS does NOT test this mechanism.** Our goal is to establish whether the centrosome age→fate CORRELATION exists. Molecular mechanism testing requires separate biochemical experiments beyond this platform's scope.
>
> Both pathways predict the same observable: daughter inheriting the mature mother centrosome behaves differently. ARGUS-LP_OS measures the output. Phase 2 (Odf2 KO with domain deletions) dissects which pathway dominates.

### 0.6. Model System Clarification

> **RPE1-hTERT** is an epithelial cell line used for **platform validation** and **cilium kinetics** (H₂). RPE1 does not undergo asymmetric fate-determining divisions — cilium formation is a cell cycle response (G1→G0), not a terminal fate decision. H₂ measures whether centrosome age predicts **timing of cilium assembly**, a quantitative, objectively measurable phenotype with a known baseline (Anderson & Stearns 2009: 94% asymmetric cilium growth).
>
> **hTERT-NPCs** are the **fate model** (H₃). Royall 2023 demonstrated mother centrosome → self-renewal in **organoid-derived** NPCs. **⚠️ Critical caveat:** Royall used hESC-derived 3D organoids, not hTERT-immortalized 2D monolayer. hTERT-NPCs may differ in centrosome asymmetry. **Pilot NPC** (10 pairs, 48h, CYTOO) validates centrosome asymmetry in 2D before main experiment. Go/No-Go: ≥70% pairs must show Cenexin asymmetry. If <70% → H₃ downgraded to exploratory; primary focus remains on RPE1 (H₂).
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

**SNR thresholds:** Centrin1-GFP spot SNR ≥5 at ≤5% LED, ≤200 ms. Below → excluded. **Missing frames:** <5% → interpolation. >5% → pair excluded. **Data:** BioImage Archive / Zenodo (CC0) upon publication.

---

## 2. Controls and Confounds

| Confound | Control |
|----------|---------|
| Centrin1-GFP/H2B-GFP may alter centrosome/cell cycle | Untagged RPE1 vs. GFP-RPE1: compare cilium kinetics in Pilot 1. Δ>10% → use lower-expression clone. **Loncarek 2008 (PMID 18297061):** Centrin1 overexpression → aberrant centriole duplication. Use weak promoter (EF1α-short) if needed. |
| IR 850 nm prolonged exposure (48h) — phototoxicity, heating | IR-ON vs. IR-OFF arms in **Pilot 0.5**: viability (Live/Dead), proliferation (EdU), ROS (CellROX), apoptosis (caspase-3/7) at 0/24/48h. Δ>10% in any metric → reduce IR duty cycle or switch to pulsed mode (1s/10min). Kiepas et al. 2020 (PMID 32111840): 850 nm safe for long-term live-cell imaging. |
| Water immersion objective evaporation → focus drift | Automated water dispenser + saturated humidity in glove-box. Monitor focus drift with GFP beads |
| Cenexin appendages disassemble during mitosis | Pilot 1: Cenexin IF at interphase/prophase/metaphase/telophase in synchronized cells. If >20% variation → use Ninein co-stain |
| Cenexin _M_ ≠ direct age measurement | Pilot 1: Centrin1-Dendra2 photoconversion calibration. Compare Dendra2-age vs. Cenexin-age. Concordance <90% → Dendra2 becomes primary age marker |
| LED 488 nm phototoxicity (≤200 ms, ≤5% power) | Dark control (no LED) vs. LED protocol. Viability ≥90% in Pilot 1 |
| Serum starvation effects on biology | Test in Pilot 2: ±serum conditions. If serum alters M→cilium → use cycling conditions |
| CYTOO retention >48h unknown | Pilot 2: test both 48h and 72h. If 72h retention <80% but 48h ≥80% → use 48h protocol. Fallback for both: gridded microwell dishes |
| 3.1% spindle asymmetry biologically meaningful? | Tested by experiment: if M (continuous) does NOT predict cilium timing → 3.1% below functional threshold |
| Stochastic inheritance vs. age effect | Anderson 2009: 94% asymmetry despite 50% random inheritance → age EFFECT dominates stochasticity. Control: randomize centrosome inheritance (Ninein KD, Royall 2023) → asymmetry should drop to ~50% if age is causal. |

---

## 3. The Experiment: Sister Tracking

### 1.1. Method

| Step | Action |
|:----:|--------|
| 1 | RPE1-hTERT Centrin1-GFP + H2B-GFP divide inside glove-box |
| 2 | **Live tracking:** Centrin1-GFP follows centriole POSITIONS through mitosis |
| 3 | Sisters tracked on CYTOO 2-cell islands for 48h. **H₂ analysis: FIRST cell cycle only** — time from cytokinesis to cilium ≥1 µm. Anderson & Stearns 2009 showed asymmetry in the immediate G1 phase; multi-generation tracking is not required for H₂. |
| 4 | **Lineage tree:** track mother→daughters→granddaughters→great-granddaughters |
| 5 | **Endpoint:** fix, Cenexin antibody → CLASSIFY + acetylated tubulin → cilium |
| 6 | **Primary analysis:** time-to-ciliogenesis (Kaplan-Meier, hazard ratio) as function of _M_ |
| 7 | **Secondary:** cilium presence (binary, McNemar) + Ki67 (proliferation status) |

**H₂ design rationale:** Anderson & Stearns 2009 demonstrated cilium asynchrony in the **first G1 phase** after mitosis. ARGUS-LP_OS quantifies this with time-to-event resolution. **One cell cycle is sufficient for H₂** — the mother→daughter cilium timing comparison. Multi-generation lineage is NOT required for the primary H₂ endpoint. This simplifies the experiment and eliminates the CYTOO multi-generation limitation.

**Lineage design (H₃ only):** For NPC fate tracking, larger CYTOO patterns (8-cell islands) or gridded microwells are used to accommodate 2-3 generations. Alternatively, micromanipulator-assisted sister separation (ARGUS-OS3) enables clean multi-generation tracking.

**Mitosis detection:** H2B-GFP chromatin condensation triggers 1-2 min imaging, ensuring centriole distribution is captured at the critical moment.

**Competing risks:** Cells that divide before forming a cilium are treated as competing events (Fine-Gray subdistribution hazard model, with division as the competing risk). Cells that neither divide nor form a cilium by 48h are right-censored.

**CYTOO note:** No published data on 72h micropattern culture. Primary protocol: 48h (within published CYTOO range). Pilot 2 tests both 48h and 72h. Fallback: gridded microwell dishes.

### 1.2. Endpoints

| Endpoint | Type | Measurement | Analysis |
|----------|:----:|-------------|----------|
| **Time-to-ciliogenesis** | 🎯 Primary | Hours from cytokinesis to acetylated tubulin⁺ cilium ≥1 µm | Kaplan-Meier, Cox PH (hazard ratio per unit _M_) |
| Cilium presence at 48h | Secondary | Binary (yes/no) | McNemar (paired) |
| Ki67 status | Secondary | Binary (Ki67⁺/Ki67⁻) | McNemar (paired) |
| Differentiation (NPCs) | Tertiary | Nestin/Sox2 → Tuj1/GFAP | Fisher exact |

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
coxph(Surv(time_to_cilium, cilium_status) ~ M + CellArea + DivisionNumber + cluster(MotherID))
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

**Target: N=300 pairs with interim analysis at N=150.** At N=200, Fine-Gray with ICC ρ=0.3, 20% attrition, 30% competing risk (division before cilium): effective N ≈ 86 pairs, power ~68% for HR=1.35. **N=300** provides effective N ≈ 129 pairs, power **82%** at HR=1.35. Interim at N=150: if HR<1.15 → escalate to N=400 or stop for futility. ICC estimated in Pilot 3, final N adjusted.

**Multiple testing protocol (preregistered on OSF):** Hierarchical gatekeeping for primary→secondary. (1) Primary: time-to-cilium → if p<0.05, test secondaries. (2-4) Secondaries: cilium binary, Ki67, NPC markers — Benjamini-Hochberg FDR (q<0.1) within this level. If primary p≥0.05 → all secondaries descriptive only.

**Power note:** At N=300 with ICC ρ=0.3, Fine-Gray competing risk model: effective N ≈ 129 pairs, power 82% at HR=1.35. Interim analysis at N=150: if HR<1.15 → escalate to N=400 or stop for futility.

**Stop-rule:** If Pilot 3 (50 pairs) shows HR<1.1 for time-to-ciliogenesis → the 3.1% spindle asymmetry is below functional threshold for this phenotype. Redesign (increase serum starvation, test NPCs). **Sensitivity:** If interim at N=150 shows HR<1.2 → escalate to N=500. At HR=1.2, N=500 with ICC=0.3 gives ~78% power.

**Model (full):**
```
coxph(Surv(time_to_cilium, cilium_status) ~ M + CellArea + DivisionNumber + Ki67 + strata(Generation) + cluster(MotherID))
```

---

## 4. Cell Strategy

| Stage | System | Duration | Go/No-Go |
|:-----:|--------|:--------:|----------|
| **Pilot 0** | GFP beads, 7 days, 60×/1.2 NA | 1 week | Drift <5 µm/24h |
| **Pilot 1** | RPE1 Centrin1-GFP + Cenexin fix + phototoxicity + EdU + TOP/FOP Wnt reporter | 3 days | Centrin-Cenexin ≥90% + viability ≥90% + cell cycle stable + prolif. Δ<5% + Wnt asymmetry (exploratory) |
| **Pilot 2** | CYTOO islands, 48h + 72h, 10 pairs each | 1 week | Cell retention ≥80% at both timepoints. 72h optional if ≥80%. |
| **Pilot 3** | RPE1, 50 pairs | 2 weeks | Effect size for final N |
| **Main RPE1** | RPE1-hTERT, 300 pairs, 48h (H₂: 1st cycle cilium timing) | 4 weeks | Primary: time-to-ciliogenesis |
| **Main NPCs** | hTERT-NPCs, 100 pairs, lineage tree (3 gen). **Gated:** Pilot NPC (10 pairs, 48h) must confirm centrosome asymmetry before main. | 4 weeks | Primary: Nestin→Tuj1/GFAP fate |
| **Pilot NPC** | hTERT-NPCs, CYTOO 48h, 30 pairs + Nestin/Sox2/Tuj1 IF | 2 weeks | Go: ≥50% Nestin⁺/Sox2⁺ maintenance in 2D. Quantify Cenexin asymmetry distribution for power calc. |
| **Phase 2 (v2.0)** | RPE1 Odf2 KO + domain deletions (Tateishi 2013) | 4 weeks | Structural necessity |
| **Phase 3 (v3.0)** | hTERT-NPCs + ExM endpoint | 6 weeks | Progenitor map |

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

**Experimental design (domain deletions, validated per Tateishi 2013):**

| Group | Construct | Tateishi 2013 phenotype | Prediction for ARGUS |
|:-----:|-----------|--------------------------|----------------------|
| WT | — | Normal appendages + cilia | 94% asymmetry (baseline) |
| Odf2⁻/⁻ | — | No appendages, no cilia | No cilia, no asymmetry |
| **Odf2⁻/⁻ + Odf2(FL)** | Full-length Odf2-GFP | Full rescue: DA+SA+, cilia+ | **Positive control.** Appendages + cilia restored → asymmetry restored |
| **Odf2⁻/⁻ + Odf2(Δ188-806)** | Central domain deletion | **DA+SA−.** Distal appendages present, subdistal absent. Cilia form but are abnormal (reduced frequency, shorter) | **Key experimental group.** Tests whether distal appendages ALONE sufficient for centrosome-age-dependent asymmetry |
| **Odf2⁻/⁻ + Odf2(Δ1-59)** | N-terminal deletion | **No centriole recruitment.** Does NOT localize to basal bodies. No appendages, no cilia | **Negative control.** Confirms recruitment is required |
| **Odf2⁻/⁻ + Odf2(ΔC)** | C-terminal deletion | Centrosome binding intact, but NO appendage formation | **Pharmacological control.** Separates centrosome binding from appendage function |

**Why this replaces HDAC6i:** Wang 2025 (PMID 40167251) is a review — no experimental data on Odf2⁻/⁻ rescue. PubMed search: 0 results for HDAC6i+Odf2 KO. Tateishi 2013 provides validated domain-level resolution. **Risk:** Tateishi used mouse F9 cells. Human RPE1 Odf2 constructs must be validated — this is a separate engineering task (6-8 weeks).

**Centrosome age determination in Odf2-KO:** Without Cenexin/Odf2, the standard age marker is absent. **Inducible Odf2 KO** (tetracycline-inducible shRNA or auxin-inducible degron). Induce KO after 1-2 Cenexin-positive divisions → backtrack from last Cenexin⁺ frame. **Plan B:** If inducible KO fails (leaky expression, incomplete KO, or toxicity) → use **Centrin1-Dendra2 photoconversion** as primary age marker (independent of appendage proteins). Photoconvert in G1 → red signal marks older centriole → track through KO. **Plan C:** Pharmacological Plk1 inhibition (BI 2536, 10 nM) — blocks Cenexin→Plk1→γ-tubulin axis without destroying centrosome structure, providing orthogonal test of the maturation pathway.

---

## 6. Optical Design

| Objective | Resolution | Centriole gap at MITOSIS (>5 µm) | Cost |
|-----------|:----------:|:-------------------------------:|:----:|
| **60×/1.2 NA WI** | ~248 nm | ✅ Easily resolved | $3,500 |

**Cenexin calibration:** FITC calibration beads (Spherotech, 2.5 µm) imaged in each experiment. Cenexin intensity normalized to bead fluorescence → cross-experiment comparable _M_. Threshold calibrated via ROC in Pilot 1. **Age validation:** Centrin1-Dendra2 photoconversion in Pilot 1 provides orthogonal age readout.

**Phase 3 (v3.0) option:** Expansion microscopy (ExM, ~4× physical expansion) for super-resolved endpoint centriole analysis.

### 6.1. Comparison with Existing Platforms

| System | Cost | 48h autonomy | Centrosome tracking | Open source |
|--------|:----:|:-----------:|:-------------------:|:-----------:|
| LUMICKS C-Trap | ~$200K | ❌ | ❌ | ❌ |
| Molecular Devices ImageXpress | ~$150K | ✅ | ❌ | ❌ |
| Nikon Ti2-E + OKO Lab | ~$80K | Partial | ❌ | ❌ |
| **ARGUS-LP_OS** | **$24K** | **✅** | **✅** | **✅ GPLv3/CC-BY-SA** |

> ARGUS-LP_OS is 3-8× cheaper and the ONLY platform designed for centrosome-aware lineage tracking. Open hardware enables community improvements impossible with proprietary systems.

---

## 7. Budget

| Line item | $ |
|-----------|--:|
| OpenFlexure v6.1.5 (ASA) | 600 |
| RasPi 5 + 1TB SSD | 250 |
| Camera HQ + RMS | 150 |
| **60×/1.2 NA WI** | 3,000 |
| LED 488 nm + filters | 450 |
| IR LED 850 nm + Camera NoIR (night vision) | 40 |
| Incubator CO₂ | 6,000 |
| O₂ control | 300 |
| Jetson Orin NX 16GB | 500 |
| RasPi 5 + Hailo-8L | 160 |
| Centrin1-GFP RPE1 | 0–1,000 |
| Cenexin antibody | 200 |
| RPE1-hTERT + NPCs | 600 |
| CYTOO coverslips ×20 | 500 |
| Tetraspeck beads | 200 |
| IF antibodies | 200 |
| Consumables | 300 |
| **Subtotal** | **13,450–14,450** |
| **+20% contingency** | **2,690–2,890** |
| **SNR fallback (sCMOS)** | 1,800 |
| **TOTAL (max)** | **$19,132** |

> Экономия: убраны микроманипулятор ($1,500), puller ($1,500), капилляры ($200). CYTOO — основной метод. Night vision (+$40) добавлен.

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

## 9. References

1. Anderson CT, Stearns T. *Curr Biol* 19:1498–1502 (2009). **PMID: 19682908.**
2. Wang X et al. *Nature* 461:947–955 (2009). **PMID: 19829375.**
3. Royall LN et al. *eLife* 12:e83157 (2023). **PMID: 37882444.**
4. Yamashita YM et al. *Science* 315:518–521 (2007). **PMID: 17255513.**
5. Paridaen JT et al. *Cell* 155:333–344 (2013). **PMID: 24120134.**
6. Barandun N et al. *Cell Rep* 44:115127 (2025). **PMID: 39764850.**
7. Reina J, Gonzalez C. *Phil Trans R Soc B* 369:20130466 (2014). **PMID: 25047620.**
8. Chatterjee A et al. *Cerebellum* 17:685–691 (2018). **PMID: 29663194.**
9. Conduit PT, Raff JW. *Curr Biol* 20:2187–2192 (2010). **PMID: 21145745.**
10. **Thomas A, Meraldi P.** Centrosome age breaks spindle size symmetry. *J Cell Biol* 223(8) (2024). **PMID: 39012627.**
11. **Tateishi K et al.** Two appendages homologous between basal bodies and centrioles are formed using distinct Odf2 domains. *J Cell Biol* 201(3):417–425 (2013). **PMID: 24189274.**
12. Ishikawa H et al. Odf2-deficient mother centrioles lack distal/subdistal appendages and the ability to generate primary cilia. *Nat Cell Biol* 7:517–524 (2005). **PMID: 15852003.**
13. **Wang Z et al.** HDAC6 in Ciliopathies. *Adv Sci* (2025). **PMID: 40167251.**
14. Gaudin N et al. *eLife* 11:e72382 (2022). **PMID: 35319462.**
15. Collins JT et al. *Biomed Opt Express* 11:2447–2460 (2020). **PMID: 32499936.**
16. Knapper J et al. *J Microsc* 285:40–51 (2022). **PMID: 34625963.**
17. Stringer C et al. *Nat Methods* 18:100–106 (2021). **PMID: 33318659.**
18. Arbelle A et al. *Med Image Anal* 47:109–126 (2018). **PMID: 29747154.**
19. Loncarek J et al. *Nat Cell Biol* 10:322–328 (2008). **PMID: 18297061.**
20. Chen C, Yamashita YM. *Open Biol* 11:200314 (2021). **PMID: 33435817.**
21. Zhao X et al. *Nat Commun* 16:10728 (2025). **PMID: 41315244.**
22. Tozer S et al. *Neuron* 93:347–361 (2017). **PMID: 28132826.**
23. Nayak SC, Radha V. *J Cell Sci* 133:jcs243113 (2020). **PMID: 32371504.**
24. **Valdes Michel MF, Phillips BT.** SYS-1/β-catenin inheritance and regulation by Wnt signaling during asymmetric cell division. *Mol Biol Cell* 36(3):ar25 (2025). **PMID: 39813084.** — **C. elegans.** Centrosomal SYS-1 degradation during ACD. Foundational mechanism paper (invertebrate). NOT human — do not cite as human mechanism.
25. **Goutas A, Trachana V.** Stem cells' centrosomes. *World J Stem Cells* 13(9):1177-1196 (2021). **PMID: 34630857.** — Review: centrosome-directed stem cell fate manipulation.
26. **Barandun N et al.** Targeted localization of the mother centrosome in CD8+ T cells undergoing ACD promotes memory formation. *Cell Rep* 44(1):115127 (2025). **PMID: 39764850.** — Mother centrosome → effector-like daughter (NOT memory) via ninein.
27. **Fuentealba LC et al.** Asymmetric mitosis: Unequal segregation of proteins destined for degradation. *Proc Natl Acad Sci USA* 105(22):7732-7737 (2008). **PMID: 18511557.** — Human ESC + Cos7 + Drosophila. p-β-catenin & polyubiquitinated proteins at mother centrosome → asymmetric inheritance. Transcription consequences NOT tested in human cells.
28. **Goutas A, Trachana V.** Stem cells' centrosomes. *World J Stem Cells* 13(9):1177-1196 (2021). **PMID: 34630857.**
29. **Januschke J, Llamazares S, Reina J, Gonzalez C.** Drosophila neuroblasts retain the daughter centrosome. *Nat Commun* 2:243 (2011). **PMID: 21407209.** — Daughter centrosome → stem cell. Tissue polarity reversal vs. mammalian systems.

---

*Version 53 — 2026-07-19. Central Hypothesis: Valdes Michel (C.elegans)→Fuentealba (human). Valdes Michel annotated as invertebrate. Fuentealba: transcriptional consequences NOT tested. Species caveats §0.6. Controls §1. H₂=kinetics. 28 refs.*
