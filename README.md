# staffbase-knowledge-portal

非エンジニア向けに、業務でそのまま使えるStaffbase関連ナレッジを集約するポータルです。Gensparkで再生成しやすいJSON構造で、GitHub Raw URLから外部参照しやすい形にしています。

## ディレクトリ構成

- `docs/` : 業務説明に変換したナレッジMarkdown
- `rfp/`, `note/`, `slides/`, `analytics/`, `product_reference/` : カテゴリ別の入口
- `public/index.html` : ポータル入口
- `data/index.json` : ナビゲーション定義
- `data/rfp.json`, `data/note.json`, `data/slides.json` : Genspark向け構造データ
- `templates/slide-template.json` : slide-template準拠のテンプレート
- `scripts/build_index.py` : docs/data から index.json を再生成
- `scripts/sync_genspark.py` : 外部Raw URLから同期

## データスキーマ（Genspark向け）

各カテゴリJSONは以下キーを持ちます。

- `category`
- `use_case`（業務トリガー）
- `how_to_use`
- `input`
- `output`
- `example`

## 使い方

```bash
python3 scripts/build_index.py
python3 scripts/sync_genspark.py
```

## 統合元リポジトリ

- https://github.com/YoheiUmezu/staffbase-rfp
- https://github.com/YoheiUmezu/note-article
- https://github.com/YoheiUmezu/slide-template
- https://github.com/YoheiUmezu/analytics_json
- https://github.com/YoheiUmezu/staffbase-product-reference
