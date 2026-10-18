"""CSV replay schema for measured or synthetic single-channel recordings."""
from dataclasses import dataclass
import csv
from pathlib import Path
import numpy as np

@dataclass(frozen=True)
class Recording:
    timestamps_s: np.ndarray
    samples: np.ndarray
    sample_rate_hz: float
    unit: str
    source: str

def load_csv(path, unit, source):
    if not unit or source not in ("synthetic", "measured"):
        raise ValueError("declare units and source as synthetic or measured")
    with Path(path).open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not {"timestamp_s", "value"}.issubset(reader.fieldnames):
            raise ValueError("CSV requires timestamp_s and value columns")
        rows = list(reader)
    if len(rows) < 3:
        raise ValueError("at least three samples are required")
    times = np.array([float(r["timestamp_s"]) for r in rows])
    samples = np.array([float(r["value"]) if r["value"].strip() else np.nan for r in rows])
    if not np.isfinite(times).all() or np.isinf(samples).any():
        raise ValueError("timestamps must be finite; infinity is not missing data")
    delta = np.diff(times)
    if (delta <= 0).any():
        raise ValueError("timestamps must strictly increase")
    nominal = float(np.median(delta))
    if not np.allclose(delta, nominal, rtol=.01, atol=1e-9):
        raise ValueError("irregular sampling: resample explicitly before using sample-index filters")
    if not np.isfinite(samples).any():
        raise ValueError("recording has no observed samples")
    return Recording(times, samples, 1/nominal, unit, source)
