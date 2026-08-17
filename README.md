# ARGUS-OS1

ARGUS is an open microscopy platform for tracking centrioles in living embryos.

**The question:** does a centriole's pedigree — the sequence of division orientations — predict whether it will be kept or eliminated?

We test this in C. elegans. It's the only organism with a complete cell lineage (558 cells at hatching, 959 total in adult), every division axis, and every cell's fate. Kalbfuss & Gönczy (2023) showed ~88% of cells lose centrioles during embryogenesis: 41 proliferating + 20 intestinal + 7 terminally differentiated = 68 cells retain them. Centriole segregation is stochastic at 4-cell stage (Gönczy & Balestra, 2023) — **Pilot validates stochasticity at ALL stages.**

**Pedigree features:** 5 quantitative metrics per centriole — fraction of ∥ divisions, mean 3D angle change, angle variance, orientation switches, cumulative angular path.

**Primary test:** within-type pedigree comparison. Plan A: sister-cell pairs. Plan C: within-cell-type comparison if pairs < 40. N = 100 embryos.

## Hardware

| Version | What | Budget |
|:---:|------|:---:|
| V0 | Bare OpenFlexure — no AI, no fluorescence. Proof of mechanics. | ~$930 |
| **V6** | **OS1: OpenFlexure + Camera HQ + Jetson Orin NX + Dry 40×/0.75. Local AI — CellPose + tracking + lineage on edge hardware.** | **~$3-5K** |
| **V7** | **OS2: 60×/1.2 NA WI + sCMOS + phase contrast + Jetson AGX + microfluidic** | **~$126,000** |
| V8 | OS3: V7 upgrade — light-sheet + fs-laser + tweezers + manipulators | +~$141K (HW) |
| V9 | OS1-3 upgrade: robot hands through glove ports + shared local LLM brain (24/7) | +~$22K to V8 (V9-Full base) |

## OS1 → OS2 → OS3

| Stage | Hardware | Budget | Goal |
|:---:|------|:---:|------|
| **OS1** | V6 | ~$3-5K | Local edge-AI platform. OpenFlexure + Jetson Orin NX + Dry 40×. Graphics-capable AI service on dedicated hardware. |
| **OS2** | V7 | ~$126K | Core science. 60× WI + sCMOS + microfluidic. Main experiment (N=100). |
| **OS3** | V8 | +$141K | Full platform. Light-sheet + fs-laser + tweezers. |

## V9 — Autonomy Layer (Robot Hands + Shared Local LLM Brain)

V9 is an autonomy layer that applies to **every OS stage** — it turns ARGUS into a self-servicing laboratory: robotic hands operate through the glove ports instead of human hands (24/7), and an external LLM brain runs on the same local host that controls the micromanipulators and micro-robots inside the enclosure. Consumables and spare parts are sterilized outside and enter through a dedicated transfer box.

| Variant | Stage | Robot hands | LLM brain | Transfer box | Budget |
|---------|:---:|-------------|-----------|--------------|:---:|
| **V9-Lite** | OS1 | 1 arm (optional, if glove-box) | Jetson Orin NX small models + shared lab host | V6-TRANSFER (optional) | ~$5-7K |
| **V9-Standard** | OS2 | 2 arms | Jetson AGX + shared host | V7-TRANSFER | ~$11-13K |
| **V9-Full** | OS3 | 2 arms | Mac Studio 192GB, 70B models | V8/V9-TRANSFER + VHP | ~$22.4K (base); ~$34.6K incl. sterilization |

- Design: [`docs/V9_PROTOTYPE.md`](docs/V9_PROTOTYPE.md)
- Sterilization & transfer-box SOPs (V7/V8/V9): [`docs/STERILIZATION_TRANSFER.md`](docs/STERILIZATION_TRANSFER.md)

## References

Sulston & Horvitz (1977) PMID 838129 | Sulston et al. (1983) PMID 6684600 | Kalbfuss & Gönczy (2023) PMID 37256957 | Kalbfuss, Berger & Gönczy (2023) PMID 37414202 | Gönczy & Balestra (2023) PMID 36988082 | Anderson & Stearns (2009) PMID 19682908 | Erpf & Mikeladze-Dvali (2020) DOI:10.17912/micropub.biology.000286 | Balestra et al. (2015) PMID 25892868 | Yamashita et al. (2007) PMID 17255513 | Januschke et al. (2011) PMID 21407209 | Wang et al. (2009) PMID 19829375 | Coffman et al. (2016) PMID 27733624 | Kalbfuss & Gönczy (2023) PMID 37963546 | Croisier et al. (2025) PMID 40475707 | Lu & Roy (2014) PMID 25360893

---

*Jaba Tqemaladze. Georgia Longevity Alliance. 2026-07-22. v186.*
