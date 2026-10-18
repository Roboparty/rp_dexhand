# Linear sensor calibration

A linear calibration predicts reference force y from raw reading x:

$$\hat y = g x + b.$$

Here g has units N/raw-unit and b has units N when the selected output unit is newtons. The fit minimizes Σ_i(y_i − g x_i − b)² over gain g and offset b. The implementation solves the least-squares problem with NumPy rather than explicitly inverting a normal-equation matrix.

Example: raw readings 0, 1, 2 paired with reference forces 1, 3, 5 N yield g = 2 N/raw-unit and b = 1 N. A raw value 1.5 predicts 4 N. Applying the calibration outside the observed raw range is rejected unless explicitly allowed.

**Why used:** raw counts do not intrinsically measure force. A calibration gives them an empirical mapping and an applicability range.

**Assumptions:** the relation is approximately linear over the calibrated range; reference measurements are trustworthy. This basic fit does not model uncertainty in both axes, temperature dependence or hysteresis.

**Code:** [fit_linear](../src/tactile_lab/calibration.py). **Background:** [NIST least squares](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd141.htm).
