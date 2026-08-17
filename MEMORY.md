# MEMORY — ARGUS-OS1

<!-- lang:ru -->
## 2026-08-17: V9 спроектирован — руки-роботы + общий LLM-мозг
<!-- /lang:ru -->

<!-- lang:ru -->
- **V9 = апгрейд V7/V8** (не новая платформа): слой автономии для 24/7 обслуживания.
- **V9-HANDS:** 2 тросовые руки (cable-driven) вставляются в glove ports бокса ВМЕСТО рук человека. Вся электроника/моторы СНАРУЖИ → стерильность и UV-C сохранены. 5-6 DOF, NEMA 17 + TMC2209 (общий стек с микроскопом/FOSH), ±0.5 мм, сменные насадки (gripper, пипетка, wipe, UV, капилляр, rake).
- **V9-BRAIN:** внешняя LLM на локальном железе — тот же хост, что управляет FOSH-манипулятором и микророботами. Mac Studio M3 Ultra 192GB / Mixtral-Llama-Qwen. Архитектура: Planner + Tool Bridge (ChemCrow-паттерн) + Safety Layer (Body Law) + Flight Recorder (AIS).
- **V9-TRANSFER (шлюз):** расходники/запчасти стерилизуются ВНЕ бокса (автоклав/UV-C/EtOH/VHP, двойная упаковка) и вносятся через специализированный ящик-шлюз (2 двери, interlock, UV-C 254 нм, HEPA-продувка). Glove ports никогда не открываются — только руки-роботы + шлюз. Внутреннюю дверь открывает рука.
- **Transfer box + стерилизация для V7/V8/V9:** общий документ `docs/STERILIZATION_TRANSFER.md`. V7-TRANSFER (базовый), V8-TRANSFER (+VHP), V9-TRANSFER (полный). Общий комплект аппаратов: автоклав Tuttnauer 2540EKA (~$5K), VHP-генератор (~$4K, для V8/V9), UV-C камера, УЗ-ванна. DIY: автоклав из pressure cooker + PID (~$300), DIY-VHP с монитором остатков (~$400).
- **Версионные SOP (V7/V8/V9, §9 документа):** для каждой версии полный цикл «стерилизация вне бокса → внос через шлюз → вынос отходов». V7: человек в перчатках, базовый шлюз, без VHP. V8: +VHP-деконтаминация бокса, УЗ-ванна (капилляры), sharps, автоклав всех биоотходов (NPCs). V9: внутреннюю дверь открывает РУКА-РОБОТ, оператор — только внешняя дверь + автоклав 1×/сутки.
- **Бюджет:** ~$14K (коммерческие glovebox-руки $30-80K). Стерилизация (общий комплект): ~$12.2K.
- **Дорожная карта:** V9.0 телеоперация → V9.1 полуавтоном → V9.2 автономия 72ч.
- **V9 применим ко ВСЕМ OS:** V9-Lite (OS1, 1 рука опц., LLM на малых моделях Jetson Orin NX + общий хост, ~$3-4K), V9-Standard (OS2, 2 руки, ~$8-9K), V9-Full (OS3, 2 руки + VHP/УЗ, ~$14.4K). Железо рук общее, разница — число рук, шлюз, LLM-хост. Развёртывание: OS1 → OS2 → OS3.
- **Дизайн:** `docs/V9_PROTOTYPE.md` + `docs/STERILIZATION_TRANSFER.md` (2026-08-17). Обновлены VERSIONS.md, README.md, TODO.md.
<!-- /lang:ru -->

<!-- lang:ru -->
## 2026-08-02: 🔴 Находки из autofix — Coscientist + ChemCrow для автоматизации лаборатории
<!-- /lang:ru -->

<!-- lang:ru -->
**Источник:** Циклы autofix статьи «Agentic AI for Scientific Discovery» (журнал IF 18+).
<!-- /lang:ru -->

**Coscientist (Boiko et al., 2023)** — Nature 624, 570-578.
<!-- lang:ru -->
- GPT-4-powered AI agent для autonomous chemical experimentation.
- Ключевые capabilities для ARGUS-OS1:
  - **Documentation Search Module:** автоматически читает и понимает техническую документацию (Opentrons OT-2 API, Emerald Cloud Lab SLL).
  - **Code Generation + Debugging:** пишет Python код для управления оборудованием, автоисправляет ошибки.
  - **Multi-Hardware Integration:** управляет liquid handler + plate reader одновременно (пример: задача «определить цвета в лунках»).
  - **Iterative Experimentation:** autonomously optimises reaction conditions через циклы plan → execute → analyse → refine.
