---
name: consequence-first-design
description: Design or revise products, software, workflows, organizations, plans, and stateful tools by tracing what else becomes different when a fact, decision, event, requirement, or user action becomes true. Use for dependency mapping, change propagation, invalidation and replacement logic, world-state models, task derivation, state-aware UX, or requests to turn a major change into coherent action rather than alerts. Do not activate for unconstrained visual styling or ideation that has no material state, dependency, or behavioral consequence.
---

# Consequence-First Design

Treat a material proposition as a source of derived state rather than a note. Begin every design pass with the question: **What else becomes different if this is true?**

## Load the relevant guidance

- Read [references/propagation-model.md](references/propagation-model.md) when designing state, dependencies, invalidations, replacements, or tasks.
- Read [references/consequence-review.md](references/consequence-review.md) when reviewing an existing product, workflow, or proposed change.
- Read both when a major state change crosses data, logic, interface, and action.

## Core method

1. State the triggering fact, decision, event, or action precisely. Record uncertainty instead of quietly converting it into truth.
2. Establish the transition from prior state to current state. A change has consequences because something that was previously valid, available, required, or assumed no longer has the same status.
3. Trace direct consequences, then follow each affected dependency until no further material decision, obligation, task, representation, or permission changes.
4. Invalidate derived state that no longer has a valid premise. Exclude false or superseded propositions from active views while preserving provenance and change history.
5. Replace obsolete work when the new state implies a successor. Deleting a task or flow without creating the work now required leaves the system consistent but unusable.
6. Recompute actions, priorities, explanations, interface states, notifications, and stored summaries from the new state.
7. Synthesize a major change in one plain paragraph before exposing detail. Explain what changed in the person’s or system’s environment and what now requires attention.
8. Project consequences into a short actionable task surface. Tie each task to the proposition or decision that makes it necessary; support completion and notes.

## Materiality

Propagate a consequence when it changes what the system or a person should believe, decide, do, see, retain, permit, or stop doing. Do not generate an exhaustive graph of associations. Stop when downstream state remains valid and behavior would be identical.

Separate truth from attention. A proposition may be true without requiring immediate action; a task may be urgent because of a dependency rather than because the underlying fact is newly entered.

## Experience standard

Do not answer a major life or operating change with a dashboard full of alarms. Lead with synthesis, then action, then inspectable detail. Every warning should explain its source and either offer a useful action or remain out of the primary attention surface.

Preserve the causal chain beneath the interface so users can inspect why an item exists, what would invalidate it, and which later state depends on it.
