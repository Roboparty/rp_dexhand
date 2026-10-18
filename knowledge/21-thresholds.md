# Threshold selection under a false-alarm budget

An alarm candidate occurs when score > threshold. The threshold has the score's units: a.u. for raw/fixed modes, dimensionless for adaptive mode.

The search combines uniformly spaced amplitude values and quantiles of training scores, plus a high finite candidate. Uniform spacing covers amplitude gaps that quantiles can miss when most samples are quiet. Candidate construction never reads test scores.

Validation retains candidates with false alarms per observed background minute no greater than the configured budget. Among those, it maximizes event recall, then prefers fewer false alarms, lower detected-event delay and a lower threshold.

**Example:** one threshold detects every event but emits 20 false alarms/min; another detects 80% with 2 false alarms/min. Under a 3/min validation budget, only the second is eligible.

**Why used:** raw accuracy over mostly quiet samples can reward a detector that never detects anything.

**Failure mode:** meeting the validation budget does not guarantee meeting it on test. The benchmark reports the test rate explicitly. Its budget is an illustrative operating point, not a hardware safety specification.

**Code:** [threshold_candidates and select_threshold](../src/tactile_lab/receivers/training.py).
