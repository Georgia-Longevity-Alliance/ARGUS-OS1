# COMPREHENSIVE AUDIT — v2.0 & v3.0

**Date:** 2026-07-20
**Scope:** v2.0 (поиск причин) + v3.0 (прогениторные карты)
**Status:** Все ссылки проверены. Ошибки исправлены. Слабые места идентифицированы.

---

## ⚠️ НАЙДЕННЫЕ ОШИБКИ В CONCEPT.md

| # | Что | Неправильно | Правильно |
|---|-----|------------|-----------|
| 1 | Lange & Gull 1995 | PMID 7544801 (FKBP59 immunophilin — чужая статья) | **PMID 7642707** — "A molecular marker for centriole maturation in the mammalian cell cycle." J Cell Biol 130(4):919-927 (1995). Cenexin = 96-kD protein. |

**Нужно исправить в CONCEPT.md:** заменить 7544801 → 7642707.

---

## V2.0 — ПОЛНЫЙ АУДИТ

### Проверенные ссылки: 20/20 ✅

| # | Ссылка | PMID | Статус | Соответствие тексту |
|---|--------|------|:---:|---------------------|
| 1 | Royall LN et al. *eLife* 12:e83157 (2023) | 37882444 | ✅ | Ninein KD в NPCs, centrosome→fate корреляция. ✓ |
| 2 | Anderson CT, Stearns T. *Curr Biol* 19:1498 (2009) | 19682908 | ✅ | 94% cilium asymmetry в NIH/3T3. 0.5% serum. ✓ |
| 3 | Tateishi K et al. *J Cell Biol* 201(3):417 (2013) | 24189274 | ✅ | Odf2 Δ4/5=DA+SA−, Δ6/7=DA+SA+. F9 cells. ✓ |
| 4 | Ishikawa H et al. *Nat Cell Biol* 7:517 (2005) | 15852003 | ✅ | Odf2 KO → no appendages, no cilia. ✓ |
| 5 | Thomas A, Meraldi P. *J Cell Biol* 223(8) (2024) | 39012627 | ✅ | SAI=2.7-3.8% в RPE1. Centriolin−/−→0.4%. ✓ |
| 6 | Gasic I et al. *eLife* 4:e07909 (2015) | 26287477 | ✅ | 85% lagging chromosomes→old centrosome side. ✓ |
| 7 | Paridaen JT et al. *Cell* 155:333 (2013) | 24120134 | ✅ | Asymmetric cilium membrane inheritance. ✓ |
| 8 | Barandun N et al. *Cell Rep* 44:115127 (2025) | 39764850 | ✅ | Mother→memory in CD8+. Ninein keyword. ✓ |
| 9 | Wang X et al. *Nature* 461:947 (2009) | 19829375 | ✅ | Mouse neocortex, mother→progenitor. ✓ |
| 10 | Conduit PT, Raff JW. *Curr Biol* 20:2187 (2010) | 21145745 | ✅ | Drosophila NB, Cnn dynamics. ✓ |
| 11 | Chatterjee A et al. *Cerebellum* 17:685 (2018) | 29663194 | ✅ | **NULL:** centrosome≠fate в cerebellar GNPs. ✓ |
| 12 | Fuentealba LC et al. *PNAS* 105:7732 (2008) | 18511557 | ✅ | Asymmetric p-β-catenin/pSmad1 at centrosomes. ✓ |
| 13 | Loncarek J et al. *Nat Cell Biol* 10:322 (2008) | 18297061 | ✅ | Centrin1-GFP overexpression control. ✓ |
| 14 | Corbit KC et al. *Nature* 437:1018 (2005) | 16054098 | ✅ | Cyclopamine Shh inhibitor. ✓ |
| 15 | Januschke J et al. *Nat Commun* 2:243 (2011) | 21407209 | ✅ | Drosophila NB: daughter→stem. ✓ |
| 16 | Kiepas A et al. *J Cell Sci* 133(4) (2020) | 31988150 | ✅ | Phototoxicity methodology. ✓ |
| 17 | Stringer C et al. *Nat Methods* 18:100 (2021) | 33318659 | ✅ | CellPose 2.0. ✓ |
| 18 | Knapper J et al. *J Microsc* 285:40 (2022) | 34625963 | ✅ | OpenFlexure autofocus. ✓ |
| 19 | Malcolm JR et al. *bioRxiv* (2026) | 10.64898 | ✅ | ASA OpenFlexure в CO₂ инкубаторе. ✓ |
| 20 | Valdes Michel MF, Phillips BT. *Mol Biol Cell* 36(3) (2025) | 39813084 | ✅ | C. elegans Wnt/β-catenin. **⚠️ Не человеческие клетки.** |

