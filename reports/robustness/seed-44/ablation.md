# Receiver Ablation Results

Evidence: **synthetic sensitivity analysis**

Configuration hash: `0e1e7ba75ddadfd64148720eed2c8b59c13b7c37fe8fcdbb28026cdf7d5456ec`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| fixed | 0.7407 | 0.6500 | 2.6925 | 35.0000 |
| adaptive | 3.2847 | 0.9000 | 2.1540 | 10.0000 |
| faster_noise_tracking | 1.8991 | 0.9000 | 3.2310 | 0.0000 |
| looser_gate | 2.8637 | 0.9000 | 1.0770 | 5.0000 |
| slower_envelope | 1.7902 | 0.9000 | 3.2310 | 10.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Variants are reported together; test results do not choose a new winner.
- Each variant independently calibrates its threshold on the same validation trials.
- These changes isolate parameter sensitivity, not biological mechanisms.
- A false-alarm budget on validation is not guaranteed on test.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
