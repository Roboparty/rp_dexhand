"""Plan B: raw, fixed-filter and adaptive-normalization receiver baselines."""
from .config import ReceiverConfig
from .detectors import CausalReceiver
from .synthetic import Trial, generate_dataset
from .benchmark import run_benchmark
__all__ = ["ReceiverConfig", "CausalReceiver", "Trial", "generate_dataset", "run_benchmark"]
