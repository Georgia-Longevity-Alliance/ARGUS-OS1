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

## Idle inference — непрерывный внутренний процесс агента (2026-11-12)

> **Триггер:** концепция В. В. Налимова (семантический континуум + P(μ|y) ∝ P(μ)·P(y|μ)) → спека внутреннего цикла агента `docs/ARGUS_Internal_Process_Idle_Inference_2026-11-12.md`; анализ `Services/docs/ANALYSIS_2026-11-12_Nalimov_Semantic_Continuum_Idle_Inference.md`. Все идентификаторы резолвнуты 2026-11-12 (Crossref/Europe PMC/arXiv).

| Тезис | Источник (PMID/DOI) | Сила | Что делать дальше |
|---|---|---|---|
| Смыслы существуют вне мозга как «поле»; мозг — приёмник | реконструкция: **doi 10.17506/ryipl.2016.17.4.2432** (Politov 2017); первичный индекс — **PMID 11605554** (единственная запись Налимова в Europe PMC) | ❌ не подтверждено и **нефальсифицируемо** — в коде/текстах не заявлять | Использовать только как метафору с пометкой; в grants/статьях не переносить |
| Мысль = байесовское обусловливание prior на контексте | **doi 10.1017/S0140525X12000477** (Clark 2013, PMID 23663408) — prior **внутри** системы | ✅ сильная (как форма, не как теория сознания) | Язык описания для леджера ARGUS; не называть «сознанием» |
| Байесовская когнитивная наука плохо фальсифицируема | **doi 10.1007/s13194-023-00533-w** (Crupi & Calzavarini 2023); продолжение — **doi 10.1007/s00421-025-05855-6** (Mangalam 2025) | ✅ сильная критика | Каждый наш байесовский вывод (ARGUS-OS1 статистика) обязан иметь критерий опровержения — иначе это риторика |
| In-context learning ≈ неявный байесовский вывод (промпт = наблюдение) | **arXiv:2111.02080** (Xie et al., ICLR 2022) | ⚠️ умеренная (теория + синтетика) | Обосновывает «фильтр» как контекст; не тянуть в биологию |
| **Наш собственный пилот CKA (12 ноя):** qwen2.5:7b × llama3.2 на 17 абзацах, 8 осей оценок → CKA 0.318 против нуля 0.377, p=0.189 | `docs/EXPERIMENT_CKA_2026-11-12.md`, `src/cka/mod.rs` | ✅ воспроизводимо (`argus-cka`), запись в `ledger/cka_*.json` | **Отрицательный** (сходимости нет; инструмент вырожден: NN-cos 0.965/0.892) | НЕ ссылаться на PRH в наших текстах, пока не снята вырожденность; следующий шаг — два энкодера через рантайм с `/v1/embeddings`, n≥60, 24–32 оси |
| **Слабая (проверяемая) форма «поля смыслов»:** независимо обученные сети сходятся к общей семантической структуре | **arXiv:2405.07987** (Huh, Cheung, Wang, Isola 2024, PRH) · **doi:10.1038/s41562-022-01316-8** (Grand 2022) · **doi:10.1038/s42003-022-03036-1** (Caucheteux & King 2022) | ✅ источники реальны; ⚠️ сходимость **неполная**: **arXiv:2609.27252** (You 2026, «Structure over Geometry») и **arXiv:2602.14486** (Gröger 2026) | Умеренная (препринты + рецензируемая поведенческая опора) | «Смысл предсуществует отдельному приёмнику» — в физической форме (веса, корпуса), а не как внешнее поле. Дешёвый тест для ARGUS: CKA-сходимость двух локальных моделей на одном корпусе против перестановочного теста |
| **Мозг — не компьютер** (нет программы, нет hardware/software, нет fetch–decode–execute) | **PMID 30714889** (Brette 2019, BBS 42:e215, doi:10.1017/S0140525X19000049) | ✅ сильная **как критика** метафоры кодирования (не как альтернативная архитектура) | Опора для главной идеи в текстах об агенте: «приёмник, а не компьютер». Не растягивать на «пассивный приём» |
| Энергобюджет мозга уходит на текущую синаптическую передачу; task-evoked изменения малы рядом с baseline | **PMID 11598490** (Attwell & Laughlin 2001, JCBFM 21:1133) · **PMID 16776593** (Raichle & Mintun 2006, Annu Rev Neurosci 29:449) | ✅ сильная (два независимых корпуса) | «Раз приёмник — он постоянно работает»: покой ≈ работа по энергетике → выключение не режим органа. Прямой аргумент для `think --loop` |
| Спонтанная мысль непрерывна, DMN измерима | **PMID 27654862** (Christoff 2016, Nat Rev Neurosci 17:718) | ✅ сильная (обзор) | Биологический якорь для «часов» в агенте; не путать с заявлением о сознании ИИ |
| Внимание распределяется байесовским «удивлением» | **PMID 18834898** (Itti & Baldi 2009, Vision Res 49:1295) | ✅ сильная (для зрения) | Механизм выбора вопроса в цикле: очередь по surprise |
| Консолидация/реплей — механизм «сна» системы | **PMID 7624455** (McClelland 1995, Psychol Rev 102:419) | ✅ сильная (канон CLS) | Ночная консолидация леджера (6 ч простоя) |
| Агенты LLM реактивны: простой между запросами теряется | **arXiv:2605.25971** (Hu et al. 2026) | ⚠️ умеренная (препринт) | Обоснование, почему `argus-agent` нужен режим `think` |
| Предвычисление в простое снижает стоимость ответа | **arXiv:2504.13171** (Lin et al. 2025) | ⚠️ умеренная (препринт) | Аргумент для бюджета/расписания; не гарантия качества |
| Проактивные агенты: распределение простоя + риски | **arXiv:2609.37267** (Oh et al. 2026) | ⚠️ слабая-умеренная (по абстракту) | Риск-раздел спеки (навязчивость, ложное чтение контекста) |

