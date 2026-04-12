#!/usr/bin/env python3
"""Generate a slide review HTML page from a Marp deck HTML file."""

import json
import os
import sys
import webbrowser
from pathlib import Path

PATTERNS = [
    # A. タイトル・セクション系
    {"id": "1", "name": "タイトルスライド", "category": "A. タイトル・セクション系"},
    {"id": "2", "name": "セクション開始", "category": "A. タイトル・セクション系"},
    {"id": "3", "name": "セクション終了・まとめ", "category": "A. タイトル・セクション系"},
    {"id": "4", "name": "目次スライド", "category": "A. タイトル・セクション系"},
    {"id": "5", "name": "クロージング", "category": "A. タイトル・セクション系"},
    # B. カラムレイアウト系
    {"id": "6", "name": "2カラム比較", "category": "B. カラムレイアウト系"},
    {"id": "7a", "name": "2カラム（テキスト＋画像）", "category": "B. カラムレイアウト系"},
    {"id": "7b", "name": "2カラム（画像＋テキスト）", "category": "B. カラムレイアウト系"},
    {"id": "8", "name": "3カラム（画像＋テキスト）", "category": "B. カラムレイアウト系"},
    {"id": "9", "name": "3カラム（アクセントカラー付き）", "category": "B. カラムレイアウト系"},
    {"id": "10", "name": "4カラムレイアウト", "category": "B. カラムレイアウト系"},
    {"id": "11", "name": "5カラム（成熟度レベル）", "category": "B. カラムレイアウト系"},
    {"id": "12", "name": "2x2グリッド（画像＋テキスト）", "category": "B. カラムレイアウト系"},
    {"id": "13", "name": "2x3グリッドレイアウト", "category": "B. カラムレイアウト系"},
    # C. 縦並びリスト系
    {"id": "14", "name": "縦3つステップ", "category": "C. 縦並びリスト系"},
    {"id": "15", "name": "番号付きステップ（横型）", "category": "C. 縦並びリスト系"},
    {"id": "16", "name": "タイムラインレイアウト", "category": "C. 縦並びリスト系"},
    {"id": "17", "name": "アイコン付きリスト", "category": "C. 縦並びリスト系"},
    # D. パネルデザイン系
    {"id": "18", "name": "基本パネル（画像ヘッダー付き）", "category": "D. パネルデザイン系"},
    {"id": "19", "name": "強調パネル（左ボーダー付き）", "category": "D. パネルデザイン系"},
    {"id": "20", "name": "ガラス風パネル", "category": "D. パネルデザイン系"},
    {"id": "21", "name": "グラデーションパネル", "category": "D. パネルデザイン系"},
    {"id": "22", "name": "カード型レイアウト（画像付き）", "category": "D. パネルデザイン系"},
    # E. 背景・画像系
    {"id": "23", "name": "背景画像全画面", "category": "E. 背景・画像系"},
    {"id": "24", "name": "背景画像右側配置", "category": "E. 背景・画像系"},
    {"id": "25", "name": "引用スライド", "category": "E. 背景・画像系"},
    {"id": "26", "name": "複数画像・分割背景", "category": "E. 背景・画像系"},
    # F. 強調・特殊系
    {"id": "27", "name": "統計強調スライド", "category": "F. 強調・特殊系"},
    {"id": "28", "name": "中央配置メッセージ", "category": "F. 強調・特殊系"},
    {"id": "29", "name": "Q&A スライド", "category": "F. 強調・特殊系"},
    # G. 応用パターン系
    {"id": "30", "name": "QRコード付き紹介", "category": "G. 応用パターン系"},
    {"id": "31", "name": "問いかけスライド", "category": "G. 応用パターン系"},
    {"id": "32", "name": "脚注引用スライド", "category": "G. 応用パターン系"},
    {"id": "33", "name": "インライン画像スライド", "category": "G. 応用パターン系"},
    {"id": "34", "name": "統計比率スライド", "category": "G. 応用パターン系"},
    {"id": "35", "name": "テキスト＋統計パネル混合", "category": "G. 応用パターン系"},
    {"id": "36", "name": "まとめスライド（ガラス風縦並び）", "category": "G. 応用パターン系"},
    {"id": "37", "name": "シンプルリスト＋補足パネル", "category": "G. 応用パターン系"},
    {"id": "38", "name": "対比＋結論スライド", "category": "G. 応用パターン系"},
    {"id": "39", "name": "テーブル＋ハイライト", "category": "G. 応用パターン系"},
]


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_review.py <deck.html>")
        print("Example: python generate_review.py output/my-deck/deck.html")
        sys.exit(1)

    deck_path = Path(sys.argv[1]).resolve()
    if not deck_path.exists():
        print(f"Error: {deck_path} not found")
        sys.exit(1)

    deck_name = deck_path.stem
    deck_filename = deck_path.name

    # Read template
    template_path = Path(__file__).parent / "review-template.html"
    template = template_path.read_text(encoding="utf-8")

    # Replace placeholders
    html = template.replace("__DECK_NAME__", deck_name)
    html = html.replace("__DECK_PATH__", deck_filename)
    html = html.replace("__PATTERNS_DATA__", json.dumps(PATTERNS, ensure_ascii=False))

    # Write output next to the deck
    output_path = deck_path.parent / f"{deck_name}-review.html"
    output_path.write_text(html, encoding="utf-8")
    print(f"Review page generated: {output_path}")

    # Open in browser
    webbrowser.open(f"file://{output_path}")


if __name__ == "__main__":
    main()
