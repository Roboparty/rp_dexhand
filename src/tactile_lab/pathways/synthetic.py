"""Synthetic contact trials, not a calibrated mechanics simulation."""
from dataclasses import dataclass
import numpy as np
from .geometry import sensor_grid, validate_coordinates


@dataclass(frozen=True)
class ContactTrial:
    trial_id: str
    session_id: str
    object_id: str
    split: str
    condition: str
    values: np.ndarray
    target_mm: np.ndarray


def generate_trials(seed=42, count=120, split="test", coordinates=None):
    """One contact per independent synthetic session/object; disjoint RNG streams.

    Gaussian contact footprint + Gaussian readout noise. No graph is used in
    data generation, avoiding a generator that mechanically favors pathways.
    Condition cycles: clean, noisy, one failed sensor, and 25% dropout.
    """
    offsets = {"train": 0, "validation": 1, "test": 2}
    if split not in offsets or not isinstance(count, int) or count < 1:
        raise ValueError("choose train/validation/test and positive integer count")
    if not isinstance(seed, int) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    p = sensor_grid() if coordinates is None else validate_coordinates(coordinates)
    rng = np.random.default_rng(np.random.SeedSequence([seed, offsets[split]]))
    conditions = ("clean", "noise", "single_dropout", "quarter_dropout")
    trials = []
    for i in range(count):
        condition = conditions[i % len(conditions)]
        target = rng.uniform(p.min(axis=0), p.max(axis=0))
        width = rng.uniform(5, 12)
        amplitude = rng.uniform(0.8, 1.2)
        pressure = amplitude * np.exp(-np.sum((p - target)**2, axis=1) / (2 * width**2))
        noise = 0.16 if condition == "noise" else 0.04
        values = pressure + rng.normal(0, noise, len(p))
        missing = 1 if condition == "single_dropout" else len(p) // 4 if condition == "quarter_dropout" else 0
        if missing:
            values[rng.choice(len(p), missing, replace=False)] = np.nan
        trials.append(ContactTrial(f"{split}-{i:04d}", f"{split}-session-{i:04d}",
                                   f"{split}-object-{i:04d}", split, condition, values, target))
    return trials
