import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HELPER = Path(__file__).resolve().parents[1] / "tools/review_commit.py"


class ReviewCommitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        (self.root / "docs/worklog").mkdir(parents=True)
        self.report = self.root / "docs/worklog/report.md"
        self.report.write_text("base\n")
        (self.root / "foreign").write_text("original\n")
        self.git("add", ".")
        self.git("commit", "-qm", "base")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()

    def git(self, *args, check=True):
        return subprocess.run(  # noqa: S603
            ["git", *args],  # noqa: S607
            cwd=self.root,
            text=True,
            capture_output=True,
            check=check,
        )

    def run_helper(self, *paths, head=None, message="review: result", env=None):
        return subprocess.run(  # noqa: S603
            [
                sys.executable,
                str(HELPER),
                "--head",
                head or self.head,
                "-m",
                message,
                *paths,
            ],
            cwd=self.root,
            text=True,
            capture_output=True,
            env=env,
        )

    def test_commit_new_modified_and_staged_literal_names(self):
        self.report.write_text("staged\n")
        self.git("add", "docs/worklog/report.md")
        self.report.write_text("complete\n")
        strange = self.root / "docs/worklog/[new] name.md"
        strange.write_text("new\n")
        result = self.run_helper("docs/worklog/report.md", "docs/worklog/[new] name.md")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.git("show", "HEAD:docs/worklog/report.md").stdout, "complete\n"
        )
        self.assertEqual(
            self.git("show", "HEAD:docs/worklog/[new] name.md").stdout, "new\n"
        )
        self.assertEqual(self.git("status", "--porcelain").stdout, "")
        self.assertEqual(self.git("rev-parse", "HEAD^").stdout.strip(), self.head)

    def test_refusals_preserve_changes(self):
        self.report.write_text("changed\n")
        for kwargs in (
            {"head": "abc"},
            {"message": "review:  "},
            {"message": "review: x\ny"},
        ):
            with self.subTest(kwargs=kwargs):
                result = self.run_helper("docs/worklog/report.md", **kwargs)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(
                    self.git("rev-parse", "HEAD").stdout.strip(), self.head
                )
                self.assertEqual(self.report.read_text(), "changed\n")
        result = self.run_helper("docs/worklog/../worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        (self.root / "untracked").write_text("foreign")
        self.assertNotEqual(self.run_helper("docs/worklog/report.md").returncode, 0)
        self.assertEqual(self.git("diff", "--cached").stdout, "")

    def test_ignored_symlink_deleted_and_operation_refused(self):
        (self.root / ".git/info/exclude").write_text("docs/worklog/ignored.md\n")
        (self.root / "docs/worklog/ignored.md").write_text("ignored")
        self.assertIn("ignored", self.run_helper("docs/worklog/ignored.md").stderr)
        link = self.root / "docs/worklog/link.md"
        link.symlink_to(self.report)
        self.assertIn("symlink", self.run_helper("docs/worklog/link.md").stderr)
        link.unlink()
        self.report.unlink()
        self.assertNotEqual(self.run_helper("docs/worklog/report.md").returncode, 0)
        self.report.write_text("changed")
        (self.root / ".git/MERGE_HEAD").write_text(self.head + "\n")
        self.assertIn("operation", self.run_helper("docs/worklog/report.md").stderr)

    def test_hook_failure_and_hook_changes_are_not_success(self):
        self.report.write_text("changed")
        hook = self.root / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\nexit 1\n")
        hook.chmod(0o755)
        result = self.run_helper("docs/worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.head)
        self.assertTrue(self.git("diff", "--cached", "--name-only").stdout)
        hook.write_text(
            "#!/bin/sh\nprintf hook > docs/worklog/report.md\ngit add docs/worklog/report.md\n"
        )
        result = self.run_helper("docs/worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.head)
        self.assertIn("Observed HEAD", result.stderr)

    def test_hook_leaves_untracked_file(self):
        self.report.write_text("changed")
        hook = self.root / ".git/hooks/post-commit"
        hook.write_text("#!/bin/sh\nprintf extra > extra\n")
        hook.chmod(0o755)
        result = self.run_helper("docs/worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((self.root / "extra").exists())
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.head)
        self.assertIn("Observed HEAD", result.stderr)

    def assert_preflight_refusal(self, *paths):
        before_index = self.git("ls-files", "--stage", "-z").stdout
        before_head = self.git("rev-parse", "HEAD").stdout
        result = self.run_helper(*paths)
        self.assertNotEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, before_head)
        self.assertEqual(self.git("ls-files", "--stage", "-z").stdout, before_index)
        return result

    def test_hidden_foreign_changes_refused_without_mutation(self):
        for flag, marker in (("--assume-unchanged", "h"), ("--skip-worktree", "S")):
            with self.subTest(flag=flag):
                self.report.write_text("report change")
                self.git("update-index", flag, "foreign")
                (self.root / "foreign").write_text("hidden change")
                result = self.assert_preflight_refusal("docs/worklog/report.md")
                self.assertIn("index flag", result.stderr)
                self.assertEqual((self.root / "foreign").read_text(), "hidden change")
                self.assertEqual(
                    self.git("ls-files", "-v", "foreign").stdout[0], marker
                )
                self.assertEqual(self.report.read_text(), "report change")
                self.git(
                    "update-index",
                    "--no-assume-unchanged",
                    "--no-skip-worktree",
                    "foreign",
                )
                (self.root / "foreign").write_text("original\n")

    def test_hook_hidden_foreign_change_is_not_success(self):
        self.report.write_text("changed")
        hook = self.root / ".git/hooks/post-commit"
        hook.write_text(
            "#!/bin/sh\ngit update-index --assume-unchanged foreign\nprintf hidden > foreign\n"
        )
        hook.chmod(0o755)
        result = self.run_helper("docs/worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("index flag", result.stderr)
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.head)
        self.assertEqual((self.root / "foreign").read_text(), "hidden")
        self.assertEqual(self.git("ls-files", "-v", "foreign").stdout[0], "h")

    def test_tracked_foreign_changes_and_rename_refused(self):
        self.report.write_text("report change")
        foreign = self.root / "foreign"
        foreign.write_text("foreign change")
        self.assert_preflight_refusal("docs/worklog/report.md")
        self.assertEqual(foreign.read_text(), "foreign change")
        self.git("add", "foreign")
        self.assert_preflight_refusal("docs/worklog/report.md")
        self.assertEqual(foreign.read_text(), "foreign change")
        self.git("reset", "-q", "HEAD", "--", "foreign")
        foreign.write_text("original\n")
        self.git("mv", "foreign", "docs/worklog/renamed.md")
        self.assert_preflight_refusal(
            "docs/worklog/report.md", "docs/worklog/renamed.md"
        )
        self.assertFalse(foreign.exists())
        self.assertEqual(
            (self.root / "docs/worklog/renamed.md").read_text(), "original\n"
        )
        self.assertEqual(self.report.read_text(), "report change")

    def test_conflict_and_type_changes_refused(self):
        self.report.write_text("report change")
        blob = self.git("rev-parse", "HEAD:docs/worklog/report.md").stdout.strip()
        index_info = f"0 {'0' * 40}\tdocs/worklog/report.md\n100644 {blob} 1\tdocs/worklog/report.md\n100644 {blob} 2\tdocs/worklog/report.md\n100644 {blob} 3\tdocs/worklog/report.md\n"
        subprocess.run(  # noqa: S603
            ["git", "update-index", "--index-info"],  # noqa: S607
            input=index_info,
            cwd=self.root,
            text=True,
            check=True,
        )
        result = self.assert_preflight_refusal("docs/worklog/report.md")
        self.assertIn("unsupported change", result.stderr)
        self.assertEqual(self.report.read_text(), "report change")
        self.git("reset", "-q", "HEAD", "--", "docs/worklog/report.md")
        self.report.unlink()
        self.report.symlink_to(self.root / "foreign")
        self.assert_preflight_refusal("docs/worklog/report.md")
        self.assertTrue(self.report.is_symlink())
        self.git("add", "docs/worklog/report.md")
        self.report.unlink()
        self.report.write_text("regular worktree")
        self.assert_preflight_refusal("docs/worklog/report.md")
        self.assertFalse(self.report.is_symlink())
        self.assertEqual(self.report.read_text(), "regular worktree")
        self.assertIn(
            "120000", self.git("ls-files", "--stage", "docs/worklog/report.md").stdout
        )

    def test_environment_and_detached_head_refused(self):
        self.report.write_text("changed")
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(self.root / "elsewhere")
        self.assertIn(
            "environment", self.run_helper("docs/worklog/report.md", env=env).stderr
        )
        env.pop("GIT_INDEX_FILE")
        env["GIT_CONFIG_PARAMETERS"] = "bad"
        result = self.run_helper("docs/worklog/report.md", env=env)
        self.assertIn("environment", result.stderr)
        self.assertIn("Observed HEAD unavailable", result.stderr)
        self.git("checkout", "--detach", "-q")
        self.assertNotEqual(self.run_helper("docs/worklog/report.md").returncode, 0)


if __name__ == "__main__":
    unittest.main()
