# The two-by-two factorial comparison

Two factors are varied: graph topology (spatial/pathway) and receiver (fixed/adaptive). Four conditions use the same synthetic multichannel trials.

Let R_SF, R_SA, R_PF and R_PA denote event recall. The pathway contribution at the fixed receiver is R_PF − R_SF. The adaptation contribution at spatial topology is R_SA − R_SF. A descriptive interaction is:

$$I=R_{PA}-R_{PF}-R_{SA}+R_{SF}.$$

Example: recalls 0.4, 0.6, 0.5 and 0.7 give I = 0: the observed changes add on this scale. If the last recall is 0.9, I = 0.2.

**Why used:** changing graph and receiver together cannot reveal which contributes to an improvement.

**Limits:** recall is bounded; interaction depends on the chosen metric scale. Each condition has a separately validation-calibrated threshold, so report false alarms and delays too. These are descriptive effects, not causal biological effects or significance tests.

The combined experiment freezes diffusion strength at 0.35 and uses maximum-channel score fusion. It does not reuse the pathway benchmark's selected zero-smoothing option.

**Code:** [combined benchmark](../src/tactile_lab/combined.py).
