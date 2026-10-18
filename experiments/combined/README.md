# Combined experiment

Run `python -m tactile_lab benchmark --experiment combined`.

The same 16-channel synthetic recordings are used by all four graph×receiver conditions: spatial/fixed, spatial/adaptive, pathway/fixed and pathway/adaptive.

Graph strength is fixed at 0.35, then each channel receives its causal detector. Maximum-channel score is the shared fusion rule. Threshold selection is performed separately with the same training/validation procedure and budget. The report includes descriptive recall effects and an interaction.

This is an illustrative multichannel extension, not a mechanics model of RP Hand. Background is common-mode with additional per-channel noise. The synthetic event perturbation uses a Gaussian spatial footprint. Some nuisance behavior is shared across channels, so coherence cannot be interpreted as proof of contact.

There are no significance claims from the small factorial run. Inspect operating points and every condition, not just the largest recall.

See [factorial equations](../../knowledge/27-factorial.md) and [fusion](../../knowledge/33-fusion.md).
