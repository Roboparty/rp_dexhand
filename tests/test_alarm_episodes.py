import numpy as np
from tactile_lab.receivers.metrics import alarm_onsets

def test_continuous_signal_is_one_alarm():
    assert alarm_onsets([0,2,2,2,0],1)==[1]

def test_refractory_and_missing_gap():
    assert alarm_onsets([0,2,0,2,0,0,2],1,3)==[1,6]
    assert alarm_onsets([2,np.nan,2],1,0)==[0,2]

def test_threshold_is_strict():
    assert alarm_onsets([1,1,1],1)==[]
