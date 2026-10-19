# Adaptive Receiver Results

Evidence: **synthetic step events, not measured physical slip**

Configuration hash: `b823af3543c2fd4fded9505d158f663fa1edf5819b2c6d2f0d993e8afaf77d0b`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| raw | 1.2288 | 0.3500 | 3.7695 | 10.0000 |
| fixed | 0.6269 | 0.7250 | 4.0388 | 35.0000 |
| adaptive | 3.2816 | 0.8500 | 2.6925 | 10.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Test false-alarm rate is measured, not guaranteed by validation calibration.
- Latency is conditional on detection; read it with recall and false alarms.
- One scalar channel per trial; multichannel coherence is not implemented here.
- Warmup and missing samples yield no decisions and reduce observed exposure.
- Fixed mode uses a fixed filter with evolving causal state; it is not a fixed-valued signal.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
