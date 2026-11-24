# /pre-deploy-audit

Execute release readiness gate prior to merging to `main`:
1. Run `python3 .claude/hooks/pre_commit_secret_check.py .` to block accidental secret commits.
2. Run all unit tests and linters (`unittest` / `npm test`).
3. Confirm `.env.example` contains placeholder values matching every newly introduced env variable.
