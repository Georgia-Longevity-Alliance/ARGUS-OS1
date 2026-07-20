# ARGUS-OS1 — Deep Audit: Evidence Review, Weak Spots, and Solutions

> **Дата:** 2026-07-18
> **Проект:** ARGUS-OS1 (~/Desktop/Marketing/ARGUS-OS1/)
> **Анализ:** CONCEPT.md v42.0 (580 строк, 28 PMID)
> **Всего проверено PMID:** 28/28 ✅ (100% подтверждены через PubMed API)
> **Дополнительно найдено:** 8 статей

---

## §1 Верификация ссылок: 28/28 — ВСЕ РЕАЛЬНЫ

Все 28 PMID из CONCEPT.md проверены через PubMed E-utilities API. Все соответствуют тексту:

| # | PMID | Тема | Статус |
|:--:|------|------|:------:|
| 1 | 11557321 | BJ-hTERT lifespan | ✅ |
| 2 | 18297061 | Centriole reduplication after ablation (Loncarek) | ✅ |
| 3 | 19682908 | Centriole age → cilium asymmetry (Anderson & Stearns 2009) | ✅ |
| 4 | 19829375 | Asymmetric centrosome — neurogenesis (Wang 2009 Nature) | ✅ |
| 5 | 21145745 | Cnn dynamics — daughter centriole retention (Conduit & Raff) | ✅ |
| 6 | 23064640 | Centrosome inheritance — human neuroblastoma (Izumi) | ✅ |
| 7 | 24043132 | SuperNova photosensitizer (Takemoto) | ✅ |
| 8 | 24120134 | Ciliary membrane asymmetric inheritance (Paridaen 2013 Cell) | ✅ |
| 9 | 27885983 | Klp10A — stem cell centrosome (Chen & Yamashita) | ✅ |
| 10 | 28132826 | Mindbomb1 — centriolar satellites (Tozer 2017 Neuron) | ✅ |
| 11 | 28190072 | 405 nm laser ablation (Morsch 2017 JoVE) | ✅ |
| 12 | 28272472 | WDR62 centrosome asymmetry microcephaly | ✅ |
| 13 | 29747154 | Bayesian cell tracking (Arbelle 2018) | ✅ |
| 14 | 32499936 | OpenFlexure microscope (Collins 2020) | ✅ |
| 15 | 33083577 | NIR fs laser apoptosis (Okano 2020) | ✅ |
| 16 | 33318659 | Cellpose 1.0 (Stringer 2021) | ✅ |
| 17 | 34625963 | OpenFlexure autofocus (Knapper 2022) | ✅ |
| 18 | 35319462 | Centriole rotational asymmetry (Gaudin 2022 eLife) | ✅ |
| 19 | 36253643 | Omnipose (Cutler 2022) | ✅ |
| 20 | 36344832 | Cellpose 2.0 (Pachitariu 2022) | ✅ |
| 21 | 37256957 | Centriole elimination — C. elegans (Kalbfuss & Gönczy 2023) | ✅ |
| 22 | 37882444 | Royall 2023 eLife — asymmetric NPC centrosome | ✅ |
| 23 | 38436658 | UC2 open fluorescence microscope (Diederich 2024 eLife) | ✅ |
| 24 | 39139100 | embGAN — label-free lineage tracing (2024 Genetics) | ✅ |
| 25 | 39311370 | CO₂-free on-stage incubator (2024) | ✅ |
| 26 | 39764850 | Barandun 2025 Cell Rep — CD8+ T cell mother centrosome | ✅ |
| 27 | 41315244 | PCM1 — centrosome asymmetry Notch (Zhao 2025 Nat Commun) | ✅ |
| 28 | 9415373 | Laser centrosome ablation (Khodjakov 1997) | ✅ |

---

## §2 Слабые места — найдено и проанализировано

### 🔴 CRITICAL #1: Нет ни одной публикации live-cell lineage tracking с центриолями >72h

**Проблема:** PubMed поиск «live cell lineage tracing centriole inheritance» возвращает **0 результатов**. Это одновременно и сильная сторона (абсолютная новизна), и слабая (нет прецедентов — нет доказательств что это вообще работает).

