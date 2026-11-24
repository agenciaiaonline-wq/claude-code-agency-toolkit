#!/usr/bin/env bash
# Install Claude Code Agency Toolkit (.claude/) into any target workspace safely
set -euo pipefail

TARGET_PROJECT="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

mkdir -p "$TARGET_PROJECT/.claude"
cp -R "$REPO_ROOT/.claude/agents" "$TARGET_PROJECT/.claude/"
cp -R "$REPO_ROOT/.claude/skills" "$TARGET_PROJECT/.claude/"
cp -R "$REPO_ROOT/.claude/commands" "$TARGET_PROJECT/.claude/"
cp -R "$REPO_ROOT/.claude/rules" "$TARGET_PROJECT/.claude/"
cp -R "$REPO_ROOT/.claude/hooks" "$TARGET_PROJECT/.claude/"

if [ ! -f "$TARGET_PROJECT/.mcp.json" ]; then
  cp "$REPO_ROOT/mcp_config.example.json" "$TARGET_PROJECT/.mcp.json"
  echo "[OK] Created sanitized $TARGET_PROJECT/.mcp.json template."
fi

echo "[OK] Installed Golden Nodalix Claude Code toolkit into $TARGET_PROJECT/.claude"
