# Coverage integration specification review

Verdict: `ACCEPTED`.

Reviewed report 147 at frozen HEAD
`e71cebfb302df1406d3cf2a54838ab6c94d1a124`, against baseline main
`4ab7fe19f5f0ba1102750a57699d18a599d8df23` and the pinned accepted tips
`f98fe2aef3784361d547f717ff0c85ea70b401ad` (Python) and
`67e5239cd9ad3a75f8fcb46b6024b0b3dd5acea0` (Go), including their specifications,
execution evidence, and reviews. Only allowed report: this file.

No blocking findings. The integration preserves both accepted behaviors,
current main's Go tooling, historical reports, and static reviewer authority.
Python JSON is a bounded addition using existing measured data;
[coverage.py 7.10.7 documents this command directly](https://coverage.readthedocs.io/en/7.10.7/commands/cmd_json.html).
Keeping Go's native machine-readable profile without a converter is consistent
with HUMAN's inexpensive-only condition and avoids a false coverage-JSON claim.

Combined checks, canonical-file and JSON/HTML/terminal accounting comparisons,
failure propagation, and final tree verification cover the integration risks.
Document ownership and conflict escalation are clear. The newly authorized
merge is reserved for LEAD after final acceptance; source branches and .idea
are preserved, with no push.

LEAD reported baseline `make check` passing formatting, lint, and 69 tests
in 31.558 seconds. Only the assignment was added before review. REVIEWER ran
no executable checks. This verdict accepts the specification, not the combined
implementation. Next owner: LEAD may release this exact assignment to DISPATCHER.
Report-writer ownership is released after commit.

## Additional HUMAN requirement and conditional acceptance

Updated verdict: `ACCEPTED_SUBJECT_TO_CHECKS`. This supersedes the initial
verdict above for the new reading-instructions scope received after that review.
The reviewed specification base remains `e71cebfb302df1406d3cf2a54838ab6c94d1a124`.
LEAD may close the following through DISPATCHER without another spec review:

C1: Append exactly the following to report 147, with no other spec edits:

```text
## Coverage report reading instructions

HUMAN additionally requests explicit REVIEWER reading instructions. Python review
uses coverage.json; Go review uses coverage/functions.txt and coverage/coverage.out.
HTML is supplementary for browsing source. DEVELOPER supplies accessible report
paths and measured source identity. LEAD may update root/base REVIEWER and PROCESS
with generic static report-reading guidance, and README/make-checks documentation
with the concrete report mapping. REVIEWER does not execute coverage. These
instructions are included in the final independent implementation review.
```

Evidence: report 147's final section must match that literal text, with the
preceding specification unchanged. The new scope is consistent with HUMAN's
request: language-specific artifact choices stay in project documentation;
shared roles retain static-only authority. The concrete downstream documentation
changes require final implementation review and are not pre-approved verbatim.

C2: LEAD runs `make check` after C1 and commits the corrected spec only after
success. Save closure evidence in
`/private/tmp/coverage-integration-spec-closure.txt` with these exact fields:

```text
Reviewed base: e71cebfb302df1406d3cf2a54838ab6c94d1a124
Command: make check
Formatting: PASS
Lint: PASS
Tests: 69 passed
Overall exit: 0
Corrected commit: FULL_HASH
```

Replace `FULL_HASH` with the full corrected commit ID; all other fields must
match literally and reflect observed results. DISPATCHER may close C1/C2 only
if that commit differs from the reviewed base solely by C1 and report 148,
the evidence matches, and the corrected identity is retained with the base
and this review. Any mismatch or additional spec change returns to REVIEWER.
Do not claim the corrected spec was separately reviewed. Release the developer
only after both conditions close; final implementation acceptance remains pending.
