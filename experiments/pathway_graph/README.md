# Pathway graph experiment

Run `python -m tactile_lab benchmark --experiment pathways`.

Input: 120 synthetic contact trials per train/validation/test split by default, with a fixed 4×4, 10 mm sensor grid. Clean, noise and two dropout conditions share the same evaluator.

Models: independent sensors, shortest-distance graph and same-column pathway graph. The two nonempty graphs have 24 edges. Shared decoder: nonnegative weighted centroid. Strength candidates: 0, 0.15, 0.35 and 0.6, selected by validation mean error with smaller-strength tie breaking.

Read selected strength before interpreting performance. Zero means no diffusion, so graph topology does not affect that selected model. The JSON includes a 0.35 fixed-strength comparison, topology diagnostics, per-condition summaries and paired bootstrap uncertainty.

The pathway mapping is explicitly arbitrary and synthetic. It is not an anatomical meridian reconstruction. The endpoint is localization error in mm, not a biological claim.

See [mapping](../../knowledge/14-pathway-mapping.md), [diffusion](../../knowledge/16-diffusion.md) and [evaluation](../../knowledge/19-localization-error.md).
