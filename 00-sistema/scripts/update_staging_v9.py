import json
from datetime import datetime, timezone

# 1. Update referencias-candidatas.json
with open('00-sistema/staging/referencias-candidatas.json', 'r', encoding='utf-8') as f:
    cands = json.load(f)

for c in cands:
    if c.get('topicId') == 'topic:justica:8d':
        c['verification'] = 'verified'
        order = c.get('orderInTopic')
        if order == 1:
            c['locatorRaw'] = 'Exodus, 22:25 / Leviticus, 25:35-37 / Deuteronomy, 23:19-20; 24:10-13 / Nehemiah, 5 (D) II Esdras, 5 / Psalms, 15:5 (D) Psalms, 14:5 / Proverbs, 28:8 / Jeremiah, 15:10 (D) Jeremias, 15:10 / Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12'
            c['workSegments'] = [
                {'workSegmentIndex': 1, 'workId': 'work:bible-exodus', 'workTitle': 'Exodus', 'locatorRaw': 'Exodus, 22:25', 'locators': ['22:25']},
                {'workSegmentIndex': 2, 'workId': 'work:bible-leviticus', 'workTitle': 'Leviticus', 'locatorRaw': 'Leviticus, 25:35-37', 'locators': ['25:35-37']},
                {'workSegmentIndex': 3, 'workId': 'work:bible-deuteronomy', 'workTitle': 'Deuteronomy', 'locatorRaw': 'Deuteronomy, 23:19-20; 24:10-13', 'locators': ['23:19-20; 24:10-13']},
                {'workSegmentIndex': 4, 'workId': 'work:bible-nehemiah', 'workTitle': 'Nehemiah (II Esdras)', 'locatorRaw': 'Nehemiah, 5 (D) II Esdras, 5', 'locators': ['5 (D) II Esdras, 5']},
                {'workSegmentIndex': 5, 'workId': 'work:bible-psalms', 'workTitle': 'Psalms', 'locatorRaw': 'Psalms, 15:5 (D) Psalms, 14:5', 'locators': ['15:5 (D) Psalms, 14:5']},
                {'workSegmentIndex': 6, 'workId': 'work:bible-proverbs', 'workTitle': 'Proverbs', 'locatorRaw': 'Proverbs, 28:8', 'locators': ['28:8']},
                {'workSegmentIndex': 7, 'workId': 'work:bible-jeremiah', 'workTitle': 'Jeremiah', 'locatorRaw': 'Jeremiah, 15:10 (D) Jeremias, 15:10', 'locators': ['15:10 (D) Jeremias, 15:10']},
                {'workSegmentIndex': 8, 'workId': 'work:bible-ezekiel', 'workTitle': 'Ezekiel', 'locatorRaw': 'Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12', 'locators': ['18:4-21 esp 18:8, 18:13, 18:17, 22:12']}
            ]
            c['totalWorkSegments'] = 8

with open('00-sistema/staging/referencias-candidatas.json', 'w', encoding='utf-8') as f:
    json.dump(cands, f, indent=2, ensure_ascii=False)

# 2. Update cobertura.json
with open('00-sistema/staging/cobertura.json', 'r', encoding='utf-8') as f:
    cob = json.load(f)

cob['baseline'] = 'STAGING_BASELINE_JUSTICE_1952_V9'
cob['totalWorkSegments'] = 1351
cob['referenciasVerificadas'] = 441
cob['workSegmentsVerificados'] = 706
cob['referenciasPendentes'] = 814 - 441
cob['workSegmentsPendentes'] = 1351 - 706

cob['porTopico']['42.8d']['workSegmentsDetectados'] = 29
cob['porTopico']['42.8d']['refsVerificadasNoVault'] = 18
cob['porTopico']['42.8d']['workSegmentsVerificadosNoVault'] = 29
cob['porTopico']['42.8d']['statusReconciliacao'] = 'verified'
cob['timestamp'] = datetime.now(timezone.utc).isoformat()

with open('00-sistema/staging/cobertura.json', 'w', encoding='utf-8') as f:
    json.dump(cob, f, indent=2, ensure_ascii=False)

print('Updated staging artifacts for Baseline V9 successfully!')
