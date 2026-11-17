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

## Personal instructions

If [COMMON.md](../agent-personal/COMMON.md) exists beside the project in
`../agent-personal/`, read it before the first user-facing response and follow
its reading and communication rules. Silently skip a missing file.
For generated projects, resolve this path from the generated project root.

## Scope

Code and agent instructions are implementation. Assess changes by their effect
on behavior, regardless of file format.

Every change requires applicable checks and independent review, including
content, documentation and typo corrections. Use PROCESS’s
[route selection](docs/workflow/PROCESS.md#choosing-the-route) for direct
implementation by LEAD or delegation with a full specification.

These scope rules take precedence over role and check ownership rules in the
role guides and PROCESS.

Use separate agents for the roles required by PROCESS when delegation is
available and permitted. If independent review or a required model is unavailable,
report the limitation; do not present self-review as independent acceptance.
