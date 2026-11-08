# Merge messages

Use `type: description`, optionally `type(scope): description`. Describe the
result of the branch, not the merge operation. Choose the type by that result:

| Type | Result |
| --- | --- |
| `feat` | New functionality |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `refactor` | Code restructuring without behavior changes |
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
refactor: simplify branch validation
```

```text
feat(generator)!: require Python 3.11 or newer
```

```text
fix(config): reject unknown options

BREAKING CHANGE: Unknown options now cause an error instead of being ignored.
```

Based on [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).
This document contains all rules needed for merge messages in this project.
