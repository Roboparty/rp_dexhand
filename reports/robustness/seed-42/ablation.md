# Receiver Ablation Results

Evidence: **synthetic sensitivity analysis**

Configuration hash: `1cfced25753f0c6102da4e8c1b6c64e7342b76bc8f7031d80704b3a87b746ce7`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| fixed | 0.6526 | 0.6500 | 3.7695 | 30.0000 |
| adaptive | 3.0856 | 0.8000 | 4.3080 | 7.5000 |
| faster_noise_tracking | 2.1003 | 0.9000 | 2.1540 | 7.5000 |
| looser_gate | 3.0769 | 0.8000 | 1.6155 | 7.5000 |
| slower_envelope | 1.8922 | 0.8000 | 3.2310 | 15.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Variants are reported together; test results do not choose a new winner.
- Each variant independently calibrates its threshold on the same validation trials.
- These changes isolate parameter sensitivity, not biological mechanisms.
- A false-alarm budget on validation is not guaranteed on test.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
