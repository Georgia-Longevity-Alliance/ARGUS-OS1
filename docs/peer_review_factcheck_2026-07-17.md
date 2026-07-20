# ФАКТ-ЧЕК PEER REVIEW — ARGUS-OS1 v34.0

**Дата:** 2026-07-17
**Проверено:** 10 ссылок через PubMed + прямой поиск

---

## СВОДКА: 7 проверенных, 1 ошибочный PMID, 1 не найдена, 2 ошибки в датах

| # | Статья (как в рецензии) | PMID | Статус | Примечание |
|---|------------------------|------|--------|------------|
| 1 | Wang et al., 2009, Nature | 19829375 | ✅ | Мышь, RGPs in vivo, Kaede-Centrin1 |
| 2 | Chatterjee et al., 2017, Cerebellum | ~~29667134~~ → **29663194** | ⚠️ PMID неверный | Правильный PMID: 29663194. Год: 2018, не 2017 |
| 3 | Royall et al., 2023, eLife | 37882444 | ✅ | **НЕ препринт!** Полноценная публикация eLife |
| 4 | Izumi & Kaneko, 2012, PNAS | 23064640 | ✅ | Нейробластома человека |
| 5 | Morsch et al., 2017, J Vis Exp | 28190072 | ✅ | 405 nm, НО: zebrafish, не mammalian |
| 6 | Loncarek et al., 2008, Nat Cell Biol | 18297061 | ✅ | S-phase-arrested (hydroxyurea), не cycling |
| 7 | Khodjakov et al., 1997, Cell Motil Cytoskel | 9415373 | ✅ | 532 nm ns, PtK1 |
| 8 | Okano et al., 2020, Biochem Biophys Rep | 33083577 | ✅ | NIR fs 800 nm, HepG2 + zebrafish |
| 9 | Barandun et al., 2025, Cell Rep | 39764850 | ✅ | CD8+ T-клетки, mother → effector (не память!) |
| 10 | Anderson 2009 (Cenexin) | — | ❌ НЕ НАЙДЕНА | Нет в PubMed. Возможная галлюцинация рецензента |

---

## 🔴 КРИТИЧЕСКИЕ ОШИБКИ РЕЦЕНЗИИ

### 1. Неверный PMID для Chatterjee
Рецензент указал PMID **29667134** — это trial препарата DFP-10917 (рак), не имеющий отношения к центросомам. Правильный PMID: **29663194**.

### 2. «bioRxiv 2022 — не рецензирован» — ЛОЖЬ
Royall et al. (PMID: 37882444) опубликован в **eLife** (октябрь 2023), полностью рецензирован. На bioRxiv был препринт (2022.09.20.508710), но статья прошла peer review и опубликована. Утверждение рецензента «This is unacceptable for grant justification» основано на ошибочной предпосылке.

### 3. Anderson 2009 не найдена
Рецензент приводит детальные данные: «Cenexin/ODF2 signal was greater on the centrosome of one cell in a sister pair after mitotic shake-off (64.4% brighter, n=100 centrosome pairs at 30 min). At 2 hr after mitotic shake-off, the centrosome with greater cenexin/ODF2 staining had the primary cilium in 84% of sister pairs. 94% asymmetry (33/35 пар) для образования цилий.» — Ни одна статья с такими параметрами не найдена в PubMed. Возможная галлюцинация.

### 4. Год Chatterjee: 2018, не 2017
Chatterjee et al. (PMID: 29663194) опубликован в Cerebellum, October 2018, 17(5):685-691.

### 5. Barandun: mother → EFFECTOR (не memory)
Рецензент пишет «In CD8+ T cells, old centriole → effector daughter — OPPOSITE direction from NPCs». На самом деле в Barandun 2025: mother centrosome → **effector-like** daughter (через ninein). Ninein deletion нарушает **memory**, не effector. Это важно: mother → effector, но для memory formation нужен ninein-dependent механизм.

---

## 🟢 СИЛЬНЫЕ СТОРОНЫ РЕЦЕНЗИИ (реальные проблемы)

### Chatterjee 2018 — РЕАЛЬНЫЙ контраргумент
PMID: 29663194. Cerebellum. 2018 Oct;17(5):685-691.
> «Centrosome Inheritance Does Not Regulate Cell Fate in Granule Neuron Progenitors of the Developing Cerebellum»
Вывод: в гранулярных нейральных прогениторах мозжечка (CGNPs) **центросомное наследование НЕ коррелирует с судьбой клетки**. Mother и daughter centrosomes существуют (разное количество PCM), но какая клетка какую наследует — не определяет дифференцировку.

