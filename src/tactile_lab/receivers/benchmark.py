"""Causal threshold detectors evaluated on synthetic held-out trial groups."""
from dataclasses import asdict
import numpy as np
from tactile_lab.evaluation.splits import validate_splits
from tactile_lab.evaluation.artifacts import content_hash
from .synthetic import generate_dataset
from .detectors import CausalReceiver
from .metrics import evaluate_trial, aggregate
from .training import fit_config, select_threshold, threshold_candidates

def run_benchmark(seed=42, trials_per_scenario=8):
    trials = generate_dataset(seed, trials_per_scenario)
    splits = validate_splits(trials)
    groups = {s: [t for t in trials if t.split == s] for s in ("train", "validation", "test")}
    config = fit_config(groups["train"])
    modes = {}
    for mode in ("raw", "fixed", "adaptive"):
        score_groups = {s: [CausalReceiver(mode, config).replay(t.samples) for t in ts] for s, ts in groups.items()}
        training_scores = np.concatenate(score_groups["train"])
        finite = training_scores[np.isfinite(training_scores)]
        # A finite no-alarm candidate is based on training only; no test score is inspected.
        candidates = threshold_candidates(finite)
        threshold, validation = select_threshold(groups["validation"], score_groups["validation"], candidates)
        rows = [evaluate_trial(t, scores, threshold) for t, scores in zip(groups["test"], score_groups["test"])]
        modes[mode] = {"threshold": threshold, "validation_candidates": validation, "summary": aggregate(rows),
                       "by_scenario": {scenario: aggregate([r for r in rows if r["scenario"] == scenario])
                                       for scenario in sorted({r["scenario"] for r in rows})}, "trials": rows}
    settings = {"seed": seed, "trials_per_scenario_per_split": trials_per_scenario,
                "receiver": asdict(config), "threshold_resolution": 64, "refractory_samples": 20, "false_alarm_budget_per_minute": 3., "sample_rate_hz": 200.}
    return {"experiment": "adaptive_receiver", "evidence": "synthetic step events, not measured physical slip",
            "config": settings, "config_sha256": content_hash(settings), "splits": splits, "models": modes,
            "limitations": ["Test false-alarm rate is measured, not guaranteed by validation calibration.",
                           "Latency is conditional on detection; read it with recall and false alarms.",
                           "One scalar channel per trial; multichannel coherence is not implemented here.",
                           "Warmup and missing samples yield no decisions and reduce observed exposure.",
                           "Fixed mode uses a fixed filter with evolving causal state; it is not a fixed-valued signal."]}
