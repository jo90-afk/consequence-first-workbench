# Work-order contract

## When to create a work order

Create a separate order when the work has:

- a coherent outcome or state delta;
- a boundary that reduces interference with other work;
- identifiable inputs and dependencies;
- an owner capable of completing it;
- proof and acceptance that can be evaluated;
- enough substance to justify coordination overhead.

Keep tightly coupled steps inside one order. Do not split research, implementation, and validation automatically when the same bounded outcome is better owned end to end.

## Minimal contract

| Field | Requirement |
| --- | --- |
| Purpose | The project condition this work advances |
| Outcome | Observable deliverable or state delta |
| In scope | Work the owner is authorized and expected to perform |
| Out of scope | Adjacent work that must remain untouched |
| Inputs | Canonical artifacts, decisions, data, and assumptions |
| Dependencies | Conditions that must be satisfied first |
| Owner | One accountable agent or human role |
| Authority | Decisions and mutations allowed, including environment limits |
| Interfaces | Shared files, APIs, schemas, or decisions that require coordination |
| Proof | Evidence the owner must produce |
| Acceptance | Who or what decides the outcome is integrated |
| Stop conditions | Conditions requiring pause, escalation, or re-scoping |
| Successor state | What becomes active, background, superseded, or newly available after acceptance |

Use the project’s current state system. A work order may be a database record, task object, issue, or structured state entry; it does not require a standalone document.

## Work-order states

- **proposed** — useful outcome identified, contract incomplete or unapproved;
- **ready** — dependencies, authority, and inputs are satisfied;
- **active** — owner is executing within the contract;
- **blocked** — a named dependency or authority gap prevents progress;
- **proof** — work is complete enough for validation or review;
- **accepted** — proof satisfies acceptance and the state delta is integrated;
- **rework** — validation found a bounded defect requiring correction;
- **superseded** — another order or changed state replaced the need;
- **canceled** — principal or authorized owner ended the work without integration.

Completed does not mean accepted. Acceptance does not mean every future improvement is complete.

## Decomposition tests

Before activation, ask:

1. Can the owner complete the order without guessing another workstream’s decisions?
2. Does the order produce a useful state delta rather than another plan?
3. Are shared files or interfaces protected from competing edits?
4. Can proof falsify the result?
5. Is escalation required before consequential actions?
6. Will acceptance reduce the active frontier?

Merge orders that fail independence because they share one decision surface. Split an order whose owner would otherwise receive unrelated authority or whose proof cannot evaluate a coherent outcome.

## Changes during execution

When new information alters the contract:

- update the governing proposition or decision first;
- identify active orders affected by it;
- retain, revise, block, supersede, or cancel each order explicitly;
- preserve completed evidence and work that remains valid;
- create successor work only for the actual new delta.

Do not allow obsolete orders to remain active with warning labels.

