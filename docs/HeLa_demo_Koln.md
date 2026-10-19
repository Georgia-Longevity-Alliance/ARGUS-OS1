# HeLa demo for Köln — ARGUS-OS1

**Goal:** two specimens that can be carried in hand luggage. No CO₂ box needed at the meeting. Minimum equipment.

---

## Demo #1 — Mitotic index (fixed cells)

**What we show:** the AI finds mitotic cells and computes the mitotic index in seconds. A technician would take an hour.

### Materials
- HeLa, ~70% confluence
- Coverslips 18×18 or 22×22 mm
- PBS
- 4% paraformaldehyde (PFA) in PBS
- Triton X-100 0.5% in PBS
- BSA 3% in PBS (blocking)
- DAPI (1 µg/ml)
- Anti-α-tubulin-FITC (clone DM1A, 1:200 dilution)
- Mowiol or ProLong Gold (mounting medium)
- Glass slides + nail polish

### Protocol (2 days)

**Day 1:**
1. Plate HeLa on coverslips in a 6-well plate, 24 h before fixation
2. Wash with PBS ×2
3. **Fixation:** 4% PFA, 15 min at room temperature
4. PBS ×3, 5 min each
5. **Permeabilization:** 0.5% Triton X-100, 10 min
6. PBS ×3, 5 min each
7. Blocking: 3% BSA, 30 min

**Day 1 (continued):**
8. Primary: α-tubulin-FITC 1:200 in 3% BSA, 1 h at 37°C (or overnight at 4°C)
9. PBS ×3, 5 min each
10. DAPI 1 µg/ml, 5 min
11. PBS ×2
12. Mount in Mowiol on a glass slide
13. Seal edges with nail polish

**Day 2:**
14. Ready. Store at 4°C in the dark.

### What ARGUS acquires
- Field: 40× objective, DAPI channel + FITC channel
- 5–10 random fields
- Brightfield as backup (if fluorescence is unavailable)

### What the AI reports
- Total cells (by DAPI nuclei)
- Mitotic cells (tubulin-FITC — mitotic spindle)
- Mitotic index = mitotic / total
- **Time:** <1 s per field

---

## Demo #2 — Colchicine (drug response)

**What we show:** HeLa + colchicine → cells arrested in metaphase. Control vs colchicine is visible to the eye. The AI computes the mitotic index: control ~3–5%, colchicine ~15–25%.

### Materials
- HeLa, two 35 mm glass-bottom dishes (#1.5)
- Colchicine, working solution 0.5 µg/ml in medium
- Control: medium without colchicine
- Fixation: as in Demo #1 (PFA, Triton, DAPI, tubulin)

### Protocol (2 days)

**Day 1:**
1. Two HeLa dishes, ~60–70% confluence
2. **Dish A (control):** replace medium with fresh medium
3. **Dish B (colchicine):** replace medium with colchicine 0.5 µg/ml
4. Incubate 4–6 h at 37°C, 5% CO₂

**Day 1 (continued):**
5. Wash with PBS ×2
6. Fixation and staining — identical to Demo #1 (PFA → Triton → tubulin-FITC → DAPI → Mowiol)

**Day 2:**
7. Ready. Store at 4°C in the dark.

### What ARGUS acquires
- Both dishes, DAPI + FITC, 5 fields each
- Brightfield (backup)

### What the AI reports
- Mitotic index: control vs colchicine
- Percentage of cells in metaphase (visible by spindle morphology)
- Bar chart: two bars, the difference is obvious

---

## What is needed for the Cologne demo

| Item | Source |
|:-----|:-------|
| ARGUS V6 (mechanics + camera + Pi) | Alexei brings it |
| Laptop with software | Alexei |
| 2 specimens (Demo #1 and #2) | Prepared in Tbilisi, Jaba carries them |
| DAPI + FITC filters | GFP is on Alexei's list |
| 40× objective | On the list |

If fluorescence is not ready — brightfield: DAPI shows nuclei and chromatin structure. Mitotic cells are morphologically distinct (round, condensed chromosomes).

---

## Backup plan (without fluorescence)

If filters/LED are not ready in time:
- **Brightfield + DAPI nuclei** — the AI counts cells, confluence
- **Scratch assay on live HeLa** — bring a scratched dish, the AI measures the scratch width
- Fixed + crystal violet or Giemsa — mitotic figures are visible without fluorescence

---

*Jaba, 25 July 2026*
