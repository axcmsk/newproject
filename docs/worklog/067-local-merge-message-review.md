# Local merge-message guide review

- Verdict: `ACCEPTED`.
- Reviewed source and review-start HEAD:
  `e300f59b8faaf155796ed5745501d1009e55c2cc`.
- Baseline: `b4e951b4e28ce8d1ae2e1249cf898939a2ce6905`.
- Assignment: `docs/worklog/066-local-merge-message-guide.md` at source.
- Scope: MERGE-MESSAGE and its references from MERGE and PROJECT-RULES.
- Findings and conditions: none.
- Next owner/action: LEAD reports completion after verifying the report commit.

The guide is self-contained for the project's selected convention: it states
the type meanings, subject syntax, optional scope/body, breaking-change placement
and description, with consistent examples. These agree with the previously
consulted Conventional Commits 1.0.0 source; the upstream link serves as attribution.
The completeness statement concerns project merge messages, not every optional
feature of the upstream specification.

Both merge modes, LEAD's message responsibility, unchanged work/report prefixes
and the helper's lack of inference/validation remain explicit. Local references
resolve to the new guide. No runtime, template or generator changes are included.
Prior check evidence remains applicable to unchanged inputs. Review was static
only, starting at the exact source with a clean tree. Commit only this report
after HEAD/index/path verification, return its hash separately and release ownership.
No executable checks, source edits, merge or push were performed.
