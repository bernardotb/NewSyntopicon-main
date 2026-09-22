import json

with open('00-sistema/manifesto-justica.json', 'r', encoding='utf-8') as f:
    man = json.load(f)

man['versao'] = '2.18.0'
man['dataAtualizacao'] = '2026-09-22'
man['stagingBaseline'] = 'STAGING_BASELINE_JUSTICE_1952_V9'
man['previousBaseline'] = 'STAGING_BASELINE_JUSTICE_1952_V8'

for bh in man.get('baselineHistory', []):
    if bh.get('baseline') == 'STAGING_BASELINE_JUSTICE_1952_V8':
        bh['status'] = 'HISTORICAL_VALID (superseded_by_v9)'

man['baselineHistory'].append({
    'baseline': 'STAGING_BASELINE_JUSTICE_1952_V9',
    'physicalReferenceCount': 814,
    'workSegmentCount': 1351,
    'referenceDelta': 0,
    'workSegmentDelta': 1,
    'status': 'ACTIVE_CURRENT_STATE',
    'description': 'Baseline V9 gerado após auditoria física e visual de 42.8d (pp. 868-869). Confirmadas 18 referências físicas impressas (referenceDelta=0). Desmembrada a fusão de Provérbios e Jeremias na entrada física #01 do Antigo Testamento, elevando o censo de workSegments em +1 (1.350 -> 1.351).'
})

man['resumoMetricas']['referencias'] = 441
man['resumoMetricas']['referenciasAuditadas'] = 441
man['resumoMetricas']['totalReferenciasVerificadas'] = 441
man['resumoMetricas']['totalWorkSegmentsVerificados'] = 706
man['resumoMetricas']['totalReferenciasCandidatas'] = 373
man['resumoMetricas']['totalObras'] = 187
man['resumoMetricas']['totalEntidadesMaterializadas'] = 767
man['resumoMetricas']['baselineAtivo'] = 'STAGING_BASELINE_JUSTICE_1952_V9'

man['topico42_8dReconciliacao'] = {
    'topicoId': 'topic:justica:8d',
    'topicCode': '42.8d',
    'nomeEn': 'Justice and the use of money: usury and interest rates',
    'nomePtBr': 'A justiça e o uso do dinheiro: usura e taxas de juros',
    'syntopiconPages': [868, 869],
    'status': 'fully_verified',
    'referenciasFisicas': 18,
    'workSegments': 29,
    'autores': 17,
    'obras': 28,
    'gbwwVolumes': 17,
    'fontesNaoNumeradas': 1,
    'passagens': 0,
    'anomaliasResolvidas': [
        'Desmembramento de Provérbios e Jeremias na entrada 01 do Antigo Testamento, recuperando +1 workSegment (7 -> 8) obscurecido por OCR 28:87 Jeremiah',
        'Correção do volume de Tácito de 6 (erro de leitura de OCR) para o volume canônico GBWW 15',
        'Retificação filológica do localizador de Tomás de Aquino de PART MI para PART I-II',
        'Correção da quebra de linha de Pascal de 55a*57a para 55a-57a',
        'Restauração do título Capital na posição inicial do localizador de Karl Marx'
    ]
}

with open('00-sistema/manifesto-justica.json', 'w', encoding='utf-8') as f:
    json.dump(man, f, indent=2, ensure_ascii=False)

print('Updated manifesto-justica.json for Baseline V9 successfully!')
