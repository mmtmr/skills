# Imagegen Prompt Contract

Use this order. The ordering is intentional: semantic structure must enter the model before visual references.

## Prompt template

```text
TASK
Create one high-fidelity [platform] UI proposal for [surface] at [viewport].

PRODUCT PURPOSE
[Primary user job and desired outcome.]

INFORMATION ARCHITECTURE — SOURCE OF TRUTH
[Paste the non-visual IA tree and reading order.]

IMMUTABLE CONSTRAINTS
- [Locked region or behavior]
- [Required entities, copy, and actions]
- Do not [explicitly rejected change]

STYLE SCOPE BY REGION
- [Region]: [target-brand style allowed / structural only / visually immutable]
- [Region]: [scope]

SEMANTIC ANTI-MAPPINGS
- [Target concept] is not [reference-product concept]. Do not reinterpret one as the other.
- Omit this section when the evidence pack records `None identified`.

CONTENT
[Exact or representative product content. Do not borrow content from references.]

TARGET-BRAND STYLE MATRIX
Typography: [families/fallbacks, sizes, weights, leading, tracking, case]
Color strategy: [adopt-reference by default / preserve-current / hybrid, with the explicit user instruction when non-default]
Color: [target-brand product canvas, navigation and content surfaces, text hierarchy, action accent, selection/pointer-over/focus, dividers, semantic feedback]
Spacing and density: [rhythm, gutters, row/control heights]
Geometry: [radius scale by component, borders, shadows]
Components: [navigation, primary input/action area, repeated content, containers, actions, controls, iconography]
States and motion: [pointer-over, selected, focus, loading, transitions]
Do: [supported distinctive traits]
Do not: [marketing-only or unsupported traits]

ATTACHMENT ROLES
1. [filename] — IMMUTABLE VISUAL REGION / EDIT TARGET. Preserve [specific region] including geometry, content, typography, color, and spacing; modify only [allowed region].
2. [filename] — TARGET-BRAND VISUAL GRAMMAR. Learn [typography/component traits]. Do not copy its content, logos, navigation, or page layout.
3. [filename] — TARGET-BRAND VISUAL GRAMMAR. Learn [different state/trait]. Do not copy its content, logos, navigation, or page layout.
4. [filename] — ADJACENT INTERACTION PATTERN ONLY. Learn [interaction]. Do not copy brand styling or IA.

COMPOSITION AND QUALITY
- Make the hierarchy legible at actual size, not only as a thumbnail.
- Treat typography as the primary hierarchy system.
- Use the documented radius scale; do not round every container.
- Preserve dense product utility where the IA requires it.
- Produce a coherent real application screen, not a mood board or marketing landing page.

NEGATIVE CONSTRAINTS
- Do not change the IA based on any screenshot.
- Do not invent extra navigation regions, tabs, cards, or floating controls.
- Do not import reference copy, names, data, logos, or trademarks.
- Do not reproduce an earlier generated proposal unless explicitly asked to edit it.
- Do not add gradients, glass effects, oversized pills, or excessive whitespace without evidence.
- Do not apply target-brand styling outside the regions permitted by STYLE SCOPE BY REGION.
- Under `adopt-reference`, do not retain the current product's colors merely because they appear in a structural reference screenshot.

OUTPUT
One polished UI proposal image. No explanatory annotations inside the image unless requested.
```

## Attachment budget

Imagegen accepts a limited reference set. Use at most five images and make every slot do a distinct job.

Recommended allocation:

1. target-brand product screenshot showing shell and typography;
2. target-brand product screenshot showing the relevant component/state;
3. target-brand or adjacent screenshot showing density and interactions;
4. current product screenshot with one unambiguous role: `structural invariant` when restyling is allowed, or `immutable visual region` as the edit target when pixels are locked;
5. one high-value adjacent-pattern screenshot.

If only one true target-brand product screenshot exists, attach it and state the limitation. Marketing imagery cannot satisfy the product-image gate unless product UI is inaccessible and the user explicitly accepts the fallback; even then it cannot justify product-shell geometry.

## Iteration protocol

For each revision:

1. preserve the approved IA and accepted regions;
2. name the single main defect being corrected;
3. retain the same evidence pack unless new evidence is required;
4. change only the prompt sections affected by that defect;
5. attach the previous proposal only when performing a controlled edit.

This keeps iteration causal: the reviewer can tell which instruction produced which visual change.
