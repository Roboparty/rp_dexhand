# Recording contract

CSV replay accepts `timestamp_s,value`. Timestamps are monotonic seconds, finite, strictly increasing and uniformly spaced within 1%. Values are finite numbers or empty cells for missing data; infinity is rejected. Supply units and `measured` or `synthetic` explicitly on the CLI.

The replay command writes scores, not calibrated event decisions. Its sample-based filter parameters must be reconsidered for a different sample rate. It never resamples silently and never opens hardware interfaces.

For research evaluation, also keep session/object/sensor IDs, sensor coordinates, calibration version, source revision, event intervals, independent labeling method, synchronization uncertainty and sample-rate metadata. Split entire sessions and objects. Keep large measured datasets outside Git and record content hashes. Do not treat this example schema as proof that real measurements exist.

Example:
```csv
timestamp_s,value
0.000,0.10
0.005,0.12
0.010,
0.015,0.11
```

## Included example

[example-synthetic.csv](example-synthetic.csv) contains 240 samples at 200 Hz. A 10 Hz sinusoid of amplitude 0.05 is combined with a unit step during [0.5,0.7) seconds. Samples 130 and 131 are missing. Values are arbitrary units. This is a mathematical teaching signal, not a physical slip recording.
