# Combined Results

Evidence: **synthetic 16-channel signals; no physical validation**

Configuration hash: `07f1a3a96d3d8724cd04a1d61cfc28ef91b3b9fb2c05840d6faa9c1301f388cb`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| spatial_fixed | 0.6580 | 0.6500 | 2.6925 | 35.0000 |
| spatial_adaptive | 3.1852 | 0.8500 | 2.1540 | 10.0000 |
| pathway_fixed | 0.6314 | 0.6500 | 3.2310 | 35.0000 |
| pathway_adaptive | 3.1533 | 0.8500 | 2.1540 | 15.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Descriptive factorial effects

- pathway_at_fixed: 0.0000
- adaptation_at_spatial: 0.2000
- interaction: 0.0000

## Limitations

- Common-mode background can dominate maximum-channel fusion.
- The spatial event generator is an illustrative perturbation, not contact mechanics.
- Effects are descriptive; no significance claim is made from this small factorial run.
- Thresholds are separately calibrated with equal candidate budgets.
- Graph strength is frozen at 0.35 to isolate graph topology from tuning.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
