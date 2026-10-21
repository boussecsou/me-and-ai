---
name: make-it-click
description: Explains any concept, mechanism, or idea so a specific person understands it, remembers it, and can pass it on, adapting depth, order, and imagery to that person and the moment instead of following a fixed template. Use this skill whenever someone asks what something is or how it works, says they don't get something, asks for a simpler, ELI5, or more intuitive version, wants an analogy or metaphor, or needs help explaining an idea to someone else (team, manager, clients, students, children). This includes rewriting jargon-heavy text for non-experts, onboarding docs, lessons, and executive briefs, even if the word "explain" never appears. Built on the curse of knowledge, the core-and-wrapper (onion and chocolate) method, the tower of knowledge, and the knowledge gap.
---

# Make It Click

## Why this skill exists

Expertise works against explanation. In Elizabeth Newton's 1990 Stanford study, "tappers" drummed the rhythm of a well-known song such as *Happy Birthday* on a table. They predicted listeners would name the song half the time. Listeners named it 2.5% of the time. The tapper hears the melody in their head; the listener hears knocks on wood. This is the **curse of knowledge**: once you know something, you struggle to imagine not knowing it.

You are always the tapper. You know a lot about almost everything, so your natural failure is to play the whole melody: everything true, in the order you know it, in vocabulary the reader lacks. Each idea below helps you hear the knocks the way the listener hears them.

The goal is that the person understands, remembers, and can reuse or retell the idea. Judge an explanation by what lands, not by what it contains.

## How to use this skill

This is a toolkit, not a procedure. Read the situation, pick the few moves that serve it, and compose them. A quick question may need only a core and one anchor. A full lesson may use every move. Choosing less is often the skill.

Details, examples, and the source cases for each move live in [references/toolkit.md](references/toolkit.md). Illustrations of how different situations combine the moves live in [references/situations.md](references/situations.md). Read them when the explanation is substantial (a lesson, a doc, a talk, a hard concept, or a second attempt after a first one failed); a short chat answer rarely needs them.

## 1. Read the situation

Before you write, build a quick picture of the listener. Take it mostly from evidence already in the session rather than from questions:

- **Who they are and what they already know.** Their vocabulary, earlier messages, role, and phrasing tell you a lot. "How does the KV cache interact with paged attention?" and "Why is ChatGPT slow sometimes?" call for different starting bricks.
- **Why they ask.** Will they decide something, build something, pass an exam, satisfy curiosity, or explain it to someone else? The purpose decides what the core is.
- **Where they are stuck.** If they say what confuses them, aim straight at it. If an earlier explanation in this session did not land, change the angle (a new anchor, a new order, a concrete case) rather than the volume.
- **Medium and size.** A chat reply, a doc, a slide, a script, a bedtime answer for a child. Match the length to the question: a one-line question deserves a short answer with a door to more.
- **Final audience.** Sometimes you explain to the user. Sometimes you help the user explain to *their* audience. In that case, the listener is their audience: reason about those people, and help the user build the explanation rather than just explaining the topic to them.

When the level is truly unknown and a wrong guess would be costly, ask one short question. Otherwise, make a sensible assumption, mention it in passing if useful, and offer to go simpler or deeper.

## 2. The moves

These are the leading ideas. Each one is a lens, not a mandatory step.

- **Find the core (peel the onion).** Ask: *if they remember only one thing, what should it be?* Write that as one plain sentence a newcomer could repeat. Peel away the layers that serve you more than them: history, trivia, edge cases, implementation detail, unexplained jargon. A storyteller who opens with "It was 2003, or maybe 2004, the year Facebook launched, I had white sneakers on..." buries the only thing that matters: *I saw Barack Obama backflip off a bridge.* Peeling stings because the layers feel important to you. Keep what the core needs; the rest can wait for a follow-up.

- **Wrap the core (the chocolate).** Understanding something and remembering it are different. Give the core a shape the mind holds on to: a story, a metaphor, a name, a rule, an equation, a diagram, a demonstration, a slogan, a short set of rules. Choose the wrapper from the shape of the concept: a process suits a rule or steps, a relationship between factors suits an equation or diagram, a counterintuitive behavior suits a story or demonstration, an invisible mechanism suits a metaphor. Mel Robbins turned "interrupt hesitation with immediate physical action" into the 5-Second Rule: you don't need behavioral psychology, you just count down.

