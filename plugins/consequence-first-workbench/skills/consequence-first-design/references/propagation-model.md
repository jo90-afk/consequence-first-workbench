# Propagation model

Use the smallest model capable of preserving consequences. The purpose is coherent behavior, not graph density.

## Core objects

### Proposition

A proposition is a claim the system may rely on.

Useful fields:

- precise statement;
- status: true, false, uncertain, or superseded;
- source and observed time;
- effective time when different;
- confidence or verification state when needed;
- dependencies;
- downstream consumers;
- superseding proposition when applicable.

Only model a proposition as consequential when some decision, action, representation, or derived state consumes it.

### Decision

A decision selects behavior under a set of propositions and constraints. Record the conditions under which it remains valid.

### Derived state

Derived state includes eligibility, priority, recommendations, computed summaries, permissions, interface states, notifications, and other conclusions generated from propositions or decisions.

### Action

An action is executable work produced by current state. Tie it to its generating premise, support status and notes, and define what completion changes.

### History event

A history event records the transition without allowing prior state to remain active. Preserve what changed, why, when, and which derived items were invalidated, retained, or replaced.

## Useful dependency relations

Use relations only when the system acts on them:

- **requires**: the dependent item is invalid without the source;
- **enables**: the source makes an option available;
- **disables**: the source removes an option;
- **contradicts**: both propositions cannot remain active in the same scope and time;
- **replaces**: the new item succeeds the old item’s function;
- **derives**: the target is computed or inferred from the source;
- **evidences**: the source changes confidence without mechanically determining truth.

Name scope and time when apparent contradictions can both be historically true.

## Propagation procedure

### 1. Normalize the transition

Write the prior and current state explicitly:

| Before | Now |
| --- | --- |
| Proposition P was active | P is false, uncertain, or superseded by Q |
| Decision D relied on P | D must be retained, revised, or invalidated |
| Tasks T1 and T2 derived from D | Each task must be retained, removed, or replaced |

Do not use a generic “changed” status when the actual relation is known.

### 2. Find direct consumers

Identify every decision, rule, task, summary, notification, permission, and interface state that explicitly depends on the changed proposition.

### 3. Propagate transitively

For each affected consumer, inspect its own dependents. Continue until later nodes remain valid and produce the same behavior.

### 4. Resolve each affected item

Choose one outcome:

- **retain** because its premises remain valid;
- **revise** because only scope, timing, or parameters changed;
- **invalidate** because a required premise failed;
- **replace** because the new state implies a successor;
- **suspend** because uncertainty prevents a safe conclusion.

Never leave a false proposition in the active model simply because history must be preserved. Move it to inspectable history and recompute the active map.

### 5. Generate the human explanation

Summarize the environmental change, its most important consequences, and the organizing logic of the next actions. Use one paragraph before lists or visualizations.

### 6. Generate the action surface

Expose only current executable work. For each action, retain:

- what to do;
- why it exists;
- the premise or event that generated it;
- timing or dependency when material;
- completion state;
- notes;
- the state change completion should cause, if any.

## Example: loss of a job

If “I have a job” becomes false, the system should not merely mark the proposition red. It should remove active tasks whose only purpose was maintaining that employment, retain obligations that survive employment, revise cash-flow and insurance assumptions, and generate the few successor actions the new state makes necessary. The primary interface should summarize the changed environment in plain language and present those actions. The former proposition and invalidated tasks remain available in history, not in the active world map.

## Example: product capability removed

If a plan no longer includes single sign-on, propagate the change through entitlement rules, upgrade paths, onboarding, account settings, support guidance, sales claims, tests, and customer communications. A banner on the settings page addresses only one representation of the consequence.

