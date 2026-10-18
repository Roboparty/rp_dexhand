# Units and dimensional analysis

A quantity combines a number and a unit. Coordinates p_i have units mm. Contact amplitudes in the synthetic generator use arbitrary units (a.u.), not newtons. Time in recordings is seconds; event latency in reports is milliseconds.

The centroid is p_hat = Σ_i w_i p_i / Σ_i w_i. Its numerator has units a.u.·mm and denominator a.u., leaving mm. Scaling every weight by the same positive constant leaves the estimate unchanged.

Example: weights 1 and 3 at positions 0 and 10 mm give (1×0 + 3×10)/(1+3) = 7.5 mm. Multiplying weights by 100 still yields 7.5 mm. This invariance does not calibrate the weights into physical force.

An adaptive score e/n divides an envelope by a noise scale in the same units, so its result is dimensionless. A fixed receiver envelope retains the input units. Their thresholds are therefore not numerically interchangeable.

**Why used:** unit tracking catches invalid comparisons and prevents treating simulated amplitude as a physical load.

**Failure mode:** transferring a threshold from volts to ADC counts, or from an arbitrary synthetic scale to newtons, silently changes behavior.

**Code:** [localization](../src/tactile_lab/pathways/filtering.py), [receiver](../src/tactile_lab/receivers/detectors.py).
