# STATE — ARGUS-OS1

**Date:** 2026-07-28
<!-- lang:ru -->
**Status:** 🟢 Пакеты Foresight + OSC готовы. Дедлайны: 31 июл (Foresight, $50K) + 1 авг (OSC, $17K).
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
- ✅ Proposal: `ARGUS_proposal_Foresight.md` + `.docx`
<!-- lang:ru -->
- ✅ 14 рецензий, 12 ссылок (все проверены), $50,050 / 15 мес
- 🔴 Дедлайн: **31 июля** — 4 дня
<!-- /lang:ru -->

<!-- lang:ru -->
### Отправлено
- 📬 David Meyer — follow-up отправлен 28 июл. 🔴 Ждём ответа завтра (29 июл).
- ❌ Susan Mango — отказ (27 июл)
- 📬 Basto (Institut Curie) + Bettencourt-Dias (IGC) — коллаборация (27 июл)
- 📬 Илья + Akaki
<!-- /lang:ru -->

<!-- lang:ru -->
### 🔴 СРОЧНО — Foresight + OSC
- [x] Basto (Institut Curie) + Bettencourt-Dias (IGC Gulbenkian) — отправлены 27 июл
- [ ] Заполнить Airtable-форму Foresight — с GLA + UNED Madrid
- [x] David Meyer — follow-up отправлен 28 июл
- [x] Submission Package Foresight: `grants/foresight_2026-07-31/SUBMISSION_PACKAGE.md`
- [x] Submission Package OSC: `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md`
- [x] GitHub-активность: 2+ недели (14–28 июл, 200+ коммитов) ✅
- [ ] **29 июл** — проверить ответ David → заполнить Airtable → submit Foresight
- [ ] **30 июл** — OSC resubmit (GitHub Verification)
<!-- /lang:ru -->

## 🆕 28 июл — Пакеты для обеих заявок созданы
- ✅ Foresight: `grants/foresight_2026-07-31/SUBMISSION_PACKAGE.md` — анализ условий, Airtable-инструкция, proposal $50,050
- ✅ OSC: `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md` — условия fiscal hosting, GitHub Verification, бюджет $17K
- ✅ GitHub-активность: условие «2 недели» выполнено (14–28 июл, 200+ коммитов)
- 🔴 Foresight (31 июл): Airtable-форма, proposal .docx
- 🟡 OSC (1 авг): GitHub Verification → открыть страницу на opencollective.com  

## 🔧 28 июл — Прогресс по железу
- ✅ Модуль камеры получен — камера подключается к компьютеру
- 🔄 Адаптер для установки на микроскоп — в пути, ожидается на днях
- ⏳ Следующий шаг: установить камеру на микроскоп через адаптер → тестовый прогон

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
