# Sangaboard firmware v1.0.4 — `nano.hex`

Официально собранный артефакт (не наша сборка). Заливается на Arduino Nano в workaround-электронике.

| Поле | Значение |
|---|---|
| Файл | `nano.hex` (Intel HEX, 42 048 байт) |
| Версия (строка в ELF) | **Sangaboard Firmware v1.0.4** |
| Источник | GitLab `openflexure/sangaboard/sangaboard-firmware`, пайплайн **2052089147** (ref `release`, 2025-09-21), job **11430994239**, артефакт `artifacts.zip` → `builds/nano.hex` |
| Прямая ссылка | https://gitlab.com/openflexure/sangaboard/sangaboard-firmware/-/jobs/11430994239/artifacts/download |
| sha256 | `dc6066ed124b686118591e48fe9f9c1053036e62d010c1beb392a868be3c36f7` |
| sha256 (nano.elf) | `48af471c9c41026566fd74049279d7d462bc887a2f0021e3eaffb3ceefff875d` |
| Проверено 18 ноя 2026 | скачано, распаковано, sha256 и версия сверены; строка версии найдена в `nano.elf` |

## Заливка

**Windows (AVRDUDESS v2.20, по MR `openflexure-microscope` !553):** preset `Arduino Nano (ATMega328P)` → выбрать COM-порт → Flash = этот `.hex` → **Program**.

**Linux / Raspberry Pi (avrdude, по тому же MR):**
```bash
avrdude -c arduino -p m328p -P /dev/ttyUSB0 -b 57600 -U flash:w:nano.hex:a
```
(в тексте MR стоит `-m 328p` — это опечатка, у avrdude часть задаётся `-p`; baud 57600 = старый бутлоадер/клоны CH340,
для нового бутлоадера официального Nano — **115200**, официальный Nano в MR не проверен.)

## Лицензия
Прошивка Sangaboard распространяется как открытое ПО (см. LICENSE в репозитории `sangaboard-firmware`).
Файл хранится локально как удобный офлайн-артефакт; в публичный git не коммитится (см. `.gitignore`).
