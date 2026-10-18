from tactile_lab.receivers import run_benchmark
from tactile_lab.evaluation.artifacts import canonical_json

def test_benchmark_all_baselines_and_scenarios():
    r=run_benchmark(7,1)
    assert set(r["models"])=={"raw","fixed","adaptive"}
    for model in r["models"].values():
        assert model["summary"]["trials"]==8
        assert len(model["by_scenario"])==8
        chosen=[row for row in model["validation_candidates"] if row["threshold"]==model["threshold"]][0]
        assert chosen["false_alarms_per_minute"]<=3
    canonical_json(r)
