# PROTOCOL v0.3: Is there a Hayflick limit in immortalized fibroblasts? Division-rate dynamics of cells with the oldest and newest centriole

**Author:** Jaba Tqemaladze¹
**Date:** 2026-10-21 · **v0.3:** 2026-11-12 (Amendment 2: sampling requirement, power, readout acceptance test)
**Status:** 🟡 hypothesis-grade protocol for validation on the ARGUS platform. All parameters are calibrated by pre-tests (V1–V6, TRD §6). NOT a ready laboratory protocol before pre-test data.
**Platform:** ARGUS (see `docs/ARGUS_TRD_v0.9b.md`)

¹ Georgia Longevity Alliance.

---

## 1. Goal and hypotheses

### 1.1 Fundamental question — split into three distinct claims

**Q1 (background, established by literature):** is there a division limit in normal fibroblasts? Yes — the classic Hayflick limit (≈50 divisions). ARGUS does not test this.

**Q2 (primary question of ARGUS):** is there an analogous limit in the chosen immortalized lines (BJ-hTERT, MRC5-hTERT) — yes or no.
- H1 (working hypothesis): a limit exists even with hTERT expression — simply much larger and masked at the population level by rapid colony growth.
- H0 (null): no limit — true «immortality» of immortalized fibroblasts.

**Q3 (mechanism):** does division rate depend on the age of the inherited centriole (OLD vs NEW).

**Rule:** Q2 and Q3 are distinct scientific claims, measured and reported **separately** (separate sections, separate criteria). Q2 = «no limit in the observation window» is one answer; Q3 = «OLD slows relative to NEW» is a mechanism compatible with a hidden limit but not identical to Q2.

### 1.1a Observation horizon and stopping criterion (first stage)

Expected division counts (somatic ≈50, stem ≈200, immortalized ≈800–1000, cancer — thousands) are **working estimates, not source-confirmed** (except somatic ≈50). They do NOT dictate the horizon. Precisely counting the number of divisions is the task of research staff, not ARGUS.

- **Horizon of the first stage is a defined window** (e.g., ≥ N generations or ≥ 6 months, whichever comes first), not «until 800–1000 divisions».
- **Stopping criterion (pre-registered):** (a) OLD/NEW divergence in interdivision time is statistically significant; **or** (b) lineages reach the senescence endpoint defined in §4a; **or** (c) the window ends without (a)/(b) → «not detected in the window», the boundary of the conclusion is recorded.
- Extending the window — only if the data justify it.
- **Autonomy = the justified window** (e.g., 6 months), not «years».

### 1.2 Context — expected division counts (working estimates)

The limit experiment is identical for any cell type; only the expected number of divisions differs. **The numbers below are working estimates, not source-confirmed** (except somatic ≈50). The horizon does not depend on them (see 1.1a).

| Cell type | Expected number of divisions |
|-----------|------------------------------|
| Somatic | ≈ 50 |
| Stem | ≈ 200 |
| **Immortalized fibroblasts** | **≈ 800–1000** |
| Cancer | several thousand |

**Precisely counting the number of divisions is the task of research staff, not of ARGUS.** ARGUS does not count «the exact number up to the last division» — it observes the dynamics by which the fact of the limit is established.

### 1.3 Instrumental task of ARGUS (how the fact is established)

**Observe how the division rate of a cell carrying the oldest centriole changes while a cell carrying the newest centriole sits beside it, over a long period (months), without opening the enclosure.**

Expected signal of limit onset (H1, mechanism): progressive slowing of the OLD lineage relative to the NEW one, if the hidden limit is masked by rapid colony growth through centriole dispersion.

**Experimental-purity constraints:** no chemical treatment is applied to tracked cells; which cell carries the oldest and which the newest centriole is determined **by their location** — therefore the system must minimize perturbation of tracked-cell position (FR-12) and register cell polarity in 3D (top/bottom in addition to left/right, FR-13) — data needed for future centriole-transplantation experiments.

**Design (per the experimental plan):** exactly **2 single cells are studied** — carrying the oldest (OLD) and the newest (NEW) centriole, side by side. All other cells produced by mitosis **are removed**. The culture does not grow: there are only the two focal cells and their lineage continuations.

