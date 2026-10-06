# Option balancing: remove cues without weakening the question

## Evidence and scope

The NBME Item-Writing Guide (November 2020, chapter 3, especially the discussion of a correct answer that stands out and the summary of technical flaws) describes extra length and detail in the key as cues for test-wise learners. It also discusses absolute wording, repeated wording and convergence cues. [Original NBME guide, hosted by ScholarRx](https://scholarrx.com/wp-content/uploads/2022/02/NBME_Item-Writing-Guide_2020.pdf). The [current NBME guide page](https://www.nbme.org/institutions/nbme-item-writing-guide/) offers the sixth edition via a request form.

The [American College of Surgeons item-writing guidelines](https://www.facs.org/for-medical-professionals/education/cme-resources/test-writing/) recommend similar-length distractors, plausible alternatives and putting common wording in the stem. [Haladyna, Downing and Rodriguez (2002)](https://doi.org/10.1207/S15324818AME1503_5) review a taxonomy of 31 guidelines using textbook consensus and research evidence. Its abstract was available during this review; the full publisher text was not accessible, so no quantitative cutoff is attributed to it.

These sources support comparable options and removing irrelevant clues. The numerical tolerances and sentence-count rule below are **Quiz Forge implementation choices**, not experimentally established guarantees of item quality. Sources checked on 6 October 2026. Medical examples inform general item-writing practice, not a claim that every recommendation has been validated in every subject.

## Required drafting and repair loop

1. Decide what the learner must distinguish and establish the key from the source.
2. Choose a shared structure: short noun phrases, one-sentence actions, or the same number of sentences for every choice. Keep register and specificity comparable.
3. Count words in each displayed option, excluding A/B/C labels and separate feedback. Use whitespace-separated tokens containing a letter or number. Apostrophes, hyphens, numbers and technical tokens stay intact; punctuation-only tokens do not count. Apply the same convention to every choice.
4. Calculate the median count. Accept only a longest-minus-shortest spread of at most `max(2, ceil(0.20 × median))` words. Aim closer when natural. Counts 10/11/12 pass (allowed spread 3); 10/11/14 fail (spread 4). Equal counts are welcome but do not justify unnatural prose.
5. Match sentence counts: normally one sentence or one fragment for every option. Move shared setup into the stem and reasoning into post-answer feedback. Do not require feedback itself to have equal word counts; its job is to explain misconceptions.
6. If the key stands out, remove dispensable wording or rewrite all choices with the same template. Do not lengthen distractors with filler, add unsupported claims, or drop essential conditions from the key. Rewrite the stem or the whole question when necessary.
7. Recheck semantic quality after balancing: one defensible key, plausible misconceptions, no grammar clues, repeated-word clue or uniquely qualified option. Counts cannot verify these properties.
8. Review the quiz as a whole. A small length advantage can still become a cue when repeated. The checker flags a uniquely longest key in more than 60% of at least five valid MCQs (ties count as no uniquely longest key). Review shorter quizzes manually. Do not impose a new deterministic pattern in word lengths or answer positions.

## Automated checks and limits

`scripts/qa_check.py` reports word counts by option ID, excessive spreads, mismatched sentence counts, empty options and recurring longest-key cues. It returns exit code 1 for detected issues. Use the internal JSON even if the final quiz uses another format.

Sentence counting is a punctuation heuristic: periods, question marks and exclamation marks followed by whitespace or the end of the text delimit units; an unpunctuated fragment counts as one. Common French/English abbreviations and decimals are handled, but initials, URLs, code, equations and other languages can still require manual inspection. A heuristic false positive must be verified explicitly; do not strip meaningful punctuation to silence the check. Languages without spaces between words also require a language-appropriate manual word count. The checker does not compare character lengths or explanation lengths, establish source truth, or prove the absence of all stylistic cues.
