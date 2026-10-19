# Validation record

Executed locally on Windows with Python 3.12.14 and NumPy 2.5.4, 2026-10-18.

| Check | Observed result |
| --- | --- |
| Full pytest suite | 154 passed in 8.19 seconds |
| Documentation and asset audit | 246 local Markdown destinations resolved; 3 upstream asset hashes matched |
| Three-seed study | Seeds 42, 43, 44 completed for pathways, receivers, combined and ablation |
| Deterministic rerun | All four seed-42 scientific JSON files byte-identical |
| Wheel build | rp_tactile_lab-0.1.0-py3-none-any.whl built successfully |
| Example CSV replay | 240 samples, 198 observed scores, approximately 200 Hz |

The missing 42 replay scores are 40 warmup samples and 2 deliberately missing samples. Replay produces scores only.

## Reproduction hashes

SHA-256 of the seed-42 JSON files:

```text
040ab348da6cc4463ee3c3c34bd3f0f0692511e830159f966e2d62c7f13a6a5e  pathways.json
fcf1c5716c249260344bc88a525e6e0bf48c7fb26687c60a8c6fa84527e55255  receivers.json
b22885c7605329ddda80c364c8f2918400be9fce8fed178911c78553492aec96  combined.json
d1066c25a5f697bcea7086a0f9579daf02d97ef3a7e8b9a8b4fee838fd2bc716  ablation.json
```

The editable install required the documented no-build-isolation fallback on this bundled runtime. The wheel was built but was not installed into a separate clean environment. CI is configured for Python 3.10 and 3.12; remote CI results are not claimed here.

No physical hand, sensor acquisition, CAN-FD commands, ROS deployment, mechanical model or real slip detector was validated. See [implementation status](IMPLEMENTATION_STATUS.md), [study interpretation](reports/README.md) and [quickstart](RESEARCH_QUICKSTART.md).
