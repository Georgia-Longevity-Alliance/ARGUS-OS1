# STATE — ARGUS-OS1

## 12 ноя 2026, 04:30 — DOI и письмо в MIRA закрыты
- 🏷 **DOI выпущен:** 10.5281/zenodo.24148459 — бенчмарк readout, CC-BY-4.0, скрипт + seed + checksum (`zenodo.org/records/24148459`). Токен Zenodo создан через UI (scopes deposit:write + deposit:actions), лежит в `~/.config/zenodo/token` (600).
- ✉️ **Письмо в Molecule отправлено** 04:26 на `support@molecule.xyz` (`250 OK`): вопрос про веса оценки, бенчмарк с DOI, исправление «91 теста» → 29, просьба скорить TRL по элементам. Лог: `MIRA_ARGUS_2026-11/_letters/SENT_LOG_mira_2026-11-12.md`. Адрес не верифицирован (домен принимает любой RCPT) — при bounce `mira@`, затем `hello@`.
- 📄 В комнате 15 файлов: протокол v0.3 (Amendment 2: ≤100 нм/px, n≈115, приёмочный тест), SOP фокус-холда, TRL evidence pack (v3, с DOI).

## 12 ноя 2026, вечер — TRL: доказательная база вместо обещаний
- 📊 **Синтетический бенчмарк readout** (`~/Desktop/MIRA_ARGUS_2026-11/phantom/`): 0.38 px RMSE и recall 0.78 / precision 0.92 при разрешимой выборке; при 250 нм/px recall падает до 0.46 (пары сливаются); при дефокусе 1.9 px — recall 0.30. Seed, checksum, отчёт — воспроизводимо одной командой.
- 📐 **Два следствия для документов:** (1) требование к выборке **≤100 нм/px, без бининга >2×2** — в ТРД его не было; (2) **n ≈ 115 клеток на группу** для разницы 2 ч при α=0.05, мощности 0.8.
- ⚠️ **Исправлена своя же цифра:** «91 unit test» в supplement и плане на 90 дней не подтверждается — в дереве 12 pytest + 17 Rust = **29**. Supplement переиздан (v2), поправка заявлена прямо в тексте; в комнате — `TRL evidence pack` v1.
- 🧾 **Политика доступа переписана v1.0 → v1.1** (v3 в комнате): убрано несуществующее обещание «агент пишет в /agent-output» — роли выдаются на лабораторию, Viewer не пишет вовсе. Добавлен `Publication boundary` (v1): что публично осознанно и почему.
- 👥 В комнате 6 участников: Owner, Aziza (Contributor), Обри и Дэвид (Viewer до 09.02.2027), два агента (Viewer, оба до 09.02.2027).
- 🐞 Инцидент (записан, чтобы не гадать по блокчейну): при переоформлении агента отозвал доступ Азизы, восстановил через 86 с; скрипт приглашений теперь с `--role`, отзыв — только по проверке текста диалога.
- ⏭ **Дальше:** письмо в MIRA (схема весов + переоценка по элементам, черновик `14_LETTER_MIRA_REASSESS_EN.md`), DOI на бенчмарк, прототип fiducial-autofocus (P0, 15 янв), ночной прогон (31 янв).

**Date:** 2026-11-12

