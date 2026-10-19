# Baseline removal and residual order

Let b_(n−1) be the baseline before seeing x_n. The implementation first computes the absolute residual r_n = |x_n − b_(n−1)|, then updates b_n = b_(n−1) + alpha_b(x_n − b_(n−1)).

The order matters. Computing the residual after the baseline update would shrink it by a factor related to alpha_b.

Example: previous baseline 2, new input 4, alpha_b = 0.5. The residual is 2 and the new baseline is 3. A post-update residual would be 1, a different algorithm. The unit test checks the implemented order.

**Why used:** a slowly moving baseline removes some drift before detection. It allows changes relative to recent context to matter.

**Assumptions:** the desired event changes faster than baseline tracking. A long constant contact will be absorbed into the baseline, so this receiver is a transient-change detector rather than a sustained-contact force estimator.

**Failure modes:** fast baseline adaptation can erase useful events; slow adaptation can leave drift as a nuisance. The initial baseline equals the first valid sample, so an event already present at startup is not independently identified.

**Code:** [CausalReceiver.update](../src/tactile_lab/receivers/detectors.py).
