# Localization error and failure penalties

For true contact c and estimate p_hat, Euclidean localization error is e = ||p_hat − c||₂ in mm. Mean error summarizes typical performance; median and 95th percentile describe distribution and tail behavior.

Example: true position (0,0), predicted position (3,4) gives sqrt(3²+4²) = 5 mm. The error is a distance, not squared error and not accuracy percentage.

If no estimate exists, the benchmark assigns the patch diagonal as an explicit penalty and records failure separately. On the default 30×30 mm patch, the diagonal is sqrt(1800) ≈ 42.43 mm.

**Why used:** silently removing failures makes a fragile estimator appear accurate on its surviving cases. A fixed penalty keeps comparisons on the same trials.

**Assumption:** the target lies inside the patch; the diagonal then bounds distances between in-patch points. For targets outside that region, the penalty would need reconsideration.

**Failure mode:** mean error alone can hide dropout failures, hence explicit failure counts and condition-level tables.

**Code:** [evaluate and summarize](../src/tactile_lab/pathways/evaluation.py).
