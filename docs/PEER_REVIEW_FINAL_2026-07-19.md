# СВЕРХСТРОГИЙ PEER REVIEW — ARGUS-LP_OS v53

**Комиссия:** Грантовые фонды высшего уровня (ERC, NIH R01, Wellcome Trust, HFSP)
**Дата:** 2026-07-19
**Рецензент:** Экспертная группа по клеточной биологии, микроскопии и открытому оборудованию
**Статус верификации ссылок:** ✅ Все 28 PMID проверены через PubMed. 2 ошибки в PMID исправлены.

---

## ИСПРАВЛЕНИЯ ОШИБОК (КРИТИЧЕСКИ)

| Ошибочный PMID (CONCEPT.md) | Правильный PMID | Статья | Журнал |
|:---|:---|------|------|
| ~~26284603~~ | **26287477** | Gasic I, Nerurkar P, Meraldi P. Centrosome age regulates kinetochore-microtubule stability and biases chromosome mis-segregation | eLife (2015) |
| ~~32111840~~ (Kiepas) | **31988150** | Kiepas A, Voorand E, Mubaid F, Siegel PM, Brown CM. Optimizing live-cell fluorescence imaging conditions to minimize phototoxicity | J Cell Sci (2020) |

> 🔴 **Эти PMID в CONCEPT.md §§0.5, 2 требуют немедленного исправления.**

---

## Общая оценка

| Критерий | Оценка (1-10) | Комментарий |
|----------|:---:|-------------|
| Научная значимость | 8.5 | Вопрос фундаментален. Открытый инструмент — важен. |
| Техническая осуществимость | 7.0 | **Серьёзные риски** по стабильности и валидации. |
| Оригинальность | 8.0 | Единственный открытый комплекс для центросомного трекинга. |
| Методологическая строгость | 7.5 | Хорошая статистика, но слабые места в контролях. |
| Бюджет | 8.5 | $24–27K — сверхконкурентно, но не все риски заложены. |

**Итоговая рекомендация:** **MAJOR REVISION.** Концепция сильна, но для финансирования уровня ERC требуется **экспериментальное доказательство концепции** и **усиление контроля воспроизводимости**. Вероятность прохождения в текущем виде: **низкая** для ERC/HFSP, **средняя** для NIH R21.

---

## 1. КЛЮЧЕВЫЕ НАУЧНЫЕ ТЕЗИСЫ — ПОЛНАЯ ВЕРИФИКАЦИЯ PMID

### 1.1. Thomas & Meraldi 2024 (PMID 39012627) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Journal of Cell Biology 223(8) (2024)
- **Название:** «Centrosome age breaks spindle size symmetry»
- **Ключевые находки:** Spindle Asymmetry Index (SAI) = 2.7 ± 5.5% (n = 28), 3.8 ± 5.6% в момент анафазы. В centriolin−/− RPE1: SAI падает до неотличимого от нуля (0.4 ± 4.7%, P = 0.42). Показано в RPE1, MCF10A, BJ-hTERT. Механизм: Cenexin → Plk1 → перицентрин/γ-тубулин/Cdk5Rap2.
- **Ограничения (честно указанные авторами):** «the functional significance is unclear.» Механизм *in vivo* не проверялся — только фиксированные клетки и FRAP.
- **Вывод:** Ссылка валидна и точно отражает содержание. 3.1% SAI — среднее значение. Ограничение честно указано в CONCEPT.md.

---

### 1.2. Royall et al. 2023 (PMID 37882444) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** eLife 12:e83157 (2023). PMCID: PMC10629821. **Рецензированная статья, НЕ препринт.**
- **Авторы:** Royall LN, Machado D, Jessberger S, Denoth-Lippuner A. Laboratory of Neural Plasticity, University of Zurich.
- **Ключевые находки:** Наследование старой центросомы → самоподдержание стволовых свойств в NPC. Использован RITE-метод (рекомбинационно-индуцированный обмен меток) для датировки центросом в человеческих органоидах. Ninein KD нарушает асимметрию.
- **Вывод:** Ссылка валидна. **Проект переводит этот феномен из 3D органоидов в 2D культуру** — рискованная, но осознанная адаптация (Pilot NPC с Go/No-Go критерием ≥60%).

---

### 1.3. Fuentealba et al. 2008 (PMID 18511557) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Proc Natl Acad Sci USA 105(22):7732-7737 (2008)
- **Авторы:** Fuentealba LC, Eivers E, Geissert D, Taelman V, De Robertis EM. HHMI/UCLA.
- **Ключевые находки:** Асимметричная сегрегация фосфо-β-катенина (pSmad1GSK3, pSmad1MAPK) и полиубиквитинированных белков → перицентросомальное накопление в одной из дочерних клеток. В Cos7: асимметричный ответ на BMP7. γ-тубулин распределяется симметрично.
- **Вывод:** Ссылка валидна. **Критическое замечание:** CONCEPT.md честно указывает: «HYPOTHESIZED differential Wnt signalling» и «transcriptional consequences NOT tested in human cells.» Это правильно.

---

### 1.4. Valdes Michel & Phillips 2025 (PMID 39813084) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Mol Biol Cell 36(3):ar25 (2025). PMCID: PMC11974967.
- **Авторы:** Valdes Michel MF, Phillips BT. University of Iowa.
- **Ключевые находки:** SYS-1/β-catenin inheritance and regulation by Wnt signaling during asymmetric cell division. C. elegans. DENDRA2-фото-конверсионный метод.
- **⚠️ КРИТИЧЕСКОЕ ЗАМЕЧАНИЕ:** C. elegans и человек имеют принципиально разные Wnt-сигнальные пути на уровне центросомных механизмов. CONCEPT.md справедливо помечает: «C. elegans. NOT human — do not cite as human mechanism.» Но в §0.5 сказано: «shows analogous mechanism in C. elegans» — слово «analogous» оправданно, но ссылка воспринимается рецензентом как слабое обоснование для человеческой биологии.

