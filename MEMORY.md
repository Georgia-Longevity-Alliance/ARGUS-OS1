# MEMORY — ARGUS-OS1

## 2026-07-23: WilliamW — Motor release already in Sangaboard 🔌

> Reply on OpenFlexure Forum (22 Jul). Sangaboard firmware **already contains** motor release command — cuts current to motor coils. Not exposed in standard API, but adding it to API is a minimal fix.
> **Consequence:** no need for TMC2209 + MOSFET rework. Call motor release via API between acquisitions (every 10 min) → heat problem solved in software.

## 2026-07-22: AUTOFIX v5 — Extended Script + Deep Review 🔧

> **Script:** autofix.sh v5 (added: git status, budget consistency, language check, ref-duplicates, core-files).
> **Fixes (10):**
> 1. `_pi.md` — translated to English (was Russian). Core-file rule.
> 2. `PARAMETERS.md` — version synced (147→150). Formatting fixed (`**Version:` → `**Version:**`).
> 3. `PARAMETERS.md` — budget updated ($35K→$98K, matching CONCEPT.md).
> 4. `MAP.md` — CONTRIBUTING/CODE_OF_CONDUCT/SECURITY moved to docs/ (were listed at root).
> 5. `MAP.md` — added scripts/, updated letters/ listing.
> 6. `CONCEPT.md` — duplicate reference numbers fixed (#2, #7 → sequential 1-14).
> 7. `TODO.md` — added deadlines, owners, phases (was bare list).
> 8. `STATE.md` — version (v112→v150), platform (V8→V7), budget ($81K→$98K).
> 9. `CONCEPT.md` — Iron-Based Centriole Detection section translated to English.
> 10. `MEMORY.md` — all entries translated to English.
>
> **Score:** 97/100 (3 remaining: git uncommitted — needs manual review).

## 2026-07-21: Iron-Based Centriole Detection 🔴

> Heidenhain's iron haematoxylin — the method Boveri used to discover centrioles (Scheer 2014, PMID 25047623). Added to CONCEPT.md §3 as a routine method for detecting whole centrioles without transgenic constructs. $5-10/sample. May detect iron-positive remnant after structural elimination. No one has applied this to C. elegans for centrioles.

## 2026-07-21: Gönczy Reply — Centrioles Retained for Functional Reason 🔴

> Pierre Gönczy (pers. comm.): centrioles in terminally differentiated cells of the C. elegans somatic gonad are retained for a functional reason — "to be able to build a centrosome or for some signaling function." This supports the ARGUS hypothesis: retained centrioles are not inert remnants but functionally significant objects. Added to CONCEPT.md §0.

---

## v112 (2026-07-21) — English, C. elegans only, V8 light-sheet

> All files translated to English. Model: C. elegans only. Platform: ARGUS V8 (light-sheet). Budget: $81K (V7). 10 verified references.

## Earlier versions

See git history. Key milestones: Odf2/Phase2 removed (v97). RPE1 removed (v106). Light-sheet added (v110). English (v112).
