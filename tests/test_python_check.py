import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

EXPECTED_TARGETS = ["tools", "newproject.py", "tests", "template/heavy/scripts"]
SCRIPT = Path(__file__).resolve().parents[1] / "tools/python_check.py"
spec = importlib.util.spec_from_file_location("check_helper", SCRIPT)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


class CheckTests(unittest.TestCase):
    def run_checks(self, responses, reformat=False, only=None):
        stream = io.StringIO()
        errors = io.StringIO()
        with (
            mock.patch.object(helper.subprocess, "run", side_effect=responses) as run,
            contextlib.redirect_stdout(stream),
            contextlib.redirect_stderr(errors),
        ):
            status = helper.run_checks(reformat, only)
        return status, stream.getvalue(), errors.getvalue(), run

    def test_sequence_arguments_cwd_and_success(self):
        status, output, _, run = self.run_checks(
            [subprocess.CompletedProcess([], 0) for _ in range(3)]
        )
        self.assertEqual(status, 0)
        calls = run.call_args_list
        self.assertEqual(len(calls), 3)
        python = str(helper.ROOT / ".venv/bin/python")
        self.assertEqual(
            calls[1].args[0], [python, "-m", "ruff", "check", *EXPECTED_TARGETS]
        )
        self.assertEqual(
            calls[0].args[0],
            [python, "-m", "ruff", "format", "--check", *EXPECTED_TARGETS],
        )
        self.assertEqual(
            calls[2].args[0],
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        )
        for call in calls:
            self.assertEqual(call.kwargs, {"cwd": helper.ROOT, "check": False})
        self.assertIn("Summary: format: exit 0; lint: exit 0; tests: exit 0", output)

    def test_failure_and_launch_error_continue(self):
        status, output, _, run = self.run_checks(
            [
                subprocess.CompletedProcess([], 2),
                FileNotFoundError("missing Ruff"),
                subprocess.CompletedProcess([], 0),
            ]
        )
        self.assertEqual(status, 1)
        self.assertEqual(run.call_count, 3)
        self.assertIn("format: exit 2", output)
        self.assertIn("lint: launch error: missing Ruff", output)
        self.assertIn("tests: exit 0", output)
        self.assertIn("Summary:", output)

    def test_reformat_sequence_and_failure_continuation(self):
        for first in (
            subprocess.CompletedProcess([], 2),
            FileNotFoundError("missing Ruff"),
        ):
            with self.subTest(first=first):
                status, output, _, run = self.run_checks(
                    [
                        first,
                        subprocess.CompletedProcess([], 0),
                        subprocess.CompletedProcess([], 0),
                    ],
                    reformat=True,
                )
                python = str(helper.ROOT / ".venv/bin/python")
                self.assertEqual(status, 1)
                self.assertEqual(run.call_count, 3)
                self.assertEqual(
                    run.call_args_list[0].args[0],
                    [python, "-m", "ruff", "format", *EXPECTED_TARGETS],
                )
                self.assertEqual(
                    run.call_args_list[1].args[0],
                    [python, "-m", "ruff", "check", *EXPECTED_TARGETS],
                )
                self.assertEqual(
                    run.call_args_list[2].args[0],
                    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
                )
                self.assertIn(
                    "format: exit 2"
                    if isinstance(first, subprocess.CompletedProcess)
                    else "format: launch error: missing Ruff",
                    output,
                )
                self.assertIn("lint: exit 0", output)
                self.assertIn("tests: exit 0", output)

    def test_flag_propagation(self):
        for args, expected in (
            ([], (False, None)),
            (["--reformat"], (True, None)),
            (["--only", "format"], (False, "format")),
            (["--only", "lint"], (False, "lint")),
            (["--only", "tests"], (False, "tests")),
        ):
            with (
                self.subTest(args=args),
                mock.patch.object(helper.sys, "argv", ["python_check.py", *args]),
                mock.patch.object(helper, "run_checks", return_value=0) as run,
            ):
                self.assertEqual(helper.main(), 0)
                run.assert_called_once_with(*expected)

    def test_selected_commands_and_summary(self):
        python = str(helper.ROOT / ".venv/bin/python")
        cases = (
            (
                "format",
                False,
                [python, "-m", "ruff", "format", "--check", *EXPECTED_TARGETS],
            ),
            ("format", True, [python, "-m", "ruff", "format", *EXPECTED_TARGETS]),
            ("lint", False, [python, "-m", "ruff", "check", *EXPECTED_TARGETS]),
            (
                "tests",
                False,
                [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
            ),
        )
        for selected, reformat, command in cases:
            with self.subTest(selected=selected, reformat=reformat):
                status, output, _, run = self.run_checks(
                    [subprocess.CompletedProcess([], 0)], reformat, selected
                )
                self.assertEqual(status, 0)
                run.assert_called_once_with(command, cwd=helper.ROOT, check=False)
                self.assertIn(f"Summary: {selected}: exit 0", output)
                for omitted in {"format", "lint", "tests"} - {selected}:
                    self.assertNotIn(f"{omitted}:", output)

    def test_selected_failure_launch_error_and_interrupt(self):
        for response, code, detail in (
            (subprocess.CompletedProcess([], 3), 1, "exit 3"),
            (FileNotFoundError("missing"), 1, "launch error: missing"),
            (KeyboardInterrupt(), 130, "interrupted"),
        ):
            with self.subTest(response=response):
                status, output, errors, run = self.run_checks([response], only="format")
                self.assertEqual(status, code)
                self.assertEqual(run.call_count, 1)
                self.assertIn(detail, errors if code == 130 else output)
                self.assertEqual("Summary:" in output, code != 130)

    def test_selection_arguments_and_invalid_combinations(self):
        for args in (
            ["--only", "format", "--reformat"],
            ["--reformat", "--only", "format"],
        ):
            with (
                self.subTest(args=args),
                mock.patch.object(helper.sys, "argv", ["python_check.py", *args]),
                mock.patch.object(helper, "run_checks", return_value=0) as run,
            ):
                self.assertEqual(helper.main(), 0)
                run.assert_called_once_with(True, "format")
        for args in (
            ["--only"],
            ["--only", "unknown"],
            ["--reformat", "--only", "lint"],
            ["--only", "tests", "--reformat"],
        ):
            with (
                self.subTest(args=args),
                mock.patch.object(helper.sys, "argv", ["python_check.py", *args]),
                mock.patch.object(helper, "run_checks") as run,
                contextlib.redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit) as result,
            ):
                helper.main()
            self.assertEqual(result.exception.code, 2)
            run.assert_not_called()

    def test_reformat_changes_temporary_file(self):
        real_run = subprocess.run
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "tools").mkdir()
            (root / "tests").mkdir()
            (root / "template/heavy/scripts").mkdir(parents=True)
            (root / "newproject.py").write_text("value=  1\n")

            def bounded(command, **kwargs):
                if command[3] == "format":
                    return real_run(
                        [str(SCRIPT.parent.parent / ".venv/bin/python"), *command[1:]],
                        **kwargs,
                    )
                return subprocess.CompletedProcess(command, 0)

            with (
                mock.patch.object(helper, "ROOT", root),
                mock.patch.object(helper.subprocess, "run", side_effect=bounded),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(helper.run_checks(True), 0)
            self.assertEqual((root / "newproject.py").read_text(), "value = 1\n")

    def test_interrupt_stops_sequence(self):
        status, output, errors, run = self.run_checks(
            [subprocess.CompletedProcess([], 0), KeyboardInterrupt()]
        )
        self.assertEqual(status, 130)
        self.assertEqual(run.call_count, 2)
        self.assertIn("interrupted", errors)
        self.assertNotIn("Summary:", output)
        self.assertNotIn("tests:", output)

    def test_help_and_bad_arguments_do_not_launch_checks(self):
        for args, expected in [(["--help"], 0), (["unexpected"], 2)]:
            with (
                self.subTest(args=args),
                mock.patch.object(helper.sys, "argv", ["python_check.py", *args]),
                mock.patch.object(helper, "run_checks") as run,
                contextlib.redirect_stdout(io.StringIO()),
                contextlib.redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit) as result,
            ):
                helper.main()
            self.assertEqual(result.exception.code, expected)
            run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
