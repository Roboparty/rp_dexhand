# Adaptive receiver experiment

Run `python -m tactile_lab benchmark --experiment receivers`.

Three causal baselines process the same synthetic scalar recordings: absolute raw input, a fixed-coefficient baseline-removal/envelope filter, and that envelope normalized by a gated adaptive noise scale.

Initial noise is fitted from training background. Candidate thresholds combine training quantiles and uniform amplitude spacing. Validation chooses recall under a 3 false-alarms/minute budget. Test rates can exceed that budget and must remain visible.

Eight scenarios include weak/short events, drift, dropout, motor-only input, no contact and a noise change without a true event. Events are synthetic step transients, not validated slip physics.

Run `--experiment ablation` to compare faster noise tracking, a looser gate and a slower envelope with the baseline settings. This is sensitivity analysis, not test-set tuning.

See [receiver equations](../../knowledge/12-adaptive-normalization.md), [thresholds](../../knowledge/21-thresholds.md) and [event metrics](../../knowledge/23-recall-and-delay.md).
