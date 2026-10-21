# ARGUS — How to Determine, by Morphology Visible in Light Microscopy (No Staining), Which Daughter Will Receive the Older and Which the Newer Centriole after Mitosis

**Date:** 2026-10-21
**Author:** Jaba Tqemaladze (Georgia Longevity Alliance)
**Status:** deep analysis of the question; single cell; first fibroblasts, then immortalized fibroblasts. Every claim carries a source (PMID/DOI).
**Russian master:** `ARGUS_label_free_centriole_assignment_2026-10-21.md`.

---

## 1. Framing and what is inherited at mitosis

Question: **one cell, light microscopy only, no fluorescent staining** — by which visible features (geometry, dimensions, shape, dynamics) to determine, after mitosis, which of the two daughter cells receives the **oldest** centriole and which the **newest**.

**Biology (what is inherited).** In G2 the cell has 4 centrioles: two "mature" (M — inherited from the mother, age N generations; D — formed last cycle, now mature, age 1) and two new procentrioles (age 0). Two centrosomes: {M + new procentriole} and {D + new procentriole}. At mitosis each daughter receives **one centrosome** = one mature (mother) centriole + one new procentriole.

**Important consequence:** after mitosis **both daughters contain a newest (just-formed) centriole** — the "newest" goes to both. The real asymmetry is in the **mature** centriole: one daughter receives the **oldest** M (founder lineage), the other the **younger mature** D (age 1). The task is therefore: **determine which daughter receives the older mature (M) and which the younger mature (D).**

## 2. What light microscopy can and cannot see without staining

| Feature | Visible in light microscopy without staining | Comment |
|---|---|---|
| Centriole as object (~200–250 nm) | ❌ | at/beyond the diffraction limit (~250 nm at NA≈1.2); invisible without contrast |
| Mother-centriole appendages | ❌ | ~100 nm, EM only |
| PTM differences (age) | ❌ | molecular; invisible without staining |
| Pericentriolar-material differences | ❌ | beyond resolution without contrast |
| **Daughter cell size/volume** | ✅ (phase/DIC) | direct measurable feature |
| **Spindle geometry, metaphase-plate position, asters** | ✅ (DIC/phase/polarized) | spindle of ordered microtubules gives contrast; asters visible in polarization |
| **Dry mass of the cell** | ✅ (QPI — quantitative phase) | label-free, measurable |
| Dynamics (anaphase timing, aster movement) | ✅ (time-lapse DIC/phase) | kinetic feature |

## 3. What is actually known from the literature (honest)

**The only published light-microscopy correlate of centriole age in division is a mild spindle/daughter-size asymmetry:**

- **Thomas & Meraldi 2024 (J Cell Biol; PMID 39012627, DOI 10.1083/jcb.202311153):** in **human epithelial and fibroblastic lines** centriole age "breaks spindle symmetry even in symmetric divisions" → **unequal daughter sizes**. Mechanism: the old centriole carries more Odf2/cenexin-bound Plk1 → higher microtubule nucleation (pericentrin, γ-tubulin, TPX2, ch-TOG) → **the half-spindle on the old-centriole side is longer**.
- **Direct morphological consequence:** without staining, by daughter size (and/or spindle asymmetry), one can *probabilistically* indicate where the older centriole is — but the effect is **weak** (not deterministic).

**What does NOT exist in the literature:**
- No method that unambiguously assigns the older centriole to one of two daughters in fibroblasts by geometry/size in light microscopy.
- No data for **immortalized fibroblasts** (BJ-hTERT/MRC5-hTERT) on centriole-age asymmetry at all — a gap (to be covered by pre-test).
- Segregation stochasticity in culture: no documented geometric rule ("older always to adhesion / to the right") for cultured fibroblasts (unlike the Drosophila niche, where position is rigid; Yamashita 2007, PMID 17255513).

## 4. Method options (morphology only, label-free)

### Option A — Daughter size/volume (phase/DIC) [published]
- Measure daughter areas/volumes at cytokinesis (phase/DIC). The larger daughter is more likely to carry the older centriole.
- Pros: simple, cheap, live, no excitation light.
- Cons: weak effect (Thomas & Meraldi 2024) → in a **single** cell this is only a probability P ≈ 0.5+δ, δ small; insufficient for rigorous assignment.
- **Fibroblasts:** included in Thomas & Meraldi (weak effect present). Immortalized — no data.

