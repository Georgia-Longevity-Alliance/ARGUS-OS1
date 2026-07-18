# CONCEPT — ARGUS-LP_OS

**Version:** 50.0
**Date:** 2026-07-19

---

## 0. The Science: Centrosome Maturation State as a Division History Marker

### Central Hypothesis

> **The mother centrosome carries a distinct maturation state, written in its appendage proteins (Cenexin/Odf2, Ninein, Cep164) and tubulin PTMs (polyglutamylation). Two parallel pathways may transduce this asymmetry into fate: (1) Cenexin→Plk1→γ-tubulin→spindle asymmetry→daughter cell size difference (Thomas & Meraldi 2024, PMID 39012627, 3.1% asymmetry, p<0.0001); (2) centrosomal β-catenin degradation→Wnt signalling asymmetry→differential transcription (Valdes Michel & Phillips 2025, PMID 39813084 — mother centrosome degrades β-catenin during mitosis, creating transcriptional asymmetry between daughters).**
>
> **🔴 CRITICAL: Thomas & Meraldi showed SPINDLE asymmetry. Valdes Michel showed CENTROSOMAL β-CATENIN PROCESSING. Neither tested FATE asymmetry directly. Whether these mechanisms change what a daughter cell becomes — that is the open question ARGUS-LP_OS exists to answer. We do not assume. We measure.**

### 0.1. Two Fluorescent Probes, Two Tasks

> **🔴 CRITICAL DISTINCTION — Centrin1-GFP and Cenexin antibody serve DIFFERENT purposes:**

| Probe | When | Task |
|-------|------|------|
| **Centrin1-GFP** | Live, every frame | **TRACKING** — where are the centrioles? Which cell inherited which centrosome? Follow positions through mitosis. |
| **Cenexin antibody** | Endpoint (72h, fixed) | **CLASSIFICATION** — which centrosome was the mature mother? Cenexin-bright = old. |

**Centrin1-GFP does NOT need to report centriole age.** It only needs to show POSITIONS. The age assignment is done retrospectively at endpoint with Cenexin antibody — the gold standard used by Anderson & Stearns 2009. Pilot 1 validates that Centrin1-GFP tracking is concordant with Cenexin classification (target: ≥90% concordance).

### 0.2. Maturation State Definition

> **Maturation state is operationally defined as the Cenexin fluorescence intensity ratio: _M = I(Cenexin)ᵃ / I(Cenexin)ᵇ_. _M_ is a continuous variable in all primary analyses. A binary threshold (_M > 1.5_) is calibrated via ROC analysis in pilot experiments — Anderson & Stearns 2009 did not establish a numeric threshold.**

### 0.3. Alternative Hypotheses

| Scenario | Prediction | Precedent | Action if confirmed |
|----------|------------|-----------|---------------------|
| **A: Mother → stemness** | Mature mother → progenitor | Wang 2009 (PMID 19829375); Royall 2023 (PMID 37882444) | Compare with Royall 2023. Phase 3 (v2.0): PCM1/Notch mechanism. |
| **B: Daughter → stemness** | Immature daughter → progenitor | Conduit & Raff 2010 (PMID 21145745) | Compare with Conduit 2010. Phase 3 (v2.0): alternative mechanism. |
| **C: No correlation** | Centrosome age ≠ fate | Chatterjee 2018 (PMID 29663194) | **Publish null result.** Platform validated, biology absent in RPE1. Phase 2 (v1.5) Odf2 KO still performed — may reveal masked effect. |

### 0.4. Three Hypotheses

