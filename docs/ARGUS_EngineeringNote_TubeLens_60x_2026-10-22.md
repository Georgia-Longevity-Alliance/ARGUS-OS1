# ARGUS — Engineering Note: Optical Tube Length / Tube Lens for the 60× Objective on a Custom Frame (OS4)

**Date:** 2026-10-22
**Trigger:** OpenFlexure community threads (2026-10-15): (1) "Scaling optical tube length for 75mm doublet with static 60× air-gap objective" (connor); (2) "Hardware Microscope Stage Controller — joystick + focus" (mcastrog). Both are directly relevant to ARGUS optics and stage UX.
**Source type (honest):** optical engineering fundamentals + manufacturer practice; not primarily biomedical literature (hence no single PMID — see §4).

---

## 1. The 60× objective and tube lens (the connor thread → ARGUS)

**Principle (established optics):**
- Infinity-corrected objectives form the image at infinity; a **tube lens** brings it to focus on the camera/sensor.
- **Effective magnification = f_tube / f_objective.** Manufacturers use a standard tube-lens focal length (commonly ~f=200 mm for major brands, but each vendor has its own standard; the "60×" label assumes the vendor's tube lens).
- **If you substitute a non-standard tube lens** (e.g., a 75 mm doublet) for the vendor's standard, the effective magnification changes: a "60×" objective with a 75 mm tube lens gives 60 × 75/200 ≈ **22.5× effective**. NA and resolution stay set by the objective; the **field of view and tube-lens aberrations** change.
- Consequences for a custom frame: (a) the image circle/field of the tube lens must cover the sensor; (b) aberrations (chromatic, field curvature) depend on the tube-lens design; (c) magnification calibration must be re-measured (this is exactly a V8/metrology item).

**For ARGUS (OS4, centrioles ~250 nm):**
- The 60× water-immersion objective (e.g., Nikon CFI Plan Apo 60×W, f_tube 200 mm) requires the **matching 200 mm tube lens** for the labelled 60× magnification and full NA performance.
- If a compact custom module uses a shorter/other tube lens (e.g., a 75 mm doublet to shrink the body), the engineer must **recalculate effective magnification and re-verify resolution/field/aberrations** on the optical bench (PSF via USAF/beads — the "possible-now" bench measurement).
- Recommendation: keep the manufacturer-standard tube-lens focal length for the chosen 60× objective; only deviate with a documented PSF/magnification calibration.

## 2. Hardware stage controller (the mcastrog thread → ARGUS UX)

- A tabletop hardware controller with **joystick (X-Y) + focus knob** is a practical addition for OpenFlexure-based instruments.
- **For ARGUS:** useful for manual positioning during calibration/metrology (V8), alignment, and sample setup — a manual-override channel complementing the software/AI control. Not a scientific requirement; an ergonomic option.
- The author's offer to contribute to the project aligns with ARGUS's open-source strategy and the Foresight "Nodes community" priority (community contribution strengthens the open-hardware narrative).

## 3. Weak spots / meta

- **Weak spot:** a non-standard tube lens (75 mm doublet) with a 60× objective is tempting for a compact body, but risks reduced effective magnification and uncorrected field aberrations — must be bench-verified before committing the optics.
- **Meta:** ARGUS's custom-frame optics should default to the vendor-standard tube lens; any deviation is a documented, bench-verified exception. The community threads confirm the demand for hardware-control ergonomics and high-resolution static-scan builds — both converging with ARGUS's design space.

## 4. Source honesty

- Tube-lens design, infinity correction, and magnification scaling are **established optical-engineering fundamentals** (manufacturer specifications and optics texts); the biomedical index does not hold a single canonical PMID for this. No PMID is claimed here; the principle is standard practice. Bench verification (PSF, effective magnification) is the evidence ARGUS will produce itself.

---

*Companion: ARGUS_BOM_fibroblasts_OS4_2026-10-22.md (A3/A6 slots), ARGUS_possible_now_cheap_testbed_2026-10-22.md (optical bench), EVIDENCE.md.*
