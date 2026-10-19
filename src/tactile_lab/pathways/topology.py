"""Structural diagnostics, independent of observed contact labels."""
import numpy as np
from .graphs import validate_graph
from .geometry import validate_coordinates

def describe_topology(adjacency,coordinates):
    a=validate_graph(adjacency); p=validate_coordinates(coordinates)
    if len(a)!=len(p):
        raise ValueError("graph and coordinate sizes differ")
    unseen=set(range(len(a))); components=[]
    while unseen:
        stack=[min(unseen)]; component=[]; unseen.remove(stack[0])
        while stack:
            i=stack.pop(); component.append(i)
            for j in np.flatnonzero(a[i]>0):
                j=int(j)
                if j in unseen: unseen.remove(j); stack.append(j)
        components.append(sorted(component))
    laplacian=np.diag(a.sum(axis=1))-a
    eigenvalues=np.linalg.eigvalsh(laplacian)
    lengths=[float(np.linalg.norm(p[i]-p[j])) for i in range(len(a)) for j in range(i+1,len(a)) if a[i,j]>0]
    return {"components":components,"component_count":len(components),
            "laplacian_eigenvalues":eigenvalues.tolist(),
            "total_edge_length_mm":sum(lengths),
            "mean_edge_length_mm":float(np.mean(lengths)) if lengths else None}
