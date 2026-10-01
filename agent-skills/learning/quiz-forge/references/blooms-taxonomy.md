# Bloom's (Revised) Taxonomy for calibrating difficulty

Used by `SKILL.md` at step 2 to decide what to test, not just how to phrase it.

## The 6 levels

| Level | What's actually being tested | Verbs / stems | Typical example |
|---|---|---|---|
| 1. Remember | Recognizing or recalling information as-is | define, list, name, identify, recall | "What is the definition of X?" |
| 2. Understand | Restating, explaining in one's own words, illustrating | explain, summarize, illustrate, paraphrase, classify | "Why does X lead to Y?" |
| 3. Apply | Using a known rule/method in a new concrete case | apply, solve, use, calculate, demonstrate | "Given this case, what happens if you apply X?" |
| 4. Analyze | Breaking down, comparing, finding the relationship between elements | compare, differentiate, categorize, break down | "What's the essential difference between X and Y in this context?" |
| 5. Evaluate | Judging against criteria, choosing the best option among several defensible ones | justify, critique, judge, prioritize, argue | "Which of these three approaches is best, and why?" |
| 6. Create | Producing something new from what's been learned | design, propose, formulate, construct | Rarely testable as pure MCQ; reserve for open-ended questions |

MCQ covers levels 1 through 5 well. Level 6 (Create) almost never fits a closed-choice format: if the user wants to test this level, suggest an open question instead of forcing an artificial MCQ.

## The verb trap

A "high-level" verb in the stem doesn't guarantee a high-level item. What actually determines the level is the mental operation needed to answer, not the word used.

- "Explain the principle of X" can be a pure recall exercise if the expected answer is a sentence memorized verbatim from the source.
- Conversely, a question that looks factual ("What happens if...") can be a genuine Apply-level item if the case posed doesn't appear as-is in the source and requires transposing a rule.

Before classifying an item, ask: would someone who just memorized the material by heart, without understanding it, get this question right? If yes, it's level 1, regardless of the verb used.

## Progression of the same fact across levels (example)

Source fact: "In n8n, credentials are encrypted and stored separately from workflows."

- **Remember**: "Where does n8n store credentials relative to workflows?"
- **Understand**: "Why does separating credential storage from workflow storage improve security?"
- **Apply**: "A workflow exported as JSON is shared with a colleague. Will the credentials be visible in that file?"
- **Analyze**: "Two workflows use the same API but different credentials. What happens if one of those two credentials is revoked?"
- **Evaluate**: "For a multi-tenant deployment on a single n8n instance, which credential-management strategy best limits the risk of leakage between tenants, and why?"

## Default distribution

- General revision quiz, mixed audience: 20% Remember, 30% Understand, 30% Apply, 20% Analyze/Evaluate.
- "Hard" / exam-level quiz / audience already trained: aim for 10% or less Remember, with the rest split across Understand, Apply, Analyze, Evaluate, weighted toward Apply/Analyze.
- First-exposure quiz (complete beginners): it's legitimate to raise Remember/Understand to 60-70%, a foundation is needed before anything can be applied. Don't impose a "hard" mix on an audience discovering the topic for the first time; difficulty should be desirable, not just punishing.
