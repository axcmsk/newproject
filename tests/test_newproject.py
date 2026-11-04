import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / 'newproject.py'


class CreationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.repo = self.base / 'source'
        self.repo.mkdir()
        shutil.copy(SCRIPT, self.repo / 'newproject.py')
        self.template = self.repo / 'template'
        self.template.mkdir()
        (self.template / '.hidden').write_text('hidden')
        (self.template / 'nested').mkdir()
        (self.template / 'nested' / 'file').write_text('hello')
        self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        self.env['XDG_CONFIG_HOME'] = str(self.base / 'xdg')
        self.env.update(HOME=str(self.base), GIT_CONFIG_NOSYSTEM='1',
                        GIT_AUTHOR_NAME='Test', GIT_AUTHOR_EMAIL='test@example.invalid',
                        GIT_COMMITTER_NAME='Test', GIT_COMMITTER_EMAIL='test@example.invalid')
        self.target = self.base / 'project'

    def tearDown(self):
        self.tmp.cleanup()

    def run_cli(self, name='project', env=None, cwd=None):
        return subprocess.run([sys.executable, str(self.repo / 'newproject.py'), name],
                              cwd=cwd or self.base, env=env or self.env, text=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def git(self, *args, cwd=None, check=True):
        return subprocess.run(['git', *args], cwd=cwd or self.target, env=self.env,
                              text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check)

    def state(self, target):
        if target.is_symlink():
            return ('link', os.readlink(target))
        if not target.exists():
            return None
        if not target.is_dir():
            return ('file', target.read_bytes())
        result = {}
        for path in target.rglob('*'):
            key = str(path.relative_to(target))
            if path.is_symlink():
                result[key] = ('link', os.readlink(path))
            elif path.is_file():
                result[key] = ('file', path.read_bytes())
            else:
                result[key] = ('dir',)
        return result

    def assert_refusal(self, result, reason):
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(reason, result.stderr)
        self.assertIn('Cannot create project at', result.stderr)
        self.assertIn('Target unchanged', result.stderr)

    def assert_success(self, result, target=None):
        target = target or self.target
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / '.hidden').read_text(), 'hidden')
        self.assertEqual((target / 'nested' / 'file').read_text(), 'hello')
        self.assertEqual(set(p.name for p in target.iterdir()), {'.git', '.hidden', 'nested'})
        self.assertEqual(self.git('symbolic-ref', 'HEAD', cwd=target).stdout.strip(), 'refs/heads/main')
        self.assertNotEqual(self.git('rev-parse', '--verify', 'HEAD', cwd=target, check=False).returncode, 0)
        self.assertEqual(self.git('ls-files', '--stage', cwd=target).stdout, '')
        self.assertEqual(self.git('remote', cwd=target).stdout, '')

    def test_new_empty_and_existing_repositories(self):
        self.assert_success(self.run_cli(cwd=self.template))
        before = self.state(self.target)
        self.assert_refusal(self.run_cli(), 'target must be empty')
        self.assertEqual(before, self.state(self.target))
        self.target = self.base / 'empty'
        self.target.mkdir()
        self.assert_success(self.run_cli('empty'))
        self.target = self.base / 'existing'
        self.target.mkdir()
        self.git('init', '-b', 'other')
        self.git('config', 'example.keep', 'yes')
        self.assert_success(self.run_cli('existing'))
        self.assertEqual(self.git('config', 'example.keep').stdout.strip(), 'yes')

    def test_names_and_parent_git(self):
        self.git('init', '-b', 'parent', cwd=self.base)
        for name in ('space name', 'юникод', '$(touch danger)', '-dash'):
            with self.subTest(name=name):
                self.assert_success(self.run_cli(name), self.base / name)
        self.assertFalse((self.base / 'danger').exists())
        for name in ('', '.', '..', 'a/b', 'a\\b', 'bad\nname', 'bad\x7f', 'bad\x85'):
            with self.subTest(name=name):
                self.assert_refusal(self.run_cli(name), 'single directory name')

    def test_target_refusals(self):
        self.target.write_text('keep')
        self.assert_refusal(self.run_cli(), 'not a directory')
        self.assertEqual(self.target.read_text(), 'keep')
        self.target.unlink()
        self.target.symlink_to(self.base / 'missing')
        self.assert_refusal(self.run_cli(), 'symlink')
        self.target.unlink()
        self.target.symlink_to(self.template, target_is_directory=True)
        self.assert_refusal(self.run_cli(), 'symlink')
        self.target.unlink()
        self.target.mkdir()
        (self.target / 'keep').write_text('keep')
        self.assert_refusal(self.run_cli(), 'target must be empty')
        self.assertEqual((self.target / 'keep').read_text(), 'keep')

    def test_invalid_git_states(self):
        for kind in ('file', 'link', 'malformed', 'bare', 'staged', 'commit', 'ref'):
            with self.subTest(kind=kind):
                self.target = self.base / kind
                self.target.mkdir()
                dotgit = self.target / '.git'
                if kind == 'file':
                    dotgit.write_text('gitdir: nowhere')
                elif kind == 'link':
                    dotgit.symlink_to(self.template, target_is_directory=True)
                elif kind == 'malformed':
                    dotgit.mkdir()
                elif kind == 'bare':
                    self.git('init', '--bare', str(dotgit), cwd=self.base)
                else:
                    self.git('init', '-b', 'other')
                    if kind in ('staged', 'commit'):
                        (self.target / 'data').write_text('data')
                        self.git('add', 'data')
                        if kind == 'commit':
                            self.git('commit', '-m', 'test')
                            (self.target / 'data').unlink()
                        else:
                            (self.target / 'data').unlink()
                    else:
                        obj = self.git('hash-object', '-w', '--stdin', cwd=self.target).stdout.strip()
                        self.git('update-ref', 'refs/tags/test', obj)
                before = self.state(self.target)
                result = self.run_cli(kind)
                self.assert_refusal(result, {'file':'target must be empty', 'link':'target must be empty',
                    'malformed':'Git rev-parse failed', 'bare':'bare', 'staged':'staged entries',
                    'commit':'refs', 'ref':'refs'}[kind])
                self.assertEqual(before, self.state(self.target))

    def test_template_refusals(self):
        shutil.rmtree(self.template)
        self.assert_refusal(self.run_cli(), 'template must be a real directory')
        self.template.mkdir()
        self.assert_refusal(self.run_cli(), 'template is empty')
        (self.template / 'link').symlink_to(self.base / 'missing')
        self.assert_refusal(self.run_cli(), 'invalid template entry')
        (self.template / 'link').unlink()
        (self.template / '.git').mkdir()
        self.assert_refusal(self.run_cli(), 'invalid template entry')
        (self.template / '.git').rmdir()
        os.mkfifo(self.template / 'fifo')
        self.assert_refusal(self.run_cli(), 'invalid template entry')
        self.assertFalse(self.target.exists())

    def test_git_environment_isolation_and_missing_git(self):
        env = self.env.copy()
        env.update(GIT_DIR=str(self.base / 'redirect'), GIT_WORK_TREE=str(self.base),
                   GIT_INDEX_FILE=str(self.base / 'index'), GIT_CONFIG_COUNT='1',
                   GIT_CONFIG_KEY_0='init.defaultBranch', GIT_CONFIG_VALUE_0='wrong')
        self.assert_success(self.run_cli(env=env))
        self.assertFalse((self.base / 'redirect').exists())
        self.assertFalse((self.base / 'index').exists())
        env['PATH'] = str(self.base / 'no-git')
        self.assert_refusal(self.run_cli('missing', env=env), 'Git executable not found')
        self.assertFalse((self.base / 'missing').exists())

    def test_traversal_failure_before_mutation(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('project_cli_walk', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        def failed_walk(source, followlinks, onerror):
            yield str(source), ['nested'], ['.hidden']
            onerror(PermissionError(13, 'injected enumeration failure', str(source / 'nested')))
        self.target.mkdir()
        before = self.state(self.target)
        with mock.patch.object(module, '__file__', str(self.repo / 'newproject.py')), \
             mock.patch.object(sys, 'argv', ['newproject.py', 'project']), \
             mock.patch.object(module.os, 'walk', failed_walk), \
             mock.patch('sys.stderr') as stderr:
            self.assertEqual(module.main(), 1)
        diagnostic = ''.join(str(c) for c in stderr.write.call_args_list)
        self.assertIn('template traversal failed', diagnostic)
        self.assertIn('nested', diagnostic)
        self.assertIn('Target unchanged', diagnostic)
        self.assertEqual(before, self.state(self.target))

    def test_ambient_git_template_is_ignored(self):
        template = self.base / 'git-template'
        template.mkdir()
        fixture = self.base / 'fixture'
        fixture.mkdir()
        self.git('init', '-b', 'other', cwd=fixture)
        (fixture / 'staged').write_text('staged')
        self.git('add', 'staged', cwd=fixture)
        self.git('remote', 'add', 'contaminant', 'https://example.invalid/repo', cwd=fixture)
        shutil.copytree(fixture / '.git', template, dirs_exist_ok=True)
        self.git('config', '--global', 'init.templateDir', str(template), cwd=self.base)
        self.assert_success(self.run_cli())
        self.assertEqual(self.git('for-each-ref', '--format=%(refname)').stdout, '')
        self.assertFalse((self.target / '.git' / 'index').exists())
        self.assertEqual(self.git('remote').stdout, '')

    def test_contaminated_environment_stays_in_fixture(self):
        sentinel = self.base / 'sentinel'
        sentinel.mkdir()
        self.git('init', '-b', 'sentinel', cwd=sentinel)
        (sentinel / 'keep').write_text('safe')
        self.git('add', 'keep', cwd=sentinel)
        before = self.state(sentinel)
        config = self.base / 'outside-config'
        config.write_text('[alias]\n  sentinel = status\n')
        config_before = config.read_bytes()
        contaminated = self.env.copy()
        contaminated.update(GIT_DIR=str(sentinel / '.git'), GIT_WORK_TREE=str(sentinel),
                            GIT_INDEX_FILE=str(sentinel / '.git' / 'index'),
                            GIT_CONFIG_GLOBAL=str(config), GIT_CONFIG_COUNT='1',
                            GIT_CONFIG_KEY_0='init.templateDir', GIT_CONFIG_VALUE_0=str(sentinel / '.git'))
        self.assert_success(self.run_cli(env=contaminated))
        self.assertEqual(before, self.state(sentinel))
        self.assertEqual(config_before, config.read_bytes())

    def test_init_failure_partial_state(self):
        fake = self.base / 'bin'
        fake.mkdir()
        git = fake / 'git'
        git.write_text('#!/bin/sh\nif [ "$1" = --version ]; then exit 0; fi\necho injected-init-failure >&2\nexit 1\n')
        git.chmod(0o755)
        env = self.env.copy()
        env['PATH'] = str(fake)
        result = self.run_cli(env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('injected-init-failure', result.stderr)
        self.assertIn('Partial state may remain', result.stderr)
        self.assertTrue(self.target.is_dir())

    def test_copy_failure_reports_partial_state_and_preserves_file(self):
        # Load the CLI as a module and inject a collision at the copy boundary.
        import importlib.util
        spec = importlib.util.spec_from_file_location('project_cli', SCRIPT)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = Path.open
        def collide(path, *args, **kwargs):
            if path.name == '.hidden' and args and args[0] == 'xb':
                path.write_text('appeared')
            return original(path, *args, **kwargs)
        with mock.patch.object(module, '__file__', str(self.repo / 'newproject.py')), \
             mock.patch.object(sys, 'argv', ['newproject.py', 'project']), \
             mock.patch.object(Path, 'open', collide), \
             mock.patch.dict(os.environ, self.env, clear=True), \
             mock.patch('sys.stderr') as stderr:
            self.assertEqual(module.main(), 1)
        self.assertEqual((self.target / '.hidden').read_text(), 'appeared')
        self.assertIn('Partial state may remain', ''.join(str(c) for c in stderr.write.call_args_list))


if __name__ == '__main__':
    unittest.main()
