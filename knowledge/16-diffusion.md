# Diffusion, convexity and repeated steps

For an observed node with observed neighbors, the update is x_i' = (1−alpha)x_i + alpha m_i, where m_i is their weighted mean and alpha lies in [0,1].

Both coefficients are nonnegative and sum to one. Therefore the updated value lies between the self value and neighbor mean. With complete finite data, repeated updates cannot create a value outside the original global minimum and maximum.

Example: self 2, neighbor mean 6, alpha = 0.25 gives 3. With the opposite node initially 6 and neighbor 2, its update is 5. Simultaneous updates produce [3,5], not [3,5.25]; the implementation uses the old state for all nodes in a step.

**Why used:** this bounded operation is transparent and has analytical checks.

**Failure modes:** more steps can over-smooth peaks. Row normalization on an irregular-degree graph does not generally preserve the unweighted sum of all sensor readings. Do not call it conservation of total pressure.

The benchmark tunes a single step's strength on validation and also reports a fixed-strength comparison. This lets no smoothing win when smoothing is harmful.

**Code:** [filtering](../src/tactile_lab/pathways/filtering.py), [property tests](../tests/test_diffusion_properties.py).
