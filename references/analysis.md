# Analysis Contract

Use for breaking down causes, patterns, tradeoffs, comparisons, business models, systems, arguments, and "why" questions.

## Classify As Analysis When

- The user asks "why", "analyze", "compare", "break down", "what is really happening", or asks how a phenomenon works in practice.
- The user wants an explanation of forces and relationships, not just a definition.
- The question involves tradeoffs, incentives, constraints, causal factors, or competing interpretations.

Tiebreaker: "why" questions are analysis unless the user is clearly asking for a basic definition.

## Ask First When

Ask 1-3 questions when scope, audience, or decision context would materially change the analysis:

- "Are you asking for technical mechanics, business model, risks, or all three?"
- "Is this for personal learning, investment/business decision, product planning, or implementation?"
- "What geography, market, time period, or source boundary matters?"

Proceed with assumptions when the request is general and safe.

## Answer Contract

Include:

- Problem type and assumptions.
- Problem frame and scope.
- Key variables and relationships.
- Competing interpretations or hypotheses.
- Known facts, reasonable inferences, recommendations, and uncertainty.
- Judgment criteria.
- Counterexamples or cases where the interpretation fails.
- Prioritized next actions.

## Quality Rules

- Do not treat one plausible explanation as certain.
- Do not list factors without ranking which matter most.
- Separate source-backed facts from inference.
- Mark legal, compliance, pricing, market-current, or high-stakes claims for verification.

## Example Routes

- "Why do startups choose microservices over monoliths?" -> analysis; include counterexamples and criteria.
- "Analyze how token relay businesses are built and monetized" -> analysis + risk; include costs, pricing, compliance, and uncertainty.
- "Compare LangChain and LlamaIndex" -> analysis; ask for use case if recommendation is expected.
