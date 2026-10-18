# Receiver Ablation Results

Evidence: **synthetic sensitivity analysis**

Configuration hash: `c9b140815d60f5023b0b6529c078e40538d128a12397f949ae4772882a3e769c`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| fixed | 0.7081 | 0.6500 | 1.6155 | 35.0000 |
| adaptive | 2.9879 | 0.8000 | 3.2310 | 5.0000 |
| faster_noise_tracking | 2.1942 | 0.8500 | 1.6155 | 0.0000 |
| looser_gate | 2.2136 | 0.9500 | 3.2310 | 0.0000 |
| slower_envelope | 1.7625 | 0.9000 | 3.2310 | 10.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Variants are reported together; test results do not choose a new winner.
- Each variant independently calibrates its threshold on the same validation trials.
- These changes isolate parameter sensitivity, not biological mechanisms.
- A false-alarm budget on validation is not guaranteed on test.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
