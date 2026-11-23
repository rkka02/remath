#!/usr/bin/env bash
set -euo pipefail

# Wrapper to invoke bundled Codex CLI (v0.171+) with gpt-6.2-astra at reasoning_effort=max,
# cleanly scoped to a study under studies/<study_slug>/.
CODEX_BIN="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <study_slug> <task_slug> <prompt_file> [sandbox_mode=workspace-write]"
  echo "Example: $0 02-next-topic phase1_scouting studies/02-next-topic/codex_logs/phase1_prompt_src.md workspace-write"
  exit 1
fi

STUDY_SLUG="$1"
TASK_SLUG="$2"
PROMPT_FILE="$3"
SANDBOX="${4:-workspace-write}"

STUDY_DIR="${REPO_ROOT}/studies/${STUDY_SLUG}"
LOG_DIR="${STUDY_DIR}/codex_logs"

if [ ! -d "$STUDY_DIR" ]; then
  echo "Error: study directory does not exist: $STUDY_DIR"
  echo "Run: python3 scripts/new_study.py ${STUDY_SLUG} \"Short Title\""
  exit 1
fi

mkdir -p "$LOG_DIR"
OUT_FILE="${LOG_DIR}/${TASK_SLUG}_output.md"
META_FILE="${LOG_DIR}/${TASK_SLUG}_stdout.log"

if [ "$(realpath "$PROMPT_FILE")" != "$(realpath -m "${LOG_DIR}/${TASK_SLUG}_prompt.md" 2>/dev/null || echo "")" ]; then
  cp "$PROMPT_FILE" "${LOG_DIR}/${TASK_SLUG}_prompt.md"
fi

"$CODEX_BIN" exec \
  -m gpt-6.2-astra \
  -c model_reasoning_effort="max" \
  -c mcp_servers.node_repl.enabled=false \
  -c mcp_servers.golmok.enabled=false \
  -C "$STUDY_DIR" \
  -s "$SANDBOX" \
  -o "$OUT_FILE" \
  - < "$PROMPT_FILE" > "$META_FILE" 2>&1

echo "Completed: $OUT_FILE (log: $META_FILE)"
