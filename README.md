# Question Router

A [Codex](https://github.com/anthropics/claude-code) / [Claude Code](https://claude.ai/code) skill that turns under-specified questions into well-framed, high-quality answers. It classifies the request, checks context sufficiency, asks only necessary clarifying questions, loads the relevant response contract, and validates the answer before finalizing.

## How It Works

The skill routes every question through a structured pipeline:

1. **Classify** — determine the primary question type
2. **Check context** — identify missing information that would materially change the answer
3. **Clarify (if needed)** — ask the fewest useful questions (1–3, max 5)
4. **Load contract** — apply a type-specific response structure
5. **Validate** — run a quality gate before finalizing

### Six Question Types

| Type | Use For | Example |
|------|---------|---------|
| `learning` | Concepts, explanations, learning paths | "What is pytest?" |
| `analysis` | Causes, tradeoffs, comparisons, "why" questions | "Why do startups choose microservices?" |
| `decision` | Choosing, prioritizing, adopting | "Should I use React or Vue?" |
| `plan` | Roadmaps, study plans, step-by-step sequences | "Build me a 10-week AI study plan" |
| `risk` | Failure modes, security, compliance, safety | "Is it safe to skip GDPR compliance?" |
| `technical` | Implementation, debugging, architecture | "My API returns 502 under load" |

## Answer Structure

Every full answer includes nine mandatory elements:

1. **Problem type** — classification and framing
2. **Assumptions** — what was inferred from incomplete context
3. **Known facts** — source-backed or widely established
4. **Reasonable inferences** — what follows from known facts
5. **Recommendations** — actionable guidance with confidence level
6. **Uncertainty / needs verification** — what should be checked
7. **Judgment standards** — criteria used to evaluate options
8. **Counterexamples or failure cases** — where the answer breaks
9. **Prioritized next actions** — ordered, concrete steps

For simple beginner questions, a compact mode compresses this into: type, direct answer, why it matters, example, next step.

## Repository Structure

```
question-router/
├── SKILL.md                           # Skill definition and core workflow
├── agents/
│   └── openai.yaml                    # Agent interface definition
├── references/                        # Response contracts per type
│   ├── learning.md
│   ├── analysis.md
│   ├── decision.md
│   ├── plan.md
│   ├── risk.md
│   └── technical.md
├── evals/
│   └── evals.json                     # Regression test cases
├── schemas/
│   ├── eval-case.schema.json          # JSON Schema for eval cases
│   └── route.schema.json              # JSON Schema for internal route objects
└── scripts/
    ├── validate_skill.py              # Validate skill structure and evals
    ├── build_promptfoo_config.py      # Generate promptfoo eval config
    └── run_evals.sh                   # Full eval pipeline (validate → build → run)
```

## Getting Started

### Prerequisites

- [Claude Code](https://claude.ai/code) or [Codex](https://github.com/anthropics/claude-code) CLI

### Installation

```bash
# Clone the skill into your Codex skills directory
git clone https://github.com/b1uelake/question-router.git ~/.codex/skills/question-router
```

The skill activates automatically when you ask broad, vague, complex, learning, analysis, decision, planning, risk, or technical questions.

### Running Validation

```bash
cd ~/.codex/skills/question-router
python3 scripts/validate_skill.py
```

### Running Eval Suite

```bash
# Requires promptfoo: npm install -g promptfoo
bash scripts/run_evals.sh
```

## Design Principles

- **Don't guess when you can ask.** Missing context that materially changes the answer triggers clarification (1–3 questions, never more than 5).
- **Don't clarify when you can assume.** If a safe default handles the ambiguity, state it and proceed.
- **Structure scales with complexity.** Simple beginner questions get compact mode; high-stakes decisions get the full nine-part structure.
- **Separate facts from inference from advice.** The reader should always know which is which.
- **Every recommendation needs criteria.** "Choose X" without "because Y under condition Z" is incomplete.
- **Mark verification needs.** Legal, compliance, pricing, and source-dependent claims must be flagged for verification.

## License

MIT
