import numpy as np
from tactile_lab.pathways import diffuse

A=np.array([[0,1],[1,0]],float)
def test_hand_computed_step():
    np.testing.assert_allclose(diffuse([2,6],A,.25),[3,5])

def test_no_evidence_stays_missing():
    assert np.isnan(diffuse([np.nan,np.nan],A)).all()

def test_imputation_and_isolation():
    np.testing.assert_allclose(diffuse([2,np.nan],A,.5),[2,2])
    result=diffuse([np.nan,2],np.zeros((2,2)))
    assert np.isnan(result[0]) and result[1]==2

def test_batch_matches_individual():
    x=np.array([[2,6],[4,np.nan]])
    np.testing.assert_allclose(diffuse(x,A),np.stack([diffuse(row,A) for row in x]),equal_nan=True)

def test_zero_strength_preserves_missingness():
    x=np.array([1,np.nan])
    np.testing.assert_allclose(diffuse(x,A,0),x,equal_nan=True)
