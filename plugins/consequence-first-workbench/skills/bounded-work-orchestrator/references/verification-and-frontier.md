# Verification and frontier management

## Proof design

Choose evidence capable of disproving the owner’s claim:

- targeted tests or reproducible behavior for software;
- source records and claim mapping for research;
- rendered artifacts and structural checks for documents;
- before-and-after state plus dependency checks for data changes;
- traceable decisions and acceptance conditions for planning work;
- independent review when interpretation, integration, or hidden assumptions dominate risk.

Self-description is not proof. A report that says “implemented” or “reviewed” must point to observable state.

## Independence

Fresh review is useful when:

- the producer selected the evidence or interpreted ambiguous results;
- several components must integrate;
- a subtle regression could survive narrow tests;
- the work affects production, safety, privacy, money, publication, or external communication;
- the acceptance criterion contains judgment rather than a deterministic check.

Independence does not require a separate agent for every task. It requires a validation perspective that does not merely repeat the producer’s conclusion. When independent delegation is unavailable, use deterministic checks, fresh artifact inspection, or explicit human review and state the limitation.

## Gate design

Use a gate when crossing a boundary such as:

- intake to authorized implementation;
- development to test;
- test to production;
- draft to approved manuscript;
- local evidence to public claim;
- reversible experiment to durable migration;
- internal plan to external communication or spending.

Define:

- entry conditions;
- required evidence;
- decision owner;
- allowed outcomes: accept, rework, block, narrow, or stop;
- state changes caused by each outcome.

Avoid gates that merely rename ordinary task completion.

## Active frontier

Keep active:

- unresolved decisions with near-term consequences;
- ready, active, blocked, proof, and rework orders;
- current integration conflicts;
- evidence awaiting acceptance;
- upcoming gates requiring human judgment.

Move out of active attention:

- accepted orders;
- canceled and superseded orders;
- stable decisions and propositions;
- evidence already incorporated into canonical state;
- summaries that can be regenerated.

Historical state remains queryable. It should not compete visually or operationally with current work.

## Integration

Before accepting a state delta:

1. confirm the order used canonical inputs;
2. inspect proof at its real scope;
3. identify shared interfaces affected by the change;
4. reconcile conflicts with later accepted work;
5. update canonical project state;
6. invalidate obsolete tasks and assumptions;
7. activate only necessary successor work;
8. move the order and settled evidence to history or background.

Do not merge an output solely because its isolated tests pass. Integration includes consistency with the project’s current truth and other accepted deltas.

## Human status surface

Provide a concise view of:

- project outcome and current phase;
- active work grouped by status;
- owner and authority for each order;
- blockers and the exact dependency they require;
- proof awaiting acceptance;
- decisions and gates requiring the principal;
- recently accepted state changes;
- material risk or drift.

Avoid activity metrics that reward order count, agent busyness, or document production. Show movement in project state.

## Timing

Represent:

- dependency order;
- expected agent execution window when known;
- human response or approval window;
- external wait conditions;
- release or calendar deadlines.

Do not translate agent speed into human-equivalent duration mechanically. State assumptions and update forecasts from observed execution.
