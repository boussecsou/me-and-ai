# Situations: worked examples

These examples show judgment at work. Each notes which moves were chosen, which were skipped, and why. Real requests mix situations: read the cues and compose.

## Direct question, technical listener

"What's a race condition?" from someone writing code.

> A race condition is a bug where the result depends on which of two operations happens first, and you don't control which one wins. Classic case: two threads both increment a counter that holds 5.
>
> ```
> T1 reads 5 → T2 reads 5 → T1 writes 6 → T2 writes 6
> ```
>
> Two increments ran, the counter says 6: one update was lost, because each thread read the value before the other wrote it back. The usual fixes make the read-and-write happen as one step: a lock around it, or an atomic increment.

**Chosen**: answer-first, the core in sentence one, a trace as the anchor (for a developer, it beats a metaphor), the fix because a coder will want it next. **Skipped**: history, types of races, memory models. The term was used straight away because the listener typed it.

## Medium explanation, newcomer

"Why does everyone say to start saving early? A few years can't make that much difference."

> It makes a huge difference, because your money earns returns, and then those returns earn returns of their own. That snowball is called compound interest.
>
> Picture two people who each invest €200 a month at 7% a year. Ana starts at 25 and stops at 35: ten years, €24,000 put in. Ben starts at 35 and keeps going until 65: thirty years, €72,000 put in. At 65, Ana has about €281,000 and Ben about €244,000. She put in a third as much and still ends up ahead, because her money had ten extra years to snowball.
>
> The lesson: in saving, time does more of the work than the amount does.

**Chosen**: answer-first, because the question contains a wrong brick ("a few years can't matter"). The worked numbers make that brick fail on a case the listener can check. The name comes after the image. The wrapper is the snowball, plus a one-line rule they can repeat. **Skipped**: the formula, inflation, taxes. They are true, but they aren't what this listener needs right now.

## A child

"Why is the sky blue?" from an 8-year-old.

Core: sunlight is all the colors mixed together, and the air bounces the blue part around the sky much more than the others, so blue reaches your eyes from everywhere.

**Chosen**: simple, but not false: no "the sky reflects the ocean". Use one image throughout (light bouncing like balls off the bits of air), and a quick thing to try: look at the sky near the sun at sunset, when the light crosses so much air that the blue has been bounced away.

## A misconception

"So evolution means animals try to adapt to their environment?"

Start from their version: they are right that species change to fit their environment. Then fix the specific wrong brick, which is *try*. Make it fail on a concrete case: giraffes didn't stretch their necks and pass on the stretch. In each generation, giraffes that happened to be born with slightly longer necks reached more food and had more offspring. Then lay the right brick: variation happens at random, and the environment filters it. No one is trying. **Skipped**: genetics and drift, until the filter idea is solid.

## "I still don't get it"

After an explanation that didn't land, find which brick failed (often an undefined term or a missing prerequisite), and change the angle: from metaphor to a concrete case, from rule to worked example, or one brick lower. Repeating the same explanation with more words rarely helps. After two failed angles, one short question about where it stops making sense is worth asking. If their earlier messages show what they got right, build from there.

## Multi-turn teaching

Lay one brick per turn, sized to what they just showed. Before the next brick, have them use the last one: predict, apply, or restate it. Their questions are your gaps. Reuse the same metaphor across turns so it grows instead of being replaced ("remember the simulator? here is where it gets things wrong"). If they are studying for an exam, favor a clean, retrievable structure and accuracy over a clever wrapper.

## Rewriting jargon-heavy text

Find the text's core first: it is often buried in the middle or at the end. Then rebuild around it. When you replace a term, check that the plain version still means the same thing. Keep the precise terms the audience will need, and define them. Cut or move layers rather than paraphrasing all of them. If a claim can't be translated without changing its meaning, flag it rather than guessing.

## Helping the user explain to others

"Help me explain technical debt to our board in five minutes."

Most users want something usable now. Usually lead with a draft written for their audience, the one-sentence core it is built around, and one or two alternative wrappers in a line each (for example, deferred maintenance on a fleet, or an interest bill that grows). Say which layers you cut and why, so they can put them back. Choose anchors from the audience's world: for an ex-finance board, money and interest; for their customers' industry, its own vocabulary.

Leave placeholders for the user's own figures and facts rather than inventing them. Prepare the questions the audience is likely to ask. Go into a step-by-step build (core, layers, wrapper, tower) only when the user wants to construct it themselves or the draft misses.

Apply the method to your own reply too: the user is also a listener. Their core and their draft come first; the background is brief.
