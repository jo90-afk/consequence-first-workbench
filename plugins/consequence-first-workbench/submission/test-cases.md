# Submission test cases

## Positive cases

### 1. Consequence propagation

Prompt: “A customer can now pause a subscription instead of cancelling it. Trace every state, task, message, metric, and interface that should change.”

Expected: Use `consequence-first-design`; identify derived state, invalidations, replacements, and operational consequences.

### 2. Canonical-state reconciliation

Prompt: “The deployed application is canonical, but this older repository contains one missing report. Recover only that report without regressing later behavior.”

Expected: Use `canonical-state-manager`; establish directional lineage and reintroduce the selected feature as a forward change.

### 3. Project intake

Prompt: “I want an internal tool for reviewing supplier risk. Ask only what you need to make it build-ready.”

Expected: Use `project-intake-architect`; resolve material unknowns adaptively and produce canonical project state.

### 4. Argument and evidence

Prompt: “Map this strategy paper’s claims, show which ones repeat, and identify the exact evidence each contestable claim needs.”

Expected: Use `argument-architecture` and `evidence-lineage-researcher`; separate claim functions and map evidence to claim scope.

### 5. Bounded implementation

Prompt: “Implement the approved workflow change in this dirty worktree, validate the affected behavior, and leave release packaging for the checkpoint.”

Expected: Use `iterative-software-builder`, with canonical-state or correction propagation support when the repository state requires it.

## Negative cases

### 1. Stable fact

Prompt: “What is the capital of France?”

Expected: Do not activate the plugin; answer directly.

### 2. Styling-only request

Prompt: “Make this button blue. Its behavior and state model are already settled.”

Expected: Do not activate consequence-first or model-to-interface skills solely for a cosmetic edit.

### 3. Conceptual software explanation

Prompt: “Explain recursion with a short example, but do not change any files.”

Expected: Do not activate `iterative-software-builder`; provide conceptual guidance only.

