import numpy as np
from tactile_lab.pathways import sensor_grid,pathway_graph,spatial_graph
from tactile_lab.pathways.topology import describe_topology

def test_components_and_zero_eigenvalues():
    p=sensor_grid(); d=describe_topology(pathway_graph(p),p)
    assert d["component_count"]==4
    assert np.isclose(d["laplacian_eigenvalues"],0,atol=1e-10).sum()==4
def test_spatial_graph_connected_and_shorter():
    p=sensor_grid(); s=describe_topology(spatial_graph(p),p); q=describe_topology(pathway_graph(p),p)
    assert s["component_count"]==1
    assert s["total_edge_length_mm"]<q["total_edge_length_mm"]
