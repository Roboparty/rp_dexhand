"""Least-squares reference-force calibration, not a certified sensor model."""
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class LinearCalibration:
    gain: float
    offset: float
    rmse: float
    raw_min: float
    raw_max: float
    unit: str = "N"

    def apply(self, raw, allow_extrapolation=False):
        x = np.asarray(raw, dtype=float)
        if not np.isfinite(x).all():
            raise ValueError("raw calibration input must be finite")
        if not allow_extrapolation and ((x < self.raw_min).any() or (x > self.raw_max).any()):
            raise ValueError("outside calibrated range")
        return self.gain*x + self.offset

def fit_linear(raw, reference, unit="N"):
    x, y = np.asarray(raw, float), np.asarray(reference, float)
    if x.ndim != 1 or x.shape != y.shape or len(x) < 3 or not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("need >= 3 finite paired calibration observations")
    if np.ptp(x) <= 0 or not isinstance(unit, str) or not unit:
        raise ValueError("raw input must vary and unit must be explicit")
    matrix = np.column_stack([x, np.ones_like(x)])
    coef, _, rank, _ = np.linalg.lstsq(matrix, y, rcond=None)
    if rank != 2:
        raise ValueError("calibration matrix is rank deficient")
    residual = y-matrix@coef
    return LinearCalibration(float(coef[0]), float(coef[1]), float(np.sqrt(np.mean(residual**2))),
                             float(x.min()), float(x.max()), unit)
