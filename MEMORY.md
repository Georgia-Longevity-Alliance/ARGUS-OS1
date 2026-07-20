# MEMORY — ARGUS-OS1

## 🔴 v51 — Renamed ARGUS-LP_OS → ARGUS-OS1 (2026-07-20)

> Comprehensive audit. ARGUS-OS2 and ARGUS-OS3 = separate projects. All 28 references verified. PMID error (7544801→7642707) fixed.

### Ключевые изменения:
1. ✅ **Переименование:** ARGUS-LP_OS → ARGUS-OS1
2. ✅ **ARGUS-OS2 (v2.0):** Causality — Ninein KD + Odf2 domain deletions
3. ✅ **ARGUS-OS3 (v3.0):** Progenitor maps — fs-laser + manipulators + mtDNA
4. ✅ **28 источников проверены** через PubMed (docs/COMPREHENSIVE_AUDIT_2026-07-20.md)
5. ✅ **PMID 7544801→7642707** (Lange & Gull 1995)
6. ✅ **letters/ исключён** из публичного GitHub

---

## 🔴 v50 — Peer Review #8 Response + Mechanism + Time-to-Ciliogenesis (2026-07-19)

> Ответ на строгое peer review (оценка 6.5→8.5/10). Все замечания приняты и внедрены.

### Ключевые изменения:
1. ✅ **Time-to-ciliogenesis — primary endpoint.** Заменён бинарный исход. Kaplan-Meier + Cox PH. Мощность выше, информативнее.
2. ✅ **β-catenin/Wnt механизм.** Valdes Michel & Phillips 2025 (PMID 39813084): centrosomal degradation of β-catenin → transcriptional asymmetry. Прямой механизм «центросома→ядро→судьба».
3. ✅ **hTERT-NPCs в Phase 1.** Параллельно с RPE1. Royall 2023 уже показал эффект в NPCs.
4. ✅ **Lineage tree.** 3 поколения (мать→дочери→внучки→правнучки). Эксплицитно в дизайне.
5. ✅ **H₁ усилена.** Платформа = самостоятельный результат, даже при нулевом биологическом исходе.
6. ✅ **Ki67.** Вторичный endpoint: пролиферативный статус.
7. ✅ **Новые PMID:** 39813084, 34630857, 39764850. Всего 26 ссылок.

### Исправлено по замечаниям рецензента:
- Цилиогенез — не судьба → добавлены маркеры дифференцировки (NPCs), Ki67, time-to-event
- RPE1 — не стволовые → NPCs добавлены в Phase 1 параллельно
- Однопоколенный анализ → lineage tree на 3 поколения
- Чёрный ящик → β-catenin/Wnt механизм найден и добавлен
- Бинарный исход → заменён на time-to-ciliogenesis
- План Б → H₁ как standalone platform result

### Верификация ссылок рецензента:
- Ishikawa 2005 (PMID 15852003): ✅ Nature Cell Biology, подтверждена
- Barandun 2025 (PMID 39764850): ✅ Cell Reports, подтверждена

---

## 🔴 v49 — Platform Versions Unified + Night Vision Standard (2026-07-19)

> Полная синхронизация всех файлов проекта.

### Ключевые изменения:
1. ✅ **Единая система версий:** v1.0 (first grant, no laser) → v1.5 (causality) → v2.0 (laser, glove-box). Старая путаница V1/V2/V3 (эксперимент), V6/V7 (железо), V1-V3/V4+ (софт) устранена.
2. ✅ **Ночное видение — СТАНДАРТ во всех версиях:** v1.0: 1× IR LED 850 nm + Camera NoIR. v2.0: 4× IR LED + 2× Camera NoIR.
3. ✅ **HEPA H13 — в обеих версиях:** v1.0 — штатный инкубатор. v2.0 — glove-box со своим HEPA + UV-C.
4. ✅ **Glove-box v2.0:** габариты 50×50×60 см, перчатки, шлюз 20×20×20 см, полки/ящики для реагентов.
5. ✅ **Бюджет обновлён:** $19,092 → **$19,132** (+$40 за night vision).
6. ✅ **CONCEPT.md:** V1/V2/V3 → Phase 1/2/3 с привязкой к платформенным версиям.