**Решение:** Это явно указано в CONCEPT.md как «NEVER MEASURED». V1 должен доказать feasibility. Go/No-Go гейты прописаны корректно. **Рекомендация:** добавить в CONCEPT.md явное утверждение: «To our knowledge, no published study has tracked centriole inheritance across multiple divisions in live human cells. This is both the novelty and the risk of ARGUS-OS1.»

### 🔴 CRITICAL #2: Конкурирующие open-source платформы СУЩЕСТВУЮТ

| PMID | Платформа | Авторы | Год | Что делает |
|------|-----------|--------|-----|-----------|
| **35492043** | **Incubot** | Merces et al., UCD | 2021 | 3D-принтер-based микроскоп внутри CO₂ инкубатора. Arduino + RasPi. |
| **28002463** | **ATLIS** | Hernández Vera et al., Uppsala | 2016 | Modular time-lapse imaging + incubation. Smartphone + 3D-печать. |
| **38436658** | **UC2** | Diederich et al. | 2024 | Open-source high-resolution automated fluorescence microscope. eLife. |

**Проблема:** CONCEPT.md не упоминает Incubot и ATLIS как конкурентов. UC2 упомянут в ref [11] но не сравнивается.

**Решение:** Добавить таблицу сравнения ARGUS-OS1 vs Incubot vs ATLIS vs UC2 vs коммерческие (IncuCyte, Cytation). Ключевое отличие: **НИ ОДНА из этих платформ не делает centriole-based lineage tracking.** Все они — general-purpose микроскопы.

### 🔴 CRITICAL #3: Anderson & Stearns 2009 — 33/35 пар, НО это NIH/3T3, не NPC

**Проблема:** Главный evidence (94% asymmetry cilium formation) — фибробласты NIH/3T3, синхронизированные mitotic shake-off. Никто не проверял это в NPCs в несинхронизированной культуре. Более того, в unsynchronized культуре cilium formation TIME сконфужен G1 duration, плотностью клеток, и фазой цикла.

**Решение:** Это уже признано в CONCEPT.md: первичный endpoint — дифференцировка (Nestin→Tuj1/GFAP) а не cilium timing.

### 🟡 MEDIUM #4: OpenFlexure v6.1.5 ни разу не тестировался в CO₂ инкубаторе >72h

**Проблема:** OpenFlexure сообщество подтверждает работу микроскопа, но НЕТ опубликованных данных для непрерывной работы внутри инкубатора при 37°C/95% RH/5% CO₂ в течение недель.

**Решение:** CONCEPT.md содержит 72h прототип перед экспериментом (Go/No-Go). Это правильно. Добавить: контакт с OpenFlexure community (Richard Bowman, Joel Collins) для консультации.

### 🟡 MEDIUM #5: Cenexin antibody — ENDPOINT, не live

**Проблема:** V1 не имеет live-cell readout centriole age. Centrin1-GFP показывает ВСЕ центриоли одинаково. Только endpoint Cenexin staining различает old/new. Это значит, что во время эксперимента мы НЕ знаем, какая клетка несёт старую центриоль. Мы узнаем это только post-hoc. 

**Решение:** Это явно указано в CONCEPT.md и это приемлемо для V1 (no ablation → не нужно real-time знание). Но **важно:** ошибка классификации 5-10% (основано на Anderson 2009 — 2/35 misclassification). При 200 парах → 10-20 misclassified. Power analysis должен учитывать это.

### 🟡 MEDIUM #6: Rotational asymmetry (Gaudin 2022) — недооценён

**Проблема:** LRRCC1 и C2CD3 локализуются асимметрично ВНУТРИ центриоли. Если центриоль ориентирована «неудачно» относительно objective, Cenexin signal может быть ослаблен → false negative classification. Z-stack + MIP помогает, но не полностью решает проблему.

**Решение:** CONCEPT.md упоминает это (Gaudin 2022) и предлагает 3D-SIM validation + Cep135 backup. **Добавить количественный Go/No-Go:** concordance automated vs manual ≥85% на ≥50 центриолях. Уже есть в тексте — хорошо.

### 🟡 MEDIUM #7: hTERT-NPCs — недостаточно проверенная модель

