# Build loop

Use this loop to keep implementation fast without losing state or evidence.

## 1. Establish the working baseline

- Read project-level instructions and the files that actually govern the behavior.
- Inspect version markers, configuration, schemas, and existing tests relevant to the path.
- Check working-tree status before editing. Treat unrelated modifications as user-owned.
- Identify the canonical runtime or deployed artifact when local and deployed state can differ.
- Reproduce the issue narrowly when diagnosis is part of the request and reproduction is feasible.

Do not inventory the whole repository when a focused trace can identify the relevant path.

## 2. Define the observable outcome

Translate the request into a small set of behaviors a user or calling system can observe. Include responsive state, persistence, error handling, or derived data only when they are part of the requested path.

Prefer a vertical slice:

> input or user action → state transition → logic or persistence → visible result

This prevents a series of locally correct changes from producing no usable behavior.

## 3. Trace the producing path

Locate the actual source of the symptom or behavior:

- component and layout rules for presentation;
- event and state flow for interaction;
- API and persistence path for stored behavior;
- schema and derivation rules for data consequences;
- configuration and environment for runtime differences;
- cache or build artifact for stale output.

Make the fix at the producing layer. Avoid compensatory CSS, duplicate state, hard-coded seed values, or client-side masking of a server defect unless the architecture deliberately assigns responsibility there.

## 4. Implement the smallest coherent change

- Preserve established conventions and public contracts.
- Change all parts required for the behavior to remain internally consistent.
- Include a migration or compatibility path when persisted data or interfaces require one.
- Scrub personal or secret data from seeds, fixtures, examples, and distributable packages.
- Reuse the project’s database, config, task state, issue state, or existing ledger. Do not create a new document for every piece of working state.
- Avoid adjacent cleanup unless it is required to make the requested path safe or understandable.

Small means bounded, not incomplete.

## 5. Validate the affected path

Choose checks from the validation cadence. Start with the fastest meaningful falsifier, then expand only when risk or failures justify it.

For a UI change, inspect the exact viewport, state, and interaction that motivated the request when possible. For a data change, validate both schema and representative state transitions. For a bug fix, add or run the narrow regression that distinguishes the defect from the corrected behavior.

## 6. Review the delta

- Inspect the diff for accidental scope expansion.
- Confirm that only intended files changed.
- Check that fallback, loading, empty, error, and stale states affected by the change remain coherent.
- Verify that active state no longer depends on obsolete or contradictory data.
- Remove temporary diagnostics unless they are intentionally retained.

## 7. Hand off the increment

Lead with what now works. Name the validation that completed and any meaningful surface that remains unverified. Keep implementation detail proportional to the user’s need.

Do not package a routine iteration as a release. Continue from the current working state until the user identifies a checkpoint or the change set is otherwise ready to ship.

