import pytest
from tactile_lab.receivers import ReceiverConfig, CausalReceiver

@pytest.mark.parametrize("field,value", [("baseline_alpha",0),("noise_alpha",1.1),("envelope_alpha",float("nan")),("noise_floor",0),("initial_noise",-1),("adaptation_gate",float("inf")),("warmup_samples",True),("warmup_samples",-1)])
def test_invalid_parameters(field,value):
    with pytest.raises(ValueError): ReceiverConfig(**{field:value})

def test_bad_mode():
    with pytest.raises(ValueError): CausalReceiver("noncausal")
def test_replay_rejects_matrix():
    with pytest.raises(ValueError): CausalReceiver().replay([[1,2],[3,4]])