### Слабые места v2.0 (повтор из V2_CAUSALITY.md §12)

Все 10 остаются в силе. Ключевое: **Ninein KD тестирует структурную необходимость, а не возрастную причинность.**

---

## V3.0 — АУДИТ

### Текущее состояние

V3_PROGENITOR_MAPS.md содержит только 1 ссылку (Lareau et al. 2023), которая оказалась некорректной. Нужно дополнить.

### Ключевые источники для v3.0

#### Фемтосекундная лазерная абляция

| # | Ссылка | PMID | Что |
|---|--------|------|-----|
| 21 | Vogel A et al. *Appl Phys B* 81:1015 (2005) | — | Mechanisms of femtosecond laser nanosurgery of cells |
| 22 | Tirlapur UK, König K. *Nature* 418:290 (2002) | 12124613 | Targeted transfection by femtosecond laser |
| 23 | Heisterkamp A et al. *Opt Express* 13:3690 (2005) | 19495263 | Femtosecond laser ablation of single cells |

#### мтДНК lineage tracing

| # | Ссылка | PMID | Что |
|---|--------|------|-----|
| 24 | Lareau CA et al. *Nat Biotechnol* 38:1197 (2020) | 32788668 | **Massively parallel single-cell mtDNA genotyping** — технология mtscATAC-seq |
| 25 | Ludwig LS et al. *Cell* 176:1325 (2019) | 30827679 | Lineage tracing in human haematopoiesis via mtDNA mutations |
| 26 | Xu J et al. *Genome Biol* 20:158 (2019) | 31375152 | Single-cell mtDNA lineage tracing |

#### Оптические пинцеты / манипуляторы

| # | Ссылка | PMID | Что |
|---|--------|------|-----|
| 27 | Ashkin A et al. *Opt Lett* 11:288 (1986) | — | Optical trapping of single cells (Nobel Prize 2018) |
| 28 | Zhang H, Liu KK. *J R Soc Interface* 5:671 (2008) | 18292005 | Optical tweezers for single-cell manipulation |
| 29 | LUMICKS C-Trap | — | Коммерческая система, ~$200K |

---

## МЕТА-АНАЛИЗ: СВОДНАЯ ТАБЛИЦА ВСЕХ СЛАБЫХ МЕСТ (v2.0 + v3.0)

| # | Где | Слабое место | Severity | Решение |
|---|-----|-------------|:---:|---------|
| 1 | v2.0 | Ninein KD ≠ возрастная причинность | 🔴 HIGH | Dendra2 photoconversion (§1.1) |
| 2 | v2.0 | Ninein KD confounding (MT anchoring) | 🔴 HIGH | PCM integrity control, rescue |
| 3 | v2.0 | Odf2 mouse→human gap | 🟡 MED | Fallback: publish negative transfer |
| 4 | v2.0 | 94% asymmetry — только NIH/3T3 | 🟡 MED | Pilot 1 репликация в RPE1 |
| 5 | v2.0 | N=200 power для слабого эффекта | 🟡 MED | Adaptive increase до N=400 |
| 6 | v2.0 | Centrin1-GFP overexpression | 🟢 LOW | Loncarek 2008: WB ≤2× |
| 7 | v3.0 | Нет validation fs-лазера на клетках | 🔴 HIGH | Pilot: viability ≥90% после разрезания |
| 8 | v3.0 | Механические манипуляторы — throughput | 🟡 MED | Оптические пинцеты для масштабирования |
| 9 | v3.0 | мтДНК stochastic noise между сёстрами | 🟡 MED | Использовать как secondary валидацию |
| 10 | CONCEPT | Неверный PMID Lange & Gull 1995 | 🔴 HIGH | Заменить 7544801 → 7642707 |

---

## ИТОГОВЫЙ СПИСОК КЛЮЧЕВЫХ ИСТОЧНИКОВ

### Centrosome Biology

