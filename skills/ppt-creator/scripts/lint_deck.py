from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# Content limits — tuned for the FJ theme (1920x1080, 92px padding).
# The content region is much larger than a 1280x720 deck, so the thresholds
# here are relaxed compared to generic consulting slides.
#
# Visual width is calculated with `**emphasis**` markers stripped, so the
# limits reflect what the reader actually sees on-screen (the bolded segment
# renders the same width whether it's wrapped in `**` or not).
MAX_BULLETS = 9
MAX_BULLET_CHARS = 120
MAX_BODY_LINES = 18
MAX_CONTENT_CHARS = 750
# h1 renders at 48px on a 1920px canvas. Roughly 72 CJK characters (visual
# width 2 each) fit on one line; leaving ~10% margin lands at 66.
MAX_TITLE_CHARS_JA = 66
MAX_TITLE_CHARS_EN = 84
# `small-text` shrinks everything to ~80% so it can hold more per slide.
# Split the multiplier so density (char count) scales more aggressively than
# layout (line count) — dense reference slides need the room, but 30 lines
# crammed into one slide is still unreadable regardless of font size.
SMALL_TEXT_CONTENT_MULTIPLIER = 2.0
SMALL_TEXT_LINES_MULTIPLIER = 1.5
MAX_CONSECUTIVE_SAME_LAYOUT = 2

# card-grid card-count caps. Derived from CSS `grid-template-rows` rules in
# fj.css: cols-2 has row rules up to nth-of-type(7) = 4 rows × 2 = 8 cards,
# cols-3 up to nth-of-type(7) = 3 rows × 3 = 9 cards, cols-4 up to
# nth-of-type(9) = 3 rows × 4 = 12 cards. Going beyond these breaks the
# layout because there's no row rule to match.
CARD_GRID_MAX_CARDS = {
    "cols-2": 8,
    "cols-3": 9,
    "cols-4": 12,
}

# column-layout is designed around 2 or 3 columns. 1 is pointless (use a
# default layout); 4+ crushes the text because each column gets ~400px.
COLUMN_LAYOUT_VALID_COUNTS = {2, 3}

# Allowlist of FJ theme class names. Unknown classes are warned about because
# they almost always indicate a typo ("titie", "columns", ...).
FJ_CLASSES = {
    "title",
    "section",
    "no-header",
    "image",
    "image-shadow",
    "content-image",
    "content-image-right",
    "content-image-left",
    "content-40",
    "content-60",
    "content-70",
    "column-layout",
    "align-center",
    "all-text-center",
    "text-center",
    "all-text-blue",
    "text-blue",
    "all-text-red",
    "text-red",
    "small-text",
    "large-text",
    "card-grid",
    "cols-2",
    "cols-3",
    "cols-4",
}

# Headings that mark a slide as an "agenda" / "table of contents" slide. These
# slides should have crisp, scannable bullets — long sentences defeat the
# purpose. Detected case-insensitively against the slide's first heading.
AGENDA_HEADING_PATTERNS = [
    "本日お伝え",
    "本日お話",
    "お話しすること",
    "お伝えすること",
    "アジェンダ",
    "目次",
    "agenda",
    "本日の流れ",
    "本日の内容",
]

# Max visual width per agenda bullet. CJK chars count as 2, so 30 ≈ 15 kanji.
AGENDA_BULLET_MAX_WIDTH = 30

# Meta-commentary prefixes that tend to leak into generated slides when the LLM
# pattern-matches phrases from the skill documentation. They read as Claude
# narrating about the slide rather than as actual slide content. Detect any
# line that begins with one of these (after whitespace and bullet markers).
META_PREFIX_PATTERNS = [
    "見出しだけ",
    "補足:",
    "補足：",
    "右上ヒント",
    "右下ヒント",
    "左上ヒント",
    "左下ヒント",
    "ヒント:",
    "ヒント：",
    "note:",
    "Note:",
    "NOTE:",
    "メモ:",
    "メモ：",
    "以下のポイント",
    "要点まとめ:",
]

