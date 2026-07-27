# STATE — ARGUS-OS1

**Date:** 2026-07-24
<!-- lang:ru -->
**Status:** 🔵 OS1 = V6. Proposal Foresight готов. Ждём ответов.
<!-- /lang:ru -->

<!-- lang:ru -->
## 24 июл — итог сессии
<!-- /lang:ru -->

### Foresight grant
- ✅ Proposal: `ARGUS_proposal_Foresight.md` + `.docx`
<!-- lang:ru -->
- ✅ 14 рецензий, 12 ссылок (все проверены), $50,050 / 15 мес
- ✅ Дедлайн: **31 июля**
<!-- /lang:ru -->

<!-- lang:ru -->
### Отправлено
- 📬 David Meyer — коллаборация
- 📬 Susan Mango — EU-аффилиация (Biozentrum Basel)
- 📬 Илья + Akaki
<!-- /lang:ru -->

<!-- lang:ru -->
### Ждёт
- [ ] Ответ David — если да → подавать форму Foresight
- [ ] Basto + Bettencourt-Dias — EU-аффилиация
- [ ] Norn Group / Impetus — письмо готово
<!-- /lang:ru -->

## 🆕 24 Jul, 13:30 — Foresight grant: everything sent  
- ✅ Proposal v4 ready (`ARGUS_proposal_v4_final.md`, $41,800)  
- ✅ David Meyer (Köln) — letter with proposal sent, waiting for reply  
- ✅ Ilya + Kaki — test run sent  
- 🔴 Foresight form — waiting for David's reply, then fill out  
- 🔴 David replied (12:57), waiting for decision on collaboration  

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
