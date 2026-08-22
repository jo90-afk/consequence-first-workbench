# Consequence review

Use this checklist to evaluate a proposal, implementation, or existing stateful experience.

## Trigger clarity

- Is the changed proposition or decision stated precisely?
- Does the model distinguish false, uncertain, and superseded state?
- Are scope and effective time clear?
- Does the design preserve the prior state as history without leaving it active?

## Propagation completeness

Inspect each affected layer:

- stored facts and derived data;
- business rules and permissions;
- dependencies and integrations;
- active tasks and recommendations;
- summaries and explanations;
- interface states and navigation;
- notifications and attention cues;
- tests, documentation, and communications that assert behavior.

A material change that appears only as copy or a dashboard indicator has probably not propagated far enough.

## Invalidation and replacement

- Which existing items became invalid?
- Were they removed from active use rather than merely marked false?
- Which items remain valid for independent reasons?
- What successor tasks, flows, or decisions does the new state require?
- Can a user inspect the change history and causal source?

## Actionability

- Does a major change receive a plain-language synthesis before detail?
- Does every primary warning lead to a decision or action?
- Are tasks executable, current, and tied to their generating premises?
- Can tasks be completed and annotated as soon as they appear?
- Does task completion feed back into state when it should?

## Materiality control

- Has the system followed all behavior-changing consequences?
- Has it avoided generating associations that alter nothing?
- Are low-attention truths kept out of the urgent surface?
- Does uncertainty suspend unsafe derivation instead of creating false precision?

## Failure patterns

- A changed fact becomes a colored node while all dependent work remains intact.
- Obsolete tasks are retained with warning badges.
- Invalid tasks disappear but no successor work is created.
- Every downstream fact produces an alert, leaving the user to reconstruct priority.
- The interface summarizes activity rather than the changed environment.
- A local UI fix leaves data, permissions, documentation, or integrations inconsistent.
- History and active truth share one undifferentiated map.

The review is complete when the new state produces coherent beliefs, behavior, and action across every material consumer.
