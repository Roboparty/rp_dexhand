# Causality and streaming equivalence

A causal score at index n depends only on inputs x[0], …, x[n] and prior internal state. It cannot use x[n+1] or a future event label.

Formally, if two input sequences share the same prefix through n, their output prefixes must match. The causality tests replace the future with very large values and verify that earlier scores do not change.

Streaming equivalence is related: processing one array or several consecutive chunks through the same receiver state must produce the same scores. Creating a new receiver for every chunk resets its baseline and noise estimate and is not equivalent.

**Worked example:** a receiver sees 0, 0, 1. Its score at the second zero cannot depend on whether the next value will be 1 or 1000. A centered moving average would violate this property unless delayed until future samples arrive.

**Why used:** offline methods can appear accurate by looking ahead. The project is intended to support later online sensing, so time direction is a correctness requirement.

**Assumptions:** samples arrive in chronological order. CSV replay validates time order; the raw sample API expects the caller to honor it.

**Code:** [detectors](../src/tactile_lab/receivers/detectors.py), [tests](../tests/test_receiver_causality.py).