## 12 ноя 2026 — ✅ Data Room заполнен, MIRA-супплемент загружен (9 файлов)
- 🎯 **Лаборатория найдена:** `app.molecule.xyz/labs/jaba-tqemaladze`, shortname `jaba-tqemaladze`, oclId `0x0101000000000000000000b396ab329cd27ded26a65566068469ef882f145ec9`, TRL в профиле = `trl-1`.
- ⚠️ **Вход:** под e-mail (djabbat@gmail.com, 0x22cc84…c905c, Admin). Под первым логином лабораторий было 0 — лаборатория создана под другим способом входа.
- ✅ **Загружено 9 файлов (public, v1):** BOM, TRD v0.9b, motor-release патч (текстом — расширение .patch платформа не принимает), протокол пилота, label-free readout, бенчмарк Axio Observer, супплемент MIRA (PDF), план на 90 дней (PDF), agent access policy (PDF). Всего в комнате 12 файлов (плюс VitaDAO proposal, readme-links, assignment agreement).
- 📄 Тексты и скрипты: `~/Desktop/MIRA_ARGUS_2026-11/` (`01`–`06`, `scripts/`, `manifest.json`).
- 🔑 **API:** credential `argus-os1-agent` выпущен 12 ноя (до 10 фев 2027), лежит в `~/.config/argus-labs/credentials.env` (600). Чтение работает: `scripts/labs.sh labs|files`.
- 🐞 **Найдено в доках Molecule:** прод-endpoint в документации указан как `prod.graphql.api.molecule.xyz` — такого хоста нет; реальный `production.graphql.api.molecule.xyz`. Плюс типы в примерах `str!`, а в схеме `String!`; поле ошибки — `error`, не `err`.
- ⏳ **Осталось:** service token (нужна подпись кошельком: `labs.sh signin` → personal_sign → `labs.sh token 0x…`), затем шесть полей формы из `02_FORM_ANSWERS_EN.md` и вопрос про веса 3/3/2 vs 2.75.
- 👥 **В команде:** contributor `azizaaubakirova74@gmail.com` (0xb32ff…fb74a), permanent.

**Предыдущая запись:** 2026-11-10
**PI affiliation:** Jaba Tqemaladze, MD — **PhD Applicant, UNED Madrid (Programa 9620)** / Georgia Longevity Alliance
<!-- lang:ru -->
**Status:** 🟢 OSC заявка отправлена, Foresight отправлен. Ответ Алексею по сборке отправлен 12 авг. ✅ **V1 build + OSC resubmit — ЗАКРЫТО (16 авг, подтверждено Джабой)**. Вопрос закрыт, ARGUS-OS1 в режиме ожидания ответа OSC.

<!-- lang:ru -->
## 10 ноя 2026 — 🔴 Sovereign Tech Fund — отказ (ARGUS-OS1 AI core, `argus-pre`)
- ❌ **STF — ОТКАЗ (письмо 10 ноя 2026, ID `YelaLvMK`):** «the proposal does not meet our criteria for investment», без фидбэка (стандартно для STF).
- 📄 Постмортем + журнал: `~/Desktop/Services/grants/GLA/SovereignTechFund/STF_REJECTION_2026-11-10.md`.
- 🎯 **Причины:** (1) ключевой критерий STF — «vital to development of OTHER software»; у молодого `argus-pre` нет зависимых проектов/adoption → отсечка prevalence; (2) черновик заявки остался на €52.5K/1,800ч/4WS, а поданная форма была €90K/2,800ч/5WS — несогласованность, урок на будущее; (3) риск overlap с OSC $17K.
- 📌 **Урок:** STF финансирует зрелые базовые технологии, не новые проекты. Переподача — не раньше Q4 2027, только после adoption-фазы (crates.io + реальные интеграторы + case studies).
- 📌 **Не влияет на главное:** Foresight RFP $100K, EIC €3.98M, NLnet €23K, CIRCBIO €2.5M, FUTO, VitaDAO, OSC — в игре.
<!-- /lang:ru -->

<!-- lang:ru -->
## 19 окт 2026 — 🔬 Axio Observer benchmark → инженерный аудит платформы 📄
<!-- /lang:ru -->

<!-- lang:ru -->
- 📄 **Полный разбор эталона Zeiss Axio Observer 7 + live-бандл** (Definite Focus 3, Colibri 7, инкубация, sCMOS, ZEN) + конкуренты (Nikon PFS, Olympus TruFocus, Leica AFC, IncuCyte) + открытые аналоги (OpenFlexure, fiducial autofocus).
- 🎯 **Анализ + мета-анализ:** `docs/AXIO_OBSERVER_ENGINEERING_ANALYSIS_2026-10-19.md`. EVIDENCE.md пополнен инженерным разделом; TODO.md — задачи P0–P2; PARAMETERS.md — таблица параметров платформы.
- 🎯 **Главный разрыв OS1 — аппаратное удержание фокуса** → P0: прототип fiducial autofocus (PMID 42274973) на OpenFlexure.
- 🎯 **Разрывы #2–4:** мультиканальный LED (фототоксичность), инкубация/среда (multi-day), piezo Z + sCMOS (центриольные стеки). Все закрываются открытыми решениями.
- 🎯 **V9-руки дают ARGUS то, чего нет у эталона** (автономная смена образцов) — аргумент для грантов.
<!-- /lang:ru -->

