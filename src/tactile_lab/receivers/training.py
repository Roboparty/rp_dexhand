"""Training-only fit and validation-only threshold selection."""
from dataclasses import replace
import numpy as np
from .config import ReceiverConfig
from .metrics import evaluate_trial, aggregate

def fit_config(trials):
    if not trials or any(t.split != "train" for t in trials):
        raise ValueError("fit_config requires training trials only")
    background = []
    for trial in trials:
        mask = np.isfinite(trial.samples)
        for start, end in trial.events:
            mask[start:end] = False
        background.extend(np.abs(trial.samples[mask]).tolist())
    if not background:
        raise ValueError("no observed training background")
    scale = max(float(np.median(background)), ReceiverConfig().noise_floor)
    return replace(ReceiverConfig(), initial_noise=scale)

def select_threshold(trials, score_arrays, candidates, false_alarms_per_minute=3.):
    if not trials or any(t.split != "validation" for t in trials) or len(trials) != len(score_arrays):
        raise ValueError("threshold selection requires matching validation trials")
    if not np.isfinite(false_alarms_per_minute) or false_alarms_per_minute < 0:
        raise ValueError("invalid false-alarm budget")
    choices = []
    for threshold in candidates:
        rows = [evaluate_trial(t, scores, float(threshold)) for t, scores in zip(trials, score_arrays)]
        summary = aggregate(rows)
        if summary["background_minutes"] <= 0:
            raise ValueError("validation requires observed background exposure")
        choices.append({"threshold": float(threshold), **summary})
    feasible = [r for r in choices if r["false_alarms_per_minute"] <= false_alarms_per_minute]
    if not feasible:
        raise ValueError("no threshold meets validation false-alarm budget")
    # Recall first, then fewer false alarms, then earlier detected latency.
    chosen = min(feasible, key=lambda r: (-(r["recall"] or 0), r["false_alarms_per_minute"],
                                          r["mean_detected_latency_ms"] if r["mean_detected_latency_ms"] is not None else float("inf"),
                                          r["threshold"]))
    return chosen["threshold"], choices


def threshold_candidates(training_scores, resolution=64):
    """Equal-budget quantile and amplitude grids, from training scores only."""
    values = np.asarray(training_scores, float)
    if values.ndim != 1 or np.isinf(values).any():
        raise ValueError("training scores must be a vector without infinity")
    values = values[np.isfinite(values)]
    if not len(values) or (values < 0).any():
        raise ValueError("need nonnegative finite training scores")
    if isinstance(resolution, bool) or not isinstance(resolution, int) or resolution < 2:
        raise ValueError("resolution must be an integer >= 2")
    maximum = float(values.max())
    return sorted(set([*np.linspace(0, maximum, resolution).tolist(),
                       *np.quantile(values, np.linspace(0, 1, resolution)).tolist(),
                       maximum*10+1]))
