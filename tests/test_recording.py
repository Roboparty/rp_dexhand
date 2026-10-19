import numpy as np
import pytest
from tactile_lab.recording import load_csv

def file(tmp_path,text):
    p=tmp_path/"samples.csv"; p.write_text(text); return p
def test_valid_recording(tmp_path):
    p=file(tmp_path,"timestamp_s,value\n0,1\n.005,\n.010,2\n")
    r=load_csv(p,"N","measured")
    assert r.sample_rate_hz==200 and np.isnan(r.samples[1])
@pytest.mark.parametrize("times",["0,1\n0,2\n.01,3","0,1\n.005,2\n.02,3","0,1\nnan,2\n.01,3"])
def test_bad_timestamps(tmp_path,times):
    with pytest.raises(ValueError): load_csv(file(tmp_path,"timestamp_s,value\n"+times),"N","measured")
def test_missing_source_declaration(tmp_path):
    with pytest.raises(ValueError): load_csv(file(tmp_path,""),"","unknown")
