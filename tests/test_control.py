import pytest
from tactile_lab.control import propose_grip

def kwargs():
    return dict(age_s=.01,homed=True,stopped=False,force_n=1)
@pytest.mark.parametrize("change", [{"age_s":.1},{"homed":False},{"stopped":True},{"force_n":5}])
def test_blocked(change):
    options=kwargs(); options.update(change)
    r=propose_grip(.5,True,**options)
    assert r.command==.5 and not r.allowed
def test_increment_is_bounded():
    assert propose_grip(.999,True,**kwargs()).command==1
    assert propose_grip(.5,False,**kwargs()).command==.5
def test_nonfinite_input():
    options=kwargs(); options["force_n"]=float("nan")
    with pytest.raises(ValueError): propose_grip(.5,True,**options)
