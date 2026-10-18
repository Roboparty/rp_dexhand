# Wilson intervals for proportions

For k successes among n independent binary trials, p_hat = k/n. The Wilson interval uses:

$$c=\frac{\hat p+z^2/(2n)}{1+z^2/n},\quad
h=\frac{z\sqrt{\hat p(1-\hat p)/n+z^2/(4n^2)}}{1+z^2/n}.$$

Report [c−h,c+h], clipped only to probability bounds. Here z ≈ 1.96 corresponds to the conventional approximate 95% score interval.

Example: zero successes in ten trials gives an interval approximately [0,0.278]. Observing zero does not prove the underlying probability is zero. Ten successes give approximately [0.722,1].

**Why used:** a symmetric normal approximation can behave poorly at zero or one. This utility provides bounded uncertainty for future independent success/failure evaluations.

**Implementation status:** the utility and its analytical tests are included; current benchmark tables report event rates without automatically applying Wilson intervals to clustered event observations.

**Assumptions:** binary outcomes and a defensible independent sampling unit. Multiple events from one object may be correlated, so naively treating each as independent can be misleading.

**Code:** [wilson_interval](../src/tactile_lab/evaluation/uncertainty.py). **Source:** [NIST proportion intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm).
