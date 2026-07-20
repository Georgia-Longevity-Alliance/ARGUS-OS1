# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in ARGUS-OS1 (especially laser safety for v2.0, network-exposed control systems, or night vision IR exposure), please report it privately:

- **Email:** jaba@longevity.ge
- **PGP:** [key to be added]

Please do NOT open a public issue for security vulnerabilities.

## v1.0 — No Laser

ARGUS-OS1 v1.0 does NOT use lasers. The only light sources are:
- **LED 488 nm** — fluorescence excitation, ≤5% power, ≤200 ms per frame. Class 1M (eye-safe under normal use). Standard lab LED safety: avoid direct eye exposure, use enclosure.
- **IR LED 850 nm** — night vision illumination. Class 1 (eye-safe). Invisible to naked eye but harmless at the power levels used (~50 mW).

No laser safety officer required for v1.0.

## v2.0 — Laser Safety (planned)

ARGUS-OS1 v2.0 adds a femtosecond laser (NIR 800 nm, Class 3B). Hardware safety measures include:
- OD6+ laser safety goggles required during operation
- Mechanical beam shutter (fail-closed)
- Interlock on glove-box door (laser shuts off if box is opened)
- 4-layer optical filtering (OD6+ filters, OD4+ dichroic, shutter, notch)
- Laser safety officer required
- IRB protocol for laser use on biological samples

**Never bypass safety interlocks.**

## Network Security

- Microscope control interface should NOT be exposed to the public internet
- Use SSH tunneling or VPN for remote access
- Default passwords must be changed on first boot
