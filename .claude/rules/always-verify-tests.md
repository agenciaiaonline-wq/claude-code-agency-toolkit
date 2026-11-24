# Always Verify With Executed Tests

- Never report a fix or feature as complete until tests run and pass after the final edit.
- Do not relax assertions or skip broken checks just to turn a pipeline green.
- Prefer fast, deterministic local tests without live external API dependencies in CI.
