"""Explicitly synthetic tactile challenges; not a physical slip simulator."""
from dataclasses import dataclass
import numpy as np

SCENARIOS = ('clean_event', 'weak_event', 'motor_only', 'no_contact',
             'drift_event', 'dropout_event', 'noise_change', 'fast_event')


@dataclass
class Trial:
    trial_id: str
    session_id: str
    object_id: str
    split: str
    scenario: str
    sample_rate_hz: float
    samples: np.ndarray
    events: tuple


def generate_dataset(seed=42, trials_per_scenario=8, sample_rate_hz=200.0):
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError('seed must be a nonnegative integer')
    if isinstance(trials_per_scenario, bool) or not isinstance(trials_per_scenario, int) or trials_per_scenario < 1:
        raise ValueError('trials_per_scenario must be a positive integer')
    if not np.isfinite(sample_rate_hz) or sample_rate_hz < 100:
        raise ValueError('sample rate must be at least 100 Hz for this generator')
    rng = np.random.default_rng(seed)
    trials = []
    n = int(sample_rate_hz * 4)
    t = np.arange(n) / sample_rate_hz
    for split in ('train', 'validation', 'test'):
        for scenario in SCENARIOS:
            for index in range(trials_per_scenario):
                noise = rng.uniform(0.04, 0.12)
                samples = rng.normal(0, noise, n)
                events = ()
                onset = int(rng.uniform(1.3, 2.1) * sample_rate_hz)
                duration = int((0.12 if scenario == 'fast_event' else 0.6) * sample_rate_hz)
                if scenario not in ('motor_only', 'no_contact', 'noise_change'):
                    amplitude = rng.uniform(0.18, 0.32) if scenario == 'weak_event' else rng.uniform(0.7, 1.2)
                    samples[onset:onset + duration] += amplitude
                    events = ((onset, onset + duration),)
                if scenario in ('motor_only', 'drift_event'):
                    samples += rng.uniform(0.1, 0.3) * np.sin(2 * np.pi * 30 * t + rng.uniform(0, 6))
                if scenario == 'drift_event':
                    samples += rng.uniform(0.1, 0.3) * t
                if scenario == 'noise_change':
                    samples[n // 2:] += rng.normal(0, 0.25, n - n // 2)
                if scenario == 'dropout_event':
                    samples[onset - 5:onset + int(0.15 * sample_rate_hz)] = np.nan
                trials.append(Trial(f'{split}-{scenario}-{index}', f'{split}-session-{index}',
                                    f'{split}-object-{index}', split, scenario,
                                    sample_rate_hz, samples, events))
    return trials
