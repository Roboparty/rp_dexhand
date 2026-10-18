# Nuisance controls and alternative explanations

A detector can respond to the wrong cause while achieving a plausible-looking trace. Controls test this possibility.

The scalar generator includes clean events, weak events, motor-only vibration, no contact, drifting baseline plus an event, dropout during an event, noise-level change without an event, and a short event. These are controlled synthetic challenges, not measured device categories.

A motor-only sinusoid at 30 Hz produces oscillating residual magnitude even with no contact. If the receiver alarms, it has detected signal change, not necessarily slip. The noise-change scenario similarly challenges adaptation without adding a positive event label.

**Why used:** positive examples alone cannot establish selectivity. A hand needs to avoid unnecessary grip changes during unrelated disturbances.

**Worked reasoning:** if a model improves event recall but also alarms on most motor-only trials, its apparent sensitivity may simply reflect a lower threshold. Evaluate recall at a constrained operating point and still inspect the achieved test false-alarm rate.

**Failure modes:** controls can be too easy or too unlike hardware. Add measured actuator vibration and independent physical slip labels before claiming practical robustness.

**Code:** [SCENARIOS and generator](../src/tactile_lab/receivers/synthetic.py).
