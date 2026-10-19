"""Portable, strict JSON with provenance; atomic replacement of result files."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
import numpy as np

def native(value):
    if isinstance(value, np.ndarray):
        return native(value.tolist())
    if isinstance(value, np.generic):
        return native(value.item())
    if isinstance(value, dict):
        return {str(k): native(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [native(v) for v in value]
    if isinstance(value, float) and not np.isfinite(value):
        raise ValueError("nonfinite result: represent unavailable quantities explicitly as null")
    return value

def canonical_json(value):
    return json.dumps(native(value), sort_keys=True, ensure_ascii=False, allow_nan=False, separators=(",", ":"))

def content_hash(value):
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()

def write_json(path, value):
    path = Path(path)
    payload = json.dumps(native(value), indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)+"\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False, suffix=".tmp") as stream:
            temporary = stream.name
            stream.write(payload)
        os.replace(temporary, path)
    finally:
        if temporary and Path(temporary).exists():
            Path(temporary).unlink()
