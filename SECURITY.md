# Security Policy

- Always run `python3 .claude/hooks/pre_commit_secret_check.py .` before pushing changes.
- Keep `mcp_config.example.json` strictly parameterized with `${ENV_VAR}` placeholders; store live credentials in gitignored `.mcp.json` or `.env`.
- Report issues via [Golden Nodalix Studio on LinkedIn](https://www.linkedin.com/in/agency-golden-nodalix-880598438/).
