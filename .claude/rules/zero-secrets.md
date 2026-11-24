# Zero Secrets in Repositories

- Never hardcode live API keys, JWTs, OAuth client secrets, webhook tokens, or private infrastructure IPs.
- Always track `.env.example` with clearly synthetic placeholders and keep `.env` in `.gitignore`.
- Run secret scanning hooks automatically prior to commits and CI builds.
