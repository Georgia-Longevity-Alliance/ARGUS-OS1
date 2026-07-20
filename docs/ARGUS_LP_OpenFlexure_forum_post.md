**Title:** ARGUS-OS1 — autonomous 24/7 cell lineage tracker on OpenFlexure v6.1.5

**Category:** Build Reports  
**Tags:** live-cell, fluorescence, laser-ablation, climate-control

---

Hi everyone — wanted to share what we're building on top of OpenFlexure.

ARGUS-OS1 is a robotic microscope that watches mammalian cells divide for weeks at a time, tracks who came from whom, and zaps selected cells with a 405 nm laser. It lives in a sealed box at 37°C with HEPA-filtered air, and the whole thing runs unattended.

We chose OpenFlexure because the upright geometry is perfect for water immersion — the 60× objective points down, gravity holds the water column, and the laser comes up through the glass dish bottom. No pumps, no fuss.

Everything is open-source: GPLv3 for code, CC-BY-SA for hardware. V1 build starts this week.

GitHub: https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1

Happy to contribute mods back upstream — laser port, climate controller, whatever's useful.
