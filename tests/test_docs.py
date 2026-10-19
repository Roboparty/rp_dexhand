"""Regression checks for the offline documentation validator."""
import subprocess
import json
import sys
import tempfile
import unittest
from pathlib import Path

CHECKER = Path(__file__).resolve().parents[1] / "tools/check_docs.py"


class DocumentationChecks(unittest.TestCase):
    def run_check(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return subprocess.run([sys.executable, "-X", "utf8", str(CHECKER), "--root", str(root)],
                                  capture_output=True, text=True, encoding="utf-8")

    def test_linked_bilingual_guide_and_html_image(self):
        result = self.run_check({"README.md": '[Guide](docs/start.md#setup)\n<img src="assets/hand.svg">',
                                 "docs/start.md": '# Setup\n[Home](../README.md)\n',
                                 "assets/hand.svg": '<svg/>'})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_broken_file_fails(self):
        result = self.run_check({"README.md": '[Guide](docs/missing.md)'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing.md', result.stdout)

    def test_typo_in_heading_fragment_fails(self):
        result = self.run_check({"README.md": '[Guide](docs/start.md#setpu)',
                                 "docs/start.md": '# Setup\n'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('setpu', result.stdout)

    def test_code_sample_is_not_a_markdown_link(self):
        result = self.run_check({"README.md": '```python\na = [0](1)\n```\n'})
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_invalid_python_snippet_fails(self):
        result = self.run_check({"README.md": '```python\nif True\n    pass\n```\n'})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Python', result.stdout)

    def resource_files(self, digest, sums):
        return {
            'README.md': '# Resources\n',
            'resources/test/manifest.json': json.dumps({'assets': [
                {'filename': 'sample.zip', 'sha256': digest}]}),
            'resources/test/SHA256SUMS.txt': sums,
        }

    def test_valid_resource_records_pass(self):
        digest = 'a' * 64
        result = self.run_check(self.resource_files(digest, digest + '  sample.zip\n'))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_non_sha256_resource_digest_fails(self):
        result = self.run_check(self.resource_files('oops', 'oops  sample.zip\n'))
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Invalid SHA-256', result.stdout)

    def test_conflicting_duplicate_checksum_filename_fails(self):
        digest = 'a' * 64
        sums = 'b' * 64 + '  sample.zip\n' + digest + '  sample.zip\n'
        result = self.run_check(self.resource_files(digest, sums))
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Duplicate checksum filename', result.stdout)

    def test_model_inspection_archive_digest_must_match_manifest(self):
        digest = 'a' * 64
        files = self.resource_files(digest, digest + '  sample.zip\n')
        files['resources/model-inspection-test.json'] = json.dumps({
            'archive': 'sample.zip', 'archive_sha256': 'b' * 64})
        result = self.run_check(files)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn('Model inspection archive mismatch', result.stdout)


if __name__ == '__main__':
    unittest.main()
