# Residuals, RMSE and calibration limitations

For reference y_i and prediction y_hat_i, residual r_i = y_i − y_hat_i. Calibration reports RMSE = sqrt(Σ_i r_i²/N), in the same units as y.

Example: residuals −1, 0 and 1 N give RMSE = sqrt(2/3) ≈ 0.816 N. This is an in-sample fit error. It is not the uncertainty of a future force reading and is not a guarantee that the sensor is accurate to ±0.816 N.

To assess repeatability, apply the same reference load several times. To assess drift, repeat across time or temperature. To assess hysteresis, compare readings at the same load approached from increasing and decreasing loads. These are distinct experimental questions; one RMSE does not replace them.

**Why used:** residuals reveal where a simple calibration stops representing the instrument.

**Failure mode:** fitting and judging on the same few points can hide nonlinearity. Hold out reference loads and repeat mounting sessions before using physical force thresholds.

**Implementation status:** gain, offset, raw range and training RMSE are implemented. Hardware drift and hysteresis measurements remain data-collection work.

**Code:** [calibration](../src/tactile_lab/calibration.py). **Related:** [calibration model](05-linear-calibration.md).
