import numpy as np
from tactile_lab.pathways import localize

P=np.array([[0,0],[10,0],[0,10]])
def test_weighted_centroid():
    np.testing.assert_allclose(localize([1,3,0],P),[7.5,0])
def test_negative_pressure_not_evidence():
    np.testing.assert_allclose(localize([-2,1,np.nan],P),[10,0])
def test_no_contact_is_not_origin():
    assert np.isnan(localize([0,0,0],P)).all()
def test_scale_invariance():
    np.testing.assert_allclose(localize([1,2,3],P),localize([10,20,30],P))