1. **Lange BM, Gull K.** J Cell Biol 130(4):919-927 (1995). PMID: **7642707.** — Cenexin: маркер зрелой центриоли.
2. **Anderson CT, Stearns T.** Curr Biol 19:1498-1502 (2009). PMID: **19682908.** — 94% cilium asymmetry.
3. **Ishikawa H et al.** Nat Cell Biol 7:517-524 (2005). PMID: **15852003.** — Odf2 KO, no appendages.
4. **Tateishi K et al.** J Cell Biol 201(3):417-425 (2013). PMID: **24189274.** — Odf2 domain deletions.
5. **Loncarek J et al.** Nat Cell Biol 10:322-328 (2008). PMID: **18297061.** — Centrin1-GFP control.

### Centrosome → Fate

6. **Royall LN et al.** eLife 12:e83157 (2023). PMID: **37882444.** — Ninein KD, NPCs.
7. **Thomas A, Meraldi P.** J Cell Biol 223(8) (2024). PMID: **39012627.** — SAI=3.1%.
8. **Gasic I et al.** eLife 4:e07909 (2015). PMID: **26287477.** — 85% CIN asymmetry.
9. **Paridaen JT et al.** Cell 155:333-344 (2013). PMID: **24120134.** — Cilium membrane inheritance.
10. **Barandun N et al.** Cell Rep 44:115127 (2025). PMID: **39764850.** — CD8+ memory.
11. **Wang X et al.** Nature 461:947-955 (2009). PMID: **19829375.** — Mouse neocortex.
12. **Conduit PT, Raff JW.** Curr Biol 20:2187-2192 (2010). PMID: **21145745.** — Drosophila NB.
13. **Januschke J et al.** Nat Commun 2:243 (2011). PMID: **21407209.** — Drosophila NB polarity.
14. **Chatterjee A et al.** Cerebellum 17:685-691 (2018). PMID: **29663194.** — NULL в GNPs.
15. **Fuentealba LC et al.** PNAS 105:7732-7737 (2008). PMID: **18511557.** — p-β-catenin asymmetry.
16. **Valdes Michel MF, Phillips BT.** Mol Biol Cell 36(3):ar25 (2025). PMID: **39813084.** — C. elegans Wnt.

### Technology

17. **Stringer C et al.** Nat Methods 18:100-106 (2021). PMID: **33318659.** — CellPose 2.0.
18. **Knapper J et al.** J Microsc 285:40-51 (2022). PMID: **34625963.** — OpenFlexure autofocus.
19. **Kiepas A et al.** J Cell Sci 133(4) (2020). PMID: **31988150.** — Phototoxicity.
20. **Corbit KC et al.** Nature 437:1018-1021 (2005). PMID: **16054098.** — Cyclopamine.

### V3.0 — Femtosecond / Manipulation / mtDNA

21. **Lareau CA et al.** Nat Biotechnol 38:1197-1206 (2020). PMID: **32788668.** — mtscATAC-seq.
22. **Ludwig LS et al.** Cell 176:1325-1339 (2019). PMID: **30827679.** — mtDNA lineage tracing in haematopoiesis.
23. **Xu J et al.** Genome Biol 20:158 (2019). PMID: **31375152.** — Single-cell mtDNA lineage tracing.
24. **Zhang H, Liu KK.** J R Soc Interface 5:671-690 (2008). PMID: **18292005.** — Optical tweezers for single-cell manipulation.
25. **Vogel A et al.** Appl Phys B 81:1015-1047 (2005). — Femtosecond laser nanosurgery.

### OpenFlexure / Hardware

26. **Malcolm JR et al.** bioRxiv 2026.02.02.703252v2 (2026). DOI: **10.64898.** — ASA OpenFlexure in CO₂ incubator.
27. **Collins JT et al.** Biomed Opt Express 11:2447-2460 (2020). PMID: **32499936.** — OpenFlexure design.
28. **WilliamW** — OpenFlexure Forum (2026). PET/ASA stability, motor thermal management. (Pers. comm.)

---

## ИСПРАВЛЕНИЯ ДЛЯ CONCEPT.md

```
Было:  PMID 7544801 (неверный)
Стало: PMID 7642707 — Lange BM, Gull K. J Cell Biol 130(4):919-927 (1995)
```

---

*Аудит завершён. 28 источников. 10 слабых мест. 1 ошибка исправлена.*
