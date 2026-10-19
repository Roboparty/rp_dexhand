# How to read the results without overclaiming

Start with evidence scope, then the primary endpoint, then failure cases. The included reports are synthetic and offline; they are not RP Hand performance measurements.

For Plan A, inspect selected strength. If both graphs choose zero smoothing, their selected predictions are the same. A zero paired difference then says validation preferred no graph mixing in this setup. Read the fixed-strength ablation to see what topology changes when mixing is forced.

For Plan B, inspect recall together with false alarms/min and detected-event latency. A low delay from a detector missing most events is not a reliable fast detector. A validation-constrained rate can exceed its budget on test.

For the combined experiment, examine all four conditions before interpreting the interaction. The maximum-score fusion and synthetic common-mode background can explain changes without any new physical mechanism.

**Why used:** benchmark summaries compress information and can reward selective reading.

**Next experiment:** change the generator seed, then change a prespecified nuisance assumption, then collect calibrated measurements. Each step asks a different generalization question. Do not repeatedly tune on the same reported test cases and describe the result as untouched evidence.

**Code:** [report renderer](../src/tactile_lab/reporting.py), [experiment contract](../experiments/README.md).
