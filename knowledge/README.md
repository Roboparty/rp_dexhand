# Knowledge Library

This folder explains what the tactile lab computes, why each operation is present, and what the results can support. Start with the evidence boundary; then follow the equations into the code and tests.

## Suggested reading routes

- **First understanding:** 01–08, then 17–24 and 36.
- **Build Plan A:** 13–20, 25, 27, 38 and 40.
- **Build Plan B:** 03–04, 08–12, 20–24, 28–33 and 39.
- **Move toward hardware:** 05–07, 32, 34, 37, the data contract and hardware guides.
- **Research review:** [equation ledger](EQUATION_LEDGER.md), [glossary](GLOSSARY.md), [results guide](36-reading-results.md).

Every implemented equation is linked to source code. Notes explicitly label background equations that are not implemented. These are original explanations and worked examples, not copies of the reading PDFs.

## Chapters

- [Evidence and hypotheses](01-evidence-and-hypotheses.md)
- [Units and dimensional analysis](02-units-and-dimensions.md)
- [Samples, timestamps and physical time](03-samples-and-time.md)
- [Noise and signal-to-noise ratio](04-noise-and-snr.md)
- [Linear sensor calibration](05-linear-calibration.md)
- [Residuals, RMSE and calibration limitations](06-residuals-and-rmse.md)
- [Missing measurements are not zero contact](07-missing-versus-zero.md)
- [Causality and streaming equivalence](08-causality.md)
- [Exponential smoothing and time constants](09-exponential-smoothing.md)
- [Baseline removal and residual order](10-baseline-removal.md)
- [Rectification and the tactile envelope](11-envelope.md)
- [Adaptive normalization and gated noise updates](12-adaptive-normalization.md)
- [Graph representation and edge budgets](13-graphs.md)
- [What the pathway mapping actually means](14-pathway-mapping.md)
- [Graph Laplacian and the implemented diffusion](15-laplacian.md)
- [Diffusion, convexity and repeated steps](16-diffusion.md)
- [Contact localization by weighted centroid](17-centroid.md)
- [Synthetic contact generator and its assumptions](18-contact-generator.md)
- [Localization error and failure penalties](19-localization-error.md)
- [Training, validation and test boundaries](20-validation.md)
- [Threshold selection under a false-alarm budget](21-thresholds.md)
- [Alarm episodes and refractory intervals](22-alarm-episodes.md)
- [Event recall and conditional detection delay](23-recall-and-delay.md)
- [False alarms and observed background exposure](24-false-alarm-exposure.md)
- [Paired comparisons and bootstrap uncertainty](25-paired-bootstrap.md)
- [Wilson intervals for proportions](26-wilson.md)
- [The two-by-two factorial comparison](27-factorial.md)
- [Nuisance controls and alternative explanations](28-nuisance-controls.md)
- [Warmup, resets and state lifecycle](29-warmup-and-reset.md)
- [Fourier representation and spectral resolution](30-fft.md)
- [Magnitude-squared coherence](31-coherence.md)
- [Clock alignment and lag estimation](32-clock-alignment.md)
- [Maximum-channel fusion and common-mode interference](33-fusion.md)
- [Bounded grip proposals and hardware limits](34-control.md)
- [Reproducibility, seeds and artifact hashes](35-reproducibility.md)
- [How to read the results without overclaiming](36-reading-results.md)
- [Contact mechanics and why this is not yet a hand model](37-contact-mechanics.md)
- [Sensing, receptive fields and biological inspiration](38-sensing-and-receptive-fields.md)
- [Ablation studies and parameter sensitivity](39-ablation.md)
- [Connectivity and the graph spectrum](40-graph-spectrum.md)

## How to study

Recalculate each worked example by hand. Find the corresponding unit test and change one input. Predict what should happen before executing it. Then inspect a benchmark result that violates an optimistic expectation: a missed event, a false alarm, or smoothing that worsens localization.

Use [RESEARCH_QUICKSTART](../RESEARCH_QUICKSTART.md) to run everything. Real hand movement and calibrated physical sensing remain future integration work; synthetic results do not establish biological meridian or consciousness mechanisms.
