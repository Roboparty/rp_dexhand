import numpy as np
import pytest
from tactile_lab.pathways.evaluation import evaluate, paired_comparison
from tactile_lab.pathways.synthetic import ContactTrial

def test_all_missing_is_explicit_failure():
    t=ContactTrial("t","s","o","test","missing",np.array([np.nan,np.nan]),np.array([0,0]))
    row=evaluate([t],[[0,0],[3,4]],np.zeros((2,2)),0)[0]
    assert row["error_mm"]==5 and row["failed"] and row["estimate_mm"] is None

def test_misaligned_pairs_rejected():
    with pytest.raises(ValueError):
        paired_comparison([{"trial_id":"a","error_mm":1}],[{"trial_id":"b","error_mm":2}])

def test_identical_models_have_zero_interval():
    rows=[{"trial_id":str(i),"error_mm":float(i)} for i in range(4)]
    result=paired_comparison(rows,rows)
    assert result["bootstrap_95pct_interval_mm"]==[0,0]