**Жёсткий гейт (взят из Correspondence в NMI):** любой выдуманный идентификатор в idle-выводе = провал архитектуры; `fabricated_identifiers` должен быть 0, иначе цикл переводится в `--dry-run`.

## §. Epistemic standard (Aletheia Harvest — 2026-10-12)
> Master: `~/Desktop/Services/docs/ALETHEIA_EPISTEMIC_HARVEST_2026-10-12.md`
1. **Evidence pyramid (Murad PMID 27339128) + stages (K):** claims about system/performance are claims of demonstrated stage, not «assembled and running».
2. **Provenance:** every measurement/claim carries a source tag (firmware/version/sensor/model); a lost tag is a defect (HART arXiv 2603.05828).
3. **Verification by construction (Conant–Ashby, DOI 10.1080/00207727008920220):** a prototype/simulation (OS1, PScan) is stronger than a citation; the model itself requires independent validation.

## OpenFlexure Forum intel — 2 threads (2026-11-15…18), verified 2026-11-18

> Master: `docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`. Источник — Discourse API (`openflexure.discourse.group/t/2896`, `/t/2886`), потому что старый домен `forum.openflexure.org` = NXDOMAIN. Все ID резолвнуты 2026-11-18 (Europe PMC + Crossref).

| Тезис | Источник (PMID/DOI) | Сила | Что делать дальше |
|---|---|---|---|
| ROM стадии OFM: проект 12.5 мм → измерено 11.4 ± 0.4 × 11.4 ± 0.5 мм; метод — корреляция смежных кадров + дешёвый тест-слайд, считает на встроенном ПО | **PMID 42960477** / doi 10.1111/jmi.70192 (Chisholm et al., J Microsc 2026) | ✅ сильная (реценз., прямо по железу) | Планировать скан от измеренного ROM своего экземпляра (10×10 мм — без запаса); F5 |
| Фокус-стекинг/EDOF на OpenFlexure реален при BOM ≈$300; сравнение fusion: **complex wavelet резче Sobel и variance** (дороже по времени); есть оценка геометрических искажений по сетчатому эталону | **PMID 42644580** / doi 10.1111/jmi.70161 (Ballesteros & Garzón, J Microsc 2026) | ✅ сильная как метод; ⚠️ модальность — отражённый свет, не проходящая биология | Взять как baseline для блендинга F4; сравнение методов перенести на наши яркопольные данные |
| Сшивка форумчанина (connor, n=1): позиции тайлов из `openflexure-stitching` + свой блендинг (feather низких частот, деталь из самого резкого поля, `libvips dzsave`) → «no visible seams, often sharper than any single field» | канон: **doi 10.1145/245.247** (Burt & Adelson 1983); **doi 10.1007/s11263-006-0002-3** (Brown & Lowe 2006); обзор **doi 10.1007/s10462-021-09961-7** (Bhat 2021) | ⚠️ умеренная (практика подтверждена каноном, метрик в треде нет) | F4: реализовать, мерить variance of Laplacian + швы |
| Грабли v3.0.0-beta: тайлы по умолчанию 1400×1400 при кропе 2800×2800 (нужно `histo scan capture mode = full`; автофокус-стек захардкожен `standard`, патч в `things/autofocus.py`) → потеря половины поля и удвоение числа тайлов | форум (connor, 2026-11-18), не проверено у нас | ⚠️ не проверено | F2: чек-пункт приёмки — сверять `scan_data.json` с фактическим размером файлов |
| Arduino-Nano workaround: скетч из инструкций не подходит для server v3.0.0-beta; нужна Sangaboard firmware v1.0.4, загрузка через AVRDUDESS (`ATmega328P`, пресет Nano, старый бутлоадер; новый — baud 115200); у ricardd моторы и подсветка заработали, скан прошёл | форум (WilliamW, ricardd, 2026-11-15…17); совместимость v1.0.4 ↔ v3.0.0-beta **не подтверждена** | ⚠️ слабая-умеренная (единичный успех) | F1: пин версий сервер↔прошивка + проба на своём Nano |
| OFM vs Aperio GT450 (275 биопсий, 5 моделей AI-триажа): AUC 0.71–0.80, accuracy 0.64–0.72; обязательны стандартизация µm/px и цветокоррекция | **PMID 42800763** / doi 10.1016/j.ijgc.2026.104993 (Corrielus et al., IJGC 2026) | ⚠️ умеренная — CI перекрываются, превосходство не показано | F6: гейт «µm/px + цвет» перед любым ML; в текстах — «пригодно для триажа», не «не хуже сканера» |
| OFM как инструмент доступной гинекологической патологии | **PMID 42103520** / doi 10.1016/j.ijgc.2026.104680 (Knapper et al., IJGC 2026) | ⚠️ умеренная (абстракт недоступен) | Нарратив open-hardware, не инженерия |
| Z-стеки = дополнительная фотодоза (перекрытие 0.35–0.5 ⇒ больше кадров) | **PMID 28661494** / doi 10.1038/nmeth.4344 (Laissue 2017, Nat Methods) | ✅ сильная (обзор) | F3: overlap — параметр протокола с измеренной дозой, не «на глаз» |
| OFM со структурированным освещением — оптическое секционирование на той же платформе | **PMID 36225006** / doi 10.1364/oe.461910 (Opt Express 2022) | ✅ сильная | Апгрейд-путь OS2/OS3 без смены платформы |

