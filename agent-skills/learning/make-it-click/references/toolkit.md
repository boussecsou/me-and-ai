# Toolkit: the moves in depth

Each section expands one move from `SKILL.md`: what it is, why it works, how to do it, and how it goes wrong. The source cases (Newton, Gilbert, Robbins, Hormozi) are illustrations of the principle, not content to reuse.

## Contents

1. The curse of knowledge (the diagnosis)
2. Find the core (peel the onion)
3. Wrap the core (the chocolate)
4. Build the tower
5. Open a knowledge gap
6. Anchor with metaphors and examples
7. Name it
8. Check the landing

---

## 1. The curse of knowledge (the diagnosis)

**What it is.** Once you know something, you can't easily simulate the mind of someone who doesn't. Economists Camerer, Loewenstein, and Weber described the effect in 1989 and credited Robin Hogarth with the name.

**The evidence.** In Elizabeth Newton's 1990 Stanford experiment, tappers drummed 120 well-known songs. They predicted listeners would identify half. Listeners identified 3 (2.5%). The gap is the distance between the melody in the tapper's head and the knocks the listener actually hears.

**How it shows up in an explanation:**

- **Dumping instead of explaining.** Saying everything you know because it is all true and all feels relevant.
- **Burying the core.** The main idea arrives late, after context that only matters to you.
- **The illusion of clarity.** Assuming that because the logic is obvious to you, it is obvious to them: undefined terms, skipped steps, "as you know".

**The counter-move.** Before you write, deliberately picture the listener's starting point: what they have, what they lack, what they want. After you write, reread as that person.

## 2. Find the core (peel the onion)

**What it is.** The core is the single most important idea: compact, deep, and graspable by a newcomer. Everything else is a layer around it.

**Typical layers, from outside in:**

- Outer: history, chronology, anecdotes, metadata (the year, the weather, the sneakers).
- Middle: secondary metrics, conditions, implementation details.
- Inner: proofs, technical nuance, expert vocabulary.
- Core: the one claim, mechanism, or decision that matters.

**How to do it:**

1. List what you could say.
2. Ask the filter question: *if they remember only one thing, what should it be?* Shape the answer by the listener's purpose. "What is an index?" has a different core for a student (a sorted lookup structure) than for a product manager (it makes reads fast and writes slower).
3. Remove the layers the core does not need.
4. Write the core as one plain, self-contained sentence.

**A good core is:**

- **Single.** One proposition, not a list.
- **Deep.** It carries the real insight, not a platitude. "Databases store data" is too shallow; "an index trades write speed and space for read speed" has depth.
- **Graspable.** A newcomer can understand it without prerequisites, or with only the ones you will lay first.

**How it goes wrong.** Experts resist peeling because each layer took effort to learn and cutting feels like losing rigor or credibility. That resistance is the curse of knowledge speaking. Peeled layers aren't lost: they become follow-up material, an appendix, or a "going further" line.

## 3. Wrap the core (the chocolate)

**What it is.** A bare truth is easy to understand in the moment and easy to forget. A wrapper gives the core a form the mind is built to store and retell.

**Wrapper types and when they fit:**

| Wrapper | Fits when the concept is... | Example |
| --- | --- | --- |
| Story or anecdote | An event, a consequence, a human stake | The Obama bridge backflip |
| Metaphor or analogy | An invisible mechanism | The prefrontal cortex as a flight simulator |
| Name or label | A pattern people should recognize again | "Impact bias" |
| Rule or method | A behavior to adopt | The 5-Second Rule |
| Equation or model | A relationship between several factors | The Value Equation |
| Diagram | A structure, a flow, a hierarchy | Onion layers, a tower of bricks |
| Demonstration | A claim people would doubt if only told | Asking the audience to predict, then showing the data |
| Slogan | A principle that must travel through an organization | "Simplify, don't falsify" |
| Small set of rules | A practice with a few key constraints | "Core first, one anchor, one door" |

**Two cases:**

- **Mel Robbins.** Core: when you hesitate, interrupt the hesitation with immediate physical action before doubt builds up. Wrapper: the 5-Second Rule (count 5-4-3-2-1, then move). The countdown acts as a pattern interrupt. Users don't need to understand the psychology; they need to count.
- **Alex Hormozi.** Core: the perceived value of an offer depends on several interacting factors. Wrapper: the Value Equation, *value = (dream outcome × perceived likelihood) / (time delay × effort and sacrifice)*. It offloads a multi-factor analysis into a formula anyone can apply to their own offer.

**Tests for a good wrapper:**

- Could someone repeat it after hearing it once?
- Does it carry the core faithfully, or does it only decorate?
- Does it lighten the mental load (cognitive offloading) or break an automatic response (pattern interrupt)?

**How it goes wrong.** A clever wrapper that doesn't match the core's structure spreads a wrong idea efficiently. Also, one wrapper is usually enough. Three competing metaphors tend to cancel each other out.

## 4. Build the tower

**What it is.** Knowledge stacks like a tower: each new block must rest on one already in place. An explanation fails where a block hangs in the air.

**How to do it:**

