# Firmware — ARGUS-OS1

## Climate Controller (RasPi Pico W) — v1.0 + v2.0

- **MCU:** Raspberry Pi Pico W
- **Sensors:** SCD41 (CO₂, T, RH), LuminOx O₂ sensor
- **Actuators:** PTC heater (PID), CO₂ solenoid valve, N₂ purge valve
- **Communication:** I²C → RasPi 5, WiFi (MQTT fallback)
- **Language:** MicroPython / C SDK

## Night Vision Controller (RasPi Pico) — v1.0 + v2.0

- **MCU:** Raspberry Pi Pico
- **Output:** PWM → IR LED 850 nm (v1.0: 1× LED, v2.0: 4× LED array)
- **Input:** I²C from RasPi 5 (on/off, brightness 0-100%)
- **Safety:** Software timeout (auto-off after 30 min to prevent accidental continuous IR exposure)
- **Language:** MicroPython

## Laser Shutter Controller (ATtiny85) — v2.0 only

- **MCU:** ATtiny85
- **Input:** TTL trigger from RasPi 5 GPIO
- **Output:** Servo PWM → mechanical shutter (Thorlabs SHB1T)
- **Safety:** Fail-closed (normally closed, opens only on active signal)
- **Response time:** <50 ms

## UV-C Sterilisation Controller (RasPi Pico W) — v2.0 only

- **MCU:** Raspberry Pi Pico W
- **Output:** Relay → UV-C lamp (254 nm)
- **Safety:** Interlock — shuts off when glove-box gloves are in use (IR beam break sensor)
- **Timer:** Pre-programmed sterilisation cycle (e.g., 30 min before experiment start)

## License

All firmware: **GPLv3**