# Patterns that indicate unfinished content — linting as ERROR so the deck
# cannot go out with placeholder text still in it.
PLACEHOLDER_PATTERNS = [
    (r"\{\{[^}]+\}\}", "{{...}} placeholder"),
    (r"【要書換】", "【要書換】 marker"),
    (r"\bTODO\b", "TODO marker"),
    (r"\bFIXME\b", "FIXME marker"),
]

# Severity levels
ERROR = "ERROR"
WARNING = "WARNING"


def visual_width(text: str) -> int:
    """Count visual width: CJK characters count as 2, others as 1."""
    width = 0
    for ch in text:
        if unicodedata.east_asian_width(ch) in ("F", "W"):
            width += 2
        else:
            width += 1
    return width


def strip_markdown_emphasis(text: str) -> str:
    """Remove `**bold**` / `*italic*` / `` `code` `` markers for visual-width
    calculation. These do not occupy space in the rendered slide, so counting
    them inflates character counts and produces spurious "too long" warnings
    on action titles that use `**強調**` for accent color."""
    # Strip bold first so the italic pass doesn't mis-match `**` as `*`.
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text


def is_japanese(text: str) -> bool:
    """Detect if text contains significant Japanese characters."""
    cjk_count = sum(1 for ch in text if unicodedata.east_asian_width(ch) in ("F", "W"))
    return cjk_count > len(text) * 0.1


def extract_frontmatter(text: str) -> str | None:
    """Extract frontmatter content if present."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end]
    return None


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def split_slides(text: str) -> list[str]:
    text = strip_frontmatter(text)
    parts = re.split(r"^---\s*$", text, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]


def strip_comments(text: str) -> str:
    """Remove HTML comments so they don't affect content-length checks."""
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def bullet_lines(slide: str) -> list[str]:
    return [line.strip() for line in slide.splitlines() if re.match(r"^[-*+]\s+", line.strip())]


def body_lines(slide: str) -> list[str]:
    """Collect content lines for density checks, excluding comments/headings/HTML scaffolding.

    Fenced code blocks (``` ... ```) are collapsed to a single placeholder line
    each — counting every line of source code as a "content line" makes
    tech-heavy slides spuriously trip the body-line / character limits when
    visually they hold one code sample.
    """
    cleaned = strip_comments(slide)
    lines: list[str] = []
    in_fence = False
    fence_buffer: list[str] = []
    for line in cleaned.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_fence:
                # Closing fence — represent the whole block as one short line.
                joined = " ".join(fence_buffer)[:80]
                lines.append(f"[code:{joined}]")
                fence_buffer = []
                in_fence = False
            else:
                in_fence = True
            continue
        if in_fence:
            if stripped:
                fence_buffer.append(stripped)
            continue
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if re.match(r"^</?(?:div|style|br|hr)\b", stripped, re.IGNORECASE):
            continue
        lines.append(stripped)
    return lines


def get_headings(slide: str) -> list[str]:
    """Extract heading text (without # prefix) from a slide."""
    headings = []
    for line in strip_comments(slide).splitlines():
        m = re.match(r"^#+\s+(.+)", line.strip())
        if m:
            text = m.group(1).strip()
            text = re.sub(r"<!--\s*fit\s*-->", "", text).strip()
            headings.append(text)
    return headings


def get_class_directive(slide: str) -> str | None:
    """Extract the full `_class:` directive value (may contain multiple class names)."""
    m = re.search(r"<!--\s*_class:\s*([^>]*?)\s*-->", slide)
    return m.group(1).strip() if m else None


def get_class_names(slide: str) -> list[str]:
    """Return individual class names applied via `_class:` on this slide."""
    directive = get_class_directive(slide)
    if not directive:
        return []
    return [c for c in directive.split() if c]


