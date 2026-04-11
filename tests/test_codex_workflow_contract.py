from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "codex-issue.yml"


class TestCodexWorkflowContract(unittest.TestCase):
    def test_required_codex_docs_exist(self) -> None:
        for relative_path in ("AGENTS.md", "PLANS.md", "IMPLEMENT.md", ".github/workflows/codex-issue.yml"):
            self.assertTrue((ROOT / relative_path).exists(), f"missing required file: {relative_path}")

    def test_issue_workflow_preserves_comment_interface(self) -> None:
        content = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("issue_comment:", content)
        self.assertIn("startsWith(github.event.comment.body, '/codex ')", content)
        self.assertIn("body.match(/^\\/codex\\s+(plan|implement|review|autopilot)\\b/i)", content)

    def test_issue_workflow_does_not_use_mutable_main_refs(self) -> None:
        content = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("@main", content)

    def test_issue_workflow_pins_reusable_workflows_to_full_sha(self) -> None:
        content = WORKFLOW.read_text(encoding="utf-8")
        workflow_refs = re.findall(
            r"rebuild-123/codex-automation/\.github/workflows/[^@\s]+@[0-9a-f]{40}",
            content,
        )
        self.assertEqual(4, len(workflow_refs))

    def test_issue_workflow_pins_github_script_to_full_sha(self) -> None:
        content = WORKFLOW.read_text(encoding="utf-8")
        pinned_refs = re.findall(r"actions/github-script@[0-9a-f]{40}", content)
        self.assertGreaterEqual(len(pinned_refs), 2)


if __name__ == "__main__":
    unittest.main()
