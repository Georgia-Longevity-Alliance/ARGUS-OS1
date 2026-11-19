# PROVENANCE — ARGUS-OS1 V6 (build record)

> Заполнять при приёмке. Правило проекта: потерянный тег provenance = дефект
> (`EVIDENCE.md` §Epistemic standard, п.2). Любая смена сервера, прошивки, объектива,
> камеры или режима кропа ⇒ повторная приёмка по `docs/ARGUS_OS1_Scan_Acceptance_Runbook_2026-11-18.md`.

## Состав (заполнить датой)

| Поле | Значение | Кто/когда |
|---|---|---|
| OpenFlexure OS (сервер) | `v2.11` (решение 18 ноя; v3.0.0-beta — только после приёмки) | |
| OpenFlexure Connect | | |
| Прошивка Sangaboard / Nano | скетч из инструкций workaround либо **v1.0.4** (AVRDUDESS) | |
| Мотор-контроллер (плата) | Sangaboard / Arduino Nano (workaround) | |
| Объектив | 40×/0.75 dry | |
| Камера | Raspberry Pi HQ (IMX477), кроп | |
| `capture_mode` в scan | должен быть `full` (иначе 1400 px вместо 2800) | |
| `overlaps_xy` | | |
| mpp у образца, нм/px | 38.8 (расчёт: 1.55 µm / 40×) — подтвердить калибровкой | |
| Измеренный ROM (мм) | `measure_rom.py`, метод PMID 42960477 (референс 11.4 ± 0.4) | |
| Дата сборки / приёмки | | |

## Чек-лист приёмки (ссылка)

| # | Критерий | Команда/наблюдение | ✅ |
|---|---|---|---|
| A1 | Connect без предупреждения о прошивке | визуально | |
| A2 | `motor_release()` по REST | вызов API | |
| A3 | Скан проходит QC | `python3 software/pipeline/qc.py scan <DIR>` → PASS | |
| A4 | Тайлы 2800 px, overlap как заявлен | тот же QC | |
| A5 | ROM измерен, внесён в PARAMETERS | `measure_rom.py` | |
| A6 | ≤100 нм/px, бининг ≤2×2 | `qc.py gate` | |
| A7 | Сшивка: швы <1.05, резкость ≥85 % GT | `blend.py` + `evaluate.py` | |
