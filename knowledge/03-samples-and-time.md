# Samples, timestamps and physical time

A discrete recording is x[n] observed at time t_n. For uniform sampling, t_n = t_0 + n/f_s, where f_s is the sample rate in Hz. The sample interval is Δt = 1/f_s seconds.

At 200 Hz, one sample is 0.005 s = 5 ms. A detector first firing 7 samples after an event onset has a delay of 35 ms. The code converts delay using 1000×(alarm_index − onset_index)/f_s.

The CSV importer estimates the nominal interval from median consecutive timestamp differences and requires agreement within 1% relative tolerance plus 10⁻⁹ s absolute tolerance. This is a data-quality guard, not a sensor synchronization guarantee.

**Why used:** the same numerical filter coefficients behave differently in seconds at different sample rates. A 40-sample warmup means 0.2 s at 200 Hz and 0.4 s at 100 Hz.

**Failure mode:** irregular timestamps cannot be repaired by merely assigning a mean sample rate. Resampling requires an explicit interpolation method and consideration of missing information; this importer rejects irregular recordings instead.

**Code:** [recording importer](../src/tactile_lab/recording.py), [event metrics](../src/tactile_lab/receivers/metrics.py).
