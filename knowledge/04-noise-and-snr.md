# Noise and signal-to-noise ratio

Write a measurement as x = s + ε, with desired signal s and nuisance ε. Gaussian readout noise in the contact generator has mean zero and configured standard deviation σ in a.u. This is a modeling choice, not a measured noise distribution.

For uncorrelated zero-mean components, a power SNR can be defined as P_s/P_ε. In decibels, SNR_dB = 10 log10(P_s/P_ε). If signal and noise powers are 4 and 1 in squared amplitude units, SNR is 4 or approximately 6.02 dB.

A noise standard deviation and an average absolute residual are different statistics. The adaptive receiver tracks absolute residual magnitude, not variance; its variable named noise must not be read as a calibrated Gaussian σ.

**Why used:** explicit nuisance generation tests whether algorithms improve detection rather than just amplifying everything.

**Failure modes:** correlated motor vibration, clipping, impulsive artifacts and drift violate an independent Gaussian-noise assumption. The receiver generator includes separate nuisance scenarios to expose some of those differences.

**Implementation status:** noise injection and absolute-residual tracking are implemented. A calibrated physical SNR estimator is not.

**Code:** [contact generator](../src/tactile_lab/pathways/synthetic.py), [receiver generator](../src/tactile_lab/receivers/synthetic.py).
