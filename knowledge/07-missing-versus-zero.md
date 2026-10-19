# Missing measurements are not zero contact

Zero is an observed numerical value. NaN marks unavailable evidence. Substituting zero for a failed channel incorrectly tells the estimator that the sensor observed no pressure.

For graph neighbors, the masked mean at node i is:

$$m_i = \frac{\sum_j A_{ij} o_j x_j}{\sum_j A_{ij} o_j},$$

where A is nonnegative adjacency and o_j is 1 for observed values and 0 otherwise. The denominator counts weighted observed neighbors only.

Example: neighbors have readings 2 and missing, both with weight 1. Their mean is 2, not 1. If neither is observed, there is no mean. The implementation retains an existing observed self value or leaves a missing node missing.

**Why used:** both pathway diffusion and temporal detectors must avoid inventing evidence during dropouts.

**Important distinction:** graph diffusion can impute a missing channel from neighbors; a receiver receiving a missing scalar sample freezes its state and returns no score. Those operations have different meanings.

**Failure modes:** imputation may spread bias; consecutive missing samples reduce information. The code does not claim that inferred readings are independent measurements.

**Code:** [diffuse](../src/tactile_lab/pathways/filtering.py), [CausalReceiver.update](../src/tactile_lab/receivers/detectors.py).
