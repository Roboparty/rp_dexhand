"""Guard evaluation boundaries before fitting any model."""
def validate_splits(trials):
    groups = {s: {"sessions": set(), "objects": set(), "trials": set()} for s in ("train", "validation", "test")}
    seen = set()
    for trial in trials:
        if trial.split not in groups:
            raise ValueError("unknown split")
        if not all(isinstance(v, str) and v for v in (trial.trial_id, trial.session_id, trial.object_id)):
            raise ValueError("identifiers must be nonempty strings")
        if trial.trial_id in seen:
            raise ValueError("duplicate trial identifier")
        seen.add(trial.trial_id)
        group = groups[trial.split]
        group["sessions"].add(trial.session_id)
        group["objects"].add(trial.object_id)
        group["trials"].add(trial.trial_id)
    for name, values in groups.items():
        if not values["trials"]:
            raise ValueError(f"empty {name} split")
    names = list(groups)
    for i, left in enumerate(names):
        for right in names[i + 1:]:
            for kind in ("sessions", "objects"):
                if groups[left][kind] & groups[right][kind]:
                    raise ValueError(f"{kind} leakage between {left} and {right}")
    return {name: {key: len(value) for key, value in group.items()} for name, group in groups.items()}
