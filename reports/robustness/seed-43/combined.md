# Combined Results

Evidence: **synthetic 16-channel signals; no physical validation**

Configuration hash: `8aac4ae6eb8e2cc131905081fdf6dd4854f7bd404d00e5af4d8b8c2464a97390`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| spatial_fixed | 0.5805 | 0.7000 | 4.3080 | 30.0000 |
| spatial_adaptive | 3.1559 | 0.8000 | 1.6155 | 7.5000 |
| pathway_fixed | 0.5545 | 0.7000 | 4.3080 | 30.0000 |
| pathway_adaptive | 2.9846 | 0.8000 | 3.2310 | 7.5000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Descriptive factorial effects

- pathway_at_fixed: 0.0000
- adaptation_at_spatial: 0.1000
- interaction: 0.0000

## Limitations

- Common-mode background can dominate maximum-channel fusion.
- The spatial event generator is an illustrative perturbation, not contact mechanics.
- Effects are descriptive; no significance claim is made from this small factorial run.
- Thresholds are separately calibrated with equal candidate budgets.
- Graph strength is frozen at 0.35 to isolate graph topology from tuning.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
