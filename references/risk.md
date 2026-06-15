# Risk Contract

Use for downside analysis, red teaming, compliance, safety, security, finance, legal, medical, and high-stakes uncertainty.

## Classify As Risk When

- The user asks "what could go wrong", "is this safe", "evaluate risk", "red team", "failure modes", or asks about compliance/security/safety.
- The answer should identify downside, likelihood, impact, controls, and verification needs.
- The question is high-stakes or error costs are material.

## Ask First When

Ask 1-3 questions when scope or control environment changes the risk profile:

- "What exact action or design are you considering?"
- "What environment, jurisdiction, users, or data sensitivity applies?"
- "What controls or constraints are already in place?"

For legal, medical, financial, security, or compliance claims, mark verification needs clearly.

## Answer Contract

Include:

- Risk scope and assumptions.
- Failure modes.
- Likelihood and impact using qualitative labels unless data supports numbers.
- Leading indicators.
- Mitigations and contingency plans.
- What must be verified before action.
- Residual risk.

## Quality Rules

- Avoid false precision.
- Do not substitute generic disclaimers for concrete controls.
- Separate risk from uncertainty.
- Say what source, expert, test, or owner would resolve the uncertainty.

## Example Routes

- "What could go wrong if I store passwords with SHA-256?" -> risk; include salt, slow password hashing, breach impact, and verification.
- "Can I skip GDPR compliance because I only have 50 users?" -> risk; mark legal verification and likely unsafe assumptions.
- "Red team my launch plan" -> risk + plan; ask scope if missing.