### 1.4 Cancer cells (future direction, LATER)

The same task for cancer cells (if time permits). Specific feature: cancer cells carry supernumerary centrioles. A control is required: **does a young centriole arise in the same cell next to the oldest one**. If so:
- this may postpone the onset of the Hayflick limit;
- if the appearance of extra young centrioles is faster than the expected limit onset, this masks the Hayflick limit and the cell appears «immortal».

Studying this process clarifies the picture of cancer origin. Requirement on ARGUS: extension slots, including multi-centriole tracking per cell (TRD §3.2).

### 1.5 Established (fact) vs hypothesis (honesty)

| Statement | Status |
|---|---|
| The mother centriole carries distal appendages, is marked by Cep164, and templates the primary cilium | ✅ established |
| Centrin-1 marks all centrioles | ✅ established |
| Asymmetric mother/daughter centriole inheritance in several stem systems (e.g., neural progenitors) | ✅ documented in some systems |
| Hayflick limit in somatic cells (≈50 divisions) and stem cells (≈200) | ✅ established (main model animals and humans) |
| **Hayflick limit in immortalized (hTERT) fibroblasts** | ❓ **hypothesis — to be tested (primary goal)** |
| Link between centriole age and fibroblast division rate | ❓ hypothesis (to be tested) |
| Masking of the limit by rapid colony growth through centriole dispersion | ❓ hypothesis (to be tested) |
| «Immortality» of cancer cells; role of supernumerary centrioles in postponing the limit | ❓ hypothesis (future direction) |

---

## 2. Cell lines and markers

| Item | Value |
|------|-------|
| Primary line | **BJ-hTERT** (skin fibroblasts, hTERT-only, p53/pRb functional) |
| Cross-validation | **MRC5-hTERT** (embryonic lung fibroblasts, hTERT-only) |
| Marker of all centrioles | Centrin1-GFP |
| Marker of mother (mature) centriole | Cep164-RFP (distal appendages) |
| Senescence markers (endpoint) | SA-β-gal; p21/p16; loss of Ki67 — full operational definition in §4a (Amendment 1) |
| Biosafety | BSL-1; BSL-2 under adenoviral transduction of markers — confirm with local committee |

> Markers are transduced (lentivirus/adenovirus) before the experiment. Polyclonal stable expression is preferred; if necessary, sort for low expression level (marker control — Phase 4).

---

## 3. Platform and culture conditions

- **Imaging:** fluorescence (488/561 nm); objective and camera selected from pre-test V3 (SNR, minimum exposure), NOT fixed before that (TRD §4).
- **Light regime:** minimal light load (FR-7): image only when needed; interval per V2/V3; manipulations in complete darkness from the 3D map of the internal cameras (FR-8).
- **Enclosure:** sealed, 37 ± 0.3 °C, 5 ± 0.5 % CO₂, 2 ± 0.3 % O₂, RH ≥ 90 %; local dehumidification at the camera (TRD §12); sterile entry/exit ports (FR-9).
- **Medium:** phenol-red-free (interferes with fluorescence); antibiotics — at the laboratory's discretion (in long runs they may mask contamination — weigh this).
- **Vessel:** fluorescence-compatible; coating per V1 (fibronectin/collagen/other); 12×12 mm sample stage + adapters (TRD §3.2).
- **Cell removal:** method per V4/V5 (TRD §4, companion comparison); swappable port.

---

## 4. Experimental design

### Phase 0 — Preparation and baseline
1. Expand the line, passage to the working passage range (P5–P25).
2. Seed at low density — clonal tracking from single cells (for the limit fact it is critical to follow individual lineages, not the population).
3. Cell-cycle synchronization NOT recommended (distorts division rate); use single-cell tracking instead.
4. Baseline recording: count, viability, control division rate in a regular plate (reference for V6).

### Phase 1 — Lineage tracking and centriole-age assignment
1. Timelapse: interval per V2 (draft 5–15 min; denser imaging around mitosis; total light dose per FR-7).
2. Mitotic event detection (FR-2: ≥ 90 %).
3. Centriole-age assignment at each division:
   - daughter receiving the **mother** centriole (Cep164+) → «old branch»;
   - daughter receiving the **daughter** centriole (Cep164−) → «new branch»;
   - chronological age = number of generations a centriole has survived since founding (assigned by **pedigree tracking**, not by the marker).
