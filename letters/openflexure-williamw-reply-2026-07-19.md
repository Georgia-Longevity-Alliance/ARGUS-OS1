Hi William,

Thanks, this is really useful for our ARGUS-LP_OS build. Three things:

**Material.** We're going with ASA based on O'Toole's preprint. Good to know PET works as a fallback — I've had mixed results with PET warping on large parts. What brand did you use? We'll probably try eSUN ASA first since it's what the York group used.

**Motor heat.** This worries me. We need 48-hour runs at 10-minute intervals. Our plan is TMC2209s with CoolStep plus a MOSFET on Vmot switched by GPIO — cut power entirely between moves. That should keep motors active about 20 seconds per cycle, so maybe 3% duty. Did you try something similar or did you solve it purely in software? Also curious what drivers you were using — if they were A4988s those idle hot even when stationary.

**Water immersion.** This is the scary part. We're planning 60x/1.2 NA water immersion for centrosome resolution. I'm worried about evaporation over 48 hours and condensation on the objective from the humidity inside the glove box. Have you or anyone on the forum tried water immersion in an incubator build? If the water evaporates mid-run the whole experiment is dead.

The Malcolm et al. preprint used 40x/0.95 dry which is sensible — we're trying something riskier with WI. Any thoughts would help.

Cheers,
Jaba

Jaba Tqemaladze
Georgia Longevity Alliance
jaba@longevity.ge
