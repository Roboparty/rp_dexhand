# Sensing, receptive fields and biological inspiration

A receptive field describes which region of input space influences a response. In this software, a sensor node's one-step graph neighborhood is an explicitly defined computational receptive field.

After k graph steps, a node may depend on nodes reachable through up to k edges. This follows by expanding repeated multiplication by a graph update matrix when observations are complete. Missing-data normalization makes the operator input-mask dependent, but the connectivity restriction still matters.

Example: in the default pathway graph, all four nodes in a column are directly connected. A single step already mixes evidence across the column, while no number of steps transfers evidence between disconnected columns.

**Why used:** it gives a precise computational meaning to pathway-inspired sensing without pretending that graph edges are biological nerves or Qi channels.

Biological touch involves specialized receptors and neural processing. This project does not reproduce their anatomy or prove correspondence to traditional meridians. It uses a conceptual question—where should information be combined?—to define an engineering experiment.

**Failure mode:** using biological terminology can hide an ordinary averaging algorithm. Always name the actual computation and inspect its causal dependencies.

**Code:** [graphs](../src/tactile_lab/pathways/graphs.py), [topology](../src/tactile_lab/pathways/topology.py).
