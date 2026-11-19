# ARGUS-OS1 Firmware

**Status:** 🟡 Planned.

## Components
| Device | Firmware | Purpose |
|--------|----------|---------|
| Sangaboard | Custom (WilliamW 2026) | X-Y stage + motor release |
| RasPi Pico W | MicroPython/C | Climate PID controller |
| Laser driver | TTL/PWM | 405/488/561/640 nm control |
| IR LED array | GPIO | Night vision illumination |
| UV-C lamp | Relay | Sterilisation |
| HEPA fan | PWM | Air filtration |
| Interlock sensors | GPIO | Laser safety cutoff |

## Motor Release (WilliamW, 2026)
Sangaboard firmware already supports `motor_release()` command. Needs REST API exposure.

## Safety
- Laser interlock: HARDWARE circuit (cannot be overridden by software)
- Temperature cutoff: hardware fuse at 50°C + software limit at 39°C
- Emergency stop: physical button → all motors + lasers off

## Версии: сервер ↔ прошивка (из форума, 2026-11-15…18)

> Источник: `docs/ARGUS_Forum_Intel_OFM_2026-11-18.md`. Диагноз ⚠️ — не проверено у нас.

| Сценарий | Что известно | Статус |
|---|---|---|
| OpenFlexure OS **v2.11** + скетч Nano из инструкций по workaround | работает (WilliamW, 2026-11-15) | ⚠️ со слов, не проверено |
| OpenFlexure OS **v3.0.0-beta** + скетч Nano из инструкций | OpenFlexure Connect **ругается на прошивку** (ricardd, 2026-11-15) | ⚠️ наш вероятный случай |
| Sangaboard firmware **v1.0.4** (prebuilt из артефактов пайплайна `OpenFlexure/Sangaboard/sangaboard-firmware`) | заливается через **AVRDUDESS** (avrdude GUI): MCU `ATmega328P` (`-p m328p`), пресет «Arduino Nano», старый бутлоадер; новый бутлоадер — те же настройки, но baud **115200**. У ricardd: моторы и подсветка заработали, скан прошёл (2026-11-17) | ✅ подтверждено двумя людьми; совместимость с v3.0.0-beta **не подтверждена** |

**Правило для V6:** версия сервера и версия прошивки фиксируются в provenance сборки; любая смена любой из них — повторный приёмочный тест (см. `TODO.md` F1–F2). Инструкции по загрузке сейчас переписываются в MR `openflexure-microscope` **!553**.

**Ограничение:** `motor_release()` — уже в прошивке Sangaboard (WilliamW 2026); остаётся выставить в REST API.