### Option B — Spindle/aster geometry (DIC/phase, polarized light) [mechanism published]
- The half-spindle on the old-centriole side is longer; the aster on the old side is larger/brighter in polarization (more ordered MTs).
- Metrics: metaphase-plate offset from center; half-spindle length difference; aster intensity in polarized light; astral-MT asymmetry.
- Pros: directly reflects the mechanism (nucleation), label-free.
- Cons: requires polarization/quality optics and kinetic imaging; the "side → daughter" + "side → older" link remains probabilistic.

### Option C — Quantitative phase / dry mass (QPI) [label-free, mature technique]
- Phase/holographic microscopy gives dry mass of daughters; mass asymmetry is more quantitative than area.
- Pros: label-free, more accurate than A; suitable for long runs (not phototoxic, FR-7).
- Cons: separate optics; link to centriole age remains weak (via size, as in A).

### Option D — Division kinetics (time-lapse DIC/phase) [not proven for age]
- Differences in anaphase-onset time, separation speed, cytokinesis symmetry between sides. Possibly correlates with nucleation asymmetry (B), but no direct data for centriole age — experimental hypothesis.

### Option E — Empirical calibration of a morphological predictor (recommended) [plan, not literature]
- **Idea:** to use only morphology (no staining) in the long run — first run a calibration phase on the same lines/conditions WITH fluorescent markers (Cep164 + age marker, pedigree) to obtain **ground truth** (which daughter got the older centriole). In parallel record a battery of label-free features: daughter size/volume, spindle asymmetry, plate offset, aster asymmetry in polarization, dry mass (QPI), kinetics.
- Train a classifier "older goes to daughter A or B" on ground truth; report accuracy (e.g., % correct assignments per division).
- **If accuracy is high (e.g., ≥ 95%):** in the working run assign OLD/NEW by morphology — and remove almost all fluorescent light (the main saving under FR-7). **If below threshold:** markers remain mandatory.
- Pros: the only honest path to "label-free" in ARGUS; turns a weak effect into a verified metric; directly serves minimal phototoxicity.
- Cons: requires a marker calibration phase; accuracy depends on lines and effect size.

### Option F — Pedigree bootstrap [NOT NEEDED in this experiment]
- Logical boundary: in the founder cell, without any anchor, "which of two centrioles is older" cannot be determined by morphology alone.
- **In this experiment it is not required:** the anchor exists — the founder's first division, where mother (mature, Cep164+) and newly formed (Cep164−) are distinguishable. The Cep164+ daughter → OLD branch; the Cep164− daughter → NEW branch. Thereafter age is assigned by continuous lineage tracking. Bootstrap over generation probabilities is unnecessary.

## 5. Fibroblasts and immortalized fibroblasts

- **Normal fibroblasts:** the only known effect is the mild spindle/daughter-size asymmetry (Thomas & Meraldi 2024, included fibroblastic lines). No geometric inheritance rule documented.
- **Immortalized fibroblasts (BJ-hTERT/MRC5-hTERT):** **no data at all** — neither on centriole-age asymmetry nor on a morphological correlate. Gap to be closed by pre-test V2/V3 (division behaviour, morphology) in the calibration phase with markers (Option E).

## 6. Honest conclusion

1. **By morphology alone, without staining, an unambiguous determination of which daughter receives the older centriole is not possible today**: the only published correlate (size/spindle, Thomas & Meraldi 2024) is weak and probabilistic, and there are no data for immortalized fibroblasts.
2. **The practical path compatible with "no staining in the working run" is empirical calibration (Option E):** a short marker phase gives ground truth; a label-free morphological classifier (daughter size + spindle + QPI + polarization + kinetics) is trained on it; if accuracy is high — work without fluorescent light (minimal phototoxicity). **If label-free does not work (accuracy below threshold) — the same marker-anchored method by which the age of the centrioles of the initial (founder) cell was determined is applied at every division: Cep164 + age marker + continuous pedigree.** The marker method is always available as the baseline.
3. **Logical boundary resolved:** the first assignment in the founder cell does not require bootstrap — the first division anchors OLD/NEW (Cep164+ vs Cep164−). Thereafter label-free, calibrated morphology can be used if Option E succeeds.
4. Consequently, for rigorous Q2/Q3 (protocol v0.2) the OLD/NEW assignment is **marker-anchored** (Cep164 + age marker + pedigree); label-free morphology serves as a **calibrated secondary channel** — and as a way to reduce the light load if calibration allows.

---

*Prepared with the assistance of AI tools for search; scientific claims verified against PMID/DOI. Companion documents: ARGUS_Protocol_v0.2, ARGUS_TRD_v0.9b, ARGUS_Literature_Analysis_EN.md.*
