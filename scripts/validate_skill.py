#!/usr/bin/env python3
"""Validate the question-router skill structure and regression data."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


PROBLEM_TYPES = {"learning", "analysis", "decision", "plan", "risk", "technical"}
REFERENCE_FILES = {
    "learning": "references/learning.md",
    "analysis": "references/analysis.md",
    "decision": "references/decision.md",
    "plan": "references/plan.md",
    "risk": "references/risk.md",
    "technical": "references/technical.md",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_quick_validate(root: Path) -> None:
    candidates = [
        Path.home() / ".codex/skills/.system/skill-creator/scripts/quick_validate.py",
        Path("/Users/chen/.codex/skills/.system/skill-creator/scripts/quick_validate.py"),
    ]
    script = next((p for p in candidates if p.exists()), None)
    if script is None:
        ok("quick_validate.py not found; skipped official validator")
        return
    result = subprocess.run(
        [sys.executable, str(script), str(root)],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        fail("official quick_validate.py failed")
    ok("official quick_validate.py passed")


def require_files(root: Path) -> None:
    required = [
        "SKILL.md",
        "evals/evals.json",
        "schemas/eval-case.schema.json",
        "schemas/route.schema.json",
        "scripts/validate_skill.py",
        "scripts/build_promptfoo_config.py",
        "scripts/run_evals.sh",
        *REFERENCE_FILES.values(),
    ]
    missing = [path for path in required if not (root / path).is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")
    ok("required files present")


def validate_skill_md(root: Path) -> None:
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    if "name: question-router" not in text:
        fail("SKILL.md frontmatter missing name: question-router")
    for route, ref in REFERENCE_FILES.items():
        if ref not in text:
            fail(f"SKILL.md does not link {route} contract: {ref}")
    if "evals/evals.json" not in text:
        fail("SKILL.md does not link evals/evals.json")
    ok("SKILL.md links references and evals")


def validate_json_file(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is not valid JSON: {exc}")


def validate_schemas(root: Path) -> None:
    for rel in ["schemas/eval-case.schema.json", "schemas/route.schema.json"]:
        schema = validate_json_file(root / rel)
        if not isinstance(schema, dict):
            fail(f"{rel} must be a JSON object")
        for key in ["$schema", "title", "type"]:
            if key not in schema:
                fail(f"{rel} missing {key}")
    ok("schema files are valid JSON objects")


def validate_evals(root: Path) -> None:
    data = validate_json_file(root / "evals/evals.json")
    if not isinstance(data, list) or not data:
        fail("evals/evals.json must be a non-empty array")

    seen_ids: set[str] = set()
    id_pattern = re.compile(r"^[a-z0-9][a-z0-9-]*$")
    for idx, case in enumerate(data, start=1):
        if not isinstance(case, dict):
            fail(f"eval case {idx} is not an object")
        required = ["id", "question", "expectedType", "shouldClarify", "mustInclude", "mustAvoid", "notes"]
        missing = [key for key in required if key not in case]
        if missing:
            fail(f"eval case {idx} missing required fields: {', '.join(missing)}")
        case_id = case["id"]
        if not isinstance(case_id, str) or not id_pattern.match(case_id):
            fail(f"eval case {idx} has invalid id: {case_id!r}")
        if case_id in seen_ids:
            fail(f"duplicate eval case id: {case_id}")
        seen_ids.add(case_id)
        if case["expectedType"] not in PROBLEM_TYPES:
            fail(f"{case_id} has invalid expectedType: {case['expectedType']!r}")
        if "secondaryType" in case and case["secondaryType"] not in PROBLEM_TYPES:
            fail(f"{case_id} has invalid secondaryType: {case['secondaryType']!r}")
        if not isinstance(case["question"], str) or not case["question"].strip():
            fail(f"{case_id} question must be a non-empty string")
        if not isinstance(case["shouldClarify"], bool):
            fail(f"{case_id} shouldClarify must be boolean")
        for key in ["mustInclude", "mustAvoid"]:
            if not isinstance(case[key], list) or not all(isinstance(x, str) and x for x in case[key]):
                fail(f"{case_id} {key} must be an array of non-empty strings")
        if not isinstance(case["notes"], str) or not case["notes"].strip():
            fail(f"{case_id} notes must be a non-empty string")
    ok(f"eval cases valid: {len(data)}")


def validate_references(root: Path) -> None:
    for route, rel in REFERENCE_FILES.items():
        text = (root / rel).read_text(encoding="utf-8")
        title = f"# {route.capitalize()}"
        if not text.lstrip().startswith(title):
            fail(f"{rel} should start with {title}")
        for heading in ["## Classify", "## Ask First", "## Answer Contract", "## Quality Rules", "## Example Routes"]:
            if heading not in text:
                fail(f"{rel} missing section starting with {heading}")
    ok("reference contracts have required sections")


def main() -> None:
    root = skill_root()
    require_files(root)
    run_quick_validate(root)
    validate_skill_md(root)
    validate_schemas(root)
    validate_evals(root)
    validate_references(root)
    ok(f"question-router skill validated at {root}")


if __name__ == "__main__":
    main()
