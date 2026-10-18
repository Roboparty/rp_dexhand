from tactile_lab.pathways import run_benchmark
from tactile_lab.evaluation.artifacts import canonical_json

def test_benchmark_reproducible_and_strict_json():
    a=run_benchmark(11,12); b=run_benchmark(11,12)
    assert canonical_json(a)==canonical_json(b)

def test_selected_strength_is_validation_optimum():
    result=run_benchmark(42,12)
    for model in result["models"].values():
        expected=min(model["validation_candidates"],key=lambda r:(r["mean_error_mm"],r["strength"]))
        assert model["strength"]==expected["strength"]
        assert all(t["split"]=="test" for t in model["trials"])
    assert result["models"]["spatial"]["graph"]["edges"]==result["models"]["pathway"]["graph"]["edges"]
