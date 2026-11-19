## 🔴 P0 — TRL (добавлено 12 ноя 2026)
- [ ] **FR: выборка ≤100 нм/px, без бининга >2×2** — внести в TRD v0.9c (в протоколе v0.3 уже зафиксировано, в ТРД ещё нет)
- [ ] **Мощность: n ≈ 115 клеток на группу** — внести в протокол до пре-регистрации
- [x] **DOI на бенчмарк readout (Zenodo)** — 10.5281/zenodo.24148459 (12 ноя)
- [x] **Письмо в MIRA** — отправлено 12 ноя 04:26 на support@molecule.xyz; ждём ответ про веса
- [ ] **Прототип fiducial-autofocus + 72-часовой лог дрейфа** — 15 янв 2027 (держит весь календарь)
- [ ] **Скорить ошибку интервала делений в фантоме** — единственная незакрытая метрика бенчмарка

# TODO — ARGUS-OS1

<!-- lang:ru -->
## 🔧 Платформа OFM — из форумной разведки 18 ноя 2026
> Master: `docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`; процедуры — `docs/ARGUS_OS1_Scan_Acceptance_Runbook_2026-11-18.md`; доказательства — `EVIDENCE.md` §«OpenFlexure Forum intel»; инструменты — `software/pipeline/` (7 тестов зелёные).

- [x] ~~**F1 (P0)** — зафиксировать пару «сервер ↔ прошивка»~~ ✅ 18 ноя: **решение — сервер OS v2.11 + скетч Nano из инструкций workaround** (v3.0.0-beta — только после F2 на стенде; связка «v1.0.4 + v3.0.0-beta» в сообществе не подтверждена)
- [x] ~~**F1-документы** — прочитать MR !553, достать прошивку~~ ✅ 18 ноя: настройки AVRDUDESS/avrdude из MR (MR открыт, официальный Nano не проверен), `nano.hex` = **v1.0.4** скачан и сверен (sha256 `dc6066ed…`, версия в ELF), лежит в `firmware/vendor/sangaboard-v1.0.4/` (не в git) с provenance
- [ ] **F1-исполнение (P0, стенд)** — Connect подключается без предупреждения о прошивке + `motor_release()` по REST; при отказе прошить v1.0.4 через AVRDUDESS (`ATmega328P`, пресет Nano, старый бутлоадер; новый — baud 115200); заполнить `hardware/PROVENANCE_V6.md`
- [x] ~~**F2 (P0)** — приёмочный чек-пункт скана~~ ✅ 18 ноя: `software/pipeline/qc.py scan` — декларация vs факт разрешения (грабли 1400↔2800), `capture_mode`, count, overlap, протяжённость в мм, оценка времени; exit 1 = FAIL; тест `test_scan_qc_catches_half_resolution_gotcha`. Осталось прогнать на реальном скане
- [x] ~~**F3 (P1)** — overlap как параметр протокола~~ ✅ 18 ноя (часть 1): регистрация точна при overlap 0.15 / 0.35 / 0.70 (0 px ошибки), фантом 0.15 → 97 % резкости GT. Часть 2 открыта: утвердить 0.15/0.35/0.50 на живом образце с измеренным временем и фотодозой (PMID 28661494)
- [x] ~~**F4 (P1)** — блендинг по рецепту форума~~ ✅ 18 ноя: `software/pipeline/blend.py` (feather НЧ + деталь из самого резкого поля + `libvips dzsave`). Фантом: PSNR **26.81** dB (feather 25.76), резкость **92 %** GT (feather 58 %), швы **0.99** (hard-paste 1.67); дефолты `lf_ratio=0.03`, `detail_power=8` из `sweep.py`. Осталось: прогнать на реальных тайлах V6
- [x] ~~**F5 (P1)** — измерить ROM своего экземпляра~~ ✅ 18 ноя (инструмент): `measure_rom.py` — корреляция кадров траверса (метод PMID 42960477); на синтетике шаг 120 px измерен точно, измерено/скомандовано = **1.0000**, 59/59 связей. Осталось: прогнать на стенде, внести в `PARAMETERS.md`
- [x] ~~**F6 (P2)** — гейт µm/px + цвет перед ML~~ ✅ 18 ноя: `qc.py gate` (38.8 нм/px PASS; 155 нм/px + 4×4 FAIL) и `qc.py colour` (аффинная нормализация по мозаике + provenance JSON). Осталось включить в скрипт скана
- [x] ~~**F8 (P0)** — приёмка A1–A7 одной командой~~ ✅ 18 ноя: `software/pipeline/acceptance.py` (API-проба firmware/motor_release, QC скана, сэмплинг, ROM, швы; exit 0 только при всех PASS; markdown-отчёт для `PROVENANCE_V6.md`), 3 теста на мок-сервере → всего **10 passed**
- [ ] **F7 (P2)** — memory-профиль блендинга: сейчас мозаика целиком в RAM (ok для OS1, пересмотреть для OS2/20k+ тайлов)

## 🧠 P1 — Внутренний цикл агента (idle inference, добавлено 12 ноя 2026)

