"""Regression checks for the offline documentation validator."""
import subprocess
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


if __name__ == '__main__':
    unittest.main()
