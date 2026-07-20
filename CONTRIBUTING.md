# Contributing to ARGUS-OS1

We're building an open-source robotic microscope that watches cells for weeks and tracks centrosome inheritance across divisions. If that sounds like fun, jump in.

## Five ways to help

**Build one.** Print the STLs, wire it up, point it at some cells. Write up what happened — what worked, what broke, what you'd change.

**Improve the hardware.** Got a better LED driver? A more stable autofocus mount? A quieter fan for the incubator? Send a PR to `hardware/`. Include the FreeCAD file and the STL.

**Write some code.** The stack is Python and Rust. Controller code in `software/microscope/`, tracking in `software/tracking/`, night vision in `software/nightvision/`. Pick an open issue or start a discussion.

**Report bugs.** If something breaks, open an issue. Tell us: (1) what happened, (2) what you expected, (3) logs or photos if you have them.

**Share data.** Got lineage tracking data? Drop it in `data/`. CC0, so anyone can use it.

## Getting set up

```bash
git clone git@github.com:Georgia-Longevity-Alliance/ARGUS-OS1.git
cd ARGUS-OS1
pip install -r requirements.txt
```

## Pull requests

1. Fork the repo
2. Branch off main: `git checkout -b my-thing`
3. Commit clearly — say what and why
4. Push and open a PR
5. If CI exists, make it green

## Hardware PRs

- Source files (FreeCAD `.FCStd`) plus exported `.stl` or `.step`
- Print settings: material, nozzle, layer height, infill
- Photos of the printed part if you've got them

## Code of Conduct

[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Short version: don't be a jerk.

## Stuck?

Open a [Discussion](https://github.com/Georgia-Longevity-Alliance/ARGUS-OS1/discussions) or email jaba@longevity.ge.
