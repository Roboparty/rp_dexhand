# Benchmark Settings

The actual executed settings are serialized into every result JSON, with a SHA-256 configuration hash. Python defaults are authoritative; this table is a reading aid.

| Setting | Default |
| --- | --- |
| Contact patch | 4×4 sensors, 10 mm spacing |
| Graph edges | 24 per nonempty graph |
| Pathway strength candidates | 0, 0.15, 0.35, 0.6 |
| Contact trials | 120 per split |
| Receiver sampling | 200 Hz, 4-second recordings |
| Scalar scenarios | 8 |
| Scalar trials | 8 per scenario per split |
| Combined/ablation trials | 4 per scenario per split |
| Threshold search | 64 amplitude positions + 64 quantiles + high candidate, deduplicated |
| Validation false-alarm budget | 3 per observed background minute |
| Refractory interval | 20 samples, strict separation >20 |
| Warmup | 40 valid samples |
| Combined strength | 0.35, one step |
| Robustness seeds | 42, 43, 44 |
| Bootstrap | 2,000 paired contact-trial resamples |

Training fits the initial noise scale. Validation chooses thresholds or graph strength. Test reports results. Do not revise a setting after reviewing a test outcome and call the same test set untouched. This is a development benchmark, not a preregistered study.

There is no external configuration-file loader in this release; the table is not an executable config. Use the CLI seed/experiment options or the documented Python APIs, and retain generated settings.