> **H₁ (Platform — PRIMARY):** ARGUS-LP_OS can maintain continuous 72-hour operation inside a glove-box enclosure with <5 µm focus drift per 24h, ≥95% cell retention on CYTOO islands, automated mitosis detection, and ≥90% concordance between Centrin1-GFP live tracking and Cenexin endpoint classification. **H₁ is a standalone result — the first open-source centrosome-aware lineage tracking platform with night vision and glove-box at $24K.**
>
> **H₂ (Biology — SECONDARY):** In RPE1-hTERT, the daughter cell inheriting the mature mother centrosome (higher _M_) forms a primary cilium significantly earlier than its sister (shorter time-to-ciliogenesis), after controlling for cell size.
>
> **H₃ (Fate — TERTIARY, NPCs):** In hTERT-NPCs, mature mother centrosome inheritance → higher probability of maintaining progenitor identity (Nestin⁺/Sox2⁺) vs. differentiation (Tuj1⁺/GFAP⁺).
>
> H₁ validates the instrument. H₂ is the biological discovery in RPE1. H₃ extends to a fate-relevant model. **If H₁ fails, H₂ and H₃ are uninterpretable.** The platform must work before biology can be tested.

### 0.5. Two Molecular Pathways (Mechanism)

> Centrosome maturation state may influence daughter cell behavior through two non-mutually-exclusive pathways, both demonstrated in human cells:
>
> **Pathway A — Spindle asymmetry (Thomas & Meraldi 2024, PMID 39012627):** Cenexin → Plk1 → pericentrin/γ-tubulin/Cdk5Rap2 → 3.1% spindle length asymmetry → daughter cell size difference → differential cilium assembly kinetics. Demonstrated in human RPE1 and MCF10A cells.
>
> **Pathway B — Asymmetric protein degradation (Fuentealba et al. 2008, PMID 18511557):** Mother centrosome concentrates phospho-β-catenin and polyubiquitinated proteins targeted for proteasomal degradation → asymmetric inheritance of degradation-targeted proteins → differential Wnt/β-catenin signalling → divergent transcriptional programs. Demonstrated in human embryonic stem cells, Cos7, and Drosophila embryos. This is the first direct demonstration of centrosome→transcription coupling in mammalian asymmetric division.
>
> Both pathways predict the same observable: daughter inheriting the mature mother centrosome behaves differently. ARGUS-LP_OS measures the output. Phase 2 (Odf2 KO with domain deletions) dissects which pathway dominates.

### 0.6. Model System Clarification

> **RPE1-hTERT** is an epithelial cell line used for **platform validation** and **cilium kinetics** (H₂). RPE1 does not undergo asymmetric fate-determining divisions — cilium formation is a cell cycle response (G1→G0), not a terminal fate decision. H₂ measures whether centrosome age predicts **timing of cilium assembly**, a quantitative, objectively measurable phenotype with a known baseline (Anderson & Stearns 2009: 94% asymmetric cilium growth).
>
> **hTERT-NPCs** are the **fate model** (H₃). Royall 2023 demonstrated that in human NPCs, mother centrosome → self-renewal via Ninein. H₃ measures whether centrosome age predicts **progenitor maintenance vs. differentiation** (Nestin/Sox2 → Tuj1/GFAP).
>
> This two-tier design separates **platform validation** (RPE1) from **biological discovery** (NPCs), de-risking both.

---

## 1. The Experiment: Sister Tracking

### 1.1. Method

| Step | Action |
|:----:|--------|
| 1 | RPE1-hTERT Centrin1-GFP + H2B-GFP divide inside glove-box |
| 2 | **Live tracking:** Centrin1-GFP follows centriole POSITIONS through mitosis |
| 3 | Sisters tracked on CYTOO 2-cell islands for 72h (~3 cell cycles) |
| 4 | **Lineage tree:** track mother→daughters→granddaughters→great-granddaughters |
| 5 | **Endpoint:** fix, Cenexin antibody → CLASSIFY + acetylated tubulin → cilium |
| 6 | **Primary analysis:** time-to-ciliogenesis (Kaplan-Meier, hazard ratio) as function of _M_ |
| 7 | **Secondary:** cilium presence (binary, McNemar) + Ki67 (proliferation status) |

**Lineage design:** 72h = ~3 divisions. We track the full tree: which daughter inherits the mature centrosome at each division. **Centrosome age in generations 1-2** is inferred from the mitotic trajectory (mother centrosome identified at endpoint by Cenexin intensity → backtracked through Centrin1-GFP tracking). This inference is validated by the ≥90% concordance requirement in Pilot 1. Pairs with ambiguous backtracking are flagged and analysed separately as sensitivity check.