def check_frontmatter(text: str) -> list[tuple[str, str]]:
    """Check frontmatter for required fields."""
    issues: list[tuple[str, str]] = []
    fm = extract_frontmatter(text)
    if fm is None:
        issues.append((ERROR, "frontmatter: missing YAML frontmatter"))
        return issues
    if "marp:" not in fm and "marp :" not in fm:
        issues.append((ERROR, "frontmatter: missing 'marp: true'"))
    if "theme:" not in fm and "theme :" not in fm:
        issues.append((ERROR, "frontmatter: missing 'theme' setting"))
    elif not re.search(r"theme\s*:\s*fj\b", fm):
        issues.append((WARNING, "frontmatter: theme is not 'fj' — this skill only ships the FJ theme"))
    if "paginate:" not in fm and "paginate :" not in fm:
        issues.append((WARNING, "frontmatter: missing 'paginate' setting"))
    return issues


def check_title_length(index: int, heading: str) -> list[tuple[str, str]]:
    """Warn on very long primary headings."""
    issues: list[tuple[str, str]] = []
    if heading.startswith("{{"):
        return issues
    vw = visual_width(strip_markdown_emphasis(heading))
    limit = MAX_TITLE_CHARS_JA if is_japanese(heading) else MAX_TITLE_CHARS_EN
    if vw > limit:
        issues.append((WARNING, f"slide {index}: heading too long ({vw} visual chars, max {limit}): '{heading[:30]}...'"))
    return issues


def check_fj_classes(index: int, slide: str) -> list[tuple[str, str]]:
    """Warn if a `_class:` directive uses an unknown name (likely a typo)."""
    issues: list[tuple[str, str]] = []
    for name in get_class_names(slide):
        if name not in FJ_CLASSES:
            issues.append(
                (WARNING, f"slide {index}: unknown _class '{name}' — not in FJ theme allowlist")
            )
    return issues


def check_placeholder_removed(index: int, slide: str) -> list[tuple[str, str]]:
    """Fail hard if the slide still contains `{{...}}`, TODO, or similar placeholders."""
    issues: list[tuple[str, str]] = []
    cleaned = strip_comments(slide)
    for pattern, label in PLACEHOLDER_PATTERNS:
        if re.search(pattern, cleaned):
            issues.append((ERROR, f"slide {index}: unresolved {label} — fill it in before building"))
    return issues


# CJK closing punctuation that, when placed immediately before `**`, breaks
# CommonMark's right-flanking rule and prevents the `**` from closing emphasis.
# In that case the literal `**` is rendered as text. Symmetric for openings:
# CJK opening punctuation immediately after `**` does NOT break things by itself,
# but `letter**punct` left-flanking failures are caught by the same scan.
_CJK_CLOSE_PUNCT = "」』）］｝〕》〉、。・…！？"
_CJK_OPEN_PUNCT = "「『（［｛〔《〈"


