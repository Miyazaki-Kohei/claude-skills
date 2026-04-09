# Marp Advanced Features Reference

## Directives

Directives control slide-level and deck-level settings via HTML comments.

### Global Directives (in frontmatter)
```yaml
---
marp: true
theme: consulting-light
paginate: true
header: "Company Name"
footer: "Confidential"
---
```

### Scoped Directives (single slide only, use underscore prefix)
```markdown
<!-- _class: center -->
<!-- _backgroundColor: #1a1a2e -->
<!-- _color: #ffffff -->
<!-- _header: "" -->
<!-- _paginate: false -->
```

Without underscore, a directive applies to the current slide AND all subsequent slides.

---

## Layout Classes

Apply via `<!-- _class: classname -->`:
- `center` — Centered title/divider
- `split` — 50/50 two columns
- `split-right` — 40/60 two columns
- `grid-2` — Two card columns
- `grid-3` — Three card columns
- `vs` — VS comparison
- `quote` — Large centered message
- `kpi` — Metric highlight boxes

See `references/layouts.md` for full examples.

---

## Image Syntax

### Inline Images
```markdown
![w:400](path/to/image.png)
![w:300 h:200](path/to/image.png)
```
- `w:` = width, `h:` = height
- Supports CSS units: px, em, %, etc.

### Background Images
```markdown
![bg](path/to/background.jpg)
![bg left:40%](path/to/image.jpg)
![bg right:50%](path/to/image.jpg)
![bg contain](path/to/image.png)
![bg fit](path/to/image.png)
```

### Image Filters
```markdown
![bg blur:5px](image.jpg)
![bg brightness:0.7](image.jpg)
![bg opacity:0.3](image.jpg)
![bg grayscale:1](image.jpg)
```

Combine filters:
```markdown
![bg blur:3px opacity:0.4](image.jpg)
```

---

## Scoped Style Blocks

Override styles for a single slide:

```markdown
<!-- _class: center -->

<style scoped>
h1 { color: #e94560; font-size: 48px; }
p { font-size: 24px; }
</style>

# Custom styled heading

Smaller subtitle text
```

Scoped styles only apply to the slide they appear on.

---

## Auto-fitting Text

Use the `<!-- fit -->` comment inside a heading to auto-scale text:

```markdown
# <!-- fit --> This long heading will shrink to fit the slide width
```

Use sparingly — if you need `fit`, the heading is probably too long.

---

## Speaker Notes

Speaker notes are HTML comments placed at the end of a slide:

```markdown
# Slide heading

- Content here

<!--
Speaker notes:
- Mention the Q2 data specifically
- Ask for budget approval
- Transition to next topic by referencing the timeline
-->
```

Notes appear in presenter view when using `marp -s` (server mode).

---

## Multi-slide Background

Set a background that persists across slides (no underscore):

```markdown
<!-- backgroundColor: #f5f6fa -->
```

This applies to the current slide and all following slides until overridden.

---

## Header / Footer

```yaml
---
header: "**Project Alpha** | Strategy Review"
footer: "Confidential — Internal Use Only"
---
```

Override per slide:
```markdown
<!-- _header: "" -->
<!-- _footer: "Appendix" -->
```

Markdown formatting works in headers and footers.

---

## Page Numbers

```yaml
---
paginate: true
---
```

Hide on specific slides (e.g., title slide):
```markdown
<!-- _paginate: false -->
```

Style via CSS:
```css
section::after {
  font-size: 14px;
  color: var(--color-muted);
}
```

---

## Tables

Use standard Markdown tables:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Data A   | Data B   | Data C   |
| Data D   | Data E   | Data F   |
```

Avoid tables wider than 4 columns or deeper than 6 rows — they overflow on slides.
For complex data, use multiple slides or visual layouts (grid-2, kpi) instead.

---

## Math (KaTeX)

Inline: `$E = mc^2$`
Block:
```markdown
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$
```

---

## Exporting

```bash
# HTML (default, best quality)
uv run python -m scripts.build decks/my-deck/deck.md --format html

# PDF (requires Chrome/Chromium)
uv run python -m scripts.build decks/my-deck/deck.md --format pdf

# PPTX (limited CSS support)
uv run python -m scripts.build decks/my-deck/deck.md --format pptx

# PNG (one image per slide, good for review)
uv run python -m scripts.build decks/my-deck/deck.md --format png
```

HTML and PDF preserve all CSS layouts. PPTX may degrade complex CSS Grid layouts.
