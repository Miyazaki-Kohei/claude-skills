from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# Content limits
MAX_BULLETS = 7
MAX_BULLET_CHARS = 80
MAX_BODY_LINES = 14
MAX_CONTENT_CHARS = 500
MAX_TITLE_CHARS_JA = 40
MAX_TITLE_CHARS_EN = 50
MAX_CONSECUTIVE_SAME_LAYOUT = 2

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


def bullet_lines(slide: str) -> list[str]:
    return [line.strip() for line in slide.splitlines() if re.match(r"^[-*+]\s+", line.strip())]


def body_lines(slide: str) -> list[str]:
    lines = []
    in_comment = False
    for line in slide.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("<!--"):
            in_comment = True
        if in_comment:
            if s.endswith("-->"):
                in_comment = False
            continue
        if s.startswith("#"):
            continue
        # Skip HTML tags that are structural (div, style)
        if re.match(r"^</?(?:div|style)", s, re.IGNORECASE):
            continue
        lines.append(s)
    return lines


def get_headings(slide: str) -> list[str]:
    """Extract heading text (without # prefix) from a slide."""
    headings = []
    for line in slide.splitlines():
        m = re.match(r"^#+\s+(.+)", line.strip())
        if m:
            text = m.group(1).strip()
            # Remove <!-- fit --> directive
            text = re.sub(r"<!--\s*fit\s*-->", "", text).strip()
            headings.append(text)
    return headings


def get_class_directive(slide: str) -> str | None:
    """Extract the _class directive value from a slide."""
    m = re.search(r"<!--\s*_class:\s*(\S+)\s*-->", slide)
    return m.group(1) if m else None


def is_multi_column(slide: str) -> bool:
    """Check if slide uses multi-column layout (has multiple <div> blocks)."""
    return slide.lower().count("<div>") >= 2


def split_div_blocks(slide: str) -> list[str]:
    """Split slide content into individual <div> blocks."""
    parts = re.split(r"</?div>", slide, flags=re.IGNORECASE)
    return [p.strip() for p in parts if p.strip()]


def has_visual_element(slide: str) -> bool:
    """Check if slide has any visual element (image, table, layout class, HTML div)."""
    if get_class_directive(slide):
        return True
    if re.search(r"!\[.*?\]\(.*?\)", slide):
        return True
    if re.search(r"^\|.*\|.*\|", slide, re.MULTILINE):
        return True
    if "<div" in slide.lower():
        return True
    return False


def check_frontmatter(text: str) -> list[tuple[str, str]]:
    """Check frontmatter for required fields. Returns list of (severity, message)."""
    issues: list[tuple[str, str]] = []
    fm = extract_frontmatter(text)
    if fm is None:
        issues.append((ERROR, "frontmatter: missing YAML frontmatter"))
        return issues
    if "marp:" not in fm and "marp :" not in fm:
        issues.append((ERROR, "frontmatter: missing 'marp: true'"))
    if "theme:" not in fm and "theme :" not in fm:
        issues.append((ERROR, "frontmatter: missing 'theme' setting"))
    if "paginate:" not in fm and "paginate :" not in fm:
        issues.append((WARNING, "frontmatter: missing 'paginate' setting"))
    return issues


def check_action_title(index: int, heading: str) -> list[tuple[str, str]]:
    """Warn if heading looks like a topic label (short noun phrase without verb-like content)."""
    issues: list[tuple[str, str]] = []
    # Skip structural headings
    skip_patterns = [
        r"^Q\s*&\s*A$", r"^Appendix", r"^Thank", r"^{{",
        r"^ありがとう", r"^付録", r"^参考",
    ]
    for pat in skip_patterns:
        if re.match(pat, heading, re.IGNORECASE):
            return issues

    # Heuristic: short heading with no verb is likely a topic label
    # For Japanese: check if it's just nouns (very short without particles/verbs)
    if is_japanese(heading):
        # Japanese action titles typically have particles or verb endings
        if len(heading) <= 6 and not re.search(r"[るたすくいうえおれ]$", heading):
            issues.append((WARNING, f"slide {index}: heading may be a topic label, not an action title: '{heading}'"))
    else:
        words = heading.split()
        if len(words) <= 3 and not any(w.lower().endswith(("s", "ed", "ing", "es")) for w in words):
            issues.append((WARNING, f"slide {index}: heading may be a topic label, not an action title: '{heading}'"))

    return issues


def check_title_length(index: int, heading: str) -> list[tuple[str, str]]:
    """Check heading length against character limits."""
    issues: list[tuple[str, str]] = []
    if heading.startswith("{{"):
        return issues
    vw = visual_width(heading)
    limit = MAX_TITLE_CHARS_JA if is_japanese(heading) else MAX_TITLE_CHARS_EN
    if vw > limit:
        issues.append((WARNING, f"slide {index}: heading too long ({vw} visual chars, max {limit}): '{heading[:30]}...'"))
    return issues


def lint_slide(index: int, slide: str) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    bullets = bullet_lines(slide)
    bodies = body_lines(slide)
    headings = get_headings(slide)

    # Bullet count — for multi-column layouts, check per block
    if is_multi_column(slide):
        for block in split_div_blocks(slide):
            block_bullets = bullet_lines(block)
            if len(block_bullets) > MAX_BULLETS:
                issues.append((WARNING, f"slide {index}: bullet count {len(block_bullets)} > {MAX_BULLETS} in a column"))
    elif len(bullets) > MAX_BULLETS:
        issues.append((WARNING, f"slide {index}: bullet count {len(bullets)} > {MAX_BULLETS}"))

    # Bullet line length
    for bullet in bullets:
        if visual_width(bullet) > MAX_BULLET_CHARS:
            issues.append((WARNING, f"slide {index}: long bullet ({visual_width(bullet)} chars): {bullet[:50]}..."))

    # Body line count
    if len(bodies) > MAX_BODY_LINES:
        issues.append((WARNING, f"slide {index}: content lines {len(bodies)} > {MAX_BODY_LINES}"))

    # Total content characters
    total_chars = sum(visual_width(line) for line in bodies)
    if total_chars > MAX_CONTENT_CHARS:
        issues.append((WARNING, f"slide {index}: total content {total_chars} chars > {MAX_CONTENT_CHARS}"))

    # Missing heading
    if not headings:
        issues.append((WARNING, f"slide {index}: missing heading"))

    # Heading checks
    for heading in headings[:1]:  # Check primary heading only
        issues.extend(check_action_title(index, heading))
        issues.extend(check_title_length(index, heading))

    # Text-only slide check
    if bodies and not has_visual_element(slide):
        issues.append((WARNING, f"slide {index}: text-only slide with no layout class or visual element"))

    return issues


def check_layout_variety(slides: list[str]) -> list[tuple[str, str]]:
    """Check that the same layout class isn't used 3+ times consecutively."""
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

    # Frontmatter checks
    all_issues.extend(check_frontmatter(text))

    # Per-slide checks
    slides = split_slides(text)
    for i, slide in enumerate(slides, start=1):
        all_issues.extend(lint_slide(i, slide))

    # Cross-slide checks
    all_issues.extend(check_layout_variety(slides))

    # Output
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
