# UI Evidence Pack

Complete this document before calling imagegen. Keep statements concise, testable, and traceable to a source.

## 1. Brief

- Surface:
- Platform and viewport:
- Primary user job:
- Target brand or visual direction:
- Desired outcome:
- Approval artifact:

## 2. Information architecture contract

Describe the product without visual adjectives.

```text
Page
├── Region A — purpose
│   ├── Entity/action
│   └── Entity/action
├── Region B — purpose
└── Region C — purpose
```

- Reading order:
- Navigation model:
- Entity relationships:
- Primary action:
- Secondary actions:
- Content hierarchy:
- Required states:
- Responsive behavior:

### IA lock

- Locked before visual research at:
- Baseline version/hash:
- Reference concepts that could be confused with target-product concepts:
- Semantic anti-mappings generated for this run (`<target concept> is not <reference concept>`), or `None identified`:

| Revision | Time | Change | Supporting user/product evidence |
|---|---|---|---|
| 0 |  | Initial lock |  |

## 3. Immutable constraints

List exact elements that cannot change, including user corrections from the conversation.

- Must preserve:
- Must not introduce:
- May reinterpret visually:
- Current implementation dependencies:

### Style scope by region

| Region | Target-brand styling allowed? | Must remain visually unchanged? | Notes |
|---|---|---|---|
|  |  |  |  |

## 4. Current-UI diagnosis

- What is working:
- What feels weak:
- Typography problems:
- Density and spacing problems:
- Hierarchy problems:
- Interaction problems:
- Accessibility risks:

## 5. Source ledger

For every source record:

| ID | Source | URL/path | Retrieved | Scope | Brand match | Interaction match | Confidence | Useful for | Do not copy |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Current product |  |  | Product | Exact |  | High | Structure | Incidental styling |
| S2 | DESIGN.md |  |  | Product/marketing/mixed | Exact |  |  | Tokens | Unverified layout |
| S3 | Target-brand screenshot |  |  | Product | Exact | Exact/partial/no-match |  | Visual grammar | Copy/data/logo |
| S4 | Adjacent product |  |  | Product | No-match | Exact/partial |  | Interaction pattern | Brand identity |

Mark unavailable, request-only, paywalled, or inferred evidence honestly.

## 6. Style matrix

### Typography

- UI family and fallbacks:
- Display family and fallbacks:
- Sizes and roles:
- Weights:
- Line heights:
- Tracking:
- Case rules:
- Numeric treatment:
- Proprietary-font substitution:
- Evidence IDs:

### Color

- Strategy (`adopt-reference` by default; `preserve-current` or `hybrid` only by explicit request):
- User instruction supporting a non-default strategy:
- Canvas:
- Navigation surface:
- Primary surface:
- Elevated/selected surface:
- Primary text:
- Secondary text:
- Muted text:
- Accent/action:
- Pointer-over/focus/selected states:
- Border/divider:
- Semantic colors:
- Evidence IDs:

### Geometry and density

- Spacing base and rhythm:
- Content width/gutters:
- Row density:
- Control heights:
- Radius scale by component:
- Border widths:
- Shadow/elevation:
- Evidence IDs:

### Components

- Navigation:
- Primary input or action area:
- Repeated content:
- Containers and surfaces:
- Actions:
- Form controls:
- Identity and iconography:
- Status and feedback:
- Evidence IDs:

### Interaction and motion

- Pointer-over:
- Selected:
- Focus:
- Loading/empty/error:
- Transitions:
- Keyboard behavior:
- Evidence IDs:

### Brand grammar

- Distinctive traits to carry over:
- Marketing-only traits to exclude:
- Do:
- Don't:
- Uncertainties/inferences:

## 7. Attachment manifest

Keep the final set to five images or fewer.

| Slot | Local path | Role | What to learn | What to ignore |
|---|---|---|---|---|
| 1 |  | Target-brand visual grammar |  | Copy, data, IA |
| 2 |  | Target-brand visual grammar |  | Copy, data, IA |
| 3 |  | Adjacent interaction pattern |  | Brand identity, IA |
| 4 |  | Immutable visual region | Preserve geometry, content, styling, and pixels | Nothing in the named locked region |
| 5 |  | Optional high-value evidence |  |  |

Selection rules:

- Always include at least one actual target-brand image.
- Prefer complementary states over near-duplicates.
- Use the current product screenshot only when visual preservation cannot be expressed sufficiently in text.
- Use `immutable visual region` when geometry and styling must both remain unchanged; verify the region after generation.
- Use `structural invariant` in another slot only when geometry/hierarchy is locked but visual restyling is allowed.
- Never attach a prior generated mockup unless the task is explicitly an edit of that mockup.

## 8. Readiness decision

- [ ] IA is complete and non-visual.
- [ ] IA and immutable constraints were locked before style research; later changes have evidence in the revision log.
- [ ] Immutable constraints reflect the user's latest corrections.
- [ ] At least one exact-target-brand image was downloaded and inspected.
- [ ] A real target-brand product UI screenshot is included when accessible; marketing-only evidence is labeled.
- [ ] Typography is specified beyond a font-family name.
- [ ] Color strategy is explicit; without contrary user instruction it is `adopt-reference`.
- [ ] The full semantic palette comes from real target-brand product UI, not merely one accent or a marketing page.
- [ ] Spacing, radius, density, borders, shadows, and components are specified.
- [ ] Product and marketing evidence are distinguished.
- [ ] Every claim has a source or an `inferred` label.
- [ ] Each attachment has one explicit role.
- [ ] Every attachment exists locally, passed image validation, was visually inspected, and its exact path will be supplied through `referenced_image_paths`.
- [ ] Every claimed visual trait is supported by its assigned image or labeled inferred.
- [ ] Prompt forbids reference-content and reference-layout leakage.

IA, immutable constraints, and qualifying exact-brand visual evidence are hard blockers. Do not generate while those boxes are unchecked. Noncritical style gaps may proceed only when labeled inferred; inaccessible real product imagery requires explicit user acceptance of a marketing-only fallback.
