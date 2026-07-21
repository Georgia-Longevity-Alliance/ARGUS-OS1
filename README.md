# ARGUS-OS1

ARGUS is an open microscopy platform for tracking centrioles in living embryos.

**The question:** does a centriole's pedigree — the sequence of division orientations — predict whether it will be kept or eliminated?

We test this in C. elegans. It's the only organism with a complete cell lineage (558 cells at hatching, 959 total in adult), every division axis, and every cell's fate. Kalbfuss & Gönczy (2023) showed ~88% of cells lose centrioles during embryogenesis: 41 proliferating + 20 intestinal + 7 terminally differentiated = 68 cells retain them. Centriole segregation is stochastic (Gönczy & Balestra, 2023) — any pedigree↔fate correlation cannot be a segregation artifact.

**Primary test:** sister-cell pairs. When a cell divides, both daughters start with the same type. One gets the older centriole, one gets the younger. If their centriole fates diverge, pedigree is the explanation.

## Hardware

| Version | What | Budget |
|:---:|------|:---:|
| V0 | Minimal — stock OpenFlexure (Alex) | ~$930 |
| V6 | Dry 40×/0.75 | $3-4K |
| **V7** | **Nikon CFI Plan Apo 60×/1.2 NA WI + Hamamatsu ORCA-Fusion BT + RasPi AI + microfluidic** | **~$35,000** |
| V8 | V7 upgrade: light-sheet + fs-laser + tweezers + manipulators + Jetson AGX | +~$141K (hardware) |

V7 is the OS1 platform. V8 is the OS2/OS3 upgrade — built on V7, not a new build.

## OS1 → OS2 → OS3

```
OS1 (V7, $35K) — measure pedigrees + fate in C. elegans
OS2 (V7→V8, +$141K HW) — test convergence + centriole transplantation
OS3 — progenitor maps as graphs with genetic networks
```

## References

Sulston & Horvitz (1977) PMID 838129 | Sulston et al. (1983) PMID 6684600 | Kalbfuss & Gönczy (2023) PMID 37256957 | Kalbfuss, Berger & Gönczy (2023) PMID 37414202 | Gönczy & Balestra (2023) PMID 36988082 | Anderson & Stearns (2009) PMID 19682908 | Erpf & Mikeladze-Dvali (2020) | Balestra et al. (2015) PMID 25892868 | Yamashita et al. (2007) PMID 17255513 | Januschke et al. (2011) PMID 21407209 | Wang et al. (2009) PMID 19829375 | Coffman et al. (2016) PMID 27733624 | Croisier et al. (2025) PMID 40475707

---

*Jaba Tqemaladze. Georgia Longevity Alliance. 2026-07-21.*
