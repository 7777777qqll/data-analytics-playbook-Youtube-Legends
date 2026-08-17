# Contributing

Thanks for improving this skill.

## Guidelines

- Keep `SKILL.md` concise and focused on instructions Codex needs at runtime.
- Prefer Chinese-facing output conventions for data deliverables unless a user explicitly requests another language.
- Preserve identifiers such as IDs, account handles, URLs, order numbers, SKUs, formulas, and system fields exactly.
- Add examples only when they clarify behavior or prevent common mistakes.
- Run validation before opening a pull request:

```bash
python scripts/validate_skill.py .
```

## Pull Request Checklist

- [ ] `SKILL.md` frontmatter has valid `name` and `description`.
- [ ] New guidance is actionable and not duplicated elsewhere.
- [ ] Chinese output rules remain intact.
- [ ] Validation passes locally.
