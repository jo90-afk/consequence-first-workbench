---
name: canonical-state-manager
description: Establish, protect, and advance authoritative state across competing files, builds, deployments, branches, databases, manuscripts, plans, and project versions. Use when the user names a canonical build or baseline, asks to continue or reconstitute prior work, supplies an older artifact, requests rebaselining or version reconciliation, or when current truth could be confused with historical state. Make lineage directional so older artifacts cannot silently merge into the current baseline. Do not activate for a simple edit where one current artifact is unambiguous and no competing state exists.
---

# Canonical State Manager

Treat canonicalization as a directional decision, not a search for the file containing the most material. Once a baseline is established, successors move forward from it. Older artifacts remain history unless a specific item is deliberately reintroduced and revalidated against current state.

## Load the relevant guidance

- Read [references/rebaselining.md](references/rebaselining.md) when choosing among versions, reconciling a deployed and local artifact, reconstituting a build, or declaring a new baseline.
- Read [references/state-ledger.md](references/state-ledger.md) when the project tracks propositions, decisions, facts, supersession, or movement from frontier state into stable background state.
- Read both when an artifact version and the truth it represents can diverge.

## Core method

1. Scope canonicality. Code, content, data, configuration, deployment, and editorial decisions may each have different authoritative sources.
2. Identify candidates and the evidence of authority for each. Do not infer canonicality from filename, timestamp, completeness, or version number alone.
3. Honor an explicit user declaration immediately. If the user says a build or deployed instance is canonical, treat conflicting older material as history.
4. Declare the baseline and lineage direction before merging or reconstructing when ambiguity is material.
5. Apply changes to the canonical baseline or a verified successor created from it.
6. Reintroduce an item from an older artifact only when the item is explicitly selected, still applicable, and verified not to reverse later decisions.
7. Record the resulting state in the project’s existing machine-readable source of truth. Avoid creating parallel standalone ledgers when a database, manifest, configuration, or established state store already serves the function.
8. Verify that the successor contains the intended delta, retains current guarantees, and has not silently restored superseded behavior.

## Authority rules

- The user’s explicit baseline decision outranks metadata.
- A deployed artifact is authoritative when the user designates it as canonical, even if local exports are newer or more complete.
- “Latest modified” and “highest version number” are clues, not decisions.
- A historical artifact may provide provenance or a recovery candidate; it does not gain merge authority from having material absent in the canonical baseline.
- Canonicality is scoped. A deployment may be canonical for interface behavior while a database is canonical for content and a private configuration is canonical for credentials.
- Secrets and environment-only configuration must remain outside distributable artifacts even when they are required to reproduce a deployment.

## Rebaseline directionally

When a new baseline is accepted, name everything before it as history for merge purposes. Future work begins from the new baseline. Do not build a “best of all versions” composite unless the user explicitly commissions reconciliation and approves the items to restore.

If an older artifact is the only recoverable source for a required item, extract that item as a candidate, compare it against every later decision it touches, and introduce it as a new forward change. Never copy the older state wholesale into the canonical artifact.

## Communicate state plainly

When state could be confused, report:

- the canonical source and scope;
- which artifacts are historical or subordinate;
- the intended successor or current version;
- any unresolved ambiguity that could materially alter the result.

Do not ask the user to reconfirm a baseline they have already declared.
