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

    def test_allowed_dirty_success_preserves_multiple_literal_paths(self):
        literal = self.root / "[literal] name"
        literal.write_text("original literal")
        clean = self.root / "clean"
        clean.write_text("clean")
        self.git("add", "--", "[literal] name", "clean")
        self.git("commit", "-qm", "add files")
        self.head = self.git("rev-parse", "HEAD").stdout.strip()
        (self.root / ".git/info/exclude").write_text("foreign\n")
        foreign = self.root / "foreign"
        foreign.write_text("operational change")
        foreign.chmod(0o755)
        literal.write_text("literal change")
        self.report.write_text("review result")
        before_index = self.git("ls-files", "--stage", "-z").stdout
        before_status = self.git("status", "--porcelain", "-z").stdout
        result = self.run_helper(
            "--allow-dirty",
            "foreign",
            "--allow-dirty",
            "[literal] name",
            "--allow-dirty",
            "clean",
            "--allow-dirty",
            "foreign",
            "docs/worklog/report.md",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        new_head = self.git("rev-parse", "HEAD").stdout.strip()
        self.assertEqual(result.stdout.strip(), new_head)
        self.assertEqual(
            self.git("rev-list", "--parents", "-n", "1", "HEAD").stdout.strip(),
            f"{new_head} {self.head}",
        )
        self.assertEqual(
            self.git(
                "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"
            ).stdout.strip(),
            "docs/worklog/report.md",
        )
        self.assertEqual(foreign.read_text(), "operational change")
        self.assertEqual(foreign.stat().st_mode & 0o777, 0o755)
        self.assertEqual(literal.read_text(), "literal change")
        self.assertEqual(clean.read_text(), "clean")
        after_index = self.git("ls-files", "--stage", "-z").stdout
        for line in before_index.split("\0"):
            if line.endswith(("\tforeign", "\t[literal] name", "\tclean")):
                self.assertIn(line + "\0", after_index)
        self.assertEqual(
            self.git("status", "--porcelain", "-z").stdout,
            before_status.replace(" M docs/worklog/report.md\0", ""),
        )

    def test_allowed_dirty_preflight_refusals_preserve_index_and_files(self):
        foreign = self.root / "foreign"
        self.report.write_text("report changed")
        for path, reason in (
            ("docs/worklog/report.md", "overlap"),
            ("missing", "regular file"),
            ("../foreign", "noncanonical"),
            (".git/config", "noncanonical"),
            (".", "noncanonical"),
        ):
            with self.subTest(path=path):
                result = self.assert_preflight_refusal(
                    "--allow-dirty", path, "docs/worklog/report.md"
                )
                self.assertIn(reason, result.stderr)
                self.assertEqual(foreign.read_text(), "original\n")
                self.assertEqual(self.report.read_text(), "report changed")
        foreign.write_text("staged content")
        self.git("add", "foreign")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.assertEqual(foreign.read_text(), "staged content")
        foreign.write_text("partly staged")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.assertEqual(foreign.read_text(), "partly staged")
        self.git("reset", "-q", "HEAD", "--", "foreign")
        foreign.unlink()
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("regular file", result.stderr)
        foreign.symlink_to(self.report)
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("symlink", result.stderr)
        self.assertTrue(foreign.is_symlink())

    def test_allowed_dirty_conflicts_rename_flags_and_unlisted(self):
        self.report.write_text("report changed")
        foreign = self.root / "foreign"
        self.git("mv", "foreign", "renamed")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("regular file", result.stderr)
        self.assertEqual((self.root / "renamed").read_text(), "original\n")
        self.git("reset", "-q", "HEAD", "--", "foreign", "renamed")
        (self.root / "renamed").rename(foreign)
        blob = self.git("rev-parse", "HEAD:foreign").stdout.strip()
        info = f"0 {'0' * 40}\tforeign\n100644 {blob} 1\tforeign\n100644 {blob} 2\tforeign\n100644 {blob} 3\tforeign\n"
        subprocess.run(  # noqa: S603
            ["git", "update-index", "--index-info"],  # noqa: S607
            input=info,
            cwd=self.root,
            text=True,
            check=True,
        )
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.git("reset", "-q", "HEAD", "--", "foreign")
        self.git("update-index", "--skip-worktree", "foreign")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index flag", result.stderr)
        self.assertEqual(self.git("ls-files", "-v", "foreign").stdout[0], "S")
        self.git("update-index", "--no-skip-worktree", "foreign")
        (self.root / "unlisted").write_text("other")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("outside supplied", result.stderr)
        self.assertEqual((self.root / "unlisted").read_text(), "other")
        (self.root / "unlisted").unlink()
        self.report.write_text("base\n")
        foreign.write_text("only operational")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("no permitted report changes", result.stderr)
        self.assertEqual(foreign.read_text(), "only operational")

    def test_allowed_dirty_filter_mutation_is_detected(self):
        self.report.write_text("report changed")
        (self.root / ".git/info/attributes").write_text(
            "docs/worklog/report.md filter=mutate\n"
        )
        self.git("config", "filter.mutate.clean", "printf filtered > foreign; cat")
        self.git("config", "filter.mutate.smudge", "cat")
        result = self.run_helper("--allow-dirty", "foreign", "docs/worklog/report.md")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("operational snapshot changed", result.stderr)
        self.assertEqual((self.root / "foreign").read_text(), "filtered")
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.head)
        self.assertEqual(self.report.read_text(), "report changed")

    def test_allowed_dirty_unsafe_paths_and_staged_mode(self):
        self.report.write_text("report changed")
        untracked = self.root / "new"
        untracked.write_text("new")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "new", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.assertEqual(untracked.read_text(), "new")
        untracked.unlink()
        link = self.root / "linked"
        link.symlink_to(self.root, target_is_directory=True)
        result = self.assert_preflight_refusal(
            "--allow-dirty", "linked/foreign", "docs/worklog/report.md"
        )
        self.assertIn("symlink", result.stderr)
        self.assertTrue(link.is_symlink())
        link.unlink()
        foreign = self.root / "foreign"
        foreign.unlink()
        os.mkfifo(foreign)
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("regular file", result.stderr)
        self.assertTrue(foreign.exists())
        foreign.unlink()
        foreign.write_text("original\n")
        foreign.chmod(0o755)
        self.git("add", "foreign")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.assertEqual(foreign.stat().st_mode & 0o777, 0o755)
        self.git("reset", "-q", "HEAD", "--", "foreign")
        foreign.unlink()
        foreign.symlink_to(self.report)
        self.git("add", "foreign")
        foreign.unlink()
        foreign.write_text("regular replacement")
        result = self.assert_preflight_refusal(
            "--allow-dirty", "foreign", "docs/worklog/report.md"
        )
        self.assertIn("index must match", result.stderr)
        self.assertIn("120000", self.git("ls-files", "--stage", "foreign").stdout)
        self.assertEqual(foreign.read_text(), "regular replacement")

    def test_allowed_dirty_hook_mutation_fails_without_repair(self):
        for action in (
            "printf changed > foreign",
            "chmod +x foreign",
            "printf staged > foreign; git add foreign",
        ):
            with self.subTest(action=action):
                self.report.write_text("report changed")
                hook = self.root / ".git/hooks/post-commit"
                hook.write_text(f"#!/bin/sh\n{action}\n")
                hook.chmod(0o755)
                result = self.run_helper(
                    "--allow-dirty", "foreign", "docs/worklog/report.md"
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertNotEqual(
                    self.git("rev-parse", "HEAD").stdout.strip(), self.head
                )
                self.assertIn("operational", result.stderr)
                if action.startswith("chmod"):
                    self.assertTrue((self.root / "foreign").stat().st_mode & 0o111)
                else:
                    self.assertNotEqual(
                        (self.root / "foreign").read_text(), "original\n"
                    )
                hook.unlink()
                self.git("reset", "--hard", "-q", self.head)

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
