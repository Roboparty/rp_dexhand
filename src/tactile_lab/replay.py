"""Observation-only replay: output scores, never motor commands."""
import csv
from pathlib import Path
import numpy as np
from .recording import load_csv
from .receivers import CausalReceiver, ReceiverConfig

def replay_csv(input_path, output_path, mode="fixed", unit="arbitrary", source="synthetic", config=None):
    if Path(input_path).resolve() == Path(output_path).resolve():
        raise ValueError("output must not overwrite raw input")
    recording = load_csv(input_path, unit, source)
    receiver = CausalReceiver(mode, config or ReceiverConfig())
    scores = receiver.replay(recording.samples)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream)
        writer.writerow(["timestamp_s", "value", "score", "decision_available"])
        for t, value, score in zip(recording.timestamps_s, recording.samples, scores):
            writer.writerow([t, value if np.isfinite(value) else "", score if np.isfinite(score) else "", int(np.isfinite(score))])
    return {"samples": len(scores), "observed_scores": int(np.isfinite(scores).sum()),
            "sample_rate_hz": recording.sample_rate_hz, "unit": unit, "source": source,
            "mode": mode, "note": "scores only; no threshold calibration or physical control"}