### Файлы, изменённые (17 правок):
- README.md — таблица версий, бюджет, What's inside, night vision
- hardware/README.md — v1.0/v2.0, габариты glove-box, полки/ящики, night vision, HEPA
- software/README.md — единая нумерация, nightvision/ модуль, biosafety/ модуль
- CONCEPT.md — Phase 1/2/3, бюджет +$40
- PARAMETERS.md — v48→v49, Phase 1/2/3, бюджет
- TODO.md — v48→v49, Phase 1/2/3, +night vision install
- STATE.md — v49, таблица версий, 5→7 reviews, core files sync
- _pi.md — v48→v49, night vision, бюджет
- MAP.md — полное перестроение, единая нумерация
- SECURITY.md — v1.0 без лазера / v2.0 с лазером
- firmware/README.md — +night vision, +UV-C, laser → v2.0 only
- CONTRIBUTING.md — убраны лазер и микроманипуляторы
- docs/Alex_update.md — обновлён под v49

---

## 🔴 v46 — Automatic Fixes Applied (2026-07-18)

> Верификация: 6/6 новых PMID ✅

### 5 критических исправлений:
1. ✅ Centrin1-GFP vs Cenexin correlation check — Pilot 1, r≥0.8, fallback Cenexin-mCherry
2. ✅ 60×/1.2 NA WI — PRIMARY objective (центриоли 200-400 nm, 40×/0.95 = 313 nm → не разрешает)
3. ✅ CYTOO micropatterned islands — PRIMARY метод разделения, микропипетка — secondary
4. ✅ 7-дневный тест стабильности — Pilot 0 с GFP beads
5. ✅ Jetson Orin AGX → Orin NX 16GB (экономия $1,500)

### Новые PMID + механизмы:
- **39012627** (Thomas & Meraldi 2024) — Cenexin→Plk1→γ-tubulin→spindle asymmetry. МЕХАНИЗМ.
- **24189274** (Tateishi 2013) — Odf2 domains → distal vs subdistal appendages
- **40167251** (Wang 2025) — HDAC6i → cilium restoration

### Data Quality Control section added.
### Budget: $23,292 max. References: 24.

> Рецензия: `docs/PEER_REVIEW_STRICT_2026-07-18.md` (5.5→8.0/10)
> Верификация: `docs/REVIEW_VERIFICATION_2026-07-18.md`

### 8 исправлений применены:
1. ✅ Alternative Hypotheses (A/B/C) + Reina 2014 (PMID 25047620) + Chatterjee 2018 (PMID 29663194)
2. ✅ PCM1 убран из biological rationale V1
3. ✅ Odf2 KO + HDAC6 inhibitor rescue (отделение эффекта Cenexin от эффекта цилии)
4. ✅ N=200 пар + formal power с cluster adjustment (ρ=0.3)
5. ✅ SNR fallback бюджет (60×/1.2 NA + cooled sCMOS)
6. ✅ Cenexin >1.5 → операциональное определение, непрерывная переменная _M_
7. ✅ Conduit 2010 как альтернативная гипотеза (дочерняя центросома → стволовость)
8. ✅ Пилот микропипетки 20-30 попыток

### Новые PMID:
- 25047620 (Reina & Gonzalez 2014) — causality uncertain
- 29663194 (Chatterjee 2018) — centrosome does NOT regulate fate

### Budget: $17-24K (max с SNR fallback)

> Полное peer review: `docs/PEER_REVIEW_STRICT_2026-07-18.md` (оценка 6.5/10, Major Revision)

### Ключевые изменения:
- **Гипотеза переформулирована:** «natural barcode» → «centrosome maturation state marking» with appendage proteins (Cenexin/Odf2, Ninein, Cep164) and polyglutamylation
- **Эксперимент заменён:** whole-cell ablation → **sister isolation** (micropipette separation + separate microwells)
- **Клеточная стратегия:** 2D NPC monolayer → ПИЛОТ. Если нет асимметрии → RPE1 (94% asymmetry confirmed). 3D органоиды убраны из V1.
- **V2: Odf2 (Cenexin) KO** — ключевой causality эксперимент. Если KO abolishes asymmetry → maturation state IS causal.

### Критические проблемы (из peer review):
1. 🔴 Maturation state не формализован (одна переменная или вектор?)
2. 🔴 RPE1 должна быть ПЕРВОЙ системой, не fallback
3. 🔴 Пилот SNR — обязателен до гранта
4. 🟡 Micropipette success rate неизвестен → micropatterned islands как запасной план
5. 🟡 Autocorrelation lineage не учтён в статистике
6. 🟡 Sham control на mechanical stress отсутствует
7. 🟡 Моторы в инкубаторе — рейтинг не проверен

