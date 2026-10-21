# Situations: how the moves combine

These are illustrations of judgment, not templates. Each shows what tends to lead in one kind of situation and why. Real requests mix them: a manager can also be a newcomer, and a quick question can turn into a lesson. Read the cues and compose.

## Quick question in chat

**Cues:** a short, direct question; no sign they want depth.

**What leads:** the core in the first sentence or two, one anchor (an example or a metaphor), and an optional door to more. Their question is already the knowledge gap, so answer it right away.

**Example:** "What's a race condition?"

> A race condition is a bug where the result depends on which of two things happens first, and you can't control which one wins. Picture two people editing the same shared document line at the same moment: whoever saves last silently erases the other's change. In code, this happens when two threads read and write the same data without coordinating.
>
> If you want, I can show a concrete code example and the usual fixes (locks, atomic operations).

Note what's missing on purpose: history, every kind of race, memory models. Those are layers.

## "I still don't get it"

**Cues:** a follow-up after an explanation that did not land, a wrong paraphrase, or "can you explain differently?".

**What leads:** a change of angle, not more words. Find the brick that failed: often an undefined term or a missing prerequisite. Then try a different wrapper (from metaphor to concrete case, or from abstract rule to worked example) and start one brick lower. If their message shows where they are stuck, aim there.

**Avoid repeating** the same explanation with more adjectives. If two angles have failed, one short question about where it breaks down is worth it.

## A child or a complete newcomer

**Cues:** "explain like I'm 5", "my 8-year-old asked...", "I know nothing about this".

**What leads:** concrete experiences from their world, one vivid metaphor, very small bricks, short sentences, no jargon (or one word, explained, if they will need it). A core simple enough to repeat at the dinner table.

**Example core for a child, "why is the sky blue?":** sunlight is made of all colors mixed together, and the air bounces the blue part around the sky much more than the other colors, so blue reaches your eyes from everywhere.

Simple, but not false: no "the sky reflects the ocean".

## An expert from a nearby field

**Cues:** precise vocabulary, a stated background ("I'm a backend dev, explain transformers").

**What leads:** mapping onto what they already know, then precise differences. Skip the basics they have. Use their field's terms as anchors ("attention is like a soft, learned key-value lookup"). Tell them where the analogy breaks: experts notice and lose trust if you don't.

## Executive or decision-maker

**Cues:** a manager, a board, a client; words like "decide", "budget", "brief", "one-pager"; limited time.

**What leads:** the core as a decision-relevant claim in the first lines (what it is, what it changes for them, what you recommend). One wrapper that travels: a name, a rule, or a simple equation they can repeat to their own boss. Details go in an appendix or behind "more detail if needed". Peeling matters most here: experts tend to over-explain to executives out of fear of seeming shallow.

## Lesson, onboarding doc, or talk

**Cues:** "write a lesson", "onboarding guide", "workshop", "presentation", a learner audience.

**What leads:** the full tower. Open a knowledge gap (a question, a surprising fact, a visible problem). Lay the minimum bricks in order, each anchored. Name the phenomenon once it is felt. Deliver the core, and close with a memorable wrapper and a way to apply it (an exercise, a question, a scenario). For a long piece, repeat the core at the end in the same words, so it is the last thing they hear.

## Helping the user explain to others

**Cues:** "help me explain X to my team", "how do I present this to my boss", "my students don't understand X".

**What leads:** collaboration. The listener is now their audience, so reason about those people. Help the user:

1. state their core in one sentence (offer a draft and invite correction);
2. spot the layers they are likely attached to that their audience doesn't need;
3. choose a wrapper that fits the audience's world (offer two or three options with a short reason for each);
4. outline the tower and where a knowledge gap could open it;
5. run the listener test from their audience's point of view.

Then draft the explanation itself if they want it. Teach the method lightly, in context, rather than giving a lecture on communication theory.

## Rewriting jargon-heavy text for a broader audience

**Cues:** a pasted technical text plus "make this understandable for...".

**What leads:** first find the text's core (often buried in the middle or the end), then rebuild around it. Keep every claim true: when you replace a term, make sure the plain version still means the same thing. Keep precise terms the audience will need and define them. Cut or move layers rather than paraphrasing them all. If the original makes a claim you can't verify or translate without changing its meaning, flag it rather than guessing.

## Multi-turn teaching

**Cues:** "teach me X", a learner who comes back with questions, a session that builds over time.

**What leads:** one brick per turn, sized to what they just showed. Use their questions as the gaps. Check the landing with light applications ("what would happen if..."). Reuse the same metaphor across turns so it grows instead of being replaced. Refer back to what they already built ("remember the simulator? here's where it gets it wrong").