3a. **Identity by location:** no chemical treatment of tracked cells; class OLD/NEW is tied to the cell's position in the chamber and held by spatial registration (FR-12) — the system must not lose who-is-where and must not displace cells.

**How it is determined which daughter receives the older and which the newer centriole at mitosis (assignment method):**
- **First-division anchor (not bootstrap):** in the founder cell the mother (mature) centriole = Cep164+, the newly formed = Cep164−. The daughter receiving Cep164+ → OLD branch (oldest lineage); the daughter receiving Cep164− → NEW branch. After mitosis each daughter contains one mature centriole + one new procentriole, so the «newest» goes to both daughters; the asymmetry is in the mature centriole: one daughter receives the oldest M (founder lineage), the other the younger mature D.
- **Per-mitosis assignment at each division:** image the two centrosomes (two foci) at metaphase/anaphase; determine which centrosome carries the older mature centriole: (a) by continuous pedigree tracking (M is followed from founding), (b) by an age/maturity marker (tubulin PTMs — polyglutamylation/polyglycylation, Odf2/cenexin; the older carries more modifications). Cep164 distinguishes mature vs immature, but not the chronological age of M vs D — so for M vs D an age marker (b) plus pedigree (a) is required.
- **Label-free channel (secondary, optional, to reduce light under FR-7):** the only published morphological correlate of centriole age is a mild spindle/daughter-size asymmetry (Thomas & Meraldi 2024, JCB, PMID 39012627): the larger daughter is more likely to carry the older. Use only after empirical calibration against marker ground truth (if accuracy ≥ 95% — assign without fluorescent light; otherwise markers are mandatory). No data exist for immortalized fibroblasts — calibrate on BJ-hTERT/MRC5-hTERT themselves (V2/V3). Pedigree bootstrap is not needed — the first-division anchor exists.
- **Fallback (if label-free fails):** calibrated morphological-channel accuracy below threshold → the same **marker-anchored method** by which the age of the centrioles of the initial (founder) cell was determined is applied at every division — Cep164 + age marker + continuous pedigree. The marker method is the baseline and always available.
3b. **Polarity registration:** for each lineage, the cell's 3D orientation is preserved — top/bottom pole in addition to left/right (FR-13), data for future centriole transplantation.

### Phase 2 — Maintaining exactly 2 studied cells (method per V4/V5)
- **Design:** exactly **2 single cells are studied** — carrying the oldest (OLD) and the newest (NEW) centriole, side by side. All other cells produced by mitosis **are removed**.
- After Phase 1, the culture is reduced to 2 focal cells: one with the maximal centriole age (OLD), one with age 0 (NEW).
- At each division only the focal lineage continuation is kept; the sister cell is removed:
  - OLD division: the daughter receiving the mother (oldest) centriole continues OLD; the daughter with a new centriole is removed;
  - NEW division: of the two daughters with new centrioles, one continues NEW, the other is removed.
- Removal is a **continuous routine function** (on the order of 1–2 removals per day for the pair, over months), not a one-off procedure. Method per V4/V5 (TRD §4, companion comparison); on the first stage — one working method (laser or micromanipulators); level 2 per V5.
- Accuracy ≤ 2 µm; do not damage the observed focal cells (V4); do not displace them (FR-12).
- Each removal is logged digitally (FR-11) with coordinates, time, method.

### Phase 3 — Measuring division-rate dynamics (primary instrumental task)
1. Record for each of the two focal cells (OLD and NEW, maintained per Phase 2) the **interdivision time** (cell-cycle length) over many generations (months), without opening the enclosure; all other progeny are removed.
2. **Primary endpoint:** the trend of interdivision time OLD vs NEW over time — stable, converging or diverging. Expectation under H1: progressive slowing of OLD relative to NEW (limit-onset signal).
3. **Secondary endpoints:** mitosis duration, divisions per lineage, fraction of quiescent cells, daughter-size symmetry, cohort growth-curve slope.
4. Continue observation until the dynamics answers the limit question (or until the practical time/autonomy horizon; target horizon — months).