def check_cjk_bold(index: int, slide: str) -> list[tuple[str, str]]:
    """Detect ``**bold**`` runs that fail to pair because of adjacent CJK punctuation.

    CommonMark requires the closing ``**`` to be *right-flanking*: preceded by
    non-whitespace AND (preceded by non-punct OR followed by punct/space). When
    Japanese authors write ``**「長文」**の三拍子``, the closing ``**`` sits between
    ``」`` (punctuation) and ``の`` (CJK letter), so neither sub-condition holds —
    the literal ``**`` ends up in the rendered slide. The fix is to move the
    delimiters *inside* the brackets: ``「**長文**」の三拍子``.

    The check pairs ``**`` markers line-by-line (odd index = open, even = close)
    and only validates the closing marker. Patterns like ``・**強調**・`` where both
    ends are punctuation are fine — both flanking conditions are satisfied — and
    must not trip the check.
    """
    issues: list[tuple[str, str]] = []
    cleaned = strip_comments(slide)
    # Skip fenced code blocks and inline code — emphasis isn't parsed there.
    cleaned = re.sub(r"```.*?```", "", cleaned, flags=re.DOTALL)
    cleaned = re.sub(r"`[^`]*`", "", cleaned)

    # Emphasis can't span line breaks in CommonMark, so process per line and
    # pair ``**`` markers within each line.
    for line in cleaned.splitlines():
        positions = [m.start() for m in re.finditer(r"\*\*", line)]
        # Drop runs that are part of `***` or longer to avoid mis-pairing.
        positions = [
            p for p in positions
            if (p == 0 or line[p - 1] != "*") and (p + 2 >= len(line) or line[p + 2] != "*")
        ]
        # Pair consecutively: 0=open, 1=close, 2=open, 3=close, ...
        for i in range(1, len(positions), 2):
            close_pos = positions[i]
            before = line[close_pos - 1] if close_pos > 0 else ""
            after = line[close_pos + 2] if close_pos + 2 < len(line) else ""
            if not before:
                continue
            if before not in _CJK_CLOSE_PUNCT:
                continue  # right-flanking holds (preceded by non-punct)
            # Right-flanking also holds if `after` is whitespace, punct, or end-of-line.
            if not after:
                continue  # end of line counts as whitespace
            if after.isspace():
                continue
            if after in _CJK_CLOSE_PUNCT or after in _CJK_OPEN_PUNCT:
                continue
            # Letter / digit / CJK character after — right-flanking fails.
            after_is_letter = (
                after.isalnum() or unicodedata.east_asian_width(after) in ("F", "W")
            )
            if not after_is_letter:
                continue
            issues.append((
                WARNING,
                f"slide {index}: closing '**' between '{before}' and '{after}' will not close — "
                f"CommonMark right-flanking rule fails on CJK punctuation. "
                f"Move ** inside the brackets, e.g. 「**強調**」 instead of **「強調」**.",
            ))
    return issues


def check_meta_prefix(index: int, slide: str) -> list[tuple[str, str]]:
    """Catch LLM-authored meta-commentary leaking into slide body text.

    When the skill docs reference phrases like "見出しだけ読んでも" or "右上のヒント",
    Claude sometimes echoes them as slide captions ("見出しだけ: ..." / "右上ヒント: ...")
    which look like internal stage-direction to the audience. Flag any body line
    that opens with one of the known meta prefixes so the author rewrites it
    into an actual paragraph, bullet, or blockquote.
    """
    issues: list[tuple[str, str]] = []
    for raw in slide.split("\n"):
        # Strip leading whitespace, bullet markers, emphasis, quote chars.
        stripped = raw.lstrip()
        stripped = re.sub(r"^([*\-+>]\s+|\d+\.\s+)+", "", stripped)
        stripped = stripped.lstrip("*_`")
        for pat in META_PREFIX_PATTERNS:
            if stripped.startswith(pat):
                issues.append((
                    WARNING,
                    f"slide {index}: line starts with meta prefix '{pat}' — "
                    f"rewrite as direct slide content (paragraph / bullet / blockquote), "
                    f"not as a narrator caption. Offending line: {raw.strip()[:60]}",
                ))
                break
    return issues


def check_agenda_bullets(index: int, slide: str) -> list[tuple[str, str]]:
    """Agenda / table-of-contents slides should use short bullets, not full
    sentences. Long bullets defeat the purpose of an at-a-glance overview, and
    they overflow the slide on common 1280×720 / 1920×1080 builds.

    Detection is based on the slide's first heading matching common Japanese
    agenda phrases. When matched, every bullet is checked against
    AGENDA_BULLET_MAX_WIDTH and a WARNING is emitted per offender.
    """
    headings = get_headings(slide)
    if not headings:
        return []
    first = headings[0].lower()
    if not any(p.lower() in first for p in AGENDA_HEADING_PATTERNS):
        return []
    issues: list[tuple[str, str]] = []
    for bullet in bullet_lines(slide):
        # Strip emphasis markers from the visual count so `**強調**` doesn't
        # inflate width spuriously.
        stripped = re.sub(r"\*\*", "", bullet)
        w = visual_width(stripped)
        if w > AGENDA_BULLET_MAX_WIDTH:
            issues.append((
                WARNING,
                f"slide {index}: agenda bullet too long ({w} > {AGENDA_BULLET_MAX_WIDTH}): "
                f"{stripped[:40]}... — keep agenda items as short noun phrases.",
            ))
    return issues


