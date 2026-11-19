# Experimental branch — do endomitotic cells keep their centrioles?

**Opened:** 2026-11-19 · **Branch:** `exp/centriole-endomitosis` · **Owner:** PI (Jaba Tqemaladze)
**Status:** 🟢 **step 1 (feasibility) CLOSED from the literature on 2026-11-19** — H3 falsified, marker validated.
The branch now starts at Q2 (see §9). No new data yet.

---

## 1. The question, and why it is open

In the *C. elegans* intestine, 14 posterior cells (rings 3–9) undergo **endomitosis** in L1:
a full M phase with chromosome segregation, **no central spindle, no cytokinetic furrow**, giving
binucleated cells, followed by endoreplication at the end of L1–L4 to a final ploidy of **64C**
(Barrull-Mascaró et al., *J Cell Biol* 226:e202604104, 2026, PMID **43037622**;
preprint `10.1101/2025.08.04.668394`).

**Nothing in that paper — or in any source found on 2026-11-19 — says what happens to the
centrioles** of such a cell:

| Check (2026-11-19) | Result |
|---|---|
| `centriole` in the endomitosis paper's full text | **0 hits** |
| `SAS-`, `PLK-4`, `SPD-2`, `MTOC` in that full text | **0 hits** |
| `centrosome(s)` | 4 hits, all about astral microtubules and PLK-1 localisation |
| Any paper connecting endomitosis/polyploidy to **centriole number** | not found in PubMed/Europe PMC/arXiv/OpenAlex queries listed in §8 |

So two well-developed literatures — **centriole elimination** (Kalbfuss & Gönczy, *Sci Adv* 2023,
PMID **37256957**; review PMID **37963546**) and **endomitosis/polyploidy** — do not meet. The
intersection is empty, and it is exactly where our two projects live.

**Why it matters for us.** CEDAR's counter runs on centriole replication, which is coupled to
S phase. An endomitotic cell is the cleanest natural test of that coupling: it keeps running S
phases (to 64C) while cytokinesis is transcriptionally switched off. If centrioles keep duplicating
there, the counter runs without divisions — a direct, observable case of "replication counter ≠
division counter". If they are lost or stabilised instead, CEDAR's coupling assumption needs
revision. Either outcome is informative, which is the mark of a good side-arm.

## 1b. STEP 1 RESULT — already answered, no bench time needed (2026-11-19)

Kalbfuss & Gönczy, *Sci Adv* 2023 (PMID **37256957**, doi:10.1126/sciadv.adg8682, OA, PMC10413642),
full text, verbatim:

> «…all 41 proliferating cells maintained centrioles. **Moreover, all 20 intestinal cells, which
> later endoreduplicate, with some undergoing endomitosis, maintained centrioles in L1 larvae**,
> although they undergo elimination later in development.»

Consequences, in order of importance:

1. **H3 (elimination before/at endomitosis) is FALSIFIED.** All 20 intestinal cells keep centrioles in
   L1, including the 14 that endomitose. Fig. 1B of that paper shows intestinal cell `int2V` with a
   centriole focus as an explicit example.
2. **The marker question is answered.** The authors scored **GFP::SAS-7** and **GFP::SAS-4** — exactly
   the markers in §4 — in intestinal cells of live L1 animals (lattice light-sheet). Feasibility of
   *detection* = **PASS**.
3. **A dated elimination event exists in the intestine**, later in development rather than at
   endomitosis. That date is a measurable target and the first thing CEDAR needs (Q4).
4. **A technical trap, now explicit:** light microscopy scores a centriole **focus** (one centriole
   pair), not individual centrioles. "Retained" vs "duplicated" (H1 vs H2) needs resolution beyond a
   focus — see how Croisier, Kalbfuss & Gönczy 2025 (PMID **40475707**) had to use **serial-section EM**
   to prove that SAS-4/SAS-7 foci in L1 rectal cells (B, F, U, Y) are bona fide centrioles.

**Note on the "7 retainers".** The 2025 microPublication reports 7 **post-mitotic** cells retaining foci
in L1 (B, F, U, Y rectal epithelial among them). The 20 intestinal cells are a *separate* class in the
2023 paper (they are not post-mitotic — they endoreplicate). Both statements are consistent; do not
conflate them in any manuscript text.

