import numpy as np
from tactile_lab.receivers import CausalReceiver, ReceiverConfig

def test_missing_freezes_state():
    r=CausalReceiver(); r.update(1)
    old=(r.baseline,r.envelope,r.noise,r.valid_samples)
    assert np.isnan(r.update(np.nan))
    assert old==(r.baseline,r.envelope,r.noise,r.valid_samples)

def test_warmup_counts_valid_only():
    r=CausalReceiver(config=ReceiverConfig(warmup_samples=2))
    assert np.isnan(r.update(0)) and np.isnan(r.update(np.nan)) and np.isnan(r.update(1))
    assert np.isfinite(r.update(1))

def test_reset_reproduces_first_run():
    r=CausalReceiver(); x=np.arange(80)
    a=r.replay(x); r.reset(); b=r.replay(x)
    np.testing.assert_allclose(a,b,equal_nan=True)