### Phase 4 — Statistics, controls and validation
**Replicates:** ≥ 3 independent experiments × 2 lines (BJ-hTERT, MRC5-hTERT).

**Required controls:**
| Control | Purpose | Expectation |
|---|---|---|
| Unpurified mixed culture | Population division-rate reference | Matches the line's literature rate |
| Marker control (Cep164-RFP without removal) | The marker itself does not change division | Interdivision time = unmarked control |
| Sham procedure (method path without action) | The removal procedure creates no selection artefact | No systematic shift in survivors |
| Technical replicates (≥ 3 positions/run) | Instrumental variability | CV ≤ specified (per pilot) |

**Tests:**
- interdivision-time distribution comparison (Mann–Whitney or log-rank on division events);
- OLD vs NEW trend analysis over time (mixed models / rank-based trend tests);
- medians with 95 % CI, effect size; power analysis from pilot (80 % power, α = 0.05).

**Independent confirmation of fluorescence-signal interpretation:**
1. a second marker/method for mother-centriole age (maturity markers Odf2/CD133; tubulin post-translational modifications that accumulate with centriole age) — on a lineage subset;
2. confocal/SIM microscopy of fixed samples at endpoint — cross-check of live interpretation;
3. electron microscopy on a subset (centriole morphology, appendages, dispersion);
4. correlation of assigned age with division rate and senescence markers (SA-β-gal, p21/p16) at limit onset.

---

## 4a. Amendment 1 (2026-11-12) — operational definition of the senescence endpoint

**Why this amendment exists.** Stopping criterion (b) in §1.1a and the marker row in §4 both said «senescence markers/arrest» without defining what counts. A pre-registered criterion that can be interpreted after the fact is not a criterion. This amendment fixes the definition **before any data exist** — no images, no lineages, no pilot run had been produced at the time of writing — so the pre-registration is still prospective.

**Source of the definition.** SenNet consortium recommendations on detecting senescent cells (PMID 38831121, DOI 10.1038/s41580-024-00738-8, *Nat Rev Mol Cell Biol* 2024). Read to abstract and scope only at the time of this amendment; the exact marker panel must be taken from the full text before the protocol is frozen for the pilot. Any change of panel after freezing is a new numbered amendment, not an edit.

**The rule this amendment imports.** A senescent call requires **at least two independent dimensions**, not one marker:

| Dimension | What ARGUS measures | Label-free? |
|---|---|---|
| D1 — durable proliferation arrest | interdivision interval of the tracked lineage, censored at the window end; arrest = no division over a pre-registered multiple of that lineage's own baseline interval | ✅ from the tracking log alone |
| D2 — senescence-associated morphology | nuclear area, eccentricity, texture and cytoplasmic/nuclear ratio per frame; a deep-learning nuclear-morphology score as the quantitative channel (precedent: PMID 37118134, DOI 10.1038/s43587-022-00263-3) | ✅ from the same image stack |
| D3 — molecular markers | SA-β-gal; p16INK4a / p21; loss of Ki67 | ❌ fixed-sample endpoint only |

**Decision rule (pre-registered).** A lineage is called senescent when D1 **and** D2 cross their thresholds; D3 is confirmatory at the endpoint and never a substitute for D1+D2. D1 with D2 negative is called **arrest of undetermined cause** — it counts towards Q2 as arrest, it does not count as senescence, and the difference is reported explicitly rather than collapsed.

**What this does not fix.** SenNet addresses senescent cells in tissues; ARGUS works with immortalised fibroblast lines in vitro, where the marker panel and thresholds are less settled. Applying a tissue consensus to a two-cell in-vitro design is an analogy, and it is recorded as an analogy: D2 thresholds are calibrated in the pilot (Phase 0–1) and frozen before the full run, which is the point at which the analogy becomes a measured operational definition.

**Consequence for §5.** «H1 supported — senescence appears» now means D1+D2 (+D3 at endpoint) as defined here. «No senescence» continues to mean «not detected in the window», never «absent».

---

## 4b. Amendment 2 (2026-11-12) — sampling requirement, power calculation and a readout acceptance test

