# Writing the work log

From the generated project, use `python3 scripts/workflow/work_log.py append`
under exclusive writer ownership. DISPATCHER records events; DEVELOPER maintains
and tests the tool. Do not manually construct or append JSON lines. The script
is authoritative for fields and validation: use `schema` or `append --help`.
New records use version 2; admitted v1/v2 history is preserved unchanged.

```sh
python3 scripts/workflow/work_log.py append \
  --task example --stage implementation \
  --role DISPATCHER --agent dispatcher \
  --event transition --result 'Ready for review' --ref SOURCE_COMMIT
```

Replace example values with actual facts. The default journal path is relative
to the installed script's project root, independent of the working directory.
`--log` selects another local JSONL file. Parent directories must already exist.
Append requires POSIX `fcntl.flock` (such as macOS/Linux); unsupported platforms
refuse clearly. `schema` and help do not require locking. No third-party Python
packages are needed. The lock supplements, rather than replaces, writer ownership.

## Provenance and timing

The tool adds a unique ID and UTC write time, validates supplied data and appends
one line. It does not verify the truth of a claim, query usage or grant permission.
For reconciliation use a known `--id`; duplicate IDs are refused.

Omit `--at` for an event happening now. For a known past event, supply its UTC
time; write time remains separate as `recorded_at`. If past time is unknown,
record receipt time and explain in `--note`; never invent timestamps.

Timing is optional: `--timing-file` supplies observed timing data and `--span`
a known span ID. Open durations remain unknown. The tool does not manage spans
or infer task duration. `--allowance-file` accepts an actual supplied sample
with its original time and source; ordinary events use null. Carried samples
are not fresh observations. Apply LIMITS separately.

Elapsed intervals include waits. Do not double-count overlaps or attribute HUMAN
wait and unobserved gaps to agent effort. Shared allowance changes are not precise
task/agent billing; retain window/reset identities and disclose other activity.

## Corrections and uncertainty

Correct facts with a new `correction` event and `--supersedes ID`; preserve the
original. `return` and `blocked` require `--cause`; use unknown when necessary.
Other failure events also need an explicit cause from the writer; the tool cannot
infer failure from prose. Invalid input appends no record (a missing log may be
created empty). Malformed/truncated history is refused without automatic repair.

After a failed/interrupted append, inspect the known ID and existing bytes before
retrying. Preserve partial bytes; never assume an error means nothing was written.
If the journal is frozen for review, buffer facts outside the repository until
released. Urgent blockers still go to LEAD; a changed fact affecting a review's
authority, scope or assumptions must reach REVIEWER immediately.

Record meaningful transitions, results, blockers and allowance checkpoints at
existing handoffs, not polling or transcripts. Link raw evidence rather than
copying it. Do not store secrets, cookies, private text or prompts. Group journal
changes with normal checkpoint/review commits; do not commit every event.
The journal replaces neither STATE nor raw evidence and never resets budgets.
