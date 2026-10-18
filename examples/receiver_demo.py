"""Print the receiver states for an explicitly synthetic transient."""
from tactile_lab.receivers import CausalReceiver,ReceiverConfig
config=ReceiverConfig(baseline_alpha=.5,envelope_alpha=.5,warmup_samples=0)
receiver=CausalReceiver("fixed",config)
for value in [2.,4.,5.,5.,5.]:
    score=receiver.update(value)
    print(f"input={value:.1f}, baseline={receiver.baseline:.3f}, envelope={score:.3f}")
print("A constant contact is absorbed into the moving baseline; this is a transient detector.")