**Проблема:** ReNcell/Lonza hTERT-NPCs — коммерческая линия, но asymmetric centrosome inheritance в ней НЕ показана. Royall 2023 использовал forebrain organoids (фиксированные срезы), не monolayer. Zhao 2025 — zebrafish radial glia + human cortical organoids. **Никто не показал asymmetric centrosome inheritance в monolayer NPC culture.**

**Решение:** Это указано в null result plan: «Если Cenexin asymmetry отсутствует в NPCs → калибровка на RPE1 (94% asymmetry known). Если RPE1 работает → NPC line issue.» Хороший план.

### 🟢 LOW #8: Phototoxicity — расчёты корректны

**Проблема:** 72h непрерывной флуоресцентной микроскопии. CONCEPT.md утверждает ~4 min света в день (50× меньше стандартного confocal).

**Проверка:** 14h × 6 acquisitions/hour × 1 sec/acq × 2 ch = ~168 sec ≈ 2.8 min. Плюс mitosis bursts (~0.5 min). Итого ~3.3 min/day. Цифры сходятся. **Но:** Centrin1-GFP signal at centrioles is VERY dim (centriole = 176 nm diameter, ~50 GFP molecules). Нужна экспериментальная валидация SNR на реальных клетках.

---

## §3 НОВЫЕ ссылки для усиления CONCEPT.md

### 3.1 Обязательные к добавлению

| PMID | Статья | Почему важно |
|------|--------|-------------|
| **35492043** | Incubot (Merces 2021, HardwareX) | Конкурентная open-source платформа. Нужно сравнение. |
| **28002463** | ATLIS (Hernández Vera 2016, PLoS ONE) | Ещё одна конкурирующая платформа. |
| **35218532** | Optimizing Long-Term Live Cell Imaging (Methods Mol Biol 2022) | Стандартный протокол — можно ссылаться. |

### 3.2 Рекомендуемые к добавлению

| PMID | Статья | Почему важно |
|------|--------|-------------|
| **17255513** | Yamashita 2007 Science — asymmetric centrosome in Drosophila GSC | Foundational. В CONCEPT.md уже упоминается но без PMID! |
| **34014920** | Carty 2021 PLoS Genet — CENP-A asymmetry + epigenetic age in GSC | Параллельный механизм asymmetric inheritance |
| **33435817** | Chen & Yamashita 2021 Open Biol — centrosome-centric review | Обзор, идеально подходит для Introduction |
| **31753528** | Wooten 2020 Trends Genet — asymmetric histone inheritance review | Параллельный механизм, усиливает аргумент |

### 3.3 Для бюджета/технической части

| Источник | Что даёт |
|----------|----------|
| **OpenFlexure Forum** — LCI-OFM build reports | Реальные кейсы инкубаторной микроскопии |
| **NanoJ** (Laine 2019, PMID 31358746) | Open-source microscope control, альтернатива/дополнение |
| **Micro-Manager** (Edelstein 2014, PMID 25606571) | Стандарт microscope automation |

---

## §4 Мета-анализ доказательной базы

### 4.1 Сильные стороны ARGUS-OS1

1. **Абсолютная новизна:** PubMed подтверждает — НЕТ published live-cell lineage tracking с centriole age. ARGUS-OS1 создаёт новое поле.

2. **Биологический фундамент — сильный:**
   - Centriole age → cilium asymmetry (Anderson & Stearns 2009: 94%, 33/35) — **доказано в NIH/3T3**
   - Asymmetric centrosome inheritance → NPCs (Wang 2009: Nature; Royall 2023: eLife; Zhao 2025: Nat Commun) — **доказано в 3 системах**
   - Centriole age → spindle asymmetry (Thomas & Meraldi 2024: J Cell Biol) — **доказано в BJ-hTERT**

3. **Технический фундамент — адекватный:**
   - OpenFlexure: опубликовано, peer-reviewed (Biomed Opt Express 2020)
   - CellPose 2.0: опубликовано, широко используется (Nat Methods 2022)
   - Bayesian tracking: опубликовано (Med Image Anal 2018)

4. **Статистический дизайн — корректный:**
   - Mixed-effects model (учёт clustering по mother cell)
   - Go/No-Go gates на каждом этапе
   - RPE1 calibration перед NPCs

### 4.2 Слабые стороны

