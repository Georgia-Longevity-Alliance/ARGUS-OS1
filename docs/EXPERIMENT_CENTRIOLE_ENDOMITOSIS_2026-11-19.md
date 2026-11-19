# Experimental branch — do endomitotic cells keep their centrioles?

**Opened:** 2026-11-19 · **Branch:** `exp/centriole-endomitosis` · **Owner:** PI (Jaba Tqemaladze)
**Status:** 🟡 protocol only — no data, no claims. Nothing in this document has been measured.

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

## 2. Hypotheses and their signatures

| # | Hypothesis | Prediction at L2–L4 (per intestinal cell) |
|---|---|---|
| **H1** | Centrioles are **retained and continue to duplicate** with each endoreplication cycle | centriole number per cell **rises** with ploidy; multiple centrioles per cell, not per nucleus |
| **H2** | Centrioles are **retained but not duplicated** (licensing blocked without mitosis) | constant number per cell across cycles; ≥1 centriole persists indefinitely |
| **H3** | Centrioles are **eliminated** after the last canonical cycle (as in most embryonic lineages) | zero centrioles by L2; a centrosome-free, acentriolar cell |
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

## 9. Execution order (cheapest first)

1. **Feasibility (1–2 days):** can the centriole marker be counted in a binucleated intestinal cell?
   If not, stop here.
2. **Fixed arm (1 week):** L1/L2/L3, DAPI + centriole marker, rings 3–9 vs rings 1–2. Gets H1/H2/H3
   directionally without live imaging and without dose risk.
3. **Live arm (2–3 weeks):** time-lapse L1→L4 with the four channels and the furrow gate; light-dose
   budget first.
4. **Only then:** decide whether this becomes a manuscript or a paragraph in CEDAR.

## 10. What would make it publishable

The negative-but-useful result is publishable: *"centrioles are retained/duplicated/lost during
endomitosis"* resolves a documented blind spot and gives the centriole-elimination field its first
polyploid tissue. The strong version links it to CEDAR's counter (H1 vs H2). The weak version is a
descriptive note in an ARGUS methods paper. Either way, the first step is the feasibility check.

---

**Related:** `results/R3_N_SCALING_2026-11-19.md` (why the furrow gate exists, measured),
`software/pipeline/lineage.py` (the gate), `docs/ANALYSIS_2026-11-19_Endomitosis_CentralSpindle_Celegans.md`
(the analysis that produced this branch), `EVIDENCE.md` §2026-11-19.
