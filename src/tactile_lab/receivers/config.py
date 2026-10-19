"""Frozen causal receiver parameters; samples are arbitrary calibrated units."""
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ReceiverConfig:
    baseline_alpha: float = 0.015
    envelope_alpha: float = 0.15
    noise_alpha: float = 0.01
    noise_floor: float = 0.03
    initial_noise: float = 0.15
    adaptation_gate: float = 4.0
    warmup_samples: int = 40

    def __post_init__(self):
        for name in ('baseline_alpha', 'envelope_alpha', 'noise_alpha'):
            value = getattr(self, name)
            if not math.isfinite(value) or not 0 < value <= 1:
                raise ValueError(f'{name} must be in (0, 1]')
        for name in ('noise_floor', 'initial_noise', 'adaptation_gate'):
            if not math.isfinite(getattr(self, name)) or getattr(self, name) <= 0:
                raise ValueError(f'{name} must be finite and positive')
        if isinstance(self.warmup_samples, bool) or not isinstance(self.warmup_samples, int) or self.warmup_samples < 0:
            raise ValueError('warmup_samples must be a nonnegative integer')
