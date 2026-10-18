"""Uncertainty for independent experimental units, never correlated frames."""
import numpy as np

def paired_interval(candidate, baseline, seed=42, replicates=2000):
    a, b = np.asarray(candidate, float), np.asarray(baseline, float)
    if a.ndim != 1 or a.shape != b.shape or len(a) < 2 or not np.isfinite(a).all() or not np.isfinite(b).all():
        raise ValueError("need at least two finite paired observations")
    if isinstance(replicates, bool) or not isinstance(replicates, int) or replicates < 100:
        raise ValueError("replicates must be an integer >= 100")
    delta = a - b
    rng = np.random.default_rng(seed)
    samples = np.array([rng.choice(delta, len(delta), replace=True).mean() for _ in range(replicates)])
    return {"mean_delta": float(delta.mean()), "interval_95": np.quantile(samples, [.025, .975]).tolist(),
            "n_units": len(delta), "replicates": replicates, "method": "paired percentile bootstrap"}

def wilson_interval(successes, total, z=1.959963984540054):
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (successes, total)) or total <= 0 or not 0 <= successes <= total:
        raise ValueError("require integers 0 <= successes <= total and total > 0")
    if not np.isfinite(z) or z <= 0:
        raise ValueError("z must be positive")
    p = successes / total
    denominator = 1 + z*z/total
    center = (p + z*z/(2*total))/denominator
    half = z*np.sqrt(p*(1-p)/total + z*z/(4*total*total))/denominator
    return [max(0., float(center-half)), min(1., float(center+half))]