**Why this amendment exists.** The protocol fixed hypotheses, the stopping criterion and the senescence endpoint, but it never said what sampling the readout needs, or how many cells would be enough. Both were open questions until the readout was benchmarked against generated ground truth on 12 November 2026 (`phantom/`, script, seed and a checksum of the results are in the data room under *TRL evidence pack*). No images, lineages or pilot data existed when this amendment was written, so it remains prospective.

### 4b.1 Sampling requirement — mandatory

**Sampling at the sample must be 100 nm/px or finer; binning above 2×2 is not allowed.**

| Sampling | What the benchmark measured |
|---|---|
| pairs 6–9 px apart (≈80 nm/px) | 0.38 px localisation RMSE, recall 0.78, precision 0.92 |
| pairs 2–3 px apart (≈250 nm/px) | 1.25 px RMSE, recall 0.46, precision 0.99 |

The failure mode is not graceful. Above roughly 150 nm/px the two centrioles of a pair merge into one object, the lineage still looks valid, and the OLD/NEW assignment becomes systematically wrong rather than noisy. A merged pair is worse than a missed detection, because it produces data that passes every downstream check.

Consequence for hardware: with a 40×/0.95 objective and a sensor pitch of 1.55 µm, the sampling is about 39 nm/px — comfortably inside the requirement; the same objective with 4×4 binning (6.2 µm effective pitch) gives 155 nm/px and fails. Any change of objective, camera or binning after this amendment requires a re-run of the acceptance test in 4b.3 and a new numbered amendment.

### 4b.2 Power — how many cells the question needs

Detecting a 2-hour difference in interdivision interval between oldest-centriole and newest-centriole carriers, at α = 0.05 two-sided and power 0.8, with the between-cell interval spread observed in the literature range (σ ≈ 6 h) and the measured localisation error converted through the frame cadence:

**n ≈ 115 cells per group** (≈ 230 tracked lineages in total per line, before attrition).

Three consequences, stated plainly because they change the plan rather than decorate it:

1. The pilot cannot be run on a dozen cells and reported as evidence in either direction; a null result from a small sample is uninformative, not reassuring.
2. Attrition must be counted from the start: lineages lost to the removal procedure, to tracking failure and to senescence censoring all consume the budget. The recruitment target is therefore set at 150 per group per line, with 115 as the analysis floor.
3. The three independent experiments in §4 are replication, not sample size. Each experiment carries its own cohort.

If the true effect is smaller than 2 h, the required n grows as the inverse square: 1 h needs ≈ 460 per group, which is outside what this platform can carry in a single window and is the honest reason to state 2 h as the smallest effect of interest, in advance, rather than discovering it in the analysis.

### 4b.3 Readout acceptance test — to be passed before the first imaging run

The analysis chain (centriole detection, identity persistence, interval extraction) must clear, on the phantom with the frozen seed, at the configured sampling:

| Metric | Threshold |
|---|---|
| localisation RMSE | ≤ 0.6 px |
| detection recall | ≥ 0.75 |
| detection precision | ≥ 0.90 |
| interdivision interval MAE | ≤ 1.0 h (metric to be implemented; not yet scored) |

The last row is the one that is not yet measured — the benchmark of 12 November counts divisions but does not score interval error, and the tracking stage in it is a reference implementation rather than the production lineage tracker. Implementing the interval metric and running the production tracker on the same phantom is a prerequisite for the pilot, and failing it is a stop condition, not a warning.

### 4b.4 What this amendment does not fix

- The phantom is a simulation. It calibrates the instrument and the analysis; it says nothing about whether the hypothesis is true.
- Its cell model is crude: Gaussian body, two Gaussian centrioles, rigid motion, Gaussian PSF.
- Sample-size assumptions use the literature range of between-cell interval spread, not a measured value from these lines; the pilot's own Phase 0 must replace it, and the analysis floor of 115 per group is recalculated then, before the primary endpoint is examined.

---

## 4c. Amendment 3 (2026-11-12) — feasibility of maintaining exactly two cells: what the design actually demands

**Why this amendment exists.** Phase 2 says «exactly 2 single cells are studied, all other progeny are removed». Read quickly, that sounds like isolating a daughter pair at a moment in time. It is not, and the difference decides whether the design is buildable. Written before the removal method is fixed, so the feasibility claim can be audited against the spec rather than against my optimism.

