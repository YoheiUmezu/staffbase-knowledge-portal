#!/usr/bin/env python3
"""Convert docs and data entries into data/index.json."""
from __future__ import annotations
from pathlib import Path
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
DOCS_DIR = ROOT / 'docs'

CATEGORY_MAP = [
    ('rfp', 'RFP回答支援'),
    ('note', '記事下書き生成'),
    ('slides', 'スライド生成'),
    ('analytics', '分析シナリオ'),
    ('product_reference', '製品リファレンス'),
    ('demo_ui_project', 'デモUI提案'),
]


def build_index() -> dict:
    categories = []
    for category_id, title in CATEGORY_MAP:
        data_file = DATA_DIR / f'{category_id}.json'
        doc_file = DOCS_DIR / f'{category_id}.md'
        if not data_file.exists() or not doc_file.exists():
            continue
        with data_file.open('r', encoding='utf-8') as f:
            record = json.load(f)
        categories.append(
            {
                'id': category_id,
                'title': title,
                'doc': str(doc_file.relative_to(ROOT)),
                'data': str(data_file.relative_to(ROOT)),
                'use_case': record.get('use_case', ''),
            }
        )

    return {
        'portal_name': 'staffbase-knowledge-portal',
        'description': '非エンジニア向けの業務ナレッジポータル',
        'last_updated': datetime.now(timezone.utc).isoformat(),
        'categories': categories,
    }


def main() -> None:
    index = build_index()
    out = DATA_DIR / 'index.json'
    out.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'updated: {out}')


if __name__ == '__main__':
    main()
