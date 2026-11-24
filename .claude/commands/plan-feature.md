# /plan-feature

Create a concise architectural specification before touching source files:
1. List affected modules, database migrations, and public API contract changes.
2. Invoke `architect-reviewer` to verify tenant isolation and idempotency.
3. Define exact automated tests that prove the new behavior passes cleanly.
