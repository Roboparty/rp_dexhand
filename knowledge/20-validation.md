# Training, validation and test boundaries

Training estimates quantities such as initial background scale. Validation selects a configuration or threshold. Test reports performance after selection is frozen.

Let theta_star = argmin_theta L_validation(theta). The reported test loss is L_test(theta_star), not min_theta L_test(theta). Minimizing the latter uses the test data to choose the answer.

The pathway model has no trained weights; its training split is reserved, and diffusion strength is selected using validation. The receiver fits initial noise from training background, constructs candidate thresholds from training scores, and chooses a threshold by validation recall under a false-alarm constraint.

**Example:** validation errors for strengths 0 and 0.35 are 3.0 and 3.4 mm. Choose 0 even if a peek at test would favor 0.35.

**Why used:** comparisons should measure transfer to observations not used in selection.

**Failure modes:** adjacent frames from one trial leak context across random frame splits. The split checker rejects shared session/object identifiers and duplicated trial IDs. It cannot detect mislabeled IDs or duplicated measurements disguised under new names.

**Code:** [split checks](../src/tactile_lab/evaluation/splits.py), [receiver fitting](../src/tactile_lab/receivers/training.py).
