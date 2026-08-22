# Scope and invariant

## Recover the actual correction

A correction usually contains more information than the replacement text. Extract:

- the old assumption;
- the corrected proposition;
- why the old state fails;
- the contexts governed by the correction;
- any explicit exclusions;
- whether future work should inherit the rule.

Prefer the user’s precise relation. If they say a distinction *defines* or *focuses* an argument, do not weaken it to the generic claim that the distinction *changes* the argument.

## Classify scope

### Occurrence-local

Only the identified instance is defective. Other identical text may be intentional or unrelated.

### Artifact-wide

The correction governs one manuscript, site, application, dataset, deck, or deliverable.

### Project-wide

The correction governs every active artifact in one project, including generated and user-facing representations.

### Durable preference or method

The correction should guide future work across relevant projects. Use this scope only when the user states or repeatedly demonstrates a general rule.

Scope can differ by surface. A title correction may be project-wide in current interfaces while historical notes retain the former title. A behavioral correction may govern code and tests while old screenshots remain historical evidence.

## Classify correction type

| Type | Governing question |
| --- | --- |
| Factual | What proposition about the world or project is now valid? |
| Terminological | Which label, spelling, title, or name is authoritative? |
| Editorial | Which rhetorical or stylistic operation is disallowed or preferred? |
| Behavioral | What should the system do under the relevant state? |
| Architectural | Which component or source now owns the responsibility? |
| Procedural | How should future work be performed or validated? |
| State-related | Which prior fact, decision, task, or version is superseded? |

One correction can span several types. A renamed button may also change the action it performs after a state transition; copy-only replacement would leave the behavior wrong.

## Write the invariant positively

Express what future work should preserve:

- “The current interface label is ‘Project Atlas.’”
- “After a working record exists, the primary action clarifies the intention.”
- “Long-form paragraphs carry complete movements of thought.”
- “The deployed instance governs current behavior for this reconstruction.”

Then record boundaries separately. Positive invariants are easier to test and less likely to produce an expanding blacklist.

## Avoid false generalization

Do not turn every correction into a universal law. Look for explicit scope language, repeated use, dependency breadth, or a stated durable preference. Preserve a local exception when broader propagation would alter valid material.

When the user corrects an example because it reveals an underlying rule, propagate the rule rather than only the example. When they correct an isolated typo, repair the typo and its genuine duplicates without inventing a new editorial rule.
