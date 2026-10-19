import csv
import pytest
from tactile_lab.replay import replay_csv
from tactile_lab.receivers import ReceiverConfig

def test_output_and_raw_preservation(tmp_path):
    p=tmp_path/"in.csv"; original="timestamp_s,value\n0,1\n.005,\n.010,2\n"; p.write_text(original)
    out=tmp_path/"out.csv"
    summary=replay_csv(p,out,config=ReceiverConfig(warmup_samples=0))
    rows=list(csv.DictReader(out.open()))
    assert rows[1]["score"]=="" and rows[1]["decision_available"]=="0"
    assert summary["observed_scores"]==2 and p.read_text()==original
def test_reject_overwrite(tmp_path):
    p=tmp_path/"data.csv"
    with pytest.raises(ValueError): replay_csv(p,p)