- **Build the tower.** Order the bricks so each one rests on the one below. Find the minimum set of prerequisites the core depends on and lay those first, each with a concrete anchor. Go from concrete to abstract, from example to definition, from familiar to new. A brick that refers to something not yet laid is where readers fall off.

- **Open a knowledge gap.** Curiosity opens the mind. Pose the puzzle, the prediction, or the paradox before the answer, so the explanation arrives as relief instead of noise. Dan Gilbert asks his audience to compare winning the lottery with becoming paraplegic, then shows that a year later the two groups are far closer in happiness than anyone predicts. Only then does he name the cause. Use a gap when attention is not guaranteed (talks, docs people skim, learners who did not choose the topic). When the user has just asked a direct question, their question is already the gap: answer it.

- **Anchor with metaphors and examples.** A good metaphor maps the structure of something known onto something unknown: Gilbert's prefrontal cortex as a *flight simulator* that lets you test experiences before you live them. Pick metaphors whose working parts match the concept, not just its surface. Say where the metaphor breaks when the break could mislead. Pair it with a concrete example (no one needs to taste liver-and-onion ice cream to know it is bad), and use a non-example to show the edges.

- **Name it.** A name turns a vague idea into a handle people can pick up, reuse, and trust: *impact bias*, *psychological immune system*. Introduce the technical term after the idea is in the reader's head, so the term labels something they already hold.

- **Check the landing.** Read your draft as the listener. Look for the knocks: undefined terms, skipped steps, "obviously", "simply", references to things not yet introduced. In a live conversation, a short check ("Does this fit how you pictured it?") or a quick application ("So what would happen if...?") tells you whether the tower stands.

## 3. Compose for the moment

Let the situation decide which moves lead. Some typical shifts:

| Situation | What usually leads |
| --- | --- |
| Quick question in chat | The core first, one anchor, an optional door to more |
| "I still don't get it" | A new angle: a different metaphor, a concrete case, a smaller first brick |
| A child or a complete newcomer | Concrete examples, one vivid metaphor, very small bricks, no jargon |
| An expert from a nearby field | Map onto what they already know; skip the basics; be precise about the differences |
| Executive or decision-maker | The core as a decision-relevant claim in the first lines; one wrapper; details in an appendix |
| Lesson, onboarding doc, or talk | The full tower, with a knowledge gap to open and a memorable wrapper to close |
| Helping the user explain to others | Work with them: find their core, suggest wrappers, outline the tower for their audience |

These are tendencies, not rules. [references/situations.md](references/situations.md) walks through each one with short examples.

## 4. Keep it true

Simplify without falsifying. Simplifying leaves things out; falsifying puts wrong things in. When precision matters, signal the simplification ("roughly", "in most cases", "the full picture adds X"). Keep surprising claims honest: even Gilbert's lottery example rounds up the research. In Brickman's 1978 study, accident victims were less happy than controls, just far happier than people expected. The surprise survives the honest version, and it usually does. When you are unsure of a fact, say so instead of smoothing it over.

## 5. Language and style

- Answer in the language the user is working in. Keep technical terms in their original form (often English) when that is the precise word practitioners use, and define them at first use if the reader may not know them.
- Use simple, direct verbs and short sentences. Put one idea in each paragraph.
- Lead with the core and expand after it.
- Use formatting to show structure: lists for parallel items, prose for reasoning, since a chain of *because* and *so* breaks when it is chopped into bullets. Use a diagram or table when the concept is spatial or comparative.
- Borrow the reader's world: their domain, their examples, their own words from earlier in the session.

## 6. The listener test

Before you send, run a quick pass:

- Can you state the core in one sentence, and does it appear early?
- Could the reader repeat the idea to someone else tomorrow?
- Is every term either familiar to this reader or defined?
- Does each brick rest only on bricks already laid?
- Does anything serve your completeness more than their understanding? Cut it, or move it to an "if you want to go further" line.
- Is it still true?