> Спека: `docs/ARGUS_Internal_Process_Idle_Inference_2026-11-12.md`. Код: `software/argus-agent` (= `~/Desktop/Services/argus-pre`).

- [x] **M1** — `src/ledger/mod.rs` (Question/Cycle, log-odds update, seeded `select_next`, `extract_identifiers`, `gate_failed`) + CLI `think`/`ledger` — ✅ **12 ноя 2026**, 11 тестов, `cargo test --lib` = 57 passed
- [x] **M1b** — засеять леджер 5 реальными открытыми вопросами ARGUS-OS1 — ✅ 12 ноя (`ledger seed`: fiducial-дрейф 72 ч, recall@250 нм/px, Amendment 3, P4 кросс-валидация маркеров, P2/P3 фототоксичность)
- [x] **M2** — `src/verify/mod.rs` (PMID/DOI/arXiv, кэш 30 дней, офлайн, Resolved/NotFound/Unverified) + `src/probe/mod.rs` (epmc/corpus, ladder, фильтр релевантности) + CLI `--probe/--judge/--qid/--offline` — ✅ **12 ноя 2026**, 72 теста; поддельные ID → `Blocked` + гейт ❌ (живой прогон)
- [x] **M3** — `src/budget/mod.rs` (20/час, 200k/сутки) + `think --loop` + суточный отчёт + systemd-таймер (`scripts/install_argus_think_timer.sh`) + ретраи 429 + фильтр релевантности (стем-доля + триграммы, порог 0.20) — ✅ **12 ноя 2026**, 86 тестов
- [x] **M3+** — эксперимент CKA (`argus-cka`): T1 механика p=0.002; T2 qwen×llama p=0.189 (**сходимости нет**, инструмент вырожден) — `docs/EXPERIMENT_CKA_2026-11-12.md`
- [x] **M3++** — `scripts/embed_server.py` + `argus-cka --a emb:<model>`; MiniLM × bge-small, n=60: CKA **0.904** против нуля 0.336 (p=0.002); контроль разных корпусов p=0.122 — ✅ 12 ноя
- [x] **M4-инфра** — `argus-think.timer` (20 мин × 2 цикла) + `argus-report.timer` (09:00, окно 24 ч) + `--hours` — ✅ 12 ноя
- [x] **M4-фиксы соака** — залипание (`consecutive_gaps` → `Gap`), `QKind::Lit/Lab` и маршрутизация канала, `think.lock` — ✅ 12 ноя
- [ ] **M4-данные** — суточная таблица метрик (13 ноя 09:00, автоматически) + 3–5 литературных вопросов с реальными шансами на ответ
- [x] **Выживание сервиса** — `systemd-inhibit --what=idle:sleep`, `Restart=always`, resume + догон пропущенных тиков, переоткрытие `Gap` через 6 ч, reload леджера — ✅ 12 ноя
- [x] **Внимание = ошибка предсказания** — `Question.last_error` (|Δlogit|/3 · 0.35 · 0.1 · 1.0), затухание `exp(−ч/24)`, очередь по ней — ✅ 12 ноя
- [ ] **M5** — LLM-проба (тогда заработает учёт токенов)
- [ ] **M4** — пре-регистрированный 24-часовой тест из Correspondence (7 метрик, публикация результата даже отрицательного) — 2 нед
- [ ] **Решение по §6 спеки** — если `fabricated_identifiers > 0` или `identifier_resolution_rate < 0.7` → цикл в `--dry-run`, запись в STATE.md

## 🔴 URGENT — August 2026
- [x] Foresight Package: `grants/foresight_2026-07-31/SUBMISSION_PACKAGE.md`
- [x] OSC Package: `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md`
- [x] GitHub Activity: 2 weeks (Jul 14–28, 200+ commits) ✅
- [x] Fill Foresight Airtable form — submitted Jul 31 ✅
- [x] OSC application on Collective — submitted Aug 1 ✅
- [ ] GitHub Verification (after OSC approval)
- [ ] Upload proposal + budget to Open Collective dashboard (after approval)
- [x] AIS Passport integration for ARGUS-OS1 ✅
- [x] AIS Knowledge Graph: upload centriole claims ✅ (32 claims)
- [x] AIS Marketplace: create listings ✅ (4 listings)
- [x] Indexes: grants/README.md, letters/README.md, hardware/software/firmware README ✅
<!-- /lang:ru -->

## 🔴 Phase 0: Pilot (Aug–Oct 2026)
- [ ] P1: Stochasticity validation — Dendra2 at all stages (10 embryos) — Owner: PI, Deadline: 2026-09-15
- [ ] P2: Phototoxicity ceiling — max duration, duty cycle (5 embryos) — Owner: PI, Deadline: 2026-09-15
- [ ] P3: Photobleaching assay — SAS-4::GFP decay over 3h — Owner: PI, Deadline: 2026-09-20
- [ ] P4: Marker cross-validation — Centrin1-GFP + SAS-4::mCherry (5 embryos) — Owner: PI, Deadline: 2026-09-30
- [ ] P5: Same-type sister pair quantification (Sulston 1983 map) — Owner: PI, Deadline: 2026-09-30
- [ ] P6: Pedigree feature extraction — 5 metrics, independence from cell type — Owner: PI, Deadline: 2026-09-30
- [ ] P7: Heidenhain haematoxylin validation — anti-SAS-4 co-stain — Owner: PI, Deadline: 2026-10-15

