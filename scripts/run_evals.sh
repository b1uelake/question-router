#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_PATH="${1:-/Users/chen/skill-test/promptfoo-tests/promptfooconfig.generated.yaml}"
OUTPUT_PATH="${2:-/Users/chen/skill-test/promptfoo-tests/results.generated.json}"
ENV_FILE="${3:-/Users/chen/skill-test/promptfoo-tests/.env}"

python3 "$SKILL_DIR/scripts/validate_skill.py"
python3 "$SKILL_DIR/scripts/build_promptfoo_config.py" --output "$CONFIG_PATH"

if ! command -v promptfoo >/dev/null 2>&1; then
  echo "promptfoo not found on PATH" >&2
  exit 1
fi

if [[ -f "$ENV_FILE" ]]; then
  promptfoo eval -c "$CONFIG_PATH" --max-concurrency 1 --no-cache --output "$OUTPUT_PATH" --env-file "$ENV_FILE"
else
  promptfoo eval -c "$CONFIG_PATH" --max-concurrency 1 --no-cache --output "$OUTPUT_PATH"
fi
