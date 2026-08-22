# Translation method

## 1. Inventory the model

Identify only distinctions the interface may need to express:

- entities, propositions, or content units;
- relationships and dependency direction;
- definitions, evidence, implications, and boundaries;
- current, uncertain, contradictory, superseded, and historical state;
- actions and the state transitions they cause;
- attention level, urgency, and timing;
- user role, authority, and visibility;
- stable position or reading context.

Separate model importance from interface prominence. A foundational fact may be structurally important while requiring little daily attention.

## 2. Define the user frame

For each stage, state:

- what the user already knows;
- what they need to understand now;
- what decision or action is available;
- what supporting detail may remain hidden;
- what context must persist after the action.

Do not present the entire ontology merely because the system stores it.

## 3. Assign interface roles

Map semantic types to stable treatments. Exact components depend on the product, but the distinctions should remain consistent.

| Semantic role | Interface responsibility |
| --- | --- |
| Orientation | Explain where the user is and what state governs the view |
| Primary material | Occupy the main reading or working surface |
| Definition or prior knowledge | Establish a frame before dependent claims or actions |
| Evidence | Remain traceable to the claim it supports without competing with it |
| Implication | Show what follows from accepted state |
| Current action | Remain visible and executable at the relevant moment |
| Attention item | Explain the changed condition and why attention is required |
| History | Remain inspectable without appearing active |
| Navigation | Preserve location and expose meaningful movement through the structure |

Do not represent definition and exploration, evidence and argument, or active and historical state with equal visual weight.

## 4. Choose a relational form

Use:

- hierarchy for containment, priority, or levels of abstraction;
- sequence for process, guided movement, or causal order;
- a state view for transitions and available actions;
- a graph or spatial map for topology that cannot be understood linearly;
- a table for exact repeated-field comparison;
- progressive layers for optional evidence, commentary, or advanced control;
- continuous text when reading itself is the primary activity.

Avoid graphs whose edges add no usable meaning and dashboards whose panels merely repeat stored categories.

## 5. Build the attention sequence

For a major state change:

1. synthesize the changed environment in plain language;
2. show the few actions now required;
3. expose dependencies, evidence, and history on demand;
4. allow completed action to update state immediately.

For a reader:

1. keep the text central;
2. introduce necessary prior knowledge before dependent passages;
3. expose metatext and evidence as optional supporting layers;
4. preserve reading position across navigation and responsive reflow.

For a builder:

1. keep the current object and relevant controls together;
2. transform controls as state changes;
3. prevent persistent navigation from covering primary actions;
4. show consequences of edits without turning every property into a permanent panel.

## 6. Translate responsively

Preserve capabilities and semantic order while changing layout:

- follow the viewport with essential controls only when they remain unobtrusive;
- collapse supporting material before shrinking primary material into a portal;
- ensure menus, pills, toolbars, and bottom controls have non-overlapping safe areas;
- retain keyboard, screen-reader, focus, label, and contrast affordances across breakpoints;
- encode position in durable state or URL when return and sharing require it;
- test real content density rather than empty mock states.

Responsive parity means equivalent access and meaning, not identical geometry.

## 7. Specify observable behavior

Describe each critical interaction as:

> user action → state transition → visible result → persisted consequence

This makes the interface implementable and testable without reducing the model to screenshots.

