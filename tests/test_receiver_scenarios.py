import numpy as np
from tactile_lab.receivers.synthetic import generate_dataset, SCENARIOS
from tactile_lab.evaluation import validate_splits

def test_scenario_coverage_and_labels():
    data=generate_dataset(1,1)
    assert len(data)==24
    assert {t.scenario for t in data}==set(SCENARIOS)
    for t in data:
        if t.scenario in ("motor_only","no_contact","noise_change"): assert not t.events
        else:
            assert len(t.events)==1
            assert 0<=t.events[0][0]<t.events[0][1]<=len(t.samples)
    assert validate_splits(data)["test"]["trials"]==8

def test_repeatability():
    for a,b in zip(generate_dataset(4,1),generate_dataset(4,1)):
        np.testing.assert_allclose(a.samples,b.samples,equal_nan=True)
