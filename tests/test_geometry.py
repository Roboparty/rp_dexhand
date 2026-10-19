import numpy as np
import pytest
from tactile_lab.pathways.geometry import sensor_grid, validate_coordinates

def test_grid_units():
    p=sensor_grid(2,3,5.)
    np.testing.assert_array_equal(p, [[0,0],[5,0],[10,0],[0,5],[5,5],[10,5]])

@pytest.mark.parametrize("points", [[[0,0]], [[0,0],[0,0]], [[0,float("nan")],[1,1]], [1,2]])
def test_bad_coordinates(points):
    with pytest.raises(ValueError): validate_coordinates(points)

@pytest.mark.parametrize("spacing", [0,-1,float("nan"),float("inf")])
def test_bad_spacing(spacing):
    with pytest.raises(ValueError): sensor_grid(spacing_mm=spacing)
