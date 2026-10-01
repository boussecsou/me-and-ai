# Contributing

This is a personal collection maintained by Ali Boussecsou. Suggestions and focused contributions are welcome through issues and pull requests. Discuss substantial additions before implementing them.

## Add or update a project

Place work in the relevant category, creating new category directories only when there is content to add. Give each project a README covering:

- Purpose and intended audience.
- Status: exploratory, available, or archived.
- Requirements, installation, and a concrete usage example.
- Permissions, external services, and credential requirements, if any.
- Known limitations and relevant validation commands.
- Attribution and licensing for any third-party material.

Add or update its entry in the root README catalogue. Include readable source files alongside distributable artifacts. Explain AI assistance when it helps reviewers understand the work; contributors remain responsible for checking correctness and redistribution rights.

## Skills and packaged artifacts

For Quiz Forge, edit sources under `agent-skills/learning/quiz-forge/`. The `.skill` file is a ZIP archive. Rebuild it from `agent-skills/learning/` with the `quiz-forge/` directory as its archive root. Include skill resources and scripts; exclude the repository-only README, caches, and temporary files. Keep every existing packaged file synchronized with its source.

Run from the repository root:

```sh
python3 scripts/validate_skills.py
```

Include the validation result and any limitations in your pull request. For changes to the checker, exercise both valid and invalid quiz input. Mechanical checks supplement human review of source grounding, explanations, and difficulty.

## Commit identity

Before committing, check `git config user.name` and `git config user.email`. Use a verified email address associated with your GitHub account, or your GitHub-provided `noreply` address, so contributions are attributed correctly. In shared environments, configure your identity with `git config --local` for this repository.

## Sensitive information

Do not submit API keys, tokens, passwords, private conversations, personal data, or confidential documents. Use synthetic or properly anonymized examples. Follow [SECURITY.md](SECURITY.md) for suspected vulnerabilities; do not disclose them in public issues.
