Алексей, привет!
Коротко по изменениям с 14 июля (обновлено 19 июля):
- База: OpenFlexure v6.1.5, напечатан из ASA/PETG. Моторизованный столик, RasPi Camera HQ.
- **v1.0 (текущая, первый грант):** водная иммерсия 60×/1.2 NA, LED 488 nm, CYTOO-островки. Ночное видение (IR 850 nm + Camera NoIR) — стандарт. БЕЗ лазера. БЕЗ микроманипуляторов.
- **v2.0 (будущий грант):** добавляется герметичный перчаточный бокс 50×50×60 см (HEPA H13, UV-C, CO₂/O₂/37°C), фемтосекундный лазер 800 нм, 2× ночные камеры, sCMOS, ящики/полки для реагентов.
- Камера: HQ для пилота → ZWO ASI183MM Pro охлаждаемая (+$1,800) для основного эксперимента.
- Весь микроскоп живёт внутри инкубатора (Binder/Thermo, $6,000) — в v1.0. В v2.0 — собственный glove-box с HEPA H13.
- Jetson Orin NX 16GB + Hailo-8L (13 TOPS) для CellPose + трекинг + Bayesian lineage.
- RasPi 5 для управления моторами, камерой и ночным видением.
- Автофокус: Knapper 2022, контрастный на brightfield, <5 мкм.
- RPE1-hTERT (первичная система). V2: hTERT-NPCs (нейральные прогениторы, ReNcell/Lonza).
- Маркеры: Centrin1-GFP (live, TRACKING) + Cenexin-антитело (фиксация в endpoint, CLASSIFICATION).
- Контроли: DAPT (Notch-ингибитор), RPE1-калибровка (94% асимметрия известна).
- Бюджет v1.0: $19,092 (макс с fallback).
- STL печатаются. Hardware/README, software/README, MAP.md — всё синхронизировано под v49.
- На форуме OpenFlexure — двое интересуются (teh, WilliamW).
- Статья в RSI (Review of Scientific Instruments) на рецензии — задержка с рецензентами.
- GitHub: https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1 — активность пошла.
Если твоему инженеру нужны конкретные STL или спецификации — скину.
