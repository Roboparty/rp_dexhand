import numpy as np
import pytest
from tactile_lab.calibration import fit_linear

def test_known_calibration():
    model=fit_linear([0,1,2],[1,3,5])
    np.testing.assert_allclose(model.apply([.5,1.5]),[2,4])
    assert abs(model.gain-2)<1e-12 and abs(model.offset-1)<1e-12 and model.rmse<1e-12
    assert model.unit=="N"
def test_extrapolation_requires_explicit_choice():
    model=fit_linear([0,1,2],[1,3,5])
    with pytest.raises(ValueError): model.apply(3)
    assert abs(model.apply(3,allow_extrapolation=True)-7)<1e-12
@pytest.mark.parametrize("raw,reference", [([1,1,1],[1,2,3]),([1,2],[1,2]),([1,2,3],[1,2]),([1,2,3],[1,float("nan"),3])])
def test_invalid_fit(raw,reference):
    with pytest.raises(ValueError): fit_linear(raw,reference)
