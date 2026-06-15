---
name: question-router
description: Use this skill when the user wants a higher-quality answer to a broad, vague, complex, learning, analysis, decision, planning, risk, or technical question. Use when the user asks to classify the question type, avoid generic answers, clarify missing context first, choose an appropriate response structure, expose assumptions, separate facts from inference and advice, provide judgment criteria, counterexamples, verification needs, and prioritized next actions.
---

# Question Router

Use this skill to turn under-specified questions into well-framed answers. Classify the request, check context sufficiency, ask only necessary clarifying questions, load the relevant response contract, and validate the answer before finalizing.

## Core Workflow

1. Classify the request into one primary type:
   - `learning`: understand a concept, mechanism, field, prerequisite, or learning path.
   - `analysis`: break down a situation, cause, tradeoff, pattern, argument, comparison, or "why" question.
   - `decision`: choose among options or decide whether to act.
   - `plan`: design a sequence of actions, process, roadmap, study plan, or implementation approach.
   - `risk`: identify failure modes, uncertainty, downside, controls, compliance issues, or warning signs.
   - `technical`: implement, debug, architect, test, deploy, or operate a technical system.

2. Apply tiebreakers:
   - If the question starts with "why", classify as `analysis` unless it is clearly a definition.
   - If the question asks "should I", classify as `decision`.
   - If the question asks "what could go wrong", "is this safe", or names compliance/security/safety, classify as `risk`.
   - If the question asks "how do I build/implement/fix/debug/deploy", classify as `technical`.
   - If the question asks "how do I learn/plan/roadmap", classify as `plan`, often with `learning` as a secondary type.
   - If a specialized skill or tool is the better owner of domain execution, use that skill for execution and use this skill only for framing, clarification, answer structure, and validation.

3. Check context sufficiency:
   - user role and background
   - current understanding level
   - goal or decision to support
   - audience for the answer
   - constraints, time horizon, budget, tools, jurisdiction, or policy boundaries
   - quality standards, such as accuracy, depth, brevity, novelty, actionability, or verifiability
   - desired output format
   - evidence or verification needs

4. Decide whether to ask questions:
   - Ask only when missing information would materially change the answer.
   - Ask the fewest useful questions, normally 1-3 and never more than 5 in one turn.
   - For complex questions, allow a second clarification round if the user's answer reveals a new critical ambiguity.
   - Use a third clarification round only for high-stakes, user-specific, or materially ambiguous work.
   - If missing information can be handled with a safe assumption, state the assumption and proceed.
   - If the user explicitly says to ask before answering, do not provide the full answer until the key questions are answered.

5. When asking clarifying questions, include only:
   - Problem type.
   - One sentence explaining why context matters for this specific question.
   - The questions.

   Do not give a full answer after the questions.

6. Load the relevant response contract before answering:
   - `learning` -> read [references/learning.md](references/learning.md)
   - `analysis` -> read [references/analysis.md](references/analysis.md)
   - `decision` -> read [references/decision.md](references/decision.md)
   - `plan` -> read [references/plan.md](references/plan.md)
   - `risk` -> read [references/risk.md](references/risk.md)
   - `technical` -> read [references/technical.md](references/technical.md)

   If two types are materially needed, read both relevant files. Do not load unrelated reference files.

## Mandatory Output Rules

When providing a full answer, include these elements unless the user explicitly asks for a very short answer:

1. Problem type
2. Assumptions
3. Known facts
4. Reasonable inferences
5. Recommendations
6. Uncertainty or needs verification
7. Judgment standards
8. Counterexamples or failure cases
9. Prioritized next actions

For short answers, compress the same logic into fewer headings instead of dropping it entirely.

Use compact mode for simple beginner questions. Compact mode should normally include:

- Problem type
- Direct answer
- Why it matters or when to use it
- One example when helpful
- Next step

Do not force the full nine-part structure onto a question that can be answered well in a short response.

## Quality Gate

Before finalizing, check:

- The answer addresses the user's actual question rather than giving background.
- The response type matches the task type.
- The correct reference contract was loaded.
- Assumptions are explicit.
- Claims are separated from inferences and advice.
- Judgment criteria are present when the answer makes a recommendation or analysis.
- Failure cases or counterexamples are present when useful.
- Next actions are ordered and concrete.
- The response is no longer than the task requires.
- High-stakes, current, or source-dependent claims are marked for verification or backed by appropriate sources.

## Evaluation Set

Use [evals/evals.json](evals/evals.json) as the regression suite for this skill. When behavior changes, add or update cases there with:

- the user question
- expected primary type
- whether clarification should happen
- required concepts or sections
- wording or behavior to avoid

Do not treat passing evals as sufficient if real user examples reveal a better rule. Update the reference contract and eval case together.
