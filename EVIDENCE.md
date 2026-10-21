# EVIDENCE — ARGUS-OS1

**Updated:** 2026-07-28 (post 5-cycle peer review)

## Core Centriole Biology

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| 6684600 | Sulston et al. (1983) — Complete C. elegans invariant lineage | Sister-pair design |
| 37256957 | Kalbfuss & Gönczy (2023) — 88% centriole elimination in embryogenesis | H₀ baseline |
| 37414202 | Kalbfuss, Berger & Gönczy (2023) — Cell fate determines centriole fate | Null model predictor |
| 37963546 | Kalbfuss & Gönczy (2023) — Three-stage elimination model, review | Mechanism framework |
| 40475707 | Croisier, Kalbfuss & Gönczy (2025) — EM confirms centrioles in L1 rectal cells | Structural validation |

## Centriole Elimination Mechanism

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| 22492357 | Mikeladze-Dvali et al. (2012) — Active elimination in oogenesis, CGH-1 delays | Active mechanism evidence |
| 37987153 | Pierron, Kalbfuss & Gönczy (2023) — SAS-1 lost first; UPS localises to centrioles; proteasome inhibition delays elimination | SAS-1 validation marker; UPS mechanism |
| 31246171 | Magescas et al. (2019) — Two-step MTOC inactivation (eLife) | PCM inactivation → elimination |
| 33798427 | Magescas et al. (2021) — Acentriolar centrosome at ciliary base (Curr Biol) | Inactivation without elimination |
| 11371350 | O'Connell et al. (2001) — zyg-1, centriole duplication (Cell) | Transformation path (spermatogenesis) |

## PCM Asymmetry & MTOC Activity

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| 15572125 | Dammermann et al. (2004) — Centriole assembly requires PCM (Dev Cell) | SPD-2/PCM role |
| 17136092 | Pelletier et al. (2006) — Centriole assembly in C. elegans (Nature) | PCM → centriole |
| 30626640 | Pintard & Bowerman (2019) — Mitotic cell division in C. elegans (Genetics) | PLK-1/PCM |
| — | Ng, Magescas & Feldman (2025) — MTOC inactivation required for elimination (bioRxiv) | Causal evidence: MTOC activation prevents elimination |
| — | Gallaud et al. (2018) — Dynamic Polo/Centrobin exchange primes centrosome asymmetry (PLoS Biol) | SPD-2 endogeneity |

## Fate-Dependent Centriole Inheritance

| PMID | Finding | Pattern |
|:----:|---------|---------|
| 17255513 | Yamashita et al. (2007) — Drosophila male GSC: mother centrosome → stem cell (Science) | Both retain → stem gets OLD |
| 19829375 | Wang et al. (2009) — Mammalian radial glia: mother centrosome → progenitor (Nature) | Both retain → stem gets OLD |
| 21407209 | Januschke et al. (2011) — Drosophila neuroblast: daughter centrosome → stem cell (Nat Commun) | Elimination → stem gets YOUNG |
| 33435817 | Colicino & Hehnly (2021) — Centrosome-centric view review (Open Biol) | Review |
| 36988082 | Rostami et al. (2023) — Sperm centrioles segregate stochastically (Genetics) | Natural variation in C. elegans |

## Longevity Connection

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| 26488501 | Zacharias et al. (2015) — Wnt/β-catenin in C. elegans (PLoS Genet) | Developmental noise → aging |
| 38900346 | Molière et al. (2024) — DAF-2 degradation restores proteostasis; PFD-6 links HSF-1→DAF-16; centriole replication GO enrichment (GeroScience) | daf-2 experiment justification |

## Spindle Orientation

| PMID | Finding |
|:----:|---------|
| 38213110 | Zhao et al. (2024) — Dynein directs prophase centrosome migration (Genetics) |
| 38488018 | Kapoor & Kotak (2024) — Aurora A in C. elegans polarization (Development) |

## AI Pipeline

| Reference | Component |
|-----------|-----------|
| Bassett et al. (2026) — One Click Wonder (bioRxiv) | Segmentation engine (Cellpose) |
| Stringer et al. (2021) — Cellpose (Nat Methods) | Base model |
| — | StarDist — Fallback segmentation |
| — | TensorRT — Jetson FP16/INT8 optimization |

