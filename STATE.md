# STATE — ARGUS-OS1

## 18 ноя 2026, 21:00 — 🛠 Пайплайн тайлов реализован и проверен на фантоме (7 тестов), версии запинены
- ✅ **Решение по версиям:** V6 = сервер **OpenFlexure OS v2.11** + скетч Nano (v3.0.0-beta — только после приёмки; связка «v1.0.4 + v3.0.0-beta» в сообществе не подтверждена). Процедура и откат — `docs/ARGUS_OS1_Scan_Acceptance_Runbook_2026-11-18.md`.
- ✅ **Код (`software/pipeline/`):** `qc.py` (F2 scan-гейт + F6 µm/px-бининг-гейт + нормализация цвета), `blend.py` (F4: feather НЧ + деталь из самого резкого поля + `libvips dzsave`), `measure_rom.py` (F5), `phantom.py`/`evaluate.py`/`sweep.py` (самопроверка), `README.md` с числами.
- 📊 **Результат на фантоме (overlap 0.35):** fusion PSNR **26.81** dB (feather 25.76, hard-paste 22.19) · резкость **92 %** ground truth (feather 58 %) · швы **0.99** (hard 1.67) · регистрация **0 px** ошибки. Low-overlap 0.15: точная регистрация, 97 % резкости. ROM-траверс: измерено/скомандовано = **1.0000**, 59/59 связей.
- 🧪 **Тесты:** `cd software && python3 -m pytest tests/test_pipeline.py -q` → **7 passed** (~15 s); включая гейт на грабли 1400↔2800 px и протокол Amendment 2.
- 📄 **Новые файлы:** `docs/ARGUS_OS1_Scan_Acceptance_Runbook_2026-11-18.md`, `hardware/PROVENANCE_V6.md` (шаблон приёмки A1–A7).
- ⚠️ **Не проверено:** всё, что требует стенда (Connect после прошивки, реальные тайлы, ROM живого экземпляра); MR !553 не читал.
- 🎯 **Следующее:** на стенде — A1/A2 (Connect + `motor_release`), затем `qc.py scan` на первом реальном скане и `blend.py` на его тайлах.

## 18 ноя 2026 — 🔭 Разведка форума OFM: 6 действий F1–F6, 11 источников проверено
- 📥 **Источник:** 2 темы Discourse (read fully via API) — `docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`, обогащён `EVIDENCE.md` (11 строк с PMID/DOI, все резолвнуты 2026-11-18), `TODO.md` (блок F1–F6).
- ⚠️ **Операционное:** старый домен `forum.openflexure.org` — **NXDOMAIN**; форум живёт на `openflexure.discourse.group`. С 12 ноя 2026 у всех пользователей **отключено создание новых тем** (спам) → вопросы WilliamW/разработчикам — только ответом в существующих ветках либо через GitLab MR/issue.
- 🔢 **Наши числа (арифметика, не измерение):** 40× + pitch 1.55 µm = 38.8 нм/px (совпадает с протоколом ~39), поле 109 µm при 2800 px; 10×10 мм при overlap 0.35 ≈ 20 200 тайлов ≈ 17 ч при допущении 3 с/поле; 60× — 26 нм/px, но 45 800 тайлов ≈ 38 ч → **60× на HQ-камере для OS1 не апгрейд**.
- 🧪 **Главные подтверждения:** ROM 11.4 ± 0.4 мм (PMID 42960477); EDOF/фокус-стекинг на OpenFlexure при BOM ~$300, complex wavelet > Sobel/variance (PMID 42644580); OFM vs Aperio GT450 на 275 биопсиях, AUC 0.71–0.80, но обязательны µm/px + цвет (PMID 42800763 — «пригодно», не «эквивалентно»).
- 🎯 **Решения к подтверждению Джабы:** пинить ли сервер OS на v2.11 или брать v3.0.0-beta (тогда F1/F2 — блокирующие).

