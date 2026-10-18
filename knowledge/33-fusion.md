# Maximum-channel fusion and common-mode interference

The combined benchmark applies a receiver independently to each smoothed sensor channel, then takes the maximum available score:

$$z_{fused}[n]=\max_{i\in O_n} z_i[n].$$

O_n contains channels with available scores. If none is available, the fused score is unavailable rather than negative infinity.

Example: scores [0.5,2.0,missing] yield 2.0. This favors sensitivity to a localized response without requiring all sensors to agree.

**Why used:** it is a simple common fusion rule across graph/receiver conditions, so different fusion methods do not confound the first comparison.

**Failure modes:** one noisy channel can dominate; adding more channels can increase false alarms. Correlated motor vibration can affect many channels together. A maximum is not an estimate of total force and does not measure coherence.

The threshold is calibrated on the fused training/validation scores. A single-channel threshold is not silently reused. The two graphs have identical sensor positions and edge budgets, but different connectivity and therefore different effects on outliers.

**Code:** [_scores](../src/tactile_lab/combined.py).
