# Consulting Frameworks Reference

## Action Titles

Every slide heading must state the **conclusion or insight**, not the topic label.
The audience should understand the message by reading only the headings.

### Transformation Examples (Japanese)

| Bad (Topic Label) | Good (Action Title) |
|---|---|
| 市場分析 | 国内SaaS市場は年率15%で拡大している |
| コスト比較 | ツールAはBより初期費用が40%低い |
| 課題 | 現行システムの保守コストが利益を圧迫している |
| 提案 | 段階的移行により年間2000万円の削減が可能 |
| スケジュール | 3フェーズ16週間で本番稼働を目指す |
| リスク | ベンダーロックインが最大のリスク要因である |
| 組織体制 | 専任チーム3名体制で推進すべき |
| 次ステップ | まず2週間のPoCで技術検証を行う |
| 成果 | Q3実績は全KPIで目標を上回った |
| 背景 | 法規制の変更により対応が急務となっている |

### Rules
- Max 40 characters (Japanese) / 50 characters (English)
- Must contain a verb or assertion (not just a noun phrase)
- Should be self-contained: the message should be clear without reading the body

---

## SCQA Framework

**Situation → Complication → Question → Answer**

Use for: proposals, problem-solving, new initiative presentations.

The audience follows a logical story: "Here's where we are → Here's the problem → Here's what we need to decide → Here's what we recommend."

### 10-Slide Outline Example

| # | Layout | Action Title Example |
|---|--------|---------------------|
| 1 | center | (Deck title + date + presenter) |
| 2 | center | 結論: 運用安定性を最優先にツールAを導入すべき |
| 3 | split | 現在3つのETLツールが市場で主流となっている (Situation) |
| 4 | split | 現行の手動運用はデータ量増加に耐えられない (Complication) |
| 5 | quote | どのETLツールを採用すべきか？ (Question) |
| 6 | center | ツールAが運用安定性・コストの両面で最適である (Answer) |
| 7 | grid-2 | ツールAは導入実績と保守性で他を上回る (Evidence 1) |
| 8 | vs | コスト比較ではツールAが3年TCOで30%有利 (Evidence 2) |
| 9 | kpi | 導入効果: 工数50%削減、エラー率80%低減 (Evidence 3) |
| 10 | split | 来週PoCを開始し、4週間で評価完了を目指す (Next Steps) |

### Flow
- Slide 2 (Executive Summary): State the conclusion upfront. Busy executives get the answer immediately.
- Slides 3-4 (Situation + Complication): Build context. Why now? What changed?
- Slide 5 (Question): Frame the decision point explicitly.
- Slide 6 (Answer): Restate the recommendation clearly.
- Slides 7-9 (Evidence): Support with data. Each slide = one argument.
- Slide 10 (Next Steps): Concrete actions with owners and timelines.

---

## Pyramid Principle

**Conclusion first, then supporting arguments.**

Use for: executive summaries, decision support, board presentations.

The audience gets the answer immediately, then can drill into supporting logic as needed.

### 5-Slide Outline Example

| # | Layout | Action Title Example |
|---|--------|---------------------|
| 1 | center | (Deck title + date) |
| 2 | quote | クラウド移行により年間4000万円の削減が見込める |
| 3 | split | インフラ費用は移行後2年で60%削減される (Argument 1) |
| 4 | split | 運用工数は自動化により月80時間の削減が可能 (Argument 2) |
| 5 | kpi | セキュリティとSLAの両面で現行水準を維持できる (Argument 3) |

### Rules
- Each supporting slide covers ONE argument only
- Arguments should be MECE (see below)
- 3 supporting arguments is the ideal number (max 5)
- Supporting arguments can have sub-arguments on additional slides if needed

---

## MECE Principle

**Mutually Exclusive, Collectively Exhaustive**

Use for: evaluation criteria, option analysis, categorization.

Ensures that categories don't overlap (ME) and cover all possibilities (CE).

### Evaluation Matrix Example

When comparing options, define 3-5 evaluation criteria and score each option:

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| Cost (3yr TCO) | 30% | A | B | C |
| Ease of migration | 25% | A | B | C |
| Vendor reliability | 20% | A | B | C |
| Feature coverage | 15% | A | B | C |
| Team familiarity | 10% | A | B | C |

### 8-Slide Comparison Outline

| # | Layout | Purpose |
|---|--------|---------|
| 1 | center | Title |
| 2 | grid-3 | Evaluation criteria overview (3-5 dimensions) |
| 3 | split | Option A: strengths and limitations |
| 4 | split | Option B: strengths and limitations |
| 5 | split | Option C: strengths and limitations (optional) |
| 6 | vs | Head-to-head on the most important criterion |
| 7 | quote | Recommendation with rationale |
| 8 | split | Next steps with timeline |

---

## Narrative Arc

Regardless of which framework you use, the deck should tell a story.

1. **Hook**: The first content slide should make the audience care (a surprising fact, a bold conclusion, a clear problem statement)
2. **Build**: Each subsequent slide adds one piece of information that builds toward the conclusion
3. **Climax**: The recommendation or key finding slide is the peak
4. **Resolution**: Next steps give the audience a clear path forward

Avoid: slides that don't advance the narrative, slides that repeat information from earlier slides, slides that introduce tangential topics.
