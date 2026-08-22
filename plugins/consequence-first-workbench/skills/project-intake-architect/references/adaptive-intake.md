# Adaptive intake

## Begin with known state

Recover decisions already made in the current conversation, project artifacts, configuration, issue state, and canonical records. Mark contradictions and stale assumptions. Do not reopen settled decisions merely because a generic intake template contains the question.

## Ask by consequence

Prioritize an unknown when a wrong guess would change:

- who the product serves;
- what successful use accomplishes;
- the core state model or data ownership;
- privacy, permissions, or destructive behavior;
- platform, deployment, or integration architecture;
- the first usable slice;
- operating cost or human workload;
- the definition of acceptance.

Defer questions whose answers can change later without invalidating current work.

## Coverage areas

Use these as a coverage map, not a questionnaire.

### Purpose and outcome

- What condition should become true because the project exists?
- Which current friction, failure, or opportunity does it address?
- What would count as the project solving the wrong problem well?

### Users and authority

- Who uses, administers, approves, or is affected by the system?
- Which decisions belong only to the principal or an accountable human?
- What may agents decide in development, test, and production?

### Core flow and state

- What begins a meaningful session or workflow?
- What state changes during the core action?
- What must persist across devices, sessions, versions, or users?
- Which propositions have downstream consequences?

### Boundaries

- Which use cases are deliberately excluded from the first product?
- Which adjacent systems remain authoritative?
- What must never be inferred, automated, or represented as evidence?

### Data and provenance

- What data enters, where does it come from, and who owns it?
- Which data is sensitive, private, regulated, or user-deletable?
- What history, source, confidence, or change record must be retained?

### Interfaces and platforms

- Which platforms and viewports are required?
- What must work offline, locally, on a private network, or through a hosted service?
- What accessibility or input constraints affect the core flow?

### Integrations

- Which external systems are required for the first slice?
- Which direction does data move, and which system remains authoritative?
- What should happen when an integration is unavailable or stale?

### Environments and operations

- Which development, test, and production environments are required?
- How is seed data separated from personal or production data?
- What administration, debugging, reset, recovery, logging, or backup capability is required?

### Constraints and economics

- What time, budget, hosting, model, device, or infrastructure constraints are real?
- Which recurring costs or human maintenance burdens are unacceptable?
- Which dependencies are already chosen and should not be relitigated?

### Acceptance and release

- What observable behavior proves the first slice works?
- What validation is required during iteration and at release?
- Who accepts the result, and what remains reversible before acceptance?

## Question shape

Ask a small coherent cluster, explain the decision it unlocks, and offer options only when the option set is genuine. Allow the user to answer in their own terms. Synthesize after each cluster so later questions reflect the new state.

Avoid forms that demand exhaustive certainty before the user can see the product. Intake should make implementation responsible, then continue learning through validated increments.

