# Branch commit messages

Use `<type>: <short description>` for work and report commits in task branches:

| Type | Result |
| --- | --- |
| `step` | A stage worth preserving for a separate revert or reuse |
| `fixup` | A correction or refinement of the current stage |
| `docs` | Supporting documentation |
| `review` | An independent review report |
| `log` | Check results, journal entries or status updates |

Choose by the main content, not the author's role. A standalone documentation
stage uses `step:`; a task's specification, implementation and review fixes may
be one stage.
