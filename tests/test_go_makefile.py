"""Exercise the copyable Go Makefile without network or global tool writes."""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parents[1] / "examples" / "go"


class GoMakefileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.module = self.root / "module"
        shutil.copytree(TEMPLATE, self.module)
        self.bin = self.root / "bin"
        self.bin.mkdir()
        self.tools = self.root / "tools with spaces"
        self.log = self.root / "log"
        self.env = os.environ.copy()
        self.env.update(PATH=f"{self.bin}:{self.env['PATH']}", LOG=str(self.log))
        self.executable(
            self.bin / "go",
            '#!/bin/sh\necho "go $*" >> "$LOG"\nexit "${GO_STATUS:-0}"\n',
        )
        self.executable(
            self.bin / "curl",
            '#!/bin/sh\necho curl >> "$LOG"\n'
            '[ "${CURL_FAIL:-0}" = 0 ] || exit 7\n'
            'while [ "$1" != "-o" ]; do shift; done\n'
            'cp "$INSTALLER" "$2"\n',
        )
        self.installer = self.root / "installer"
        self.executable(
            self.installer,
            '#!/bin/sh\necho "install $*" >> "$LOG"\n'
            '[ "${INSTALL_FAIL:-0}" = 0 ] || exit 8\n'
            'cp "$LINTER" "$2/golangci-lint"\n',
        )
        self.linter = self.root / "linter"
        self.executable(
            self.linter,
            '#!/bin/sh\necho "lint $*" >> "$LOG"\n'
            'case "$*" in\n'
            '  "fmt --diff") [ "${FMT_FAIL:-0}" = 0 ] || { echo error-diff; exit 9; }; '
            '[ "${DIRTY:-0}" = 0 ] || echo diff;;\n'
            "  fmt) echo formatted > source.go;;\n"
            '  run) exit "${LINT_FAIL:-0}";;\n'
            "esac\n",
        )
        self.env.update(INSTALLER=str(self.installer), LINTER=str(self.linter))
        (self.module / "source.go").write_text("original\n")

    @staticmethod
    def executable(path, content):
        path.write_text(content)
        path.chmod(0o755)

    def make(self, *targets, **env):
        return subprocess.run(  # noqa: S603 - controlled test inputs
            [
                shutil.which("make"),
                "-C",
                str(self.module),
                f"TOOLS_DIR={self.tools}",
                *targets,
            ],
            env={**self.env, **env},
            capture_output=True,
            text=True,
            check=False,
        )

    def loglines(self):
        return self.log.read_text().splitlines() if self.log.exists() else []

    def test_default_order_install_and_reuse(self):
        result = self.make()
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = self.loglines()
        self.assertEqual(lines[0], "curl")
        self.assertIn("v2.15.0", lines[1])
        self.assertEqual(lines[2:], ["lint fmt --diff", "lint run", "go test ./..."])
        self.assertEqual(self.make("check").returncode, 0)
        self.assertEqual(self.loglines().count("curl"), 1)

    def test_parallel_install_once(self):
        result = self.make("-j", "check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.loglines().count("curl"), 1)
        self.assertEqual(sum(x.startswith("install ") for x in self.loglines()), 1)

    def test_install_failures_stop_target(self):
        for variable in ("CURL_FAIL", "INSTALL_FAIL"):
            with self.subTest(variable=variable):
                result = self.make("format", **{variable: "1"})
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((self.tools / "golangci-lint").exists())
                self.assertNotIn("lint fmt --diff", self.loglines())

    def test_test_target_does_not_install_and_propagates_failure(self):
        self.assertEqual(self.make("test").returncode, 0)
        self.assertEqual(self.loglines(), ["go test ./..."])
        self.assertNotEqual(self.make("test", GO_STATUS="2").returncode, 0)
        self.assertFalse(self.tools.exists())

    def test_format_is_read_only_and_reformat_writes(self):
        source = self.module / "source.go"
        for variable in ("DIRTY", "FMT_FAIL"):
            result = self.make("format", **{variable: "1"})
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(source.read_text(), "original\n")
            self.assertIn("diff", result.stdout)
        self.assertEqual(self.make("reformat").returncode, 0)
        self.assertEqual(source.read_text(), "formatted\n")

    def test_lint_failure(self):
        self.assertNotEqual(self.make("lint", LINT_FAIL="3").returncode, 0)

    def test_explicit_tools(self):
        self.assertEqual(self.make("tools").returncode, 0)
        self.assertTrue((self.tools / "golangci-lint").is_file())


if __name__ == "__main__":
    unittest.main()