<!-- lang:ru -->
## 3 окт 2026 — 🔴 Foresight AI Node program — отказ
- ❌ **Foresight AI Node program — НЕ ВЫБРАН (письмо 3 окт 2026):** «your project was not selected this round», индивидуальной обратной связи не дают.
- ⚠️ Это **отдельная программа** от гранта Foresight Fellowship ($50,050, подан 31 июл) — грант всё ещё pending (подтверждение получения 4 авг).
- ✅ OSC ($17K) — всё ещё pending на Open Collective.
- 📌 Приоритет: ждать OSC; по гранту Foresight — follow-up (~6–8 нед цикл уже прошёл, ~12–26 сен).
<!-- /lang:ru -->

<!-- lang:ru -->
## 15 сен — анализ Aletheia + AISocket → ARGUS 📄
- ✅ Прочитаны новые README: Aletheia README + AISocket (переписан).
- 📄 Анализ и предложения: `docs/ALETHEIA_AISOCKET_ARGUS_ANALYSIS.md`.
- 🎯 **P0:** обновить README DAIS под новую грамматику (CLAIM/EVIDENCE/REPLICATION/OPEN/COVERAGE) + сверить статусы «Ready».
  - ✅ **Реализовано 15 сен (локально, Marketing/DAIS, коммит `3ed0bd6`)**: Aletheia grammar в Rust (`core/src/aletheia.rs`, 91 тест ✅), Python-клиент расширен, web-миграция (replication/coverage/valid_in), README/CONCEPT/THEORY выровнены, Body Law → 6 слоёв.
  - ⚠️ **Не запушено**: gla/main — тонкий ребренд (73 файла, daisocket-нейминг) без полной реализации; локальная полная реализация (118 файлов, aisocket-нейминг). Субмодуль указывает на тонкую gla/main. Ждём решения по слиянию линий (варианты A/B/C в анализе, §5.1).
- 🎯 **P1:** coverage-гейт в V9-BRAIN (Green-поиск трасс до Red-LLM); Trace→Aletheia консолидация.
- 🎯 **P2:** MVP knowledge field «центриольная биология» (P0–P8 как CLAIM/EVIDENCE) + COVERAGE-таблица в «Asymmetric Divisions».
<!-- /lang:ru -->

<!-- lang:ru -->
## 12 авг — Motor Release API ✅
- ✅ Исследование апстрима: прошивка `release` (julianstirling/sangaboard-firmware) + pysangaboard `release_motors()` — уже существуют.
- ✅ Патч для openflexure-microscope-server: `software/microscope/motor_release_sangaboard.patch` (новый action `release_motors` → `POST /sangaboardthing/release_motors`).
- ✅ Тесты: 5/5 проходят. Thing Description подтверждает endpoint.
- 📄 Спецификация: `docs/MOTOR_RELEASE_API.md`.
- 📬 Письмо WilliamW с патчем **ОТПРАВЛЕНО** (12 авг, через contact@openflexure.org) — ждём ответа.

## 12 авг — письмо Алексею 📬
- 📬 Ответ Алексею (Filippov) отправлен: статус заказа (камера получена, адаптер в пути), вопрос по готовности лаборатории, виза в Кёльн, следующие конференции.
- 📄 Письмо: `letters/email_alex_2026-08-12.md`
<!-- /lang:ru -->

<!-- lang:ru -->
## 1 авг — OSC заявка отправлена ✅
- ✅ **OSC ($17K):** Заявка на Open Source Collective отправлена. Collective: opencollective.com/argus-os1 (pending review).
- ✅ **Foresight ($50,050):** Отправлен 31 июля.
<!-- /lang:ru -->

