# Me & AI

A personal collection of skills, plugins, tools, and workflows I create through collaboration with AI.

This repository documents both the things I build and the practices I develop along the way: experiments, reusable methods, and lessons learned. It is maintained by Ali Boussecsou.

Some projects are ready to use; others are exploratory. Each project should document its purpose, requirements, usage, and limitations. Inclusion here does not imply support for every AI platform.

## Catalogue

| Project | Type | Purpose | Status |
| --- | --- | --- | --- |
| [Quiz Forge](agent-skills/learning/quiz-forge/README.md) | Agent skill | Generate source-grounded learning quizzes with feedback and a mechanical quality checker | Available; sample validation automated |

## Explore the repository

- [`agent-skills/`](agent-skills/): reusable instructions, reference material, and supporting scripts for AI agents.
- Future plugins, tools, workflows, and experiments will have their own directories as they are added.
- Methods and lessons learned can be documented alongside the projects that inspired them.

Only directories containing actual work are created. The repository is a collection, so each project has its own setup instructions rather than one shared application runtime.

## Get started

1. Choose a project from the catalogue and read its README.
2. Check its requirements, permissions, and limitations before using it.
3. Follow its instructions to use the sources or packaged artifact.

For Quiz Forge, the sources are readable in [`agent-skills/learning/quiz-forge/`](agent-skills/learning/quiz-forge/), and the distributable is [`quiz-forge.skill`](agent-skills/learning/quiz-forge.skill).

## Validation

Python 3.12 is used in CI. The current checks require only the Python standard library:

```sh
python3 scripts/validate_skills.py
```

This checks skill archive integrity, correspondence between packaged files and checked-in sources, and the bundled quiz example with its quality checker. It also verifies that the checker rejects duplicate answer options. These checks do not establish the factual or pedagogical quality of generated quizzes.

## Contribute and use safely

See [CONTRIBUTING.md](CONTRIBUTING.md) for project documentation and validation expectations, and [SECURITY.md](SECURITY.md) for handling sensitive information and reporting vulnerabilities.

AI-assisted output should be reviewed before use or publication. Do not commit credentials, private conversations, or source material you do not have permission to redistribute.

## License

Original content in this repository is available under the [MIT License](LICENSE), unless a file explicitly states otherwise. Preserve license notices when reusing it. Third-party material retains its own license and attribution requirements.
