import json
import numpy as np
import pytest
from tactile_lab.evaluation.artifacts import canonical_json,content_hash,write_json

def test_order_independent_hash():
    assert content_hash({"a":1,"b":2})==content_hash({"b":2,"a":1})
    assert content_hash({"a":1})!=content_hash({"a":2})
def test_numpy_conversion():
    assert json.loads(canonical_json({"a":np.array([1,2]),"b":np.float64(3)}))=={"a":[1,2],"b":3}
def test_no_nonstandard_nan():
    with pytest.raises(ValueError): canonical_json({"a":np.nan})
def test_atomic_output(tmp_path):
    p=tmp_path/"nested"/"result.json"
    write_json(p,{"ok":True})
    assert json.loads(p.read_text())=={"ok":True}
    assert not list(p.parent.glob("*.tmp"))