### 4c.1 What the design does not require

- No micromanipulation of a pair at a single instant, no picking, no re-plating, no clonal colony.
- No enzyme treatment of the tracked cells and no disturbance of their position: the chamber stays sealed for the whole run, identity is held by spatial registration (FR-12).
- No dependence on the label-free channel. Markers plus continuous pedigree are the baseline (Phase 1); label-free assignment is an optional way to cut light dose under FR-7 and is used only if calibrated to ≥ 95 % against marker ground truth.

### 4c.2 What it does require, in numbers

The hard part is not isolation, it is a **repeated removal routine that keeps the field at two cells** for months:

| Requirement | Value | Source |
|---|---|---|
| removals per pair | 1–2 per day | Phase 2 |
| horizon | 6–12 months per experiment | §1.1a |
| planned pairs | 6 (3 experiments × 2 lines) | §4 |
| removal events per run-year, derived | ≈ 2,200–4,400 | 1–2/day × 365 × 6 pairs |
| hit accuracy | ≤ 2 µm from target | NFR-2 / FR-5 |
| survival of the observed cell | ≥ threshold set in V4 | FR-5 |
| logging | 100 % of events, with coordinates, time, method | FR-11 |

On the order of a thousand removal decisions per pair per year, each one an opportunity to hit the wrong object or to miss.

### 4c.3 The consequence people underestimate: recoverability beats reliability

At 99.9 % per-event reliability over 4,000 events the probability of a clean run is (1 − 0.001)^4000 ≈ 0.018 — two in a hundred. Perfection is not an achievable target, so the design cannot be built around it. What it is built around is recovery:

1. **Detection latency below one doubling time.** A missed removal leaves a sister that begins to divide; the tracker runs at 5–15 min cadence against a ~24 h interdivision time in BJ-hTERT, so contamination is caught two orders of magnitude before it becomes a colony. Mitosis detection is specified at ≥ 90 % (FR-2) and every newly appearing cell is a trigger, not an exception.
2. **Re-anchoring at every division.** OLD/NEW is re-derived at each mitosis from marker plus pedigree, so a single ambiguous frame cannot silently propagate a wrong lineage identity.
3. **Every event logged and auditable.** A run with a removal failure is not discarded; the failure, its detection time and its correction are in the log (FR-11), and the affected interval is censored.
4. **Selection artefact controlled, not assumed away.** Sham procedure and unpurified reference run in parallel (§4 Phase 4); if survivors shift systematically, that is the finding, and it is reported.

### 4c.4 The one failure that stops the design

If no level-1 removal method (laser, micromanipulators, per the companion comparison) meets both V4 survival and NFR-2 accuracy, Phase 2 changes shape rather than being waived: the pair is maintained by **periodic manual splitting at intervals**, with identity re-anchored by pedigree at each split. That costs handling steps, adds light and manipulation per split, and reduces the number of usable lineages per experiment — a real cost to sample size that must be re-costed against the 115-per-group floor of §4b.2. It is stated here, before the run, so that the fallback is a documented design change and not an unannounced substitution.

### 4c.5 What remains genuinely unproven

Removal-module survival on these lines (V4), necrosis and debris management (V5), and month-scale mechanical reliability of the stage and enclosure (V8). None of these is answered by argument, and none of them is answered by the synthetic benchmark, which calibrates optics and analysis only. They are answered by pre-tests that are already dated, and the answer can be negative.

---

## 5. Success criteria (ARGUS acceptance, per TRD §8)

| Function | Criterion |
|----------|-----------|
| FR-2 mitosis detection | ≥ 90 % divisions detected |
| FR-3 centriole tracking | SNR ≥ 3× above background; Completeness ≥ 80 % |
| FR-4 OLD/NEW dynamics | Trend statistically detectable (pilot → power) |
| FR-5 removal | Accuracy ≤ 2 µm; observed-cell survival ≥ specified (V4) |
| FR-7 light load | Within NFR-12 while meeting SNR (V3) |
| FR-11 logging | 100 % events registered |

