from types import SimpleNamespace as S
import pytest
from tactile_lab.evaluation import validate_splits

def data():
    return [S(split=s,trial_id=s,session_id=s,object_id=s) for s in ("train","validation","test")]
def test_valid_splits():
    assert validate_splits(data())["test"]=={"sessions":1,"objects":1,"trials":1}
@pytest.mark.parametrize("field",["session_id","object_id","trial_id"])
def test_leakage(field):
    rows=data(); setattr(rows[2],field,getattr(rows[0],field))
    with pytest.raises(ValueError): validate_splits(rows)
def test_missing_split():
    with pytest.raises(ValueError): validate_splits(data()[:2])
