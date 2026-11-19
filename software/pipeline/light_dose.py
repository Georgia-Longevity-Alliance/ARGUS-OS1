"""R8 (2026-11-19) — light-dose budget for live fluorescence imaging.

**The problem this solves.** In our own work "the act of measuring alters what is
observed" is not a quantum slogan, it is a photobleaching/phototoxicity budget:
illumination changes the phenotype we are about to score. The relevant variable is
**radiant exposure (dose)**, not the instantaneous intensity that a UI shows.

**Evidence (verified 2026-11-19):**

* Laissue, Alghamdi, Tomancak et al., "Assessing phototoxicity in live fluorescence
  imaging", *Nature Methods* 14(7):657-661 (2017) — doi:10.1038/nmeth.4344,
  PMID 28661494. Establishes phototoxicity as a systematic confounder of live imaging
  and asks for routine assessment rather than an ad-hoc "keep it dim" rule.
* Alghamdi, Exposito-Rodriguez, Mullineaux et al., "Assessing Phototoxicity in a
  Mammalian Cell Line: How Low Levels of Blue Light Affect Motility in PC3 Cells",
  *Front Cell Dev Biol* 9:738786 (2021) — doi:10.3389/fcell.2021.738786,
  PMID 34977004. Even low blue-light levels measurably change cell motility.

**No threshold is invented here.** A safe dose depends on wavelength, dye, specimen
and duration, and the two papers above do not hand down a universal number. This
module therefore *computes* the dose and compares it to a limit **you supply**
(`--max-j-cm2`). If no limit is supplied it reports and does not judge. That is
deliberate: a fabricated threshold would be worse than no threshold.

Units
-----
irradiance at the sample : I  [mW/cm^2]  (= 1e-3 W/cm^2)
exposure per frame       : t  [ms]      (= 1e-3 s)
radiant exposure         : H = I * t    [J/cm^2]   (W/cm^2 * s)
total dose on one specimen: D = H * frames * z_slices * repeats

1 W/m^2 = 0.1 mW/cm^2, so the two conventions in vendor datasheets differ by 10x —
`to_mw_cm2()` exists so that mistake is made once, in one place, with a test.

CLI
---
  python light_dose.py --irradiance-mw-cm2 0.5 --exposure-ms 50 --frames 400 --z 5
  python light_dose.py ... --max-j-cm2 1.0        # gate: exit 1 if the budget is exceeded
"""

from __future__ import annotations

import argparse
import json
import sys

#: 1 W/m^2 expressed in mW/cm^2.
W_M2_TO_MW_CM2 = 0.1


def to_mw_cm2(value: float, unit: str) -> float:
    """Convert an irradiance to mW/cm^2. Accepts 'mw/cm2', 'w/m2', 'uw/mm2'."""
    u = unit.strip().lower().replace(" ", "")
    if u in ("mw/cm2", "mw/cm^2"):
        return float(value)
    if u in ("w/m2", "w/m^2"):
        return float(value) * W_M2_TO_MW_CM2
    if u in ("uw/mm2", "uw/mm^2", "µw/mm2", "µw/mm^2"):
        # 1 µW/mm^2 = 1e-3 mW / 1e-2 cm^2 = 0.1 mW/cm^2
        return float(value) * 0.1
    if u in ("w/cm2", "w/cm^2"):
        return float(value) * 1000.0
    raise ValueError(f"unknown irradiance unit: {unit!r}")


def exposure_j_cm2(irradiance_mw_cm2: float, exposure_ms: float) -> float:
    """Radiant exposure of one frame: H = I[W/cm^2] * t[s]  ->  J/cm^2."""
    if irradiance_mw_cm2 < 0 or exposure_ms < 0:
        raise ValueError("irradiance and exposure must be non-negative")
    return (irradiance_mw_cm2 * 1e-3) * (exposure_ms * 1e-3)


def total_dose_j_cm2(
    irradiance_mw_cm2: float,
    exposure_ms: float,
    frames: int,
    z_slices: int = 1,
    repeats: int = 1,
) -> float:
    """Dose delivered to one specimen over a full acquisition."""
    for name, value in (("frames", frames), ("z_slices", z_slices), ("repeats", repeats)):
        if value < 0:
            raise ValueError(f"{name} must be non-negative")
    return exposure_j_cm2(irradiance_mw_cm2, exposure_ms) * frames * z_slices * repeats


def budget(
    irradiance_mw_cm2: float,
    exposure_ms: float,
    frames: int,
    z_slices: int = 1,
    repeats: int = 1,
    max_j_cm2: float | None = None,
) -> dict:
    """Compute the dose and, if a limit is supplied, judge it."""
    h = exposure_j_cm2(irradiance_mw_cm2, exposure_ms)
    total = h * frames * z_slices * repeats
    out = {
        "irradiance_mw_cm2": irradiance_mw_cm2,
        "exposure_ms": exposure_ms,
        "exposure_j_cm2_per_frame": h,
        "frames": frames,
        "z_slices": z_slices,
        "repeats": repeats,
        "total_j_cm2": total,
        "max_j_cm2": max_j_cm2,
        "verdict": "reported_only",
        "evidence": "PMID 28661494 (doi:10.1038/nmeth.4344); PMID 34977004 "
        "(doi:10.3389/fcell.2021.738786)",
    }
    if max_j_cm2 is not None:
        if max_j_cm2 <= 0:
            raise ValueError("--max-j-cm2 must be positive")
        out["verdict"] = "pass" if total <= max_j_cm2 else "exceeded"
        out["headroom_factor"] = (max_j_cm2 / total) if total > 0 else float("inf")
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Light-dose budget for live fluorescence acquisitions (R8)."
    )
    p.add_argument("--irradiance", type=float, required=True,
                   help="irradiance at the sample, in --unit")
    p.add_argument("--unit", default="mw/cm2",
                   choices=["mw/cm2", "w/m2", "uw/mm2", "w/cm2"])
    p.add_argument("--exposure-ms", type=float, required=True,
                   help="exposure time per frame, ms")
    p.add_argument("--frames", type=int, required=True, help="frames per acquisition")
    p.add_argument("--z", type=int, default=1, help="z-slices (default 1)")
    p.add_argument("--repeats", type=int, default=1, help="repeats over the experiment")
    p.add_argument("--max-j-cm2", type=float, default=None,
                   help="your own measured-safe limit; without it the result is only reported")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    a = p.parse_args(sys.argv[1:] if argv is None else argv)

    irr = to_mw_cm2(a.irradiance, a.unit)
    res = budget(irr, a.exposure_ms, a.frames, a.z, a.repeats, a.max_j_cm2)

    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"irradiance        : {irr:g} mW/cm^2  (from {a.irradiance:g} {a.unit})")
        print(f"exposure / frame  : {res['exposure_j_cm2_per_frame']:.3e} J/cm^2")
        print(f"acquisition       : {a.frames} frames x {a.z} z x {a.repeats} repeats")
        print(f"TOTAL DOSE        : {res['total_j_cm2']:.3e} J/cm^2")
        if a.max_j_cm2 is None:
            print("verdict           : reported only (no --max-j-cm2 supplied; "
                  "no threshold is invented)")
        else:
            print(f"verdict           : {res['verdict'].upper()} vs {a.max_j_cm2:g} J/cm^2")

    return 0 if res["verdict"] in ("pass", "reported_only") else 1


if __name__ == "__main__":
    raise SystemExit(main())
