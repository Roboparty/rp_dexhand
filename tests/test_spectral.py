import numpy as np
import pytest
from tactile_lab.spectral import coherence,estimate_lag

def test_identical_sine_has_unit_peak_coherence():
    t=np.arange(512)/200
    x=np.sin(2*np.pi*25*t)
    r=coherence(x,x,200)
    k=np.argmin(abs(r["frequency_hz"]-25))
    assert r["coherence"][k]==pytest.approx(1)

def test_zero_signal_has_undefined_coherence():
    assert np.isnan(coherence(np.zeros(512),np.zeros(512),200)["coherence"]).all()

def test_delayed_pulse_lag():
    x=np.zeros(100); x[30:33]=[1,3,1]
    y=np.zeros(100); y[35:38]=[1,3,1]
    assert estimate_lag(x,y,10)==5

def test_short_record_rejected():
    with pytest.raises(ValueError): coherence(np.ones(128),np.ones(128),200)