## Verification by construction — tile pipeline (2026-11-18)

> Код: `software/pipeline/` (README с числами), тесты: `software/tests/test_pipeline.py` (7 passed, ~15 s). Фантом — синтетическая мозаика с дрейфом освещения, переменным дефокусом (σ 0/0.6/1.2/1.8 px) и парами субдифракционных точек; регистрация — patch voting + глобальный МНК.

| Тезис (наш собственный результат) | Как проверено | Сила | Что делать дальше |
|---|---|---|---|
| «Деталь из самого резкого поля» сохраняет резкость, усреднение — нет: fusion 92 % резкости ground truth против 58 % у feather-усреднения, при этом PSNR **выше** (26.81 vs 25.76 dB), швы невидимы (0.99 против 1.67 у наивной вставки) | `evaluate.py` на фантоме 1080 px / 16 полей / overlap 0.35; дефолты выбраны `sweep.py` (15 комбинаций) | ✅ воспроизводимо (синтетика) | Прогнать на реальных тайлах V6; если на живом образце разрыв меньше — не заявлять в статьях |
| Регистрация тайлов точна при overlap 0.15 / 0.35 / 0.70 | 0 px ошибки против известных позиций фантома; 59/59 связей на траверсе | ✅ воспроизводимо | Заменить «позиции из openflexure-stitching» нашей регистрацией, если внешние позиции расходятся >1 px |
| Два тупика (документированы в коде): глобальная фазовая корреляция даёт 124 px при истинных 260 px; одиночная полоса по краю даёт 0.944 при полностью неверном сдвиге на overlap 0.70 | прямые измерения на фантоме | ✅ отрицательный результат | Не повторять; метод ROM из PMID 42960477 применять только при шаге < половины поля |
| Гейты F2/F6 исполняемы: декларация vs факт разрешения (1400↔2800), ≤100 нм/px, бининг ≤2×2, ROM из корреляции кадров (измерено/скомандовано = 1.0000) | `qc.py scan/gate`, `measure_rom.py`; тесты | ✅ воспроизводимо | Включить `qc.py scan` в скрипт скана как обязательный exit-code gate |