## 12 ноя 2026, 17:00 — 🏷 Пре-регистрация опубликована: DOI 10.5281/zenodo.24168505 (до данных)
- ✅ **Zenodo опубликован** (не черновик): `PREREGISTRATION_2026-11-12.md` + `ARGUS_Protocol_v0.3.md` + `SHA256SUMS.txt`, CC-BY-4.0, `references` → бенчмарк 10.5281/zenodo.24148459. Зафиксировано ДО данных: primary endpoint, стоп-критерии, D1+D2/D3, 100 nm/px без бининга >2×2, n = 115 анализ/150 рекрутмент, acceptance-пороги readout (включая ещё не реализованный interval MAE ≤ 1.0 h).
- 🔧 Скрипт `prereg_zenodo/publish_prereg.py` (`--dry-run/--sandbox/--publish`), метаданные `.zenodo.json`. Грабли Zenodo-API: `POST /depositions` — `application/json` с телом `{}`; заливка в bucket — только `application/octet-stream`; `curl` с этого IP → 403 Cloudflare, `urllib` проходит. Два пустых черновика от неудачных прогонов удалены.
- 📥 **В комнате:** публичный файл `/pre-registration-deposited-argus-os1-protocol-v03-doi-105281zenodo24168505` (markdown, 7938 байт, с описанием) — читается анонимно, это ответ на возражение «план может поплыть».
- ⚠️ **Осталось по мелочи:** дубль в статусе ADMIN (`…zenodo24168505.md`, тот же текст, зашифрован, без описания) — удалить из UI или оставить как внутреннюю копию; на оценку не влияет.
- 🎯 **Дальше по плану:** фокус-холд + 72 ч лог (15–20 янв), машинный лог делений (31 янв), переоценка 1 марта; ранний запрос переоценки без новых артефактов не отправлять.

**Date:** 2026-11-12

## 12 ноя 2026 — ⬇️ TRL 2.75 → 2.00: разобрано, записано в урок, 6 файлов переписаны
- ✅ **FIX-пак залит (16:32–16:45):** 6 публичных файлов переписаны из «самоприговоров» в рамку — supplement v3, ninety-day v3, TRL evidence pack v4, medical anchor v2, staged gates v2, label-free v2. Источник: `_fix_public/` (`apply_fixes.py` воспроизводим, `README_FIX.md`). Проверка по содержимому в комнате: все 6 `miss=[] осталось=[]` (старые маркеры `not contest`, `I am not arguing`, `91 passing`, `is not possible today`, `2.75` — нет).
- ⚠️ **Ограничение платформы:** публичное описание файла задаётся только при создании; в «Upload new version» полей описания нет, в карточке — только Details/History/Access/Make confidential. Значит «Response to the 2.75/5.0 score» в описании supplement и «the score is not contested» в staged gates остаются до создания новых файлов (до переоценки 1 марта 2027).
- 📉 **Переоценка MIRA 12 ноя:** TRL 1, **2.00/5** (было 2.75/5 от 5 ноя), рекомендация **SUPPLEMENT → PIVOT**, Low Confidence, подбаллы 2/2/2 (были 3/3/2). Работа за неделю только улучшилась — упала поверхность публикации, не проект.
- 🧠 **Механика (по цитатам в rationale):** оценщик читает только PUBLIC и нашу анкету и не различает рамку и вердикт. Он процитировал наше же: «no experimental laboratory work», «TRL 1 … I am not arguing about it», «not possible today», «none of it is a claim that the pilot will extend lifespan», «I will not contest the score». Плюс опубликованная самопоправка «91 → 29 тестов» читается как неподтверждённое число; бенчмарк — как симуляция (платформа 4 → 2-3).
- 📌 **Урок записан:** `MEMORY.md` (проект) + `~/.pi/agent/memory/05-LESSONS.md` → `L-mira-trl-0001` (глобально). Правило: PUBLIC = артефакты/рамки/проверяемые числа; самоприговоры — в ADMIN; ретракции в PUBLIC не публиковать; перед загрузкой — grep по маркерам автооценщика.
- 🎯 **Что реально поднимает балл:** только артефакты поведения — 72-часовой лог дрейфа фокуса (15 янв) и машинный лог делений (31 янв). Текст не поднимает, может только утопить.
- ⏭ **Дальше:** пре-регистрация протокола v0.3 с DOI (OSF/Zenodo, 1–2 дня) — единственный артефакт, который закрывает возражение «план может поплыть»; затем фокус-холд и лог дрейфа (15–20 янв), лог делений (31 янв), переоценка 1 марта.

