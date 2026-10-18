# Research results

The [three-seed study](robustness/SUMMARY.md) retains all 12 experiment runs, complete validation candidate tables and test-trial metrics. [Machine-readable summary](robustness/summary.json) and [execution provenance](robustness/provenance.json) accompany the per-seed files.

## Findings

- **Plan A:** no demonstrated useful pathway advantage on any seed. Seeds 42 and 44 select zero smoothing for both graphs; seed 43 selects a small spatial smoothing strength, with mean errors 3.3536 mm spatial versus 3.3607 mm pathway. This is evidence against expecting this particular pathway map to help this generator.
- **Plan B:** adaptive versus fixed recall is 0.675 versus 0.700 on seed 42, 0.700 versus 0.700 on seed 43, and 0.850 versus 0.725 on seed 44. Adaptive false alarms/minute are 4.0388, 3.5003 and 2.6925. The validation budget of 3/minute does not transfer reliably to test.
- **Combined experiment:** adaptation improves recall on these three synthetic multichannel sets, but pathway topology has no consistent advantage over spatial topology. Inspect false alarms alongside recall; the models operate at independently calibrated thresholds.
- **Ablations:** changing noise adaptation, gating or envelope speed changes the tradeoff. All variants are retained. These test results have not been used to promote a new default.

These are development benchmarks with synthetic contacts/events, not real slip, physical grasp performance or evidence for meridian/consciousness mechanisms. Three generator seeds are not three physical replications.

## Reproduce

Run from the repository root after the [quickstart](../RESEARCH_QUICKSTART.md):

```text
python -m tactile_lab sweep --seeds 42 43 44 --output runs/robustness
```

Compare scientific JSON separately from provenance, which records the executing environment and revision. The report source revision is `b03df232adb34c894ff025946fcea2494d032cc7`. Its dirty flag is true because output reports were untracked during execution; source files were committed before the run. Reports were committed afterward.

During development, a coarse quantile-only threshold grid was found to undersample useful fixed-detector operating points. The final shared search uses both uniform amplitude and quantile grids, each with resolution 64. This change followed inspection of early results: these seeds are therefore transparent development evaluations, not a preregistered untouched confirmatory study. A future confirmatory study needs frozen code and newly acquired data.

## Next decision

Keep the independent/spatial baseline. Collect calibrated, timestamped sensor data with independent event labels, then freeze an operating requirement and compare on new sessions/objects. Choose adaptive settings on training/validation data only. Physical integration gates remain in the [project plan](../PROJECT_PLANS.md).