### Новые PMID добавлены:
- 32371504 (Nayak 2020 — C3G cenexin-dependent)
- 34268309, 24947469, 17078042 (Odf2 knockout papers)
- Sulston & White 1980 (C. elegans lineage, micropipette)

## Decisions

### 2026-07-17: ცომაია (Tsoamaia)'s Epistemological Framing — Dialogical Evolutionary-Abductive Research Machine

> «Мы создаём диалоговую, эволюционно-абдуктивную исследовательскую машину, где один участник выбрасывает семантически плотные, ещё не формализованные кандидаты; второй их широко реконструирует; оба критикуют не только результаты, но и сами operational frame'ы поиска; а выжившие структуры остаются общей сетью и меняют форму следующего поиска.»

**Translation:** We are building a dialogical, evolutionary-abductive research machine. One participant throws out semantically dense, not-yet-formalized candidates; the second broadly reconstructs them; both criticize not only results but the operational frames of the search itself; and the surviving structures remain as a shared network, altering the form of the next search.

**Applied to ARGUS-OS1:** Jaba → concept/intuition. AI/system → literature reconstruction, methodology, peer review simulation. Both → criticize framing ("is this an instrument grant or a causality claim?"). Surviving structures (v38 framework: centriole=barcode, map=deliverable) → baseline for next iteration.

**This is the method.** Not hypothesis-testing. Not engineering. It is dialogical evolutionary abduction — Peircean logic implemented as human-AI collaboration. Reply sent to ცომაია 2026-07-17.

### 2026-07-17: Peer Review Fact-Check — Literature Verification

**Trigger:** Simulated peer review (v34.0) raised 7 concerns. Full fact-check via PubMed.

**Key findings:**
1. Royall et al., 2023 (PMID: 37882444) — **published in eLife**, NOT a preprint. Reviewer's claim of "non-peer-reviewed" is false.
2. Chatterjee et al., 2018 (PMID: 29663194, Cerebellum) — REAL. Centrosome inheritance does NOT regulate fate in cerebellar GNPs. Added to CONCEPT.md with tissue-specificity context.
3. Reviewer cited wrong PMID (29667134 = cancer drug trial). Correct PMID: 29663194.
4. Anderson & Stearns 2009 (PMID: 19682908) — verified. 33/35 pairs, Cenexin asymmetry.
5. Barandun et al., 2025 (PMID: 39764850) — mother → effector (not memory). Ninein-dependent.

**Changes applied:**
- CONCEPT.md v34→35: fixed Royall 2023 status, +Chatterjee 2018, +Cenexin quant threshold (>1.5), +null-result plan
- PARAMETERS.md: Fisher→glmer, N: 50-100→150-200 pairs, power recalculated
- TODO.md: +pre-experiment Cenexin asymmetry check (Go/No-Go), +threshold validation

**Assessment:** Core concerns valid (statistical power, Cenexin quantitation, tissue-specificity). Royall 2023 being eLife STRENGTHENS our position. Chatterjee 2018 ADDED as honest counter-example — makes proposal more credible.

### 2026-07-16: Critical Design Correction — Cell Ablation, Not Centriole Ablation

**Trigger:** User clarification — the experiment ablates the CELL based on centriole identity, not the centriole itself.

**Decision:** Reverted from direct centriole ablation (§0.5 v6.0) to **lineage-specific whole-cell ablation** based on centriole inheritance pattern.

**Rationale:**
1. Between-arms comparison (kill Cell-Old vs. kill Cell-New) controls for "just removed a cell" confound.
2. Whole-cell ablation is technically simpler (2-5 µm targeting vs. 250 nm).
3. Loncarek 2008 concerns about centriole reduplication after ablation are irrelevant — we don't ablate centrioles.
4. Morsch 2017 (PMID: 28190072) already validated 405 nm single-cell killing.

**Experimental arms:**
- Arm A: Ablate cell that inherited OLD centriole → track surviving sister
- Arm B: Ablate cell that inherited NEW centriole → track surviving sister
- Sham: Laser at intercellular space → track both
- H₁: Sister fate differs between Arm A and Arm B → centriole identity of dead cell matters.