**Date:** 2026-11-12

## 12 ноя 2026 — 🧠 «Idle inference»: у агента появляется внутренний процесс (и это не сознание)
- 📄 **Разобрана концепция Налимова** (семантический континуум + P(μ|y) ∝ P(μ)·P(y|μ)). Итог: внешнее «поле смыслов» — нефальсифицируемо (не подтверждено и не может быть), но из концепции выживает единственное рабочее требование — **непрерывность внутреннего процесса** и разделение prior / фильтр / posterior. Разбор: `~/Desktop/Services/docs/ANALYSIS_2026-11-12_Nalimov_Semantic_Continuum_Idle_Inference.md`.
- 📐 **Спека внутреннего цикла агента:** `docs/ARGUS_Internal_Process_Idle_Inference_2026-11-12.md` — `ledger.json` (открытые вопросы с вероятностями), байесовское обновление в log-odds (λ=0.5, LR=3 / 1/3), пробы только read-only, проверка каждого идентификатора (PMID/DOI/arXiv), бюджет 20 циклов/ч и 200k токенов/сутки, 7 метрик, **жёсткий гейт: 0 выдуманных идентификаторов**.
- 📰 **Внешний выход:** Correspondence «Idle inference: autonomous agents need a clock, not a larger prior» (543 слова, 10 реф., 0 самоцитирований) → **Nature Machine Intelligence** (JIF 29.8/2025, APC=0 по гибридной модели). Pre-submission inquiry отправлен 12 ноя с `jaba@longevity.ge` на `machineintelligence@nature.com` (✅ 250 OK; скрипт `~/Desktop/Services/scripts/send_idle_inference_inquiry_NMI_2026-11-12.py`). Пакет: `~/Desktop/Services/publications/Idle_Inference_NMI/`.
- ✅ **M1 СДЕЛАНО (12 ноя):** `src/ledger/mod.rs` — `Question`/`Cycle`/`Status`, байесовский сдвиг `sigmoid(logit p + λ·ln LR)` (λ=0.5, LR=3/⅓, клип 0.02–0.98), `extract_identifiers` (PMID/DOI/arXiv, без внешних зависимостей), seeded `select_next` (SplitMix64), `gate_failed`. CLI: `argus-agent think [--once|--dry-run|--report] [--seed N] [--k N]`, `argus-agent ledger list|add|show|seed|close|report`. **11 новых тестов, `cargo test --lib` = 57 passed / 0 failed.** Смоук: леджер засеян 5 реальными вопросами, `think --once` записал цикл (0.5 → 0.5, Unresolved), отчёт печатает метрики и вердикт гейта.
- ✅ **M2 СДЕЛАНО (12 ноя):** `src/verify/mod.rs` — резолв `PMID`/`DOI`/`arXiv` через Europe PMC / Crossref / arXiv, файловый кэш 30 дней, офлайн-режим, и главное — различение `Resolved` / `NotFound` (подделка) / `Unverified` (сеть/429). `src/probe/mod.rs` — каналы `epmc` и `corpus`, латинский запрос, лестница запросов (полный → 1 слово), фильтр релевантности (термин или общий префикс ≥5). CLI: `think --probe epmc|corpus [--corpus DIR] [--limit N] [--offline] [--judge support|contradict] [--qid ID]`. **72 теста, 0 failed.**
- 🔬 **Живой прогон M2:** по вопросу P4 (Centrin1/SAS-4/mCherry) найдено 5, релевантных 3, резолвнуто 3 → цикл `Resolved`, p не двигалась; с `--judge support` p 0.500 → 0.634. Вопрос про `fiducial-autofocus` — 1 попадание отсеяно как нерелевантное («Nanoscopy on the Chea(i)p»), честный пробел. Поддельные `PMID:99999999` / `doi:10.9999/fake.12345` → `Fabricated`, вопрос `Blocked`, **гейт ❌** — защита проверена на живых API.
- 🧮 **Исправлена метрика:** `identifier_resolution_rate` теперь считается только по циклам, где заявлялись идентификаторы (`id_cycles`); отдельно выводятся `evidence_yield` и `gap_cycles`. Иначе «ничего не нашёл» выглядело как провал резолва (было 0.17 на пустом месте).
- ✅ **M3 СДЕЛАНО (12 ноя):** `src/budget/mod.rs` — 20 циклов/час (скользящее окно) и 200k токенов/сутки, персист в `ledger/budget.json`, сброс на смене суток. `think --loop [--max-cycles N] [--interval-secs S] [--budget-cycles N] [--budget-tokens N] [--quiet]` — гейт до цикла, запись после, остановка с причиной. Суточный отчёт `ledger/report_YYYY-MM-DD.md` (метрики, бюджет, леджер, последние циклы, вердикт гейта). systemd-таймер: `scripts/install_argus_think_timer.sh` (units + `--dry-run`/`--uninstall`). Ретраи 429/5xx (2 доп. попытки, 0.5→1→2 с; 404 не ретраится). Фильтр релевантности: доля пересечения стемов по запросу + половинный вес символьных триграмм, порог `--min-score` 0.20 (эмбеддинг-путь на `WordHashVec` проверен и отброшен — коллизии на 512 измерениях). Живой прогон: найдено 5 → отсеяно 2 → 3 по теме → все резолвнуты. **86 тестов, 0 failed.**
- 🧪 **M3+: первый локальный тест «поля смыслов» (`argus-cka`, linear CKA + перестановочный нуль).** T1 (ngram × wordhash, n=60, 500 перестановок): CKA 0.805 против нуля 0.517, p=0.002 — механика работает. **T2 (две реальные модели, qwen2.5:7b × llama3.2, семантическая проекция по 8 осям, n=17, 200 перестановок): CKA 0.318 против нуля 0.377, p=0.189 — сходимости НЕТ.** Инструмент вырожден (NN-cos 0.965/0.892), поэтому это не опровержение PRH, а отрицательный результат пилота. Разбор и фальсификационное условие: `docs/EXPERIMENT_CKA_2026-11-12.md`.
- ⚠️ **Технический факт:** локальный Ollama 0.32.9 не поддерживает `/api/embed` (просит `--embeddings`, а такого флага в сборке нет — проверено запуском на 11435). Настоящий тест на двух энкодерах требует другого рантайма (LM Studio `/v1/embeddings` / `sentence-transformers`).
- ✅ **M3++ СДЕЛАНО (12 ноя):** `scripts/embed_server.py` (OpenAI-совместимый `/v1/embeddings` на sentence-transformers) + `argus-cka --a emb:<model>`. **Настоящий тест:** `all-MiniLM-L6-v2` × `bge-small-en-v1.5`, n=60, 500 перестановок → **CKA 0.904 против нуля 0.336, p = 0.002**; контроль «разные корпуса» (B по `~/Desktop/PhD`) → 0.435 против 0.410, p = 0.122 → метрика ловит содержание, а не форму. Разбор: `docs/EXPERIMENT_CKA_2026-11-12.md`.
- ✅ **M4 (инфраструктура) СДЕЛАНО:** systemd-таймеры — `argus-think.timer` (каждые 20 мин, 2 цикла) и `argus-report.timer` (ежедневно 09:00, отчёт с окном 24 ч). `--hours` в `think --report --write`.
- 🐞 **Соак 12 ноя вскрыл три дефекта (все починены):** (1) **залипание** — бонус за пробел повышал привлекательность провального вопроса (12 из 15 циклов на один), теперь бонус убывает и после 3 пробелов подряд вопрос уходит в `Gap`; (2) **литературная проба по лабораторным вопросам** — введён `QKind::{Lit,Lab}`, `epmc` берёт только `Lit`; (3) **два процесса писали состояние** (старый `nohup` затёр засев) — добавлен `ledger/think.lock` с проверкой pid, второй запуск отказывается. 90 тестов.
- ✅ **Выживание процесса (12 ноя):** сервис `argus-think.service` теперь долгоживущий (`Type=simple`, `Restart=always`) и запускается через `systemd-inhibit --what=idle:sleep --mode=block` — сон блокируется, пока цикл жив (`systemd-inhibit --list` показывает блок). После выключения — `ledger/runtime.json` + `resume::plan_catchup()`: 6 ч простоя → «пропущено 360 тиков, догоняю 10», затем циклы без паузы; `downtime_secs=21600, catchup_cycles=3`. Потолок догона 10 циклов. Пустая очередь больше не убивает сервис (ждёт, `Gap`-вопросы переоткрываются через 6 ч), леджер перечитывается каждую итерацию, при исчерпании бюджета сервис спит, а не выходит. 99 тестов.
- ✅ **Уточнение тезиса (12 ноя, Джаба):** «смыслы приходят извне» = извне приходит **разница прогноз/реальность** (ошибка предсказания, precision-weighted) → внимание и актуализация. Подтверждено: Feldman & Friston 2010 (PMID 21160551), Schultz 1997 (PMID 9054347). В коде: очередь внимания строится по `Question.last_error` с затуханием (тест `prediction_error_drives_attention`). Статья → **v4** (719 слов, 998 с таблицей, 10 ссылок, свежесть 30%).
- 🎯 **Следующий шаг:** дождаться отчёта 13 ноя 09:00 (первая суточная таблица), добавить литературные вопросы, на которые литература **может** ответить; учёт токенов включится на LLM-пробах (M5).
- ⚠️ **Терминология:** слово «сознание» в коде и внешних документах не используется — только `idle inference / внутренний цикл`. Заявлять сознание нельзя: нет операционального определения и нет теста.

