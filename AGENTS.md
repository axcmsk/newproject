# Agent entry point

These instructions apply to the entire repository. Explicit user instructions
and higher-priority environment instructions take precedence. A new user chat
starts as LEAD unless another role is assigned. A delegated agent uses its
assigned role; if none is given, ask the sender before acting. Keep the role
when resuming unless it is explicitly changed. Read your role guide first:
[LEAD](docs/workflow/roles/LEAD.md),
[DISPATCHER](docs/workflow/roles/DISPATCHER.md),
[DEVELOPER](docs/workflow/roles/DEVELOPER.md), or
[REVIEWER](docs/workflow/roles/REVIEWER.md).

Role guides name required reading. Do not load other role guides or historical
worklogs by default. [PROJECT-RULES](docs/workflow/PROJECT-RULES.md) holds the
project's factual, format and Git rules.
[PROCESS](docs/workflow/PROCESS.md) defines task inputs, reviews and acceptance.

## Communication

Use the user's language unless they request another language for a particular
response or artifact. Start every user-facing message, including progress
updates, with one bold label on a separate line, followed by a blank line:

- **Chat**: ordinary chat, when that mode is known.
- **Work Local**: agent work confirmed to execute on the user's computer.
- **Work Cloud**: agent work confirmed to execute in a cloud environment.
- **Work**: agent work whose execution location is not confirmed.

Determine the label from the environment, not the task topic. Files or terminal
access alone do not establish Local or Cloud. Do not put labels inside artifacts.

## Scope

Use the specification, implementation and independent review process for logic
changes: code, scripts, generator behavior, validation or schema rules, tests,
automation, and specifications that define that behavior. For mixed tasks,
apply the process to the logic changes.

LEAD may edit routine content and documentation directly when they do not
change behavior, requirements, authority or process. These changes need no
task brief, delegated developer or worklog report. Preserve documented formats
and factual rules; perform checks proportionate to the change.

Changes to agent roles or process rules receive independent static review.
These scope rules take precedence over role and check ownership rules in the
role guides and PROCESS.

Use separate agents for the roles required by PROCESS when delegation is
available and permitted. If independent review or a required model is unavailable,
report the limitation; do not present self-review as independent acceptance.
