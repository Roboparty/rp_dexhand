"""Sample-by-sample receivers: no future samples and no test-label updates."""
import numpy as np
from .config import ReceiverConfig


class CausalReceiver:
    def __init__(self, mode='fixed', config=None):
        if mode not in ('raw', 'fixed', 'adaptive'):
            raise ValueError('mode must be raw, fixed, or adaptive')
        self.mode = mode
        self.config = config or ReceiverConfig()
        self.reset()

    def reset(self):
        self.baseline = None
        self.envelope = 0.0
        self.noise = self.config.initial_noise
        self.valid_samples = 0

    def update(self, sample):
        x = float(sample)
        if not np.isfinite(x):
            # Missing data produce no decision and never update the state.
            return float('nan')
        c = self.config
        if self.baseline is None:
            self.baseline = x
        residual = abs(x - self.baseline)
        self.baseline += c.baseline_alpha * (x - self.baseline)
        self.envelope += c.envelope_alpha * (residual - self.envelope)
        scale = max(self.noise, c.noise_floor)
        score = {'raw': abs(x), 'fixed': self.envelope,
                 'adaptive': self.envelope / scale}[self.mode]
        # Gate noise updates during strong events to reduce event absorption.
        # The gate can still absorb weak events; benchmarks include that failure.
        if self.envelope < c.adaptation_gate * scale:
            self.noise += c.noise_alpha * (residual - self.noise)
        self.valid_samples += 1
        return float('nan') if self.valid_samples <= c.warmup_samples else float(score)

    def replay(self, samples):
        values = np.asarray(samples, dtype=float)
        if values.ndim != 1:
            raise ValueError('replay expects a one-dimensional signal')
        return np.asarray([self.update(x) for x in values])
