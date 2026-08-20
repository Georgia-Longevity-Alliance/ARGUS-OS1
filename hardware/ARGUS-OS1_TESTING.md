# ARGUS-OS1 — Calibration and Testing Instructions

**Version:** 1.0 (2026)
**Applies to:** V6 (OpenFlexure-based) instrument
**Status:** Calibration routines are defined and executable; quantitative results to be reported per the pre-registered protocol (see Section 6 of the metapaper and the CTC benchmark).

---

## 1. Purpose

These instructions give the operator a reproducible procedure to (a) calibrate the instrument and (b) test that the acquisition-and-analysis loop works end-to-end on local compute. They are written so that any builder of ARGUS-OS1 can reproduce the same checks and record the results in a comparable form.

## 2. Tools and consumables

- Fluorescent fiducial beads (e.g., 0.5 µm FluoSpheres 505/515) on a coverslip
- A test sample with a defined fluorophore (for validation of the optics)
- A metric ruler / graticule for field-of-view scaling
- The Jetson Orin NX command shell (on-device)

## 3. Calibration procedures

### 3.1 Camera and optical calibration
1. Mount the camera and objective; centre the camera on the optical axis using the C-mount.
2. Image a graticule to determine the pixel-to-micron scaling at the 40× objective; record the scaling factor per pixel.
3. Verify the field-of-view dimensions and record them.

### 3.2 Focus calibration
1. Bring a fiduciary bead into focus manually; record the focus actuator position as a reference.
2. Execute the automated focus metric (Laplacian variance of a 488 nm frame).
3. Record the focus actuator position that maximizes the metric; this is the reference focus plane.

### 3.3 Positioning repeatability
1. Image a fiduciary field.
2. Command the stage off-target, return to the target, and re-image.
3. Measure the fiduciary displacement (retrace error).
4. Repeat for n ≥ 30 cycles; record mean ± SD and the statistical model.

### 3.4 Environmental calibration
1. Power the PID controller; set the target to 37.0 °C.
2. Record the temperature time-series for 30–60 min; confirm the controller reaches and holds the set point.
3. Record the steady-state temperature deviation.

## 4. Testing procedures

### 4.1 On-device inference test (core loop)
1. Disconnect the instrument network.
2. Start a short acquisition on the test sample.
3. Confirm, from the flight-recorder log, that segmentation, division-event detection, and scheduling all ran on the Jetson module with no network call.
4. Confirm that inferred results are written with logged input frames.

### 4.2 Segmentation and lineage accuracy (CTC)
1. Run the model stack on the public Cell Tracking Challenge fluorescence sequences with published ground truth.
2. Compute DET, TRA, and lineage metrics using the CTC evaluation software.
3. Record the full metric set (not a single headline number).

### 4.3 Division-event accuracy
1. Compare division events against CTC ground truth.
2. Where a biological run is available, compare against independent human annotation.
3. Report Cohen's κ, the confusion matrix, false-positive and false-negative rates.

### 4.4 Focus stability (24 h)
1. Lock focus on a fiduciary; leave the instrument idle for 24 h under nominal climate.
2. Record the focus drift (RMS and maximum) and the sample temperature history over the window.

### 4.5 End-to-end autonomy
1. Run a multi-hour unattended acquisition.
2. Record the event log: operator interventions, autofocus failures, and the fraction of frames retained with usable focus.

## 5. Data recording and reproducibility

- Every test records: date, software version, firmware version, instrument build, and the flight-recorder log.
- Results are reported with sample size, dispersion, and the statistical model used for confidence intervals.
- Raw frames and the reconstructed lineage are exported for deposit in a public archive (Zenodo / BioImage Archive).
- This document is versioned in the repository so that any builder runs the same checks.

## 6. References

- Maška, M., et al. (2014). A benchmark for comparison of cell tracking algorithms. *Bioinformatics, 30*(11), 1609–1617. https://doi.org/10.1093/bioinformatics/btu080
- Stringer, C., et al. (2021). Cellpose: A generalist algorithm for cellular segmentation. *Nature Methods, 18*, 100–106. https://doi.org/10.1038/s41592-020-01018-x
