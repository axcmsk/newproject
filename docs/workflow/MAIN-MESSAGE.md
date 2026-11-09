# Main commit messages

Use these rules for merge results and standalone commits made directly on `main`.

Use `type: description`, optionally `type(scope): description`. Choose the type
by the primary result, not file extensions or the merge operation. Supporting
documentation and tests do not change it. Agent instructions are part of the
implementation.

| Type | Result |
| --- | --- |
| `feat` | New functionality |
| `fix` | Bug fix |
| `docs` | Explanatory documentation without behavior changes |
| `refactor` | Restructuring code or instructions without changing behavior |
| `test` | Test changes without changes to product behavior |
| `chore` | Maintenance not covered above |

Scope names the affected area and is optional. A short subject is enough;
add a body after a blank line when explanation is useful.

For a breaking change, put `!` immediately before the colon and describe the
incompatibility in the subject, or add a `BREAKING CHANGE: description` footer
separated from preceding text by a blank line. This applies to any type.

Examples:

```text
feat(generator): add heavy project variant
fix(merge): preserve ignored files
feat(workflow): integrate merge helper
fix(workflow): correct review handoff instructions
refactor: simplify branch validation
test(merge): cover empty source branches
```

```text
feat(generator)!: require Python 3.11 or newer
```

```text
fix(config): reject unknown options

BREAKING CHANGE: Unknown options now cause an error instead of being ignored.
```

Based on [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).
This document contains all rules needed for main commit messages in this project.
