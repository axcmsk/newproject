import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "merge.py"


class MergeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(
            HOME=str(self.root),
            XDG_CONFIG_HOME=str(self.root / "xdg"),
            GIT_CONFIG_NOSYSTEM="1",
        )
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.write("base", "base")
        self.commit("initial")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("checkout", "-b", "feature")

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(  # noqa: S603 - controlled fixture
            ["git", *args],  # noqa: S607 - Git on PATH
            cwd=cwd or self.repo,
            env=self.env,
            capture_output=True,
            text=True,
            check=check,
        )

    def write(self, name, text):
        (self.repo / name).write_text(text)

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-m", message)
        return self.git("rev-parse", "HEAD").stdout.strip()

    def helper(self, *args, env=None, cwd=None):
        return subprocess.run(  # noqa: S603 - controlled fixture
            [sys.executable, str(SCRIPT), *args],
            cwd=cwd or self.repo,
            env=env or self.env,
            text=True,
            capture_output=True,
        )

    def prepare(self, messages=("step: one",), diverged=False):
        for i, message in enumerate(messages):
            self.write(f"file{i}", message)
            self.commit(message)
        source = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("checkout", "main")
        if diverged:
            self.write("target", "target")
            self.commit("target history")
        target = self.git("rev-parse", "HEAD").stdout.strip()
        return source, target

    def test_modes_topology_and_message(self):
        for messages, mode, diverged in [
            (("step: one", "docs: details"), "squash", False),
            (("docs: details",), "squash", True),
            (("step: one", "step: two"), "merge", False),
            (("other",), "merge", True),
        ]:
            with self.subTest(messages=messages):
                if self.git("branch", "--show-current").stdout.strip() != "feature":
                    self.git("reset", "--hard", self.base)
                    self.git("branch", "-D", "feature")
                    self.git("checkout", "-b", "feature")
                source, target = self.prepare(messages, diverged)
                message = "  supplied title\n\nbody  "
                result = self.helper("feature", "-m", message)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(mode, result.stdout)
                parents = self.git(
                    "rev-list", "--parents", "-n", "1", "HEAD"
                ).stdout.split()[1:]
                self.assertEqual(
                    parents, [target] if mode == "squash" else [target, source]
                )
                self.assertEqual(
                    self.git("rev-parse", "feature").stdout.strip(), source
                )
                self.assertEqual(
                    self.git("show", "-s", "--format=%B", "HEAD").stdout,
                    message + "\n\n",
                )
                self.assertEqual((self.repo / "file0").read_text(), messages[0])
                self.assertEqual(self.git("status", "--porcelain").stdout, "")

    def test_precondition_refusals(self):
        self.prepare()
        for dirty in ("untracked", "tracked", "staged"):
            if dirty == "untracked":
                self.write("extra", "keep")
            else:
                self.write("base", "changed")
                if dirty == "staged":
                    self.git("add", "base")
            before = self.git("status", "--porcelain").stdout
            result = self.helper("feature", "-m", "message")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("not clean", result.stderr)
            self.assertEqual(before, self.git("status", "--porcelain").stdout)
            self.git("reset", "--hard", "HEAD")
            if (self.repo / "extra").exists():
                (self.repo / "extra").unlink()
        for args in [
            ("missing", "-m", "x"),
            ("main", "-m", "x"),
            ("feature", "-m", "  "),
        ]:
            self.assertNotEqual(self.helper(*args).returncode, 0)
        self.git("checkout", "--detach")
        self.assertNotEqual(self.helper("feature", "-m", "x").returncode, 0)
        self.git("checkout", "main")
        self.git("branch", "empty", "main")
        self.assertIn("empty", self.helper("empty", "-m", "x").stderr)

    def test_conflict_and_hook_failure(self):
        self.write("base", "source")
        self.commit("unknown")
        self.git("checkout", "main")
        self.write("base", "target")
        target = self.commit("target")
        result = self.helper("feature", "-m", "merge")
        self.assertIn("partial", result.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), target)
        self.assertTrue((self.repo / ".git/MERGE_HEAD").exists())
        self.assertIn("UU base", self.git("status", "--porcelain").stdout)
        self.git("merge", "--abort")
        hook = self.repo / ".git/hooks/pre-commit"
        hook.write_text("#!/bin/sh\necho rejected >&2\nexit 1\n")
        hook.chmod(0o755)
        self.git("checkout", "feature")
        self.write("base", "base")
        hook.unlink()
        self.commit("step: fix")
        self.git("checkout", "main")
        hook.write_text("#!/bin/sh\necho rejected >&2\nexit 1\n")
        hook.chmod(0o755)
        result = self.helper("feature", "-m", "merge")
        self.assertIn("rejected", result.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), target)

    def test_operation_markers_and_linked_worktree(self):
        self.prepare()
        for marker in (
            "MERGE_HEAD",
            "rebase-merge",
            "rebase-apply",
            "CHERRY_PICK_HEAD",
            "REVERT_HEAD",
            "sequencer",
        ):
            path = self.repo / ".git" / marker
            path.write_text("marker")
            result = self.helper("feature", "-m", "x")
            self.assertIn("unfinished operation", result.stderr)
            self.assertIn(marker, result.stderr)
            self.assertEqual(path.read_text(), "marker")
            path.unlink()
        self.git("checkout", "feature")
        linked = self.root / "linked"
        self.git("worktree", "add", str(linked), "main")
        marker = Path(
            self.git("rev-parse", "--git-path", "MERGE_HEAD", cwd=linked).stdout.strip()
        )
        if not marker.is_absolute():
            marker = linked / marker
        marker.write_text("marker")
        result = self.helper("feature", "-m", "x", cwd=linked)
        self.assertIn("unfinished operation: MERGE_HEAD", result.stderr)
        self.assertEqual(marker.read_text(), "marker")

    def test_ignored_files_and_configuration(self):
        self.write(".gitignore", "ignored*\n")
        self.commit("docs: ignore")
        self.write("ignored-collision", "source")
        self.git("add", "-f", "ignored-collision")
        self.git("commit", "-m", "step: source")
        self.git("checkout", "main")
        (self.repo / ".git/info/exclude").write_text("ignored*\n")
        self.write("ignored-collision", "keep")
        self.git("config", "merge.autoStash", "true")
        self.git("config", "merge.ff", "only")
        self.git("config", "rerere.enabled", "true")
        before = self.git("rev-parse", "HEAD").stdout
        result = self.helper("feature", "-m", "merge")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.repo / "ignored-collision").read_text(), "keep")
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, before)
        (self.repo / "ignored-collision").unlink()
        self.write("ignored-other", "keep")
        result = self.helper("feature", "-m", "merge")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.repo / "ignored-other").read_text(), "keep")
        self.assertEqual((self.repo / "ignored-collision").read_text(), "source")

    def test_no_net_change_squash(self):
        self.write("base", "changed")
        self.commit("step: change")
        self.write("base", "base")
        self.commit("fixup: undo")
        self.git("checkout", "main")
        result = self.helper("feature", "-m", "x")
        self.assertIn("no net change", result.stderr)
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.base)
        self.assertEqual((self.repo / "base").read_text(), "base")

    def test_help_errors_and_environment_isolation(self):
        self.prepare()
        outside = self.root / "outside"
        outside.mkdir()
        self.git("init", "-b", "outside", cwd=outside)
        before = self.git("status", "--porcelain", cwd=outside).stdout
        env = self.env.copy()
        env.update(
            GIT_DIR=str(outside / ".git"),
            GIT_WORK_TREE=str(outside),
            GIT_INDEX_FILE=str(self.root / "index"),
            GIT_CONFIG_COUNT="1",
            GIT_CONFIG_KEY_0="merge.ff",
            GIT_CONFIG_VALUE_0="only",
        )
        result = self.helper("feature", "-m", "x", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.git("status", "--porcelain", cwd=outside).stdout, before)
        self.assertFalse((self.root / "index").exists())
        for flag in ("-h", "--help"):
            self.assertEqual(self.helper(flag).returncode, 0)
        self.assertEqual(self.helper().returncode, 2)
        self.assertEqual(self.helper("feature", "main", "-m", "x").returncode, 2)
        env["PATH"] = str(self.root / "no-git")
        result = self.helper("feature", "-m", "x", env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("git", result.stderr)

    def test_real_merge_overrides_ff_only_and_counts_source_range(self):
        self.write("file", "one")
        self.commit("step: first")
        self.write("file", "two")
        source = self.commit("step: second")
        self.git("checkout", "main")
        self.git("config", "merge.ff", "only")
        self.git("config", "merge.autoStash", "true")
        self.git("config", "rerere.enabled", "true")
        result = self.helper("feature", "-m", "message")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("merge commit", result.stdout)
        self.assertEqual(
            self.git("rev-list", "--parents", "-n", "1", "HEAD").stdout.split()[1:],
            [self.base, source],
        )

    def test_merge_commit_in_source_history_selects_merge(self):
        self.git("checkout", "main")
        self.write("shared", "shared")
        self.commit("step: shared")
        self.git("branch", "side")
        self.git("checkout", "feature")
        self.write("feature", "feature")
        self.commit("docs: feature")
        self.git("checkout", "side")
        self.write("side", "side")
        self.commit("docs: side")
        self.git("checkout", "feature")
        self.git("merge", "--no-ff", "side", "-m", "unknown merge")
        source = self.git("rev-parse", "HEAD").stdout.strip()
        self.git("checkout", "main")
        target = self.git("rev-parse", "HEAD").stdout.strip()
        result = self.helper("feature", "-m", "message")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("merge commit", result.stdout)
        self.assertEqual(
            self.git("rev-list", "--parents", "-n", "1", "HEAD").stdout.split()[1:],
            [target, source],
        )
