---
name: brand-grounded-ui-design
description: Research, specify, and generate evidence-backed UI proposals in the visual language of a named product or brand. Use for UI redesigns, brand-flavored interface explorations, imagegen mockups, or requests involving GetDesign, DESIGN.md, Mobbin, reference screenshots, typography, spacing, radius, density, components, or information architecture. Separates product logic from visual references so borrowed screenshots cannot accidentally rewrite the product.
---

# Brand-Grounded UI Design

Create UI proposals from an auditable evidence pack instead of aesthetic guesswork. Freeze the product's information architecture in text, research the target brand's design grammar, then give imagegen a small set of role-labeled visual references.

## Required references

Read these files completely before beginning:

- `references/evidence-pack.md` — research checklist and evidence-pack template
- `references/prompt-contract.md` — imagegen prompt structure and attachment budget

Also read and follow the installed `imagegen` skill. When Mobbin is available, read and follow the installed `mobbin-search` skill.

## Non-negotiable rules

1. Write the information architecture and immutable product constraints before collecting style references.
2. Treat text IA as the semantic source of truth. A reference image never gets to invent navigation, content, hierarchy, or product behavior.
3. Inspect the real current product when it exists. Preserve every region the user asked to keep.
4. Retrieve DESIGN.md into a run-specific evidence directory, never the repository root.
5. Distinguish a product interface from its marketing site. GetDesign often documents the latter.
6. Search Mobbin for the exact brand and for structurally similar products. Download and inspect the original screenshots.
7. Always attach real images from the exact target brand to imagegen. Include actual product UI—not only a landing page—whenever it is accessible. URLs and prose alone do not qualify.
8. Label every attachment's role and explicitly prohibit copying its content or unrelated layout. Use `immutable visual region` for an existing region that must remain visually unchanged.
9. Do not attach an old generated proposal unless editing an approved proposal.
10. Generate a proposal for approval before implementing production UI.
11. Default to the target brand's real product-UI palette. Preserve or hybridize the current product palette only when the user explicitly requests it.

## Workflow

### 1. Freeze the product logic

Inspect the current UI and conversation history. Write a plain-text IA contract using `references/evidence-pack.md`.

Record:

- page purpose and primary user job;
- exact regions and their order;
- navigation hierarchy, entities, and relationships;
- required content and actions;
- states, responsive behavior, and target viewport;
- locked elements that must not change;
- visual problems the proposal should solve.

Resolve contradictions in the conversation explicitly. Do not silently let the most recent screenshot override a verbal constraint such as “preserve the existing navigation.”

Lock `ia.md` and its immutable constraints before style research. Add a revision log with timestamp, reason, and supporting user/current-product evidence. Never revise IA merely because a brand reference looks appealing.

Identify semantic anti-mappings dynamically only when a reference product contains concepts that could be confused with the target product's concepts. Write each as `<target concept> is not <reference concept>`. If no credible collision exists, record `None identified`; never invent mappings or carry mappings over from another run.

### 2. Create the evidence directory

Use a run-specific directory such as:

```text
.context/ui-design/<YYYY-MM-DD>-<surface>-<brand>/
  ia.md
  provenance.md
  target-brand/
  adjacent-products/
  getdesign/
  evidence-pack.md
  prompt.md
  proposal/
```

Keep downloaded sources and generated proposals separate.

### 3. Retrieve and qualify GetDesign evidence

Resolve the brand slug using the current official catalog or `npx getdesign@latest list`. For a public template, run:

```bash
python <skill-dir>/scripts/fetch_getdesign.py <slug> --output <run-dir>/getdesign
```

Resolve `<skill-dir>` from this SKILL.md location; do not assume the caller's working directory is the skill directory.

Do not confuse GetDesign's two inventories:

- `https://getdesign.md/<slug>/design-md` identifies a curated downloadable template;
- `https://getdesign.md/design-md/<slug>` may be only a catalog or request page;
- `https://getdesign.md/design-md/<slug>/preview` is a generated token showcase, not proof of real product UI.

Never claim a DESIGN.md was fetched when the brand is catalog-only, request-only, private, or absent. In that case, record the gap and build the style matrix from the brand's live product imagery and Mobbin. Ask for a licensed/private DESIGN.md only if it is necessary.

Extract these fields into the evidence pack:

- font family, fallbacks, scale, weights, leading, and tracking;
- semantic color roles and contrast relationships;
- spacing rhythm and layout density;
- radius scale and where each radius is used;
- border, divider, shadow, and surface treatment;
- component geometry and control height;
- icon style, imagery, and illustration treatment;
- interaction, focus, pointer-over, selected, loading, and motion behavior;
- explicit do/don't rules.

Flag proprietary fonts and select a defensible fallback. Record whether each rule describes marketing UI, product UI, or both.

Choose one color strategy before imagegen:

- `adopt-reference` — default. Apply the target brand's product-UI color system across every region that is not explicitly visually locked.
- `preserve-current` — use only when the user explicitly asks to retain the target product's existing colors.
- `hybrid` — use only when the user explicitly asks to combine named parts of both palettes.

