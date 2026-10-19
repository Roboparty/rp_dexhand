# Combined Results

Evidence: **synthetic 16-channel signals; no physical validation**

Configuration hash: `5a9c78f07b92275af598cb14e54173e9e14d5fa44d89e03232240e3babd3fd24`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| spatial_fixed | 0.5548 | 0.6500 | 3.7695 | 25.0000 |
| spatial_adaptive | 3.2545 | 0.7500 | 2.6925 | 5.0000 |
| pathway_fixed | 0.5483 | 0.6500 | 3.7695 | 25.0000 |
| pathway_adaptive | 3.1244 | 0.8000 | 3.2310 | 10.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Descriptive factorial effects

- pathway_at_fixed: 0.0000
- adaptation_at_spatial: 0.1000
- interaction: 0.0500

## Limitations

- Common-mode background can dominate maximum-channel fusion.
- The spatial event generator is an illustrative perturbation, not contact mechanics.
- Effects are descriptive; no significance claim is made from this small factorial run.
- Thresholds are separately calibrated with equal candidate budgets.
- Graph strength is frozen at 0.35 to isolate graph topology from tuning.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
