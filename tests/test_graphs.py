import numpy as np
import pytest
from tactile_lab.pathways import sensor_grid, spatial_graph, pathway_graph, independent_graph
from tactile_lab.pathways.graphs import graph_summary, validate_graph

def test_budget_and_symmetry():
    p=sensor_grid()
    for graph in (spatial_graph(p), pathway_graph(p)):
        assert graph_summary(graph)["edges"]==24
        np.testing.assert_array_equal(graph,graph.T)
        assert np.diag(graph).sum()==0
    assert independent_graph(p).sum()==0

def test_pathways_are_same_columns():
    p=sensor_grid(); a=pathway_graph(p)
    for i,j in zip(*np.nonzero(a)): assert p[i,0]==p[j,0]
    assert not np.array_equal(a,spatial_graph(p))

@pytest.mark.parametrize("graph", [[[0,1],[0,0]], [[1,0],[0,0]], [[0,-1],[-1,0]], [[0,float("inf")],[float("inf"),0]]])
def test_invalid_graph(graph):
    with pytest.raises(ValueError): validate_graph(graph)

def test_budget_bounds():
    with pytest.raises(ValueError): spatial_graph(sensor_grid(),121)
