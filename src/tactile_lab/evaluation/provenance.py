"""Execution metadata, kept separate from deterministic scientific results."""
import platform
import subprocess
import numpy as np
from tactile_lab import __version__

def provenance():
    try:
        revision = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, timeout=5, check=True).stdout.strip()
        dirty = bool(subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, timeout=5, check=True).stdout)
    except (OSError, subprocess.SubprocessError):
        revision, dirty = None, None
    return {"package_version": __version__, "python": platform.python_version(), "numpy": np.__version__,
            "platform": platform.system(), "git_revision": revision, "working_tree_dirty": dirty,
            "evidence": "synthetic and offline replay; no physical hand commands"}
