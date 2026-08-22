---
name: bounded-work-orchestrator
description: Decompose and govern complex initiatives as bounded work with explicit authority, dependencies, state deltas, proof, acceptance, and integration. Use when the user asks to run an agent team or portfolio agency, create work orders, coordinate parallel tasks, establish gates, manage project/task/agent status, reduce an overloaded active frontier, or prevent planning documents and completed orders from accumulating as false project state. Preserve settled truth in shared project state and require evidence before accepting work. Do not activate for a simple task that one agent can complete directly without coordination or delegated authority.
---

# Bounded Work Orchestrator

Coordinate complex work through a small active frontier and durable shared state. Every work unit should have enough boundary to execute independently, enough authority to act safely, and enough proof to integrate without trusting self-report.

## Load the relevant guidance

- Read [references/work-order-contract.md](references/work-order-contract.md) when decomposing work, assigning an owner, or defining authority, outputs, dependencies, and acceptance.
- Read [references/verification-and-frontier.md](references/verification-and-frontier.md) when operating gates, validating work independently, managing task and agent status, or moving settled state out of the active frontier.
- Read both before activating a multi-agent or multi-workstream initiative.

## Core method

1. Establish the canonical mandate, current project state, principal, environments, and existing authority before creating work.
2. Decompose by coherent state change or deliverable. Avoid micro-orders whose coordination costs exceed their independent value.
3. Define each work order’s scope, inputs, dependencies, owner, authority, expected state delta, proof, acceptance, and stop conditions.
4. Activate only orders whose dependencies are satisfied and whose work can proceed without competing edits or contradictory assumptions.
5. Parallelize genuinely independent work. Preserve one accountable owner for integration and any shared decision surface.
6. Require observable proof proportionate to risk. Separate implementation from acceptance when fresh review can expose errors the producing agent is unlikely to see.
7. Write decisions, facts, task state, and evidence into the project’s shared state mechanism. Use documents only when the deliverable itself is a document.
8. Integrate accepted state deltas into the canonical project, resolve conflicts, and move completed orders and settled truth out of the active attention surface.
9. Present humans with the current project, active tasks, agents, blockers, decisions, and gates. Do not make them reconstruct state from a stack of work orders.

## Authority and gates

Treat authorization as scoped by environment and consequence. Broad decision authority in development does not imply authority to deploy, spend money, delete durable data, communicate externally, or change production state.

Use gates where evidence or human judgment changes what may happen next. Do not add ceremonial approvals to reversible low-risk work. Do not bypass a gate merely because an agent reports confidence.

When the environment supports delegation and the user has authorized it, assign bounded work to capable agents. When delegation is unavailable, preserve the same contracts and execute sequentially rather than pretending independent work occurred.

## Frontier discipline

Keep only unresolved decisions, active work, blockers, and near-term gates in the frontier. Completed orders are history; accepted outputs become project state; stable propositions become background truth.

Do not create a new work order to restate existing state, summarize another order, or record every conversational step. Views and summaries should be generated from the shared state rather than stored as another competing source.

Express timing through dependencies, checkpoints, and human decision windows. Do not assume agent elapsed time maps directly to human work time.
