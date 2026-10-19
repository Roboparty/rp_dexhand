# Ablation studies and parameter sensitivity

An ablation changes a defined component while preserving the rest of an evaluation. Here the receiver study compares a fixed baseline, the default adaptive receiver, faster noise tracking, a looser update gate and a slower envelope.

Changing noise_alpha from 0.01 to 0.03 makes the scale respond more rapidly. Changing gate from 4 to 10 permits more residuals into the update. Changing envelope_alpha from 0.15 to 0.05 smooths more slowly. These are different mechanisms, so their results are reported separately.

**Worked example:** for q_previous = 0.1 and residual r = 0.4, a permitted update yields q = 0.103 at alpha = 0.01 or 0.109 at alpha = 0.03. The faster estimate can track interference sooner but may absorb useful events sooner too.

**Why used:** an adaptive receiver is not a single universal technique. Sensitivity can reveal which design choice produces a gain or failure.

Each variant recalibrates its threshold on the same validation set with equal candidate construction. Test results describe sensitivity and do not select a new deployed winner. Doing so would require another untouched evaluation.

**Code:** [ablation study](../src/tactile_lab/ablation.py).