## MR !553 прочитан + прошивка верифицирована (2026-11-18)

> Ранее в §«OpenFlexure Forum intel» стояло «MR не читал». Закрыто: прочитан diff MR и скачан официальный артефакт прошивки.

| Тезис | Источник | Сила | Что делать дальше |
|---|---|---|---|
| Прошивка Nano: AVRDUDESS v2.20, preset `Arduino Nano (ATMega328P)`, flash `.hex`, Program; на Linux `avrdude -c arduino -p m328p -P /dev/ttyUSB0 -b 57600 -U flash:w:nano.hex:a` (в MR опечатка `-m`) | GitLab MR `openflexure/openflexure-microscope` **!553**, diff (состояние: **открыт, не смержен**) | ⚠️ умеренная: автор проверил на клоне с CH340; **официальный Arduino Nano не проверен**; ссылки на прошивку в MR нет | Использовать как есть; при новом бутлоадере официального Nano — baud 115200 (форум, не проверено) |
| `nano.hex` = **Sangaboard Firmware v1.0.4**, sha256 `dc6066ed…3c36f7`, из пайплайна `sangaboard-firmware` job 11430994239 | артефакт скачан и проверен: строка версии найдена в `nano.elf` | ✅ сильная (проверено нами: файл, хеш, версия) | Лежит в `firmware/vendor/sangaboard-v1.0.4/` (не в git), provenance рядом |
| Приёмка стенда автоматизируема: A1 (mismatch-признаки в API), A2 (`motor_release` в API), A3/A4 (QC скана), A5 (ROM), A6 (сэмплинг), A7 (швы) | `software/pipeline/acceptance.py` + 3 теста на мок-сервере (здоровая прошивка → PASS/PASS; «firmware mismatch» → FAIL/UNKNOWN; сервер недоступен → UNKNOWN/UNKNOWN) | ✅ воспроизводимо (мок-сервер, без железа) | На стенде: один запуск `acceptance.py --url … --scan …`, отчёт в `PROVENANCE_V6.md` |

## Network reality check + bundle verification (2026-11-19)

| Тезис | Как проверено | Сила | Что делать дальше |
|---|---|---|---|
| Микроскопа V6 в локальной сети Джабы нет: порт 5000 закрыт на всех 254×2 хостах (192.168.50/100); открыты только роутеры (80) и одна Windows-машина (192.168.100.134, `OpenSSH_for_Windows_9.5`) | скан сокетами + разбор баннеров, 19 ноя | ✅ прямое измерение | A1/A2 закрываются только на стенде (Тбилиси) |
| Пакет приёмки самодостаточен: распаковка `dist/argus-os1-acceptance-2026-11-19.tar.gz` в чистый каталог → `sha256sum -c` OK, `pytest ../tests/test_pipeline.py` **10 passed**, `./v6_accept.sh --demo` выдаёт A3/A4/A6/A7 PASS | прогон из `/tmp/handoff_test` | ✅ воспроизводимо | Отправить пакет тому, кто у микроскопа; вернуть `acceptance_*.md` |
| Демо-прогон как тест-среда находит настоящие баги: (1) сшивка внутрь папки скана ломала QC («inconsistent field sizes»); (2) короткий траверс (0.18 мм) попадал в A5 | демо-прогоны 19 ноя, до/после патча | ✅ отрицательный результат (полезный) | Правило: любой новый шаг пайплайна сначала гонять в `--demo` |


## Agent-team architecture: PNAS law + light-dose budget (2026-11-19)

> Триггер: разбор трёх источников (PNAS `10.1073/pnas.2612825123`; APS *Physics* 19,154; Medium/Siegel). Мастер-анализ: `~/Desktop/Services/docs/ANALYSIS_2026-11-19_LLM_Teams_Hawking_AI_Measurement.md`. Все ID проверены 2026-11-19 (Crossref / arXiv API / NCBI E-utilities). Это **внешние подтверждения дизайна**, не наши измерения.

