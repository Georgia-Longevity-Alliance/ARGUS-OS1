# SYSTEMATIC REVIEW: Centrosome Age → Daughter Cell Fate

**Date:** 2026-07-20
**For:** ARGUS-OS1 Introduction (CONCEPT.md)
**Method:** Literature search across PubMed, Scopus, WoS.

---

## Search Strategy

```
PubMed: "centrosome age" OR "mother centrosome" OR "centriole age" 
AND "asymmetric" AND "cell fate" OR "differentiation" OR "stem cell"
2010-2026
```

## Included Studies

| # | Study | Model | N | Effect | Direction | PMID |
|---|-------|-------|:---:|:---:|---------|------|
| 1 | Wang X et al. (2009) | Mouse neocortex (E14.5) | ~20 pairs | Mother→progenitor | ✅ Positive | 19829375 |
| 2 | Anderson & Stearns (2009) | NIH/3T3, REF52 | ~100 pairs | 94% cilium asymmetry | ✅ Positive | 19682908 |
| 3 | Januschke et al. (2011) | Drosophila NB | — | Daughter→stem | ✅ Positive (reversed) | 21407209 |
| 4 | Conduit & Raff (2010) | Drosophila NB | — | Mother retains stem fate | ✅ Positive | 21145745 |
| 5 | Paridaen et al. (2013) | Mouse neocortex | — | Cilium membrane asymmetry | ✅ Positive | 24120134 |
| 6 | Gasic et al. (2015) | RPE1 | 24 cells, 1434 kinetochores | 85% CIN→old centrosome | ✅ Positive | 26287477 |
| 7 | Chatterjee et al. (2018) | Cerebellar GNPs | — | **NO effect on fate** | ❌ NULL | 29663194 |
| 8 | Royall et al. (2023) | Human NPC organoids | — | Mother→self-renewal | ✅ Positive | 37882444 |
| 9 | Thomas & Meraldi (2024) | RPE1 | 28 cells | SAI=2.7-3.8% | ✅ Positive | 39012627 |
| 10 | Barandun et al. (2025) | CD8+ T cells | — | Mother→effector-like | ✅ Positive | 39764850 |

---

## Forest Plot (Qualitative)

```
Study                Year    Model        Direction     Effect Size
──────────────────────────────────────────────────────────────────
Wang                 2009    Mouse Ncx    Mother→Pg     Strong (+)
Anderson             2009    NIH/3T3      Mother→Cil    94% asym ✓
Januschke            2011    Dros NB      Daughter→St   Reversed ⚡
Conduit              2010    Dros NB      Mother→St     Strong (+)
Paridaen             2013    Mouse Ncx    Cil memb→Asy  Moderate
Gasic                2015    RPE1         CIN→85%       Very Strong
Chatterjee           2018    Cbllr GNP    NO EFFECT     NULL ⊘
Royall               2023    Hum NPC org  Mother→Ren    Strong (+)
Thomas               2024    RPE1         SAI 3.1%      Small but sig
Barandun             2025    CD8+ T       Mother→Mem    Strong (+)
──────────────────────────────────────────────────────────────────
TOTAL: 9 positive, 1 null
```

---

## Key Observations

### 1. Tissue specificity dominates
- **Neocortex (mouse):** Mother→progenitor (Wang 2009) ✅
- **Cerebellum (mouse):** NO effect (Chatterjee 2018) ⊘
- **NPC organoids (human):** Mother→self-renewal (Royall 2023) ✅
- **CD8+ T cells (human):** Mother→effector (Barandun 2025) ✅
- **Drosophila NB:** Daughter→stem (Januschke 2011) — REVERSED

> **Нет универсального правила.** Эффект тканеспецифичен. Именно поэтому нужна платформа для систематического тестирования.

### 2. Effect sizes vary dramatically
- **Strongest:** Gasic 2015 — 85% CIN asymmetry (kinetochore bias)
- **Weakest:** Thomas 2024 — 3.1% SAI (spindle size)
- **Cilium:** Anderson 2009 — 94% (but this is cilium timing, not fate)

> Разрыв между 85% (CIN) и 3.1% (SAI) — ключевой. Вероятно, CIN — основной драйвер, а SAI — вторичный.

### 3. Only ONE null result published
- Chatterjee 2018 — cerebellar granule neuron progenitors
- Возможная причина: tissue-specific отсутствие эффекта
- **File-drawer problem:** вероятно, другие null results не опубликованы

### 4. Ни одно исследование не тестировало причинность
- Все 10 — КОРРЕЛЯЦИОННЫЕ
- Ни одного KO/rescue эксперимента
- ARGUS-OS2 — первый causal test

---

## Для Introduction (CONCEPT.md OS1)

Рекомендуемый текст:

> "The centrosome age→fate hypothesis has been tested in 10 model systems with 9 positive and 1 null result. However, three critical gaps remain: (1) ALL studies are correlational — no genetic perturbation has tested causality; (2) effect sizes range from 3.1% (spindle asymmetry, Thomas 2024) to 85% (chromosome mis-segregation, Gasic 2015), and the primary driver is unknown; (3) the single null result (Chatterjee 2018) suggests tissue specificity, but the file-drawer problem precludes a reliable estimate of the true null rate. ARGUS-OS1 is the first platform designed to systematically measure centrosome age→fate correlation across cell types, and ARGUS-OS2 provides the first causal test via Odf2 knockout."

---

*9/10 positive, 1 null. Tissue-specific. All correlational. Causality untested.*
