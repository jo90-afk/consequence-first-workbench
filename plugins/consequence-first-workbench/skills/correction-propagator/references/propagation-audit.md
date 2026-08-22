# Propagation audit

## 1. Establish the active baseline

- Identify the canonical source for every affected scope.
- Separate current artifacts from historical copies, exports, caches, and generated output.
- Preserve unrelated user changes.

## 2. Search for literal and semantic dependents

Inspect relevant surfaces:

- source copy and content records;
- code constants, conditionals, and state transitions;
- interface labels, accessibility names, navigation, and responsive variants;
- metadata, social previews, structured data, indexes, and search records;
- schemas, seeds, fixtures, migrations, and stored propositions;
- tests, snapshots, validation rules, and acceptance criteria;
- prompts, instructions, documentation, and project decisions;
- generated builds, exports, packages, and caches at their proper checkpoint.

Search variants, misspellings, aliases, old labels, and conceptual paraphrases when the correction concerns meaning rather than a literal token.

## 3. Classify every candidate

Choose one disposition:

- **correct now** — active state encodes the old assumption;
- **regenerate later** — derived output will update from corrected source at a checkpoint;
- **retain as history** — the occurrence accurately records former state;
- **retain as quotation or source identity** — alteration would falsify evidence;
- **unrelated** — the same term has a different meaning;
- **clarify** — scope cannot be resolved safely from available evidence.

Do not report raw search totals as defects until this classification is complete.

## 4. Apply in dependency order

1. governing decision, proposition, or requirement;
2. canonical source data or content;
3. logic and state transitions;
4. interface and explanatory copy;
5. tests and validation;
6. derived artifacts at the proper checkpoint.

This order prevents a corrected symptom from being overwritten by an unchanged source.

## 5. Verify absence

- Search active scope for the superseded token and meaningful paraphrases.
- Confirm retained occurrences are intentional.
- Check that old behavior cannot still be reached through another route, breakpoint, or state.
- Confirm future generation uses the corrected source.

## 6. Verify coherence

- Ensure labels describe the action that now occurs.
- Ensure tests assert the corrected behavior rather than merely accepting new output.
- Ensure metadata and navigation use current terminology.
- Ensure superseded facts and tasks have left active views while remaining available in history when required.
- Ensure the correction did not erase legitimate distinctions or unrelated uses.

## 7. Report the result

Lead with the durable correction and its scope. Summarize the affected surfaces and validation. Mention retained historical or quoted occurrences only when they could otherwise look like missed defects.
