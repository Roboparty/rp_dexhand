"""A two-node example with a hand-checkable diffusion step."""
import numpy as np
from tactile_lab.pathways import diffuse,localize
positions=np.array([[0.,0.],[10.,0.]])
adjacency=np.array([[0.,1.],[1.,0.]])
raw=np.array([2.,6.])
filtered=diffuse(raw,adjacency,.25)
print("Raw values:",raw,"Filtered:",filtered)
print("Raw centroid (mm):",localize(raw,positions))
print("Filtered centroid (mm):",localize(filtered,positions))
print("Smoothing changes a centroid; whether it improves accuracy needs a known target.")