## 2. Hypotheses and their signatures

| # | Hypothesis | Prediction at L2–L4 (per intestinal cell) |
|---|---|---|
| **H1** | Centrioles are **retained and continue to duplicate** with each endoreplication cycle | centriole number per cell **rises** with ploidy; multiple centrioles per cell, not per nucleus |
| **H2** | Centrioles are **retained but not duplicated** (licensing blocked without mitosis) | constant number per cell across cycles; ≥1 centriole persists indefinitely |
| ~~**H3**~~ | ~~Centrioles are eliminated after the last canonical cycle~~ | **FALSIFIED 2026-11-19** — all 20 intestinal cells keep centrioles in L1 (PMID 37256957); elimination happens *later* in development, now a dated target (Q4) rather than a hypothesis |
| **H4** | Mixed: duplication proceeds but clusters/amplifies | centriole clusters, supernumerary centrioles inside one binucleated cell |

H1 vs H2 is the discriminator CEDAR needs: H2 says the replication counter and the division
counter are **coupled by licensing**, H1 says they can be **decoupled**.

## 3. System and staging

- **Organism/stage:** *C. elegans*, intestinal cells, imaged from late embryo through L1 (endomitosis)
  and into L2–L3 (endoreplication cycles). Intestinal rings 3–9 = the 14 endomitotic cells; rings 1–2
  do not endomitose → **internal control within the same animal**.
- **Reference divisions:** seam cells (canonical cycles throughout larval life) — positive control
  for a normal centriole cycle.
- **Staging anchor:** intestinal nuclei count (20 cells → 34 nuclei after endomitosis) and the
  `elt-2`/`elt-2p::mCherry` intestine marker.

## 4. Markers (four channels, all established in this organism)

| Channel | Purpose |
|---|---|
| Centriole marker (endogenously tagged **SAS-4** or **SPD-2**, fluorescent) | centriole number and position per cell |
| Membrane (**GFP-PH** or mCherry-PH) | the **furrow gate** — division vs nuclear split (see `software/pipeline/lineage.py`) |
| Nucleus (**H2B-mCherry**) | nuclear count, binucleation, ploidy proxy (integrated intensity) |
| Optional: **SAS-6 phospho-status** (EMBO Rep 2025, PMID **40410380**) | candidate "doomed centriole" readout; exploratory only |

**Light-dose budget is mandatory** before imaging: `software/pipeline/light_dose.py` (R8). Four
channels on a live animal at 40× dry is the expensive case; the gate refuses to judge without an
explicit `--max-j-cm2` measured on our own sample, and no threshold in this protocol is invented.

## 5. Readouts (per cell, per timepoint)

1. Centriole count per cell, and per nucleus.
2. Furrow index at each nuclear split → event class from `lineage.py`
   (`division` vs `nuclear_split_no_furrow`).
3. Ploidy proxy: nuclear H2B-mCherry / Hoechst integrated intensity, calibrated on a diploid and a
   binucleated reference.
4. Centriole-to-nucleus geometry (are centrioles shared between the two nuclei of a binucleated cell?).

## 6. Design and statistics

- **n = 30 animals** per condition minimum, ≥3 independent experimental days.
- **Primary comparison:** rings 3–9 (endomitotic) vs rings 1–2 (non-endomitotic) **within the same
  animal** — paired design, removes animal-to-animal variance.
- **Primary test:** centriole count per cell at L2. Equivalence framing, not "significant difference":
  we must be able to say "unchanged" honestly → use **TOST/equivalence bounds** (±1 centriole) rather
  than a failure to reject H0.
- **Pre-registered decision rule:**
  - H1 if median count rises by ≥2 from L1 to L3 in rings 3–9 (p<0.05, paired);
  - H2 if the median is unchanged within ±1 centriole (equivalence);
  - H3 if centrioles are undetectable in ≥80 % of rings 3–9 cells at L2;
  - H4 if clusters (>4 centrioles/cell) appear in a bimodal distribution.

## 7. Controls and falsification

