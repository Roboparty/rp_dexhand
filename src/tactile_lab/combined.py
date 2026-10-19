"""Four-condition graph x receiver experiment on the same synthetic trials."""
from dataclasses import replace, asdict
import numpy as np
from .pathways import sensor_grid, spatial_graph, pathway_graph, diffuse
from .receivers import generate_dataset, CausalReceiver
from .receivers.training import fit_config, select_threshold, threshold_candidates
from .receivers.metrics import evaluate_trial, aggregate
from .evaluation import validate_splits, content_hash

def multichannel_trials(seed=42, trials_per_scenario=4):
    trials = generate_dataset(seed, trials_per_scenario)
    p = sensor_grid()
    rng = np.random.default_rng(np.random.SeedSequence([seed, 777]))
    arrays = []
    for t in trials:
        target = rng.uniform(p.min(axis=0), p.max(axis=0))
        footprint = np.exp(-np.sum((p-target)**2, axis=1)/(2*8.**2))
        # Scalar background remains common-mode; only labeled synthetic event is spatial.
        spatial = np.tile(t.samples[:, None], (1, len(p)))
        for start, end in t.events:
            # Use a known synthetic increment; this generator does not estimate it from test labels.
            spatial[start:end] -= .5
            spatial[start:end] += .5*footprint
        spatial += rng.normal(0, .03, spatial.shape)
        arrays.append(spatial)
    return trials, arrays, p

def _scores(array, graph, mode, config):
    smoothed = diffuse(array, graph, .35, 1)
    scores = np.stack([CausalReceiver(mode, config).replay(smoothed[:, i]) for i in range(smoothed.shape[1])], axis=1)
    valid = np.isfinite(scores)
    maximum = np.max(np.where(valid, scores, -np.inf), axis=1)
    return np.where(valid.any(axis=1), maximum, np.nan)

def run_benchmark(seed=42, trials_per_scenario=4):
    trials, arrays, p = multichannel_trials(seed, trials_per_scenario)
    split_counts = validate_splits(trials)
    config = fit_config([t for t in trials if t.split == "train"])
    graphs = {"spatial": spatial_graph(p), "pathway": pathway_graph(p)}
    models = {}
    for name, graph in graphs.items():
        for mode in ("fixed", "adaptive"):
            scores = [_scores(a, graph, mode, config) for a in arrays]
            train = np.concatenate([s for t, s in zip(trials, scores) if t.split == "train"])
            finite = train[np.isfinite(train)]
            candidates = threshold_candidates(finite)
            val = [(t,s) for t,s in zip(trials,scores) if t.split == "validation"]
            threshold, tuning = select_threshold([t for t,s in val], [s for t,s in val], candidates)
            test = [(t,s) for t,s in zip(trials,scores) if t.split == "test"]
            rows = [evaluate_trial(t,s,threshold) for t,s in test]
            models[name+"_"+mode] = {"threshold": threshold, "summary": aggregate(rows), "trials": rows,
                                     "validation_candidates": tuning}
    r = {k:v["summary"]["recall"] for k,v in models.items()}
    settings = {"seed": seed, "trials_per_scenario_per_split": trials_per_scenario,
                "diffusion_strength": .35, "steps": 1, "edge_budget": 24,
                "receiver": asdict(config), "fusion": "maximum channel score", "threshold_resolution": 64, "refractory_samples": 20, "false_alarm_budget_per_minute": 3.}
    return {"experiment": "combined", "evidence": "synthetic 16-channel signals; no physical validation",
            "config": settings, "config_sha256": content_hash(settings), "splits": split_counts, "models": models,
            "recall_effects": {"pathway_at_fixed": r["pathway_fixed"]-r["spatial_fixed"],
                              "adaptation_at_spatial": r["spatial_adaptive"]-r["spatial_fixed"],
                              "interaction": r["pathway_adaptive"]-r["pathway_fixed"]-r["spatial_adaptive"]+r["spatial_fixed"]},
            "limitations": ["Common-mode background can dominate maximum-channel fusion.",
                           "The spatial event generator is an illustrative perturbation, not contact mechanics.",
                           "Effects are descriptive; no significance claim is made from this small factorial run.",
                           "Thresholds are separately calibrated with equal candidate budgets.",
                           "Graph strength is frozen at 0.35 to isolate graph topology from tuning."]}