For `adopt-reference`, extract a complete semantic palette from real product screenshots: canvas, navigation surface, primary and elevated surfaces, primary/secondary/muted text, action accent, selected/pointer-over/focus states, borders, and semantic feedback. Do not reduce a brand to one accent swatch. Marketing colors may supplement this palette only when the product screenshots support them.

### 4. Collect product screenshots

Search Mobbin on the correct platform in this order:

1. exact target brand and relevant product surface;
2. exact interaction pattern, such as navigation/list/detail/composer/search;
3. two or three adjacent products with the same structural problem.

Download originals, save source URLs and screen IDs, and inspect every candidate. Favor screenshots that reveal typography, density, selected states, dividers, control geometry, and the relevant interaction—not dramatic marketing art.

For each selected Mobbin result, archive the returned `image_url` and canonical `mobbin_url` with:

```bash
python <skill-dir>/scripts/download_reference.py \
  --image-url <image-url> \
  --source-url <mobbin-url> \
  --output <run-dir>/target-brand/<descriptive-name>.jpg \
  --screen-id <screen-id> \
  --app-name <app-name>
```

Also capture or locate the current product screenshot when preserving existing regions. If the current screenshot would contaminate style, translate it to text IA and omit it from the final attachment set. Use `structural invariant` when only hierarchy or geometry is locked. Use `immutable visual region` as the imagegen edit target when its styling and pixels must remain unchanged.

When Mobbin is only an evidence substep, do not pause to create a board unless the user explicitly requested one. Grade every result `exact`, `partial`, or `no-match` for both brand and interaction. The correct brand with the wrong surface is not an exact match.

### 5. Complete the evidence gate

Do not call imagegen until the evidence pack contains:

- a complete IA contract;
- explicit immutable constraints;
- at least one inspected exact-target-brand image and, when accessible, one real product UI screenshot;
- a typography specification;
- colors, spacing, radius, borders/shadows, and density;
- component and interaction rules;
- source provenance and uncertainty labels;
- a deliberate attachment manifest.

IA, immutable constraints, and qualifying exact-brand visual evidence are hard blockers. Only noncritical style values may remain unknown; label them as inferred. Never fill gaps with invented brand facts. Marketing-only imagery cannot satisfy the product-image requirement unless real product UI is inaccessible and the user accepts that limitation.

Before generation, verify that every manifest file exists, is a validated image, and has been visually inspected. Pass those exact local paths to imagegen through `referenced_image_paths`; naming files only inside the prompt is insufficient.

### 6. Build and run the imagegen prompt

Follow `references/prompt-contract.md`. Put the IA before the style matrix in the prompt. Name each local attachment and assign exactly one role: `structural invariant`, `immutable visual region`, `target-brand visual grammar`, or `adjacent interaction pattern`.

State that target-brand and adjacent-product screenshots are visual references only. Forbid importing their copy, navigation labels, data, logos, or unrelated page structure.

Use no more than five attachments. Attach at least one real target-brand image; prefer two or three when available. Render typography as a first-class design system, not a decorative afterthought.

When an existing region must remain visually unchanged, use the current screenshot as imagegen's edit target and give it the manifest role `immutable visual region`. Instruct imagegen to modify only the named mutable region. After generation, crop and compare the locked region at original resolution. For an `exactly` or pixel-identical constraint, require a zero-difference comparison. If generative editing changes any locked pixels, do not present the result as compliant: generate only the mutable region for review or ask the user to relax the constraint. Production implementation must reuse the existing region rather than recreate it.

### 7. Review before presenting

Reject and regenerate the proposal if it:

- changes locked navigation or information hierarchy;
- resembles an earlier generated proposal more than the target brand;
- uses generic system typography despite stronger evidence;
- applies one radius everywhere;
- imports marketing gradients or oversized pills into dense product UI without evidence;
- copies reference content or logos;
- omits important states or product actions.

Present the proposal image with a concise explanation of the IA, typography, and reference roles. Request approval before production implementation.

### 8. Archive reproducibly

Save the final prompt, selected references, provenance, fetched DESIGN.md, and proposal together. Reuse the archived DESIGN.md for iteration unless the user explicitly asks to refresh it; `@latest` is mutable.

## Evidence precedence

When sources disagree, use this order:

1. explicit user constraints;
2. verified current-product behavior and locked UI;
3. written IA contract;
4. target brand's real product screenshots;
5. target brand's DESIGN.md product rules;
6. adjacent-product screenshots;
7. marketing-site DESIGN.md rules;
8. clearly labeled inference.

This precedence controls structure as well as style. Never use a lower-ranked source to override a higher-ranked one.

Apply precedence per design dimension. Current-product evidence may outrank references for locked structure or behavior while target-brand product screenshots outrank current-product colors, typography, and surface styling under the default `adopt-reference` strategy. A screenshot does not make all of its visual properties immutable.