- Архитектура: Planner (GPT-4) + Web Searcher + Documentation Searcher + Code Execution (Docker) + Automation.
- Прямое применение к ARGUS-OS1:
  - Coscientist architecture = шаблон для ARGUS-OS1 control software.
  - Documentation Search → авто-чтение документации OpenFlexure, камер, syringe pumps.
  - Code Execution → авто-генерация и отладка microscopy control scripts.
  - Multi-hardware → координация microscope + pump + incubator.
<!-- /lang:ru -->

**ChemCrow (Bran et al., 2024)** — Nature Machine Intelligence 6, 525-535.
<!-- lang:ru -->
- LLM augmented с chemistry tools (молекулярный докинг, synthesis planning, safety assessment).
- Архитектурный паттерн: LLM + domain-validated external tools → grounding against hallucination.
- Для ARGUS-OS1: microscopy tools (cell detection, tracking, division detection) как external tools для LLM.
<!-- /lang:ru -->

**Self-Driving Laboratories (Burger et al., 2020)** — Nature 583, 237-241.
<!-- lang:ru -->
- Mobile robotic chemist: автономный синтез + характеризация материалов.
- Архитектурный шаблон для ARGUS-OS1 как SDL для longevity microscopy.
<!-- /lang:ru -->

<!-- lang:ru -->
**План действий:**
- Изучить Coscientist architecture (open-source components) для ARGUS-OS1 control stack.
- Интегрировать Documentation Search pattern для авто-конфигурации оборудования.
- ChemCrow pattern: cell segmentation/detection как external tools.
<!-- /lang:ru -->

## 2026-08-01: Autofix Cycle 2 — AIS Integration + Content
<!-- lang:ru -->
- **AIS Passport:** ARGUS-OS1 V6 зарегистрирован в локальном реестре AIS (17 capabilities, 9 запретов).
- **Knowledge Graph:** 32 centriole claims загружены (S-P-O: centriole biology, PCM, elimination, longevity). +160 credits.
- **Marketplace:** 4 listings созданы (Knowledge Pack, Dataset, Consultation, Build Guide).
- **Индексы:** grants/README.md, letters/README.md, hardware/README.md, software/README.md, firmware/README.md.
- **Результат:** ARGUS-OS1 ↔ AIS полностью интегрирован. Knowledge Economy активен.
<!-- /lang:ru -->

<!-- lang:ru -->
## 2026-08-01: Autofix Cycle 1 — Структурная чистка
- **Удалено:** CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md из корня (дубликаты — уже были в docs/).
- **Обогащён:** DESIGN.md — добавлены разделы: AIS Integration, Energy Architecture, Blind Protocol, C. elegans rationale.
- **Обновлён:** MAP.md — добавлены DESIGN.md, THEORY.md, EVIDENCE.md в дерево.
- **Результат:** 11/11 core-файлов в корне, 0 дубликатов, 0 нарушений структуры.
<!-- /lang:ru -->

<!-- lang:ru -->
## 2026-08-01: AIS Global Server — Dedicated server на 10 лет ($18,000)
- **Решение:** Закладываем Dedicated server на 10 лет в бюджет ARGUS-OS1 и общую инфраструктуру.
- **Сумма:** $18,000 (~$150/мес × 120 мес).
- **Зачем:** Глобальная платформа AIS (Autonomous Intelligence Socket) для всех longevity-роботов — ARGUS-OS1, OS2, OS3, и других AIS-based роботов.
- **Компоненты:** AIS Dashboard, Registry, Knowledge Browser, Event Store, Noepedia API.
- **Общий бюджет ARGUS-OS1:** $264,000 → $282,000.
<!-- /lang:ru -->

<!-- lang:ru -->
## 2026-08-01: OSC заявка отправлена ✅, Foresight отправлен ✅
<!-- /lang:ru -->

### Foresight ($75,240)
<!-- lang:ru -->
- ✅ Отправлен 29 июля 2026.
- Airtable-форма заполнена, proposal прикреплён.
- Бюджет: $75,240 / 18 мес. Hub: Berlin.
- ✅ **4 авг 2026 — подтверждение получения.** The Grants Team: «It will be reviewed in the next review cycle. You will hear from us.»
- Рассмотрение: ~2 месяца (результат — конец сентября).
<!-- /lang:ru -->

### OSC — Open Source Collective ($17,000)
<!-- lang:ru -->
- ✅ Заявка на создание Collective отправлена 1 авг (opencollective.com/argus-os1, pending review).
<!-- /lang:ru -->
- Fiscal host: Open Source Collective (US 501(c)(6)).
<!-- lang:ru -->
- Что сделано: создан Collective, заполнено описание, теги, ссылка на GitHub, описание кодовой базы, план проекта.
- Что НЕ прикреплено (в форме не было поля загрузки): proposal (`ARGUS_proposal_OSC.md`) и бюджет ($17,000).
- После одобрения: загрузить proposal + бюджет в дашборде, пройти GitHub Verification.
<!-- /lang:ru -->

