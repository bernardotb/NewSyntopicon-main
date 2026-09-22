import os
import yaml

refs_data = [
    {
        'file_name': 'ref-42-8d-01-antigo-testamento.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:01-antigo-testamento',
            'slug': 'ref-42-8d-01-antigo-testamento',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 1,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': None,
            'volume-gbww': None,
            'authorId': 'author:bible-old-testament',
            'authorCanonicalName': 'Old Testament',
            'workIds': [
                'work:bible-exodus',
                'work:bible-leviticus',
                'work:bible-deuteronomy',
                'work:bible-nehemiah',
                'work:bible-psalms',
                'work:bible-proverbs',
                'work:bible-jeremiah',
                'work:bible-ezekiel'
            ],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:bible-exodus',
                    'canonicalWorkTitle': 'Exodus',
                    'displayWorkTitlePtBr': 'Êxodo',
                    'gbwwVolume': None,
                    'locatorRaw': 'Exodus, 22:25',
                    'locators': [{'locatorRaw': '22:25', 'subLocator': '22:25'}]
                },
                {
                    'workSegmentIndex': 2,
                    'workId': 'work:bible-leviticus',
                    'canonicalWorkTitle': 'Leviticus',
                    'displayWorkTitlePtBr': 'Levítico',
                    'gbwwVolume': None,
                    'locatorRaw': 'Leviticus, 25:35-37',
                    'locators': [{'locatorRaw': '25:35-37', 'subLocator': '25:35-37'}]
                },
                {
                    'workSegmentIndex': 3,
                    'workId': 'work:bible-deuteronomy',
                    'canonicalWorkTitle': 'Deuteronomy',
                    'displayWorkTitlePtBr': 'Deuteronômio',
                    'gbwwVolume': None,
                    'locatorRaw': 'Deuteronomy, 23:19-20; 24:10-13',
                    'locators': [{'locatorRaw': '23:19-20; 24:10-13', 'subLocator': '23:19-20; 24:10-13'}]
                },
                {
                    'workSegmentIndex': 4,
                    'workId': 'work:bible-nehemiah',
                    'canonicalWorkTitle': 'Nehemiah (II Esdras)',
                    'displayWorkTitlePtBr': 'Neemias',
                    'gbwwVolume': None,
                    'locatorRaw': 'Nehemiah, 5 (D) II Esdras, 5',
                    'locators': [{'locatorRaw': '5 (D) II Esdras, 5', 'subLocator': '5'}]
                },
                {
                    'workSegmentIndex': 5,
                    'workId': 'work:bible-psalms',
                    'canonicalWorkTitle': 'Psalms',
                    'displayWorkTitlePtBr': 'Salmos',
                    'gbwwVolume': None,
                    'locatorRaw': 'Psalms, 15:5 (D) Psalms, 14:5',
                    'locators': [{'locatorRaw': '15:5 (D) Psalms, 14:5', 'subLocator': '15:5'}]
                },
                {
                    'workSegmentIndex': 6,
                    'workId': 'work:bible-proverbs',
                    'canonicalWorkTitle': 'Proverbs',
                    'displayWorkTitlePtBr': 'Provérbios',
                    'gbwwVolume': None,
                    'locatorRaw': 'Proverbs, 28:8',
                    'locators': [{'locatorRaw': '28:8', 'subLocator': '28:8'}]
                },
                {
                    'workSegmentIndex': 7,
                    'workId': 'work:bible-jeremiah',
                    'canonicalWorkTitle': 'Jeremiah',
                    'displayWorkTitlePtBr': 'Jeremias',
                    'gbwwVolume': None,
                    'locatorRaw': 'Jeremiah, 15:10 (D) Jeremias, 15:10',
                    'locators': [{'locatorRaw': '15:10 (D) Jeremias, 15:10', 'subLocator': '15:10'}]
                },
                {
                    'workSegmentIndex': 8,
                    'workId': 'work:bible-ezekiel',
                    'canonicalWorkTitle': 'Ezekiel',
                    'displayWorkTitlePtBr': 'Ezequiel',
                    'gbwwVolume': None,
                    'locatorRaw': 'Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12',
                    'locators': [{'locatorRaw': '18:4-21 esp 18:8, 18:13, 18:17, 22:12', 'subLocator': '18:4-21'}]
                }
            ],
            'locatorRaw': 'Exodus, 22:25 / Leviticus, 25:35-37 / Deuteronomy, 23:19-20; 24:10-13 / Nehemiah, 5 (D) II Esdras, 5 / Psalms, 15:5 (D) Psalms, 14:5 / Proverbs, 28:8 / Jeremiah, 15:10 (D) Jeremias, 15:10 / Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; segmentação de 8 livros bíblicos veterotestamentários'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-antigo-testamento|Antigo Testamento]]',
            'obras': [
                '[[obra-exodo-antigo-testamento|Êxodo]]',
                '[[obra-levitico-antigo-testamento|Levítico]]',
                '[[obra-deuteronomio-antigo-testamento|Deuteronômio]]',
                '[[obra-neemias-antigo-testamento|Neemias]]',
                '[[obra-salmos-antigo-testamento|Salmos]]',
                '[[obra-proverbios-antigo-testamento|Provérbios]]',
                '[[obra-jeremias-antigo-testamento|Jeremias]]',
                '[[obra-ezequiel-antigo-testamento|Ezequiel]]'
            ],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (01) - Antigo Testamento'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (01): [[autor-antigo-testamento|Antigo Testamento]]',
        'author_link': '[[autor-antigo-testamento|Antigo Testamento]]',
        'vol_display': 'Corpus Bíblico (Não numerado)',
        'locator': 'Exodus, 22:25 / Leviticus, 25:35-37 / Deuteronomy, 23:19-20; 24:10-13 / Nehemiah, 5 (D) II Esdras, 5 / Psalms, 15:5 (D) Psalms, 14:5 / Proverbs, 28:8 / Jeremiah, 15:10 (D) Jeremias, 15:10 / Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12',
        'works_table': '''| 1 | [[obra-exodo-antigo-testamento|Êxodo]] (*Exodus*) | Corpus Bíblico | `Exodus, 22:25` |
| 2 | [[obra-levitico-antigo-testamento|Levítico]] (*Leviticus*) | Corpus Bíblico | `Leviticus, 25:35-37` |
| 3 | [[obra-deuteronomio-antigo-testamento|Deuteronômio]] (*Deuteronomy*) | Corpus Bíblico | `Deuteronomy, 23:19-20; 24:10-13` |
| 4 | [[obra-neemias-antigo-testamento|Neemias]] (*Nehemiah*) | Corpus Bíblico | `Nehemiah, 5 (D) II Esdras, 5` |
| 5 | [[obra-salmos-antigo-testamento|Salmos]] (*Psalms*) | Corpus Bíblico | `Psalms, 15:5 (D) Psalms, 14:5` |
| 6 | [[obra-proverbios-antigo-testamento|Provérbios]] (*Proverbs*) | Corpus Bíblico | `Proverbs, 28:8` |
| 7 | [[obra-jeremias-antigo-testamento|Jeremias]] (*Jeremiah*) | Corpus Bíblico | `Jeremiah, 15:10 (D) Jeremias, 15:10` |
| 8 | [[obra-ezequiel-antigo-testamento|Ezequiel]] (*Ezekiel*) | Corpus Bíblico | `Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12` |'''
    },
    {
        'file_name': 'ref-42-8d-02-platao.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:02-plato',
            'slug': 'ref-42-8d-02-platao',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 2,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 7,
            'volume-gbww': '[[vol-07|Volume 7]]',
            'authorId': 'author:plato',
            'authorCanonicalName': 'Plato',
            'workIds': ['work:republic-plato', 'work:laws-plato'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:republic-plato',
                    'canonicalWorkTitle': 'Republic',
                    'displayWorkTitlePtBr': 'A República',
                    'gbwwVolume': 7,
                    'locatorRaw': 'Republic, BK viii, 408c-d',
                    'locators': [{'locatorRaw': 'BK viii, 408c-d', 'subLocator': 'BK viii'}]
                },
                {
                    'workSegmentIndex': 2,
                    'workId': 'work:laws-plato',
                    'canonicalWorkTitle': 'Laws',
                    'displayWorkTitlePtBr': 'As Leis',
                    'gbwwVolume': 7,
                    'locatorRaw': 'Laws, BK v, 694c-d; BK xi, 775c-d',
                    'locators': [{'locatorRaw': 'BK v, 694c-d; BK xi, 775c-d', 'subLocator': 'BK v, BK xi'}]
                }
            ],
            'locatorRaw': 'Republic, BK viii, 408c-d / Laws, BK v, 694c-d; BK xi, 775c-d',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-platao|Platão]]',
            'obras': ['[[obra-republica-platao|A República]]', '[[obra-leis-platao|As Leis]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (02) - Platão'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (02): [[autor-platao|Platão]]',
        'author_link': '[[autor-platao|Platão]]',
        'vol_display': 'Volume 7',
        'locator': 'Republic, BK viii, 408c-d / Laws, BK v, 694c-d; BK xi, 775c-d',
        'works_table': '''| 1 | [[obra-republica-platao|A República]] (*Republic*) | [[vol-07|Vol. 7]] | `Republic, BK viii, 408c-d` |
| 2 | [[obra-leis-platao|As Leis]] (*Laws*) | [[vol-07|Vol. 7]] | `Laws, BK v, 694c-d; BK xi, 775c-d` |'''
    },
    {
        'file_name': 'ref-42-8d-03-aristoteles.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:03-aristotle',
            'slug': 'ref-42-8d-03-aristoteles',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 3,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 9,
            'volume-gbww': '[[vol-09|Volume 9]]',
            'authorId': 'author:aristotle',
            'authorCanonicalName': 'Aristotle',
            'workIds': ['work:nicomachean-ethics', 'work:politics-aristotle', 'work:athenian-constitution'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:nicomachean-ethics',
                    'canonicalWorkTitle': 'Nicomachean Ethics',
                    'displayWorkTitlePtBr': 'Ética a Nicômaco',
                    'gbwwVolume': 9,
                    'locatorRaw': 'Ethics, BK v, CH 2 [1130b13-b8] 377c-378a; CH 5 [1133a5-b29] 380d-381c; BK ix, CH 2 [1164b10-1165a11] 417d-418a',
                    'locators': [{'locatorRaw': 'BK v, CH 2 377c-378a; CH 5 380d-381c; BK ix, CH 2 417d-418a', 'subLocator': 'BK v, BK ix'}]
                },
                {
                    'workSegmentIndex': 2,
                    'workId': 'work:politics-aristotle',
                    'canonicalWorkTitle': 'Politics',
                    'displayWorkTitlePtBr': 'Política',
                    'gbwwVolume': 9,
                    'locatorRaw': 'Politics, BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d',
                    'locators': [{'locatorRaw': 'BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d', 'subLocator': 'BK i, CH 9-10'}]
                },
                {
                    'workSegmentIndex': 3,
                    'workId': 'work:athenian-constitution',
                    'canonicalWorkTitle': 'Athenian Constitution',
                    'displayWorkTitlePtBr': 'Constituição de Atenas',
                    'gbwwVolume': 9,
                    'locatorRaw': 'Athenian Constitution, CH 12, par 4 557d-558a',
                    'locators': [{'locatorRaw': 'CH 12, par 4 557d-558a', 'subLocator': 'CH 12'}]
                }
            ],
            'locatorRaw': 'Ethics, BK v, CH 2 [1130b13-b8] 377c-378a; CH 5 [1133a5-b29] 380d-381c; BK ix, CH 2 [1164b10-1165a11] 417d-418a / Politics, BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d / Athenian Constitution, CH 12, par 4 557d-558a',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; 3 obras aristotélicas'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-aristoteles|Aristóteles]]',
            'obras': ['[[obra-etica-a-nicomaco-aristoteles|Ética a Nicômaco]]', '[[obra-politica-aristoteles|Política]]', '[[obra-constituicao-de-atenas-aristoteles|Constituição de Atenas]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (03) - Aristóteles'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (03): [[autor-aristoteles|Aristóteles]]',
        'author_link': '[[autor-aristoteles|Aristóteles]]',
        'vol_display': 'Volume 9',
        'locator': 'Ethics, BK v, CH 2 [1130b13-b8] 377c-378a; CH 5 [1133a5-b29] 380d-381c; BK ix, CH 2 [1164b10-1165a11] 417d-418a / Politics, BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d / Athenian Constitution, CH 12, par 4 557d-558a',
        'works_table': '''| 1 | [[obra-etica-a-nicomaco-aristoteles|Ética a Nicômaco]] (*Nicomachean Ethics*) | [[vol-09|Vol. 9]] | `Ethics, BK v, CH 2 [1130b13-b8] 377c-378a; CH 5 [1133a5-b29] 380d-381c; BK ix, CH 2 [1164b10-1165a11] 417d-418a` |
| 2 | [[obra-politica-aristoteles|Política]] (*Politics*) | [[vol-09|Vol. 9]] | `Politics, BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d` |
| 3 | [[obra-constituicao-de-atenas-aristoteles|Constituição de Atenas]] (*Athenian Constitution*) | [[vol-09|Vol. 9]] | `Athenian Constitution, CH 12, par 4 557d-558a` |'''
    },
    {
        'file_name': 'ref-42-8d-04-plutarco.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:04-plutarch',
            'slug': 'ref-42-8d-04-plutarco',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 4,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 14,
            'volume-gbww': '[[vol-14|Volume 14]]',
            'authorId': 'author:plutarch',
            'authorCanonicalName': 'Plutarch',
            'workIds': ['work:marcus-cato-plutarch', 'work:lucullus-plutarch'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:marcus-cato-plutarch',
                    'canonicalWorkTitle': 'Marcus Cato',
                    'displayWorkTitlePtBr': 'Marco Catão',
                    'gbwwVolume': 14,
                    'locatorRaw': 'Marcus Cato, 287c-d',
                    'locators': [{'locatorRaw': '287c-d', 'subLocator': '287c-d'}]
                },
                {
                    'workSegmentIndex': 2,
                    'workId': 'work:lucullus-plutarch',
                    'canonicalWorkTitle': 'Lucullus',
                    'displayWorkTitlePtBr': 'Lúculo',
                    'gbwwVolume': 14,
                    'locatorRaw': 'Lucullus, 409b-d',
                    'locators': [{'locatorRaw': '409b-d', 'subLocator': '409b-d'}]
                }
            ],
            'locatorRaw': 'Marcus Cato, 287c-d / Lucullus, 409b-d',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; 2 obras plutarquianas'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-plutarco|Plutarco]]',
            'obras': ['[[obra-marco-catao-plutarco|Marco Catão]]', '[[obra-luculo-plutarco|Lúculo]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (04) - Plutarco'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (04): [[autor-plutarco|Plutarco]]',
        'author_link': '[[autor-plutarco|Plutarco]]',
        'vol_display': 'Volume 14',
        'locator': 'Marcus Cato, 287c-d / Lucullus, 409b-d',
        'works_table': '''| 1 | [[obra-marco-catao-plutarco|Marco Catão]] (*Marcus Cato*) | [[vol-14|Vol. 14]] | `Marcus Cato, 287c-d` |
| 2 | [[obra-luculo-plutarco|Lúculo]] (*Lucullus*) | [[vol-14|Vol. 14]] | `Lucullus, 409b-d` |'''
    },
    {
        'file_name': 'ref-42-8d-05-tacito.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:05-tacitus',
            'slug': 'ref-42-8d-05-tacito',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 5,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 15,
            'volume-gbww': '[[vol-15|Volume 15]]',
            'authorId': 'author:tacitus',
            'authorCanonicalName': 'Cornelius Tacitus',
            'workIds': ['work:annals-tacitus'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:annals-tacitus',
                    'canonicalWorkTitle': 'The Annals',
                    'displayWorkTitlePtBr': 'Os Anais',
                    'gbwwVolume': 15,
                    'locatorRaw': 'Annals, BK vi, 90a-c',
                    'locators': [{'locatorRaw': 'BK vi, 90a-c', 'subLocator': 'BK vi'}]
                }
            ],
            'locatorRaw': 'Annals, BK vi, 90a-c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; correção do volume OCR 6 -> 15'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-tacito|Tácito]]',
            'obras': ['[[obra-anais-tacito|Os Anais]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (05) - Tácito'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (05): [[autor-tacito|Tácito]]',
        'author_link': '[[autor-tacito|Tácito]]',
        'vol_display': 'Volume 15',
        'locator': 'Annals, BK vi, 90a-c',
        'works_table': '''| 1 | [[obra-anais-tacito|Os Anais]] (*The Annals*) | [[vol-15|Vol. 15]] | `Annals, BK vi, 90a-c` |'''
    },
    {
        'file_name': 'ref-42-8d-06-tomas-de-aquino.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:06-aquinas',
            'slug': 'ref-42-8d-06-tomas-de-aquino',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 6,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 20,
            'volume-gbww': '[[vol-20|Volume 20]]',
            'authorId': 'author:aquinas',
            'authorCanonicalName': 'Thomas Aquinas',
            'workIds': ['work:summa-theologica'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:summa-theologica',
                    'canonicalWorkTitle': 'Summa Theologica',
                    'displayWorkTitlePtBr': 'Suma Teológica',
                    'gbwwVolume': 20,
                    'locatorRaw': 'Summa Theologica, PART I-II, Q 105, A 2, REP 4 309d-316a',
                    'locators': [{'locatorRaw': 'PART I-II, Q 105, A 2, REP 4 309d-316a', 'subLocator': 'PART I-II, Q 105, A 2, REP 4'}]
                }
            ],
            'locatorRaw': 'Summa Theologica, PART I-II, Q 105, A 2, REP 4 309d-316a',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868; correção OCR PART MI -> PART I-II'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-tomas-de-aquino|Tomás de Aquino]]',
            'obras': ['[[obra-suma-teologica-aquino|Suma Teológica]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (06) - Tomás de Aquino'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (06): [[autor-tomas-de-aquino|Tomás de Aquino]]',
        'author_link': '[[autor-tomas-de-aquino|Tomás de Aquino]]',
        'vol_display': 'Volume 20',
        'locator': 'Summa Theologica, PART I-II, Q 105, A 2, REP 4 309d-316a',
        'works_table': '''| 1 | [[obra-suma-teologica-aquino|Suma Teológica]] (*Summa Theologica*) | [[vol-20|Vol. 20]] | `Summa Theologica, PART I-II, Q 105, A 2, REP 4 309d-316a` |'''
    },
    {
        'file_name': 'ref-42-8d-07-dante.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:07-dante',
            'slug': 'ref-42-8d-07-dante',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 7,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 21,
            'volume-gbww': '[[vol-21|Volume 21]]',
            'authorId': 'author:dante',
            'authorCanonicalName': 'Dante Alighieri',
            'workIds': ['work:divine-comedy-dante'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:divine-comedy-dante',
                    'canonicalWorkTitle': 'The Divine Comedy',
                    'displayWorkTitlePtBr': 'A Divina Comédia',
                    'gbwwVolume': 21,
                    'locatorRaw': 'Divine Comedy, HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c',
                    'locators': [{'locatorRaw': 'HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c', 'subLocator': 'HELL, xi, xvii'}]
                }
            ],
            'locatorRaw': 'Divine Comedy, HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-dante-alighieri|Dante Alighieri]]',
            'obras': ['[[obra-divina-comedia-dante|A Divina Comédia]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (07) - Dante Alighieri'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (07): [[autor-dante-alighieri|Dante Alighieri]]',
        'author_link': '[[autor-dante-alighieri|Dante Alighieri]]',
        'vol_display': 'Volume 21',
        'locator': 'Divine Comedy, HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c',
        'works_table': '''| 1 | [[obra-divina-comedia-dante|A Divina Comédia]] (*The Divine Comedy*) | [[vol-21|Vol. 21]] | `Divine Comedy, HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c` |'''
    },
    {
        'file_name': 'ref-42-8d-08-rabelais.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:08-rabelais',
            'slug': 'ref-42-8d-08-rabelais',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 8,
            'syntopiconPage': 868,
            'editionId': 'gbww-1952',
            'gbwwVolume': 24,
            'volume-gbww': '[[vol-24|Volume 24]]',
            'authorId': 'author:rabelais',
            'authorCanonicalName': 'François Rabelais',
            'workIds': ['work:gargantua-pantagruel-rabelais'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:gargantua-pantagruel-rabelais',
                    'canonicalWorkTitle': 'Gargantua and Pantagruel',
                    'displayWorkTitlePtBr': 'Gargântua e Pantagruel',
                    'gbwwVolume': 24,
                    'locatorRaw': 'Gargantua and Pantagruel, BK iii, 133b-140b',
                    'locators': [{'locatorRaw': 'BK iii, 133b-140b', 'subLocator': 'BK iii'}]
                }
            ],
            'locatorRaw': 'Gargantua and Pantagruel, BK iii, 133b-140b',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 868'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-francois-rabelais|François Rabelais]]',
            'obras': ['[[obra-gargantua-e-pantagruel-rabelais|Gargântua e Pantagruel]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (08) - François Rabelais'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (08): [[autor-francois-rabelais|François Rabelais]]',
        'author_link': '[[autor-francois-rabelais|François Rabelais]]',
        'vol_display': 'Volume 24',
        'locator': 'Gargantua and Pantagruel, BK iii, 133b-140b',
        'works_table': '''| 1 | [[obra-gargantua-e-pantagruel-rabelais|Gargântua e Pantagruel]] (*Gargantua and Pantagruel*) | [[vol-24|Vol. 24]] | `Gargantua and Pantagruel, BK iii, 133b-140b` |'''
    },
    {
        'file_name': 'ref-42-8d-09-shakespeare.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:09-shakespeare',
            'slug': 'ref-42-8d-09-shakespeare',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 9,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 26,
            'volume-gbww': '[[vol-26|Volume 26]]',
            'authorId': 'author:shakespeare',
            'authorCanonicalName': 'William Shakespeare',
            'workIds': ['work:merchant-of-venice-shakespeare'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:merchant-of-venice-shakespeare',
                    'canonicalWorkTitle': 'The Merchant of Venice',
                    'displayWorkTitlePtBr': 'O Mercador de Veneza',
                    'gbwwVolume': 26,
                    'locatorRaw': 'Merchant of Venice, ACT i, sc iii 409c-411b',
                    'locators': [{'locatorRaw': 'ACT i, sc iii 409c-411b', 'subLocator': 'ACT i, sc iii'}]
                }
            ],
            'locatorRaw': 'Merchant of Venice, ACT i, sc iii 409c-411b',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-william-shakespeare|William Shakespeare]]',
            'obras': ['[[obra-mercador-de-veneza-shakespeare|O Mercador de Veneza]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (09) - William Shakespeare'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (09): [[autor-william-shakespeare|William Shakespeare]]',
        'author_link': '[[autor-william-shakespeare|William Shakespeare]]',
        'vol_display': 'Volume 26',
        'locator': 'Merchant of Venice, ACT i, sc iii 409c-411b',
        'works_table': '''| 1 | [[obra-mercador-de-veneza-shakespeare|O Mercador de Veneza]] (*The Merchant of Venice*) | [[vol-26|Vol. 26]] | `Merchant of Venice, ACT i, sc iii 409c-411b` |'''
    },
    {
        'file_name': 'ref-42-8d-10-pascal.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:10-pascal',
            'slug': 'ref-42-8d-10-pascal',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 10,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 33,
            'volume-gbww': '[[vol-33|Volume 33]]',
            'authorId': 'author:pascal',
            'authorCanonicalName': 'Blaise Pascal',
            'workIds': ['work:provincial-letters-pascal'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:provincial-letters-pascal',
                    'canonicalWorkTitle': 'The Provincial Letters',
                    'displayWorkTitlePtBr': 'Cartas Provinciais',
                    'gbwwVolume': 33,
                    'locatorRaw': 'Provincial Letters, 55a-57a',
                    'locators': [{'locatorRaw': '55a-57a', 'subLocator': '55a-57a'}]
                }
            ],
            'locatorRaw': 'Provincial Letters, 55a-57a',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869; correção OCR 55a*57a -> 55a-57a'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-blaise-pascal|Blaise Pascal]]',
            'obras': ['[[obra-cartas-provinciais-pascal|Cartas Provinciais]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (10) - Blaise Pascal'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (10): [[autor-blaise-pascal|Blaise Pascal]]',
        'author_link': '[[autor-blaise-pascal|Blaise Pascal]]',
        'vol_display': 'Volume 33',
        'locator': 'Provincial Letters, 55a-57a',
        'works_table': '''| 1 | [[obra-cartas-provinciais-pascal|Cartas Provinciais]] (*The Provincial Letters*) | [[vol-33|Vol. 33]] | `Provincial Letters, 55a-57a` |'''
    },
    {
        'file_name': 'ref-42-8d-11-montesquieu.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:11-montesquieu',
            'slug': 'ref-42-8d-11-montesquieu',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 11,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 38,
            'volume-gbww': '[[vol-38|Volume 38]]',
            'authorId': 'author:montesquieu',
            'authorCanonicalName': 'Montesquieu',
            'workIds': ['work:spirit-of-laws-montesquieu'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:spirit-of-laws-montesquieu',
                    'canonicalWorkTitle': 'The Spirit of Laws',
                    'displayWorkTitlePtBr': 'O Espírito das Leis',
                    'gbwwVolume': 38,
                    'locatorRaw': 'Spirit of Laws, BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c',
                    'locators': [{'locatorRaw': 'BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c', 'subLocator': 'BK v, BK xii, BK xxi, BK xxii'}]
                }
            ],
            'locatorRaw': 'Spirit of Laws, BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-montesquieu|Montesquieu]]',
            'obras': ['[[obra-o-espirito-das-leis-montesquieu|O Espírito das Leis]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (11) - Montesquieu'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (11): [[autor-montesquieu|Montesquieu]]',
        'author_link': '[[autor-montesquieu|Montesquieu]]',
        'vol_display': 'Volume 38',
        'locator': 'Spirit of Laws, BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c',
        'works_table': '''| 1 | [[obra-o-espirito-das-leis-montesquieu|O Espírito das Leis]] (*The Spirit of Laws*) | [[vol-38|Vol. 38]] | `Spirit of Laws, BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c` |'''
    },
    {
        'file_name': 'ref-42-8d-12-adam-smith.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:12-smith',
            'slug': 'ref-42-8d-12-adam-smith',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 12,
            'syntopiconPage': 869,
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
                    'locatorRaw': 'Wealth of Nations, BK i, 37b-41d; BK ii, 140b; 154c-155a',
                    'locators': [{'locatorRaw': 'BK i, 37b-41d; BK ii, 140b; 154c-155a', 'subLocator': 'BK i, BK ii'}]
                }
            ],
            'locatorRaw': 'Wealth of Nations, BK i, 37b-41d; BK ii, 140b; 154c-155a',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-adam-smith|Adam Smith]]',
            'obras': ['[[obra-riqueza-das-nacoes-smith|A Riqueza das Nações]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (12) - Adam Smith'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (12): [[autor-adam-smith|Adam Smith]]',
        'author_link': '[[autor-adam-smith|Adam Smith]]',
        'vol_display': 'Volume 39',
        'locator': 'Wealth of Nations, BK i, 37b-41d; BK ii, 140b; 154c-155a',
        'works_table': '''| 1 | [[obra-riqueza-das-nacoes-smith|A Riqueza das Nações]] (*The Wealth of Nations*) | [[vol-39|Vol. 39]] | `Wealth of Nations, BK i, 37b-41d; BK ii, 140b; 154c-155a` |'''
    },
    {
        'file_name': 'ref-42-8d-13-edward-gibbon-vol-40.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:13-gibbon-vol-40',
            'slug': 'ref-42-8d-13-edward-gibbon-vol-40',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 13,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 40,
            'volume-gbww': '[[vol-40|Volume 40]]',
            'authorId': 'author:gibbon',
            'authorCanonicalName': 'Edward Gibbon',
            'workIds': ['work:decline-and-fall'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:decline-and-fall',
                    'canonicalWorkTitle': 'The Decline and Fall of the Roman Empire',
                    'displayWorkTitlePtBr': 'Declínio e Queda do Império Romano',
                    'gbwwVolume': 40,
                    'locatorRaw': 'Decline and Fall, 498c',
                    'locators': [{'locatorRaw': '498c', 'subLocator': '498c'}]
                }
            ],
            'locatorRaw': 'Decline and Fall, 498c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869; Gibbon Vol. 40'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-edward-gibbon|Edward Gibbon]]',
            'obras': ['[[obra-declinio-e-queda-gibbon|Declínio e Queda do Império Romano]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (13) - Edward Gibbon (Vol. 40)'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (13): [[autor-edward-gibbon|Edward Gibbon]] (Vol. 40)',
        'author_link': '[[autor-edward-gibbon|Edward Gibbon]]',
        'vol_display': 'Volume 40',
        'locator': 'Decline and Fall, 498c',
        'works_table': '''| 1 | [[obra-declinio-e-queda-gibbon|Declínio e Queda do Império Romano]] (*The Decline and Fall of the Roman Empire*) | [[vol-40|Vol. 40]] | `Decline and Fall, 498c` |'''
    },
    {
        'file_name': 'ref-42-8d-14-edward-gibbon-vol-41.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:14-gibbon-vol-41',
            'slug': 'ref-42-8d-14-edward-gibbon-vol-41',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 14,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 41,
            'volume-gbww': '[[vol-41|Volume 41]]',
            'authorId': 'author:gibbon',
            'authorCanonicalName': 'Edward Gibbon',
            'workIds': ['work:decline-and-fall'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:decline-and-fall',
                    'canonicalWorkTitle': 'The Decline and Fall of the Roman Empire',
                    'displayWorkTitlePtBr': 'Declínio e Queda do Império Romano',
                    'gbwwVolume': 41,
                    'locatorRaw': 'Decline and Fall, 90d-91a',
                    'locators': [{'locatorRaw': '90d-91a', 'subLocator': '90d-91a'}]
                }
            ],
            'locatorRaw': 'Decline and Fall, 90d-91a',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869; Gibbon Vol. 41'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-edward-gibbon|Edward Gibbon]]',
            'obras': ['[[obra-declinio-e-queda-gibbon|Declínio e Queda do Império Romano]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (14) - Edward Gibbon (Vol. 41)'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (14): [[autor-edward-gibbon|Edward Gibbon]] (Vol. 41)',
        'author_link': '[[autor-edward-gibbon|Edward Gibbon]]',
        'vol_display': 'Volume 41',
        'locator': 'Decline and Fall, 90d-91a',
        'works_table': '''| 1 | [[obra-declinio-e-queda-gibbon|Declínio e Queda do Império Romano]] (*The Decline and Fall of the Roman Empire*) | [[vol-41|Vol. 41]] | `Decline and Fall, 90d-91a` |'''
    },
    {
        'file_name': 'ref-42-8d-15-immanuel-kant.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:15-kant',
            'slug': 'ref-42-8d-15-immanuel-kant',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 15,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 42,
            'volume-gbww': '[[vol-42|Volume 42]]',
            'authorId': 'author:kant',
            'authorCanonicalName': 'Immanuel Kant',
            'workIds': ['work:science-of-right'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:science-of-right',
                    'canonicalWorkTitle': 'The Science of Right',
                    'displayWorkTitlePtBr': 'A Ciência do Direito',
                    'gbwwVolume': 42,
                    'locatorRaw': 'Science of Right, 424a-425b',
                    'locators': [{'locatorRaw': '424a-425b', 'subLocator': '424a-425b'}]
                }
            ],
            'locatorRaw': 'Science of Right, 424a-425b',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-immanuel-kant|Immanuel Kant]]',
            'obras': ['[[obra-ciencia-do-direito-kant|A Ciência do Direito]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (15) - Immanuel Kant'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (15): [[autor-immanuel-kant|Immanuel Kant]]',
        'author_link': '[[autor-immanuel-kant|Immanuel Kant]]',
        'vol_display': 'Volume 42',
        'locator': 'Science of Right, 424a-425b',
        'works_table': '''| 1 | [[obra-ciencia-do-direito-kant|A Ciência do Direito]] (*The Science of Right*) | [[vol-42|Vol. 42]] | `Science of Right, 424a-425b` |'''
    },
    {
        'file_name': 'ref-42-8d-16-james-boswell.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:16-boswell',
            'slug': 'ref-42-8d-16-james-boswell',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 16,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 44,
            'volume-gbww': '[[vol-44|Volume 44]]',
            'authorId': 'author:boswell',
            'authorCanonicalName': 'James Boswell',
            'workIds': ['work:life-of-johnson'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:life-of-johnson',
                    'canonicalWorkTitle': 'The Life of Samuel Johnson, LL.D.',
                    'displayWorkTitlePtBr': 'Vida de Samuel Johnson',
                    'gbwwVolume': 44,
                    'locatorRaw': 'Johnson, 304b-c, 409a-b',
                    'locators': [{'locatorRaw': '304b-c, 409a-b', 'subLocator': '304b-c, 409a-b'}]
                }
            ],
            'locatorRaw': 'Johnson, 304b-c, 409a-b',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-james-boswell|James Boswell]]',
            'obras': ['[[obra-vida-de-johnson-boswell|Vida de Samuel Johnson]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (16) - James Boswell'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (16): [[autor-james-boswell|James Boswell]]',
        'author_link': '[[autor-james-boswell|James Boswell]]',
        'vol_display': 'Volume 44',
        'locator': 'Johnson, 304b-c, 409a-b',
        'works_table': '''| 1 | [[obra-vida-de-johnson-boswell|Vida de Samuel Johnson]] (*The Life of Samuel Johnson, LL.D.*) | [[vol-44|Vol. 44]] | `Johnson, 304b-c, 409a-b` |'''
    },
    {
        'file_name': 'ref-42-8d-17-gwf-hegel.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:17-hegel',
            'slug': 'ref-42-8d-17-gwf-hegel',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 17,
            'syntopiconPage': 869,
            'editionId': 'gbww-1952',
            'gbwwVolume': 46,
            'volume-gbww': '[[vol-46|Volume 46]]',
            'authorId': 'author:hegel',
            'authorCanonicalName': 'Georg Wilhelm Friedrich Hegel',
            'workIds': ['work:philosophy-of-history'],
            'workSegments': [
                {
                    'workSegmentIndex': 1,
                    'workId': 'work:philosophy-of-history',
                    'canonicalWorkTitle': 'The Philosophy of History',
                    'displayWorkTitlePtBr': 'Filosofia da História',
                    'gbwwVolume': 46,
                    'locatorRaw': 'Philosophy of History, PART iv, 353b-c',
                    'locators': [{'locatorRaw': 'PART iv, 353b-c', 'subLocator': 'PART iv'}]
                }
            ],
            'locatorRaw': 'Philosophy of History, PART iv, 353b-c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-gwf-hegel|G. W. F. Hegel]]',
            'obras': ['[[obra-filosofia-da-historia-hegel|Filosofia da História]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (17) - G. W. F. Hegel'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (17): [[autor-gwf-hegel|G. W. F. Hegel]]',
        'author_link': '[[autor-gwf-hegel|G. W. F. Hegel]]',
        'vol_display': 'Volume 46',
        'locator': 'Philosophy of History, PART iv, 353b-c',
        'works_table': '''| 1 | [[obra-filosofia-da-historia-hegel|Filosofia da História]] (*The Philosophy of History*) | [[vol-46|Vol. 46]] | `Philosophy of History, PART iv, 353b-c` |'''
    },
    {
        'file_name': 'ref-42-8d-18-karl-marx.md',
        'data': {
            'tipo': 'referencia',
            'id': 'ref:justica:8d:18-karl-marx',
            'slug': 'ref-42-8d-18-karl-marx',
            'topicId': 'topic:justica:8d',
            'ideaId': 'idea:justica',
            'orderInTopic': 18,
            'syntopiconPage': 869,
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
                    'locatorRaw': 'Capital, 77c-78b; 252b; 293a-d [fn 1]; 371c-372c',
                    'locators': [{'locatorRaw': '77c-78b; 252b; 293a-d [fn 1]; 371c-372c', 'subLocator': '77c-78b, 252b, 293a-d, 371c-372c'}]
                }
            ],
            'locatorRaw': 'Capital, 77c-78b; 252b; 293a-d [fn 1]; 371c-372c',
            'passageIds': [],
            'provenance': 'original-corpus',
            'epistemology': 'canonical',
            'verification': 'verified',
            'source-id': 'source:pdf-justice-1952',
            'warningResolution': 'resolved-by-visual-audit',
            'warningsResolved': ['Conferência visual direta contra Justice.pdf p. 869; restauração de Capital no início'],
            'warningsOpen': [],
            'topico': '[[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]',
            'autor': '[[autor-karl-marx|Karl Marx]]',
            'obras': ['[[obra-o-capital-marx|O Capital]]'],
            'tags': ['type/referencia', 'type/canonico', 'theme/justica'],
            'aliases': ['Ref. 42.8d (18) - Karl Marx'],
            'status': 'ativo',
            'created': '2026-09-22',
            'modified': '2026-09-22'
        },
        'title': 'Ref. 42.8d (18): [[autor-karl-marx|Karl Marx]]',
        'author_link': '[[autor-karl-marx|Karl Marx]]',
        'vol_display': 'Volume 50',
        'locator': 'Capital, 77c-78b; 252b; 293a-d [fn 1]; 371c-372c',
        'works_table': '''| 1 | [[obra-o-capital-marx|O Capital]] (*Capital*) | [[vol-50|Vol. 50]] | `Capital, 77c-78b; 252b; 293a-d [fn 1]; 371c-372c` |'''
    }
]

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ref_dir = os.path.join(base_dir, '03-referencias', 'justica')

for item in refs_data:
    p = os.path.join(ref_dir, item['file_name'])
    yaml_header = yaml.dump(item['data'], allow_unicode=True, sort_keys=False)
    vol_line = f"Volume GBWW: {item['vol_display']}" if item['vol_display'] else "Volume GBWW: Não numerado"
    page_num = item['data']['syntopiconPage']
    body = f"""---
{yaml_header}---

# {item['title']}

> **Tópico Canônico:** [[topico-42-8d|42.8d: A justiça e o uso do dinheiro: usura e taxas de juros]]  
> **Autor:** {item['author_link']}  
> **{vol_line}** | **Página Syntopicon:** {page_num}  
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
    print('Materialized:', item['file_name'])
