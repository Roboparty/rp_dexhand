# Implementation Status

## Implemented and runnable

- Plan A: synthetic contact generation, explicit spatial/pathway graphs, equal edge budgets, missing-aware diffusion, centroid localization, validation-only strength selection, per-condition evaluation and paired bootstrap comparisons.
- Plan B: synthetic nuisance scenarios, causal raw/fixed/adaptive receivers, training-only noise fitting, validation-only threshold calibration, event-level metrics and adaptation ablations.
- Combined: four graph×receiver conditions on shared multichannel recordings with fixed graph strength and maximum-score fusion.
- Shared: calibration utilities, CSV replay, strict result artifacts, software provenance, multi-seed runs, offline coherence/lag diagnostics and observation-quality checks.
- Education: 40 concept chapters, glossary, equation ledger, executable examples and run instructions.
- Tests: analytical examples, causal prefix/chunk checks, missing data, label contracts, split leakage, calibration, topology, CLI output and test-perturbation guards.

## Not claimed as complete

No physical tactile sensor has been calibrated or acquired through RP Hand. No CAN-FD command is sent by this package. No driver/ROS integration, physical homing, actuator stop, joint mapping, force-controlled grasp, CAD load or robot simulation has been validated.

The pure grip policy illustrates decision guards; it is not a deployed controller or a physical grasp dynamics model. Coherence is an offline diagnostic, not part of the streaming detector. The pathway graph is a synthetic column mapping, not anatomical reconstruction.

Hardware milestones A2/A5 and B5 from the original plan require equipment, measured data, compatible software and explicit acceptance records. Software prototypes support that work but do not replace it.

## Interpreting evaluation

Synthetic results can reject an optimistic algorithmic claim on the chosen distribution. They cannot establish a biological or consciousness mechanism. The benchmark's validation false-alarm budget is measured again on test and can fail there. Every reported seed is retained.
