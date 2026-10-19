# Synthetic contact generator and its assumptions

At sensor position p_i, a generated contact centered at c has noiseless amplitude:

$$s_i=a\exp\left(-\frac{\|p_i-c\|^2}{2w^2}\right).$$

Here p_i, c and width w are in mm; amplitude a and readings are in a.u. The squared-distance ratio is dimensionless.

Example: one width away from the center, the amplitude is a·exp(−1/2) ≈ 0.607a. Two widths away it is approximately 0.135a. The default generator samples widths from 5 to 12 mm and amplitude from 0.8 to 1.2 a.u.

Readout noise is added independently, then selected channels are marked missing. Conditions cycle through clean, noisier readout, one missing sensor and one-quarter missing sensors. No graph determines the generated target or footprint.

**Why used:** known ground truth permits exact localization error and controlled failures.

**Limits:** real elastomer deformation, friction, shear, contact area, hysteresis and sensor saturation are not modeled. Random target positions are not a model of a user's grasp distribution.

**Code:** [contact synthetic data](../src/tactile_lab/pathways/synthetic.py).
