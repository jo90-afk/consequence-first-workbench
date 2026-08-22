---
name: model-to-interface-translator
description: Translate conceptual models, argument maps, relational systems, evidence structures, and world-state models into coherent interface hierarchy and interaction. Use for readers, dashboards, builders, maps, guided paths, task systems, and stateful tools where semantic differences need distinct visual treatment, changed state must become action, or responsive behavior must preserve meaning and position. Define experience structure, attention, controls, persistence, and accessibility before or alongside implementation. Do not activate for visual styling with no underlying model or for an already specified implementation whose interface semantics are settled.
---

# Model-to-Interface Translator

Make the model legible through use. Preserve its distinctions in hierarchy, spatial relation, interaction, and state without forcing the user to inspect the model directly.

## Load the relevant guidance

- Read [references/translation-method.md](references/translation-method.md) when turning a model, argument, or state system into an interface specification or prototype.
- Read [references/experience-coherence-audit.md](references/experience-coherence-audit.md) when reviewing an existing interface for semantic loss, attention problems, responsive drift, or action failures.
- Read both before a substantial redesign of a stateful or conceptually dense experience.

## Core method

1. Recover the model’s meaningful objects, relations, state transitions, evidence, history, and boundaries. Do not treat every node as an equal card.
2. Identify what the user is trying to understand, decide, or do at each stage. The interface should reveal the portion of the model needed for that action.
3. Assign stable visual and interaction roles to different semantic types. Definition, evidence, implication, task, warning, history, and navigation should not share one undifferentiated frame.
4. Establish attention order: orient the user, synthesize material change, expose current action, then provide inspectable detail and history.
5. Translate relationships into the smallest useful visual form. Use hierarchy, sequence, spatial position, connection, grouping, or progressive disclosure only when the relation becomes easier to understand.
6. Keep relevant actions available at the moment they become useful. Prevent persistent controls, menus, evidence panels, and mobile navigation from obscuring one another.
7. Preserve meaning across responsive transformations. Mobile and desktop may use different layouts, but must retain equivalent state, accessibility, and capability.
8. Preserve user position and context across reflow, navigation, filtering, and optional supporting layers when continuity is part of the experience.
9. Validate the interface against actual model states, including major change, empty, uncertain, contradictory, completed, error, and historical states.

## Experience principles

Lead with the human consequence of state, not the system’s internal activity. A catastrophic or complex change should become a plain synthesis and a short action surface before it becomes a field of indicators.

Use color, motion, density, and spatial prominence to encode meaning or attention. Do not make the interface look active by making everything visually urgent.

Keep primary material primary. Commentary, evidence, controls, and navigation should support reading or action without shrinking the central work into a decorative viewport.

When implementation is requested, translate the specification into the project’s existing architecture and validate the affected viewports and states. Do not stop at a wireframe if the user authorized a build.
