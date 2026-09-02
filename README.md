# mmtmr Skills

Portable skills for Codex.

## Included skills

### Brand-Grounded UI Design

`brand-grounded-ui-design` creates evidence-backed UI proposals in the visual language of a named product or brand. It freezes the target product's semantics and information architecture before gathering visual references, then turns verified target-brand evidence into a style matrix for an approval-ready image-generation proposal.

Its default palette strategy adopts the reference product's product-UI palette. It preserves the current product palette, or uses a hybrid, only when the user explicitly requests that approach.

Prerequisites:

- Codex image generation;
- optional Mobbin access for product-UI reference research;
- Node.js 18 or later when retrieving GetDesign templates.

## Install

Install the skill with the Codex skill installer:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \\
  --repo mmtmr/skills \\
  --path skills/brand-grounded-ui-design
```

The skill becomes available in a new Codex turn after installation.

## License

MIT. See [LICENSE](LICENSE).
