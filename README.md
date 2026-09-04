# Consequence-First Workbench

A public Codex marketplace for work in which decisions, evidence, state, prose, interfaces, and implementation depend on one another.

## Install

```sh
codex plugin marketplace add jo90-afk/consequence-first-workbench
codex plugin add consequence-first-workbench@consequence-first-workbench
```

Start a new Codex or Work conversation after installation so the skills load.

## Included skills

- Editorial Voice Architecture
- Argument Architecture
- Consequence-First Design
- Iterative Software Builder
- Canonical State Manager
- Correction Propagator
- Project Intake Architect
- Evidence & Lineage Researcher
- Model-to-Interface Translator
- Manuscript Steward
- Bounded Work Orchestrator

## Suggested tests

1. `A customer can now pause a subscription instead of cancelling it. Trace every state, task, message, metric, and interface that should change.`
2. `The deployed application is canonical, but this older repository contains one missing report. Recover only that report without regressing later behavior.`
3. `I want an internal tool for reviewing supplier risk. Ask only what you need to make it build-ready.`
4. `Map this strategy paper’s claims, show which ones repeat, and identify the exact evidence each contestable claim needs.`
5. `Implement the approved workflow change in this dirty worktree, validate the affected behavior, and leave release packaging for the checkpoint.`

More detailed positive and negative activation cases are included in [`plugins/consequence-first-workbench/submission/test-cases.md`](plugins/consequence-first-workbench/submission/test-cases.md).

Automated distribution checks and the host-observation evaluation procedure are
documented in [Distribution assurance](assurance/README.md). GitHub Actions checks
the manifests, versions, resources, and evaluation harness. Actual skill activation
and reasoning require recorded host evidence; a passing build does not establish them.

## Public scope

This distribution is author-neutral and domain-neutral. It contains generalized methods and public-safe examples only. Private source material is not part of the repository.

## Status

Version 1.0.0 is ready for public installation and testing.
