# Color System Reference

## 60-30-10 Rule

Professional presentations use color in three tiers:

- **60% Dominant** — Background and large surfaces. Sets the overall tone.
- **30% Secondary** — Cards, panels, table headers. Provides structure.
- **10% Accent** — Highlights, key numbers, CTAs. Draws attention.

Exceeding 6 unique colors in a palette reduces visual coherence.

---

## Theme Catalog

### consulting-light (Default)

Best for: proposals, operational reviews, general business presentations.

| Variable | Value | Role |
|----------|-------|------|
| `--color-bg` | `#ffffff` | Page background (60%) |
| `--color-fg` | `#2d3436` | Body text |
| `--color-primary` | `#f5f6fa` | Card/panel backgrounds (30%) |
| `--color-secondary` | `#dfe6e9` | Borders, table stripes |
| `--color-accent` | `#0984e3` | Highlights, KPI numbers (10%) |
| `--color-alert` | `#d63031` | Warnings, negative metrics |
| `--color-success` | `#00b894` | Positive metrics |
| `--color-muted` | `#636e72` | Captions, footnotes |

### consulting-dark

Best for: strategy decks, executive presentations, M&A materials, keynotes.

| Variable | Value | Role |
|----------|-------|------|
| `--color-bg` | `#1a1a2e` | Deep navy background (60%) |
| `--color-fg` | `#e8e8e8` | Light text |
| `--color-primary` | `#16213e` | Card backgrounds (30%) |
| `--color-secondary` | `#0f3460` | Panel accents |
| `--color-accent` | `#e94560` | Highlights, key data (10%) |
| `--color-alert` | `#ffc048` | Warnings (amber on dark) |
| `--color-success` | `#00b894` | Positive metrics |
| `--color-muted` | `#a0a0b0` | Captions, footnotes |

### minimal

Best for: technical content, data-heavy presentations, internal documentation.

| Variable | Value | Role |
|----------|-------|------|
| `--color-bg` | `#fafafa` | Near-white background (60%) |
| `--color-fg` | `#333333` | Dark gray text |
| `--color-primary` | `#f0f0f0` | Card backgrounds (30%) |
| `--color-secondary` | `#e0e0e0` | Borders |
| `--color-accent` | `#00b894` | Teal highlights (10%) |
| `--color-alert` | `#d63031` | Warnings |
| `--color-success` | `#00b894` | Positive metrics |
| `--color-muted` | `#888888` | Captions |

---

## Topic-to-Theme Mapping

| Topic / Audience | Recommended Theme |
|------------------|-------------------|
| Strategy, M&A, Board | consulting-dark |
| Proposals, Operations | consulting-light |
| Technical, Data, Internal | minimal |
| Finance, Compliance | consulting-dark |
| Marketing, Customer | consulting-light |
| Engineering, DevOps | minimal |

When in doubt, use `consulting-light`.

---

## Custom Accent Override

Override the accent color in a specific deck's frontmatter:

```yaml
---
marp: true
theme: consulting-light
paginate: true
style: |
  :root {
    --color-accent: #6c5ce7;
  }
---
```

This changes all accent-colored elements (headings, KPI numbers, highlights) without modifying the theme file.

---

## WCAG AA Contrast Requirements

- Body text on background: minimum 4.5:1 contrast ratio
- Large text (≥24px or ≥18.67px bold): minimum 3:1
- All three bundled themes meet WCAG AA by default

To verify contrast when customizing:
1. Check foreground color against background color
2. Use any online contrast checker (e.g., WebAIM)
3. Ensure ratio ≥ 4.5:1 for body text
