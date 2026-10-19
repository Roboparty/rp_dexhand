# What the pathway mapping actually means

The default patch is a 4×4 grid with 10 mm spacing. Nodes are ordered by row, then column. The selected pathway graph connects every pair within each vertical column: four disjoint four-node complete graphs.

Each column has C(4,2) = 6 edges; four columns yield 24 edges, matching the spatial baseline's budget. Connections within a column include longer distances than immediate neighbors.

This is a deliberately simple longitudinal-pathway analogy. It is not digitized acupuncture anatomy, and the patch is not a geometrically faithful hand. Naming the graph pathway does not supply biological evidence.

**Why used:** a fixed, auditable structural proposal is testable. If it fails, the result is about this mapping and generator; it does not refute every conceivable pathway design.

**Worked example:** a node at (0,0) connects to (0,10), (0,20) and (0,30) mm. It does not connect to the equally close (10,0) node in the default pathway graph.

**Failure mode:** disconnected columns cannot exchange evidence. Increasing edge count eventually adds cross-column connections, changing the hypothesis. Record the exact graph, not only its name.

**Code:** [pathway_graph](../src/tactile_lab/pathways/graphs.py).
