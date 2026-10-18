import numpy as np
import pytest
from tactile_lab.receivers.synthetic import Trial

@pytest.mark.parametrize("events", [((-1,2),),((2,11),),((3,2),),((1,5),(4,8)),((1.5,3),),((True,3),)])
def test_invalid_events(events):
    with pytest.raises(ValueError): Trial("t","s","o","test","x",100,np.zeros(10),events)
@pytest.mark.parametrize("rate",[0,-1,float("nan")])
def test_invalid_rate(rate):
    with pytest.raises(ValueError): Trial("t","s","o","test","x",rate,np.zeros(10),())
def test_infinity_not_missing():
    with pytest.raises(ValueError): Trial("t","s","o","test","x",100,np.array([np.inf]),())