## 🟡 Phase 1: Build (Aug–Sep 2026)
- [ ] Build ARGUS V6 = OS1 (OpenFlexure + 40×/0.75 dry + Jetson Orin NX) — Owner: Alex, Deadline: 2026-09-30
- [ ] Build ARGUS V7 = OS2 (60×/1.2 NA WI + sCMOS + phase contrast) — Owner: Alex, Deadline: 2026-12-31
- [x] **Motor release API** — patch ready: `software/microscope/motor_release_sangaboard.patch` + specification `docs/MOTOR_RELEASE_API.md` (Aug 12) ✅
- [x] **Motor release — email to WilliamW sent** (Aug 12, contact@openflexure.org) 📬 — awaiting response / MR
- [ ] **Flat-field calibration for HQ Camera** — verify Pi HQ Camera (IMX477) support in OpenFlexure/libcamera; if absent — implement flat-field correction (lesson from C270 thread, refs/OpenFlexure_forum_uneven_lighting_C270_2026-08-06.md) — Owner: Alex, Deadline: 2026-09-15
- [ ] Triple transgenic strain: Centrin1-GFP + SAS-4::mCherry + histone::BFP — Owner: PI, Deadline: 2026-09-01

## 🟢 Phase 2: Main Experiment (Oct 2026 – Jan 2027)
- [ ] Main: 100 embryos, record pedigrees + fate — Owner: PI, Deadline: 2027-01-15
- [ ] Analysis: mixed-effects logistic regression + Bayesian hierarchical model — Owner: PI, Deadline: 2027-02-15

## 🔧 Engineering: Axio Observer benchmark → ARGUS (2026-10-19)

> Source: `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. Lessons from the commercial benchmark (Definite Focus 3, Colibri 7, Axio Observer live) for the open platform. All PMIDs verified.

### P0 — Focus-hold (main gap, critical for multi-day)
- [ ] **Fiducial autofocus prototype** on OpenFlexure — accuracy/drift vs stepper-Z — Owner: Alex, Deadline: 2026-11-30 (method: PMID 42274973)
- [ ] Compare with LED optical autofocus (PMID 42525498) and OpenFlexure autofocus (arXiv 2109.06842) — Owner: Alex

### P1 — Illumination and environment
- [ ] **4-channel LED engine** (DAPI/FITC/TRITC/Cy5, TTL-controlled) — replaces single LED — Owner: Alex, Deadline: 2026-12-15 (lesson: Colibri 7)
- [ ] **Incubation module** (stage-top, CO₂/temp/humidity) — OS2 design, modelled on Axio Observer live / IncuCyte — Owner: PI, Deadline: 2027-01-15
- [ ] **Phototoxicity ceiling check** — exposure minimisation in all channels, sensitive cameras (PMID 42393487, 28749075) — Owner: PI

### P2 — Detection and pipeline
- [ ] **sCMOS** into OS2 budget (pco.edge/ORCA class) + **piezo Z** for centriole Z-stacks — Owner: Alex
- [ ] **Micro-Manager + Mastodon** lineage-pipeline integration (PMID 42841415) — Owner: PI
- [ ] SIM/HiLo module as low-cost optical sectioning (Apotome 3 alternative) — Owner: Alex (OS2/OS3)
- [ ] **Tiled region-list acquisition loop + objective pass/fail thresholds** (pattern: Kaneshiro 2022, DOI 10.1017/qpb.2022.24) — register per-cell x,y → re-locate across tiles; avoid session drift — Owner: Alex, Deadline: 2027-01-15

## 🔵 Grants / Outreach
<!-- lang:ru -->
- [x] Foresight proposal final ($50,050) — sent Jul 31 ✅
- [x] OSC application to Collective — sent Aug 1 ✅
- [x] GitHub activity: commits, photos, issue updates — 200+ commits, Jul 14–28 ✅
<!-- /lang:ru -->
- [x] OSC submission package — `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md`
- [x] OSC proposal — `grants/osc_2026-08-01/ARGUS_proposal_OSC.md`
<!-- lang:ru -->
- [ ] GitHub Verification (after OSC approval)
- [ ] Upload proposal + budget to Open Collective dashboard (after approval)
<!-- /lang:ru -->
- [x] Pre-submission inquiry to journal editor — Owner: PI

## ⚪ Backlog
- [ ] ARGUS V8 = OS3 (light-sheet upgrade) — Owner: Alex
- [ ] ARGUS V9 = robot hands through glove ports + shared local LLM brain (24/7 servicing) — design: `docs/V9_PROTOTYPE.md` + `docs/STERILIZATION_TRANSFER.md` — Owner: PI
- [ ] Cross-strain validation (N2 + CB4856) — Owner: PI
- [ ] Cross-species validation — Owner: PI
