import pytest
from tactile_lab.sweep import run_sweep

@pytest.mark.parametrize("seeds",[[],[1,1],[-1],[True],[1.5]])
def test_invalid_seed_sets(seeds,tmp_path):
    with pytest.raises(ValueError): run_sweep(seeds,tmp_path)