**Почему это серьёзно для ARGUS-OS1:**
- Wang 2009 — неокортекс, Chatterjee 2018 — мозжечок. Разные регионы мозга → разная зависимость от centrosome inheritance.
- ARGUS-OS1 планирует использовать NPC (передний мозг), но в humans (Royall 2023 — forebrain organoids, eLife). Royall 2023 **подтверждает** asymmetric inheritance в human NPCs.
- Chatterjee НЕ опровергает Wang/Royall — он показывает, что механизм НЕ универсален для всех neural progenitors.

### Статистическая мощность — реальная проблема
Fisher's exact test при N=50-100, α=0.05: для детекции разницы 70% vs 30% мощность достаточная (>90%). НО если реальная разница меньше (скажем, 55% vs 45% = 10 п.п.), то при N=50 мощность падает ниже 20%. Смешанная логистическая регрессия (glmer) с учётом кластеризации по материнской клетке — правильная рекомендация.

### Morsch 2017 — zebrafish, не mammalian
405 nm ablation валидирован в zebrafish neurons (Morsch 2017), а не в mammalian NPC. Для mammalian cells нужно отдельное подтверждение. Okano 2020 (NIR fs) тоже частично в zebrafish.

### Loncarek 2008 — S-phase-arrested
Дочерняя центриоль регенерирует через ~4h после абляции в S-phase-arrested (hydroxyurea) HeLa. В cycling cells динамика может отличаться.

---

## 🟡 УТОЧНЕНИЯ КОНТЕКСТА

### Направление асимметрии — контекстно-зависимо
| Система | Направление | Ссылка |
|---------|------------|--------|
| Mouse cortical RGPs | Mother → **progenitor** (самообновление) | Wang 2009 |
| Human forebrain NPCs | Mother → **progenitor** (самообновление) | Royall 2023 |
| Human neuroblastoma | Daughter (younger) → **NuMA+** (differentiation?) | Izumi 2012 |
| CD8+ T cells | Mother → **effector** (дифференцировка) | Barandun 2025 |
| Cerebellar GNPs | **Нет корреляции** с судьбой | Chatterjee 2018 |

Вывод: направление зависит от типа клеток, ткани, стадии развития. Для human forebrain NPCs данные Royall 2023 + Wang 2009 подтверждают mother → progenitor.

---

## 📋 РЕКОМЕНДАЦИИ ПО ДОРАБОТКЕ CONCEPT.md

### Обязательно (устранить фактические ошибки)
1. **Заменить «bioRxiv 2022, preprint» → Royall et al., 2023, eLife (PMID: 37882444)** — полноценная публикация
2. **Добавить Chatterjee et al., 2018 (PMID: 29663194)** — с пояснением: GNP мозжечка ≠ NPC переднего мозга, механизм не универсален
3. **Добавить Barandun et al., 2025 (PMID: 39764850)** — mother → effector в CD8+ T cells
4. **Уточнить Morsch 2017** — zebrafish, метод переносим на mammalian с валидацией

### Рекомендовано (усилить аргументацию)
5. **Контрольный эксперимент:** фиксация + Cenexin/Centrin окрашивание NPC до V1 — подтвердить асимметрию в конкретной линии
6. **Статистика:** Fisher → смешанная логистическая регрессия. N≥150-200 пар для 15 п.п. при мощности 80%.
7. **Cenexin quantitative threshold:** ratio >1.5, валидация на фиксированных образцах
8. **План для нулевого результата:** явно прописать — «даже отсутствие корреляции будет опубликовано как значимый результат»

### Факультативно
9. Валидация 72h стабильности (ASA 48h — увеличить бюджет на тестирование)
10. Контроль фотоксичности (сравнение illuminated vs dark)

---

## 📊 ИТОГОВЫЙ ВЕРДИКТ ПО РЕЦЕНЗИИ

Рецензия содержит **реальные методологические проблемы** (Chatterjee 2018, статмощность, Cenexin-quantitation) и **фактические ошибки** (неверный PMID, неверный статус Royall 2023, возможно галлюцинированная Anderson 2009).

**Общая оценка:** замечания 1, 2, 4, 5 — валидны и требуют доработки. Замечание 3 (про препринт) — ошибочно, но указание на необходимость рецензированных источников было правильным по духу (Royall 2023 как раз и есть рецензированный).

**Рекомендация:** учесть все реальные замечания, исправить фактические ошибки в ссылках, добавить Chatterjee 2018 + Barandun 2025. CONCEPT.md станет сильнее.