def check_image_with_text_layout(index: int, slide: str, classes: list[str]) -> list[tuple[str, str]]:
    """Warn when a default-layout slide combines a standalone image with
    bullet/text content. In the FJ theme, the default layout has no dedicated
    image column — the image renders in the natural flex flow and either
    steals vertical space from the bullets (pushing them off the slide) or
    invades the h1 header bar. Authors should use `content-image-right` /
    `content-image-left` for this pattern so the image gets a fixed panel
    and the text column is properly reserved.

    Skip the check for layouts that already handle images explicitly.
    """
    image_layout_classes = {
        "content-image-right", "content-image-left", "content-image",
        "image", "image-shadow", "title", "section",
        "card-grid", "column-layout",
    }
    if any(cls in image_layout_classes for cls in classes):
        return []
    # Look for a standalone image paragraph: a line that is just `![alt](src)`.
    has_standalone_image = bool(
        re.search(r"^\s*!\[[^\]]*\]\([^)]+\)\s*$", slide, re.MULTILINE)
    )
    if not has_standalone_image:
        return []
    # Any non-heading text content? Bullets, blockquotes, tables, paragraphs.
    body = body_lines(slide)
    # body_lines filters headings/directives but keeps text lines; image line
    # itself is a paragraph, so filter it out before counting.
    non_image_body = [
        ln for ln in body
        if not re.match(r"^\s*!\[[^\]]*\]\([^)]+\)\s*$", ln)
    ]
    if not non_image_body:
        return []
    return [(
        WARNING,
        f"slide {index}: default-layout slide combines an image with text content — "
        f"pick a layout by image aspect ratio: tall/portrait/square → "
        f"`<!-- _class: content-image-right -->` (or -left) to put the image in a "
        f"side panel; wide/landscape (timeline, gantt, horizontal flow) → "
        f"`<!-- _class: content-image -->` to stack title→text→image vertically. "
        f"Wide images squeezed into a side panel get crushed.",
    )]


def check_card_count(index: int, slide: str, classes: list[str]) -> list[tuple[str, str]]:
    """Cap `card-grid` at the card counts supported by fj.css row rules.

    The theme uses `grid-template-rows: repeat(N, 1fr)` plus `:has(.card:nth-of-type(X))`
    selectors to allocate rows. Each column variant has a maximum beyond which
    no row rule matches and cards spill off the slide. This check uses ERROR
    because the result is guaranteed layout breakage, not a stylistic nit.
    """
    if "card-grid" not in classes:
        return []
    # Pick the active column variant; default is cols-2.
    variant = "cols-2"
    for v in ("cols-4", "cols-3", "cols-2"):
        if v in classes:
            variant = v
            break
    card_count = slide.count('class="card"')
    limit = CARD_GRID_MAX_CARDS[variant]
    if card_count > limit:
        return [(
            ERROR,
            f"slide {index}: card-grid {variant} has {card_count} cards > max {limit} — "
            f"fj.css row rules only cover up to {limit} cards for {variant}, extra cards "
            f"will overflow. Split the slide or drop down to a variant with more rows.",
        )]
    if "card-grid" in classes and card_count == 0:
        return [(
            WARNING,
            f"slide {index}: `card-grid` class applied but no `<div class=\"card\">` children found.",
        )]
    return []


