# Glossary

| Term | Meaning here | Units or caution |
| --- | --- | --- |
| Sensor | A channel producing an observation | Synthetic channels are not actual instruments |
| Calibration | Empirical map from raw readings to reference quantity | Gain and offset carry units |
| Bias | Systematic deviation | Different from variance |
| Noise scale | Tracked absolute residual magnitude | Not automatically standard deviation |
| Drift | Slow change of baseline | Can mimic gradual contact |
| Hysteresis | Different output at the same input depending on prior trajectory | Not modeled by a single line |
| Adjacency | Matrix of graph connections | Dimensionless weights |
| Degree | Sum of incident edge weights | Count for unit-weight graphs |
| Laplacian | Degree matrix minus adjacency | Encodes graph differences |
| Diffusion | Convex mixture with observed-neighbor averages | Can blur a real peak |
| Pathway | Synthetic column-prioritized graph | Not verified biological anatomy |
| Centroid | Positive weighted average of positions | mm |
| Residual | Difference from prior baseline | Input units |
| Envelope | Smoothed absolute residual | Input units, not power |
| Adaptive score | Envelope divided by prior noise scale | Dimensionless |
| Causal | Uses no future samples | Must preserve prefix outputs |
| Warmup | Valid samples withheld from scoring at startup | Count and implied time |
| Refractory interval | Minimum spacing between accepted alarm onsets | Samples |
| Event | Labeled interval to detect | Half-open sample interval |
| Recall | Fraction of events detected | Dimensionless; null without events |
| False-alarm rate | Alarms outside events per observed background minute | alarms/min |
| Detection delay | First matched alarm minus event start | ms; conditional on detection |
| Coverage | Fraction of observations or decisions available | Report with performance |
| Leakage | Evaluation information entering fitting/selection | Can occur through reused sessions |
| Ablation | Controlled component or parameter change | Same data and evaluation |
| Coherence | Normalized cross-spectral association | Not causality or a field detector |
| Bootstrap | Resampling experimental units | Unit choice matters |
| Provenance | Record of source, configuration and environment | Not proof of validity |
| Synthetic | Produced by the declared generator | Not measured hardware |
| Replay | Offline processing of recorded samples | Does not actuate the hand |
| Grip proposal | Bounded abstract command decision | Not deployed force control |
