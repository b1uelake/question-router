# Learning Contract

Use for concept learning, mechanism explanations, definitions, prerequisites, study paths, and confusion signals.

## Classify As Learning When

- The user asks "what is", "explain", "teach me", "how does X work", "I do not understand", or asks for a learning path.
- The main goal is intellectual understanding, not choosing, implementing, or diagnosing a specific operational problem.
- A terse concept name likely means "help me understand this".

## Ask First When

Ask 1-3 questions only when level or goal changes the explanation materially:

- "What do you already know about this?"
- "Do you want a quick overview, a worked example, or a learning path?"
- "Are you learning for coding, business/product work, exams, or general understanding?"

Do not ask before simple beginner definitions. Use compact mode.

## Answer Contract

Include:

- Problem type and assumptions.
- Minimal cognitive map: core concepts, key variables, common misconceptions, and major disagreements if relevant.
- Direct explanation at the user's level.
- One-sentence definitions for prerequisite terms introduced in the answer.
- One concrete example or analogy when useful.
- A check for understanding.
- Next learning steps.

For short concept questions, compress to:

- Problem type.
- Direct answer.
- Why it matters or when to use it.
- Example.
- Next step.

## Quality Rules

- Keep prerequisite hygiene: define terms the answer depends on immediately.
- Do not move a term to "next steps" if the current explanation already uses it.
- Avoid encyclopedia surveys.
- Avoid long prerequisite lists unless the user asks for a path.
- Avoid unexplained jargon.

## Example Routes

- "What is pytest?" -> learning, compact mode, no clarification; define `assert` if used.
- "Explain vector databases from scratch" -> learning; likely include cognitive map and example.
- "What should I learn before RAG?" -> learning + plan; ask about current level and target if missing.