## Statistical Methods

| Reference | Method |
|-----------|--------|
| Kass & Raftery (1995) — Bayes factors (JASA) | BIC comparison framework |
| Rizopoulos (2023) — JMbayes2 (R package) | Joint longitudinal-survival models |
| Gronau et al. (2017) — bridgesampling (J Stat Softw) | Bayes factor computation |
| Tingley et al. (2014) — mediation (J Stat Softw) | SPD-2 mediation analysis |
| McElreath (2020) — Statistical Rethinking (CRC Press) | Bayesian workflow, informative priors |

## Motor Release (2026-07-23)
WilliamW (OpenFlexure Forum): Sangaboard firmware already has motor release command.
Not exposed in API — minimal software fix needed. Heat problem solved in software.

## Germline QC & Spermatogenesis (2026-10-12, Semantic Scholar alert)

> Master analysis: `~/Desktop/Services/docs/LITERATURE_ALERT_2026-10-12_Centrosome_Germline_G0.md`. All PMIDs verified via PubMed E-utilities 2026-10-12.

### ⭐⭐⭐ Centriole elimination in MAMMALIAN spermatogenesis (direct analog of C. elegans elimination)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42471456** | EMBO Rep (2026) — Basal body docking failure triggers **centriole clustering + elimination** in mammalian spermatogenesis | Validates platform hypothesis «centriole fate = retained/eliminated» beyond C. elegans → germline of mammals. New comparative target for OS1/OS2 |
| **41415467** | bioRxiv (2025) — Loss of cilia drives centriole clustering + elimination (mammalian spermatogenesis) | Same line (preprint) |

### Germ cell quality selection & non-apoptotic death (G0)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42182475** | Stark et al. 2026 (bioRxiv, Capel lab) — necroptosis of damaged MGCs during G0 arrest: ~70% PI+, DND1-lo (dsDNA breaks, mito dysfunction), pMLKL/RIPK3 at birth, NOT TNF/ZBP1; mito stress → DND1-lo | Model of cell-fate selection by quality: DND1-hi (healthy, high DNA-repair machinery) vs DND1-lo (damaged, necroptotic) — a phenotype readout relevant to lineage/fate tracking |
| **40780962** | Annu Rev Genet (2025) — Selective Quality Control in Mammalian Oogenesis | Conceptual basis of germline quality selection |
| **38826313** | bioRxiv (2024) — Germline status regulates somatic mitochondrial QC (C. elegans) | ⭐ Germline↔soma QC axis in C. elegans — directly relevant to ARGUS model |

### Intercellular bridges (ICB) — spermatogenesis structure & genome integrity

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42203835** | Cui et al. 2026 (Commun Biol) — ICB formation/function in male germlines (review): incomplete cytokinesis, cytoplasmic sharing, synchronization | ICB = candidate structures for live imaging of germ-cell cysts; cyst geometry records division pattern — relevant to pedigree/lineage mapping |
| **39929837** | Nat Commun (2025) — ICBs essential for **transposon repression and meiosis** in male germline | ICB → piRNA sharing → genome integrity (ties germline integrity to centriole/genome quality themes) |
| **38242343** | Dev Biol (2024) — ARF6 (ICB component) essential for spermatogenesis | Molecular component of ICB |
| **37039784** | FASEB J (2023) — Far1 KO → disrupted ICBs + spermatogenesis | Lipid/resource mechanism |
| **40581359** | Mol Hum Reprod (2025) — TTBK2 → sperm quality via centrosomal proteins + flagellar transport | Centrosome ↔ sperm quality |

### Notes
- These add a **mammalian germline elimination** strand to the existing C. elegans centriole-elimination core (Kalbfuss/Gönczy, 88%), strengthening the comparative claim that centriole fate is regulated.
- Stark et al. is a **preprint** (bioRxiv, CC BY-NC-ND, PMC13192861) — cite with caution; no causal test of quality-selection yet.

## Engineering / Platform Evidence — Axio Observer benchmark (2026-10-19)