<!-- lang:ru -->
## 29 июл — письма 📬
- 📬 David Glover (Caltech) — предложение коллаборации по ARGUS-OS1 (centriole tracking, TIAM1)
<!-- /lang:ru -->

<!-- lang:ru -->
## 27 июл — Susan Mango отказ 🔴
<!-- /lang:ru -->

<!-- lang:ru -->
- 🔴 Susan Mango (Biozentrum Basel): обсудила с командой, отказ. Причина: «this will not work out.»
- Post-mortem записан в MEMORY.md.
- Урок: не просить affiliation без предварительной коллаборации.
- Foresight (31 июл): подавать с GLA + UNED Madrid. Без EU-аффилиации пока.
<!-- /lang:ru -->

### Foresight grant
<!-- lang:ru -->
- ✅ **ОТПРАВЛЕН 31 июля 2026** — Airtable-форма + proposal .docx
<!-- /lang:ru -->
- ✅ Proposal: `ARGUS_proposal_Foresight.md` + `.docx`
<!-- lang:ru -->
- ✅ 14 рецензий, 12 ссылок (все проверены), $50,050 / 15 мес
- ✅ **ОТПРАВЛЕН 31 июля**
<!-- /lang:ru -->

<!-- lang:ru -->
### Отправлено
- 📬 David Glover (Caltech) — предложение коллаборации (29 июл)
- 🔴 David Meyer — ждём ответа (отправлено 28 июл)
- ❌ Susan Mango — отказ (27 июл)
- 📬 Basto (Institut Curie) + Bettencourt-Dias (IGC) — коллаборация (27 июл)
- 📬 Илья + Akaki
<!-- /lang:ru -->

<!-- lang:ru -->
### 🔴 СРОЧНО — OSC (1 авг)
- [x] Заявка на Open Source Collective отправлена ✅
- [ ] GitHub Verification (после одобрения OSC)
- [x] OSC Submission Package создан: `grants/osc_2026-08-01/`
<!-- /lang:ru -->
- [x] OSC Proposal: `grants/osc_2026-08-01/ARGUS_proposal_OSC.md`

<!-- lang:ru -->
## 🆕 28 июл — Пакеты для обеих заявок созданы
- ✅ Foresight: `grants/foresight_2026-07-31/SUBMISSION_PACKAGE.md` — анализ условий, Airtable-инструкция, proposal $50,050
- ✅ OSC: `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md` — условия fiscal hosting, GitHub Verification, бюджет $17K
- ✅ GitHub-активность: условие «2 недели» выполнено (14–28 июл, 200+ коммитов)
- 🔴 Foresight (31 июл): Airtable-форма, proposal .docx
- 🟡 OSC (1 авг): GitHub Verification → открыть страницу на opencollective.com  
<!-- /lang:ru -->

<!-- lang:ru -->
## 🔧 28 июл — Прогресс по железу
- ✅ Модуль камеры получен — камера подключается к компьютеру
- 🔄 Адаптер для установки на микроскоп — в пути, ожидается на днях
- ⏳ Следующий шаг: установить камеру на микроскоп через адаптер → тестовый прогон
<!-- /lang:ru -->

## OS Stages  
- **V0:** ~$930 — bare OpenFlexure mechanics, no AI  
- **OS1 = V6:** ~$3-5K — local AI (Jetson Orin NX, CellPose + tracking + lineage)  
- **OS2 = V7:** ~$70K HW / ~$307K full (60×/1.2 WI + sCMOS + microfluidic)  
- **OS3 = V8:** +$141K — light-sheet + fs-laser + tweezers  

## 23 Jul: Motor release — breakthrough from WilliamW  
- Sangaboard firmware **already contains** motor release command  
- No need for TMC2209 + MOSFET — just expose via REST API  
- Result: CO₂ incubator heat problem solved in software  
- Task: expose motor_release() in API → PR to OpenFlexure