<!-- lang:ru -->
## 2026-07-31: Инкубатор — контроль влажности с осушителем
- **Решение:** Активный контроль влажности ±2% RH + dehumidifier.
- **Зачем:** Конденсат на оптике при 95% RH убивает длительные съёмки. Снижение влажности → чистая оптика.
- **Обновлено:** CONCEPT.md, hardware/README.md (v1.0/v2.0), grants/ (бюджет +$400).
<!-- /lang:ru -->

<!-- lang:ru -->
## 📚 2026-07-29: Обзор — TIAM1/центриоли/аутофагия (Coelho, Yu & Glover, Caltech)
<!-- /lang:ru -->

<!-- lang:ru -->
**Статья:** Coelho PA, Yu C, Glover DM. "Functions of TIAM1 at the interface of centriole assembly and autolysosome cycling." bioRxiv 2026-07-03. DOI: `10.64898/2026.07.02.735969`
<!-- /lang:ru -->

<!-- lang:ru -->
**Значение для ARGUS-OS1:**
- PLK4 — ключевой маркер центриольной сборки для детектора
- David Glover (Caltech) — потенциальный advisor
- Центриоль-лизосомальный интерфейс — новый фенотип для скрининга
<!-- /lang:ru -->

<!-- lang:ru -->
**✅ 2026-07-29: Письмо David Glover отправлено** — с proposal Foresight. Ждём ответа.
<!-- /lang:ru -->

---

<!-- lang:ru -->
## 🔴 2026-07-27: Post-Mortem — Susan Mango (Biozentrum Basel) отказ
<!-- /lang:ru -->

<!-- lang:ru -->
**Тип:** Отказ партнёра (visiting researcher / EU-аффилиация).
**Дней до ответа:** 3 (24 июл → 27 июл).
**Причина:** обсудила с командой — «this will not work out».
<!-- /lang:ru -->

<!-- lang:ru -->
### Что сказала
<!-- /lang:ru -->
> «I had a look and also discussed this with some team members, and I think this will not work out.»

<!-- lang:ru -->
### Что мы упустили
1. **Запрос слишком прямой и короткий.** «I need a European affiliation» — это честно, но ставит человека в неловкое положение. Нет предварительных отношений, нет совместной работы.
2. **OCW → ARGUS связь недостаточна.** То, что мы используем OCW как segmentation engine — слабый повод для аффилиации. Нет совместной публикации, нет коллаборации.
3. **Тайминг.** 7 дней до дедлайна Foresight (31 июл) — слишком сжато для такого решения.
4. **GLA как организация.** «Neither a university nor industry» — для Biozentrum это red flag. Они не знают, как классифицировать такое партнёрство.
<!-- /lang:ru -->

<!-- lang:ru -->
### Что изменить
- [ ] EU-аффилиацию искать через реальную научную коллаборацию, а не административный запрос
- [ ] Сначала — совместный preprint/эксперимент, потом — affiliation request
- [ ] Для Foresight: подавать без EU-аффилиации или через UNED Madrid (PhD с осени)
- [ ] Basto и Bettencourt-Dias — письма ещё не отправлены (TODO с 25 июл). **Срочно.**
- [ ] Рассмотреть UNED Madrid как аффилиацию — PhD там уже принят
<!-- /lang:ru -->

<!-- lang:ru -->
### Следующий шаг
1. **Foresight (31 июл):** подавать с GLA + UNED Madrid (двойная аффилиация). David Meyer если согласится — добавить.
2. **Basto + Bettencourt-Dias:** ✅ отправлены 27 июл. Учтён урок Mango — предлагаем коллаборацию, не affiliation.
<!-- /lang:ru -->

---

<!-- lang:ru -->
## 2026-07-24: Susan Mango — Visiting Researcher pitch отправлен 📬
<!-- /lang:ru -->

<!-- lang:ru -->
> Ответ на первое письмо (16:39). Сьюзан попросила CV + proposal.
> Отправлено: письмо + CV (10 PMID + 4 центриольных препринта) + ARGUS proposal (Foresight).
> CV сфокусировано на центриольной биологии — 21 год публикаций, прямая связь OCW→ARGUS.
> Цель: visiting researcher status @ Biozentrum Basel → EU-аффилиация для ERC, EIC, Horizon Europe.
> Письмо короткое (4 абзаца), честный ответ про GLA (не универ, не индустрия), PhD в UNED Madrid с осени.
> Ждём ответа.
<!-- /lang:ru -->

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
