# ARGUS-OS1

ARGUS is an open microscopy platform for tracking centrioles in living embryos.

**The question:** does a centriole's pedigree — the sequence of division orientations (∥ or ⟂) it went through — predict whether it will be kept or eliminated?

We test this in C. elegans. It's the only organism where we know the complete cell lineage (959 cells), every division axis, and every cell's fate. Kalbfuss & Gönczy (2023) showed that ~88% of cells lose their centrioles during embryogenesis. Only 68 cells keep them. We know exactly which ones. What we don't know is whether the path the centriole took to get there matters.

Centriole segregation is stochastic (Gönczy & Balestra, 2023). This is good — it means any correlation we find between pedigree and fate cannot be a segregation artifact.

## The hardware

| Version | What | Budget |
|:---:|------|:---:|
| V0 | Minimal — stock OpenFlexure (Alex's suggestion) | ~$930 |
| V6 | Dry 40×/0.75 | $3-4K |
| V7 | Water immersion 60×/1.2 NA, local AI | ~$15K |
| **V8** | **Light-sheet. All new, best components. LLSM equivalent.** | **~$83,000** |

ARGUS V8 costs 14 times less than a lattice light-sheet microscope ($500K) and delivers comparable SNR for C. elegans embryos. It's the only open platform with both 3D time-lapse and centriole tracking.

## The bigger picture

```
OS1 — measure centriole pedigrees + fate in C. elegans (this project)
OS2 — test convergence: different pedigrees → same fate?
OS3 — build progenitor maps as graphs with genetic networks

MCARA — centriole counter reset → totipotency from any cell
         ARGUS V8 provides the platform for this.
```

## Key numbers

- 959 cells in C. elegans, all fates known (Sulston & Horvitz, 1977)
- ~88% eliminate centrioles during embryogenesis (Kalbfuss & Gönczy, 2023)
- 68 cells retain them
- Centriole segregation is stochastic (Gönczy & Balestra, 2023)
- Pedigree threshold: <30° = ∥, >60° = ⟂

## References

Sulston & Horvitz (1977) PMID 838129 | Kalbfuss & Gönczy (2023) PMID 37256957 | Gönczy & Balestra (2023) PMID 36988082 | Anderson & Stearns (2009) PMID 19682908 | Yamashita et al. (2007) PMID 17255513 | Januschke et al. (2011) PMID 21407209 | Wang et al. (2009) PMID 19829375 | Magescas & Feldman (2025) preprint | Erpf & Mikeladze-Dvali (2020) | Das (2021)

---

*Jaba Tqemaladze. Georgia Longevity Alliance. 2026-07-21.*
