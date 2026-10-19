# False alarms and observed background exposure

False-alarm rate is F/T_bg, where F counts alarm onsets outside event intervals and T_bg is observed background duration in minutes.

The exposure denominator excludes labeled event samples and unavailable scores, including warmup and missing measurements. At sample rate f_s, N observed background samples correspond to N/(60 f_s) minutes.

Example: three false alarms during 90 observed background seconds give 2 false alarms/min. If half a nominal 90-second recording is missing, three alarms give 4/min on the 45 observed seconds.

**Why used:** comparing raw alarm counts across recordings with different durations or missingness is misleading.

**Failure mode:** a detector can withhold decisions and reduce coverage. Therefore observed sample counts remain in per-trial results. No available exposure produces a null rate; it is not evidence of zero false alarms.

The current rate treats every observed non-event sample as background, including residual response after an event ends. That makes event-boundary definitions consequential.

**Code:** [metrics](../src/tactile_lab/receivers/metrics.py). **Related:** [missing data](07-missing-versus-zero.md), [warmup](29-warmup-and-reset.md).
