# Validation cadence

Select validation by stage and blast radius. More tests do not automatically produce more information.

## Iteration checks

Run these after each relevant change when available and useful:

- syntax, parse, or compilation checks for edited files;
- focused lint or type checks for the affected module;
- targeted unit or regression tests for the behavior;
- schema, migration, fixture, or data-integrity checks;
- a focused server request, command, or component render;
- visual inspection at the affected viewport and state.

Do not run every category mechanically. Choose checks capable of falsifying the change.

## Integration checks

Use broader checks when an increment crosses boundaries such as:

- client and server;
- schema and application logic;
- authentication and authorization;
- multiple routes or shared components;
- background jobs and user-visible state;
- external integrations and retries.

Run the smallest integration path that crosses the changed boundary. Expand when failures or blast radius warrant it.

## Release checkpoint

At an explicit release checkpoint, perform the project’s applicable gate:

- broader regression suite;
- full type or lint pass;
- production build;
- migration rehearsal or compatibility check;
- responsive and accessibility checks across affected surfaces;
- packaging, version update, checksums, or deployment verification.

Do not pay this cost on every UI adjustment. A checkpoint is the moment to prove the assembled change set, not a substitute for targeted evidence during development.

## Known-dead tests

Treat a test path as known-dead when prior attempts establish that it predictably hangs, times out, cannot reach a dependency, or cannot start in the current environment.

Retain enough context to avoid repeating it:

- command or validation path;
- observed failure mode;
- relevant environment constraint;
- condition that would justify another attempt.

Do not run the path again merely for ceremony. Reconsider it when the environment changes, the test itself changes, the implicated code path changes in a way that may resolve the failure, or the user explicitly requests it.

Use a safer available proxy when it provides real evidence: targeted unit coverage, syntax and data checks, static inspection, a deployed canonical instance, or a rendered artifact. Label the proxy accurately.

## Timeouts and failures

A timeout is an observation, not a diagnosis. Determine whether the product failed, the test harness failed, a dependency was unavailable, or the environment cannot support the path.

When a command stalls:

1. stop it within a bounded interval;
2. preserve useful output;
3. explain the limitation plainly;
4. select a narrower check or continue with the unverified surface disclosed.

Do not leave the user without an update while repeatedly retrying the same blocked path.

## Claims justified by evidence

Report validation at its real scope:

- “syntax and targeted regression passed”;
- “the affected mobile state was visually inspected”;
- “the full suite was not run at this iteration”;
- “browser automation remains unavailable in this environment.”

Avoid “fully tested,” “production-ready,” or “fixed everywhere” unless the completed gate warrants the claim.
