# Quality Checklist Reference

## Scoring Rubric (100 points)

### Content (30 points)
| Check | Points | Deduction |
|-------|--------|-----------|
| All headings are action titles | 10 | -3 per topic-label heading |
| One message per slide | 5 | -3 per multi-message slide |
| Within content limits (≤500 chars, ≤7 bullets) | 5 | -3 per violation |
| Logical SCQA/Pyramid/MECE structure | 5 | -5 if no framework |
| Slide count matches request (±2 枚以内) | 5 | -5 if significantly off |

### Information Sufficiency (25 points)
| Check | Points | Deduction |
|-------|--------|-----------|
| 具体的な数値・データが含まれている | 10 | -3 per slide lacking data where expected |
| ユーザーの要求事項がすべてカバーされている | 10 | -5 per missing requirement |
| 意思決定に必要な比較・根拠が十分にある | 5 | -5 if arguments are superficial |

### Design (25 points)
| Check | Points | Deduction |
|-------|--------|-----------|
| Layout variety (no 3+ consecutive same layout) | 8 | -4 per violation |
| No text-only slides (every slide has structure) | 7 | -3 per text-only slide |
| Consistent theme applied | 5 | -5 if mixed or default |
| Visual hierarchy (headings > body > notes) | 5 | -3 if flat |

### Code Quality (10 points)
| Check | Points | Deduction |
|-------|--------|-----------|
| Valid frontmatter (marp, theme, paginate) | 4 | -4 if missing |
| Proper `---` slide separators | 3 | -3 if broken |
| No raw HTML tables (use Markdown tables) | 3 | -3 per instance |

### Accessibility (10 points)
| Check | Points | Deduction |
|-------|--------|-----------|
| WCAG AA contrast (4.5:1 body text) | 4 | -4 if violated |
| Font size ≥ 22px for body text | 3 | -3 if too small |
| Images have context (alt text or caption) | 3 | -3 per missing |

---

## Score Interpretation

| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | Excellent | Ready to present |
| 80-89 | Good | Minor polish needed |
| 70-79 | Passing | Fix highlighted issues |
| Below 70 | Needs work | Restructure and rewrite |

---

## Before / After Fix Examples

### Example 1: Topic Label → Action Title

**Before (deduction: -5)**
```markdown
# コスト分析
- ツールAは年間100万円
- ツールBは年間150万円
- ツールCは年間200万円
```

**After (full score)**
```markdown
# ツールAが3年TCOで最もコスト効率が高い
- ツールA: 年間100万円 (3年合計 300万円)
- ツールB: 年間150万円 (3年合計 450万円)
- 差額150万円で追加機能への投資が可能
```

### Example 2: Overloaded Slide → Split into Two

**Before (deduction: -5 multi-message, -3 over limit)**
```markdown
# 導入計画と体制
- フェーズ1: 要件定義 (2週間)
- フェーズ2: 開発 (8週間)
- フェーズ3: テスト (4週間)
- フェーズ4: 移行 (2週間)
- PM: 田中
- 開発: 鈴木、佐藤
- QA: 山田
- インフラ: 高橋
```

**After (full score, 2 slides)**
```markdown
# 16週間4フェーズで段階的に導入する

- Phase 1: 要件定義 (2週間)
- Phase 2: 開発 (8週間)
- Phase 3: テスト (4週間)
- Phase 4: 移行 (2週間)

---

# 専任5名体制でプロジェクトを推進する

- PM: 田中 (全体統括)
- 開発: 鈴木、佐藤
- QA: 山田
- インフラ: 高橋
```

### Example 3: Text-Only → Structured Layout

**Before (deduction: -3 text-only)**
```markdown
# 現状の課題は3つに集約される

手動でのデータ連携に工数がかかっている。
エラー発生時の検知が遅れている。
スケーリングに対応できていない。
```

**After (full score, with layout)**
```markdown
<!-- _class: grid-3 -->

# 現状の課題は3つに集約される

<div>

### 工数過多
手動データ連携に月40時間を消費

</div>
<div>

### 検知遅延
エラー検知まで平均4時間のラグ

</div>
<div>

### 拡張限界
データ量2倍で処理時間が4倍に増加

</div>
```

### Example 4: No Framework → SCQA Applied

**Before**: Slides in random order with no narrative arc.

**After**: Reorganized as Situation → Complication → Question → Answer → Evidence → Next Steps. Each heading is an action title.

### Example 5: Missing Frontmatter → Proper Setup

**Before (deduction: -5)**
```markdown
# Title Slide
...
```

**After (full score)**
```markdown
---
marp: true
theme: consulting-light
paginate: true
title: Project Alpha Proposal
---

<!-- _class: center -->

# Project Alpha Proposal
2024-12-15 | Strategy Team
```