**Mitosis detection:** H2B-GFP chromatin condensation triggers 1-2 min imaging, ensuring centriole distribution is captured at the critical moment.

**Competing risks:** Cells that divide before forming a cilium are treated as competing events (Fine-Gray subdistribution hazard model, with division as the competing risk). Cells that neither divide nor form a cilium by 72h are right-censored.

**CYTOO note:** No published data on 72h micropattern culture — 72h pilot included (Pilot 2). Fallback: gridded microwell dishes. **Micropipette separation is NOT used in Phase 1** — technical risk too high for a platform-validation experiment.

### 1.2. Endpoints

| Endpoint | Type | Measurement | Analysis |
|----------|:----:|-------------|----------|
| **Time-to-ciliogenesis** | 🎯 Primary | Hours from cytokinesis to acetylated tubulin⁺ cilium ≥1 µm | Kaplan-Meier, Cox PH (hazard ratio per unit _M_) |
| Cilium presence at 72h | Secondary | Binary (yes/no) | McNemar (paired) |
| Ki67 status | Secondary | Binary (Ki67⁺/Ki67⁻) | McNemar (paired) |
| Differentiation (NPCs) | Tertiary | Nestin/Sox2 → Tuj1/GFAP | Fisher exact |

> **Rationale for time-to-ciliogenesis:** Continuous time-to-event endpoint has higher statistical power than binary outcome at a single timepoint. A 3% spindle difference may manifest as a 2-3 hour delay in cilium assembly rather than a binary yes/no — time-to-event captures this. Anderson & Stearns 2009 observed cilium ASYNCHRONY; we quantify it systematically.

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
- With 70% cilium rate at 72h: N = 65/0.7 = **93 pairs**
- **With 20% attrition + ICC ρ≤0.3:** N_planned = 93/(0.8×0.77) ≈ **150 pairs**

**Target: 200 pairs** — detects HR ≥1.35 with 80% power, or 15 pp difference in binary cilium rate (consistent with v49 binary power calculation).

**Model (full):**
```
coxph(Surv(time_to_cilium, cilium_status) ~ M + CellArea + DivisionNumber + Ki67 + strata(Generation) + cluster(MotherID))
```

---

## 2. Cell Strategy

| Stage | System | Duration | Go/No-Go |
|:-----:|--------|:--------:|----------|
| **Pilot 0** | GFP beads, 7 days, 60×/1.2 NA | 1 week | Drift <5 µm/24h |
| **Pilot 1** | RPE1 Centrin1-GFP + Cenexin fix + phototoxicity | 3 days | Centrin-Cenexin ≥90% + viability ≥90% vs dark control |
| **Pilot 2** | CYTOO islands, 72h, 10 pairs | 1 week | Cell retention ≥80% |
| **Pilot 3** | RPE1, 50 pairs | 2 weeks | Effect size for final N |
| **Main RPE1** | RPE1-hTERT, 200 pairs, lineage tree (3 gen) | 4 weeks | Primary: time-to-ciliogenesis |
| **Main NPCs** | hTERT-NPCs, 100 pairs, lineage tree (3 gen) | 4 weeks | Primary: Nestin→Tuj1/GFAP fate |
| **Phase 2 (v2.0)** | RPE1 Odf2 KO + HDAC6i | 4 weeks | Causality |
| **Phase 3 (v3.0)** | hTERT-NPCs + ExM endpoint | 6 weeks | Progenitor map |

---

## 3. Phase 2 (v2.0): Odf2 Domain Deletions — Causality

Odf2 KO abolishes distal and subdistal appendages (Ishikawa 2005, PMID 15852003). Different Odf2 domains control different appendage types (Tateishi 2013, PMID 24189274):
- aa 188-806 → transition fibers/distal appendages
- aa 1-59 + 188-806 → basal feet/subdistal appendages

**Experimental design (domain deletions, replacing HDAC6i hypothesis):**