| Тезис | Источник | ID | Сила | Что делать дальше (для ARGUS) |
|---|---|---|---|---|
| Скейлинг команд LLM подчиняется классическим законам распределённых систем, и применимый закон определяется **структурой задачи** | Mieczkowski et al., PNAS 123(47), 2026-11-18 | `10.1073/pnas.2612825123` (абстракт; полный текст не прочитан — pnas.org блокирует) | Сильная как публикация; для нас — рамка | Классифицировать каждый workflow: разложимая задача → параллельные воркеры + гейт; последовательная (назначение линии по кадрам, решения по протоколу) → **один агент** |
| Количественная цена ошибки архитектуры: **+80.8 %** на разложимом рассуждении → **−70.0 %** на последовательном планировании против одного агента; 260 конфигураций, 5 архитектур, 3 семейства моделей, R²=0.373 | Kim, Gu, Park et al. 2025 | `arXiv:2512.08296` (препринт) | Сильная (контролируемый эксперимент) | Не строить команду под последовательный участок пайплайна (линия/судьба центриоли — последовательна) |
| **Архитектуры без централизованной верификации распространяют ошибки сильнее** централизованных; у централизации и децентрализации уязвимости **асимметричны** (не «одна лучше») | PNAS (абстракт); Kim 2025; Cemri 2025 | `10.1073/pnas.2612825123`; `arXiv:2512.08296`; `arXiv:2503.13657` / `10.52202/085713-4082` | **Сильная** | Верификация — детерминированный гейт (`qc.py scan`, `acceptance.py`), НЕ голос LLM-агентов; назвать явно, какую уязвимость выбираем (единая точка отказа vs распространение ошибки) |
| Добавление агентов немонотонно (рост→насыщение→падение) при смеси лёгких/трудных задач; оптимальное N оценивается по малой выборке | Chen, Davis, Hanin 2024; Li 2024 | `arXiv:2403.02419`; `arXiv:2402.05120` | Сильная | Мерить N=1/3/5/9 на замороженном наборе (напр. 30 эмбрионов-фантомов QC) перед фиксацией конфига |
| Самоорганизующиеся команды LLM **не дотягивают до лучшего эксперта** (до −41.1 %), механизм — усреднение эксперта с не-экспертом; растёт с размером команды | Pappu, El, Cao 2026 | `arXiv:2602.01011` (препринт, одна группа) | ⚠️ Умеренная | В агентских ролях ARGUS (сегментация / трекинг / QC / отчёт) — **явные веса и авторитет по критерию**, не голосование «поровну» |
| **Реальный «эффект наблюдателя» для нас — световая доза:** фототоксичность в live-флуоресценции; даже низкий уровень синего света достоверно меняет подвижность клеток (PC3), т.е. измерение меняет измеряемый фенотип | Laissue, Alghamdi, Tomancak et al. 2017; Alghamdi et al. 2021 | `10.1038/nmeth.4344` · **PMID 28661494**; `10.3389/fcell.2021.738786` · **PMID 34977004** | Сильная (in vitro) | Бюджет световой дозы на каждый OS-этап (доза, а не только интенсивность), контрольная необлучённая область, фиксация в протоколе; это же — **измеренное** обоснование предпочтения label-free (P7), а не эстетика |

**Мета-анализ:** правила «структура задачи → архитектура», «централизованная верификация», «явные веса вместо консенсуса» сходятся у трёх независимых групп и совпадают с уже принятыми решениями ARGUS (детерминированные гейты F2/F6, watchdog, лимиты шагов). Ни одна из найденных работ не касается LLM-мозга, управляющего актуаторами 24/7 (V9) — этот режим остаётся без внешней опоры, поэтому V9 требует человека-в-контуре и аварийного стопа как **нашего** инженерного требования, а не «подтверждённого литературой».


## R1/R2/R8 — реализовано и проверено сборкой/тестами (2026-11-19)

