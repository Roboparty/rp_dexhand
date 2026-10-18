from pathlib import Path
import subprocess
import sys
import pytest

@pytest.mark.parametrize("example",["calibration_demo.py","pathway_demo.py","receiver_demo.py"])
def test_example_executes(example):
    root=Path(__file__).resolve().parents[1]
    completed=subprocess.run([sys.executable,str(root/"examples"/example)],capture_output=True,text=True,check=True)
    assert completed.stdout.strip()
