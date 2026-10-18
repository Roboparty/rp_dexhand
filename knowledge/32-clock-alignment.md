# Clock alignment and lag estimation

A measured delay between channels may reflect transport or clock alignment rather than a physical propagation mechanism.

The offline lag estimator examines normalized correlations of overlapping portions for integer lags l in a bounded range. It subtracts the overlap means and divides the dot product by the product of vector norms. Positive reported lag means y arrives later than x.

Example: a pulse at index 30 in x and 35 in y gives lag +5 samples. At 200 Hz this corresponds to 25 ms. This does not identify whether the delay came from sensing, buffering or the physical process.

**Why used:** multichannel comparisons require time alignment. A detector cannot infer coherence meaningfully from unrelated clocks.

**Failure modes:** periodic signals can have several equally plausible lags; constant signals contain no identifiable lag and are rejected. The search returns an integer-sample estimate, without sub-sample interpolation or uncertainty.

The estimator reads the complete signals and must not be presented as a real-time causal operation. For deployment, timestamp synchronization and measured acquisition latency are preferable to retroactively aligning labels to improve a score.

**Code:** [estimate_lag](../src/tactile_lab/spectral.py).
