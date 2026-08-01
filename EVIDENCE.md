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
