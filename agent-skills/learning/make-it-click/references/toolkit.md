# Toolkit: the moves in depth

Each section expands one move from `SKILL.md`: why it works, how to do it well, and how it goes wrong. The source cases (Newton, Gilbert, Robbins, Hormozi) show the principles at work; build your own anchors and wrappers from the listener's world rather than reusing these.

## The curse of knowledge

Camerer, Loewenstein, and Weber described the effect in 1989 and credited Robin Hogarth with the name. In Newton's 1990 experiment, 120 songs from a list of 25 well-known tunes were tapped in total; tappers expected listeners to name about half, and listeners named 3.

It shows up in three ways:

- **Dumping**: saying everything because it is all true and all feels relevant.
- **Burying**: the main idea arrives late, after context that matters only to you.
- **False clarity**: logic that feels obvious to you, so you leave terms undefined and steps out.

## Find the core

The core is the most important idea: compact, deep, graspable by a newcomer. The rest is layers: outside, history, chronology, anecdotes ("it was 2003, or 2004, the year Facebook launched, I had white sneakers on..." when the point is *I saw Obama backflip off a bridge*); further in, conditions and implementation detail; deepest, proofs, nuance, and expert vocabulary.

Shape the core by the listener's purpose. "What is an index?" has one core for a student (a sorted lookup structure) and another for a product manager (it makes reads fast and writes slower). A good core is **deep** as well as short: "databases store data" is too shallow; "an index trades write speed and space for read speed" carries the insight.

Peeling stings, because each layer took effort to learn and cutting it feels like losing rigor. That feeling is the curse of knowledge talking, and often ego: detail added to prove expertise rather than to help. Peeled layers aren't lost; they become follow-ups, appendices, or a "going further" line.

## Clear wrong bricks

A tower built over a wrong brick gets absorbed into the wrong model: the listener nods, then keeps believing that heavier objects fall faster, that evolution has a goal, or that a p-value is the probability that the hypothesis is true. Research on conceptual change and "refutation texts" shows that naming the wrong idea and confronting it works better than explaining around it.

Bring it out (a prediction, a vote, "most people picture X"), let it fail on a concrete case the listener can check, then give the right brick and show why it handles that case. Keep it respectful: a common misconception is common because it is reasonable. When the listener offers their own version, it is the most precise map you will get of where the wrong brick sits.

## Build the tower

Work backwards from the core to the minimum set of bricks it needs, drop the ones this listener already holds, and order the rest so each one rests on what came before. Useful orders: concrete before abstract, example before definition, familiar before new, whole before parts when the listener needs a map, parts before whole when the whole would mean nothing yet. A forward reference ("we'll see why later") loses more listeners than it promises to bring back.

Gilbert's tower ("The surprising science of happiness", TED, 2004):

- **Hook**: in two million years, the human brain nearly tripled in mass. Why would nature want that?
- **Organ**: Gilbert credits much of the growth to the frontal lobe, especially the prefrontal cortex.
- **Function**: it works as an *experience simulator*, like a pilot's flight simulator.
- **Anchor**: no one needs to taste liver-and-onion ice cream to know it is bad.
- **Gap**: lottery winners versus paraplegics.
- **Name**: *impact bias*, the simulator's habit of overestimating how strong and how long an emotional impact will be.
- **Core**: we *synthesize* happiness through a *psychological immune system*.

Note the order: the real gap comes only after the simulator is in place, because the audience needs it to make the prediction that fails.

## Open a gap