| Что | Где | Как проверено | Сила |
|---|---|---|---|
| **R1** гейт структуры задачи: команда разрешена только для `decomposable`; `unknown` = отказ (fail-safe) | `software/argus-agent/src/agent/mod.rs` — `TaskStructure`, `resolve_team_size`; CLI `fusion … --task-structure …` в `src/bin/argus_agent.rs` | `cargo build --offline` OK; `cargo test --offline` **20 passed / 2 ignored** (5 из них — R1); прогон CLI: без объявления → `exit 2` + сообщение с `arXiv:2512.08296`, неверное значение → `exit 1` | ✅ воспроизводимо |
| **R2** инвариант «верификация = детерминированный гейт, не голос LLM», машинно проверяемый | `software/pipeline/invariants.py` (`check_all`, `accepted_failure_mode`) | `python3 pipeline/invariants.py` → exit 0 (5 gate-модулей без модели и сети); 4 теста, включая подсадку `import openai` и `import urllib` — чекер их ловит | ✅ воспроизводимо |
| **R8** бюджет световой дозы с **невыдуманным** порогом (гейт только при явном `--max-j-cm2`) | `software/pipeline/light_dose.py` | `pytest tests/test_pipeline.py` — **17 passed** (3 теста R8: H(1 мВт/см², 1000 мс)=1e-3 Дж/см²; 1 Вт/м²=0.1 мВт/см²=1 мкВт/мм²; без лимита вердикт `reported_only`) | ✅ воспроизводимо |
| Принятый риск назван, а не спрятан: централизованная верификация = единая точка отказа | `invariants.accepted_failure_mode()` | тест `test_r2_accepted_risk_is_named` | ✅ |



## R3 — измерено: добавлять агентов к нашему QC-решению бесполезно (2026-11-19)

> Стенд: `software/pipeline/n_scaling.py` (8 само-проверок). Данные: `results/n_scaling_llm_2026-11-19.json`. Отчёт: `results/R3_N_SCALING_2026-11-19.md`. Замороженный набор 30 кейсов, fingerprint `485be3fada07c1e5…`, ground truth = вердикт пре-регистрированного гейта (≤100 нм/px, бининг ≤2×2, разрешение = заявленное).

| Тезис (наш результат) | Как проверено | Сила | Что делать дальше |
|---|---|---|---|
| **Детерминированный гейт: 1.00 при N=1; LLM 7B: 0.90 при N=1, 0.867 при N=3, 0.90 при N=5 и N=9** (270 вызовов `qwen2.5:7b-16k`, T=0.9, 0 сбоев). Best N = **1**; выигрыша от голосования нет, цена ×9 | прогон 2026-11-19, 9 бюллетеней на кейс, вложенные префиксы для N=1/3/5/9 | ✅ воспроизводимо (n=30, без CI) | Не строить команду для решений, у которых есть правило; для `publication_status`-подобных задач — только детерминированный обработчик |
| **Причина видна в бюллетенях: 29/30 кейсов — единогласие**, расхождение только в 1/30. Усреднять нечего: у локальной модели нет сэмплингового шума | подсчёт по сохранённым бюллетеням | ✅ прямое измерение | Голосование применять только там, где ошибки — i.i.d. шум (разные сильные модели), а не политика |
| **3/30 систематических ошибок, единогласно 9/9 при любом N** (27/27 бюллетеней): «2790 px в 1 из 240 полей» → модель говорит ACCEPT, гейт говорит REJECT. Смещение не лечится количеством агентов | разбор 3 кейсов (QC12, QC15, QC18) | ✅ прямое измерение | Лечится **правилом**, а не панелью: «любое поле ниже заявленного разрешения = fail, включая 1 из 1000» — внести в §gate протокола |
| Панель **приняла 3 скана**, которые гейт отвергает; ни одно N это не исправило | сравнение vote(N) с ground truth | ✅ | Аргумент для R2: голос моделей не должен перекрывать гейт — теперь это не принцип, а измерение |
| Контрольная страта `borderline` содержит 3 «ловушки» (внутри лимитов, ответ ACCEPT) — модель их прошла ⇒ провал не в keyword-matching | состав набора + разбор | ✅ | При расширении набора держать обе стороны (false-ACCEPT и false-REJECT) |

> Попутно: `_gh/ARGUS-OS1/software/argus-agent` не собирался внутри cargo-workspace `Services/` (не член и не в `exclude`). Добавлен в `exclude` (`Services/Cargo.toml`) — до этого `cargo build` падал на конфигурации, а не на коде.
