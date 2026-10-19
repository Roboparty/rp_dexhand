import numpy as np
from tactile_lab.receivers.synthetic import Trial
from tactile_lab.receivers.training import select_threshold

def test_select_rejects_high_recall_with_false_alarms():
    t=Trial("v","s","o","validation","x",100.,np.zeros(100),((50,60),))
    scores=np.zeros(100); scores[10]=1; scores[52]=2
    threshold,choices=select_threshold([t],[scores],[.5,1.5,3],0.)
    assert threshold==1.5
    assert choices[0]["false_alarms_per_minute"]>0
