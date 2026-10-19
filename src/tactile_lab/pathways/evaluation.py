"""Trial-level endpoints and paired bootstrap uncertainty."""
import numpy as np
from .filtering import diffuse, localize


def evaluate(trials, coordinates, adjacency, strength, steps=1):
    """No-estimate penalty = patch diagonal; failures additionally explicit."""
    p = np.asarray(coordinates, dtype=float)
    diagonal = float(np.linalg.norm(np.ptp(p, axis=0)))
    rows = []
    for trial in trials:
        estimate = localize(diffuse(trial.values, adjacency, strength, steps), p)
        valid = bool(np.isfinite(estimate).all())
        error = float(np.linalg.norm(estimate - trial.target_mm)) if valid else diagonal
        rows.append({"trial_id": trial.trial_id, "session_id": trial.session_id,
                     "object_id": trial.object_id, "split": trial.split,
                     "condition": trial.condition, "target_mm": trial.target_mm.tolist(),
                     "estimate_mm": estimate.tolist() if valid else None,
                     "error_mm": error, "failed": not valid})
    if not rows:
        raise ValueError("evaluation requires at least one trial")
    return rows


def summarize(rows):
    if not rows:
        raise ValueError("cannot summarize empty rows")
    errors = np.array([r["error_mm"] for r in rows])
    return {"trials": len(rows), "mean_error_mm": float(errors.mean()),
            "median_error_mm": float(np.median(errors)),
            "p95_error_mm": float(np.quantile(errors, 0.95)),
            "failures": sum(r["failed"] for r in rows)}


def paired_comparison(candidate, baseline, seed=42, replicates=2000):
    if len(candidate) != len(baseline) or not candidate:
        raise ValueError("paired comparisons require equal nonempty trials")
    if any(a["trial_id"] != b["trial_id"] for a, b in zip(candidate, baseline)):
        raise ValueError("trial order/identity mismatch")
    if not isinstance(replicates, int) or replicates < 2:
        raise ValueError("replicates must be >= 2")
    delta = np.array([a["error_mm"] - b["error_mm"] for a, b in zip(candidate, baseline)])
    rng = np.random.default_rng(seed)
    boot = delta[rng.integers(0, len(delta), size=(replicates, len(delta)))].mean(axis=1)
    return {"mean_delta_mm": float(delta.mean()),
            "bootstrap_95pct_interval_mm": np.quantile(boot, [0.025, 0.975]).tolist(),
            "negative_favors": "candidate", "unit": "independent synthetic trial",
            "replicates": replicates}
