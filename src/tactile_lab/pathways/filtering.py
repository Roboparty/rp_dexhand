"""Missing-data-aware graph diffusion and positive-pressure localization."""
import numpy as np
from .graphs import validate_graph
from .geometry import validate_coordinates


def diffuse(values, adjacency, strength=0.25, steps=1):
    """Row-normalized diffusion; NaNs excluded, no evidence stays NaN.

    Accept (N,) or (..., N). Infinity is invalid, NaN denotes missing data.
    For observed nodes: (1-strength)*self + strength*neighbor mean.
    Missing nodes may be imputed from observed neighbors when strength > 0.
    """
    a = validate_graph(adjacency)
    x = np.asarray(values, dtype=float).copy()
    if x.ndim < 1 or x.shape[-1] != len(a) or np.isinf(x).any():
        raise ValueError("values must end in N channels and contain no infinity")
    if not np.isfinite(strength) or not 0 <= strength <= 1:
        raise ValueError("strength must lie in [0, 1]")
    if not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    if strength == 0:
        return x
    for _ in range(steps):
        observed = np.isfinite(x)
        denominator = observed.astype(float) @ a.T
        numerator = np.where(observed, x, 0.0) @ a.T
        neighbor = np.divide(numerator, denominator, out=np.zeros_like(x), where=denominator > 0)
        updated = np.where(observed, (1 - strength) * x + strength * neighbor, neighbor)
        x = np.where(denominator > 0, updated, x)
    return x


def localize(values, coordinates):
    """Positive weighted centroid in mm; no positive evidence returns NaNs."""
    p = validate_coordinates(coordinates)
    x = np.asarray(values, dtype=float)
    if x.ndim < 1 or x.shape[-1] != len(p) or np.isinf(x).any():
        raise ValueError("values must end in N channels and contain no infinity")
    weights = np.where(np.isfinite(x), np.maximum(x, 0), 0)
    total = weights.sum(axis=-1, keepdims=True)
    return np.divide(weights @ p, total, out=np.full(x.shape[:-1] + (2,), np.nan), where=total > 0)
