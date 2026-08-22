---
name: project-intake-architect
description: Turn a rough product, software, service, research, or internal-tool idea into sufficient canonical project state for coherent implementation. Use when starting or bootstrapping a project, designing a setup wizard, repairing an incomplete brief, establishing Gate 0, or deciding whether enough is known to build a full product. Resolve users, outcomes, boundaries, states, data, integrations, permissions, environments, constraints, authority, acceptance conditions, and material unknowns through a small adaptive intake. Do not activate for open-ended brainstorming with no intent to define a project, or when an already complete specification answers the material questions.
---

# Project Intake Architect

Reduce the uncertainty that would force architecture, behavior, or product purpose to be guessed during implementation. Produce usable project state, not a long intake document.

## Load the relevant guidance

- Read [references/adaptive-intake.md](references/adaptive-intake.md) when interviewing the user, designing a setup wizard, or identifying missing decisions.
- Read [references/readiness-model.md](references/readiness-model.md) when synthesizing answers, recording project state, or deciding whether implementation can begin.
- Read both for a new product or a project whose current brief has repeatedly produced rework.

## Core method

1. Inspect existing project state, prior decisions, artifacts, and user-provided context before asking questions. Never ask for information already available.
2. State the proposed project outcome in plain language and surface any consequential interpretation you are making.
3. Identify the smallest set of unresolved questions whose answers could change architecture, scope, data ownership, user experience, permissions, or acceptance.
4. Ask adaptively. Prefer one coherent cluster at a time, using concrete options when they clarify a real decision and free text where the user’s own framing is necessary.
5. Distinguish decisions the principal must make from defaults the agent may safely choose and discoveries that can wait for implementation.
6. Translate answers into the project’s existing machine-readable state, configuration, database, brief, or issue system. Avoid creating parallel documents that will drift.
7. Record assumptions as assumptions, unresolved risks as bounded questions, and delegated authority with its limits.
8. Declare the project build-ready when the first coherent vertical slice can be implemented without silently inventing product purpose or irreversible architecture.

## Intake discipline

Do not ask every possible product question. A complete questionnaire can still leave the consequential ambiguity untouched. Order questions by the cost of guessing wrong.

Do not force the user to make low-level implementation choices the agent can safely derive from existing constraints. Do not hide a product, privacy, financial, or authorization decision inside an implementation default.

When the user authorizes broad decisions in a development environment, preserve separate authority for test, production, external communication, destructive operations, and other consequential transitions unless they explicitly delegate those as well.

## Handoff

Conclude intake with:

- the canonical project outcome and boundaries;
- the users and core flow;
- the state and data the product must preserve;
- environments, integrations, and authority;
- acceptance conditions for the first slice;
- unresolved items with an owner and the latest safe decision point.

Keep the synthesis short enough to govern work. Store detail where the project will actually use it.