| Control | What it excludes |
|---|---|
| Seam cells in the same animal | marker failure presented as "elimination" |
| Rings 1–2 (non-endomitotic) | a tissue-wide artefact |
| `zen-4` RNAi or CYE-1/CDK-2 forced M phase (as in PMID 43037622) | "endomitosis" being a fixation/imaging artefact |
| Marker-only strain without the centriole tag | bleed-through mistaken for centrioles |
| Fixation + DAPI arm (separate from live imaging) | light-induced centriole loss (see R8 dose budget) |

**Falsifiers.** H1 is false if centriole number per cell is flat while ploidy doubles. H2 is false
if number rises or falls outside the equivalence band. H3 is false if any ring 3–9 cell retains a
centriole past L3. **The whole branch is uninformative if** the centriole marker cannot resolve
individual centrioles in a binucleated cell — that must be established first (§9 step 1).

## 8. Searches already done (so nobody repeats them)

Run 2026-11-19 on PubMed/Europe PMC and OpenAlex: `C. elegans intestine polyploid endoreplication
ploidy`, `centrosome amplification polyploid endoreplication centriole reduplication`, `centriole
elimination C. elegans embryo intestine`, `endomitosis central spindle intestine`. Result: the
centriole-elimination corpus (PMID 37256957, 37963546, 40410380) and the endomitosis corpus
(43037622, 35609035, 38727809) are disjoint. **Not a systematic review** — a systematic search is
step 0 before any manuscript claim.

## 9. Execution order — revised after the step-1 result

| # | Question | Cost | Status |
|:--:|---|:--:|---|
| **Q1** | Do intestinal cells have centrioles at L1, and can SAS-4/SAS-7 resolve them? | 10 min (literature) | ✅ **ANSWERED 2026-11-19** — yes, all 20 (PMID 37256957) |
| **Q2** | Once the cell is binucleated (L2–L4): **how many foci per cell, and per nucleus?** One shared, or one per nucleus? | **1 day imaging**, fixed arm | open — the real first measurement |
| **Q3** | Does the number of **centrioles per focus** rise with ploidy (duplication = H1) or stay two (H2)? | 2–4 weeks: U-ExM, or serial-section EM as in PMID 40475707 | open — needs sub-focus resolution |
| **Q4** | When exactly are intestinal centrioles eliminated, and does that date track ploidy (64C) or animal age? | 1 week, fixed L1→adult series | open — the CEDAR-relevant date |

**Do Q2 first, and only Q2.** One day of imaging on an already-published strain decides whether Q3/Q4
earn their cost:

- **2 foci, one per nucleus** → the pair is *partitioned* between the two nuclei, so duplication must
  proceed without division: that is H1's signature and it justifies Q3.
- **1 focus, shared** → one pair is kept while the genome doubles: H2 becomes the live hypothesis and
  Q3 is unnecessary.
- **0 foci in some cells** → mixed population; Q4 (dating) comes first.

**Strain logistics — the only real bottleneck.** The published work used GFP::SAS-4 / GFP::SAS-7 with
pan-nuclear mCherry::HIS-58 and `elt-2p::GFP` for the intestine. Before any bench time:
(1) check the **Caenorhabditis Genetics Center** for these alleles; (2) if absent, **request them from
the authors** (published reagents, standard C. elegans practice); (3) only if both fail does a cross
become necessary — and a cross is **2–3 weeks**, not 1–2 days. That cost belongs in the plan, not in
the surprise.

## 10. What would make it publishable

The negative-but-useful result is publishable: *"centrioles are retained/duplicated/lost during
endomitosis"* resolves a documented blind spot and gives the centriole-elimination field its first
polyploid tissue. The strong version links it to CEDAR's counter (H1 vs H2). The weak version is a
descriptive note in an ARGUS methods paper. Either way, the first step is the feasibility check.

---

**Related:** `results/R3_N_SCALING_2026-11-19.md` (why the furrow gate exists, measured),
`software/pipeline/lineage.py` (the gate), `docs/ANALYSIS_2026-11-19_Endomitosis_CentralSpindle_Celegans.md`
(the analysis that produced this branch), `EVIDENCE.md` §2026-11-19.
