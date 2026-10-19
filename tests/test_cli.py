import json
import pytest
from tactile_lab.cli import main

def test_pathway_cli_writes_artifacts(tmp_path):
    assert main(["benchmark","--experiment","pathways","--output",str(tmp_path)])==0
    result=json.loads((tmp_path/"pathways.json").read_text())
    assert result["experiment"]=="pathway_graph"
    assert (tmp_path/"provenance.json").exists()
    assert "synthetic" in (tmp_path/"pathways.md").read_text()
def test_negative_seed_rejected(tmp_path):
    with pytest.raises(SystemExit): main(["benchmark","--seed","-1","--output",str(tmp_path)])
