# Graph representation and edge budgets

A graph contains nodes (sensors) and edges (relationships used by processing). The adjacency matrix A has entries A_ij = 1 for a selected connection and zero otherwise. Our graphs are undirected: A = Aᵀ, with zero diagonal and no negative weights.

For an unweighted undirected graph, edge count is E = (Σ_ij A_ij)/2 because each edge appears twice. Degree d_i = Σ_j A_ij counts neighbors. A 16-node graph with 24 edges has average degree 2E/N = 3.

**Why used:** a graph makes the pathway hypothesis explicit and reproducible. Equal edge counts remove one simple confound, although they do not equalize every property: degrees, connectivity and edge lengths can still differ.

The independent baseline has no edges. The spatial graph chooses shortest Euclidean pairs with deterministic index tie-breaking. The pathway graph prioritizes pairs in the same synthetic column before cross-column neighbors.

**Failure mode:** a graph can encode the answer if selected using test labels. Constructors use coordinates only.

**Code:** [graphs](../src/tactile_lab/pathways/graphs.py). **Background:** [graph signal processing survey](https://arxiv.org/abs/1211.0053).
