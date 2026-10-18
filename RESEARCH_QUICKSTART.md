# Run the tactile research lab

This release runs synthetic experiments and CSV replay. It does not command a robot.

## Install

Use Python 3.10 or newer in a local virtual environment.

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m tactile_lab benchmark --experiment all --output runs/demo
```

Linux/macOS:
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest -q
.venv/bin/python -m tactile_lab benchmark --experiment all --output runs/demo
```

If an embedded Python runtime cannot import the isolated build backend, install `setuptools wheel` inside this virtual environment and retry the editable install with `--no-build-isolation`. That fallback was used on the local bundled Windows runtime; it does not require changing the system Python.

## Inspect results

Each run writes JSON with configurations, candidate scores, selected thresholds and held-out trial results, plus Markdown summaries and a provenance file. Read recall, false alarms and delay together. Missing latency is unavailable, not zero.

Select `pathways`, `receivers`, `combined`, or `ablation` with `--experiment`. Start learning at [knowledge/README.md](knowledge/README.md).

## Replay a recording

```powershell
.\.venv\Scripts\python.exe -m tactile_lab replay data/example-synthetic.csv runs/replay.csv --mode adaptive --unit arbitrary --source synthetic
```

This writes scores only. It does not calibrate a threshold or connect to hardware. For a measured recording, declare `--source measured` and its actual units, after meeting [the data contract](data/README.md).

## Robustness study

```powershell
.\.venv\Scripts\python.exe -m tactile_lab sweep --seeds 42 43 44 --output runs/robustness
```

Retain every seed's result. Do not pick the best seed or describe synthetic repetitions as real-device replication.