def check_column_count(index: int, slide: str, classes: list[str]) -> list[tuple[str, str]]:
    """Require `column-layout` to have 2 or 3 `<div class="column">` children.

    1 column is pointless (use the default layout instead). 4+ columns crush
    each column to ~400px, which is below the readable threshold for the
    32px body font in column-layout. Either split the slide or use a table.
    """
    if "column-layout" not in classes:
        return []
    column_count = slide.count('class="column"')
    if column_count == 0:
        return [(
            WARNING,
            f"slide {index}: `column-layout` class applied but no `<div class=\"column\">` children found.",
        )]
    if column_count not in COLUMN_LAYOUT_VALID_COUNTS:
        return [(
            WARNING,
            f"slide {index}: column-layout has {column_count} columns — "
            f"use 2 or 3 (1 = use default layout, 4+ = too narrow at 32px body font, "
            f"split the slide or switch to a table).",
        )]
    return []


SKIP_KEY_MESSAGE_CLASSES = {"title", "section", "align-center", "all-text-center"}


def check_citation_format(index: int, slide: str) -> list[tuple[str, str]]:
    """Warn if citations use inline italic or HTML comments instead of <cite>."""
    issues: list[tuple[str, str]] = []
    # Inline italic: *出典: ...* or *出典：...*
    if re.search(r"\*出典[:：]", slide):
        issues.append((
            WARNING,
            f"slide {index}: citation uses inline italic `*出典:*` — "
            f"use `<cite>出典: ...</cite>` instead (renders at bottom-right automatically).",
        ))
    # HTML comment: <!-- 出典: ... -->
    if re.search(r"<!--\s*出典[:：]", slide):
        issues.append((
            WARNING,
            f"slide {index}: citation in HTML comment `<!-- 出典: -->` — "
            f"comments render nothing. Use `<cite>出典: ...</cite>` instead.",
        ))
    return issues


def check_key_message(index: int, slide: str, classes: list[str]) -> list[tuple[str, str]]:
    """Warn if a content slide is missing a key-message lead paragraph below h1."""
    # Skip slides where key messages are not expected.
    if SKIP_KEY_MESSAGE_CLASSES & set(classes):
        return []
    # Need at least an h1 heading to qualify.
    headings = get_headings(slide)
    if not headings:
        return []
    # Strip directives/comments and heading lines to isolate body.
    body = re.sub(r"<!--.*?-->", "", slide, flags=re.DOTALL)
    lines = body.strip().split("\n")
    # Find the h1 line.
    h1_idx = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            h1_idx = i
            break
    if h1_idx is None:
        return []
    # The line(s) immediately after h1 (skipping blanks) should be a plain
    # paragraph — not a bullet, not a div, not a table header, not an h2+.
    found_lead = False
    for line in lines[h1_idx + 1:]:
        stripped = line.strip()
        if not stripped:
            continue  # skip blanks
        # It's a lead paragraph if it's plain text (not starting with -, *, #, |, <div, <cite, ```)
        if not re.match(r"^[-*#|<`>]|^\d+\.", stripped):
            found_lead = True
        break  # only check the first non-blank line after h1

    if not found_lead:
        return [(
            WARNING,
            f"slide {index}: missing key-message paragraph below h1 — "
            f"add a 1-sentence lead explaining what this slide conveys, "
            f"between the h1 and the first content element.",
        )]
    return []


def check_image_alt(index: int, slide: str) -> list[tuple[str, str]]:
    """Warn if an image has empty alt text (accessibility)."""
    issues: list[tuple[str, str]] = []
    for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", slide):
        alt, src = match.group(1), match.group(2)
        # Strip Marp sizing keywords that live inside the alt slot.
        alt_stripped = re.sub(r"\b(?:w|h|bg)\s*:\s*\S+", "", alt).strip()
        if not alt_stripped:
            issues.append((WARNING, f"slide {index}: image '{src}' has empty alt text"))
    return issues


