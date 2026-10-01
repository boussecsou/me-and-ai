---
name: quiz-forge
description: Generates pedagogically sound quizzes (multiple-choice and other formats) from a course, PDF, notes, or any source material. Use this skill whenever the user asks for a quiz, multiple-choice questions, an MCQ, a knowledge check, an assessment, a revision test, choice-based flashcards, or wants to "test" understanding of a document, even if the word "quiz" isn't used. Applies item-writing guidelines (Haladyna et al.), Bloom's taxonomy, and retention research (testing effect, Bjork's desirable difficulties) to produce questions grounded in the source, calibrated in difficulty, with plausible distractors and per-option feedback. Always generates the actual quiz content in whichever language the user is working in, keeping technical or domain-specific terms in their original language. Not for personality quizzes, opinion polls, or purely entertainment content with no learning stakes.
---

# Quiz Forge

## Why this skill exists

Most AI-generated quizzes without a strict framework share three recurring flaws:

1. They test raw recall (isolated dates, definitions) because that's easy to turn into a question, not because it's what actually matters in the content.
2. Distractors are either absurd (the question becomes trivial guesswork) or riddled with cues (length, grammar, phrasing) that give away the answer without requiring any real knowledge.
3. Questions, and sometimes even answers, aren't actually grounded in the source: the model fills gaps with general "knowledge" about the topic, which can introduce factual errors invisible to the user.

This skill encodes rules from research in educational measurement and cognitive science to avoid these three traps. The goal isn't to produce "a quiz" but a quiz that genuinely measures understanding and, if retaken, helps retain the content better.

## Language

The instructions in this skill are written in English, but the quiz content itself must always be produced in whichever language the user is actually working in, inferred from their message and/or the source material's language. Default to that language for everything: stems, options, explanations, titles.

**Keep technical and domain-specific terms in their original language whenever forcing a translation would be unnatural, ambiguous, or would break the vocabulary the learner already uses.** Examples: product names, protocol and API names, programming keywords, tool-specific jargon (n8n nodes, HTTP methods, SQL clauses), scientific nomenclature already standardized in another language. A French quiz about a REST API should still say "endpoint" and "webhook," not force an awkward French neologism. An English quiz about French administrative procedures should still use the French term if that's what practitioners actually use. Use judgment: the test is whether a real practitioner of the subject, in the target language, would recognize and expect the term as-is.

If the language to use is genuinely ambiguous (mixed-language source, no clear signal from the user), ask rather than guess.

## Process in 6 steps

### 1. Understand the source before writing a single question

Never generate questions from a rough mental summary of the document. Read the whole source.

- If the source is a PDF, use the `pdf-reading` skill to extract it properly before continuing (don't guess content from a filename or a skim).
- Identify what actually matters: core concepts, mechanisms, cause-and-effect relationships, distinctions the document itself emphasizes (headings, repetition, worked examples). Ignore purely anecdotal details unless the user explicitly wants fine-grained factual recall.
- If the content covers several sub-topics of unequal importance, distribute questions proportionally to that importance, not evenly by page or paragraph. A quiz that gives a footnote the same weight as the chapter's central concept is a bad quiz, even if every individual question is well written.

### 2. Decide the cognitive distribution before drafting

See `references/blooms-taxonomy.md` for the full breakdown of the 6 levels and verb stems.

By default, aim for a mix that isn't dominated by recall: roughly 20% Remember, 30% Understand, 30% Apply, 20% Analyze/Evaluate. If the user explicitly asks for a hard or advanced quiz ("challenging," "exam-level," "for people who already know the basics"), cut Remember sharply and push toward Apply/Analyze/Evaluate: questions that force reasoning about a case, comparing two elements of the material, or spotting the error in a scenario, not just recognizing a sentence already seen.

Trap to avoid: a question's cognitive level isn't decided by the verb used in the stem. "Explain why X" can still be pure recall if the expected answer is a sentence memorized verbatim from the source. The real test: does answering correctly require a mental operation (combining, transposing, judging), or just retrieving a sentence already read?

### 3. Draft each item against the anti-flaw rules

See `references/item-writing-rules.md` for the full list with good/bad examples. The highest-impact rules to apply every time:

- **The stem must be answerable without seeing the options.** A real question or a completable statement, never a bare "Which of the following..." that only makes sense after reading the choices.
- **Exactly one correct answer, unambiguous.** If two options can reasonably be defended, the item is miscalibrated, not just tricky.
- **3 to 4 options, no more.** Beyond that, extra distractors are almost always non-functional (nobody picks them) and just add reading noise. Aim for 3 strong options rather than 5 where 2 are laughable.
- **Every distractor must be a plausible, realistically-made error**, ideally a documented or predictable confusion about this exact topic, not a random wrong answer. A good distractor is what someone who misunderstood one specific point would actually answer.
- **Forbidden:** "all of the above," "none of the above," negatively-phrased stems without clear emphasis, grammatical cues that give away the answer (singular/plural agreement, articles), a correct answer that's systematically longer or more detailed than the distractors.
- **One idea per item.** Never test two concepts at once; if the learner gets it wrong, it should be clear exactly what they got wrong.

### 4. Ground every item in the source (anti-hallucination)

This is the step most automated quiz generators skip, and it's the leading documented cause of poor quality in AI-generated questions: invented facts, distractors disconnected from the actual content, "correct" answers that aren't quite correct.

For each item, before finalizing it, mentally identify the exact passage of the source that justifies the stem, the correct answer, AND the distractors (distractors must also be verifiable: either a documented confusion or a plausible variation of a real fact from the material, never a fabricated fact). If a concept seems worth testing but isn't clearly covered by the source, don't fill the gap with general knowledge without flagging it. Either drop the question, or mark it explicitly as "beyond the source" if the user asked to go further than the material provided.

The `source_ref` field in the output format (see below) exists precisely to document this grounding, and lets the user spot-check it quickly.

### 5. Write pedagogical feedback, not just an answer key

For every option, write a short explanation: why the correct answer is correct, and why each distractor is wrong, naming the specific misconception it represents. This isn't decoration. Research on the testing effect shows the memory benefit comes mainly from active retrieval followed by corrective feedback, especially on mistakes: a quiz with no feedback is an assessment; a quiz with feedback is a learning tool.

### 6. Self-check before delivering

Before presenting the final result, review every item against `references/qa-checklist.md`. If the quiz is generated as structured JSON (see below), also run `scripts/qa_check.py` on the file to catch mechanical flaws automatically (duplicate options, abnormal length, forbidden phrasing, missing fields). Fix everything flagged before showing the result. Don't expose this verification work to the user, just deliver a clean quiz, unless they explicitly ask to see the audit.

## Output format

Decide how to deliver the quiz in this order of priority:

1. **A native quiz mechanism already available in the current session or platform** (an interactive quiz widget/tool, an LMS the user is connected to, a quiz feature of the app being used). If one exists, use it directly to render the quiz. Don't force a JSON dump into the chat just because a schema exists below, when a proper interactive tool is right there.
2. **The user's own existing quiz system.** If the user mentions they already have an internal quiz format, a platform, or an API their tooling expects, generate the content to match that system's fields and structure instead of inventing a new one. Ask what fields/format it needs if unclear.
3. **The default structured schema** in `assets/example-quiz.json`, when neither of the above applies. This keeps the output machine-readable and reusable (an automation pipeline, a database, a custom front-end) rather than throwaway prose. Field names in the schema stay as written (English keys); only the content values (stems, options, explanations) follow the target language decided in the Language section above.
4. **Plain readable text** (question, options, then answer and explanations) as a last resort, when the user just wants to read the quiz in the chat and none of the above applies.

Whichever presentation is chosen, the structured content described in step 5 above (grounded stem, options, correct answer, per-option explanation, source reference, Bloom level) should still exist internally before rendering, since it's what step 6's self-check runs against.

## Variants and edge cases

- **Question format.** Classic MCQ is a recognition format: research shows its long-term retention effect is weaker than short-answer or open questions, which force genuine retrieval. Default to pure MCQ (that's what's expected of "a quiz"), but if the user's stated goal is long-term retention rather than a quick self-check, suggest mixing in a few short-answer questions instead of going 100% MCQ.
- **A series of quizzes across sessions.** If the user is preparing several quizzes on the same body of material (exam prep, a course advancing chapter by chapter), favor interleaving topics rather than blocking one quiz per chapter, and space out repetition of key concepts rather than concentrating everything on the first occurrence. These are two of Bjork's four "desirable difficulties," alongside retrieval practice itself.
- **Unclear audience.** If the target audience's level isn't clear (beginners vs. an audience already expert in the topic), ask a quick question rather than guessing; difficulty calibration depends directly on it.
