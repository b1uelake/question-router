# Technical Contract

Use for implementation, debugging, architecture, testing, infrastructure, automation, data processing, and codebase work.

## Classify As Technical When

- The user asks "how do I build/implement/fix/debug/test/deploy".
- The answer depends on tools, code, runtime, environment, APIs, logs, data, or system architecture.
- There is a concrete artifact or system the user can act on.

## Ask First When

Ask 1-3 questions when missing environment details change the path:

- "What framework, runtime, version, or provider are you using?"
- "What exact error, log, input, or observed behavior do you see?"
- "What sits around the system: proxy, CDN, database, queue, deployment platform, or CI?"

For debugging, key unknowns include stack, framework/server, logs, and reproduction conditions.

Proceed directly when the user provides enough local context or asks for a general architecture overview.

## Answer Contract

Include:

- Task classification and success criteria.
- Current environment or code assumptions.
- Minimal design or debugging hypothesis.
- Implementation steps.
- Edge cases and tests.
- Verification commands or checks.
- Rollback or limitation notes when relevant.

## Quality Rules

- Do not invent APIs, files, tables, or commands without checking available context.
- Do not skip verification when commands or tests are available.
- Prefer repo patterns and existing tooling when working in a codebase.
- For implementation work, finish with what changed and how it was verified.

## Example Routes

- "My Python API returns 502 under load" -> technical; ask about proxy, framework/server, and logs before detailed debugging plan.
- "How do I build a RAG app?" -> technical + plan; clarify stack and target if needed.
- "Implement this feature" -> technical; inspect codebase first and verify with tests.
