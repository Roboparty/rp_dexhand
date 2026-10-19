# Reproducibility, seeds and artifact hashes

A pseudorandom seed fixes a computational sampling stream. Repeating a seed and configuration should reproduce deterministic scientific results in the same supported numerical environment. It does not make a synthetic model true or provide independent physical replication.

Configuration hashes use SHA-256 of canonical JSON with sorted keys. For example, dictionaries with keys inserted in different orders hash identically when their content matches. Changing a numerical parameter changes the serialized content and normally its hash.

**Why used:** each result can be associated with a specific configuration rather than a vague label such as latest run.

The provenance file separately records Python, NumPy, package version, operating system, Git revision and working-tree state. Timing metadata and source revision are not mixed into a deterministic scientific-content hash.

**Failure modes:** a seed alone is insufficient when generator code changes. A configuration hash is not a cryptographic signature of scientific validity. Floating-point changes across environments can alter exact numerical bytes.

**Code:** [artifact serialization](../src/tactile_lab/evaluation/artifacts.py), [provenance](../src/tactile_lab/evaluation/provenance.py).
