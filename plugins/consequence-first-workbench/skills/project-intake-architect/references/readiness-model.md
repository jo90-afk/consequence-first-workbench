# Readiness model

## Readiness levels

### Idea

The motivating concept exists, but users, state, outcome, or boundaries remain too ambiguous for coherent implementation.

### Bounded concept

The product outcome, initial user, and excluded adjacent problems are clear. Architecture may still depend on unresolved state, data, or authority decisions.

### Build-ready

The first vertical slice can be implemented without silently inventing product purpose, data ownership, or irreversible architecture. Known uncertainty has an owner and a safe decision point.

### Release-ready

The assembled product has satisfied its applicable integration, operational, security, migration, accessibility, and release conditions. Intake does not confer this status.

## Minimum build-ready state

Record the following in the project’s existing state mechanism:

| Area | Required clarity |
| --- | --- |
| Outcome | The condition the project is intended to produce |
| Users | Primary user, affected roles, and decision authority |
| Boundary | Included first slice and deliberately deferred problems |
| Core flow | Trigger, meaningful action, state transition, and visible result |
| State | Facts, decisions, tasks, or content that must persist |
| Data | Sources, ownership, sensitivity, and history requirements |
| Environment | Development, test, production, device, hosting, and runtime constraints |
| Integrations | Required systems, authority direction, and failure behavior |
| Acceptance | Observable behavior that proves the slice works |
| Unknowns | Open questions, risk, owner, and latest safe decision point |

Do not require a separate artifact for every row. Use the project’s database, configuration, issue system, or established brief.

## Assumptions and defaults

Classify each unresolved item:

- **principal decision** — requires user or accountable-human choice before work crosses the affected boundary;
- **delegated decision** — falls within authority already granted;
- **safe default** — reversible and unlikely to change product purpose;
- **implementation discovery** — can be resolved through code inspection, prototyping, or testing;
- **blocked** — prevents a coherent or authorized next step.

Write defaults as explicit current decisions so they can be revised. Do not convert silence into permanent preference.

## Readiness test

Ask:

1. Can the first slice be stated as an observable state transition?
2. Can the implementing agent identify where state lives and who owns it?
3. Are authorization and environment boundaries explicit?
4. Could an apparently reasonable default cause destructive, private, costly, or externally visible behavior?
5. Are acceptance conditions capable of falsifying the implementation?
6. Are deferred questions genuinely safe to defer?

If the first three answers are yes, the fourth is no, and the final two are yes, begin implementation. Continue intake only where evidence exposes a consequential gap.

## Handoff shape

Provide a concise project-state synthesis rather than a ceremonial requirements document. Include current decisions, open frontier items, and the next executable slice. Preserve provenance for decisions likely to be revisited.
