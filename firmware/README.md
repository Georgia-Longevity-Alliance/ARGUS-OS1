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
