from dataclasses import replace
import numpy as np
import tactile_lab.pathways.benchmark as b
from tactile_lab.pathways.synthetic import generate_trials

def test_test_targets_cannot_change_selected_strength(monkeypatch):
    baseline=b.run_benchmark(4,12)
    def changed(seed,count,split,coordinates):
        trials=generate_trials(seed,count,split,coordinates)
        return [replace(t,target_mm=np.array([0.,0.])) for t in trials] if split=="test" else trials
    monkeypatch.setattr(b,"generate_trials",changed)
    result=b.run_benchmark(4,12)
    for mode in baseline["models"]:
        assert result["models"][mode]["strength"]==baseline["models"][mode]["strength"]
