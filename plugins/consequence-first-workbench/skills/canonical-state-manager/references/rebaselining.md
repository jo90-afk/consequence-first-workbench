# Directional rebaselining

Use this procedure when several artifacts make plausible claims to current state.

## 1. Split the scopes

Canonicality may differ across:

- source code;
- generated build;
- deployed behavior;
- database content;
- schema;
- editorial content;
- private configuration and secrets;
- design decisions and requirements;
- packaged release artifacts.

Do not crown one archive authoritative for every scope merely because it is the most complete package.

## 2. Inventory candidates

For each relevant candidate, record:

| Field | Purpose |
| --- | --- |
| Identity | Exact file, build, deployment, branch, or state store |
| Claimed scope | What kind of state it could govern |
| Version or marker | Explicit version information, if any |
| Effective time | When its state was intended to apply |
| Authority evidence | User declaration, release record, deployed use, or other evidence |
| Completeness | Missing or generated portions |
| Conflicts | Decisions or behavior inconsistent with other candidates |

Do not use timestamps as a substitute for authority. Copies, exports, generated packages, and restored backups routinely acquire misleading modification times.

## 3. Select the baseline

Use this order of reasoning:

1. explicit user declaration for the relevant scope;
2. an already established canonical source in project instructions or state;
3. a verified release or deployment record for the relevant scope;
4. internal version and lineage evidence;
5. timestamps and apparent completeness as secondary clues.

If the remaining ambiguity would change the work materially, ask a focused question. If the user has already declared the baseline, proceed.

## 4. Freeze lineage direction

Record a simple relation:

> historical candidates → canonical baseline → verified successors

Historical candidates can be inspected. They cannot silently contribute changes to the baseline.

When useful, fingerprint the exact baseline with an existing version marker or checksum. A fingerprint proves identity, not authority.

## 5. Classify differences

Classify each difference before acting:

- **current decision**: intentional state present in the canonical baseline;
- **forward candidate**: a requested new change compatible with current decisions;
- **regression**: older behavior that reverses a later decision;
- **omission**: required material absent from the baseline and still applicable;
- **environment-only**: deployment state that should not enter a distributable artifact;
- **secret**: private material that must remain separated;
- **generated**: build, cache, vendor, or derived output;
- **unverified**: a difference whose authority or applicability is unknown.

An omission does not authorize wholesale merge from the artifact that contains it. Recover the missing item as a forward candidate and test it against later state.

## 6. Produce the successor

- Start from the canonical baseline.
- Apply only approved forward changes.
- Preserve version and identity conventions.
- Update the existing state marker or manifest.
- Keep private configuration and secrets separated.
- Generate builds and packages only at the appropriate checkpoint.

## 7. Verify

Check that:

- the intended delta is present;
- later decisions remain intact;
- superseded labels, copy, behavior, and data have not returned;
- schema and content versions agree where required;
- generated output comes from the successor rather than an older working tree;
- the declared canonical source and successor are still identifiable.

## Reconstitution from a deployed artifact

When the user designates a deployed site or running system as canonical, inspect it as evidence of current behavior and content. Reconstruct local source around that state. Use older packages only to recover implementation candidates, then compare each candidate to the deployed behavior and later decisions. A successful reconstruction reproduces the canonical experience and creates a forward-maintainable source; it does not recreate an arbitrary older archive.

