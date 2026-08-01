# THEORY — ARGUS-OS1

**Updated:** 2026-07-28 (post 5-cycle peer review, 32 references)

## Central Hypothesis (Reframed)

> There is measurable heterogeneity in centriole elimination timing among cells of the same type, and division geometry (captured by Pedigree Score) explains a fraction of this variance.

This reframes the question from causality («does geometry cause elimination?») to variance partitioning («can we measure within-type variability using geometric parameters?»).

**H₀:** Cell fate alone predicts elimination timing. Pedigree Score adds nothing.

**H₁:** Pedigree Score captures within-type variance in elimination timing beyond cell fate, PAR asymmetry, and centriole age.

---

## Fate-Dependent Centriole Inheritance Rule

> When the differentiating daughter **eliminates/inactivates/transforms** its centriole, the stem cell keeps the **younger** centriole. When both daughters retain active centrioles, the stem cell keeps the **older** one.

This is not tissue-specific — it is fate-dependent. The rule is validated across four systems: Drosophila male GSC (Yamashita 2007), mammalian radial glia (Wang 2009), Drosophila neuroblast (Januschke 2011), human neural progenitors (Colicino & Hehnly 2021).

In C. elegans embryos, sperm centrioles segregate stochastically (Rostami 2023), creating natural variation. ~88% of somatic cells eliminate centrioles. We predict: the daughter inheriting the mother centriole eliminates it SOONER.

**Note on centriole «age»:** C. elegans centrioles lack mammalian post-translational modifications (acetylation, glutamylation). «Age» reflects assembly state and PCM complement, not cumulative oxidative damage.

---

## Three Centriole Fates

| Fate | Definition | Marker |
|------|-----------|--------|
| **Elimination** | Structural loss — SAS-4 disappearance | SAS-4::GFP |
| **Inactivation** | MTOC loss without structural loss — SPD-2 disappearance | SPD-2::mCherry |
| **Transformation** | Radical restructuring (e.g., sperm basal body) | N/A |

SPD-2 loss precedes SAS-4 loss. We track both endpoints via dual-outcome joint model.

---

## Plausible Mechanism (5 Pathways)

### 1. PCM Inheritance (Primary)
Mother centriole → more SPD-2/PCM (Dammermann 2004, Pelletier 2006) → higher MTOC activity → delayed elimination (Feldman 2025). PLK-1 drives differential PCM recruitment (Pintard & Bowerman 2019).

### 2. Ubiquitin-Proteasome System (UPS)
Proteasome + ubiquitin localise to centrioles at SAS-1 loss onset (Pierron 2023). Proteasome inhibition delays elimination in C. elegans and Naegleria. SPD-2/PCM may physically block UPS access → PCM delays elimination.

### 3. Cumulative Division Bias
Each asymmetric division adds small PCM bias. Accumulated MTOC differences → measurable shift in elimination timing — even between same-type cells.

### 4. Microtubule Mechanics (Alternative)
Asymmetric spindle tension → differential acetylation of centriolar tubulin → mechanical signal independent of SPD-2 levels. Speculative but testable.

### 5. PFD-6 / Longevity Link
Prefoldin subunit PFD-6 mediates HSF-1→DAF-16 longevity signalling. PFD-6-dependent genes in daf-2 mutants are enriched for centriole replication GO terms (Molière 2024). Direct transcriptional link: insulin/IGF-1 → centriole homeostasis.

---

## Pedigree Score

Three primary metrics (Bonferroni α = 0.0167):
| Metric | Rationale | Source |
|--------|-----------|--------|
| (a) Fraction ∥ A-P axis | A-P divisions → different fates | Sulston 1983 |
| (b) Mean 3D angle Δ | Angular change → fate divergence | Kalbfuss & Gönczy 2023 |
| (c) Orientation switches | Axis flips → scramble protein segregation | Mikeladze-Dvali 2012 |

Two secondary/exploratory: (d) angle variance, (e) cumulative angular path.

PCA on primary metrics. If PC1 < 10% → UMAP fallback. Computed from lineage history BEFORE current division (avoids circularity).

---

## Statistical Architecture

### Stage 1: Cox Mixed-Effects + BIC
```
m0: time ~ cell_type + age + SPD2 + centriole_age + PARs + (1|embryo/lineage)
m1: m0 + PedigreeScore * age
m2: m1 + PedigreeScore * cell_type + SPD2 * centriole_age
```
ΔBIC > 6 → strong evidence; > 10 → decisive (Kass & Raftery 1995).
Fine-Gray competing risks for dependent censoring sensitivity.

### Stage 2: Hierarchical Bayesian + Mediation
- brms Weibull survival, sceptical priors: normal(0, 0.5)
- Mediation: PedigreeScore → SPD-2 → elimination (Tingley 2014)
- Bridge sampling BF (Gronau 2017)
- Dual-outcome JMbayes2: SPD-2 loss + SAS-4 loss jointly

### daf-2 Pooled Model
```
coxme(Surv(time, event) ~ PedigreeScore * genotype + cell_type + SPD2 + age + (1|embryo/lineage))
```
All 140 embryos (100 WT + 50 daf-2) in single hierarchical framework.

### Power (1,000 simulations)
| Scenario | HR | ICC | Power |
|----------|----|-----|-------|
| Optimistic | 1.15 | 0.10 | 0.91 |
| Realistic | 1.12 | 0.15 | 0.84 |
| Conservative | 1.08 | 0.20 | 0.67 |

N=100 at realistic scenario → 84% power. If ICC > 0.15 → scale to N=150.

### Multiple Testing
3 primary hypotheses × α = 0.05/3 = 0.0167 (Bonferroni).
Secondary analyses reported with nominal p-values, labelled exploratory.

---

## Model System
C. elegans — complete invariant lineage (Sulston 1983). 558 somatic cells at hatching, ~88% eliminate centrioles (Kalbfuss & Gönczy 2023). Sister pairs from same division share cell type, cytoplasm, history — only geometry differs.

## daf-2 Longevity Experiment
50 WT (N2) + 50 daf-2(e1370) embryos. Hypothesis: daf-2 shows lower within-type variance (tighter IQR) — enhanced proteostasis reduces «aged centriole» signal.

## Key Reagents
- SAS-4::GFP — structural centriole marker
- SPD-2::mCherry — PCM/MTOC marker
- SAS-1::mNeonGreen — early elimination marker (20-embryo validation)
- Dendra2::SAS-4 — mother/daughter centriole identification
- CED-3::mKate2 — apoptosis
- PAR-2::GFP, PAR-3::mCherry — cortical polarity
- HIS-72::mCherry — nuclear tracking
