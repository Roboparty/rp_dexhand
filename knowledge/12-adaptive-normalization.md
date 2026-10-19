# Adaptive normalization and gated noise updates

The adaptive score is z_n = e_n / max(q_(n−1), q_min), where e is the envelope, q is a tracked absolute-residual scale and q_min prevents division by zero. Both e and q have the same amplitude units, making z dimensionless.

After scoring, update q_n = q_(n−1) + alpha_q(r_n − q_(n−1)) only when e_n < gate × max(q_(n−1), q_min). Otherwise freeze q.

Example: e = 0.3 and previous q = 0.1 yield score 3. A gate of 4 permits a noise update because 0.3 < 0.4. With e = 0.6 it freezes the scale instead. The scale used to produce the score is the previous value, not the new one.

**Why used:** background normalization can let the same dimensionless threshold work over changing noise levels. Gating reduces the chance that a strong event is immediately learned as background.

**Failure modes:** weak events may enter the noise estimate and disappear; persistent interference may keep the gate closed. The gate is a heuristic, not an optimal estimator or a consciousness-receiver mechanism.

**Code:** [receiver](../src/tactile_lab/receivers/detectors.py), [training scale](../src/tactile_lab/receivers/training.py).
