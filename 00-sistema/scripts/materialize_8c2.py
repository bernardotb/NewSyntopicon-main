import os
import yaml

refs = [
    {
        'file_name': 'ref-42-8c-2-01-plutarco.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8c-2:01-plutarch',
            'slug': 'ref-42-8c-2-01-plutarco',
            'topicId': 'topic:justica:8c-2',
            'ideaId': 'idea:justica',
            'orderInTopic': 1,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 14,
            'volume-gbww': '[[vol-14|Volume 14]]',
            'authorId': 'author:plutarch',
            'authorCanonicalName': 'Plutarch',
            'workIds': ['work:marcus-cato-plutarch'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:marcus-cato-plutarch',
                    'canonicalWorkTitle': 'Marcus Cato',
                    'displayWorkTitlePtBr': 'Marco Catão',
                    'gbwwVolume': 14,
                    'locatorRaw': 'Marcus Cato, 287c-d',
                    'locators': [
                        {
                            'locatorRaw': '287c-d',
                            'subLocator': '287c-d'
                        }
                    ]
                }
            ],
            'locatorRaw': 'Marcus Cato, 287c-d',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868'],
            'warningsOpen': [],
            'topico': '[[topico-42-8c-2|42.8c(2): Lucro e incremento não auferido]]',
            'autor': '[[autor-plutarco|Plutarco]]',
            'obras': ['[[obra-marco-catao-plutarco|Marco Catão]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8c(2) (01) - Plutarco'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8c(2) (01): [[autor-plutarco|Plutarco]]',
        'author_link': '[[autor-plutarco|Plutarco]]',
        'vol_num': 14,
        'locator': 'Marcus Cato, 287c-d',
        'works_table': '| 1 | [[obra-marco-catao-plutarco|Marco Catão]] (*Marcus Cato*) | [[vol-14|Vol. 14]] | `Marcus Cato, 287c-d` |'
    },
    {
        'file_name': 'ref-42-8c-2-02-adam-smith.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8c-2:02-smith',
            'slug': 'ref-42-8c-2-02-adam-smith',
            'topicId': 'topic:justica:8c-2',
            'ideaId': 'idea:justica',
            'orderInTopic': 2,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 39,
            'volume-gbww': '[[vol-39|Volume 39]]',
            'authorId': 'author:smith',
            'authorCanonicalName': 'Adam Smith',
            'workIds': ['work:wealth-of-nations'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:wealth-of-nations',
                    'canonicalWorkTitle': 'The Wealth of Nations',
                    'displayWorkTitlePtBr': 'A Riqueza das Nações',
                    'gbwwVolume': 39,
                    'locatorRaw': 'Wealth of Nations, BK i, 20b-23b passim, esp 21a-c; 27b-28a; 109d-110d',
                    'locators': [
                        {
                            'locatorRaw': 'BK i, 20b-23b passim, esp 21a-c',
                            'subLocator': 'BK i, 20b-23b passim, esp 21a-c'
                        },
                        {
                            'locatorRaw': '27b-28a',
                            'subLocator': '27b-28a'
                        },
                        {
                            'locatorRaw': '109d-110d',
                            'subLocator': '109d-110d'
                        }
                    ]
                }
            ],
            'locatorRaw': 'Wealth of Nations, BK i, 20b-23b passim, esp 21a-c; 27b-28a; 109d-110d',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; correção de quebra de linha tipográfica OCR'],
            'warningsOpen': [],
            'topico': '[[topico-42-8c-2|42.8c(2): Lucro e incremento não auferido]]',
            'autor': '[[autor-adam-smith|Adam Smith]]',
            'obras': ['[[obra-riqueza-das-nacoes-smith|A Riqueza das Nações]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8c(2) (02) - Adam Smith'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8c(2) (02): [[autor-adam-smith|Adam Smith]]',
        'author_link': '[[autor-adam-smith|Adam Smith]]',
        'vol_num': 39,
        'locator': 'Wealth of Nations, BK i, 20b-23b passim, esp 21a-c; 27b-28a; 109d-110d',
        'works_table': '| 1 | [[obra-riqueza-das-nacoes-smith|A Riqueza das Nações]] (*The Wealth of Nations*) | [[vol-39|Vol. 39]] | `Wealth of Nations, BK i, 20b-23b passim, esp 21a-c; 27b-28a; 109d-110d` |'
    },
    {
        'file_name': 'ref-42-8c-2-03-gwf-hegel.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8c-2:03-hegel',
            'slug': 'ref-42-8c-2-03-gwf-hegel',
            'topicId': 'topic:justica:8c-2',
            'ideaId': 'idea:justica',
            'orderInTopic': 3,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 46,
            'volume-gbww': '[[vol-46|Volume 46]]',
            'authorId': 'author:hegel',
            'authorCanonicalName': 'Georg Wilhelm Friedrich Hegel',
            'workIds': ['work:philosophy-of-right-hegel'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:philosophy-of-right-hegel',
                    'canonicalWorkTitle': 'Philosophy of Right',
                    'displayWorkTitlePtBr': 'Filosofia do Direito',
                    'gbwwVolume': 46,
                    'locatorRaw': 'Philosophy of Right, PART iii, par 243, 77b-c',
                    'locators': [
                        {
                            'locatorRaw': 'PART iii, par 243, 77b-c',
                            'subLocator': 'PART iii, par 243, 77b-c'
                        }
                    ]
                }
            ],
            'locatorRaw': 'Philosophy of Right, PART iii, par 243, 77b-c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; correção OCR PART in -> PART iii'],
            'warningsOpen': [],
            'topico': '[[topico-42-8c-2|42.8c(2): Lucro e incremento não auferido]]',
            'autor': '[[autor-gwf-hegel|G. W. F. Hegel]]',
            'obras': ['[[obra-filosofia-do-direito-hegel|Filosofia do Direito]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8c(2) (03) - G. W. F. Hegel'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8c(2) (03): [[autor-gwf-hegel|G. W. F. Hegel]]',
        'author_link': '[[autor-gwf-hegel|G. W. F. Hegel]]',
        'vol_num': 46,
        'locator': 'Philosophy of Right, PART iii, par 243, 77b-c',
        'works_table': '| 1 | [[obra-filosofia-do-direito-hegel|Filosofia do Direito]] (*Philosophy of Right*) | [[vol-46|Vol. 46]] | `Philosophy of Right, PART iii, par 243, 77b-c` |'
    },
    {
        'file_name': 'ref-42-8c-2-04-karl-marx.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8c-2:04-karl-marx',
            'slug': 'ref-42-8c-2-04-karl-marx',
            'topicId': 'topic:justica:8c-2',
            'ideaId': 'idea:justica',
            'orderInTopic': 4,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 50,
            'volume-gbww': '[[vol-50|Volume 50]]',
            'authorId': 'author:marx',
            'authorCanonicalName': 'Karl Marx',
            'workIds': ['work:capital-marx'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:capital-marx',
                    'canonicalWorkTitle': 'Capital',
                    'displayWorkTitlePtBr': 'O Capital',
                    'gbwwVolume': 50,
                    'locatorRaw': 'Capital, 71d-72c; 85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d; 267b; 267d-275c passim, esp 271b-c; 286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b',
                    'locators': [
                        {
                            'locatorRaw': '71d-72c',
                            'subLocator': '71d-72c'
                        },
                        {
                            'locatorRaw': '85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d',
                            'subLocator': '85a-263d'
                        },
                        {
                            'locatorRaw': '267b',
                            'subLocator': '267b'
                        },
                        {
                            'locatorRaw': '267d-275c passim, esp 271b-c',
                            'subLocator': '267d-275c passim, esp 271b-c'
                        },
                        {
                            'locatorRaw': '286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b',
                            'subLocator': '286a-301b'
                        }
                    ]
                }
            ],
            'locatorRaw': 'Capital, 71d-72c; 85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d; 267b; 267d-275c passim, esp 271b-c; 286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; correção OCR lOOa-lOlb -> 100a-101b e ordem do título Capital'],
            'warningsOpen': [],
            'topico': '[[topico-42-8c-2|42.8c(2): Lucro e incremento não auferido]]',
            'autor': '[[autor-karl-marx|Karl Marx]]',
            'obras': ['[[obra-o-capital-marx|O Capital]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8c(2) (04) - Karl Marx'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8c(2) (04): [[autor-karl-marx|Karl Marx]]',
        'author_link': '[[autor-karl-marx|Karl Marx]]',
        'vol_num': 50,
        'locator': 'Capital, 71d-72c; 85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d; 267b; 267d-275c passim, esp 271b-c; 286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b',
        'works_table': '| 1 | [[obra-o-capital-marx|O Capital]] (*Capital*) | [[vol-50|Vol. 50]] | `Capital, 71d-72c; 85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d; 267b; 267d-275c passim, esp 271b-c; 286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b` |'
    }
]

out_dir = '03-referencias/justica'
for item in refs:
    p = os.path.join(out_dir, item['file_name'])
    yaml_header = yaml.dump(item['data'], allow_unicode=True, sort_keys=False)
    body = f"""---
{yaml_header}---

# {item['title']}

> **Tópico Canônico:** [[topico-42-8c-2|42.8c(2): Lucro e incremento não auferido]]  
> **Autor:** {item['author_link']}  
> **Volume GBWW:** Volume {item['vol_num']} | **Página Syntopicon:** 868  
> **Status de Auditoria:** `verification: verified` | **Resolução:** `resolved-by-visual-audit`

---

## 📖 Localizador Textual Canônico (*Locator Raw*)

```text
{item['locator']}
```

---

## 🏛️ Segmentos de Obras Citadas

| # | Obra Canônica | Volume | Localizador no Volume |
| :-: | :--- | :-: | :--- |
{item['works_table']}

---

## 📜 Passagens Verificadas da Edição (04-passagens/)
*(Nenhuma passagem literal transcrita para esta referência nesta fase — regra estrita `Referência != Passagem`).*
"""
    with open(p, 'w', encoding='utf-8') as f:
        f.write(body)
    print('Materialized:', p)
