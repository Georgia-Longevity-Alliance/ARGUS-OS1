# STATE — ARGUS-OS1

**Date:** 2026-08-05
**PI affiliation:** Jaba Tqemaladze, MD — **PhD Applicant, UNED Madrid (Programa 9620)** / Georgia Longevity Alliance
<!-- lang:ru -->
**Status:** 🟢 OSC заявка отправлена, Foresight отправлен. UNED добавлен как аффилиация.
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
- **OS2 = V7:** ~$126K — 60×/1.2 WI + sCMOS + microfluidic  
- **OS3 = V8:** +$141K — light-sheet + fs-laser + tweezers  

## 23 Jul: Motor release — breakthrough from WilliamW  
- Sangaboard firmware **already contains** motor release command  
- No need for TMC2209 + MOSFET — just expose via REST API  
- Result: CO₂ incubator heat problem solved in software  
- Task: expose motor_release() in API → PR to OpenFlexure
