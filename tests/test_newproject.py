import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "newproject.py"


class CreationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.repo = self.base / "source"
        self.repo.mkdir()
        shutil.copy(SCRIPT, self.repo / "newproject.py")
        (self.repo / "tools").mkdir()
        for name in ("merge.py", "review_commit.py"):
            shutil.copy2(SCRIPT.parent / "tools" / name, self.repo / "tools" / name)
        self.template = self.repo / "template" / "base"
        self.template.mkdir(parents=True)
        (self.template / ".hidden").write_text("hidden")
        (self.template / "nested").mkdir()
        (self.template / "nested" / "file").write_text("hello")
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env["XDG_CONFIG_HOME"] = str(self.base / "xdg")
        self.env.update(
            HOME=str(self.base),
            GIT_CONFIG_NOSYSTEM="1",
            GIT_AUTHOR_NAME="Test",
            GIT_AUTHOR_EMAIL="test@example.invalid",
            GIT_COMMITTER_NAME="Test",
            GIT_COMMITTER_EMAIL="test@example.invalid",
        )
        self.target = self.base / "project"

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, name="project", env=None, cwd=None):
        return subprocess.run(  # noqa: S603 - Controlled fixture arguments; no shell.
            [sys.executable, str(self.repo / "newproject.py"), name],
            cwd=cwd or self.base,
            env=env or self.env,
            text=True,
            capture_output=True,
        )

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(  # noqa: S603 - Controlled fixture arguments; no shell.
            ["git", *args],  # noqa: S607 - Tests intentionally use Git on PATH.
            cwd=cwd or self.target,
            env=self.env,
            text=True,
            capture_output=True,
            check=check,
        )

    def state(self, target):
        if target.is_symlink():
            return ("link", os.readlink(target))
        if not target.exists():
            return None
        if not target.is_dir():
            return ("file", target.read_bytes())
        result = {}
        for path in target.rglob("*"):
            key = str(path.relative_to(target))
            if path.is_symlink():
                result[key] = ("link", os.readlink(path))
            elif path.is_file():
                result[key] = ("file", path.read_bytes())
            else:
                result[key] = ("dir",)
        return result

    def assert_refusal(self, result, reason):
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(reason, result.stderr)
        self.assertIn("Cannot create project at", result.stderr)
        self.assertIn("Target unchanged", result.stderr)

    def assert_success(self, result, target=None):
        target = target or self.target
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / ".hidden").read_text(), "hidden")
        self.assertEqual((target / "nested" / "file").read_text(), "hello")
        self.assertEqual(
            set(p.name for p in target.iterdir()),
            {".git", ".hidden", "nested", "tools"},
        )
        self.assertEqual(
            self.git("symbolic-ref", "HEAD", cwd=target).stdout.strip(),
            "refs/heads/main",
        )
        self.assertNotEqual(
            self.git(
                "rev-parse", "--verify", "HEAD", cwd=target, check=False
            ).returncode,
            0,
        )
        self.assertEqual(self.git("ls-files", "--stage", cwd=target).stdout, "")
        self.assertEqual(self.git("remote", cwd=target).stdout, "")

    def test_new_empty_and_existing_repositories(self):
        self.assert_success(self.run_cli(cwd=self.template))
        before = self.state(self.target)
        self.assert_refusal(self.run_cli(), "target must be empty")
        self.assertEqual(before, self.state(self.target))
        self.target = self.base / "empty"
        self.target.mkdir()
        self.assert_success(self.run_cli("empty"))
        self.target = self.base / "existing"
        self.target.mkdir()
        self.git("init", "-b", "other")
        self.git("config", "example.keep", "yes")
        self.assert_success(self.run_cli("existing"))
        self.assertEqual(self.git("config", "example.keep").stdout.strip(), "yes")

    def test_names_and_parent_git(self):
        self.git("init", "-b", "parent", cwd=self.base)
        for name in ("space name", "юникод", "$(touch danger)"):
            with self.subTest(name=name):
                self.assert_success(self.run_cli(name), self.base / name)
        self.assertFalse((self.base / "danger").exists())
        for name in ("", ".", "..", "a/b", "a\\b", "bad\nname", "bad\x7f", "bad\x85"):
            with self.subTest(name=name):
                self.assert_refusal(self.run_cli(name), "single directory name")

    def test_target_refusals(self):
        self.target.write_text("keep")
        self.assert_refusal(self.run_cli(), "not a directory")
        self.assertEqual(self.target.read_text(), "keep")
        self.target.unlink()
        self.target.symlink_to(self.base / "missing")
        self.assert_refusal(self.run_cli(), "symlink")
        self.target.unlink()
        self.target.symlink_to(self.template, target_is_directory=True)
        self.assert_refusal(self.run_cli(), "symlink")
        self.target.unlink()
        self.target.mkdir()
        (self.target / "keep").write_text("keep")
        self.assert_refusal(self.run_cli(), "target must be empty")
        self.assertEqual((self.target / "keep").read_text(), "keep")

    def test_invalid_git_states(self):
        for kind in ("file", "link", "malformed", "bare", "staged", "commit", "ref"):
            with self.subTest(kind=kind):
                self.target = self.base / kind
                self.target.mkdir()
                dotgit = self.target / ".git"
                if kind == "file":
                    dotgit.write_text("gitdir: nowhere")
                elif kind == "link":
                    dotgit.symlink_to(self.template, target_is_directory=True)
                elif kind == "malformed":
                    dotgit.mkdir()
                elif kind == "bare":
                    self.git("init", "--bare", str(dotgit), cwd=self.base)
                else:
                    self.git("init", "-b", "other")
                    if kind in ("staged", "commit"):
                        (self.target / "data").write_text("data")
                        self.git("add", "data")
                        if kind == "commit":
                            self.git("commit", "-m", "test")
                            (self.target / "data").unlink()
                        else:
                            (self.target / "data").unlink()
                    else:
                        obj = self.git(
                            "hash-object", "-w", "--stdin", cwd=self.target
                        ).stdout.strip()
                        self.git("update-ref", "refs/tags/test", obj)
                before = self.state(self.target)
                result = self.run_cli(kind)
                self.assert_refusal(
                    result,
                    {
                        "file": "target must be empty",
                        "link": "target must be empty",
                        "malformed": "Git rev-parse failed",
                        "bare": "bare",
                        "staged": "staged entries",
                        "commit": "refs",
                        "ref": "refs",
                    }[kind],
                )
                self.assertEqual(before, self.state(self.target))

    def test_template_refusals(self):
        shutil.rmtree(self.template)
        self.assert_refusal(self.run_cli(), "template layer must be a real directory")
        self.template.mkdir()
        self.assert_refusal(self.run_cli(), "template is empty")
        (self.template / "link").symlink_to(self.base / "missing")
        self.assert_refusal(self.run_cli(), "invalid template entry")
        (self.template / "link").unlink()
        (self.template / ".git").mkdir()
        self.assert_refusal(self.run_cli(), "invalid template entry")
        (self.template / ".git").rmdir()
        os.mkfifo(self.template / "fifo")
        self.assert_refusal(self.run_cli(), "invalid template entry")
        self.assertFalse(self.target.exists())

    def test_git_environment_isolation_and_missing_git(self):
        env = self.env.copy()
        env.update(
            GIT_DIR=str(self.base / "redirect"),
            GIT_WORK_TREE=str(self.base),
            GIT_INDEX_FILE=str(self.base / "index"),
            GIT_CONFIG_COUNT="1",
            GIT_CONFIG_KEY_0="init.defaultBranch",
            GIT_CONFIG_VALUE_0="wrong",
        )
        self.assert_success(self.run_cli(env=env))
        self.assertFalse((self.base / "redirect").exists())
        self.assertFalse((self.base / "index").exists())
        env["PATH"] = str(self.base / "no-git")
        self.assert_refusal(
            self.run_cli("missing", env=env), "Git executable not found"
        )
        self.assertFalse((self.base / "missing").exists())

    def test_traversal_failure_before_mutation(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("project_cli_walk", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        def failed_walk(source, followlinks, onerror):
            yield str(source), ["nested"], [".hidden"]
            onerror(
                PermissionError(
                    13, "injected enumeration failure", str(source / "nested")
                )
            )

        self.target.mkdir()
        before = self.state(self.target)
        with (
            mock.patch.object(module, "__file__", str(self.repo / "newproject.py")),
            mock.patch.object(sys, "argv", ["newproject.py", "project"]),
            mock.patch.object(module.os, "walk", failed_walk),
            mock.patch("sys.stderr") as stderr,
        ):
            self.assertEqual(module.main(), 1)
        diagnostic = "".join(str(c) for c in stderr.write.call_args_list)
        self.assertIn("template traversal failed", diagnostic)
        self.assertIn("nested", diagnostic)
        self.assertIn("Target unchanged", diagnostic)
        self.assertEqual(before, self.state(self.target))

    def test_ambient_git_template_is_ignored(self):
        template = self.base / "git-template"
        template.mkdir()
        fixture = self.base / "fixture"
        fixture.mkdir()
        self.git("init", "-b", "other", cwd=fixture)
        (fixture / "staged").write_text("staged")
        self.git("add", "staged", cwd=fixture)
        self.git(
            "remote", "add", "contaminant", "https://example.invalid/repo", cwd=fixture
        )
        shutil.copytree(fixture / ".git", template, dirs_exist_ok=True)
        self.git("config", "--global", "init.templateDir", str(template), cwd=self.base)
        self.assert_success(self.run_cli())
        self.assertEqual(self.git("for-each-ref", "--format=%(refname)").stdout, "")
        self.assertFalse((self.target / ".git" / "index").exists())
        self.assertEqual(self.git("remote").stdout, "")

    def test_contaminated_environment_stays_in_fixture(self):
        sentinel = self.base / "sentinel"
        sentinel.mkdir()
        self.git("init", "-b", "sentinel", cwd=sentinel)
        (sentinel / "keep").write_text("safe")
        self.git("add", "keep", cwd=sentinel)
        before = self.state(sentinel)
        config = self.base / "outside-config"
        config.write_text("[alias]\n  sentinel = status\n")
        config_before = config.read_bytes()
        contaminated = self.env.copy()
        contaminated.update(
            GIT_DIR=str(sentinel / ".git"),
            GIT_WORK_TREE=str(sentinel),
            GIT_INDEX_FILE=str(sentinel / ".git" / "index"),
            GIT_CONFIG_GLOBAL=str(config),
            GIT_CONFIG_COUNT="1",
            GIT_CONFIG_KEY_0="init.templateDir",
            GIT_CONFIG_VALUE_0=str(sentinel / ".git"),
        )
        self.assert_success(self.run_cli(env=contaminated))
        self.assertEqual(before, self.state(sentinel))
        self.assertEqual(config_before, config.read_bytes())

    def test_init_failure_partial_state(self):
        fake = self.base / "bin"
        fake.mkdir()
        git = fake / "git"
        git.write_text(
            '#!/bin/sh\nif [ "$1" = --version ]; then exit 0; fi\necho injected-init-failure >&2\nexit 1\n'
        )
        git.chmod(0o755)
        env = self.env.copy()
        env["PATH"] = str(fake)
        result = self.run_cli(env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("injected-init-failure", result.stderr)
        self.assertIn("Partial state may remain", result.stderr)
        self.assertTrue(self.target.is_dir())

    def test_copy_failure_reports_partial_state_and_preserves_file(self):
        # Load the CLI as a module and inject a collision at the copy boundary.
        import importlib.util

        spec = importlib.util.spec_from_file_location("project_cli", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = Path.open

        def collide(path, *args, **kwargs):
            if path.name == ".hidden" and args and args[0] == "xb":
                path.write_text("appeared")
            return original(path, *args, **kwargs)

        with (
            mock.patch.object(module, "__file__", str(self.repo / "newproject.py")),
            mock.patch.object(sys, "argv", ["newproject.py", "project"]),
            mock.patch.object(Path, "open", collide),
            mock.patch.dict(os.environ, self.env, clear=True),
            mock.patch("sys.stderr") as stderr,
        ):
            self.assertEqual(module.main(), 1)
        self.assertEqual((self.target / ".hidden").read_text(), "appeared")
        self.assertIn(
            "Partial state may remain",
            "".join(str(c) for c in stderr.write.call_args_list),
        )


if __name__ == "__main__":
    unittest.main()


class VariantTests(unittest.TestCase):
    assert_refusal = CreationTests.assert_refusal
    tearDown = CreationTests.tearDown

    def setUp(self):
        CreationTests.setUp(self)
        (self.template / "AGENTS.md").write_text("base\n\n")
        self.heavy = self.repo / "template" / "heavy"
        self.heavy.mkdir()
        (self.heavy / "AGENTS.add.md").write_text("heavy\n\n")
        (self.heavy / "nested").mkdir()
        (self.heavy / "nested" / "extra").write_text("addition")

    def cli(self, *args):
        return subprocess.run(  # noqa: S603 - controlled fixture
            [sys.executable, str(self.repo / "newproject.py"), *args],
            cwd=self.base,
            env=self.env,
            capture_output=True,
            text=True,
        )

    def test_variants_and_options(self):
        (self.template / "AGENTS.md").chmod(0o640)
        for args, name, heavy in [
            (("--heavy", "one"), "one", True),
            (("two", "--heavy"), "two", True),
            (("--", "--heavy"), "--heavy", False),
            (("--heavy", "--", "--heavy"), "--heavy", True),
        ]:
            target = self.base / name
            if target.exists():
                shutil.rmtree(target)
            result = self.cli(*args)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                (target / "AGENTS.md").read_text(),
                "base\n\nheavy\n" if heavy else "base\n\n",
            )
            self.assertEqual((target / "AGENTS.md").stat().st_mode & 0o777, 0o640)
            self.assertEqual((target / "nested" / "extra").exists(), heavy)
            self.assertFalse((target / "AGENTS.add.md").exists())
        repeated = self.cli("--heavy", "--heavy", "repeated")
        self.assertEqual(repeated.returncode, 0, repeated.stderr)
        self.assertEqual(
            (self.base / "repeated" / "AGENTS.md").read_text(), "base\n\nheavy\n"
        )

    def test_help_and_syntax_errors_need_no_sources_or_git(self):
        shutil.rmtree(self.repo / "template")
        shutil.rmtree(self.repo / "tools")
        self.env["PATH"] = str(self.base / "no-git")
        for flag in ("-h", "--help"):
            result = self.cli(flag)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("NAME", result.stdout)
            self.assertIn("--heavy", result.stdout)
        for args in ((), ("--heavy",), ("x", "y"), ("--unknown", "x")):
            result = self.cli(*args)
            self.assertEqual(result.returncode, 2)
            self.assertIn("usage:", result.stderr)
            self.assertFalse((self.base / "x").exists())
        self.assertFalse(self.target.exists())

    def test_unreadable_metadata_and_unsafe_roots(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("variant_cli", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = Path.read_bytes

        def denied(path):
            if path.name == "AGENTS.add.md":
                raise PermissionError("injected unreadable metadata")
            return original(path)

        with (
            mock.patch.object(module, "__file__", str(self.repo / "newproject.py")),
            mock.patch.object(sys, "argv", ["newproject.py", "--heavy", "project"]),
            mock.patch.object(Path, "read_bytes", denied),
            mock.patch("sys.stderr") as stderr,
        ):
            self.assertEqual(module.main(), 1)
        diagnostic = "".join(str(c) for c in stderr.write.call_args_list)
        self.assertIn("injected unreadable metadata", diagnostic)
        self.assertIn("Target unchanged", diagnostic)
        self.assertFalse(self.target.exists())
        shutil.rmtree(self.heavy)
        self.heavy.symlink_to(self.template, target_is_directory=True)
        self.assert_refusal(self.cli("--heavy", "project"), "real directory")
        self.assertFalse(self.target.exists())
        self.assertEqual(self.cli("normal").returncode, 0)

    def test_helper_sources(self):
        for name in ("merge.py", "review_commit.py"):
            helper = self.repo / "tools" / name
            original = helper.read_bytes()
            for kind in ("missing", "link", "directory", "fifo"):
                with self.subTest(name=name, kind=kind):
                    helper.unlink()
                    if kind == "link":
                        helper.symlink_to(SCRIPT)
                    elif kind == "directory":
                        helper.mkdir()
                    elif kind == "fifo":
                        os.mkfifo(helper)
                    self.assert_refusal(self.cli("project"), "regular file")
                    self.assertFalse(self.target.exists())
                    if kind == "directory":
                        helper.rmdir()
                    elif kind != "missing":
                        helper.unlink()
                    helper.write_bytes(original)
        tools = self.repo / "tools"
        tools.rename(self.repo / "saved-tools")
        tools.symlink_to(self.repo / "saved-tools", target_is_directory=True)
        self.assert_refusal(self.cli("project"), "real directory")
        self.assertFalse(self.target.exists())

    def test_helper_collisions_and_shared_directories(self):
        names = ("merge.py", "review_commit.py")
        for layer in (self.template, self.heavy):
            for name in names:
                for kind in ("tools_file", "helper_file", "helper_dir"):
                    with self.subTest(layer=layer, name=name, kind=kind):
                        tools = layer / "tools"
                        if kind == "tools_file":
                            tools.write_text("collision")
                        else:
                            tools.mkdir()
                            if kind == "helper_file":
                                (tools / name).write_text("collision")
                            else:
                                (tools / name).mkdir()
                        args = (
                            ("--heavy", "project")
                            if layer == self.heavy
                            else ("project",)
                        )
                        self.assert_refusal(self.cli(*args), "collision")
                        self.assertFalse(self.target.exists())
                        if tools.is_dir():
                            shutil.rmtree(tools)
                        else:
                            tools.unlink()
        (self.template / "tools").mkdir()
        (self.template / "tools/base.txt").write_text("base")
        (self.heavy / "tools").mkdir()
        (self.heavy / "tools/heavy.txt").write_text("heavy")
        (self.repo / "tools/unrelated.py").write_text("unrelated")
        self.assertEqual(self.cli("--heavy", "project").returncode, 0)
        self.assertEqual((self.target / "tools/base.txt").read_text(), "base")
        self.assertEqual((self.target / "tools/heavy.txt").read_text(), "heavy")
        for name in names:
            self.assertEqual(
                (self.target / "tools" / name).read_bytes(),
                (self.repo / "tools" / name).read_bytes(),
            )
        self.assertFalse((self.target / "tools/unrelated.py").exists())

    def test_unreadable_helper_and_copy_collision(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("helper_fixture", SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = Path.open
        for name in ("merge.py", "review_commit.py"):
            helper = self.repo / "tools" / name

            def denied(path, *args, **kwargs):
                if path.resolve() == helper.resolve() and args and args[0] == "rb":  # noqa: B023
                    raise PermissionError("injected helper read failure")
                return original(path, *args, **kwargs)

            with (
                self.subTest(name=name, kind="unreadable"),
                mock.patch.object(module, "__file__", str(self.repo / "newproject.py")),
                mock.patch.object(sys, "argv", ["newproject.py", "project"]),
                mock.patch.object(Path, "open", denied),
                mock.patch("sys.stderr") as stderr,
            ):
                self.assertEqual(module.main(), 1)
                self.assertIn(
                    "injected helper read failure", str(stderr.write.call_args_list)
                )
                self.assertIn("Target unchanged", str(stderr.write.call_args_list))
                self.assertFalse(self.target.exists())

            def collide(path, *args, **kwargs):
                if (
                    path.resolve() == (self.target / "tools" / name).resolve()  # noqa: B023
                    and args
                    and args[0] == "xb"
                ):
                    path.write_text("appeared")
                return original(path, *args, **kwargs)

            with (
                self.subTest(name=name, kind="copy collision"),
                mock.patch.object(module, "__file__", str(self.repo / "newproject.py")),
                mock.patch.object(sys, "argv", ["newproject.py", "project"]),
                mock.patch.object(Path, "open", collide),
                mock.patch.dict(os.environ, self.env, clear=True),
                mock.patch("sys.stderr") as stderr,
            ):
                self.assertEqual(module.main(), 1)
                self.assertIn(
                    "Partial state may remain", str(stderr.write.call_args_list)
                )
                self.assertEqual((self.target / "tools" / name).read_text(), "appeared")
            shutil.rmtree(self.target)

    def test_layer_refusals_and_normal_independence(self):
        for kind in (
            "file",
            "ancestor",
            "reverse",
            "fragment",
            "utf8",
            "reserved",
            "missing",
            "empty",
        ):
            with self.subTest(kind=kind):
                if kind == "file":
                    (self.heavy / ".hidden").write_text("collision")
                elif kind == "ancestor":
                    (self.heavy / "nested" / "file").mkdir()
                elif kind == "reverse":
                    shutil.rmtree(self.heavy / "nested")
                    (self.heavy / "nested").write_text("collision")
                elif kind == "fragment":
                    (self.heavy / "AGENTS.add.md").write_text("")
                elif kind == "utf8":
                    (self.heavy / "AGENTS.add.md").write_bytes(b"\xff")
                elif kind == "reserved":
                    (self.template / "AGENTS.add.md").write_text("reserved")
                elif kind == "missing":
                    shutil.rmtree(self.heavy)
                else:
                    shutil.rmtree(self.heavy)
                    self.heavy.mkdir()
                result = self.cli("--heavy", "project")
                self.assert_refusal(
                    result,
                    {
                        "file": "collision",
                        "ancestor": "collision",
                        "reverse": "collision",
                        "fragment": "nonempty",
                        "utf8": "UTF-8",
                        "reserved": "reserved",
                        "missing": "real directory",
                        "empty": "empty",
                    }[kind],
                )
                self.assertFalse(self.target.exists())
                shutil.rmtree(self.heavy, ignore_errors=True)
                self.heavy.mkdir()
                (self.heavy / "AGENTS.add.md").write_text("heavy")
                (self.heavy / "nested").mkdir()
                (self.heavy / "nested" / "extra").write_text("addition")
                (self.template / "AGENTS.add.md").unlink(missing_ok=True)
        shutil.rmtree(self.heavy)
        self.assertEqual(self.cli("normal").returncode, 0)


class RealTemplateTests(unittest.TestCase):
    def test_generated_variants_and_installed_journal(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "source"
            source.mkdir()
            shutil.copy(SCRIPT, source / "newproject.py")
            shutil.copytree(SCRIPT.parent / "template", source / "template")
            shutil.copytree(SCRIPT.parent / "tools", source / "tools")
            env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
            env.update(
                HOME=str(root),
                XDG_CONFIG_HOME=str(root / "xdg"),
                GIT_CONFIG_NOSYSTEM="1",
            )
            for name, flags in [("normal", []), ("heavy", ["--heavy"])]:
                result = subprocess.run(  # noqa: S603 - controlled fixture
                    [sys.executable, str(source / "newproject.py"), *flags, name],
                    cwd=root,
                    env=env,
                    text=True,
                    capture_output=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                target = root / name
                self.assertEqual(
                    (target / "docs/workflow/HEAVY.md").exists(), bool(flags)
                )
                self.assertFalse((target / "AGENTS.add.md").exists())
                installed = target / "tools/merge.py"
                reference = source / "tools/merge.py"
                self.assertEqual(installed.read_bytes(), reference.read_bytes())
                self.assertEqual(
                    installed.stat().st_mode & 0o777, reference.stat().st_mode & 0o777
                )
                review_helper = target / "tools/review_commit.py"
                reference_review = source / "tools/review_commit.py"
                self.assertEqual(
                    review_helper.read_bytes(), reference_review.read_bytes()
                )
                self.assertEqual(
                    review_helper.stat().st_mode & 0o777,
                    reference_review.stat().st_mode & 0o777,
                )
                self.assertEqual(
                    {p.name for p in (target / "tools").iterdir()},
                    {"merge.py", "review_commit.py"},
                )
                for guide in (
                    "MERGE.md",
                    "MAIN-MESSAGE.md",
                    "BRANCH-MESSAGE.md",
                    "REVIEW-COMMIT.md",
                ):
                    self.assertTrue((target / "docs/workflow" / guide).is_file())

                def git(*args, target=target):
                    return subprocess.run(  # noqa: S603 - controlled fixture
                        ["git", *args],  # noqa: S607 - Git on PATH
                        cwd=target,
                        env=env,
                        text=True,
                        capture_output=True,
                        check=True,
                    ).stdout.strip()

                git("config", "user.name", "Test")
                git("config", "user.email", "test@example.invalid")
                git("add", ".")
                git("commit", "-m", "bootstrap")
                git("checkout", "-b", "feature")
                (target / "fixture.txt").write_text("merged")
                git("add", "fixture.txt")
                git("commit", "-m", "step: fixture")
                source_tip = git("rev-parse", "feature")
                git("checkout", "main")
                merged = subprocess.run(  # noqa: S603 - controlled fixture
                    [sys.executable, str(installed), "feature", "-m", "fixture merge"],
                    cwd=target,
                    env=env,
                    text=True,
                    capture_output=True,
                )
                self.assertEqual(merged.returncode, 0, merged.stderr)
                self.assertEqual(
                    git("show", "-s", "--format=%s", "HEAD"), "fixture merge"
                )
                self.assertEqual(git("rev-parse", "feature"), source_tip)
                self.assertEqual((target / "fixture.txt").read_text(), "merged")
                self.assertEqual(git("status", "--porcelain"), "")
                review_env = {k: v for k, v in env.items() if not k.startswith("GIT_")}
                report = target / "docs/worklog/001-review.md"
                report.parent.mkdir(parents=True, exist_ok=True)
                report.write_text("review report\n")
                review_head = git("rev-parse", "HEAD")
                command = [
                    sys.executable,
                    str(review_helper),
                    "--head",
                    review_head,
                    "-m",
                    "review: fixture",
                    "docs/worklog/001-review.md",
                ]
                reviewed = subprocess.run(  # noqa: S603
                    command, cwd=target, env=review_env, text=True, capture_output=True
                )
                self.assertEqual(reviewed.returncode, 0, reviewed.stderr)
                committed = git("rev-parse", "HEAD")
                self.assertEqual(reviewed.stdout.strip(), committed)
                self.assertEqual(
                    git("rev-list", "--parents", "-n", "1", "HEAD"),
                    f"{committed} {review_head}",
                )
                self.assertEqual(
                    git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"),
                    "docs/worklog/001-review.md",
                )
                self.assertEqual(report.read_text(), "review report\n")
                self.assertEqual(git("status", "--porcelain"), "")
                report.write_text("second report\n")
                foreign = target / "fixture.txt"
                foreign.write_text("foreign dirt\n")
                command[3] = committed
                refused = subprocess.run(  # noqa: S603
                    command, cwd=target, env=review_env, text=True, capture_output=True
                )
                self.assertNotEqual(refused.returncode, 0)
                self.assertIn("change outside supplied reports", refused.stderr)
                self.assertEqual(git("rev-parse", "HEAD"), committed)
                self.assertEqual(git("diff", "--cached", "--name-only"), "")
                self.assertEqual(report.read_text(), "second report\n")
                self.assertEqual(foreign.read_text(), "foreign dirt\n")
            journal = root / "heavy/scripts/workflow/work_log.py"
            result = subprocess.run(  # noqa: S603 - controlled fixture
                [
                    sys.executable,
                    str(journal),
                    "append",
                    "--task",
                    "fixture",
                    "--stage",
                    "test",
                    "--role",
                    "DEVELOPER",
                    "--agent",
                    "fixture",
                    "--event",
                    "check_result",
                    "--result",
                    "passed",
                ],
                cwd=root,
                env=env,
                text=True,
                capture_output=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "fixture", (root / "heavy/docs/workflow/work-log.jsonl").read_text()
            )
            self.assertFalse((root / "docs/workflow/work-log.jsonl").exists())
