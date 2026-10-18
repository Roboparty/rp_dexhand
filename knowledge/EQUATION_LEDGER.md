# Equation-to-Code Ledger

| Computation | Equation / rule | Symbols and units | Implementation | Verification |
| --- | --- | --- | --- | --- |
| Linear calibration | y_hat = gx+b | y in selected output unit; g in output/raw | [calibration.py](../src/tactile_lab/calibration.py) | [known gain and range](../tests/test_calibration.py) |
| Calibration RMSE | sqrt(mean(residual²)) | Same units as output | [calibration.py](../src/tactile_lab/calibration.py) | Exact linear example |
| Contact footprint | a exp(-distance²/(2w²)) | a arbitrary; distance,w in mm | [synthetic.py](../src/tactile_lab/pathways/synthetic.py) | [generator tests](../tests/test_contacts.py) |
| Masked neighbor mean | sum(A o x)/sum(A o) | x amplitude; o observed mask | [filtering.py](../src/tactile_lab/pathways/filtering.py) | [missing-data tests](../tests/test_diffusion.py) |
| Diffusion | (1-alpha)x + alpha m | alpha dimensionless | [filtering.py](../src/tactile_lab/pathways/filtering.py) | [maximum principle](../tests/test_diffusion_properties.py) |
| Centroid | sum(w p)/sum(w) | p in mm | [filtering.py](../src/tactile_lab/pathways/filtering.py) | [hand calculation](../tests/test_localization.py) |
| Localization error | norm(estimate-target) | mm | [evaluation.py](../src/tactile_lab/pathways/evaluation.py) | [3-4-5 distance](../tests/test_pathway_scoring.py) |
| Baseline | b + alpha_b(x-b) | Input units | [detectors.py](../src/tactile_lab/receivers/detectors.py) | [arithmetic](../tests/test_receiver_equations.py) |
| Envelope | e + alpha_e(abs(x-b_old)-e) | Input units | [detectors.py](../src/tactile_lab/receivers/detectors.py) | [arithmetic](../tests/test_receiver_equations.py) |
| Adaptive score | e/max(q_old,q_min) | Dimensionless | [detectors.py](../src/tactile_lab/receivers/detectors.py) | Old-noise ordering |
| Noise update | q + alpha_q(r-q), if gate passes | Input units | [detectors.py](../src/tactile_lab/receivers/detectors.py) | [state tests](../tests/test_receiver_missing.py) |
| Alarm | Rising edge above threshold after refractory | Sample index | [metrics.py](../src/tactile_lab/receivers/metrics.py) | [episodes](../tests/test_alarm_episodes.py) |
| Recall | detected/total events | Fraction | [metrics.py](../src/tactile_lab/receivers/metrics.py) | [event tests](../tests/test_event_metrics.py) |
| False alarms | outside-event count / observed minutes | alarms/min | [metrics.py](../src/tactile_lab/receivers/metrics.py) | [exposure](../tests/test_event_metrics.py) |
| Delay | 1000(alarm-start)/f_s | ms | [metrics.py](../src/tactile_lab/receivers/metrics.py) | 10 ms example |
| Paired bootstrap | resampled mean(candidate-baseline) | Endpoint units | [uncertainty.py](../src/tactile_lab/evaluation/uncertainty.py) | [constant difference](../tests/test_uncertainty.py) |
| Wilson interval | score-interval center ± half width | Probability | [uncertainty.py](../src/tactile_lab/evaluation/uncertainty.py) | Boundary cases |
| Laplacian spectrum | eigenvalues(D-A) | Graph weights | [topology.py](../src/tactile_lab/pathways/topology.py) | [component nullity](../tests/test_topology.py) |
| Coherence | abs(P_xy)²/(P_xx P_yy) | Dimensionless | [spectral.py](../src/tactile_lab/spectral.py) | [identical sine](../tests/test_spectral.py) |
| Lag | maximum normalized overlap correlation | Samples | [spectral.py](../src/tactile_lab/spectral.py) | Delayed pulse |
| Fusion | maximum available channel score | Score units | [combined.py](../src/tactile_lab/combined.py) | Shared-trial comparison |
| Factorial interaction | R_PA-R_PF-R_SA+R_SF | Recall difference | [combined.py](../src/tactile_lab/combined.py) | Four-condition results |
| Grip proposal | min(1,current+step) if permitted | Abstract command | [control.py](../src/tactile_lab/control.py) | [guards](../tests/test_control.py) |

The Coulomb-friction relation, biological receptive-field discussion and time-constant interpretation are explanatory background. They do not imply that mechanics, neuroscience or a physical robot has been simulated or validated.
