"""Check local Markdown destinations and preserved upstream asset checksums."""
import hashlib
from pathlib import Path
import re
import sys

def check(root):
    root=Path(root); errors=[]; count=0
    excluded={".git",".venv","runs","build","dist"}
    for path in root.rglob("*.md"):
        if excluded.intersection(path.relative_to(root).parts): continue
        text=path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)",text):
            target=target.strip("<>").split("#")[0]
            if not target or "://" in target or target.startswith("mailto:"): continue
            count+=1
            if not (path.parent/target).exists(): errors.append(f"{path.relative_to(root)}: {target}")
    for line in (root/"assets"/"SHA256SUMS.txt").read_text().splitlines():
        expected,name=line.split(maxsplit=1)
        file=root/name.lstrip("*")
        if hashlib.sha256(file.read_bytes()).hexdigest()!=expected: errors.append(f"asset checksum: {name}")
    return count,errors

if __name__=="__main__":
    count,errors=check(Path(__file__).resolve().parents[1])
    print(f"Checked {count} local Markdown links and 3 original asset hashes.")
    for error in errors: print(error)
    sys.exit(bool(errors))