---

### 1.5. Tateishi et al. 2013 (PMID 24189274) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** J Cell Biol 203(3):417-425 (2013)
- **Авторы:** Tateishi K, Yamazaki Y, Nishida T, Watanabe S, Kunimoto K, Ishikawa H, Tsukita S. Osaka University.
- **Ключевые находки:** Два типа аппендиксов (дистальные DA и субдистальные SA) формируются разными доменами Odf2. Делеция Δ4/5 → DA+SA− (дистальные есть, субдистальных нет). Делеция Δ6/7 → DA+SA+. KO → DA−SA−. Ультраструктурная томография (UHVEMT).
- **⚠️ КРИТИЧЕСКОЕ ЗАМЕЧАНИЕ ДЛЯ ФАЗЫ 2:** Все эксперименты Tateishi 2013 выполнены на **клетках мышиной F9**, не на человеческих RPE1. Перенос на человеческие клетки требует заново валидировать конструкции. Это не «инжиниринг 6–8 недель» — это **риск неработоспособности конструкций** в человеческой системе. CONCEPT.md §5 упоминает этот риск, но не закладывает время на валидацию.

---

### 1.6. Anderson & Stearns 2009 (PMID 19682908) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Curr Biol 19(17):1498-1502 (2009)
- **Авторы:** Anderson CT, Stearns T. Stanford University.
- **Ключевые находки:** 94% асимметрия роста цилии между дочерними клетками: старая центросома → более ранний и длинный цилиум. Сыворотка 0.5% → усиление асимметрии. NIH/3T3 и RPE1. **Это фундаментальная работа — эталонный результат, на котором строится проект.**
- **Вывод:** Ссылка валидна.

---

### 1.7. Barandun et al. 2025 (PMID 39764850) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Cell Reports 44(1):115127 (2025)
- **Авторы:** Barandun N, Meier B, Stehli G, Gräbnitz F, Zangger N, Oxenius A. ETH Zürich.
- **Ключевые находки:** При асимметричном делении CD8+ T-клеток материнская центросома → эффекторная судьба (НЕ память). Два метода анализа распределения центросом. Ninein как ключевой маркер.
- **Вывод:** Ссылка валидна. В CONCEPT.md корректно: «mother→effector (не memory).» **Важное дополнение:** Barandun 2025 — это ПЕРВОЕ прямое доказательство, что наследование центросомы ФУНКЦИОНАЛЬНО влияет на судьбу в первичных человеческих клетках. Это сильнейший прецедент для проекта.

---

### 1.8. Gasic et al. 2015 (PMID 26287477) — ✅ ПОДТВЕРЖДЕНО (PMID ИСПРАВЛЕН)

- **Журнал:** eLife 4:e07909 (2015). PMCID: PMC4579388.
- **Авторы:** Gasic I, Nerurkar P, Meraldi P. University of Geneva.
- **Ключевые находки:** Центросомный возраст регулирует стабильность кинетохор-микротрубочек. **85% отстающих хромосом остаются на стороне старой центросомы.** Cenexin-зависимый механизм. 1434 кинетохоры в 6 независимых экспериментах.
- **Вывод:** Ссылка валидна. **PMID в CONCEPT.md §0.5 должен быть исправлен с 26284603 на 26287477.**

---

### 1.9. Wang et al. 2009 (PMID 19829375) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Nature 461(7266):947-955 (2009)
- **Авторы:** Wang X, Tsai JW, Imai JH, Lian WN, Vallee RB, Shi SH. MSKCC.
- **Ключевые находки:** Asymmetric centrosome inheritance maintains neural progenitors in the neocortex. E14.5 кортекс мыши. Материнская центросома остаётся в пролиферирующем прогениторе.
- **Вывод:** Ссылка валидна. Фундаментальная работа.

---

### 1.10. Yamashita et al. 2007 (PMID 17255513) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Science 315(5811):518-521 (2007)
- **Авторы:** Yamashita YM, Mahowald AP, Perlin JR, Fuller MT. Stanford.
- **Ключевые находки:** Первая демонстрация: материнская центросома → стволовая клетка в Drosophila germline. Только 50–60% GSC мечены GFP-PACT.
- **Вывод:** Ссылка валидна. Foundational work.

---

### 1.11. Chatterjee et al. 2018 (PMID 29663194) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Cerebellum 17:685-691 (2018)
- **Авторы:** Indian Institute of Science.
- **Ключевые находки:** В клетках-предшественниках гранулярных нейронов мозжечка (cGNPs) **нет** корреляции между наследованием центросомы и судьбой клетки. Null-результат.
- **Вывод:** Ссылка валидна. Честно указан как «Scenario C» в CONCEPT.md §0.3. Это **усиливает научную честность**, но также ослабляет универсальность гипотезы.

---

### 1.12. Januschke et al. 2011 (PMID 21407209) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Nature Communications 2:243 (2011)
- **Авторы:** Januschke J, Llamazares S, Reina J, Gonzalez C. IRB-Barcelona.
- **Ключевые находки:** Drosophila neuroblasts retain the DAUGHTER centrosome. Дочерняя центросома → стволовая клетка. Инверсия по сравнению с млекопитающими (Wang 2009, Royall 2023). Фото-конверсия PACT-d2Eos.
- **Вывод:** Ссылка валидна. Ключевой прецедент для тканеспецифичности.

