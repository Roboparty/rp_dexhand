"""Coordinates are millimeters on a synthetic rectangular tactile patch."""
import numpy as np


def sensor_grid(rows=4, columns=4, spacing_mm=10.0):
    if not isinstance(rows, int) or not isinstance(columns, int) or min(rows, columns) < 2:
        raise ValueError("rows and columns must be integers >= 2")
    if not np.isfinite(spacing_mm) or spacing_mm <= 0:
        raise ValueError("spacing_mm must be finite and positive")
    return np.array([(c * spacing_mm, r * spacing_mm)
                     for r in range(rows) for c in range(columns)], dtype=float)


def validate_coordinates(coordinates):
    points = np.asarray(coordinates, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2 or len(points) < 2:
        raise ValueError("coordinates must have shape (N >= 2, 2)")
    if not np.isfinite(points).all() or len(np.unique(points, axis=0)) != len(points):
        raise ValueError("coordinates must be finite and distinct")
    return points
