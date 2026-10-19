import numpy as np
import tactile_lab.receivers.benchmark as b
from tactile_lab.receivers.synthetic import generate_dataset

def test_test_values_cannot_change_chosen_threshold(monkeypatch):
    baseline=b.run_benchmark(9,1)
    def changed(seed,count):
        trials=generate_dataset(seed,count)
        for t in trials:
            if t.split=="test": t.samples=np.nan_to_num(t.samples)*100
        return trials
    monkeypatch.setattr(b,"generate_dataset",changed)
    changed_result=b.run_benchmark(9,1)
    assert baseline["config"]==changed_result["config"]
    for mode in baseline["models"]:
        assert baseline["models"][mode]["threshold"]==changed_result["models"][mode]["threshold"]
