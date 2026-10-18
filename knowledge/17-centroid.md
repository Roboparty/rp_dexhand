# Contact localization by weighted centroid

Given sensor positions p_i in mm and readings x_i, define nonnegative weights w_i = max(x_i,0) for observed channels and zero for missing channels. Then:

$$\hat p = \frac{\sum_i w_i p_i}{\sum_i w_i}.$$

Example: weights [1,3,0] at [(0,0),(10,0),(0,10)] give (7.5,0) mm. The result lies in the convex hull of contributing sensor positions.

**Why used:** the centroid is a simple shared decoder with no learned parameters. Keeping it fixed makes the graph comparison easier to interpret.

**Assumptions:** a single dominant contact creates a positive footprint. This decoder does not identify multiple separate contacts. For two equal contacts it can return their midpoint, even if no object touches that point.

**Failure modes:** truncating a footprint at patch edges biases the centroid inward; negative noise is clipped while positive noise contributes; dropout changes the available spatial support. A zero total weight yields no estimate, represented internally by NaNs and externally by a null estimate plus a failure flag.

**Code:** [localize](../src/tactile_lab/pathways/filtering.py), [localization tests](../tests/test_localization.py).
