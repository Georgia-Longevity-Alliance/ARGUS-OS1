# MEMORY — ARGUS-OS1

<!-- lang:ru -->
## 2026-08-01: OSC заявка отправлена ✅, Foresight отправлен ✅

### Foresight ($50,050)
- ✅ Отправлен 31 июля 2026.
- Airtable-форма заполнена, proposal .docx загружен.
- 14 рецензий, 12 ссылок (все проверены), $50,050 / 15 мес.
- Рассмотрение: ~2 месяца (результат — конец сентября).

### OSC — Open Source Collective ($17,000)
- ✅ Заявка на создание Collective отправлена 1 авг (opencollective.com/argus-os1, pending review).
- Fiscal host: Open Source Collective (US 501(c)(6)).
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

**Значение для ARGUS-OS1:**
- PLK4 — ключевой маркер центриольной сборки для детектора
- David Glover (Caltech) — потенциальный advisor
- Центриоль-лизосомальный интерфейс — новый фенотип для скрининга

**✅ 2026-07-29: Письмо David Glover отправлено** — с proposal Foresight. Ждём ответа.

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
> «I had a look and also discussed this with some team members, and I think this will not work out.»
<!-- /lang:ru -->

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
