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
SHA256 = re.compile(r"[0-9a-fA-F]{64}")


def checksum_records(path, root, errors):
    records = {}
    if not path.is_file():
        errors.append(f"Missing checksum file: {path.relative_to(root)}")
        return records
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64}) [ *](.+)", line)
        if match is None:
            errors.append(f"Invalid SHA-256 record: {path.relative_to(root)}:{number}")
            continue
        digest, name = match.groups()
        if name in records:
            errors.append(f"Duplicate checksum filename: {name}")
            continue
        records[name] = digest.lower()
    return records


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
        for name, digest in checksum_records(sums, root, errors).items():
            asset = root / name
            if not asset.is_file() or hashlib.sha256(asset.read_bytes()).hexdigest() != digest:
                errors.append(f"Asset checksum mismatch: {name}")
    archive_records = {}
    for manifest in root.glob("resources/*/manifest.json"):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        sums = checksum_records(manifest.with_name("SHA256SUMS.txt"), root, errors)
        names = set()
        for asset in data["assets"]:
            name = asset["filename"]
            digest = asset["sha256"]
            valid = isinstance(digest, str) and SHA256.fullmatch(digest) is not None
            if not valid:
                errors.append(f"Invalid SHA-256 in manifest: {name}")
            if name in names or not valid or sums.get(name) != digest.lower():
                errors.append(f"Resource manifest/checksum mismatch: {name}")
            names.add(name)
            if valid:
                archive_records.setdefault(name, set()).add(digest.lower())
        if names != set(sums):
            errors.append(f"Resource file list differs: {manifest.parent.name}")
    for inspection in root.glob("resources/model-inspection-*.json"):
        data = json.loads(inspection.read_text(encoding="utf-8"))
        digest = data.get("archive_sha256", "")
        if not isinstance(digest, str) or digest.lower() not in archive_records.get(data.get("archive"), set()):
            errors.append(f"Model inspection archive mismatch: {inspection.name}")
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
