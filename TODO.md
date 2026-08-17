# TODO — ARGUS-OS1

<!-- lang:ru -->
## 🔴 URGENT — August 2026
- [x] Foresight Package: `grants/foresight_2026-07-31/SUBMISSION_PACKAGE.md`
- [x] OSC Package: `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md`
- [x] GitHub Activity: 2 weeks (Jul 14–28, 200+ commits) ✅
- [x] Fill Foresight Airtable form — submitted Jul 31 ✅
- [x] OSC application on Collective — submitted Aug 1 ✅
- [ ] GitHub Verification (after OSC approval)
- [ ] Upload proposal + budget to Open Collective dashboard (after approval)
- [x] AIS Passport integration for ARGUS-OS1 ✅
- [x] AIS Knowledge Graph: upload centriole claims ✅ (32 claims)
- [x] AIS Marketplace: create listings ✅ (4 listings)
- [x] Indexes: grants/README.md, letters/README.md, hardware/software/firmware README ✅
<!-- /lang:ru -->

## 🔴 Phase 0: Pilot (Aug–Oct 2026)
- [ ] P1: Stochasticity validation — Dendra2 at all stages (10 embryos) — Owner: PI, Deadline: 2026-09-15
- [ ] P2: Phototoxicity ceiling — max duration, duty cycle (5 embryos) — Owner: PI, Deadline: 2026-09-15
- [ ] P3: Photobleaching assay — SAS-4::GFP decay over 3h — Owner: PI, Deadline: 2026-09-20
- [ ] P4: Marker cross-validation — Centrin1-GFP + SAS-4::mCherry (5 embryos) — Owner: PI, Deadline: 2026-09-30
- [ ] P5: Same-type sister pair quantification (Sulston 1983 map) — Owner: PI, Deadline: 2026-09-30
- [ ] P6: Pedigree feature extraction — 5 metrics, independence from cell type — Owner: PI, Deadline: 2026-09-30
- [ ] P7: Heidenhain haematoxylin validation — anti-SAS-4 co-stain — Owner: PI, Deadline: 2026-10-15

## 🟡 Phase 1: Build (Aug–Sep 2026)
- [ ] Build ARGUS V6 = OS1 (OpenFlexure + 40×/0.75 dry + Jetson Orin NX) — Owner: Alex, Deadline: 2026-09-30
- [ ] Build ARGUS V7 = OS2 (60×/1.2 NA WI + sCMOS + phase contrast) — Owner: Alex, Deadline: 2026-12-31
- [x] **Motor release API** — patch ready: `software/microscope/motor_release_sangaboard.patch` + specification `docs/MOTOR_RELEASE_API.md` (Aug 12) ✅
- [x] **Motor release — email to WilliamW sent** (Aug 12, contact@openflexure.org) 📬 — awaiting response / MR
- [ ] **Flat-field calibration for HQ Camera** — verify Pi HQ Camera (IMX477) support in OpenFlexure/libcamera; if absent — implement flat-field correction (lesson from C270 thread, refs/OpenFlexure_forum_uneven_lighting_C270_2026-08-06.md) — Owner: Alex, Deadline: 2026-09-15
- [ ] Triple transgenic strain: Centrin1-GFP + SAS-4::mCherry + histone::BFP — Owner: PI, Deadline: 2026-09-01

## 🟢 Phase 2: Main Experiment (Oct 2026 – Jan 2027)
- [ ] Main: 100 embryos, record pedigrees + fate — Owner: PI, Deadline: 2027-01-15
- [ ] Analysis: mixed-effects logistic regression + Bayesian hierarchical model — Owner: PI, Deadline: 2027-02-15

## 🔵 Grants / Outreach
<!-- lang:ru -->
- [x] Foresight proposal final ($50,050) — sent Jul 31 ✅
- [x] OSC application to Collective — sent Aug 1 ✅
- [x] GitHub activity: commits, photos, issue updates — 200+ commits, Jul 14–28 ✅
<!-- /lang:ru -->
- [x] OSC submission package — `grants/osc_2026-08-01/OSC_SUBMISSION_PACKAGE.md`
- [x] OSC proposal — `grants/osc_2026-08-01/ARGUS_proposal_OSC.md`
<!-- lang:ru -->
- [ ] GitHub Verification (after OSC approval)
- [ ] Upload proposal + budget to Open Collective dashboard (after approval)
<!-- /lang:ru -->
- [x] Pre-submission inquiry to journal editor — Owner: PI

## ⚪ Backlog
- [ ] ARGUS V8 = OS3 (light-sheet upgrade) — Owner: Alex
- [ ] ARGUS V9 = robot hands through glove ports + shared local LLM brain (24/7 servicing) — design: `docs/V9_PROTOTYPE.md` + `docs/STERILIZATION_TRANSFER.md` — Owner: PI
- [ ] Cross-strain validation (N2 + CB4856) — Owner: PI
- [ ] Cross-species validation — Owner: PI
