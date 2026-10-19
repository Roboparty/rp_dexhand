import numpy as np
from tactile_lab.pathways import generate_trials
from tactile_lab.evaluation import validate_splits

def test_seed_reproduction():
    a=generate_trials(42,8); b=generate_trials(42,8); c=generate_trials(43,8)
    for x,y in zip(a,b): np.testing.assert_allclose(x.values,y.values,equal_nan=True)
    assert not np.allclose(a[0].values,c[0].values)

def test_splits_are_isolated():
    data=[t for split in ("train","validation","test") for t in generate_trials(42,8,split)]
    assert validate_splits(data)["test"]["trials"]==8

def test_dropout_counts():
    data=generate_trials(42,4)
    assert [np.isnan(t.values).sum() for t in data]==[0,0,1,4]