Curiosity is the feeling of a gap between what you know and what you want to know (Loewenstein's information-gap account). It pulls only when the listener knows enough to feel the gap. A puzzle they can't parse is just noise.

Ways to open one:

- **Commit, then flip**: get the listener to commit to their intuition (a guess, a vote), then show the real result. Gilbert even shows a chart that confirms the audience's expectations, then says he made it up and shows the real data. If you stage anything, reveal it right away.
- **A paradox**: two things that both seem true and seem to contradict each other.
- **A surprising number**: 3 songs out of 120, when tappers expected half.
- **A visible problem**: show the failure the concept solves before showing the concept.

Close every gap you open: name the phenomenon, then deliver the core. Keep the surprise honest (see "Keep it true" in `SKILL.md`).

## Anchors and metaphors

An **anchor** makes a brick understandable now. A **wrapper** makes the core memorable later. A metaphor can do either job; decide which one you are asking it to do.

To find a metaphor for any subject, start from the concept's two or three key relations (what causes, limits, or flows into what), then look in the listener's world for a domain with the same relations. Check every part that maps across; if a key part maps wrongly, drop the metaphor. When the point where it breaks could mislead, name it: "like a filing cabinet, except that reading an entry slightly changes it." Keep one main metaphor per idea and extend it rather than switching mid-explanation.

Examples work alongside metaphors. Give a concrete instance near the abstract claim, a non-example to mark the boundary ("a list sorted by date is not an index, because..."), and for procedures, one worked example on a real case.

## Wrap the core

A bare truth is easy to understand now and easy to forget later. Choose the wrapper from the concept's shape:

| Wrapper | Fits when the concept is... |
| --- | --- |
| Story or anecdote | An event, a consequence, a human stake |
| Metaphor | An invisible mechanism |
| Name | A pattern people should recognize again |
| Rule or method | A behavior to adopt |
| Equation or model | A relationship that really is proportional or multiplicative |
| Diagram | A structure, a flow, a hierarchy, a feedback loop |
| Demonstration | A claim people would doubt if only told |
| Slogan | A principle that must travel through a group |

Two cases from the sources:

- **Mel Robbins.** Core: when you hesitate, act physically before doubt builds. Wrapper: the 5-Second Rule (count 5-4-3-2-1, then move). Robbins frames the countdown as a "pattern interrupt"; that is her explanation, not settled science. The wrapper works because anyone can count; you don't need the psychology to use it.
- **Alex Hormozi.** Core: perceived value depends on several interacting factors. Wrapper: the Value Equation, *value = (dream outcome × perceived likelihood) / (time delay × effort and sacrifice)*. It is a mnemonic, not a real equation: it tells you which factors to push and in which direction, not a number. It offloads a multi-factor judgment into a shape people can apply.

Test a wrapper by asking: could someone repeat it after hearing it once? Does it carry the core faithfully rather than decorate it? Is it true at the precision it implies? If the relationship isn't really multiplicative, a list or a 2×2 grid beats a pseudo-equation. Several competing wrappers tend to cancel each other out.

## Name it

A precise name makes a phenomenon credible, reusable, and easy to discuss. Gilbert names *impact bias* only after the audience has been fooled by it, so the term labels an experience they just had. Prefer the field's real term when the listener will meet it again; coin a name only when none exists, and make it self-explanatory.

## Show it

Some explanations land fastest as an artifact the listener can look at:

- **A trace** for concurrency, algorithms, or data flow: `T1 reads 5 → T2 reads 5 → T1 writes 6 → T2 writes 6`, one increment lost.
- **A worked number** for finance, statistics, or physics.
- **A table** for comparisons and trade-offs.
- **A diagram** (ASCII, Mermaid, or an image where available) for structures, flows, and feedback loops.
- **A tiny code snippet** when the listener reads code more easily than prose.

Always say what to notice; an artifact without a pointer is one more thing to decode.

## Check the landing

On the page, reread as the listener and mark where they would hear knocks: terms you didn't define, steps you skipped because they feel obvious, words like "simply" and "just" that hide a jump, and paragraphs that serve your completeness rather than their understanding.

In conversation, the strongest checks make the listener *use* the idea: predict a case ("so what happens if both threads read first?"), apply it to something new, or put it in their own words. These also strengthen memory, through retrieval and self-explanation. When they restate the idea, correct the specific part that is off rather than re-explaining everything. Use checks sparingly: one good question beats a quiz.

The retell test applies when they need to remember or pass the idea on: could they explain it to someone else in two sentences tomorrow? If not, the core or the wrapper needs work.
