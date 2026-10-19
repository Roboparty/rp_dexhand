import numpy as np
from tactile_lab.receivers.synthetic import Trial
from tactile_lab.receivers.metrics import evaluate_trial, aggregate

def trial():
    return Trial("t","s","o","test","event",100.,np.zeros(10),((4,8),))

def test_event_match_false_alarm_and_latency():
    score=np.array([0,2,0,0,0,2,2,0,0,0],float)
    r=evaluate_trial(trial(),score,1,0)
    assert r["false_alarms"]==1 and r["detected_events"]==1
    assert r["detection_delays_ms"]==[10.]
    assert np.isclose(r["background_minutes"],6/100/60)

def test_miss_latency_is_null():
    r=evaluate_trial(trial(),np.zeros(10),1)
    s=aggregate([r])
    assert s["recall"]==0 and s["median_detected_latency_ms"] is None

def test_missing_background_not_counted_as_exposure():
    score=np.zeros(10); score[:2]=np.nan
    r=evaluate_trial(trial(),score,1)
    assert np.isclose(r["background_minutes"],4/100/60)

def test_alarm_before_event_does_not_count_as_detection():
    score=np.ones(10)*2
    assert evaluate_trial(trial(),score,1)["detected_events"]==0
