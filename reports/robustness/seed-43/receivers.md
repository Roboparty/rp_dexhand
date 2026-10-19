# Adaptive Receiver Results

Evidence: **synthetic step events, not measured physical slip**

Configuration hash: `9b41fcf80c9d9afabd5864f4d01a354615ea8dc59b75f5f429ae42dbf9a7da9b`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| raw | 1.1681 | 0.4500 | 5.9235 | 7.5000 |
| fixed | 0.6552 | 0.7000 | 2.4233 | 45.0000 |
| adaptive | 3.4652 | 0.7000 | 3.5003 | 10.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Test false-alarm rate is measured, not guaranteed by validation calibration.
- Latency is conditional on detection; read it with recall and false alarms.
- One scalar channel per trial; multichannel coherence is not implemented here.
- Warmup and missing samples yield no decisions and reduce observed exposure.
- Fixed mode uses a fixed filter with evolving causal state; it is not a fixed-valued signal.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
