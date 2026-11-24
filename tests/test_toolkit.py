import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


class ToolkitStructureTests(unittest.TestCase):
    def test_mcp_config_example_valid_json(self) -> None:
        data = json.loads((ROOT / "mcp_config.example.json").read_text(encoding="utf-8"))
        self.assertIn("mcpServers", data)
        for server in ("playwright", "context7", "postgres", "github"):
            self.assertIn(server, data["mcpServers"])

    def test_agents_and_skills_have_frontmatter(self) -> None:
        agents = list((ROOT / ".claude" / "agents").glob("*.md"))
        skills = list((ROOT / ".claude" / "skills").glob("*/SKILL.md"))
        self.assertGreaterEqual(len(agents), 3)
        self.assertGreaterEqual(len(skills), 2)
        for md_file in agents + skills:
            text = md_file.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"Missing frontmatter in {md_file}")
            self.assertIn("name:", text)
            self.assertIn("description:", text)

    def test_pre_commit_hook_detects_synthetic_secret(self) -> None:
        hook_path = ROOT / ".claude" / "hooks" / "pre_commit_secret_check.py"
        spec = importlib.util.spec_from_file_location("pre_commit_secret_check", hook_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            synthetic = "ghp_" + ("A1b2C3d4E5" * 3)
            (temp_root / "leak.txt").write_text(f"token={synthetic}\n", encoding="utf-8")
            hits = module.scan_paths(temp_root)
            self.assertEqual(len(hits), 1)
            self.assertEqual(module.scan_paths(ROOT), [])


if __name__ == "__main__":
    unittest.main()
