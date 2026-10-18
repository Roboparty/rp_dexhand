# Warmup, resets and state lifecycle

A receiver begins without a baseline. Its first valid sample initializes that baseline; the envelope starts at zero and the noise scale at the fitted/configured value.

The first W valid samples yield no score. Missing samples do not advance the valid-sample count. At 200 Hz, W = 40 corresponds to 0.2 seconds only when all samples are observed.

Example: with W = 2, inputs [0, missing, 1, 1] produce unavailable scores for the first three inputs; the fourth can be scored. The warmup rule is not a guarantee that the estimated state has converged.

**Why used:** startup transients differ from steady operation. Explicitly reporting unavailability is more honest than emitting confident decisions from an uninitialized state.

A new receiver is created for each independent synthetic trial. Consecutive chunks of the same recording must use the same receiver to preserve continuity. Reset is explicit and tested for reproducibility.

**Failure modes:** an event entirely inside warmup can be missed. The built-in generator places events later, so it does not evaluate startup-contact detection. Long missing gaps freeze state; they do not prove that its old baseline remains appropriate.

**Code:** [receiver lifecycle](../src/tactile_lab/receivers/detectors.py).
