# Exponential smoothing and time constants

The recursive smoother is:

$$y_n=(1-\alpha)y_{n-1}+\alpha x_n,\qquad 0<\alpha\le1.$$

It uses O(1) state. Expanding the recurrence gives geometrically decreasing weights on older samples. Alpha is dimensionless; y and x have the same units.

Example: with alpha = 0.5, previous y = 2 and new x = 6, updated y is 4. For a constant step input from zero, y_n approaches the new level with an error proportional to (1−alpha)^n.

For uniformly spaced samples, an equivalent exponential time constant is tau = −Δt/log(1−alpha) for alpha below 1. At alpha = 0.15 and 200 Hz, tau is approximately 0.0308 s. Alpha = 1 directly follows the new sample and the logarithmic expression is treated as a limiting case.

**Why used:** the receiver smooths the baseline, absolute residual envelope and adaptive noise scale without accessing future samples.

**Failure modes:** smoothing suppresses rapid changes and introduces delay. A parameter sensible at 200 Hz is not automatically sensible at a different sample rate.

**Code:** [receiver config](../src/tactile_lab/receivers/config.py), [updates](../src/tactile_lab/receivers/detectors.py).
