import pytest
from tactile_lab.evaluation.uncertainty import paired_interval,wilson_interval

def test_constant_paired_difference():
    r=paired_interval([2,3,4],[1,2,3])
    assert r["mean_delta"]==1 and r["interval_95"]==[1,1]
def test_no_successes_still_has_upper_uncertainty():
    low,high=wilson_interval(0,10)
    assert low==0 and .27<high<.29
def test_all_successes_not_certainty():
    low,high=wilson_interval(10,10)
    assert .71<low<.73 and high==pytest.approx(1)
@pytest.mark.parametrize("a,b", [([],[]),([1],[1]),([1,2],[1]),([1,float("nan")],[1,2])])
def test_invalid_pairs(a,b):
    with pytest.raises(ValueError): paired_interval(a,b)
