# Layout Patterns Reference

All layouts are activated via `<!-- _class: classname -->` in the slide comment.
Each layout works with all three themes (consulting-light, consulting-dark, minimal).

---

## 1. center

Title slides, section dividers, closing slides.

```markdown
<!-- _class: center -->

# Deck Title Here

## Subtitle or date
```

When to use: First slide, last slide, section break slides. Avoid for content-heavy slides.

---

## 2. split

50/50 left-right layout. Heading spans full width, then two content areas side by side.

```markdown
<!-- _class: split -->

# Action title stating the key insight

<div>

## Left Column
- Point A
- Point B
- Point C

</div>
<div>

## Right Column
- Data X
- Data Y
- Data Z

</div>
```

When to use: Text + visual, explanation + evidence, current state + target state.

---

## 3. split-right

Left narrow (40%), right wide (60%). Good for label + detail pattern.

```markdown
<!-- _class: split-right -->

# Action title stating the takeaway

<div>

### Context
Brief background on the left side

</div>
<div>

### Key Details
- Detailed point 1 with supporting data
- Detailed point 2 with evidence
- Detailed point 3 with metrics

</div>
```

When to use: When right content needs more space (charts, detailed lists).

---

## 4. grid-2

Two equal card-style columns with background. Ideal for A vs B comparison.

```markdown
<!-- _class: grid-2 -->

# Both approaches have distinct trade-offs

<div>

### Option A
- Advantage 1
- Advantage 2
- Risk: implementation complexity

</div>
<div>

### Option B
- Advantage 1
- Advantage 2
- Risk: higher ongoing cost

</div>
```

When to use: Comparing two options, before/after, pros/cons.

---

## 5. grid-3

Three equal columns. Good for process steps or triple comparison.

```markdown
<!-- _class: grid-3 -->

# Implementation proceeds in three phases

<div>

### Phase 1
Design & prototype
4 weeks

</div>
<div>

### Phase 2
Development & test
8 weeks

</div>
<div>

### Phase 3
Rollout & monitoring
4 weeks

</div>
```

When to use: 3-step processes, 3-option comparison, category breakdowns. Keep text short per column.

---

## 6. vs

Head-to-head comparison with a visual divider. Three children: left card, "VS" label, right card.

```markdown
<!-- _class: vs -->

# Cloud migration reduces cost by 40% vs on-premise

<div>

### On-Premise
- Annual cost: $2.4M
- Scaling: manual
- Uptime: 99.5%

</div>
<div>

**VS**

</div>
<div>

### Cloud
- Annual cost: $1.4M
- Scaling: auto
- Uptime: 99.99%

</div>
```

When to use: Direct two-option comparison where you want visual emphasis on the contrast.

---

## 7. quote

Large centered message for emphasis. Use for key questions, bold statements, or key takeaways.

```markdown
<!-- _class: quote -->

# We must decide now: build or buy?

The cost of inaction exceeds the cost of either option by Q3.
```

When to use: SCQA "Question" slide, key takeaway slides, executive attention-grabbers.
Keep to 1-2 sentences max. The layout centers everything with large text.

---

## 8. kpi

Metric highlight boxes with large numbers. Each `<div>` becomes a card with a colored top border.

```markdown
<!-- _class: kpi -->

# Q3 results exceeded all targets

<div>

**+23%**
<span>Revenue growth YoY</span>

</div>
<div>

**$4.2M**
<span>New contract value</span>

</div>
<div>

**98.5%**
<span>Customer retention</span>

</div>
```

When to use: KPI dashboards, executive summaries, progress reports. Use 2-4 metric boxes.
Put `<strong>` for the number and `<span>` for the label.

---

## Layout Variety Rule

Never use the same layout class for 3 or more consecutive slides.
The lint script enforces this automatically.

Good pattern example for a 10-slide deck:
```
center → split → split → grid-2 → quote → split → kpi → grid-3 → split → center
```

---

## Combining Layouts with Background Images

Layouts can be combined with Marp's `![bg]` syntax:

```markdown
<!-- _class: split -->

# Customer satisfaction improved by 15 points

<div>

- NPS: 42 → 57
- Churn reduced by 8%
- Response time halved

</div>
<div>

![bg right:50%](assets/satisfaction-chart.png)

</div>
```

For background images on center slides:
```markdown
<!-- _class: center -->

![bg opacity:0.3](assets/hero.jpg)

# Bold Statement Here
```
