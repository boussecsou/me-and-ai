# Make It Click

An agent skill for explaining any concept so a specific audience understands it, remembers it, and can pass it on. It adapts to the person, the purpose, and the moment instead of imposing a fixed template.

## Status and requirements

Available as readable sources and as [`../make-it-click.skill`](../make-it-click.skill), a ZIP package. Import compatibility depends on your AI platform; this repository does not provide a universal installer.

The skill contains instructions only: no scripts, API keys, network access, or dependencies.

## What it does

The skill gives the agent a toolkit of moves and the judgment to pick among them:

- **Find the core** (peel the onion): the one idea the listener should keep.
- **Clear wrong bricks**: surface and fix a common misconception instead of building over it.
- **Build the tower**: lay the minimum prerequisites in dependency order, each with a concrete anchor.
- **Open a gap**: create curiosity once the listener knows enough to feel it.
- **Wrap the core** (the chocolate): a story, metaphor, name, rule, equation, or diagram that makes it stick, true at the precision it implies.
- **Name it**, **show it** (traces, worked numbers, tables, diagrams), and **check the landing** with application rather than "does that make sense?".

It reads the listener from the session (what they know and believe, why they ask, live signals, the final audience), picks an answer-first or build-up shape, and adapts to the type of concept (procedure, mechanism, formal idea, category, comparison, contested topic). A plain direct answer stays plain when it already lands.

## Use the skill

Read [SKILL.md](SKILL.md) for the instructions. The references hold the detail:

- [references/toolkit.md](references/toolkit.md): each move in depth, with the source cases.
- [references/situations.md](references/situations.md): how the moves combine in typical situations.

Example requests:

- "I've watched ten videos on blockchain and still don't get it. I'm an accountant."
- "Help me explain technical debt to our board in five minutes."
- "My 7-year-old asked how the internet works. What do I say?"

The instructions are written in English. The skill answers in the user's language and keeps technical terms in their original form when that is the precise word.

## Limitations

The skill shapes how an explanation is built; it doesn't verify facts. Explanations can still contain mistakes and should be reviewed before teaching or publication. There is no automated quality check for this skill.

## Background and attribution

The method synthesizes widely discussed ideas: the curse of knowledge (Camerer, Loewenstein, and Weber, 1989, crediting Robin Hogarth for the term) and Elizabeth Newton's 1990 tapper-listener study; the core-and-wrapper ("onion and chocolate") approach; the tower-of-knowledge and knowledge-gap structure, illustrated by Dan Gilbert's 2004 TED talk, "The surprising science of happiness"; and memorable wrappers such as Mel Robbins's 5-Second Rule and Alex Hormozi's Value Equation. Those ideas belong to their authors; the wording of this skill is original. It was written with AI assistance from the maintainer's personal study notes, which are not redistributed here.

## Development and license

Sources correspond to the packaged skill; this README is repository documentation and is not part of the package. See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for validation and packaging expectations. Original repository content uses the [MIT License](../../../LICENSE).
