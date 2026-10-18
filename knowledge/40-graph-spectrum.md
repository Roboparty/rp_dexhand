# Connectivity and the graph spectrum

For symmetric nonnegative adjacency A, the combinatorial Laplacian L = D − A is positive semidefinite. The number of zero eigenvalues equals the number of connected components.

A simple explanation: a vector constant within each connected component has no edge differences, so its quadratic form and Laplacian action are zero. Independent component-wise constants give independent null directions.

The default spatial graph is connected and has one zero eigenvalue. The same-column pathway graph has four components and four zero eigenvalues, subject to floating-point tolerance. The topology tests verify these counts.

**Why used:** equal edge budgets do not imply equal ability to exchange information. The spectrum and component listing make an architectural difference explicit.

Edge length is another distinction. For coordinates in mm, sum each undirected edge length once. The pathway graph uses longer within-column connections; the spatial graph prefers local edges.

**Failure mode:** a spectral statistic alone does not predict task performance. A connected graph can blur a contact peak; disconnected groups can preserve useful separation. Use these diagnostics to explain outcomes, not as substitutes for evaluation.

**Code:** [describe_topology](../src/tactile_lab/pathways/topology.py). This diagnostic computes eigenvalues; the detector itself does not use an eigendecomposition.
