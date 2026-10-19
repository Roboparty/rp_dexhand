import numpy as np
import pytest
from tactile_lab.receivers import CausalReceiver, ReceiverConfig

@pytest.mark.parametrize("mode",["raw","fixed","adaptive"])
def test_future_changes_do_not_affect_prefix(mode):
    x=np.linspace(0,1,100); y=x.copy(); y[60:]=1000
    a=CausalReceiver(mode).replay(x); b=CausalReceiver(mode).replay(y)
    np.testing.assert_allclose(a[:60],b[:60],equal_nan=True)

@pytest.mark.parametrize("mode",["raw","fixed","adaptive"])
def test_chunk_replay_matches_sample_updates(mode):
    x=np.sin(np.arange(100))
    one=CausalReceiver(mode).replay(x)
    r=CausalReceiver(mode); chunks=np.r_[r.replay(x[:33]),r.replay(x[33:])]
    np.testing.assert_allclose(one,chunks,equal_nan=True)
