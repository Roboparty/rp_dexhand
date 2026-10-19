# Rectification and the tactile envelope

The receiver takes the magnitude of its baseline residual and smooths it:

$$e_n=e_{n-1}+\alpha_e(r_n-e_{n-1}).$$

The envelope e is in input amplitude units and is nonnegative when initialized at zero. It measures recent magnitude of change; it is not a direct contact force or spectral power.

Example: e_previous = 1, r = 3 and alpha_e = 0.25 produce e_new = 1.5. Reversing a signal's sign does not necessarily change its absolute residual magnitude, so positive and negative transients can trigger similar scores.

**Why used:** rectification avoids cancellation between positive and negative deviations, while smoothing reduces rapidly fluctuating readout noise.

**Failure modes:** motor vibration also creates large absolute residuals. Rectification discards polarity, so the envelope alone cannot tell compressive contact from release or distinguish all physical mechanisms.

The fixed detector thresholds this envelope. The adaptive detector normalizes the same envelope by a changing background scale. The comparison therefore isolates normalization with shared baseline/envelope parameters, not every possible fixed versus adaptive filter design.

**Code:** [detectors](../src/tactile_lab/receivers/detectors.py), [arithmetic tests](../tests/test_receiver_equations.py).