# Mermaid diagram types that produce horizontally-oriented (landscape)
# output. These must NOT be placed inside content-image-right/-left panels
# because the panel width squashes them. Use `content-image` (vertical
# stack) instead.
_HORIZONTAL_MERMAID = re.compile(
    r"(?:graph\s+LR|flowchart\s+LR|gantt|timeline|journey|gitgraph)",
    re.IGNORECASE,
)


def check_horizontal_image_in_side_panel(index: int, slide: str, classes: list[str]) -> list[tuple[str, str]]:
    """Warn when a landscape Mermaid diagram or a known-horizontal image sits
    inside a content-image-right or content-image-left layout.

    This catches the single most common visual accident: a wide diagram
    crammed into a narrow side panel, rendering as a tiny squished thumbnail.
    """
    issues: list[tuple[str, str]] = []
    is_side_panel = "content-image-right" in classes or "content-image-left" in classes
    if not is_side_panel:
        return issues

    # Check for horizontal Mermaid blocks (they'll have been converted to
    # images by build time, but the original ```mermaid block may still be
    # in the source during lint).
    if _HORIZONTAL_MERMAID.search(slide):
        issues.append((
            WARNING,
            f"slide {index}: horizontal Mermaid diagram (graph LR / gantt / timeline etc.) "
            f"should use `content-image` (vertical stack), not `content-image-right/-left`",
        ))

    # Also check image references — if a Mermaid PNG was already generated
    # and there's no raw mermaid block, look at the image filename for hints.
    # Mermaid images are named mermaid-<hash>.png — we can't tell orientation
    # from the hash alone, but if someone explicitly put `w:` wider than tall
    # that's a signal too. For now, the mermaid-block check above catches the
    # primary case.

    return issues


def lint_slide(index: int, slide: str) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    bullets = bullet_lines(slide)
    bodies = body_lines(slide)
    headings = get_headings(slide)
    classes = get_class_names(slide)
    is_small_text = "small-text" in classes
    is_columns = "column-layout" in classes
    is_card_grid = "card-grid" in classes
    # small-text targets density: allow 2x characters but only 1.5x lines —
    # 30 stacked lines look cramped even at small font.
    content_multiplier = SMALL_TEXT_CONTENT_MULTIPLIER if is_small_text else 1.0
    line_multiplier = SMALL_TEXT_LINES_MULTIPLIER if is_small_text else 1.0
    body_line_limit = int(MAX_BODY_LINES * line_multiplier)
    content_char_limit = int(MAX_CONTENT_CHARS * content_multiplier)
    bullet_char_limit = int(MAX_BULLET_CHARS * content_multiplier)
    # `column-layout` distributes bullets across 2-3 columns, so the per-slide
    # bullet limit should scale with the number of columns.
    if is_columns:
        column_count = max(1, slide.count('class="column"'))
        bullet_limit = int(MAX_BULLETS * column_count * line_multiplier)
    elif is_card_grid:
        # card-grid distributes content across N independent cards; each gets
        # its own bullet budget. Use the actual card count from the markup.
        card_count = max(1, slide.count('class="card"'))
        bullet_limit = int(MAX_BULLETS * card_count * line_multiplier)
    else:
        bullet_limit = int(MAX_BULLETS * line_multiplier)

    # Bullet count
    if len(bullets) > bullet_limit:
        issues.append((WARNING, f"slide {index}: bullet count {len(bullets)} > {bullet_limit}"))

    # Bullet line length — strip emphasis markers before counting so
    # `**強調**` doesn't inflate visual width for a segment that renders the
    # same width bolded or not.
    for bullet in bullets:
        vw = visual_width(strip_markdown_emphasis(bullet))
        if vw > bullet_char_limit:
            issues.append((WARNING, f"slide {index}: long bullet ({vw} chars): {bullet[:50]}..."))

    # Body line count
    if len(bodies) > body_line_limit:
        issues.append((WARNING, f"slide {index}: content lines {len(bodies)} > {body_line_limit}"))

    # Total content characters (emphasis-stripped)
    total_chars = sum(visual_width(strip_markdown_emphasis(line)) for line in bodies)
    if total_chars > content_char_limit:
        issues.append((WARNING, f"slide {index}: total content {total_chars} chars > {content_char_limit}"))

    # Missing heading — rare but worth catching
    if not headings:
        issues.append((WARNING, f"slide {index}: missing heading"))

    # Primary heading length check
    for heading in headings[:1]:
        issues.extend(check_title_length(index, heading))

    # FJ class allowlist
    issues.extend(check_fj_classes(index, slide))

    # Placeholder leaks
    issues.extend(check_placeholder_removed(index, slide))

    # CJK bold pairing — `**「...」**` style failures
    issues.extend(check_cjk_bold(index, slide))

    # Structural guardrails for card-grid / column-layout
    issues.extend(check_card_count(index, slide, classes))
    issues.extend(check_column_count(index, slide, classes))

    # Image alt accessibility
    issues.extend(check_image_alt(index, slide))

    # Horizontal image in side panel — landscape Mermaid in content-image-right/-left
    issues.extend(check_horizontal_image_in_side_panel(index, slide, classes))

    # Image + text in default layout — prompt author to switch to
    # content-image-right/-left so the image gets a fixed side panel.
    issues.extend(check_image_with_text_layout(index, slide, classes))

    # Agenda slides — short bullets only
    issues.extend(check_agenda_bullets(index, slide))

    # Meta-commentary prefixes (見出しだけ: / 補足: / 右上ヒント: / note:)
    issues.extend(check_meta_prefix(index, slide))

    # Citation format — must use <cite>, not inline italic or HTML comment
    issues.extend(check_citation_format(index, slide))

    # Key-message lead paragraph — required on all content slides
    issues.extend(check_key_message(index, slide, classes))

    return issues


