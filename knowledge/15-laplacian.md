# Graph Laplacian and the implemented diffusion

For adjacency A and diagonal degree matrix D, the combinatorial Laplacian is L = D − A. Its quadratic form xᵀLx = Σ_(i,j in edges)(x_i − x_j)² measures disagreement across undirected edges.

Example: two connected nodes with readings 2 and 6 give disagreement (2−6)² = 16. Equal readings give zero. Smoothness here means agreement along the chosen graph, not necessarily physical truth.

With complete observations and nonzero degrees, the implemented update is x_new = (1−alpha)x + alpha D⁻¹Ax, equivalently x − alpha(I−D⁻¹A)x. This is a random-walk-normalized diffusion step, not an eigendecomposition or learned graph neural network.

**Why used:** averaging can reduce independent noise when neighbors measure related phenomena.

**Failure mode:** real contact may be sharply localized. Smoothing can spread a true peak and worsen localization. Missing observations also make the normalization depend on the current observation mask, so a single fixed linear operator no longer fully describes the algorithm.

**Code:** [diffuse](../src/tactile_lab/pathways/filtering.py). **Background:** [graph signal processing survey](https://arxiv.org/abs/1211.0053).
