---
name: make-it-click
description: Explains a concept, mechanism, or idea so a specific person understands it, remembers it, and can pass it on, adapting depth, order, and imagery to that person and the moment. Use when someone wants to understand how or why something works or how two ideas differ, asks for the intuition behind something, says they don't get it, wants a simpler, ELI5, or more intuitive version or an analogy, or needs help explaining an idea to someone else (team, boss, clients, students, a child). Also covers rewriting jargon-heavy text so non-experts understand it, and the explanation inside lessons, onboarding docs, and briefs. Not for quick fact lookups, debugging, plain summaries, quiz generation, or coaching on delivering a talk (voice, slides, rehearsal).
---

# Make It Click

## Why this skill exists

Expertise works against explanation. In Elizabeth Newton's 1990 Stanford study, "tappers" drummed the rhythm of well-known songs on a table and predicted listeners would name half of them. Listeners named 3 out of 120. The tapper hears the melody in their head; the listener hears knocks on wood. This is the **curse of knowledge**: once you know something, you struggle to imagine not knowing it.

You are always the tapper. You know a lot about almost everything, so your natural failure is to play the whole melody: everything true, in the order you know it, in words the listener lacks. Everything below helps you hear the knocks the way the listener hears them.

An explanation succeeds when the listener understands, remembers what they need to, and can use or retell it. Judge it by what lands, not by what it contains.

## How to use this skill

Treat what follows as a toolkit you compose from, fresh for each person and each turn. A plain, direct answer that already lands for this person is the best answer: give it. Each metaphor, name, story, or check must earn its place by fixing a specific understanding or memory problem, because decoration costs attention. Choosing less is often the skill.

In this file, the **listener** is whoever receives the explanation; the **user** is the person you are talking to. They are often the same person, but not always.

For substantial work (a lesson, a doc, a hard concept, a second attempt after one failed, or helping the user explain to others), read [references/toolkit.md](references/toolkit.md) for each move in depth and [references/situations.md](references/situations.md) for worked examples.

## Read the listener

Build your picture mostly from evidence already in the session:

- **What they know**: their vocabulary, role, earlier messages, the way they phrased the question. "How does the KV cache interact with paged attention?" and "Why is ChatGPT slow sometimes?" start on different ground.
- **What they already believe**: many concepts come with a predictable wrong intuition. A wrong brick already in place matters more than an empty spot.
- **Why they ask**: to decide, to build, to pass an exam, to satisfy curiosity, or to explain it to someone else. The purpose decides what the core is.
- **Live signals**: pace and patience, whether they want to *do* the thing or *understand* it, how they reacted to your last answer, and what they got right in their own words. Re-read these every turn; the right shape can change mid-session.
- **Final audience**: when the user wants to explain something to *their* people, reason about those people, and help the user reach them.

When the level is truly unknown and a wrong guess would be costly, ask one short question. Otherwise, make a sensible assumption and adjust from the reply.

## Two shapes

Most explanations take one of two shapes:

- **Answer-first**: the core comes in the first lines, and the rest supports it. Use it when the listener asked a direct question or has little time. Their question is already the knowledge gap, so answer it.
- **Build-up**: lay the bricks, open a gap, and land the core at the top. Use it when attention isn't guaranteed (talks, docs people skim, learners who didn't choose the topic), or when the core makes no sense without its ground.

You can mix them: answer in one line, then build up for those who want more.

## The moves

