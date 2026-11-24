# CLAUDE.md (Drop-In Agency Project Template)

## 1. Engineering Discipline
- Plan architecture and tenant boundaries before editing source code.
- Never hardcode live tokens, database URLs, or personal PII in source files or tests.
- Re-run all affected unit tests and lint/typecheck gates after the final code edit.

## 2. Subagent Routing
- Invoke `architect-reviewer` before schema or API contract changes.
- Invoke `security-auditor` prior to exposing new routes, RLS rules, or Docker services.
- Invoke `qa-verifier` to collect exact command output before declaring completion.
