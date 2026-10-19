# Contact mechanics and why this is not yet a hand model

Background equation, not implemented contact physics: a basic static Coulomb-friction condition is |F_t| ≤ μF_n, where F_t is tangential force, F_n is normal force and μ is a dimensionless friction coefficient.

Example: supporting 1 N tangential load with μ = 0.5 requires at least 2 N normal force under this idealized condition. Actual grasp stability also depends on contact geometry, torque, compliance and changing surface properties.

**Why learn it:** slip detection has a mechanical purpose. Increasing grip can reduce slip but can also damage an object. Position commands alone do not determine contact force.

The synthetic scalar event is a step transient. The spatial generator is a Gaussian footprint. Neither solves contact deformation, frictional transitions or coupled finger mechanics. There is no justified conversion from synthetic event amplitude to newtons.

**Failure mode:** a detector that recognizes synthetic steps may miss real slip vibration or confuse release with contact. Collect measured force/motion references before using its thresholds on hardware.

**Code boundary:** [generators](../src/tactile_lab/receivers/synthetic.py) and [abstract policy](../src/tactile_lab/control.py). The friction equation is explanatory background only.