def check_layout_variety(slides: list[str]) -> list[tuple[str, str]]:
    """Flag 3+ consecutive slides sharing the same `_class:` directive."""
    issues: list[tuple[str, str]] = []
    classes = [get_class_directive(s) for s in slides]
    consecutive = 1
    for i in range(1, len(classes)):
        if classes[i] and classes[i] == classes[i - 1]:
            consecutive += 1
            if consecutive > MAX_CONSECUTIVE_SAME_LAYOUT:
                issues.append(
                    (WARNING, f"slides {i - consecutive + 2}-{i + 1}: "
                     f"layout '{classes[i]}' used {consecutive} times consecutively (max {MAX_CONSECUTIVE_SAME_LAYOUT})")
                )
        else:
            consecutive = 1
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint a Marp markdown deck.")
    parser.add_argument("deck", type=Path)
    args = parser.parse_args()

    text = args.deck.read_text(encoding="utf-8")

    all_issues: list[tuple[str, str]] = []
    all_issues.extend(check_frontmatter(text))

    slides = split_slides(text)
    for i, slide in enumerate(slides, start=1):
        all_issues.extend(lint_slide(i, slide))

    all_issues.extend(check_layout_variety(slides))

    if all_issues:
        errors = [(sev, msg) for sev, msg in all_issues if sev == ERROR]
        warnings = [(sev, msg) for sev, msg in all_issues if sev == WARNING]

        if errors:
            print(f"Errors ({len(errors)}):")
            for _, msg in errors:
                print(f"  [ERROR] {msg}")

        if warnings:
            print(f"Warnings ({len(warnings)}):")
            for _, msg in warnings:
                print(f"  [WARN]  {msg}")

        print(f"\nTotal: {len(errors)} error(s), {len(warnings)} warning(s)")

        if errors:
            sys.exit(1)
    else:
        print("No issues found.")


if __name__ == "__main__":
    main()