- **Find the core.** Peel the onion: ask *if they keep only one thing, what should it be?* Write it as one plain sentence a newcomer could repeat. If the concept truly has two or three parts, say how they connect. The outer layers (history, trivia, edge cases, detail that reassures you) wait for a follow-up.
- **Clear wrong bricks.** When a common misconception exists, bring it out (ask for a prediction, or say "most people picture X"), show where it fails on a concrete case, then lay the right brick in its place. If the listener offers their own version, start from it: confirm what is right and fix the specific part that is wrong.
- **Build the tower.** Work backwards from the core: what must they already hold? Keep the minimum, skip what this person already has, and order the rest so nothing rests on a brick not yet laid. Give each brick an **anchor**, something concrete that makes it understandable now: an example, a familiar comparison, a case from their world.
- **Open a gap.** Curiosity makes the listener want the answer. A gap pulls only when they know enough to feel it, so use a light hook to start, and open the real gap once the first bricks let them make a prediction.
- **Wrap the core.** Understanding fades; a shape stays. Give the core a **wrapper** that makes it memorable later: a story, a metaphor, a name, a rule, an equation, a diagram. Pick it from the concept's own shape, and check that it is true at the precision it implies. One wrapper is usually enough. A metaphor can serve as an anchor or as a wrapper; know which job you are giving it.
- **Name it.** When a term is new to them, give the idea first and the name after, so the name labels something they already hold. When they used the term themselves, use it from the start.
- **Show it.** A worked number, a five-line code trace, a before-and-after table, or a small diagram often explains faster than words, especially for technical listeners. Pair it with one sentence saying what to notice.
- **Check the landing.** For a short answer, one glance: is the core there, and is every term familiar or defined? For a long piece, reread it as the listener and look for the knocks: undefined terms, skipped steps, "obviously", references to things not yet introduced. In conversation, test understanding with a quick application or a request to put it in their own words, because "does that make sense?" almost always gets a yes.

## Shape of the concept

| Concept type | What usually carries understanding |
| --- | --- |
| Procedure | The goal first, one worked example on a real case, then the steps |
| Mechanism | A cause-and-effect chain in prose, a structural metaphor, a diagram |
| Abstract or formal | A definition, a small worked instance, a second representation, why it is defined that way; metaphors used sparingly, with their limits stated |
| Category | Two or three varied examples and one near-miss non-example |
| Comparison | The dimension that separates them, then a table |
| Contested or uncertain | What is established, where experts disagree and why, what would settle it |

## Shape of the situation

| Situation | What usually leads |
| --- | --- |
| Direct question in chat | Answer-first: the core, one anchor, more only if there is a meaningful next layer |
| "I still don't get it" | A change of angle rather than of volume: a new anchor, a concrete case, a smaller first brick |
| A child or a complete newcomer | Concrete experiences from their world, one vivid metaphor kept throughout, very small bricks |
| An expert from a nearby field | Map onto their field, skip the basics, be precise about the differences and where the analogy breaks |
| Decision-maker | The core as a decision-relevant claim up front, one wrapper they can repeat, the details on request |
| Lesson, onboarding doc, or talk | Build-up: a hook, the bricks, the real gap, the name, the core, a way to apply it |
| Multi-turn teaching | One brick per turn; they use the last brick before you lay the next |
| Rewriting jargon-heavy text | Find the text's buried core, rebuild around it, keep every claim true |
| Helping the user explain to others | A usable draft for their audience, built around a stated core, with one-line alternatives |

## Keep it true

Simplify without falsifying: simplifying leaves things out; falsifying puts wrong things in. When precision matters, flag the simplification ("roughly", "in most cases"). Keep surprises honest. Gilbert's talk says lottery winners and paraplegics end up equally happy; in Brickman's 1978 study, accident victims were less happy than controls, though still above the scale's midpoint, and lottery winners were no happier than controls. The honest version still surprises, and it usually does. A sticky wrapper spreads errors as efficiently as truths.

## Style

- Keep technical terms in their original form (often English) when they are the precise word practitioners use, and define them on first use when the listener may not know them.
- Prefer concrete verbs (show, cut, build, test) over abstract nouns (utilization, implementation). Let sentences flow into each other: short is good, choppy is not.
- Use prose for reasoning, since a chain of *because* and *so* breaks when you chop it into bullets.
- Borrow the listener's world: their domain, their examples, their own words from earlier in the session. When you answer in another language, choose metaphors native to that culture rather than translating English idioms.
