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

> Мастер-анализ: `~/Desktop/Services/docs/LITERATURE_ALERT_2026-10-12_Centrosome_Germline_G0.md`. All PMID verified via PubMed E-utilities 2026-10-12.

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

> Мастер-анализ: `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. Все PMID верифицированы Europe PMC/NCBI 2026-10-19.

### ⭐ Hardware autofocus / focus-hold — главный технический разрыв OS1

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42274973** | Djafer-Cherif & Waclaw 2026 (J Microsc) — **Affordable fiducial marker strategy for reliable autofocus in long-term live microscopy** | ⭐ Открытый дешёвый путь к аппаратному удержанию фокуса — кандидат P0 для OpenFlexure (замена степпера-Z-дрейфа) |
| **42525498** | Habte et al. 2026 (J Microsc) — Quantitative evaluation of **LED-based optical autofocus** module | Количественная оценка LED-автофокуса — воспроизводимо на своём железе |
| **42373656** | Wang et al. 2026 (Nat Commun) — Real-time robust autofocus for sustained scanning light-field (<2 µm error, 0.1 s) | Автофокус без аппаратных модификаций — альтернатива для multi-day |

### Phototoxicity — главный биологический конфaундер длительной съёмки

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42393487** | Stadter et al. 2026 (Arch Gynecol Obstet) — Phototoxicity of **brightfield** live-cell imaging on murine ovarian follicles | ⭐ Даже проходящий свет убивает клетки → обоснование phototoxicity ceiling в Body Law + минимизация экспозиции во ВСЕХ каналах |
| **28749075** | Icha et al. 2017 (BioEssays) — Phototoxicity in live fluorescence microscopy, and how to avoid it | Классический обзор — стратегии снижения повреждения |
| **23931522** | Magidson & Khodjakov 2013 (Methods Cell Biol) — Circumventing photodamage in live-cell microscopy | Практика: короткие экспозиции, сенсорные камеры |
| **19261845** | Frigault et al. 2009 (J Cell Sci) — Live-cell microscopy: tips and tools | Классика live-cell контраста/среды |

### Lineage-tracking / слежение (ядро платформы)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42841415** | Girstmair et al. 2026 (Development) — **Mastodon: command center for large-scale lineage-tracing microscopy datasets** | ⭐ Инструмент для lineage-конвейера — интеграция в OS1/OS2 |
| **42261409** | Tran et al. 2026 (MicroPubl Biol) — **Lineage-resolved cell identities in uncompressed C. elegans embryos** | Прямой прецедент lineage-resolved идентичности у C. elegans |
| **42499344** | Chandra et al. 2026 — Open-source longitudinal single-cell tracking pipeline | Открытый конвейер слежения + клеточный цикл |
| **42506143** | Martí-Pérez et al. 2026 (J Imaging) — Microscopy Cell Segmentation: review & benchmarking | Актуальный выбор сегментации (CellPose/StarDist) |

### Open hardware / live-cell (подтверждение архитектуры ARGUS)

| PMID | Finding | Role in ARGUS |
|:----:|---------|---------------|
| **42583731** | Malcolm et al. 2026 (J Cell Sci) — Removing barriers to advanced imaging + ML analysis | ⭐ OpenFlexure + ML = подтверждение архитектуры ARGUS |
| **36756063** | McDermott et al. 2023 (R Soc Open Sci) — OpenFlexure Voice Control + Blockly | Скриптование OpenFlexure для автономии |
| **41795377** | Moncada-Madrazo et al. 2026 (Biosens Bioelectron) — In-incubator chip-sized holographic microscope | Микроскоп в инкубаторе — концепция для длинных серий OS2 |
| **42103520** | Knapper et al. 2026 (Int J Gynecol Cancer) — OpenFlexure in gynecological pathology | OpenFlexure — реальное применение вне лаборатории |
| — | Malcolm et al. 2026 — Adapting OpenFlexure for Affordable Live-Cell Imaging (DOI 10.64898/2026.02.02.703252) | Live-cell адаптация OpenFlexure (preprint) |

### Benchmark-эталон (vendor-claims)
- **Zeiss Axio Observer 7** (Definite Focus 3, Colibri 7 LED, motorized Z/XY/revolver/condenser/filter, pco.edge 4.2 sCMOS, ZEN 3.3, Scanning Stage 130×100) + **Axio Observer live** (Glass Lid CO₂/O₂ heated, Temperature Controller, Heated Plate K, Z8+RTX A4000) — эталон инженерного набора для multi-day live-cell.
- Конкуренты с аналогичным аппаратным автофокусом: **Nikon PFS**, **Olympus TruFocus ZDC (IX3-ZDC2)**, **Leica AFC**. Бенчтоп-класс: **IncuCyte S3/SX5** (в инкубаторе).

### Notes
- Позиционирует инженерию как первый класс доказательств для платформы: focus-hold + среда + LED-мультиканал — условия валидности multi-day lineage-данных, а не «удобства».
- Все vendor-claim'ы помечены; независимая проверка — по PMID в таблицах выше.

## §. Эпистемический стандарт (Noepedia Harvest — 2026-10-12)
> Мастер: `~/Desktop/Services/docs/NOEPEDIA_HARVEST_2026-10-12.md`
1. **Пирамида доказательств (Murad PMID 27339128) + ступени (K):** заявления о системе/производительности — ступень доказанности, не «собрано и работает».
2. **Provenance:** каждый замер/claim несёт метку происхождения (прошивка/версия/датчик/модель); потеря метки = дефект (HART arXiv 2603.05828).
3. **Проверка построением (Conant–Ashby, DOI 10.1080/00207727008920220):** прототип/симуляция (OS1, PScan) сильнее цитаты; модель сама требует независимой валидации.
