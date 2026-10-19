"""Plan A: explicit synthetic longitudinal pathways versus spatial baselines."""
from .benchmark import run_benchmark
from .geometry import sensor_grid
from .graphs import independent_graph, spatial_graph, pathway_graph
from .filtering import diffuse, localize
from .synthetic import generate_trials
__all__ = ["run_benchmark", "sensor_grid", "independent_graph", "spatial_graph",
           "pathway_graph", "diffuse", "localize", "generate_trials"]
