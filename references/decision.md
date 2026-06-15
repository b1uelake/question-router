# Decision Contract

Use when the user must choose, prioritize, approve, adopt, buy, defer, or stop.

## Classify As Decision When

- The user asks "should I", "which should I choose", "is X worth it", "do I still need", or asks for a recommendation among options.
- The answer should help a person or team act.
- The outcome depends on criteria, constraints, reversibility, and tradeoffs.

## Ask First When

Ask 1-3 questions when missing context changes the recommendation:

- "What is the decision you need to make and by when?"
- "What options are actually available?"
- "What matters most: speed, cost, quality, maintainability, learning value, risk, or flexibility?"
- "What constraints are fixed?"

If the user asks a broad public question, answer with criteria rather than a universal verdict.

## Answer Contract

Include:

- Decision to be made.
- Options under consideration.
- Decision criteria and weights when inferable.
- Tradeoffs, reversibility, dependencies, and constraints.
- Recommendation with confidence level.
- What evidence would change the recommendation.
- Failure cases.
- Next action.

## Quality Rules

- Do not give a verdict without criteria.
- Do not hide uncertainty behind confident language.
- For time-sensitive decisions, mark current-market or tooling claims for verification.
- Prefer "choose X if..., choose Y if..." when context is incomplete.

## Example Routes

- "Should I use React or Vue?" -> decision; ask about project/team/priorities if missing.
- "Do I still need to handwrite Python code in the AI era?" -> decision + learning; give criteria, not an absolute answer.
- "Should I use paid APIs or local models?" -> decision + risk; ask about budget, privacy, latency, and quality bar.
