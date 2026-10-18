import numpy as np
import pytest
from tactile_lab.receivers.training import threshold_candidates

def test_amplitude_grid_fills_sparse_quantiles():
    values=np.r_[np.zeros(1000),10]
    grid=threshold_candidates(values,11)
    assert 5 in grid and max(grid)>10 and grid==sorted(set(grid))
@pytest.mark.parametrize("scores", [[],[-1,0],[0,float("inf")],[float("nan")]])
def test_invalid_scores(scores):
    with pytest.raises(ValueError): threshold_candidates(scores)