---

### 1.13. Conduit & Raff 2010 (PMID 21145745) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Curr Biol 20(24):2187-2192 (2010)
- **Авторы:** Conduit PT, Raff JW. Oxford.
- **Ключевые находки:** Cnn dynamics drive centrosome size asymmetry → daughter centriole retention in Drosophila neuroblasts. Материнская центросома организует больше PCM → остаётся в стволовой клетке.
- **Вывод:** Ссылка валидна.

---

### 1.14. Ishikawa et al. 2005 (PMID 15852003) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Nature Cell Biology 7:517-524 (2005)
- **Авторы:** Ishikawa H, Kubo A, Tsukita S, Tsukita S. Kyoto University.
- **Ключевые находки:** Odf2 (cenexin) — scaffold-белок дистальных/субдистальных аппендиксов. Odf2−/− F9 клетки: нет аппендиксов, нет цилий. Цикл не нарушен. Экзогенный Odf2 восстанавливает цилиогенез. «Odf2 is indispensable for the formation of distal/subdistal appendages and the generation of primary cilia.»
- **Вывод:** Ссылка валидна.

---

### 1.15. Paridaen et al. 2013 (PMID 24120134) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Cell 155(2):333-344 (2013)
- **Авторы:** Paridaen JTML, Wilsch-Bräuninger M, Huttner WB. MPI-CBG Dresden.
- **Ключевые находки:** Asymmetric inheritance of centrosome-associated primary cilium membrane directs ciliogenesis after cell division. Ninein как ключевой маркер.
- **Вывод:** Ссылка валидна.

---

### 1.16. Tozer et al. 2017 (PMID 28132826) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Neuron 93(3):542-551.e4 (2017)
- **Авторы:** Tozer S, Baek C, Fischer E, Goiame R, Morin X. IBENS Paris.
- **Ключевые находки:** Mindbomb1 (Mib1) ко-локализуется асимметрично с центриолярными сателлитными белками PCM1 и AZI1 у дочерней центриоли в интерфазе. Notch-зависимая асимметричная судьба нейральных прогениторов.
- **Вывод:** Ссылка валидна. **Критически важный механизм:** Mib1-PCM1-Notch ось связывает центросому с Notch-сигналингом. Это один из немногих молекулярных механизмов, напрямую связывающих центросомную асимметрию с судьбой.

---

### 1.17. Zhao et al. 2025 (PMID 41315244) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Nature Communications 16(1):10728 (2025). PMCID: PMC12663461.
- **Ключевые находки:** PCM1 coordinates centrosome asymmetry with polarized endosome dynamics to regulate daughter cell fate. PCM1-Dlic1-Par3 ось.
- **Вывод:** Ссылка валидна. Работа 2025 года — самая свежая в области. Подтверждает PCM1-центросомную ось в судьбе клетки.

---

### 1.18. Nayak & Radha 2020 (PMID 32371504) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** J Cell Sci 133(11):jcs243113 (2020)
- **Ключевые находки:** C3G (RAPGEF1) локализуется на материнской центриоли cenexin-зависимым образом. C3G depletion → снижение cenexin. Регуляция дупликации центросомы и длины цилии.
- **Вывод:** Ссылка валидна. **Важно для проекта:** C3G — ещё один cenexin-зависимый регулятор. Подтверждает, что Cenexin — не пассивный маркер, а активный организатор сигнальных комплексов.

---

### 1.19. Goutas & Trachana 2021 (PMID 34630857) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** World J Stem Cells 13(9):1177-1196 (2021)
- **Тип:** Review.
- **Ключевые находки:** Обзор: центросомы стволовых клеток. Асимметрия, дифференцировка, самообновление, первичная цилия.
- **Вывод:** Ссылка валидна.

---

### 1.20. Киепас 2020 (PMID 31988150) — ✅ ПОДТВЕРЖДЕНО (PMID ИСПРАВЛЕН)

- **Журнал:** J Cell Sci 133(4):jcs242834 (2020)
- **Авторы:** Kiepas A, Voorand E, Mubaid F, Siegel PM, Brown CM. McGill University.
- **Название:** «Optimizing live-cell fluorescence imaging conditions to minimize phototoxicity.»
- **Замечание:** Это ОБЩАЯ работа по минимизации фототоксичности. Не содержит специфических данных о 850 нм непрерывном облучении 48 часов. Для обоснования безопасности IR нужно искать дополнительные источники.
- **Вывод:** Ссылка релевантна для общей методологии, но НЕ ДОСТАТОЧНА для обоснования безопасности 48-часового 850 нм облучения RPE1. **PMID в CONCEPT.md §2 должен быть исправлен с 32111840 на 31988150.**

---

### 1.21. Reina & Gonzalez 2014 (PMID 25047620) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Phil Trans R Soc B 369:20130466 (2014)
- **Тип:** Review.
- **Название:** «When fate follows age: unequal centrosomes in asymmetric cell division.»
- **Вывод:** Ссылка валидна.

---

### 1.22. Chen & Yamashita 2021 (PMID 33435817) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Open Biol 11:200314 (2021)
- **Тип:** Review.
- **Название:** «Centrosome-centric view of asymmetric stem cell division.»
- **Вывод:** Ссылка валидна.

---

### 1.23. Loncarek et al. 2008 (PMID 18297061) — ✅ ПОДТВЕРЖДЕНО

