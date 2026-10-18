import numpy as np
import pytest
from tactile_lab.pathways import diffuse, sensor_grid, spatial_graph

def test_convex_range_and_constant_invariance():
    a=spatial_graph(sensor_grid())
    x=np.arange(16,dtype=float); before=x.copy()
    y=diffuse(x,a,.4,5)
    assert y.min()>=x.min() and y.max()<=x.max()
    np.testing.assert_array_equal(x,before)
    np.testing.assert_allclose(diffuse(np.ones(16)*3,a,.6,10),3)

@pytest.mark.parametrize("strength", [-.1,1.1,float("nan")])
def test_invalid_strength(strength):
    with pytest.raises(ValueError): diffuse([1,2],[[0,1],[1,0]],strength)

def test_infinite_input_rejected():
    with pytest.raises(ValueError): diffuse([1,np.inf],[[0,1],[1,0]])

def test_invalid_steps():
    with pytest.raises(ValueError): diffuse([1,2],[[0,1],[1,0]],steps=-1)
