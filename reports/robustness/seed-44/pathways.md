# Pathway Graph Results

Evidence: **synthetic Gaussian contacts, not real hardware**

Configuration hash: `35214076ebeda27379d332807b464072b36beced47bb48935bc2e7ef8d495655`

| Model | Strength | Mean error (mm) | P95 error (mm) | Failures |
| --- | --- | --- | --- | --- |
| independent | 0.0000 | 3.5404 | 7.4150 | 0 |
| spatial | 0.0000 | 3.5404 | 7.4150 | 0 |
| pathway | 0.0000 | 3.5404 | 7.4150 | 0 |

Pathway minus spatial error: 0.0000 mm; paired bootstrap 95% interval: [0.0, 0.0].
Decision: **no_demonstrated_useful_gain**. Negative deltas favor pathways.

The fixed-strength ablation and condition-level results remain in the JSON artifact.

## Limitations

- Longitudinal columns are an arbitrary pathway analogy, not anatomical meridians.
- Gaussian footprint generator is not a validated contact-mechanics model.
- Train split is reserved; this nonparametric model tunes strength on validation only.
- A 0.25 mm margin is an illustrative prespecified benchmark criterion, not a hardware requirement.

## Reproduction

Use the saved configuration and the recorded source revision. The JSON contains validation candidates and individual held-out trial results. No physical hand was commanded.