1. Start from the core and work backwards: what must the listener already hold to understand it? Those are the bricks.
2. Keep the minimum set. Every extra brick is a chance to lose them.
3. Remove the bricks this listener already has. That is where reading the situation pays off.
4. Lay them in dependency order, each with a concrete anchor.
5. Place the core on top when the ground is ready.

**Gilbert's tower (TED, "The surprising science of happiness", 2004):**

1. Hook: in two million years, the human brain nearly tripled in mass. Why would nature want that?
2. Brick, the organ: much of the growth went into the frontal lobe, especially the prefrontal cortex.
3. Brick, the function: it is an *experience simulator*, like a pilot's flight simulator.
4. Anchor: there's no liver-and-onion ice cream, because you simulate the taste and reject it without tasting.
5. Gap: lottery winners versus paraplegics (see section 5).
6. Name: *impact bias*, our simulator's habit of overestimating how strong and how long an emotional impact will be.
7. Core: we *synthesize* happiness through a *psychological immune system*.

**Ordering heuristics:** concrete before abstract, example before definition, familiar before new, question before answer, whole before parts when the reader needs a map, parts before whole when the whole would make no sense yet.

**How it goes wrong.** Forward references ("we'll see why later") lose more readers than they promise. A tower that is too tall for the request is a lecture nobody asked for.

## 5. Open a knowledge gap

**What it is.** Curiosity is the feeling of a gap between what you know and what you want to know. Make the listener feel the gap and they will pull the explanation toward them.

**Ways to open one:**

- **Prediction then reveal.** Ask them to predict, then show the real result. Gilbert asks the audience to compare lottery winners and paraplegics, which flips their intuition.
- **Paradox.** Two things that both seem true and seem to contradict each other.
- **Surprising number.** A figure that clashes with expectations (2.5% versus 50%).
- **Open question.** "Why would nature give us such a costly brain?"
- **Visible problem.** Show the failure the concept solves before showing the concept.

**Then close it.** Name the phenomenon, then deliver the core. A gap left open is frustrating; a gap closed is the "aha" moment that makes the idea stick.

**When to skip it.** When the user already asked a direct question, their curiosity is already there. Building suspense in front of the answer then feels like stalling. Answer first; open a smaller gap later only if it helps the next brick land.

**Honesty.** The gap must be real. Gilbert's talk says the two groups end up "equally happy"; the underlying study (Brickman, Coates, and Janoff-Bulman, 1978) found accident victims less happy than controls, though far happier than people predicted. The honest version is still surprising. Prefer it.

## 6. Anchor with metaphors and examples

**What it is.** A metaphor is a mold: it gives an unknown idea the shape of a known one. An example makes an abstract claim visible.

**Choosing a metaphor:**

- **Match the structure, not the surface.** The flight simulator works because its working parts match the prefrontal cortex's role: test in a virtual space, avoid real crashes.
- **Draw from the listener's world.** For a cook, a recipe. For a developer, a cache. For a child, a toy or a game.
- **Say where it breaks** if the break could mislead. "Like a filing cabinet, except that reading an entry slightly changes it."
- **One main metaphor per idea.** Extend it rather than switching mid-explanation.

**Examples:**

- Give a concrete instance soon after the abstract claim, or before it.
- Add a non-example to mark the boundary: "A list sorted by date is not an index, because..."
- Use a worked example for procedures: show the steps on a real case once.

**Metaphor bank from the sources:**

| Abstract concept | Familiar mold | What it makes visible |
| --- | --- | --- |
| Prefrontal cortex | Flight simulator | Testing experiences safely before living them |
| Synthetic happiness | Biological immune system | An active, unconscious defense against adversity |
| Learning progression | Tower of bricks | Each idea must rest on one already in place |
| Distilling a message | Onion and chocolate | Reducing (peel) is a different job from making memorable (wrap) |
| Curse of knowledge | Tapping a song | The speaker hears a melody; the listener hears knocks |

## 7. Name it

**What it is.** Giving a phenomenon a precise name makes it credible, reusable, and easy to talk about.

**How to do it:** let the listener experience the idea first (through the gap, the example, the metaphor), then give the name. The term then labels something they already hold instead of adding vocabulary to memorize. Gilbert names *impact bias* only after the audience has been fooled by it.

**Coined versus established names.** Prefer the field's real term when the listener will meet it again. Coin a name only when none exists, and make it self-explanatory.

## 8. Check the landing

**On the page:** reread as the listener and mark every place where they would hear knocks instead of melody:

- terms they don't know and you didn't define;
- steps you skipped because they feel obvious to you;
- words like "simply", "obviously", "just", which often hide a jump;
- references to things not yet introduced;
- paragraphs that serve your completeness rather than their understanding.

**In conversation:** watch the reply. Confusion, a wrong paraphrase, or a question about an early brick means the tower needs a different base. A light check helps: ask them to predict a case, or offer two directions ("want the intuition or the formal version?"). Use these sparingly; one good question beats a quiz.

**The retell test:** could they explain it to someone else in two sentences tomorrow? If not, the core or the wrapper needs work.