> Master analysis: `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. All PMIDs verified via Europe PMC/NCBI 2026-10-19.

### ⭐ Hardware autofocus / focus-hold — OS1's main technical gap

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42274973** | Djafer-Cherif & Waclaw 2026 (J Microsc) — **Affordable fiducial marker strategy for reliable autofocus in long-term live microscopy** | ⭐ Open low-cost path to hardware focus-hold — P0 candidate for OpenFlexure (replaces stepper-Z drift) |
| **42525498** | Habte et al. 2026 (J Microsc) — Quantitative evaluation of **LED-based optical autofocus** module | Reproducible LED autofocus on own hardware |
| **42373656** | Wang et al. 2026 (Nat Commun) — Real-time robust autofocus for sustained scanning light-field (<2 µm error, 0.1 s) | Autofocus without hardware modification — alternative for multi-day |

### Phototoxicity — main biological confounder of long-term imaging

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42393487** | Stadter et al. 2026 (Arch Gynecol Obstet) — Phototoxicity of **brightfield** live-cell imaging on murine ovarian follicles | ⭐ Even transmitted light kills cells → justifies phototoxicity ceiling in Body Law + exposure minimisation in ALL channels |
| **28749075** | Icha et al. 2017 (BioEssays) — Phototoxicity in live fluorescence microscopy, and how to avoid it | Classic review — damage-reduction strategies |
| **23931522** | Magidson & Khodjakov 2013 (Methods Cell Biol) — Circumventing photodamage in live-cell microscopy | Practice: short exposures, sensitive cameras |
| **19261845** | Frigault et al. 2009 (J Cell Sci) — Live-cell microscopy: tips and tools | Classic live-cell contrast/environment |

### Lineage tracking / cell following (platform core)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42841415** | Girstmair et al. 2026 (Development) — **Mastodon: command center for large-scale lineage-tracing microscopy datasets** | ⭐ Lineage-conveyor tool — integrate into OS1/OS2 |
| **42261409** | Tran et al. 2026 (MicroPubl Biol) — **Lineage-resolved cell identities in uncompressed C. elegans embryos** | Direct precedent of lineage-resolved identity in C. elegans |
| **42499344** | Chandra et al. 2026 — Open-source longitudinal single-cell tracking pipeline | Open tracking pipeline + cell cycle |
| **42506143** | Martí-Pérez et al. 2026 (J Imaging) — Microscopy Cell Segmentation: review & benchmarking | Up-to-date segmentation choice (CellPose/StarDist) |

### Open hardware / live-cell (confirmation of ARGUS architecture)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42583731** | Malcolm et al. 2026 (J Cell Sci) — Removing barriers to advanced imaging + ML analysis | ⭐ OpenFlexure + ML = confirmation of ARGUS architecture |
| **36756063** | McDermott et al. 2023 (R Soc Open Sci) — OpenFlexure Voice Control + Blockly | Scripting OpenFlexure for autonomy |
| **41795377** | Moncada-Madrazo et al. 2026 (Biosens Bioelectron) — In-incubator chip-sized holographic microscope | Microscope-in-incubator concept for long OS2 runs |
| **42103520** | Knapper et al. 2026 (Int J Gynecol Cancer) — OpenFlexure in gynecological pathology | OpenFlexure real-world use beyond the lab |
| — | Malcolm et al. 2026 — Adapting OpenFlexure for Affordable Live-Cell Imaging (DOI 10.64898/2026.02.02.703252) | OpenFlexure live-cell adaptation (preprint) |

### Benchmark reference (vendor claims)
- **Zeiss Axio Observer 7** (Definite Focus 3, Colibri 7 LED, motorized Z/XY/revolver/condenser/filter, pco.edge 4.2 sCMOS, ZEN 3.3, Scanning Stage 130×100) + **Axio Observer live** (Glass Lid CO₂/O₂ heated, Temperature Controller, Heated Plate K, Z8+RTX A4000) — benchmark engineering set for multi-day live-cell.
- Competitors with analogous hardware autofocus: **Nikon PFS**, **Olympus TruFocus ZDC (IX3-ZDC2)**, **Leica AFC**. Benchtop class: **IncuCyte S3/SX5** (in-incubator).

### Notes
- Positions engineering as first-class evidence for the platform: focus-hold + environment + LED multi-channel are preconditions for the validity of multi-day lineage data, not conveniences.
- All vendor claims are flagged; independent verification is via the PMIDs in the tables above.

### In-situ cell isolation / automated laser targeting — Nikon GA+JOBS benchmark (2026-10-20)

> Master analysis: `../docs/NIKON_AUTOMATED_LASER_SORTING_ANALYSIS_2026-10-20.md` (index-level; also OS3). Primary paper read in full (open access). All PMIDs verified via Europe PMC 2026-10-20.

| Source | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **10.1017/qpb.2022.24** | Kaneshiro et al. 2022 (Quant Plant Biol) — **fully automated detect→classify→mask→IR-laser→verify loop** for in-situ cell isolation (NIS-Elements GA+JOBS, inverted Ti2-E); **positional info preserved** → continuous before/after lineage observation; target enrichment up to 8.3× | ⭐ Independent confirmation of ARGUS's **in-situ-elimination/positional-lineage paradigm** (vs FACS/microfluidics which destroy position). Citable in grants. |
| **25470130** | Gokce et al. 2014 (PLoS ONE) — **fully automated microfluidic fs-laser axotomy** in C. elegans (~17 s/worm) | Automated detect→laser loop in ARGUS's model organism |
| **19079252** | Kamei et al. 2009 (Nat Methods) — **IR-LEGO**: 1480 nm single-cell laser manipulation in C. elegans, 10⁵× water heating vs 440 nm | Single-cell laser precision in C. elegans (IR family) |
| **42234731** | van den Brink et al. 2026 (Sci Adv) — image-based phenotypic sorting with real-time NN analysis | Neural-network-driven automated selection — convergence with Cellpose+loop |
| **42669673** | Di Sante/Pezzotti et al. 2026 (Nat Commun) — **CALIPERS**: cell cycle-aware live imaging | Live-tracking platform pattern (OS1/OS2) |
| **41868091** | Liotta et al. 2025 (Nat Rev Methods Primers) — Laser capture microdissection primer | Laser-based cell isolation is a mature field |

**Transferable to OS1:** tiled region-list acquisition loop (register x,y per cell → re-locate across tiles) + objective pass/fail thresholds to avoid session drift; keep-out masking pattern protects sister-pair control cells. See OS3 `docs/AUTOMATED_ABLATION_LOOP.md` for the closed-loop design.

### Notes (OS1 automation addenda)
- Vendor claims (Nikon app note 2311E) are flagged; all numbers above are from the peer-reviewed primary paper (CC BY 4.0).

## Immortalized-Fibroblast Experiment — Literature Anchors (2026-10-21)

Relevant to the primary goal (does an hTERT-immortalized fibroblast have a Hayflick limit?) and the OLD/NEW division-rate dynamics experiment (protocol v0.2, TRD v0.9b). Full analysis: `docs/ARGUS_Literature_Analysis_EN.md`.

| PMID / DOI | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **9454332** | Bodnar et al. (1998, Science) — hTERT extends lifespan of BJ/RPE ≥ 20 PD, normal karyotype; causal link telomere shortening ↔ replicative senescence | hTERT bypass of the telomeric limit is fact; whether a hidden limit exists in single hTERT lines is untested |
| **39684765** | Shitova, Alpeeva, Vorotelyak (2024, IJMS) — no standard to assess hTERT «immortality»; studies use different parameters | «Immortality» of hTERT lines is methodologically open → justifies the fundamental question |
| **40789644** | Nassour & Karlseder (2025, CSH Perspect Med) — telomere crisis: tumor-suppressive barrier; rare cells escape | Context for hidden-limit / escape hypotheses in cancer cells |
| **39012627** | Thomas & Meraldi (2024, JCB) — centriole age breaks spindle symmetry even in «symmetric» divisions in human epithelial & fibroblastic lines; old centriole higher MT nucleation; Odf2/Plk1 pool | Direct human-cell evidence that centriole age affects division; also a covariate (daughter-size asymmetry) for the OLD/NEW measurement |
| **42602968** | Izumi et al. (2026, iScience) — Odf2 status → asymmetric CD133⁺ endosome inheritance; younger mother centriole ↔ more stem-like (SK-N-DZ) | Human-cell evidence: centriole age ↔ asymmetric fate; Odf2 as maturity/age marker |
| **17255513** | Yamashita et al. (2007, Science) — mother centriole → stem cell (Drosophila GSC) | Asymmetric centriole inheritance paradigm |
| **19829375** | Wang et al. (2009, Nature) — mother centrosome → progenitor, radial glia (mouse) | Mammalian asymmetric inheritance |
| **41315244** | Zhao et al. (2025, Nat Commun) — PCM1 coordinates centrosome asymmetry with polarized endosomes → daughter fate | Additional asymmetric-inheritance mechanism in human cells |
| **29363672** | Nigg & Holland (2018, Nat Rev Mol Cell Biol) — centriole duplication «once and only once»; deregulation in disease; **centrioles are microtubule-based organelles** | Terminology anchor (centriole = organelle); centriole-number regulation |
| **28130345** | Fava et al. (2017, Genes Dev) — PIDDosome activates p53 upon supernumerary centrosomes | Counter-evidence: supernumerary centrioles can LIMIT proliferation (p53), not confer immortality → control needed for the cancer hypothesis |
| **39406735** | Schapfl et al. (2024, Nat Commun) — centriole amplification in early B-cell development, dispensable | Supernumerary centrioles occur normally, can be dispensable |
| **29567643** | Ganier et al. (2018, EMBO J) — structural centrosome aberrations promote invasiveness | Centrosome aberration → invasiveness |
| **40009365** | Curinha et al. (2025, JCB) — centriole structural integrity defects (hydrolethalus) | Centriole integrity matters; structural readout rationale |
| **41174898** | Wang C. et al. (2026, Cytoskeleton) — tubulin PTMs | Tubulin PTM as centriole age/state marker (independent confirmation) |
| **42481875** | Sahin & Firat-Karalar (2026, EMBO Rep) — centrosome/cilium/satellite axis in neurodegeneration | Centrosome aging/degradation context |
| **36583780** | Tkemaladze (2022, Mol Biol Rep) — selective accumulation of old centrioles in stem cells | Theoretical frame for old-centriole accumulation |

**Gaps identified (no direct experiment found; Europe PMC 2026-10-21):**
1. Hidden replicative limit of hTERT-immortalized fibroblasts under long-term clonal observation (single lines, not population) — **not tested**.
2. Months-long OLD/NEW **division-rate dynamics** (interdivision-time trend) — **not measured** anywhere.
3. Centriole dispersion masking a Hayflick limit — **hypothesis, no experiment**.
4. Young supernumerary centrioles postponing/masking a limit — **hypothesis, no experiment**.
5. 24/7 months-long single-cell mammalian lineage tracking with continuous progeny removal — **no precedent** (mother machine = bacteria; mammalian microfluidics = weeks; IncuCyte-class = population level).

**Design implications (from the meta-analysis):** (a) old centrioles retain/high MT nucleation in normal cells (39012627) — the dispersion hypothesis must be tested at the scale of hundreds of divisions, with a scale-discriminator in the design; (b) supernumerary centrioles activate p53 (28130345) — cancer part needs proliferation/survival controls; (c) daughter-size asymmetry from centriole age (39012627) is a covariate in OLD/NEW dynamics — measure size/fate as covariates, not only interdivision time.

**OLD/NEW assignment at mitosis (method, resolved 2026-10-21):** after mitosis each daughter gets one centrosome (one mature + one new procentriole); the «newest» goes to both daughters — the real asymmetry is in the mature centriole. Rigorous assignment = **marker-anchored pedigree**: (1) the founder's first division anchors OLD/NEW (mother Cep164+ vs new Cep164−); (2) age is propagated by continuous lineage tracking; (3) per-mitosis assignment by imaging the two centrosomes + an age/maturity marker (Odf2/cenexin, tubulin polyglutamylation/polyglycylation; Cep164 alone does not separate M vs D chronological age). No bootstrap needed (anchor exists). Label-free morphology (daughter-size/spindle asymmetry, 39012627) is only a **calibrated secondary channel** for phototoxicity reduction (FR-7) — use only if calibrated accuracy ≥ 95% on the actual lines; no data exist for immortalized fibroblasts. Full analysis: `docs/ARGUS_label_free_centriole_assignment.md` (RU master: `ARGUS_label_free_centriole_assignment_2026-10-21.md`).

**Recognition pipeline (oldest/newest centriole):** two-channel spot detection (Centrin1-GFP = all centrioles; Cep164-RFP = mature mother); first-division anchor (Cep164+ → OLD, Cep164− → NEW); thereafter age from continuous pedigree + age marker (Odf2 / tubulin PTMs — Cep164 alone cannot separate M vs D after both mature); per-mitosis classification of daughters by which centrosome carries the tracked oldest centriole. Events below a tracking/marker confidence threshold are flagged **indeterminate** (no automatic decision); thresholds set in the pilot on independent annotation. Independent confirmation: second age marker, SIM/confocal at endpoint, EM subset.

**Validation & data-requirements methodology (adopted from engineering review, 2026-10-21):** every pre-test is delivered as (1) measurement conditions, (2) raw data incl. images where applicable, (3) values + spread, (4) uncertainty estimate, (5) acceptance criterion set by the bio group, (6) experiment-confirmed vs hypothesis. Requirements close **sequentially** (optics ← V3; scanning/focus ← V1/V2; autonomy/storage ← V6 + horizon window; tracking software ← pilot), not all at once. Six engineering data groups (optics, stage/scanning, focus/chamber, long-term environment, tracking software, storage) map to pre-tests V1–V6 and TRD sections. A list of required data is an input to engineering decisions, not consent to build subsystems.

## Base Experiment (Immortalized Fibroblasts) — Literature Data Package (2026-10-21)

| Parameter | Literature value | Source | Reliability | Node to measure ourselves |
|---|---|---|---|---|
| BJ-hTERT origin | normal foreskin fibroblasts, hTERT-immortalized, p53/pRb functional, normal karyotype | Bodnar et al. 1998 (9454332) | high | — |
| MRC5-hTERT origin | fetal lung (MRC-5) hTERT-immortalized | standard hTERT line | high | — |
| Parent MRC-5 / BJ Hayflick limit | ~42–50 / ~50–60 PD | MRC-5 lit.; Bodnar 1998 | high | — (context Q1) |
| Doubling time | ~24–30 h (fibroblasts) | standard range | medium | V6 |
| **Centriole age affects division in human epithelial & fibroblastic lines** (spindle/daughter-size asymmetry) | established, direct | Thomas & Meraldi 2024 (39012627) | high | — |
| Centriole age ↔ asymmetric fate (CD133 endosomes) | established (SK-N-DZ) | Izumi et al. 2026 (42602968) | high | — |
| Odf2/cenexin, tubulin PTMs — age/maturity markers | established | Thomas & Meraldi 2024; Wang C. 2026 (41174898) | high | V3 calibration on our lines |
| Centriole size | ~200–250 nm × ~400–500 nm | ultrastructure; Nigg & Holland 2018 (29363672) | high | pilot (2 centrioles per centrosome) |
| Fibroblast migration | ~10–50 µm/h | established range | medium | V1 |
| Mitosis duration | ~30–60 min | established | high | V2 |
| Segmentation methods | Cellpose 2.0/3.0; StarDist fallback | Pachitariu & Stringer 2022 (36344832); Stringer & Pachitariu 2025 (39939718); Schmidt 2018 | high | fine-tune after V3 |
| hTERT «immortality» assessment | methodologically unsettled | Shitova et al. 2024 (39684765) | high (uncertainty) | justifies Q2 |
| **Hidden Hayflick limit in immortalized fibroblasts (Q2)** | **not tested anywhere** | search 2026-10-21 | n/a | **the experiment itself** |

**Nodes requiring own measurement (literature gaps; need grant/lab):** V3 (SNR, min exposure, light budget), V1 (attachment, migration, track loss), V2 (division behaviour, mitosis timing), V6 (chamber vs control proliferation, light effect), pilot (AI accuracy on our markers + label-free calibration), Q2 (the hidden-limit question). Literature supplies structure, ranges and feasibility anchors; line-specific numbers for BJ/MRC5-hTERT are absent and cannot be replaced by assumptions or protocol count.

## Weak-Spot Literature — Deep Search (2026-10-21)

Follow-up on the identified weak spots; all PMIDs verified via Europe PMC.

| Weak spot | New literature anchor | Implication for ARGUS |
|---|---|---|
| Centriole age → functional consequences (Q3) | **Gasic, Nerurkar, Meraldi 2015 (26287477, eLife):** centrosome age regulates kinetochore–microtubule stability and **biases chromosome mis-segregation** | The older-centriole side is more prone to mis-segregation → **aneuploidy covariate** in OLD/NEW division-rate measurement (must be tracked/controlled) |
| Hidden Hayflick limit in immortalized cells (Q2) | **Ho et al. 2010 (21176396):** replicative senescence of human stem cells **independent of telomere shortening and p53** (Ras / oxidative stress) | hTERT fixes telomeres, but senescence can arise via non-telomere pathways → a hidden limit in hTERT cells is **biologically plausible** (supports Q2) |
| Supernumerary centrioles with age / cancer | **Na et al. 2015 (25988874) & 2024 (39680672):** age- and oxidative-stress-induced **centrosome amplification** in Drosophila stem cells; metformin inhibits it (AKT/TOR) | Aging itself drives centriole-number abnormalities → anchor for the cancer/supernumerary-centriole hypothesis and for age-related phenotype |
| Phototoxicity / light budget (FR-7) | **Icha et al. 2017 (28749075, Bioessays):** phototoxicity in live fluorescence microscopy and how to avoid it — light dose, wavelength dependence, imaging frequency | Practical framework for the V3/V6 light-budget node; no universal J/cm² threshold — must be measured on our lines |

**Meta (weak spots, updated):** (1) line-specific numbers remain absent — the binding gap, measured only on real samples; (2) the older-centriole side shows both higher MT nucleation (Thomas & Meraldi 2024) and higher mis-segregation (Gasic 2015) — a scale discriminator and aneuploidy covariate are required; (3) telomere-independent senescence is documented (Ho 2010) — strengthens the plausibility of Q2; (4) phototoxicity has no universal threshold (Icha 2017) — a measured light budget is mandatory.

## Commercial Systems for ARGUS-Like Tasks — Consolidated Engineering Benchmark (2026-10-21)

> Master: `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md` (Zeiss/Nikon/Olympus/Leica + open class), `docs/NIKON_AUTOMATED_LASER_SORTING_ANALYSIS_2026-10-20.md` (Nikon GA+JOBS in-situ laser sorting). Vendor specs = vendor claims (flagged); PMIDs verified.

### Per-vendor engineering solutions

| Vendor / system | Focus-hold | Illumination | Incubation | Detection | Software | Automation | Notes |
|---|---|---|---|---|---|---|---|
| **Zeiss Axio Observer 7 / live** | Definite Focus 3 (NIR) | Colibri 7 LED (7 ch) | XL/stage-top/heated glass lid CO₂/O₂ | pco.edge sCMOS + Axiocam color | ZEN | motorized Z/XY/turret/filter; piezo Z | $100–200K; closed; benchmark minimum set |
| **Nikon Eclipse Ti2-E** | Perfect Focus System (PFS, IR) | SOLA/Lumencor LED | Ti2 incubators | Prime/ORCA sCMOS | NIS-Elements (GA/JOBS — automated detect→classify→laser→verify) | motorized; in-situ IR laser (1480 nm) sorting | $100K+; closed |
| **Nikon BioStation CT** | fixed-focus incubation system | LED phase/fluo | integrated incubator | CCD/sCMOS | dedicated | multi-position | population-level, not single-cell months |
| **Olympus/Evident IXplore IX83** | TruFocus ZDC | pE-300/400 LED | IX3 incubators | ORCA sCMOS | cellSens | motorized; SpinSR sectioning | $100K+; closed |
| **Leica DMi8** | Adaptive Focus Control (AFC) | LED8/LED5 | DMi8 incubators | DFC/ORCA | LAS X | motorized; THUNDER deconvolution | $100K+; closed |
| **Sartorius IncuCyte S3/SX5** | in-incubator, fixed optics | LED (phase + fluo) | sits inside lab incubator | CCD | IncuCyte SW | multi-position, automated | population/well-level; no single-cell lineage; phototoxicity low |
| **Molecular Devices ImageXpress** | hardware AF | LED/Laser | optional incubation | sCMOS | MetaXpress | high-throughput multi-well | screening, not long-term single-cell lineage |
| **OpenFlexure (ARGUS base)** | software/stepper (gap → fiducial AF, PMID 42274973) | 1 ch → multi-LED | stage-top/chamber | RasPi HQ → sCMOS | Micro-Manager + Mastodon (42841415) | open; V9 hands | $3–5K; open — the advantage |

### Meta-analysis
- **Four critical modules every long-term platform must close:** (1) hardware focus-hold (Definite Focus/PFS/TruFocus/AFC → open fiducial AF), (2) multi-channel LED (low phototoxicity), (3) incubation/environment (CO₂/temperature/humidity), (4) sensitive sCMOS + unified software. ARGUS OS1 gaps: focus-hold, incubation, multi-LED, piezo Z — all closable open (Axio analysis §5.1).
- **Weak spots of commercial systems (for ARGUS):** price ($100–200K), closed/proprietary (ZEN, NIS-Elements), phototoxicity not eliminated (brightfield included — 42393487), no autonomous sample handling (V9 hands exceed benchmark), service/repair closed.
- **ARGUS unique niche (no commercial system):** months-long 24/7 single-cell mammalian lineage tracking with in-situ progeny removal (2-cell OLD/NEW design). IncuCyte/BioStation = population/well level; ImageXpress = screening; Ti2/Axio = multi-day, human-operated. The 6–12-month autonomous single-cell lineage + addressable removal + open cost is not offered by any vendor — the grant/publication novelty anchor.
- **Centriole appropriateness:** centrioles ~200–250 nm sit at the diffraction limit; commercial widefield (high-NA 60–100×, sCMOS) images them (Thomas & Meraldi 2024), but multi-day fluorescence on centrioles imposes phototoxicity; ARGUS's label-free calibrated channel + minimal-light regime is a differentiator vs all commercial systems.

## Engineering Note — Tube Lens / 60× Objective & Hardware Controller (2026-10-22)

> Master: `docs/ARGUS_EngineeringNote_TubeLens_60x_2026-10-22.md`. Triggered by OpenFlexure community threads (2026-10-15): 60× + 75 mm doublet tube-length scaling; hardware stage controller (joystick + focus).

- **Tube lens scaling (established optics):** effective magnification = f_tube / f_objective. A "60×" infinity objective with a non-standard 75 mm tube lens gives ≈ 60 × 75/200 ≈ 22.5× effective; NA/resolution stay objective-set, but field/aberrations change. **ARGUS rule:** use the vendor-standard tube-lens focal length for the chosen 60× objective (OS4); any deviation must be bench-verified (PSF + effective magnification, USAF/beads — possible-now optical bench).
- **Hardware stage controller (UX, not scientific requirement):** joystick + focus knob for manual positioning during calibration/metrology (V8), alignment, sample setup — a manual-override channel alongside AI control.
- **Community/open-source:** the 60× static-scan and hardware-controller builds converging with ARGUS's design space; contribution aligns with the open-hardware narrative and Foresight Nodes priority.
- **Weak spot:** non-standard tube lens risks reduced effective magnification and uncorrected field aberrations — bench-verify before committing optics.

## §. Epistemic standard (Noepedia Harvest — 2026-10-12)
> Master: `~/Desktop/Services/docs/NOEPEDIA_HARVEST_2026-10-12.md`
1. **Evidence pyramid (Murad PMID 27339128) + stages (K):** claims about system/performance are claims of demonstrated stage, not «assembled and running».
2. **Provenance:** every measurement/claim carries a source tag (firmware/version/sensor/model); a lost tag is a defect (HART arXiv 2603.05828).
3. **Verification by construction (Conant–Ashby, DOI 10.1080/00207727008920220):** a prototype/simulation (OS1, PScan) is stronger than a citation; the model itself requires independent validation.