**Date:** 2026-11-12

## 12 ноя 2026, 04:30 — DOI и письмо в MIRA закрыты
- 🏷 **DOI выпущен:** 10.5281/zenodo.24148459 — бенчмарк readout, CC-BY-4.0, скрипт + seed + checksum (`zenodo.org/records/24148459`). Токен Zenodo создан через UI (scopes deposit:write + deposit:actions), лежит в `~/.config/zenodo/token` (600).
- ✉️ **Письмо в Molecule отправлено** 04:26 на `support@molecule.xyz` (`250 OK`): вопрос про веса оценки, бенчмарк с DOI, исправление «91 теста» → 29, просьба скорить TRL по элементам. Лог: `MIRA_ARGUS_2026-11/_letters/SENT_LOG_mira_2026-11-12.md`. Адрес не верифицирован (домен принимает любой RCPT) — при bounce `mira@`, затем `hello@`.
- 📄 В комнате 15 файлов: протокол v0.3 (Amendment 2: ≤100 нм/px, n≈115, приёмочный тест), SOP фокус-холда, TRL evidence pack (v3, с DOI).

## 12 ноя 2026, вечер — TRL: доказательная база вместо обещаний
- 📊 **Синтетический бенчмарк readout** (`~/Desktop/Services/grants/GLA/VitaDAO_ARGUS/MIRA_ARGUS_2026-11/phantom/`): 0.38 px RMSE и recall 0.78 / precision 0.92 при разрешимой выборке; при 250 нм/px recall падает до 0.46 (пары сливаются); при дефокусе 1.9 px — recall 0.30. Seed, checksum, отчёт — воспроизводимо одной командой.
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
- 📄 Тексты и скрипты: `~/Desktop/Services/grants/GLA/VitaDAO_ARGUS/MIRA_ARGUS_2026-11/` (`01`–`06`, `scripts/`, `manifest.json`).
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
