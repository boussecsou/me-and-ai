# Quiz Forge

An agent skill for generating source-grounded learning quizzes with plausible distractors, per-option feedback, and a mix of cognitive difficulty levels.

## Status and requirements

The skill is available as readable sources and as [`../quiz-forge.skill`](../quiz-forge.skill), a ZIP package. Import compatibility depends on your AI platform; this repository does not provide a universal installer.

The supporting checker requires Python 3 and uses only the standard library. No API key, network connection, or third-party Python dependency is needed to run it. Generating a quiz requires an AI agent and source material; any service credentials are managed by that platform.

## Use the skill

Read [SKILL.md](SKILL.md) for the complete instructions. Supply the agent with source material and specify the intended audience and quiz requirements. Use the reference documents to review item writing, cognitive levels, and quality. For PDFs, the skill expects a suitable PDF-reading capability in the agent's environment; none is bundled here.

The default JSON structure is illustrated in [assets/example-quiz.json](assets/example-quiz.json).

From the repository root, check the bundled example:

```sh
python3 agent-skills/learning/quiz-forge/scripts/qa_check.py \
  agent-skills/learning/quiz-forge/assets/example-quiz.json
```

To check your own quiz, replace the final path with your JSON file. Exit code `0` means no mechanical issue was found; exit code `1` means issues were detected or invocation failed. Invalid JSON or file errors also terminate unsuccessfully.

## Permissions and limitations

The checker reads the supplied JSON file and reports issues to standard output. It does not write files or contact external services.

It checks answer counts, duplicate options, selected forbidden phrases, answer-length imbalance, answer keys, and the presence of explanations, source references, and Bloom levels. It does not verify that answers are true, that source references are accurate, or that distractors and difficulty are appropriate. Human review remains necessary.

Only share source material you are authorized to use. Generated quizzes may contain mistakes and should be reviewed before assessment or publication.

## Development and license

Sources correspond to the packaged skill; this README is repository documentation and is not part of the package. See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for validation and packaging expectations. Original repository content uses the [MIT License](../../../LICENSE).
