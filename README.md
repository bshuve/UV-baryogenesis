# UV-baryogenesis
## Repository for code from arXiv:2507.18739

Authors: Tian Dong, Conor M. Floyd, Antonia Hekster, Derek J. Li, Brian Shuve, David Tucker-Smith

### Quantum Kinetic Equations Solver/Results

Run the initialization cells in each Mathematica notebook before solving QKEs or plotting results.

All data from plots in paper are tabulated in separate files in the "results" directory. If you simply want to plot results, find the "Import" command in the appropriate notebook section
and go from there.

If you wish to generate the results for yourself, you can execute the code in each section up to
the "Export" command. 

The code to generate each of the following plots can be found in the corresponding file:

- Fig. 1:    UV-IR comparison-analytic.nb
- Figs. 2-5: uv-qke.nb
- Fig. 6:    uv-qke-leptonZ2V.nb
- Fig. 7:    uv-qke-pertcompare.nb
- Fig. 8:    UV-IR comparison.nb

### Interpolating Functions Used for Reaction Density Integrals

The results of certain integrals used in reaction densities have been pre-calculated, tabulated,
and are then imported in the above notebooks to create interpolating functions.

These tables are provided: pert-chislog.dat, pert-chitlog.dat, and pert-mixed-gammaylog.dat. The code used to generate these tables can be found in: generate-s-and-t-integrals.nb, UV-IR comparison-tablegen.nb

### Power Spectrum Transfer Functions in CLASS

We used CLASS to compute the linear matter power spectrum in UV and IR freeze-in limits of our model. The tabulated DM spectra in each case are provided in DMspectrum-for-CLASS-UV.dat and DMspectrum-for-CLASS-IR.dat. The code used to compute the linear matter power spectrum in CLASS is wdm_UV_IR.py