**Trigger:** Second simulated expert review — 5 new methodological weaknesses.
**Assessment:** Valid concerns on biomarker selection, ablation validation, optical resolution.

**New fixes applied:**
1. mCherry-α-tubulin → SiR-Tubulin alternative for long-term imaging (>72h). Fluorogenic probe, no genetic modification needed.
2. Ablation death criteria: dual-channel (H2B-GFP nuclear integrity + mCherry-tubulin cytoskeletal collapse) within 15-30 min.
3. CellPose on widefield: added Omnipose as fallback (PMID: 36253643) + RL deconvolution for resolution enhancement.
4. Adaptive imaging: 10 min interphase / 3-5 min during mitosis (chromatin condensation trigger).
5. Centriole resolution: 60×/1.2 NA + RL deconvolution → effective ~200nm. Sufficient for mother/daughter discrimination via Cenexin intensity.
6. Statistical power: N ≥ 100 divisions per cohort (α=0.05, 20% effect size).
7. Contingency plan: `docs/CONTINGENCY_PLAN.md` — laser failure, CellPose tracking loss, contamination.
8. Verified: "CellPose 3.0" does not exist — latest is CellPose 2.0 (PMID: 36344832).

### 2026-07-16: English-Only Rule

**Decision:** CONCEPT.md and all core files must be in English only. Any Russian text → immediate translation.
Added to: `_pi.md`, `~/.pi/agent/AGENTS.md`.

### 2026-07-16: Peer Review #1 — Post-Mortem Analysis

**Trigger:** Simulated expert peer review of CONCEPT.md + PARAMETERS.md.
**Assessment:** High potential, 7 weaknesses, revision required.

**Critical fixes (blocking grants — done by 16 Jul):**
1. Scientific hypothesis missing → added centriolar hypothesis (§0.1, 4 supporting papers).
2. Literature references missing → added 16 verified refs with PMID/DOI (§8).
3. Validation plan missing → new `docs/VALIDATION_PLAN.md` (21 criteria).

**Technical fixes (implemented in CONCEPT v5.0):**
4. Objective heater band (anti-drift).
5. Heated ITO lid (anti-condensation).
6. Autofocus: wavelet FFT → contrast-based (Knapper 2022, PMID: 34625963).
7. Laser calibration: power + duration for BJ-hTERT.

**Methodological fixes:**
8. LLM removed from decision loop (V4-V6). LLM → post-hoc analysis only. Mac M4 Pro → NVIDIA Jetson Orin.
9. Imaging interval: 5 min → 10 min (LFCT standard).
10. 2 TB SSD: recalculate for 3-channel × 10 min × weeks.
11. Mac M4 Pro → Jetson (standard robotics platform).

**Documentation:**
12. Algorithm flowchart, optical path diagram, interlock details.

**Priority for OSC resubmit (~1 Aug):** items 1-3 (hypothesis, references, validation).
Rest — during V1 build.

### 2026-07-15: Renamed → ARGUS-OS1

**Trigger:** Analysis — grant project identity needed in name.
**Decision:** ARGUS-LP → ARGUS-OS1 (Open Science). All core files, AGENTS.md, Marketing updated.

### 2026-07-15: Restart — org, fork, real budgets

**Trigger:** Open Source Collective rejected application. Private repo (`djabbat/CEDAR-Aubrey`), no visible activity.

**Actions:**
1. New public repo: `Georgia-Longevity-Alliance/ARGUS-LP` (GitHub org)
2. Forked `rwb27/openflexure_microscope` as hardware base
3. Budgets recalculated — real numbers with 15% contingency
4. Emphasis: 24/7 autonomous operation, climate control with HEPA + biofilters
5. Full community scaffolding: CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md

**OSC reapplication:** once we have visible activity (commits, issues, stars, a second admin).

### 2026-07-14: OpenFlexure pivot

Upright beats inverted. Water immersion objective from above → gravity holds water. Laser from below through glass dish bottom. OpenFlexure v6.1.5 mechanics for ~$500. Notified Alex.

### 2026-06-27: F partnership

Alex — IT entrepreneur with robotics team. Agreed: he funds + provides engineers, Jaba provides scientific direction. BOM v2.0 (54 line items).

### 2026-06-16: ARGUS-OS1 split from Aubrey

Became standalone grant project under Marketing. Previously embedded in LC/MCARA/Aubrey. Renamed ARGUS-OS1 2026-07-15.
