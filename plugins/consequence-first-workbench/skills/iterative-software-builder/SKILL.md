---
name: iterative-software-builder
description: Implement, debug, and refine software through small coherent changes and fast evidence-based validation. Use when the user asks to build, fix, change, or continue an application, especially during active UI and behavior iteration, in an existing or dirty worktree, or where some tests are known to time out or cannot run in the current environment. Apply targeted regressions and syntax/data checks during iteration, reserving broad test gates, rebuilds, packaging, hashes, and release work for actual checkpoints. Do not activate for conceptual software advice that does not authorize implementation.
---

# Iterative Software Builder

Move the product forward in inspectable increments. Each loop should leave the relevant behavior more correct and produce evidence proportionate to the change.

## Load the relevant guidance

- Read [references/build-loop.md](references/build-loop.md) before implementing a nontrivial change or debugging an existing system.
- Read [references/validation-cadence.md](references/validation-cadence.md) when selecting tests, handling timeouts, validating UI, or preparing a release checkpoint.
- Read both when continuing an established product across several iterations.

## Core loop

1. Inspect the current artifact, project instructions, working tree, and exact path the behavior follows. Preserve unrelated user changes.
2. Define the smallest coherent outcome that satisfies the current request. Prefer a vertical slice that reaches the actual user-visible or system-visible behavior over disconnected scaffolding.
3. Implement the change in the existing architecture. Use the project’s current state mechanisms instead of creating standalone planning documents or parallel sources of truth.
4. Run the narrowest checks that can falsify the implementation: targeted regressions, syntax or type checks, schema or data validation, and visual inspection at the affected state or viewport.
5. Inspect the diff and the observed behavior. Fix problems found by evidence before broadening scope.
6. Report the implemented outcome, the checks that completed, and any unverified surface. Do not make the user infer whether a timeout was a product failure or an environment limitation.
7. Repeat on feedback without rebuilding or revalidating unaffected parts of the system.

## Validation discipline

- Do not run tests known not to complete in the current environment. Re-run one only when the environment, command, test, or implicated code path has materially changed, or when the user explicitly requests it.
- During UI iteration, favor targeted regressions plus syntax and data checks. Use browser or visual validation when the environment supports it; do not repeatedly attempt a known-dead local browser or Playwright path.
- A syntax check proves syntax. A unit test proves its covered behavior. A rendered screenshot proves only the inspected state. State validation at its actual scope.
- Reserve the full regression gate for an explicit release checkpoint or a change whose blast radius genuinely requires it.
- Avoid rebuilding, packaging, versioning, or hashing until the change set is ready to ship.
- Keep the user informed during long-running work. Do not disappear behind a command that is already known to stall.

## Scope and state

Honor the latest canonical artifact and the user’s current request. Do not merge older versions into the active project merely because they contain apparently missing material. When baseline selection or version reconciliation is part of the task, use the canonical-state-manager skill as well.

Diagnose before widening a fix. A visible symptom may originate in state, data, server behavior, layout, or caching; change the layer that produces it. Once the cause is established and implementation is authorized, complete the fix rather than stopping at a plan.
