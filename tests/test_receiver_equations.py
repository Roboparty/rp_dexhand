import numpy as np
from tactile_lab.receivers import ReceiverConfig,CausalReceiver

def test_fixed_residual_and_envelope():
    c=ReceiverConfig(baseline_alpha=.5,envelope_alpha=.5,warmup_samples=0)
    r=CausalReceiver("fixed",c)
    assert r.update(2)==0
    assert r.update(4)==1
    assert r.baseline==3
    assert r.update(5)==1.5

def test_adaptive_score_uses_previous_noise():
    c=ReceiverConfig(baseline_alpha=.5,envelope_alpha=.5,noise_alpha=.5,initial_noise=1,warmup_samples=0)
    r=CausalReceiver("adaptive",c)
    r.update(0)
    # noise became .5; next envelope is 1, so score is 2 before noise update.
    assert r.update(2)==2

def test_raw_output_is_absolute_input():
    r=CausalReceiver("raw",ReceiverConfig(warmup_samples=0))
    assert r.update(-3)==3
