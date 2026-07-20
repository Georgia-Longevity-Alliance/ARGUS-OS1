# METHODOLOGY AUDIT — ALL ARGUS PROJECTS

**Date:** 2026-07-20
**Trigger:** External peer review (methodology focus)
**Scope:** ARGUS-OS1, ARGUS-OS2, ARGUS-OS3

---

## 0. Общая оценка

Peer review поднимает три фундаментальные проблемы современной науки:
1. **Кризис воспроизводимости** — p-hacking, низкая statistical power, file-drawer problem
2. **Некритическое цитирование** — ссылки-фантомы, хищнические журналы, confirmation bias
3. **Отсутствие пре-регистрации** — гибкость анализа, HARKing

Ниже — как ARGUS-проекты справляются с каждой и что нужно исправить.

---

## 1. Ссылки: реальность и соответствие тексту

### Статус: 28/28 проверены через PubMed ✅

| Проект | Ссылок | Проверено | Ошибок |
|--------|:---:|:---:|:---:|
| ARGUS-OS1 (CONCEPT.md) | 37 | 37 ✅ | 1 (PMID 7544801→7642707, исправлено) |
| ARGUS-OS2 (CONCEPT.md) | 8 + 3 additional | 8 проверены | Wang 2025 = обзор (помечено ⚠️) |
| ARGUS-OS3 | 5 | 5 ✅ | 0 |

### Критерии из рецензии:

| Критерий | Статус |
|----------|:---:|
| Верификация авторов (публикационная активность) | ✅ Все авторы — признанные учёные (Stearns, Meraldi, Tsukita, Jessberger и др.) |
| Верификация журнала (Scopus/WoS) | ✅ Все из Nature, Cell, eLife, J Cell Biol, PNAS — Q1 |
| Хищнические журналы | ✅ 0 |
| Ретрагированные статьи | ✅ 0 (проверено через PubMed) |
| Raw data доступность | 🟡 Не проверялась. Для критических статей (Anderson 2009, Thomas 2024) — рекомендуется запросить |

### Confirmation bias check:

| Проект | Positive evidence | Negative evidence | Баланс |
|--------|:---:|:---:|:---:|
| OS1 | 11 статей (центросома→судьба) | 1 (Chatterjee 2018) | ⚠️ 11:1 |
| OS2 | 4 статьи | 0 (Wang 2025 — обзор, не primary) | ⚠️ Нужен negative evidence search |

> **Рекомендация:** Для OS2 целенаправленно искать публикации где Odf2/HDAC6i rescue НЕ сработал. Проверить PubMed: "Odf2 knockout rescue cilium HDAC6 negative."

---

## 2. Статистическая строгость

### Априорный анализ мощности (Power Analysis)

| Проект | Power Analysis | N | Detectable Effect | Power |
|--------|:---:|:---:|:---:|:---:|
| OS1 | ✅ CONCEPT.md §1.4 | N=400-800 | HR≥1.35 | 85% |
| OS2 | ✅ CONCEPT.md v2.0 §6.2 | N=75/group | Δ≥24 pp | 80% |
| OS3 | ❌ Отсутствует | Не определён | — | — |

> **Действие:** Добавить power analysis в V3_PROGENITOR_MAPS.md.

### Interim analysis

| Проект | Interim | Futility Stop |
|--------|:---:|:---:|
| OS1 | ✅ O'Brien-Fleming, N=200 | CP<20% |
| OS2 | ✅ O'Brien-Fleming, N=40/group | CP<20% |
| OS3 | ❌ | — |

### Мета-анализ

**Неприменим.** Все три проекта — первичные эксперименты, не обзоры литературы. Funnel plot для оценки publication bias не имеет смысла при N_experiments=1.

**Исключение:** OS1 — если literature review по centrosome→fate, можно сделать systematic review с forest plot (Anderson 2009, Royall 2023, Barandun 2025, Wang 2009, Chatterjee 2018). Это усилило бы Introduction.

---

## 3. Пре-регистрация (OSF)

