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

## §. Epistemic standard (Noepedia Harvest — 2026-10-12)
> Master: `~/Desktop/Services/docs/NOEPEDIA_HARVEST_2026-10-12.md`
1. **Evidence pyramid (Murad PMID 27339128) + stages (K):** claims about system/performance are claims of demonstrated stage, not «assembled and running».
2. **Provenance:** every measurement/claim carries a source tag (firmware/version/sensor/model); a lost tag is a defect (HART arXiv 2603.05828).
3. **Verification by construction (Conant–Ashby, DOI 10.1080/00207727008920220):** a prototype/simulation (OS1, PScan) is stronger than a citation; the model itself requires independent validation.
