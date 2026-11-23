#!/usr/bin/env bash
set -euo pipefail

# Wrapper to invoke Codex CLI (v0.171+) with gpt-6.2-astra at reasoning_effort=max
CODEX_BIN="/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex"
WORKDIR="/Users/mw/Desktop/math/remath"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <log_slug> <prompt_file> [sandbox_mode=workspace-write]"
  exit 1
fi

SLUG="$1"
PROMPT_FILE="$2"
SANDBOX="${3:-workspace-write}"
OUT_FILE="${WORKDIR}/codex_logs/${SLUG}_output.md"
META_FILE="${WORKDIR}/codex_logs/${SLUG}_stdout.log"

cp "$PROMPT_FILE" "${WORKDIR}/codex_logs/${SLUG}_prompt.md"

"$CODEX_BIN" exec \
  -m gpt-6.2-astra \
  -c model_reasoning_effort="max" \
  -c mcp_servers.node_repl.enabled=false \
  -c mcp_servers.golmok.enabled=false \
  -C "$WORKDIR" \
  -s "$SANDBOX" \
  -o "$OUT_FILE" \
  - < "$PROMPT_FILE" > "$META_FILE" 2>&1

echo "Completed: $OUT_FILE (log: $META_FILE)"
