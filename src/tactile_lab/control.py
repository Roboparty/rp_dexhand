"""Pure simulated grip decisions; this module has no hardware transport."""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class GripDecision:
    command: float
    reason: str
    allowed: bool

def propose_grip(current, slip_detected, *, age_s, homed, stopped, force_n, max_force_n=5., step=.01, max_age_s=.05):
    values = (current, age_s, force_n, max_force_n, step, max_age_s)
    if not all(math.isfinite(v) for v in values):
        raise ValueError("all control inputs must be finite")
    if not 0 <= current <= 1 or age_s < 0 or force_n < 0 or min(max_force_n, step, max_age_s) <= 0 or step > 1:
        raise ValueError("invalid control range")
    for blocked, reason in ((stopped, "stop requested"), (not homed, "unverified home"),
                            (age_s > max_age_s, "stale sensor"), (force_n >= max_force_n, "force limit")):
        if blocked:
            return GripDecision(current, reason, False)
    return GripDecision(min(1., current+step) if slip_detected else current,
                        "bounded increment" if slip_detected else "hold", True)
