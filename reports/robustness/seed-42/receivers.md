# Adaptive Receiver Results

Evidence: **synthetic step events, not measured physical slip**

Configuration hash: `d1d85de13281f613ec8259ac81db65f585dc053246572d8de6b267c9da78419e`

| Model | Threshold | Event recall | False alarms/min | Detected median delay (ms) |
| --- | --- | --- | --- | --- |
| raw | 1.0625 | 0.5750 | 11.5778 | 15.0000 |
| fixed | 0.6182 | 0.7000 | 4.3080 | 30.0000 |
| adaptive | 4.9928 | 0.6750 | 4.0388 | 25.0000 |

Latency includes detected events only. Read it alongside recall, missing observations and false alarms. A validation false-alarm budget is not a test-set guarantee.

## Limitations

- Test false-alarm rate is measured, not guaranteed by validation calibration.
- Latency is conditional on detection; read it with recall and false alarms.
- One scalar channel per trial; multichannel coherence is not implemented here.
- Warmup and missing samples yield no decisions and reduce observed exposure.
- Fixed mode uses a fixed filter with evolving causal state; it is not a fixed-valued signal.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