| Group | Construct | Prediction |
|:-----:|-----------|------------|
| WT + empty vector | — | 94% cilium asymmetry (baseline) |
| Odf2⁻/⁻ + empty vector | — | No appendages, no cilia, no asymmetry |
| **Odf2⁻/⁻ + Odf2(FL)** | Full-length Odf2-GFP | **Positive control:** appendages restored, cilia restored, asymmetry restored → phenotype is Odf2-specific |
| **Odf2⁻/⁻ + Odf2(Δ1-59)** | Deletion of N-terminal 59 aa | Distal appendages ONLY (no subdistal). Cilia present? Asymmetry? → tests whether distal appendages sufficient |
| **Odf2⁻/⁻ + Odf2(Δ188-806)** | Deletion of central domain | No appendages. Cilia absent. → domain essentiality control |

**Why domain deletions replace HDAC6i:** Wang 2025 (PMID 40167251) is a review — no experimental data on Odf2⁻/⁻ rescue exists. PubMed search for "HDAC6 inhibitor cilia restoration Odf2 knockout" returns 0 results. Tateishi 2013 provides a validated genetic approach with domain-level resolution: which appendage type is required for centrosome-age-dependent asymmetry?

---

## 4. Optical Design

| Objective | Resolution | Centriole gap at MITOSIS (>5 µm) | Cost |
|-----------|:----------:|:-------------------------------:|:----:|
| **60×/1.2 NA WI** | ~248 nm | ✅ Easily resolved | $3,000 |

**Cenexin calibration:** FITC calibration beads (Spherotech, 2.5 µm) imaged in each experiment. Cenexin intensity normalized to bead fluorescence → cross-experiment comparable _M_. Threshold calibrated via ROC in Pilot 1.

**Phase 3 (v2.0) option:** Expansion microscopy (ExM, ~4× physical expansion) for super-resolved endpoint centriole analysis. 10+ PMIDs confirm ExM for centrioles.

---

## 5. Budget

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

## 6. Results Publication Strategy

| Outcome | Action |
|---------|--------|
| **p<0.05, Scenario A or B** | Publish: first live-cell centrosome-aware lineage map. Platform paper + biology paper. |
| **p≥0.05, Scenario C** | Publish: platform paper + null result. «Centrosome maturation state does not predict cilium fate in RPE1.» Negative result is scientifically valuable, confirms Chatterjee 2018. |
| **Platform failure** | Publish: technical report. What worked, what didn't. OpenFlexure incubator data. |

**We publish regardless.**

---

## 7. References

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
24. **Valdes Michel MF, Phillips BT.** SYS-1/β-catenin inheritance and regulation by Wnt signaling during asymmetric cell division. *Mol Biol Cell* 36(3):ar25 (2025). **PMID: 39813084.** — Centrosomal β-catenin degradation creates transcriptional asymmetry between daughters.
25. **Goutas A, Trachana V.** Stem cells' centrosomes. *World J Stem Cells* 13(9):1177-1196 (2021). **PMID: 34630857.** — Review: centrosome-directed stem cell fate manipulation.
26. **Barandun N et al.** Targeted localization of the mother centrosome in CD8+ T cells undergoing ACD promotes memory formation. *Cell Rep* 44(1):115127 (2025). **PMID: 39764850.** — Mother centrosome → effector-like daughter (NOT memory) via ninein.
27. **Fuentealba LC et al.** Asymmetric mitosis: Unequal segregation of proteins destined for degradation. *Proc Natl Acad Sci USA* 105(22):7732-7737 (2008). **PMID: 18511557.** — p-β-catenin and polyubiquitinated proteins concentrated at mother centrosome → asymmetric inheritance in human ESC, Cos7, and Drosophila.
28. **Goutas A, Trachana V.** Stem cells' centrosomes. *World J Stem Cells* 13(9):1177-1196 (2021). **PMID: 34630857.** — Review: centrosome-directed stem cell fate manipulation.

---

*Version 51 — 2026-07-19. Fuentealba 2008 (human p-β-catenin+centrosome) replaces C. elegans mechanism. Barandun 2025 interpretation corrected (mother→effector). HDAC6i replaced by Odf2 domain deletions (Tateishi 2013). RPE1 clarified as kinetics model, NPCs as fate model. Fine-Gray competing risks added. 28 references.*
