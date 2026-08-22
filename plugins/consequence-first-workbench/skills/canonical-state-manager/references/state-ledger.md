# Canonical state ledger

Use the project’s existing database, manifest, configuration, or state store whenever possible. The ledger is a logical model, not a requirement to create another document.

## Minimal record

Track only fields the system can use:

- scope and stable key;
- precise proposition, decision, or state value;
- status: canonical, uncertain, superseded, or historical;
- source or evidence;
- effective time and observation time when materially different;
- the item it supersedes or the item that supersedes it;
- dependents or consequences when they affect behavior;
- attention state: frontier or background;
- last verification when freshness matters.

## Frontier and background state

**Frontier state** contains newly introduced, contradicted, or unresolved information whose consequences are still being propagated or whose status still requires attention.

**Background state** contains settled canonical information the system continues to rely on without repeatedly reconsidering it.

Moving a proposition from frontier to background does not archive or weaken it. The proposition remains active; its contradictions have been resolved, its material consequences have been propagated, and it no longer needs to occupy the primary reasoning surface.

When new evidence contradicts background state:

1. create a new frontier event;
2. preserve the former proposition with its historical scope;
3. resolve truth, uncertainty, and effective time;
4. supersede rather than overwrite when history is material;
5. propagate consequences through dependent decisions and tasks;
6. return the settled successor to background state.

## Artifact state and world state

Keep these distinct:

- **artifact state** answers which file, build, database, or deployment is authoritative;
- **world state** answers which propositions and decisions are currently valid.

An artifact can be canonical while containing uncertain propositions. A proposition can be canonical for a time period while its original file is historical. Preserve both dimensions so version management does not become truth management by accident.

## Contradiction handling

Do not overwrite a proposition merely because new information arrives. Determine whether the statements differ by time, scope, subject, confidence, or actual truth. Preserve a change event and update active state deliberately.

Do not leave a superseded proposition active merely to preserve history. Active queries and interfaces should resolve to the current proposition; history remains inspectable through lineage.

## Decision persistence

Record a decision as background state once it is approved and its consequences are integrated. Later work should inherit it without re-litigating it. Reopen the decision only when the user changes it, new evidence invalidates a premise, or the current request explicitly calls for reconsideration.

This prevents settled project state from consuming frontier reasoning on every turn while keeping the basis of the decision available.
