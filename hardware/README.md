# ARGUS-OS1 Hardware

**Status:** 🟡 V6 = OpenFlexure v6.1.5 being assembled by Alex (Tbilisi).

## V6 (OS1) — Current Build
| Component | Spec | Status |
|-----------|------|--------|
| Frame | OpenFlexure v6.1.5 | 🔵 Assembly |
| Stage | Sangaboard X-Y motors | 🔵 |
| Objective | 40×/0.75 NA Dry | 🔵 |
| Camera | Raspberry Pi HQ Camera | 🔵 |
| Compute | Jetson Orin NX | 🔵 |
| Climate | HEPA H13 incubator | 🔵 |

## V7 (OS2) — Planned
| Component | Spec | Budget |
|-----------|------|:---:|
| Objective | 60×/1.2 NA WI | ~$15K |
| Camera | sCMOS (Hamamatsu ORCA-Fusion BT) | ~$25K |
| Compute | Jetson AGX Orin 64GB | ~$2K |
| Lasers | 405/488/561/640 nm | ~$5K |
| Microfluidic | Embryo loading/unloading | ~$3K |

## Planned Subdirectories
- `openflexure/` — OpenFlexure modifications
- `enclosure/` — Glove-box (FreeCAD)
- `optics/` — Optical path, filter cube
- `electronics/` — Schematics (KiCad), BOM
- `lasers/` — Laser safety & integration

## Кинематика стадии и сэмплинг (18 ноя 2026)

> Источник: `docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`; источники — PMID 42960477, PMID 42644580, PMID 42800763.

| Параметр | Значение | Статус |
|---|---|---|
| ROM стадии (проект) | 12.5 мм | паспорт OFM |
| ROM стадии (измерено, 2026) | **11.4 ± 0.4 × 11.4 ± 0.5 мм** (Chisholm et al., doi 10.1111/jmi.70192) | ✅ рецензируемо; у нас не измерено → TODO F5 |
| Сэмплинг 40×/0.75 dry + Pi HQ (pitch 1.55 µm) | 38.8 нм/px (в пределах нашего требования ≤100 нм/px) | расчёт |
| Сэмплинг 60× + Pi HQ | 25.8 нм/px, но поле 72 µm при 2800 px → 45 800 тайлов на 10×10 мм | расчёт; **60× на HQ для OS1 не берём** |
| Поле тайла 40× | 54 µm (1400 px) / 109 µm (2800 px) — режим `full` обязателен | форум (⚠️ не проверено у нас) |
| Overlap | 0.15 ровные слайды; 0.35–0.5 неровные (время и фотодоза растут) | практика форума |
| EDOF/фокус-стекинг на платформе | возможно, BOM ≈$300, complex wavelet резче Sobel/variance (doi 10.1111/jmi.70161) | ✅ рецензируемо |
| Обязательный гейт перед ML | стандартизация µm/px + цветокоррекция (doi 10.1016/j.ijgc.2026.104993) | ✅ рецензируемо |