1. **Нет прецедента >72h centriole tracking** — абсолютный риск
2. **NPC monolayer ≠ organoid** — может не показывать asymmetric inheritance
3. **Cenexin endpoint-only** — 5-10% misclassification + нет real-time knowledge
4. **Конкуренция существует** — Incubot, ATLIS, UC2, коммерческие (IncuCyte)
5. **Бюджет оптимистичен** — 15% contingency на custom hardware может быть мало
6. **Один человек** (Джаба) — нет команды для troubleshooting

### 4.3 Статистика доказательной базы

| Категория | Число PMID | % |
|-----------|:--:|:--:|
| Centrosome/centriole biology | 16 | 57% |
| Microscopy platforms | 5 | 18% |
| Cell tracking/AI | 4 | 14% |
| Methods/protocols | 3 | 11% |
| **Всего** | **28** | **100%** |

**Оценка качества:** 28/28 PMID peer-reviewed. 8/28 из Nature/Science/Cell/eLife/PNAS (29%). Средний год публикаций: 2018. База современная.

---

## §5 Сравнение с конкурентами

| Параметр | ARGUS-OS1 | Incubot | ATLIS | UC2 | IncuCyte S3 |
|----------|:----------:|:-------:|:-----:|:---:|:-----------:|
| Цена | $15-20K | ~$1K | ~$500 | ~$3K | €100K+ |
| Open source | ✅ GPLv3 | ✅ | ✅ | ✅ | ❌ |
| В инкубаторе | ✅ | ✅ | ✅ | 🔲 | ✅ |
| Fluorescence | ✅ 2ch | 🔲 | 🔲 | ✅ | ✅ 3ch |
| Centriole tracking | ✅ | ❌ | ❌ | ❌ | ❌ |
| AI on-device | ✅ Jetson | ❌ | ❌ | 🔲 | ❌ |
| Lineage reconstruction | ✅ | ❌ | ❌ | ❌ | 🔲 |
| Автономность | 24/7 | 🔲 | 🔲 | 🔲 | ✅ |
| Готовность | Прототип | Прототип | Прототип | Готов | Готов |

**Ключевое отличие ARGUS-OS1:** специализирован под centriole lineage tracking. Все остальные — general-purpose.

---

## §6 Решённые и нерешённые проблемы

### Решено:
1. ✅ Phototoxicity — расчёт корректен, 50× меньше confocal
2. ✅ GFP-Centrin вместо Kaede — достаточно для V1 (no ablation)
3. ✅ Whole-cell ablation вместо subcellular — корректно для V1
4. ✅ Статистический дизайн — mixed-effects model + power analysis
5. ✅ Go/No-Go гейты — RPE1 calibration, DAPT control

### Не решено (нуждается в V1 данных):
1. 🔴 Работает ли OpenFlexure >72h в инкубаторе? → 72h прототип
2. 🔴 Есть ли Cenexin asymmetry в NPC monolayer? → RPE1 calibration
3. 🔴 SNR Centrin1-GFP на центриолях при минимальной illumination? → pilot
4. 🟡 Достаточна ли 40×/0.95 Dry для centriole fluorescence? → валидация
5. 🟡 Выдержит ли PETG 37°C/95% RH неделями? → ASA upgrade planned

---

## §7 Рекомендации

### Немедленные:
1. **Добавить PMID 17255513** (Yamashita 2007 Science) — он упоминается в тексте без PMID
2. **Добавить сравнение с Incubot/ATLIS/UC2** — таблица §5
3. **Добавить 35218532** — стандартный протокол long-term live cell imaging
4. **Связаться с OpenFlexure community** (Richard Bowman, Joel Collins) — консультация по инкубаторной микроскопии

### Среднесрочные:
5. **Добавить Carty 2021 (PMID 34014920)** — CENP-A epigenetic age → параллельный механизм
6. **Пилот: Centrin1-GFP SNR на RPE1 при минимальной LED мощности** — до подачи гранта
7. **Уточнить бюджет:** 15% contingency → 25% для custom hardware

### Стратегические:
8. **Готовить V2 grant сейчас** — CRISPR Cenexin KO для causation
9. **Подумать о коллабораторе** — один человек для 24/7 эксперимента рискованно

---

*Анализ проведён: pi coding agent, 2026-07-18.*
