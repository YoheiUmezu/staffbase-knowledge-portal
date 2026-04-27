#!/usr/bin/env python3
"""Sync Genspark-ready JSON/Markdown outputs from configured raw URLs."""
from __future__ import annotations
from pathlib import Path
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SYNC_DIR = ROOT / 'data' / 'genspark_synced'
SYNC_DIR.mkdir(parents=True, exist_ok=True)

CONFIG = {
    'note_manus': 'https://raw.githubusercontent.com/YoheiUmezu/note-article/main/manus_input.md',
    'analytics_index': 'https://raw.githubusercontent.com/YoheiUmezu/analytics_json/main/analytics_json/scenario_index.json',
    'product_urls': 'https://raw.githubusercontent.com/YoheiUmezu/staffbase-product-reference/main/staffbase_urls.md',
}


def fetch_text(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode('utf-8')


def main() -> None:
    result = []
    for name, url in CONFIG.items():
        data = fetch_text(url)
        suffix = '.json' if name.endswith('index') else '.md'
        out = SYNC_DIR / f'{name}{suffix}'
        out.write_text(data, encoding='utf-8')
        result.append({'name': name, 'source': url, 'saved_to': str(out.relative_to(ROOT))})

    manifest = SYNC_DIR / 'manifest.json'
    manifest.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'synced {len(result)} items -> {manifest}')


if __name__ == '__main__':
    main()
