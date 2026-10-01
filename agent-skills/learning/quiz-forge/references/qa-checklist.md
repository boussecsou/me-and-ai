# Self-check checklist (before delivering the quiz)

Apply to every item, either mentally or via `scripts/qa_check.py` for the mechanical part. Inspired by item-writing-flaw (IWF) rubrics used in research to audit MCQ items.

## Per item

- [ ] The stem is understandable and answerable without reading the options.
- [ ] The stem tests exactly one idea.
- [ ] There is exactly one correct answer, with no possible ambiguity against a distractor.
- [ ] There are 3 or 4 options, no more, no less.
- [ ] No option is "all of the above" / "none of the above" / a variant of these phrases, in any language.
- [ ] Every distractor is plausible: a mistake a learner could realistically make, not something eliminable by pure common sense without knowing the subject.
- [ ] Options are homogeneous in length and level of detail (the correct answer doesn't mechanically stand out from the distractors).
- [ ] No grammatical cue (agreement, article) gives away the correct answer.
- [ ] If the stem contains a negation, it's made unambiguously visible.
- [ ] The stem, the key, and every distractor are grounded in the source (a verifiable fact, not an unflagged extrapolation).
- [ ] Every option has an associated explanation (why it's right / why it's wrong, naming the misconception for distractors).
- [ ] The targeted cognitive level (Bloom) matches the mental operation actually required, not just the verb used.
- [ ] Content (stem, options, explanations) is in the target language, with technical/domain terms correctly kept in their original language where appropriate.

## Across the whole quiz

- [ ] The distribution of questions reflects the relative importance of sub-topics in the source, not a mechanical split by page/paragraph.
- [ ] The overall cognitive distribution matches what was decided at step 2 (not defaulting to 100% recall).
- [ ] No question depends on the answer to another question.
- [ ] The position of the correct answer (A/B/C/D) varies across questions, not always in the same spot.
- [ ] The delivery format matches what step 6 of `SKILL.md` calls for: a native quiz tool if one exists, the user's own system if they have one, otherwise the structured schema in `assets/example-quiz.json`.
