---
name: correction-propagator
description: Turn an accepted correction into a correctly scoped, durable change across affected copy, code, data, tests, metadata, interfaces, requirements, and project state. Use when the user corrects a term, title, fact, interpretation, behavior, workflow, or design rule; says an error survives, asks to fix something everywhere, or makes a local correction that may expose sibling occurrences or dependent assumptions. Infer whether the correction is local, artifact-wide, project-wide, or durable across future work. Do not activate for a new feature request with no prior state being corrected, and do not universalize a one-off preference without evidence.
---

# Correction Propagator

Treat an accepted correction as new governing information. Repair the active system that depended on the old assumption, preserve legitimate historical uses, and prevent the defect from returning.

## Load the relevant guidance

- Read [references/scope-and-invariant.md](references/scope-and-invariant.md) when deciding what the correction actually establishes and how far it applies.
- Read [references/propagation-audit.md](references/propagation-audit.md) when searching, changing, and verifying affected surfaces.
- Read both when the correction changes behavior, architecture, canonical terminology, or several artifact types.

## Core method

1. Extract the corrected proposition or invariant in positive, precise language. Preserve the user’s exact distinction when their wording is more specific than the prior model.
2. Classify the correction: factual, terminological, editorial, behavioral, architectural, procedural, or state-related.
3. Determine scope across occurrence, artifact, project, and durable preference. Resolve time and context before treating apparent contradictions as errors.
4. Find semantic dependents as well as literal matches. Include derived copy, labels, metadata, tests, schemas, documentation, navigation, prompts, and generated representations when they encode the old assumption.
5. Classify each candidate before changing it: active defect, historical record, intentional quotation, generated output, unrelated usage, or unresolved ambiguity.
6. Correct canonical sources first. Update derived artifacts only when their normal generation or release cadence calls for it.
7. Record a durable rule in the project’s existing state mechanism when future work must inherit it. Do not create a parallel correction document merely to remember the change.
8. Verify both absence and coherence: the old assumption no longer governs active state, and the corrected state behaves consistently across its dependents.

## Boundaries

Do not replace legitimate historical language, quotations, source titles, migration records, or version notes merely because they contain superseded wording. Preserve them with enough context to prevent their reuse as current truth.

Do not ask the user to reconfirm a correction they have already made. Ask only when two materially different scopes remain plausible and choosing silently could damage unrelated work.

When several artifacts make competing claims to current state, establish the canonical baseline before propagation. When the corrected proposition materially changes downstream tasks, permissions, or behavior, trace those consequences rather than stopping at string replacement.
