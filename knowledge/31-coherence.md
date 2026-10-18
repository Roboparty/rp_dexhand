# Magnitude-squared coherence

The offline diagnostic estimates:

$$C_{xy}(f)=\frac{|P_{xy}(f)|^2}{P_{xx}(f)P_{yy}(f)}.$$

P_xx and P_yy are averages of squared windowed FFT magnitudes; P_xy averages cross-products. Shared normalization factors cancel in the ratio. Coherence is dimensionless and ideally between zero and one.

The implementation subtracts each segment's mean, applies a Hann window, uses 50% overlap and requires at least three segments. For identical nonzero sinusoidal signals, coherence at the signal peak is one. If both signals are identically zero, the ratio is undefined and returned as NaN.

**Why used:** coherent motor vibration can explain multichannel agreement that might otherwise be interpreted as useful contact information.

**Failure modes:** high coherence does not establish causation or a particular field mechanism. A single-segment estimate can be misleadingly unity; averaging matters. Overlapping segments are not independent samples for a confidence interval.

This is an offline diagnostic, not a causal detector feature in the current benchmark.

**Code:** [coherence](../src/tactile_lab/spectral.py). **Reference definition:** [SciPy coherence documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.coherence.html).