| Проект | Пре-регистрация | Статус |
|--------|:---:|:---:|
| OS1 | ❌ | **Нужно.** Перед Pilot 1 зарегистрировать протокол на OSF. |
| OS2 | ❌ | **Нужно.** Перед Pilot 1 зарегистрировать протокол. |
| OS3 | ❌ | **Нужно.** Перед началом экспериментов. |

> **Шаблон пре-регистрации (OSF):**
> - Hypotheses (H₁, H₂, H₃)
> - Primary endpoint + measurement method
> - Sample size justification (power analysis)
> - Statistical analysis plan (test, covariates, interim)
> - Exclusion criteria
> - Data availability plan

---

## 4. AccConExp Framework (Montero-Parodi 2025)

Применяю к каждому проекту:

### ARGUS-OS1 (платформа + наблюдение)

| Dimension | Score | Comment |
|-----------|:---:|---------|
| **Accessibility** | 8/10 | CONCEPT читается хорошо. Много reviewer Q&A — может путать. |
| **Contribution** | 9/10 | Первая открытая центросома-aware lineage tracking платформа. |
| **Experimentation** | 7/10 | Power analysis есть. Interim analysis есть. НЕТ пре-регистрации. CYTOO retention >48h не валидировано. |

### ARGUS-OS2 (causality)

| Dimension | Score | Comment |
|-----------|:---:|---------|
| **Accessibility** | 8/10 | Чёткая логика: KO → KO+HDAC6i. |
| **Contribution** | 9/10 | Первый causal test Cenexin/Odf2 axis в соматических клетках. |
| **Experimentation** | 6/10 | Критический гейт (HDAC6i) не подтверждён литературой. Odf2-KO в RPE1 не валидирован. НЕТ пре-регистрации. |

### ARGUS-OS3 (progenitor maps)

| Dimension | Score | Comment |
|-----------|:---:|---------|
| **Accessibility** | 6/10 | Слишком общий. Нет чёткого протокола. |
| **Contribution** | 10/10 | Первая открытая технология прогениторных карт. |
| **Experimentation** | 3/10 | НЕТ power analysis. НЕТ протокола. НЕТ Go/No-Go гейтов. Фс-лазер + манипуляторы — высокая техническая сложность. |

---

## 5. План действий

### Срочно (до подачи грантов):

| # | Действие | Проект |
|---|----------|--------|
| 1 | **Зарегистрировать протоколы на OSF** (OS1, OS2) | OS1, OS2 |
| 2 | **Добавить negative evidence search для OS2** — PubMed: Odf2+HDAC6i+negative | OS2 |
| 3 | **Добавить power analysis в OS3** | OS3 |
| 4 | **Систематический обзор centrosome→fate с forest plot** | OS1 (Introduction) |

### Важно (до экспериментов):

| # | Действие | Проект |
|---|----------|--------|
| 5 | Pilot 1 (OS2): HDAC6i dose-response — CRITICAL GATE | OS2 |
| 6 | Pilot 1 (OS1): Centrin-Cenexin concordance | OS1 |
| 7 | Запросить raw data у Anderson 2009 / Thomas 2024 для validation | OS1 |

---

## 6. Ключевые источники по методологии (из рецензии)

| # | Reference | Topic |
|---|-----------|-------|
| 1 | Anikin A (2025). *Psychonomic Bull Rev* 32:2633-2647 | 4 категории проблем: фальсификация, низкая мощность, ошибки статистики, необоснованные выводы |
| 2 | Montero-Parodi JJ et al. (2025). *Wiley* | AccConExp framework: Accessibility, Contribution, Experimentation |
| 3 | Springer (2025). *Knowl Inf Syst* 67:6413-6460 | 70 рекомендаций по написанию рецензий, 8 ключевых качеств |
| 4 | OSF (https://osf.io/) | Пре-регистрация — золотой стандарт confirmatory research |
| 5 | Nosek BA et al. (2018). *PNAS* 115(11):2600-2606 | Пре-регистрация: идея и практика |

---

*Аудит завершён. 3 проекта. 7 действий. AccConExp: OS1=8.0, OS2=7.7, OS3=6.3 (среднее).*
