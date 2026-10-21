# PROTOCOL v0.2: Is there a Hayflick limit in immortalized fibroblasts? Division-rate dynamics of cells with the oldest and newest centriole

**Author:** Jaba Tqemaladze¹
**Date:** 2026-10-21
**Status:** 🟡 hypothesis-grade protocol for validation on the ARGUS platform. All parameters are calibrated by pre-tests (V1–V6, TRD §6). NOT a ready laboratory protocol before pre-test data.
**Platform:** ARGUS (see `docs/ARGUS_TRD_v0.9b.md`)

¹ Georgia Longevity Alliance.

---

## 1. Goal and hypotheses

### 1.1 Fundamental fact (primary goal)

**Test whether immortalized human fibroblasts (BJ-hTERT, MRC5-hTERT) have a Hayflick limit — yes or no.**

- **H1 (working hypothesis):** a limit exists even with hTERT expression — it is simply much larger than in somatic cells and is masked at the population level by rapid colony growth.
- **H0 (null):** no limit — true «immortality» of immortalized fibroblasts.

This is the anchor: without the established fundamental fact, all subsequent tasks (cancer cells, stem-cell niches) are more complex and their results more controversial.

### 1.2 Context — expected division counts

The limit experiment is identical for any cell type; only the expected number of divisions differs:

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
| Senescence markers (endpoint) | SA-β-gal; p21/p16; loss of Ki67 |
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
- H1 supported: OLD slows relative to NEW, senescence/dispersion markers appear → the fundamental fact (immortalized fibroblasts have a Hayflick limit) is established.

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