- **Журнал:** Nat Cell Biol 10:322-328 (2008)
- **Название:** «Control of daughter centriole formation by the pericentriolar material.»
- **Ключевые находки:** Абляция дочерней центриоли → материнская формирует новую дочернюю. PCM контролирует формирование центриоли.
- **Вывод:** Ссылка валидна. Используется для обоснования контроля Centrin1-GFP.

---

### 1.24. HDAC6 обзор (PMID 40167251) — ✅ ПОДТВЕРЖДЕНО (НО СЛАБАЯ ССЫЛКА)

- **Журнал:** Advanced Science (2025). PMCID: PMC12140351.
- **Тип:** Review.
- **Название:** «Histone Deacetylase 6 (HDAC6) in Ciliopathies: Emerging Insights and Therapeutic Implications.»
- **⚠️ КРИТИЧЕСКОЕ ЗАМЕЧАНИЕ:** Это обзорная статья. **PubMed search: 0 результатов для HDAC6i + Odf2 KO.** Обзор не содержит экспериментальных данных о rescue Odf2−/− через HDAC6i. CONCEPT.md §5 использует эту ссылку как основание для HDAC6i — **это слабое обоснование.** Рекомендация: заменить на Tateishi 2013 (PMID 24189274).

---

## 2. МЕТОДОЛОГИЧЕСКИЙ АНАЛИЗ — СЛАБЫЕ МЕСТА

### 2.1. Центросомный возраст vs. Cenexin-интенсивность — КРИТИЧЕСКАЯ НЕДООПРЕДЕЛЁННОСТЬ

**Проблема:** Cenexin (Odf2) — не просто маркер возраста. Это **активный структурный и сигнальный белок:**

- Nayak & Radha 2020 (PMID 32371504): C3G локализуется на cenexin-зависимым образом. C3G depletion → ↓cenexin → нарушение дупликации центросомы и длины цилии.
- Ishikawa 2005 (PMID 15852003): Odf2−/− → нет аппендиксов, нет цилий.
- Thomas & Meraldi 2024 (PMID 39012627): Cenexin → Plk1 → перицентрин/γ-тубулин/Cdk5Rap2 → организация PCM.

**Следствие для проекта:** Если _M_ низкое, это может означать не «молодую центросому», а **функционально дефектную центросому с нарушенной организацией PCM и аппендиксов.** Различие критическое для интерпретации.

**Рекомендация:** В Pilot 1 добавить контроль на **целостность PCM** (перицентрин, γ-тубулин, Cdk5Rap2) и **целостность аппендиксов** (Ninein для SA, Cep164 для DA). Если _M_ коррелирует с фрагментацией PCM или потерей аппендиксов — Cenexin не годится как изолированный маркер возраста. **Рекомендация рецензента остаётся в силе.**

---

### 2.2. 2D NPCs vs. 3D органоиды — НОВЫЕ ДАННЫЕ

Royall 2023 (PMID 37882444) — 3D органоиды. Проект переводит в 2D.

**Новые данные из литературы:**
- Tozer 2017 (PMID 28132826): Mib1-PCM1-Notch ось работает в нейроэпителии мыши *in vivo* — тканевый контекст. В 2D культуре этот механизм может нарушаться.
- Zhao 2025 (PMID 41315244): PCM1-Dlic1-Par3 ось — тоже в тканевом контексте (радиальная глия мыши).

**Риск:** В 2D клетки поляризованы иначе, механические сигналы от матрикса отличаются, межклеточные взаимодействия отсутствуют. Pilot NPC с Go/No-Go (≥60%) — правильный дизайн. Но **для грантового комитета риск 2D-переноса остаётся значительным.**

**Усиление:** Добавить в Pilot NPC: Mib1/PCM1/Notch1 ICD иммунофлуоресценцию. Если Mib1/PCM1 асимметрия детектируется в 2D (как в Tozer 2017 в ткани) — это валидирует модель.

---

### 2.3. N=300 пар — ДОСТАТОЧНОСТЬ И НОВЫЕ ДАННЫЕ

**Расчёт проекта:** HR=1.35, ICC ρ=0.3, 20% аттриция, 30% конкурирующий риск → N=300 → эффективный N≈129 → мощность 82%.

**Анализ рецензента остаётся в силе:**

1. **HR=1.35 не обоснован биологически.** Из Anderson 2009 — 94% асимметрия, но это бинарный исход (цилия есть/нет, 24h). Time-to-event HR для этого перехода не известен.
2. **ICC ρ=0.3 — предположение без данных.** Pilot 3 должен дать реальное ICC.
3. **Адаптивный N не заложен в бюджет (CONCEPT §5: $1,200 на CYTOO ×20).** Если ICC>0.4, потребуется N=600 — дополнительные $600 на CYTOO. Это не учтено в бюджете $27,733.

**Рекомендация:** Добавить строку в бюджет: «CYTOO coverslips ×10 (резерв, для адаптивного N) — $600.»

---

### 2.4. H₂ — «цилиогенез как судьба» — КОНЦЕПТУАЛЬНАЯ ПРОБЛЕМА (УСИЛЕНО)

В RPE1 цилиогенез — выход из клеточного цикла (G0). CONCEPT.md §0.6 признаёт: «RPE1 cilium formation is a cell cycle response (G1→G0), not a terminal fate decision.»

**Дополнительная литература:**
- Paridaen 2013 (PMID 24120134): Цилиарная мембрана наследуется асимметрично, направляя цилиогенез. Но это НЕ судьба в смысле дифференцировки.
- Nayak & Radha 2020 (PMID 32371504): C3G регулирует длину цилии — количественный, не качественный признак.

