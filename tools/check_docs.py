"""Offline checks for local documentation links, Python examples and resource records."""
import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

FENCES = re.compile(r"^```([^\n]*)\n(.*?)^```\s*$", re.M | re.S)
LINKS = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)|(?:href|src)="([^"]+)"')


def anchors(text):
    result, counts = set(), {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"[\s]+", "-", re.sub(r"[^\w\-\s]", "", heading.lower()))
        count = counts.get(heading, 0)
        result.add(heading if count == 0 else f"{heading}-{count}")
        counts[heading] = count + 1
    result.update(re.findall(r'(?:id|name)="([^"]+)"', text))
    return result


def check(root):
    errors = []
    documents = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    for path in documents:
        text = path.read_text(encoding="utf-8")
        for language, body in FENCES.findall(text):
            if language.strip() == "python":
                try:
                    ast.parse(body)
                except SyntaxError as exc:
                    errors.append(f"{path.relative_to(root)}: Python syntax: {exc.msg}")
        text = FENCES.sub("", text)
        for md_link, html_link in LINKS.findall(text):
            link = md_link or html_link
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{path.relative_to(root)}: link escapes repository: {link}")
                continue
            if not target.exists():
                errors.append(f"{path.relative_to(root)}: missing local link: {link}")
            elif parsed.fragment and target.suffix.lower() == ".md":
                if unquote(parsed.fragment) not in anchors(FENCES.sub("", target.read_text(encoding="utf-8"))):
                    errors.append(f"{path.relative_to(root)}: missing heading: {link}")
    for sums in root.glob("assets/SHA256SUMS.txt"):
        for line in sums.read_text(encoding="utf-8").splitlines():
            digest, name = line.split(maxsplit=1)
            asset = root / name
            if not asset.is_file() or hashlib.sha256(asset.read_bytes()).hexdigest() != digest:
                errors.append(f"Asset checksum mismatch: {name}")
    for manifest in root.glob("resources/*/manifest.json"):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        sums = dict(line.split(maxsplit=1)[::-1] for line in
                    manifest.with_name("SHA256SUMS.txt").read_text(encoding="utf-8").splitlines() if line.strip())
        names = set()
        for asset in data["assets"]:
            name = asset["filename"]
            if name in names or sums.get(name) != asset["sha256"]:
                errors.append(f"Resource manifest/checksum mismatch: {name}")
            names.add(name)
        if names != set(sums):
            errors.append(f"Resource file list differs: {manifest.parent.name}")
    return documents, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    documents, errors = check(args.root.resolve())
    for error in errors:
        print(error)
    print(f"Checked {len(documents)} Markdown files; {len(errors)} errors. External URLs and hardware behavior are not tested.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
