"""Frozen graph construction: no labels or observations enter these functions."""
import numpy as np
from .geometry import validate_coordinates


def validate_graph(adjacency):
    a = np.asarray(adjacency, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or not len(a):
        raise ValueError("adjacency must be a nonempty square matrix")
    if not np.isfinite(a).all() or (a < 0).any():
        raise ValueError("weights must be finite and nonnegative")
    if not np.allclose(a, a.T) or not np.allclose(np.diag(a), 0):
        raise ValueError("graph must be undirected without self edges")
    return a


def independent_graph(coordinates):
    return np.zeros((len(validate_coordinates(coordinates)),) * 2)


def _budget(n, edge_count):
    if not isinstance(edge_count, int) or not 0 <= edge_count <= n * (n - 1) // 2:
        raise ValueError("invalid undirected edge budget")


def _from_pairs(n, pairs, edge_count):
    _budget(n, edge_count)
    a = np.zeros((n, n))
    for i, j in pairs[:edge_count]:
        a[i, j] = a[j, i] = 1.0
    return a


def spatial_graph(coordinates, edge_count=24):
    p = validate_coordinates(coordinates)
    pairs = [(i, j) for i in range(len(p)) for j in range(i + 1, len(p))]
    pairs.sort(key=lambda ij: (float(np.linalg.norm(p[ij[0]] - p[ij[1]])), *ij))
    return _from_pairs(len(p), pairs, edge_count)


def pathway_graph(coordinates, edge_count=24):
    """Prioritize same-column pairs, then nearest cross-column pairs.

    This deliberately arbitrary longitudinal-pathway analogy is NOT a mapping
    of acupuncture points. Long connections test a different inductive bias.
    """
    p = validate_coordinates(coordinates)
    pairs = [(i, j) for i in range(len(p)) for j in range(i + 1, len(p))]
    pairs.sort(key=lambda ij: (p[ij[0], 0] != p[ij[1], 0],
                              float(np.linalg.norm(p[ij[0]] - p[ij[1]])), *ij))
    return _from_pairs(len(p), pairs, edge_count)


def graph_summary(adjacency):
    a = validate_graph(adjacency)
    degrees = (a > 0).sum(axis=1)
    return {"nodes": len(a), "edges": int((a > 0).sum() // 2),
            "degrees": degrees.tolist(), "isolated_nodes": int((degrees == 0).sum())}