**Усиление защиты:** H₂ переименовать из «Fate» в «Kinetics» в заявке (в CONCEPT.md уже сделано: «H₂ = kinetics»). Подчеркнуть: RPE1 — валидация платформы, не биологическое открытие.

---

### 2.5. Валидация Centrin1-GFP — ДОПОЛНИТЕЛЬНЫЙ КОНТРОЛЬ

**Проблема:** Указано: «если экспрессия >2× эндогенной → риск.» Но Western blot даёт среднее по популяции.

**Новые данные:**
- Loncarek 2008 (PMID 18297061): Избыточная экспрессия центрина может влиять на дупликацию центриоли.
- Chen & Yamashita 2021 (PMID 33435817): Обзор по центросомам стволовых клеток — подчёркивает важность уровня экспрессии.

**Рекомендация (дополнение):** Добавить single-cell immunofluorescence против эндогенного центрина в Pilot 1 (антитело к центрину-2, которое не cross-react с GFP). Если >20% клеток имеют Centrin1-GFP >2× эндогенного → клон отбраковать.

---

## 3. ТЕХНИЧЕСКИЕ РИСКИ — УСИЛЕНИЕ

### 3.1. Стабильность 72 часов при 60×/1.2 NA WI

**Дополнительная литература:**
- Collins 2020 (PMID 32499936, Biomed Opt Express 11:2447-2460, ref #15): OpenFlexure с водной иммерсией — стабильность <5 µm/24h в температурно-контролируемой среде. **Но Collins использовал 40×/0.95 dry, не 60×/1.2 NA WI.**
- Knapper 2022 (PMID 34625963, J Microsc 285:40-51, ref #16): OpenFlexure v6 с автофокусом.

**Рекомендация остаётся:** Pilot 0.5 с водной иммерсией и средой на 72 часа.

---

### 3.2. Glove-box: новые данные по материалам

**Дополнительная проверка:** ASA (acrylonitrile styrene acrylate) при 37°C/95% RH:
- ASA не гидролизуется при типичных условиях культуральной среды, но длительная экспозиция (72h) может вызывать leaching остаточных мономеров.
- **Рекомендация:** В Pilot 0.5 добавить анализ среды на цитотоксичность (экстракт ASA, 72h, 37°C, тест на RPE1 — MTT/WST-1).

---

### 3.3. IR ночное видение — ПОИСК ДОПОЛНИТЕЛЬНЫХ ИСТОЧНИКОВ

**Kiepas 2020 (PMID 31988150):** Общая методология минимизации фототоксичности. Не содержит данных о 850 нм непрерывном облучении 48 часов.

**НЕОБХОДИМ ДОПОЛНИТЕЛЬНЫЙ ПОИСК:**

Рекомендуется поискать следующие ключевые слова в PubMed/Google Scholar:
- «near-infrared 850 nm long-term live cell imaging phototoxicity»
- «infrared LED cell viability prolonged exposure»
- «RPE1 infrared light stress response»

Если специфические данные отсутствуют (что вероятно — это редко тестируемый параметр), Pilot 0.5 становится НЕ опциональным, а ОБЯЗАТЕЛЬНЫМ экспериментом. Данные будут **оригинальным вкладом** в методологию (публикация: «Safety of continuous 850 nm illumination for 48h live-cell imaging in RPE1»).

---

## 4. СТАТИСТИЧЕСКАЯ СТРОГОСТЬ — ДОПОЛНИТЕЛЬНЫЕ СООБРАЖЕНИЯ

### 4.1. Fine-Gray vs. Cox — ПРАВИЛЬНЫЙ ВЫБОР (ПОДТВЕРЖДЕНО)

Проект использует Fine-Gray для конкурирующих рисков (деление до цилии). Это корректно.

**Проблема:** Fine-Gray несовместим со случайными эффектами (PlateID/IslandID/MotherID) в стандартных R пакетах.

**Решение (дополнительное):**
- R package `frailtypack` (Rondeau et al. 2012, J Stat Softw): поддерживает Fine-Gray с frailty-эффектами.
- Альтернатива: `coxme` с цензурированием → сравнить с Fine-Gray без random effects → sensitivity analysis.

**Рекомендация:** Указать `frailtypack` как метод анализа в Statistical Analysis Plan.

---

### 4.2. Остановка для тщетности — УСЛОВНАЯ МОЩНОСТЬ

Проект: остановка при N=150, если HR<1.15.

**Рекомендация (дополнительно):** Использовать **условную мощность (conditional power)** вместо фиксированного порога HR. Пакет `rpact` (Wassmer & Brannath 2016) или `gsDesign` (Anderson 2021) в R.

- При N=150 вычислить conditional power для HR=1.35 при текущем тренде.
- Если CP<20% → остановка.
- Если CP 20-50% → увеличить N до 400 (адаптивный дизайн с перерасчётом выборки, Cui-Hung-Wang метод для контроля α).

---

## 5. КОНКУРЕНТНАЯ СРЕДА — УСИЛЕНИЕ

### 5.1. Коммерческие альтернативы — ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ

| Система | Cost | 48h автономия | Центросомное разрешение | Открытость |
|----------|:----:|:-----------:|:---------------------:|:--------:|
| LUMICKS C-Trap | ~$200K | ❌ | ❌ (optical tweezers) | ❌ |
| ImageXpress Micro Confocal | ~$150K | ✅ | ⚠️ (40×/0.95, marginal) | ❌ |
| Nikon Ti2-E + OKO Lab | ~$80K | Partial | ⚠️ (60×/1.4 oil — не для живых) | ❌ |
| Incucyte S3 | ~$40K | ✅ | ❌ (10×/20× only) | ❌ |
| **ARGUS-LP_OS** | **$24-27K** | **✅** | **✅ 60×/1.2 NA WI** | **✅ GPLv3/CC-BY-SA** |

**Уникальность — три параметра одновременно:** центросомное разрешение (60×/1.2 NA WI) + 48-часовая автономия (CO₂/O₂/IR) + открытость (GPLv3/CC-BY-SA). **Ни одна коммерческая система не сочетает все три.**

---

### 5.2. Открытость — ПЛАН РАСПРОСТРАНЕНИЯ (УСИЛЕНО)

**Рекомендация:** Добавить в заявку конкретные метрики:
1. OpenFlexure community: 1000+ сборок, 40+ стран, форум (https://openflexure.discourse.group)
2. План: workshop в Georgia (бесплатно для местных исследователей), онлайн-документация с видео
3. Партнёрство: Jessberger Lab (U Zurich, Royall 2023), Meraldi Lab (U Geneva, Thomas & Meraldi 2024) — оба заинтересованы в центросомном трекинге
4. BioImage Archive (CC0) для всех raw данных

---

## 6. ДОПОЛНИТЕЛЬНЫЕ НАХОДКИ (ШИРОКИЙ ПОИСК)

### 6.1. Cenexin — маркер vs. регулятор (МЕТА-АНАЛИЗ)

**Сводка доказательств из литературы:**

| Функция Cenexin | PMID | Доказательство |
|:---|:---:|---|
| **Структурный белок аппендиксов** | 15852003 | Odf2−/− → нет DA/SA, нет цилий |
| **Организация PCM через Plk1** | 39012627 | Cenexin → Plk1 → перицентрин/γ-тубулин |
| **Регулятор стабильности кинетохор-МТ** | 26287477 | 85% lagging chromosomes → old centrosome side |
| **Платформа для C3G** | 32371504 | C3G-cenexin interdependence |
| **Маркер возраста (в паре с Dendra2)** | 19682908, 21407209 | Anderson 2009, Januschke 2011 |

**Вывод:** Cenexin — **одновременно и маркер, и регулятор.** Это делает его использование как ИЗОЛИРОВАННОГО маркера проблематичным. Pilot 1 должен разделить эти роли:
- Маркерная роль: Dendra2 photoconversion (ортогональный метод)
- Регуляторная роль: Odf2 domain deletions (Phase 2)

---

### 6.2. Тканеспецифичность — НОВАЯ ТАБЛИЦА

**Систематический обзор литературы:**

| Система | Организм | Материнская → | PMID | Условия |
|:--------|:--------|:------------:|:----:|:--------|
| Drosophila GSC | Дрозофила | Stem cell | 17255513 | In vivo |
| Drosophila NB | Дрозофила | **Daughter → stem** | 21407209 | In vivo |
| Mouse neocortex RG | Мышь | Progenitor | 19829375 | In vivo |
| Mouse cerebellar GNP | Мышь | **No correlation** | 29663194 | In vivo |
| RPE1 (cilium timing) | Человек | Earlier/longer cilium | 19682908 | In vitro |
| Human NPC organoids | Человек | Self-renewal | 37882444 | 3D organoid |
| Human CD8+ T cells | Человек | Effector (not memory) | 39764850 | In vitro |
| Human NPC (2D) | Человек | **НЕИЗВЕСТНО** | — | Предлагается |

**Вывод:** Нет универсального правила. Тканеспецифичность — не weakness, а **центральный научный вопрос.** ARGUS-LP_OS — первая платформа для систематического кросс-тканевого сравнения.

---

### 6.3. Молекулярные механизмы — ПОЛНАЯ КАРТА

**Три верифицированных механизма:**

| Механизм | PMID | Белки | Клеточный контекст |
|:---------|:---:|-------|-------------------|
| **Spindle asymmetry** | 39012627 | Cenexin→Plk1→pericentrin/γ-tubulin/Cdk5Rap2 | RPE1, MCF10A (человек) |
| **Chromosome segregation** | 26287477 | Cenexin→kinetochore-MT stability | RPE1 (человек) |
| **Notch signalling** | 28132826, 41315244 | Mib1-PCM1-Notch1, PCM1-Dlic1-Par3 | Мышиные NPC, радиальная глия |
| **Protein degradation** | 18511557 | p-β-catenin, polyUb → asymmetric inheritance | ESC, Cos7 (человек, обезьяна) |
| **Wnt (invertebrate)** | 39813084 | SYS-1/β-catenin | C. elegans |

**Только первые два механизма протестированы в RPE1.** Третий (Notch) — в NPC/глии in vivo. Четвёртый (деградация) — в ESC. **ARGUS-LP_OS может впервые протестировать все механизмы в единой системе (RPE1 + NPCs).**

---

## 7. СЛАБЫЕ МЕСТА, НАЙДЕННЫЕ ПРИ ВЕРИФИКАЦИИ

### 7.1. 🔴 Ошибка PMID Gasic (26284603 → 26287477)

В CONCEPT.md §0.5:
```
Pathway C — Chromosome segregation bias (Gasic et al. 2015, PMID 26284603)
```
PMID 26284603 — это CRISPR Cas1 integrase (неправильная статья). Правильный PMID: **26287477**. Необходимо исправить во всех файлах проекта.

### 7.2. 🔴 Ошибка PMID Kiepas (32111840 → 31988150)

В CONCEPT.md §2:
```
Kiepas et al. 2020 (PMID 32111840): 850 nm safe for long-term live-cell imaging.
```
PMID 32111840 — это stem rust resistance in wheat. Правильный PMID: **31988150**.

**⚠️ Дополнительная проблема:** Kiepas 2020 (PMID 31988150) — это ОБЩАЯ методология минимизации фототоксичности через оптимизацию условий флуоресцентной микроскопии. Работа **НЕ содержит специфических данных о безопасности 850 нм непрерывного облучения 48 часов.** Утверждение «850 nm safe for long-term live-cell imaging» не подтверждено этой ссылкой. Требуется отдельный поиск или Pilot 0.5 как оригинальное исследование.

### 7.3. 🟡 HDAC6 обзор (PMID 40167251) — слабая ссылка

CONCEPT.md §5 использует Wang 2025 (PMID 40167251) как обоснование HDAC6i. Это обзор без экспериментальных данных по Odf2. PubMed search: 0 результатов для «HDAC6i + Odf2 KO.» Рекомендация: ссылка должна быть заменена на Tateishi 2013 (PMID 24189274) с явным указанием: «HDAC6i не тестировался на Odf2−/−.»

### 7.4. 🟡 Kiepas 2020 не подтверждает безопасность 850 нм

Как отмечено в §7.2. Необходимо:
1. Провести отдельный поиск литературы по безопасности 850 нм 48-часового облучения
2. Если данные отсутствуют — явно указать в заявке: «Safety of 850 nm continuous illumination >24h in RPE1 has NOT been tested. Pilot 0.5 will provide these data.»
3. Это превращается из риска в **научную новизну:** публикация методологической статьи о безопасности IR.

---

## 8. ИТОГОВАЯ ОЦЕНКА И РЕКОМЕНДАЦИИ

### Сильные стороны

1. **Научный вопрос фундаментален** — центросомный возраст как регулятор судьбы клетки.
2. **Библиографическая база валидна** — 26/28 PMID подтверждены через PubMed, 2 ошибки исправлены.
3. **Открытый инструмент уникален** — единственная платформа, сочетающая центросомный трекинг, 48-часовую автономию и доступность $24-27K.
4. **Честность** — альтернативные гипотезы, план публикации null-результатов, признание ограничений RPE1 как модели.
5. **Статистика** — Fine-Gray, кластеризация, адаптивный дизайн, промежуточный анализ.

### Слабые стороны (блокирующие для ERC/HFSP)

1. **⚠️ Cenexin как маркер возраста — недостаточно валидирован.** Cenexin — одновременно структурный и сигнальный белок (Nayak 2020, Thomas 2024, Gasic 2015). Dendra2 photoconversion в Pilot 1 — правильный контроль, но **экспериментальные данные должны быть получены до подачи гранта.**
2. **⚠️ 2D NPCs — непроверенный перенос.** Royall 2023 — 3D органоиды. В 2D феномен может исчезнуть (Tozer 2017, Zhao 2025 — оба в тканевом контексте).
3. **⚠️ Технические риски недостаточно митигированы** — водная иммерсия (Collins 2020 — на 40× dry, не 60×/1.2 WI), герметичность глов-бокса, IR фототоксичность (Kiepas 2020 не подтверждает 48h безопасность).
4. **⚠️ Отсутствие экспериментального proof-of-concept.** Для гранта уровня ERC нужно **предварительное подтверждение** в лаборатории заявителя — хотя бы 10 пар RPE1 Centrin1-GFP.

### Рекомендации для ревизии

| № | Действие | Приоритет |
|:-:|----------|:---------:|
| 1 | **Исправить PMID:** Gasic 26284603 → 26287477, Kiepas 32111840 → 31988150 | 🔴 Критический |
| 2 | **Pilot 0.5 с водной иммерсией и средой** (не только GFP-бусы) | 🔴 Критический |
| 3 | **Добавить контроль PCM** (перицентрин, γ-тубулин, Cdk5Rap2) + аппендиксов (Ninein, Cep164) в Pilot 1 | 🔴 Критический |
| 4 | **Экспериментальный proof-of-concept:** 10 пар Centrin1-GFP + Cenexin IF до подачи гранта | 🔴 Критический |
| 5 | **Добавить строку в бюджет:** CYTOO coverslips ×10 (резерв для адаптивного N) — $600 | 🟡 Важный |
| 6 | **Усилить план распространения:** партнёрства (Jessberger, Meraldi), OpenFlexure community | 🟡 Важный |
| 7 | **Убрать утверждение «850 nm safe»** из Kiepas 2020 — заменить на: «Pilot 0.5 определит безопасность IR.» | 🟡 Важный |
| 8 | **Заменить HDAC6 обзор (PMID 40167251)** на Tateishi 2013 (PMID 24189274) как обоснование Odf2 domain deletions | 🟡 Важный |
| 9 | **Добавить Mib1/PCM1/Notch1 ICD IF в Pilot NPC** — валидация Notch-оси в 2D | 🟢 Для усиления |
| 10 | **Указать `frailtypack` (R)** для Fine-Gray с random effects | 🟢 Для строгости |
| 11 | **Добавить single-cell IF против эндогенного центрина** в Pilot 1 | 🟢 Для контроля |

---

## 9. ПОЛНЫЙ СПИСОК КЛЮЧЕВЫХ ИСТОЧНИКОВ (ВЕРИФИЦИРОВАННЫХ)

| # | Авторы | Год | Название | Журнал | PMID | Статус |
|:--|--------|:---:|----------|--------|:----:|:------:|
| 1 | Anderson CT, Stearns T | 2009 | Centriole age underlies asynchronous primary cilium growth in mammalian cells | Curr Biol | 19682908 | ✅ |
| 2 | Yamashita YM et al. | 2007 | Asymmetric inheritance of mother vs. daughter centrosome in stem cell division | Science | 17255513 | ✅ |
| 3 | Wang X et al. | 2009 | Asymmetric centrosome inheritance maintains neural progenitors in the neocortex | Nature | 19829375 | ✅ |
| 4 | Januschke J et al. | 2011 | Drosophila neuroblasts retain the daughter centrosome | Nat Commun | 21407209 | ✅ |
| 5 | Paridaen JTML et al. | 2013 | Asymmetric inheritance of centrosome-associated primary cilium membrane directs ciliogenesis | Cell | 24120134 | ✅ |
| 6 | Fuentealba LC et al. | 2008 | Asymmetric mitosis: Unequal segregation of proteins destined for degradation | PNAS | 18511557 | ✅ |
| 7 | Ishikawa H et al. | 2005 | Odf2-deficient mother centrioles lack distal/subdistal appendages | Nat Cell Biol | 15852003 | ✅ |
| 8 | Tateishi K et al. | 2013 | Two appendages homologous between basal bodies and centrioles are formed using distinct Odf2 domains | J Cell Biol | 24189274 | ✅ |
| 9 | Gasic I, Nerurkar P, Meraldi P | 2015 | Centrosome age regulates kinetochore-microtubule stability and biases chromosome mis-segregation | eLife | **26287477** | ✅⚠️ |
| 10 | Thomas A, Meraldi P | 2024 | Centrosome age breaks spindle size symmetry | J Cell Biol | 39012627 | ✅ |
| 11 | Royall LN et al. | 2023 | Asymmetric inheritance of centrosomes maintains stem cell properties in human NPCs | eLife | 37882444 | ✅ |
| 12 | Barandun N et al. | 2025 | Targeted localization of the mother centrosome in CD8+ T cells undergoing ACD | Cell Rep | 39764850 | ✅ |
| 13 | Chatterjee A et al. | 2018 | Centrosome Inheritance Does Not Regulate Cell Fate in GNPs of the Developing Cerebellum | Cerebellum | 29663194 | ✅ |
| 14 | Conduit PT, Raff JW | 2010 | Cnn dynamics drive centrosome size asymmetry to ensure daughter centriole retention in Drosophila NB | Curr Biol | 21145745 | ✅ |
| 15 | Tozer S et al. | 2017 | Differential Routing of Mindbomb1 via Centriolar Satellites Regulates Asymmetric Divisions of Neural Progenitors | Neuron | 28132826 | ✅ |
| 16 | Zhao X et al. | 2025 | PCM1 coordinates centrosome asymmetry with polarized endosome dynamics to regulate daughter cell fate | Nat Commun | 41315244 | ✅ |
| 17 | Nayak SC, Radha V | 2020 | C3G localizes to the mother centriole in a cenexin-dependent manner and regulates centrosome duplication and primary cilium length | J Cell Sci | 32371504 | ✅ |
| 18 | Loncarek J et al. | 2008 | Control of daughter centriole formation by the pericentriolar material | Nat Cell Biol | 18297061 | ✅ |
| 19 | Kiepas A et al. | 2020 | Optimizing live-cell fluorescence imaging conditions to minimize phototoxicity | J Cell Sci | **31988150** | ✅⚠️ |
| 20 | Valdes Michel MF, Phillips BT | 2025 | SYS-1/β-catenin inheritance and regulation by Wnt signaling during ACD | Mol Biol Cell | 39813084 | ✅ |
| 21 | Reina J, Gonzalez C | 2014 | When fate follows age: unequal centrosomes in asymmetric cell division | Phil Trans R Soc B | 25047620 | ✅ |
| 22 | Chen C, Yamashita YM | 2021 | Centrosome-centric view of asymmetric stem cell division | Open Biol | 33435817 | ✅ |
| 23 | Goutas A, Trachana V | 2021 | Stem cells' centrosomes | World J Stem Cells | 34630857 | ✅ |
| 24 | Wang Z et al. | 2025 | HDAC6 in Ciliopathies | Adv Sci | 40167251 | ⚠️ |
| 25 | Gaudin N et al. | 2022 | eLife 11:e72382 | eLife | 35319462 | ✅ |
| 26 | Collins JT et al. | 2020 | Biomed Opt Express 11:2447-2460 | Biomed Opt Express | 32499936 | ✅ |
| 27 | Knapper J et al. | 2022 | J Microsc 285:40-51 | J Microsc | 34625963 | ✅ |
| 28 | Stringer C et al. | 2021 | Cellpose 2.0 | Nat Methods | 33318659 | ✅ |

> **Легенда:** ✅ Подтверждено через PubMed. ⚠️ С оговорками (PMID исправлен / слабая ссылка / требуется дополнительный источник).

---

## 10. ЗАКЛЮЧЕНИЕ

Концепция ARGUS-LP_OS выдающаяся. Библиографическая база в целом валидна (26/28 PMID подтверждены, 2 исправлены). Главные уязвимости — **недостаточная валидация Cenexin как изолированного маркера возраста, непроверенный 2D-перенос NPC фенотипа, и отсутствие экспериментального proof-of-concept.** Все три проблемы решаемы в рамках Pilot 0/1 до подачи гранта.

**Стратегическая рекомендация:** Получить экспериментальные данные (Pilot 0 + Pilot 1 ≥10 пар) до подачи. Это превращает заявку из «амбициозной, но рискованной» в «амбициозную и подкреплённую данными» — разница в вероятности финансирования в разы.

---

*Рецензия подготовлена 2026-07-19. Все PMID верифицированы через PubMed. Исправлены ошибки в PMID Gasic (26284603→26287477) и Kiepas (32111840→31988150).*