**Answer to the scientific question (what counts as an answer):**
- H0 supported: OLD and NEW divide at the same stable rate over the whole observation window, no senescence → «no limit detected in the observation window» (with the caveat about the horizon).
- H1 supported: OLD slows relative to NEW, senescence/dispersion markers appear → the fundamental fact (immortalized fibroblasts have a Hayflick limit) is established. «Senescence appears» means the endpoint of §4a (D1+D2, D3 confirmatory), not a single marker.

---

## 6. What is NOT established and risks (honest assessment)

1. **Segregation pattern** of mother/daughter centrioles in BJ-hTERT/MRC5-hTERT may be symmetric/stochastic — then OLD/NEW classes do not form. Checked in Phase 1 before mass removal.
2. **Removal of intermediate cells** may itself select stress-resistant cells → systematic shift. Control — sham procedure and unpurified reference.
3. **Small population after removal** → risk of lineage extinction; keep buffer copies in a parallel plate.
4. **Cep164-RFP SNR in live cells** may be insufficient → V3 (camera/filters/exposure) or an alternative mother-centriole marker.
5. **Observation horizon:** the ~800–1000-division limit may not arrive within realistic time — then «not detected in window» ≠ «no limit». This is recorded as the boundary of the conclusion.
6. **Long run (months)** → medium drift, fouling, condensation, contamination — standard enclosure mechanisms (TRD §12, FR-9) and monitoring.
7. **Phototoxicity in long observation** → «image on demand» mode (FR-7); control — V6 (proliferation in chamber vs plate).
8. **Reliability of continuous removal (Phase 2):** a removal failure/error accumulates (each unremoved sister cell generates new progeny and fouls the field). Critical: the removal method and tracking must run for months with minimal failures; safeguard — frame verification and alerts (FR-11).

---

## 7. Schedule, dependencies and pre-tests

| Step | Dependency | Deadline |
|------|------------|----------|
| Pre-tests V1–V6 (V2 — migration/interval, V3 — marker SNR, V4 — survival at removal, V5 — necrosis, V6 — environment effect) | — | 03.11.2026 |
| TRD v1.0 (fix optics/camera/filters, removal method) | pre-tests | 06.11.2026 |
| Pilot protocol (Phases 0–1, 20–30 lineages) | TRD v1.0 | after 06.11 |
| Power analysis → full run (Phases 1–3, months) | pilot | per plan |
| Analysis and report | full run | per plan |

---

## 8. Result registration

- Full digital event log (divisions, removals, media changes) — from ARGUS (FR-11).
- Tables: lineage_id, class (OLD/NEW), interdivision time by generation, fate (alive/removed/extinct), light dose.
- Report output: OLD/NEW trends, medians (95 % CI), distributions, effect size, senescence markers, conclusion on the fundamental fact (H0/H1).

---

## 9. Future directions (after the fundamental fact)

1. **Cancer cells (if time permits):** the same dynamics; control — whether a young centriole arises next to the oldest one in the same cell (supernumerary centrioles); role in postponing/masking the limit; clarifying cancer origin.
2. **Centriole transplantation:** experiments transferring centrioles between cells require knowledge of cell polarity — top/bottom pole in addition to left/right. ARGUS therefore registers polarity from the first stage (FR-13).
3. **Stem-cell niches (students/research staff):** counting the limit in a specific, not-yet-counted stem-cell niche.
4. **Cardiac eliminate-reprogram-rebuild:** a separate protocol on the same platform.

---

*v0.2 — primary goal changed to the fundamental fact (Hayflick limit in immortalized fibroblasts) and the instrumental task (OLD/NEW dynamics). Companion documents: TRD v0.9b (docs/ARGUS_TRD_v0.9b.md), Cell Removal Methods Comparison (docs/ARGUS_Cell_Removal_Methods_Comparison.md).*

*Amendment 1 (2026-11-12): the senescence endpoint of stopping criterion (b) is operationally defined in §4a (SenNet, PMID 38831121), before any data were collected.*
*Amendment 2 (2026-11-12): sampling requirement (≤ 100 nm/px), power calculation (n ≈ 115 per group) and the readout acceptance test fixed in §4b, from the synthetic benchmark deposited as DOI 10.5281/zenodo.24148459.*
*Amendment 3 (2026-11-12): feasibility of maintaining exactly two cells, the recoverability argument and the stop condition for the removal module stated in §4c.*
