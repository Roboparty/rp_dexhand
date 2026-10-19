"""Reproducible graph comparisons with no test-dependent tuning."""
import numpy as np
from tactile_lab.evaluation.splits import validate_splits
from tactile_lab.evaluation.artifacts import content_hash
from .geometry import sensor_grid
from .topology import describe_topology
from .graphs import independent_graph, spatial_graph, pathway_graph, graph_summary
from .synthetic import generate_trials
from .evaluation import evaluate, summarize, paired_comparison

def run_benchmark(seed=42, count=120):
    coordinates = sensor_grid()
    dataset = {split: generate_trials(seed, count, split, coordinates) for split in ("train", "validation", "test")}
    splits = validate_splits([t for group in dataset.values() for t in group])
    graphs = {"independent": independent_graph(coordinates), "spatial": spatial_graph(coordinates),
              "pathway": pathway_graph(coordinates)}
    grid = [0., .15, .35, .6]
    models = {}
    for name, graph in graphs.items():
        candidates = [0.] if name == "independent" else grid
        validation = [{"strength": a, **summarize(evaluate(dataset["validation"], coordinates, graph, a))} for a in candidates]
        chosen = min(validation, key=lambda row: (row["mean_error_mm"], row["strength"]))["strength"]
        rows = evaluate(dataset["test"], coordinates, graph, chosen)
        models[name] = {"strength": chosen, "steps": 1, "graph": graph_summary(graph), "topology": describe_topology(graph, coordinates),
                        "validation_candidates": validation, "summary": summarize(rows), "trials": rows,
                        "by_condition": {c: summarize([r for r in rows if r["condition"] == c])
                                         for c in sorted({r["condition"] for r in rows})}}
    # Fixed strength avoids hiding graph differences when validation selects no smoothing.
    fixed = {name: evaluate(dataset["test"], coordinates, graph, .35) for name, graph in graphs.items() if name != "independent"}
    comparison = paired_comparison(models["pathway"]["trials"], models["spatial"]["trials"], seed)
    config = {"seed": seed, "count_per_split": count, "strength_candidates": grid, "edge_budget": 24,
              "primary_endpoint": "mean localization error in mm", "useful_margin_mm": .25}
    return {"experiment": "pathway_graph", "evidence": "synthetic Gaussian contacts, not real hardware",
            "config": config, "config_sha256": content_hash(config), "splits": splits,
            "coordinates_mm": coordinates.tolist(), "models": models, "paired_pathway_minus_spatial": comparison,
            "fixed_strength_ablation": {"strength": .35, "spatial": summarize(fixed["spatial"]),
                                       "pathway": summarize(fixed["pathway"]),
                                       "paired": paired_comparison(fixed["pathway"], fixed["spatial"], seed)},
            "decision": "promising_on_this_generator" if comparison["bootstrap_95pct_interval_mm"][1] < -.25 else "no_demonstrated_useful_gain",
            "limitations": ["Longitudinal columns are an arbitrary pathway analogy, not anatomical meridians.",
                           "Gaussian footprint generator is not a validated contact-mechanics model.",
                           "Train split is reserved; this nonparametric model tunes strength on validation only.",
                           "A 0.25 mm margin is an illustrative prespecified benchmark criterion, not a hardware requirement."]}
