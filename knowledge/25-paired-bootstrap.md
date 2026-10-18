# Paired comparisons and bootstrap uncertainty

Compare models on identical trials. Define d_i = e_candidate,i − e_baseline,i. Their paired mean difference is d_bar = Σ_i d_i/N.

The bootstrap repeatedly samples N trial differences with replacement and computes each resampled mean. The 2.5th and 97.5th percentiles form the reported percentile interval. The pathway benchmark uses 2,000 replicates with a recorded seed.

Example: candidate errors [2,3,4] and baseline [1,2,3] yield differences [1,1,1]. Every bootstrap mean is 1, so the interval is [1,1]. Pairing removes variation shared by the same test cases.

**Why used:** trial difficulty can vary strongly. Comparing paired differences is more informative than comparing unrelated groups when models see identical data.

**Assumptions:** resampled units represent independent trials. The contact generator assigns one independent synthetic session/object per trial. For real repeated measurements from one object, resample appropriate clusters instead of treating frames as independent.

**Failure modes:** an interval over a small synthetic distribution does not cover modeling bias or transfer to hardware. A degenerate zero interval can arise because two selected models are identical, not because all possible settings are equivalent.

**Code:** [paired_comparison](../src/tactile_lab/pathways/evaluation.py), [generic utility](../src/tactile_lab/evaluation/uncertainty.py).
