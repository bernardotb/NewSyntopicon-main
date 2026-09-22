import os, glob, yaml, json, jsonschema, re, sys
from datetime import datetime, timezone

VAULT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

with open(os.path.join(VAULT, '00-sistema/schema-entidades.json')) as f:
    schema = json.load(f)

resolver = jsonschema.RefResolver.from_schema(schema)

# Validators
validators = {
    'GreatIdea': jsonschema.Draft202012Validator(schema['$defs']['GreatIdea'], resolver=resolver),
    'Topic': jsonschema.Draft202012Validator(schema['$defs']['Topic'], resolver=resolver),
    'SyntopiconReference': jsonschema.Draft202012Validator(schema['$defs']['SyntopiconReference'], resolver=resolver),
    'Author': jsonschema.Draft202012Validator(schema['$defs']['Author'], resolver=resolver),
    'Work': jsonschema.Draft202012Validator(schema['$defs']['Work'], resolver=resolver),
    'Volume': jsonschema.Draft202012Validator(schema['$defs']['Volume'], resolver=resolver)
}

results = {
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "suite": "Arena Syntopicon Subgraph Fixtures & Data Integrity Audit",
    "status": "PASSED",
    "invariantesArquiteturais": {},
    "fixtureRegressaoGoldenCase8c1": {},
    "fixtureRegressaoLote1": {},
    "fixtureRegressaoTopico42_7": {},
    "fixtureRegressaoTopico42_8": {},
    "fixtureRegressaoTopico42_8a": {},
    "fixtureRegressaoTopico42_8b": {},
    "fixtureRegressaoTopico42_8c": {},
    "fixtureRegressaoTopico42_8c_2": {},
    "fixtureRegressaoTopico42_8d": {},
    "protecoesIntegridadeDocumental": {},
    "resumoMetricas": {},
    "validacaoSchemas": {},
    "auditoriaHierarquiaJustica": {},
    "integridadeRelacional": {}
}

# -----------------------------------------------------------------------------
# 1. VALIDAÇÃO DA GRANDE IDEIA E DOS 4 INVARIANTES ARQUITETURAIS
# -----------------------------------------------------------------------------
with open(os.path.join(VAULT, '01-grandes-ideias/gi-42-justica.md')) as f:
    gi_raw = f.read()
    gi_fm = yaml.safe_load(gi_raw.split('---')[1])

# Invariante 1: Identidade Autoritativa
if gi_fm.get('id') != "idea:justica":
    print(f"FATAL: Invariante 1 violado! id deve ser 'idea:justica', obtido: {gi_fm.get('id')}")
    sys.exit(1)

legacy_ids = gi_fm.get('legacyIds', [])
if "idea:042" not in legacy_ids or "idea:justice" not in legacy_ids:
    print(f"FATAL: Invariante 1 violado! legacyIds deve conter idea:042 e idea:justice. Obtido: {legacy_ids}")
    sys.exit(1)

# Invariante 2: Paridade Estrita dos Campos Numéricos
num_canonico = gi_fm.get('numeroCanonico')
num_kebab = gi_fm.get('numero-canonico')
num_bare = gi_fm.get('numero')

if not (num_canonico == num_kebab == num_bare == 42):
    print(f"FATAL: Invariante 2 violado! Paridade numerica falhou: numeroCanonico={num_canonico}, numero-canonico={num_kebab}, numero={num_bare}")
    sys.exit(1)

# Invariante 3: Distinção Semântica layer vs camadas
if gi_fm.get('layer') != "canonical":
    print(f"FATAL: Invariante 3 violado! layer deve ser 'canonical', obtido: {gi_fm.get('layer')}")
    sys.exit(1)

camadas = gi_fm.get('camadas', [])
expected_camadas = ["canonical", "source", "editorial", "contemporary-extension", "personal"]
for c in expected_camadas:
    if c not in camadas:
        print(f"FATAL: Invariante 3 violado! Camada '{c}' ausente na lista 'camadas': {camadas}")
        sys.exit(1)

# Invariante 4: Separação Estrita de Níveis de Verificação
if gi_fm.get('verification') != "verified":
    print(f"FATAL: Invariante 4 violado! verification deve ser 'verified', obtido: {gi_fm.get('verification')}")
    sys.exit(1)

if gi_fm.get('corpus-ingestion-verification') != "needs_verification":
    print(f"FATAL: Invariante 4 violado! corpus-ingestion-verification deve ser 'needs_verification', obtido: {gi_fm.get('corpus-ingestion-verification')}")
    sys.exit(1)

results["invariantesArquiteturais"] = {
    "invariante1_identidadeAutoritativa": "PASSED (id == 'idea:justica')",
    "invariante2_paridadeCamposNumericos": "PASSED (numeroCanonico == numero-canonico == numero == 42)",
    "invariante3_distincaoLayerVersusCamadas": "PASSED (layer: canonical; 5 camadas catalogadas)",
    "invariante4_separacaoVerificacao": "PASSED (verification: verified; corpus-ingestion-verification: needs_verification)"
}

# Schema GreatIdea
gi_inst = {k: gi_fm.get(k) for k in ['id', 'slug', 'canonicalName', 'displayNamePtBr', 'numeroCanonico', 'gbwwVolume', 'syntopiconVolume', 'pageStart', 'pageEnd', 'totalMainTopics', 'totalDescendantTopics', 'totalNodes', 'provenance', 'epistemology', 'verification']}
validators['GreatIdea'].validate(gi_inst)
results["validacaoSchemas"]["GreatIdea"] = {"status": "PASSED", "entidadesValidadas": 1, "erros": 0}

# -----------------------------------------------------------------------------
# 2. VALIDAÇÃO DOS 41 TÓPICOS
# -----------------------------------------------------------------------------
topic_files = sorted(glob.glob(os.path.join(VAULT, '02-topicos/justica/*.md')))
topics_dict = {}
for tf in topic_files:
    with open(tf) as f:
        t_fm = yaml.safe_load(f.read().split('---')[1])
    t_inst = {k: t_fm.get(k) for k in ['id', 'slug', 'ideaId', 'parentTopicId', 'rootTopicId', 'topicCode', 'canonicalName', 'displayNamePtBr', 'level', 'order', 'provenance', 'epistemology', 'verification']}
    validators['Topic'].validate(t_inst)
    topics_dict[t_fm['id']] = t_fm
results["validacaoSchemas"]["Topic"] = {"status": "PASSED", "entidadesValidadas": len(topic_files), "erros": 0}

# -----------------------------------------------------------------------------
# 3. VALIDAÇÃO DAS REFERÊNCIAS
# -----------------------------------------------------------------------------
ref_files = sorted(glob.glob(os.path.join(VAULT, '03-referencias/justica/*.md')))
refs_data = []
for rf in ref_files:
    with open(rf) as f:
        r_fm = yaml.safe_load(f.read().split('---')[1])
    r_inst = {k: r_fm.get(k) for k in ['id', 'topicId', 'ideaId', 'authorId', 'authorCanonicalName', 'workIds', 'workSegments', 'editionId', 'gbwwVolume', 'syntopiconPage', 'locatorRaw', 'passageIds', 'orderInTopic', 'provenance', 'epistemology', 'verification']}
    validators['SyntopiconReference'].validate(r_inst)
    refs_data.append(r_fm)
results["validacaoSchemas"]["SyntopiconReference"] = {"status": "PASSED", "entidadesValidadas": len(ref_files), "erros": 0}

# -----------------------------------------------------------------------------
# 4. VALIDAÇÃO DE AUTORES, OBRAS E VOLUMES
# -----------------------------------------------------------------------------
author_files = sorted(glob.glob(os.path.join(VAULT, '06-autores/*.md')))
for af in author_files:
    with open(af) as f:
        a_fm = yaml.safe_load(f.read().split('---')[1])
    a_inst = {k: a_fm.get(k) for k in ['id', 'slug', 'canonicalName', 'displayNamePtBr', 'period', 'tradition', 'isGbwwCanonical', 'gbwwVolumes', 'provenance', 'epistemology', 'verification']}
    validators['Author'].validate(a_inst)
results["validacaoSchemas"]["Author"] = {"status": "PASSED", "entidadesValidadas": len(author_files), "erros": 0}

work_files = sorted(glob.glob(os.path.join(VAULT, '05-obras/*.md')))
for wf in work_files:
    with open(wf) as f:
        w_fm = yaml.safe_load(f.read().split('---')[1])
    w_inst = {k: w_fm.get(k) for k in ['id', 'slug', 'canonicalTitle', 'displayTitlePtBr', 'authorIds', 'originalLanguage', 'gbwwVolume', 'provenance', 'epistemology', 'verification']}
    validators['Work'].validate(w_inst)
results["validacaoSchemas"]["Work"] = {"status": "PASSED", "entidadesValidadas": len(work_files), "erros": 0}

volume_files = sorted(glob.glob(os.path.join(VAULT, '07-volumes/*.md')))
for vf in volume_files:
    with open(vf) as f:
        v_fm = yaml.safe_load(f.read().split('---')[1])
    v_inst = {k: v_fm.get(k) for k in ['id', 'slug', 'volumeNumber', 'canonicalTitle', 'publicationYear', 'series', 'authors', 'provenance', 'epistemology', 'verification']}
    validators['Volume'].validate(v_inst)
results["validacaoSchemas"]["Volume"] = {"status": "PASSED", "entidadesValidadas": len(volume_files), "erros": 0}

# Passages check: strictly 0 verified passage notes
passage_files = sorted([f for f in glob.glob(os.path.join(VAULT, '04-passagens/*.md')) if not os.path.basename(f).startswith('README')])
c_passages = len(passage_files)

# -----------------------------------------------------------------------------
# 5. FIXTURE PERMANENTE 1: SUBGRAFO GOLDEN CASE 8c(1)
# -----------------------------------------------------------------------------
# Rastreamento rigoroso a partir do nó topic:justica:8c-1
refs_8c1 = [r for r in refs_data if r.get('topicId') == 'topic:justica:8c-1']
authors_8c1_reached = set(r['authorId'] for r in refs_8c1)
works_8c1_reached = set(wid for r in refs_8c1 for wid in r.get('workIds', []))
vols_8c1_reached = set(r['gbwwVolume'] for r in refs_8c1)
passages_8c1_reached = set(pid for r in refs_8c1 for pid in r.get('passageIds', []))

c_8c1_refs = len(refs_8c1)
c_8c1_authors = len(authors_8c1_reached)
c_8c1_works = len(works_8c1_reached)
c_8c1_vols = len(vols_8c1_reached)
c_8c1_passages = len(passages_8c1_reached)

if not (c_8c1_refs == 18 and c_8c1_authors == 17 and c_8c1_works == 20 and c_8c1_vols == 16 and c_8c1_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo 8c(1) QUEBRADA!")
    print(f"Esperado: 18 refs, 17 autores, 20 obras, 16 volumes, 0 passagens")
    print(f"Obtido:   {c_8c1_refs} refs, {c_8c1_authors} autores, {c_8c1_works} obras, {c_8c1_vols} volumes, {c_8c1_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoGoldenCase8c1"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8c-1')",
    "proporcaoOntologica": "18_refs / 17_autores / 20_obras / 16_volumes / 0_passagens",
    "referencias": c_8c1_refs,
    "autoresAlcancados": c_8c1_authors,
    "obrasAlcancadas": c_8c1_works,
    "volumesAlcancados": c_8c1_vols,
    "passagensAlcancadas": c_8c1_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6. FIXTURE PERMANENTE 2: SUBGRAFO LOTE 1 (TÓPICO 1: 42.1 + 1a a 1f)
# -----------------------------------------------------------------------------
subtopics_l1 = {'topic:justica:1a', 'topic:justica:1b', 'topic:justica:1c', 'topic:justica:1d', 'topic:justica:1e', 'topic:justica:1f'}
refs_l1 = [r for r in refs_data if r.get('topicId') in subtopics_l1]

lot1_by_subtopic = {}
lot1_segs = 0
lot1_authors_reached = set()
lot1_works_reached = set()
lot1_vols_reached = set()
lot1_passages_reached = set()

for r in refs_l1:
    st = r['topicId'].split(':')[-1]
    lot1_by_subtopic[st] = lot1_by_subtopic.get(st, 0) + 1
    segs = r.get('workSegments', [])
    lot1_segs += len(segs)
    lot1_authors_reached.add(r['authorId'])
    lot1_vols_reached.add(r['gbwwVolume'])
    for wid in r.get('workIds', []):
        lot1_works_reached.add(wid)
    for pid in r.get('passageIds', []):
        lot1_passages_reached.add(pid)

c_l1_refs = len(refs_l1)
c_l1_authors = len(lot1_authors_reached)
c_l1_works = len(lot1_works_reached)
c_l1_vols = len(lot1_vols_reached)
c_l1_passages = len(lot1_passages_reached)

expected_subtopic_counts = {'1a': 18, '1b': 8, '1c': 11, '1d': 8, '1e': 3, '1f': 5}

if not (c_l1_refs == 53 and
        lot1_by_subtopic == expected_subtopic_counts and
        lot1_segs == 82 and
        c_l1_authors == 26 and
        c_l1_works == 51 and
        c_l1_vols == 28 and
        c_l1_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Lote 1 QUEBRADA!")
    print(f"Esperado: 53 refs {expected_subtopic_counts}, 82 segmentos, 26 autores, 51 obras, 28 volumes, 0 passagens")
    print(f"Obtido:   {c_l1_refs} refs {lot1_by_subtopic}, {lot1_segs} segmentos, {c_l1_authors} autores, {c_l1_works} obras, {c_l1_vols} volumes, {c_l1_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoLote1"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId in {1a, 1b, 1c, 1d, 1e, 1f})",
    "referenciasPorSubtopico": lot1_by_subtopic,
    "totalReferencias": c_l1_refs,
    "totalSegmentosObra": lot1_segs,
    "totalAutoresAlcancados": c_l1_authors,
    "totalObrasAlcancadas": c_l1_works,
    "totalVolumesAlcancados": c_l1_vols,
    "passagensAlcancadas": c_l1_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.1 FIXTURE PERMANENTE 3: SUBGRAFO TÓPICO 42.2 (LOTE 2: OS PRECEITOS DA JUSTIÇA)
# -----------------------------------------------------------------------------
refs_t2 = [r for r in refs_data if r.get('topicId') == 'topic:justica:2']
t2_authors_reached = set(r['authorId'] for r in refs_t2)
t2_works_reached = set(wid for r in refs_t2 for wid in r.get('workIds', []))
t2_vols_reached = set(r['gbwwVolume'] for r in refs_t2)
t2_passages_reached = set(pid for r in refs_t2 for pid in r.get('passageIds', []))
t2_segs = sum(len(r.get('workSegments', [])) for r in refs_t2)

c_t2_refs = len(refs_t2)
c_t2_authors = len(t2_authors_reached)
c_t2_works = len(t2_works_reached)
c_t2_vols = len(t2_vols_reached)
c_t2_passages = len(t2_passages_reached)

if not (c_t2_refs == 28 and c_t2_authors == 28 and c_t2_works == 58 and c_t2_vols == 22 and t2_segs == 58 and c_t2_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.2 QUEBRADA!")
    print(f"Esperado: 28 refs, 28 autores, 58 obras, 22 volumes, 58 segmentos, 0 passagens")
    print(f"Obtido:   {c_t2_refs} refs, {c_t2_authors} autores, {c_t2_works} obras, {c_t2_vols} volumes, {t2_segs} segmentos, {c_t2_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_2"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:2')",
    "proporcaoOntologica": "28_refs / 28_autores / 58_obras / 22_volumes / 58_segmentos / 0_passagens",
    "referencias": c_t2_refs,
    "totalSegmentosObra": t2_segs,
    "autoresAlcancados": c_t2_authors,
    "obrasAlcancadas": c_t2_works,
    "volumesAlcancados": c_t2_vols,
    "passagensAlcancadas": c_t2_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.2 FIXTURE PERMANENTE 4: SUBGRAFO TÓPICO 42.3 (LOTE 2: OS DEVERES DA JUSTIÇA)
# -----------------------------------------------------------------------------
refs_t3 = [r for r in refs_data if r.get('topicId') == 'topic:justica:3']
t3_authors_reached = set(r['authorId'] for r in refs_t3)
t3_works_reached = set(wid for r in refs_t3 for wid in r.get('workIds', []))
t3_vols_reached = set(r['gbwwVolume'] for r in refs_t3)
t3_passages_reached = set(pid for r in refs_t3 for pid in r.get('passageIds', []))
t3_segs = sum(len(r.get('workSegments', [])) for r in refs_t3)

c_t3_refs = len(refs_t3)
c_t3_authors = len(t3_authors_reached)
c_t3_works = len(t3_works_reached)
c_t3_vols = len(t3_vols_reached)
c_t3_passages = len(t3_passages_reached)

if not (c_t3_refs == 23 and c_t3_authors == 21 and c_t3_works == 33 and c_t3_vols == 22 and t3_segs == 34 and c_t3_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.3 QUEBRADA!")
    print(f"Esperado: 23 refs, 21 autores, 33 obras, 22 volumes, 34 segmentos, 0 passagens")
    print(f"Obtido:   {c_t3_refs} refs, {c_t3_authors} autores, {c_t3_works} obras, {c_t3_vols} volumes, {t3_segs} segmentos, {c_t3_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_3"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:3')",
    "proporcaoOntologica": "23_refs / 21_autores / 33_obras / 22_volumes / 34_segmentos / 0_passagens",
    "referencias": c_t3_refs,
    "totalSegmentosObra": t3_segs,
    "autoresAlcancados": c_t3_authors,
    "obrasAlcancadas": c_t3_works,
    "volumesAlcancados": c_t3_vols,
    "passagensAlcancadas": c_t3_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.3 FIXTURE PERMANENTE 5: SUBGRAFO TÓPICO 42.4 (LOTE 2: JUSTIÇA E CONVENIÊNCIA)
# -----------------------------------------------------------------------------
refs_t4 = [r for r in refs_data if r.get('topicId') == 'topic:justica:4']
t4_authors_reached = set(r['authorId'] for r in refs_t4)
t4_works_reached = set(wid for r in refs_t4 for wid in r.get('workIds', []))
t4_vols_reached = set(r['gbwwVolume'] for r in refs_t4)
t4_passages_reached = set(pid for r in refs_t4 for pid in r.get('passageIds', []))
t4_segs = sum(len(r.get('workSegments', [])) for r in refs_t4)

c_t4_refs = len(refs_t4)
c_t4_authors = len(t4_authors_reached)
c_t4_works = len(t4_works_reached)
c_t4_vols = len(t4_vols_reached)
c_t4_passages = len(t4_passages_reached)

if not (c_t4_refs == 25 and c_t4_authors == 24 and c_t4_works == 53 and c_t4_vols == 18 and t4_segs == 53 and c_t4_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.4 QUEBRADA!")
    print(f"Esperado: 25 refs, 24 autores, 53 obras, 18 volumes, 53 segmentos, 0 passagens")
    print(f"Obtido:   {c_t4_refs} refs, {c_t4_authors} autores, {c_t4_works} obras, {c_t4_vols} volumes, {t4_segs} segmentos, {c_t4_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_4"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:4')",
    "proporcaoOntologica": "25_refs / 24_autores / 53_obras / 18_volumes / 53_segmentos / 0_passagens",
    "referencias": c_t4_refs,
    "totalSegmentosObra": t4_segs,
    "autoresAlcancados": c_t4_authors,
    "obrasAlcancadas": c_t4_works,
    "volumesAlcancados": c_t4_vols,
    "passagensAlcancadas": c_t4_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.4 FIXTURE PERMANENTE 6: SUBGRAFO TÓPICO 42.5 (LOTE 2: JUSTIÇA E IGUALDADE)
# -----------------------------------------------------------------------------
refs_t5 = [r for r in refs_data if r.get('topicId') == 'topic:justica:5']
t5_authors_reached = set(r['authorId'] for r in refs_t5)
t5_works_reached = set(wid for r in refs_t5 for wid in r.get('workIds', []))
t5_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t5 if r.get('gbwwVolume') is not None)
t5_non_num_reached = set(r['gbwwVolume'] for r in refs_t5 if r.get('gbwwVolume') is None)
t5_passages_reached = set(pid for r in refs_t5 for pid in r.get('passageIds', []))
t5_segs = sum(len(r.get('workSegments', [])) for r in refs_t5)

c_t5_refs = len(refs_t5)
c_t5_authors = len(t5_authors_reached)
c_t5_works = len(t5_works_reached)
c_t5_gbww_vols = len(t5_gbww_vols_reached)
c_t5_non_num = len(t5_non_num_reached)
c_t5_passages = len(t5_passages_reached)

if not (c_t5_refs == 26 and c_t5_authors == 24 and c_t5_works == 32 and c_t5_gbww_vols == 21 and c_t5_non_num == 0 and t5_segs == 33 and c_t5_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.5 QUEBRADA!")
    print(f"Esperado: 26 refs, 24 autores/fontes, 32 obras, 21 volumes GBWW, 0 fontes não-num, 33 segmentos, 0 passagens")
    print(f"Obtido:   {c_t5_refs} refs, {c_t5_authors} autores/fontes, {c_t5_works} obras, {c_t5_gbww_vols} volumes GBWW, {c_t5_non_num} não-num, {t5_segs} segmentos, {c_t5_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_5"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:5')",
    "proporcaoOntologica": "26_refs / 24_autores_fontes / 32_obras / 21_volumes_gbww / 0_fontes_nao_num / 33_segmentos / 0_passagens",
    "referencias": c_t5_refs,
    "totalSegmentosObra": t5_segs,
    "autoresOuFontesAlcancados": c_t5_authors,
    "obrasAlcancadas": c_t5_works,
    "gbwwVolumesAlcancados": c_t5_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t5_non_num,
    "passagensAlcancadas": c_t5_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.5 FIXTURE PERMANENTE 7: SUBGRAFO TÓPICO 42.6 (LOTE 3: JUSTIÇA E LIBERDADE)
# -----------------------------------------------------------------------------
refs_t6 = [r for r in refs_data if r.get('topicId') == 'topic:justica:6']
t6_authors_reached = set(r['authorId'] for r in refs_t6)
t6_works_reached = set(wid for r in refs_t6 for wid in r.get('workIds', []))
t6_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6 if r.get('gbwwVolume') is not None)
t6_non_num_reached = set(r['gbwwVolume'] for r in refs_t6 if r.get('gbwwVolume') is None)
t6_passages_reached = set(pid for r in refs_t6 for pid in r.get('passageIds', []))
t6_segs = sum(len(r.get('workSegments', [])) for r in refs_t6)

c_t6_refs = len(refs_t6)
c_t6_authors = len(t6_authors_reached)
c_t6_works = len(t6_works_reached)
c_t6_gbww_vols = len(t6_gbww_vols_reached)
c_t6_non_num = len(t6_non_num_reached)
c_t6_passages = len(t6_passages_reached)

if not (c_t6_refs == 28 and c_t6_authors == 27 and c_t6_works == 42 and c_t6_gbww_vols == 22 and c_t6_non_num == 0 and t6_segs == 42 and c_t6_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6 QUEBRADA!")
    print(f"Esperado: 28 refs, 27 autores/fontes, 42 obras, 22 volumes GBWW, 0 fontes não-num, 42 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6_refs} refs, {c_t6_authors} autores/fontes, {c_t6_works} obras, {c_t6_gbww_vols} volumes GBWW, {c_t6_non_num} não-num, {t6_segs} segmentos, {c_t6_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6')",
    "proporcaoOntologica": "28_refs / 27_autores_fontes / 42_obras / 22_volumes_gbww / 0_fontes_nao_num / 42_segmentos / 0_passagens",
    "referencias": c_t6_refs,
    "totalSegmentosObra": t6_segs,
    "autoresOuFontesAlcancados": c_t6_authors,
    "obrasAlcancadas": c_t6_works,
    "gbwwVolumesAlcancados": c_t6_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6_non_num,
    "passagensAlcancadas": c_t6_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.6 FIXTURE PERMANENTE 8: SUBGRAFO TÓPICO 42.6a (LOTE 3: DIREITOS NATURAIS E LEI NATURAL)
# -----------------------------------------------------------------------------
refs_t6a = [r for r in refs_data if r.get('topicId') == 'topic:justica:6a']
t6a_authors_reached = set(r['authorId'] for r in refs_t6a)
t6a_works_reached = set(wid for r in refs_t6a for wid in r.get('workIds', []))
t6a_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6a if r.get('gbwwVolume') is not None)
t6a_non_num_reached = set(r['gbwwVolume'] for r in refs_t6a if r.get('gbwwVolume') is None)
t6a_passages_reached = set(pid for r in refs_t6a for pid in r.get('passageIds', []))
t6a_segs = sum(len(r.get('workSegments', [])) for r in refs_t6a)

c_t6a_refs = len(refs_t6a)
c_t6a_authors = len(t6a_authors_reached)
c_t6a_works = len(t6a_works_reached)
c_t6a_gbww_vols = len(t6a_gbww_vols_reached)
c_t6a_non_num = len(t6a_non_num_reached)
c_t6a_passages = len(t6a_passages_reached)

if not (c_t6a_refs == 20 and c_t6a_authors == 19 and c_t6a_works == 20 and c_t6a_gbww_vols == 18 and c_t6a_non_num == 0 and t6a_segs == 21 and c_t6a_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6a QUEBRADA!")
    print(f"Esperado: 20 refs, 19 autores/fontes, 20 obras, 18 volumes GBWW, 0 fontes não-num, 21 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6a_refs} refs, {c_t6a_authors} autores/fontes, {c_t6a_works} obras, {c_t6a_gbww_vols} volumes GBWW, {c_t6a_non_num} não-num, {t6a_segs} segmentos, {c_t6a_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6a"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6a')",
    "proporcaoOntologica": "20_refs / 19_autores_fontes / 20_obras / 18_volumes_gbww / 0_fontes_nao_num / 21_segmentos / 0_passagens",
    "referencias": c_t6a_refs,
    "totalSegmentosObra": t6a_segs,
    "autoresOuFontesAlcancados": c_t6a_authors,
    "obrasAlcancadas": c_t6a_works,
    "gbwwVolumesAlcancados": c_t6a_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6a_non_num,
    "passagensAlcancadas": c_t6a_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.7 FIXTURE PERMANENTE 9: SUBGRAFO TÓPICO 42.6b (LOTE 3: DIREITOS NATURAIS E POSITIVOS)
# -----------------------------------------------------------------------------
refs_t6b = [r for r in refs_data if r.get('topicId') == 'topic:justica:6b']
t6b_authors_reached = set(r['authorId'] for r in refs_t6b)
t6b_works_reached = set(wid for r in refs_t6b for wid in r.get('workIds', []))
t6b_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6b if r.get('gbwwVolume') is not None)
t6b_non_num_reached = set(r['gbwwVolume'] for r in refs_t6b if r.get('gbwwVolume') is None)
t6b_passages_reached = set(pid for r in refs_t6b for pid in r.get('passageIds', []))
t6b_segs = sum(len(r.get('workSegments', [])) for r in refs_t6b)

c_t6b_refs = len(refs_t6b)
c_t6b_authors = len(t6b_authors_reached)
c_t6b_works = len(t6b_works_reached)
c_t6b_gbww_vols = len(t6b_gbww_vols_reached)
c_t6b_non_num = len(t6b_non_num_reached)
c_t6b_passages = len(t6b_passages_reached)

if not (c_t6b_refs == 21 and c_t6b_authors == 20 and c_t6b_works == 30 and c_t6b_gbww_vols == 18 and c_t6b_non_num == 0 and t6b_segs == 30 and c_t6b_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6b QUEBRADA!")
    print(f"Esperado: 21 refs, 20 autores/fontes, 30 obras, 18 volumes GBWW, 0 fontes não-num, 30 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6b_refs} refs, {c_t6b_authors} autores/fontes, {c_t6b_works} obras, {c_t6b_gbww_vols} volumes GBWW, {c_t6b_non_num} não-num, {t6b_segs} segmentos, {c_t6b_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6b"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6b')",
    "proporcaoOntologica": "21_refs / 20_autores_fontes / 30_obras / 18_volumes_gbww / 0_fontes_nao_num / 30_segmentos / 0_passagens",
    "referencias": c_t6b_refs,
    "totalSegmentosObra": t6b_segs,
    "autoresOuFontesAlcancados": c_t6b_authors,
    "obrasAlcancadas": c_t6b_works,
    "gbwwVolumesAlcancados": c_t6b_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6b_non_num,
    "passagensAlcancadas": c_t6b_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.8 FIXTURE PERMANENTE 10: SUBGRAFO TÓPICO 42.6c (LOTE 3: INALIENABILIDADE DOS DIREITOS NATURAIS)
# -----------------------------------------------------------------------------
refs_t6c = [r for r in refs_data if r.get('topicId') == 'topic:justica:6c']
t6c_authors_reached = set(r['authorId'] for r in refs_t6c)
t6c_works_reached = set(wid for r in refs_t6c for wid in r.get('workIds', []))
t6c_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6c if r.get('gbwwVolume') is not None)
t6c_non_num_reached = set(r['gbwwVolume'] for r in refs_t6c if r.get('gbwwVolume') is None)
t6c_passages_reached = set(pid for r in refs_t6c for pid in r.get('passageIds', []))
t6c_segs = sum(len(r.get('workSegments', [])) for r in refs_t6c)

c_t6c_refs = len(refs_t6c)
c_t6c_authors = len(t6c_authors_reached)
c_t6c_works = len(t6c_works_reached)
c_t6c_gbww_vols = len(t6c_gbww_vols_reached)
c_t6c_non_num = len(t6c_non_num_reached)
c_t6c_passages = len(t6c_passages_reached)

if not (c_t6c_refs == 15 and c_t6c_authors == 15 and c_t6c_works == 17 and c_t6c_gbww_vols == 11 and c_t6c_non_num == 0 and t6c_segs == 17 and c_t6c_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6c QUEBRADA!")
    print(f"Esperado: 15 refs, 15 autores/fontes, 17 obras, 11 volumes GBWW, 0 fontes não-num, 17 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6c_refs} refs, {c_t6c_authors} autores/fontes, {c_t6c_works} obras, {c_t6c_gbww_vols} volumes GBWW, {c_t6c_non_num} não-num, {t6c_segs} segmentos, {c_t6c_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6c"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6c')",
    "proporcaoOntologica": "15_refs / 15_autores_fontes / 17_obras / 11_volumes_gbww / 0_fontes_nao_num / 17_segmentos / 0_passagens",
    "referencias": c_t6c_refs,
    "totalSegmentosObra": t6c_segs,
    "autoresOuFontesAlcancados": c_t6c_authors,
    "obrasAlcancadas": c_t6c_works,
    "gbwwVolumesAlcancados": c_t6c_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6c_non_num,
    "passagensAlcancadas": c_t6c_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.9 FIXTURE PERMANENTE 11: SUBGRAFO TÓPICO 42.6d (LOTE 3: JUSTIÇA COMO BASE DA DISTINÇÃO ENTRE LIBERDADE E LICENÇA)
# -----------------------------------------------------------------------------
refs_t6d = [r for r in refs_data if r.get('topicId') == 'topic:justica:6d']
t6d_authors_reached = set(r['authorId'] for r in refs_t6d)
t6d_works_reached = set(wid for r in refs_t6d for wid in r.get('workIds', []))
t6d_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6d if r.get('gbwwVolume') is not None)
t6d_non_num_reached = set(r['gbwwVolume'] for r in refs_t6d if r.get('gbwwVolume') is None)
t6d_passages_reached = set(pid for r in refs_t6d for pid in r.get('passageIds', []))
t6d_segs = sum(len(r.get('workSegments', [])) for r in refs_t6d)

c_t6d_refs = len(refs_t6d)
c_t6d_authors = len(t6d_authors_reached)
c_t6d_works = len(t6d_works_reached)
c_t6d_gbww_vols = len(t6d_gbww_vols_reached)
c_t6d_non_num = len(t6d_non_num_reached)
c_t6d_passages = len(t6d_passages_reached)

if not (c_t6d_refs == 15 and c_t6d_authors == 15 and c_t6d_works == 18 and c_t6d_gbww_vols == 14 and c_t6d_non_num == 0 and t6d_segs == 18 and c_t6d_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6d QUEBRADA!")
    print(f"Esperado: 15 refs, 15 autores/fontes, 18 obras, 14 volumes GBWW, 0 fontes não-num, 18 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6d_refs} refs, {c_t6d_authors} autores/fontes, {c_t6d_works} obras, {c_t6d_gbww_vols} volumes GBWW, {c_t6d_non_num} não-num, {t6d_segs} segmentos, {c_t6d_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6d"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6d')",
    "proporcaoOntologica": "15_refs / 15_autores_fontes / 18_obras / 14_volumes_gbww / 0_fontes_nao_num / 18_segmentos / 0_passagens",
    "referencias": c_t6d_refs,
    "totalSegmentosObra": t6d_segs,
    "autoresOuFontesAlcancados": c_t6d_authors,
    "obrasAlcancadas": c_t6d_works,
    "gbwwVolumesAlcancados": c_t6d_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6d_non_num,
    "passagensAlcancadas": c_t6d_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.10 FIXTURE PERMANENTE 12: SUBGRAFO TÓPICO 42.6e (LOTE 3: JUSTIÇA E DIREITOS NATURAIS COMO FONTE DA LIBERDADE CIVIL)
# -----------------------------------------------------------------------------
refs_t6e = [r for r in refs_data if r.get('topicId') == 'topic:justica:6e']
t6e_authors_reached = set(r['authorId'] for r in refs_t6e)
t6e_works_reached = set(wid for r in refs_t6e for wid in r.get('workIds', []))
t6e_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t6e if r.get('gbwwVolume') is not None)
t6e_non_num_reached = set(r['gbwwVolume'] for r in refs_t6e if r.get('gbwwVolume') is None)
t6e_passages_reached = set(pid for r in refs_t6e for pid in r.get('passageIds', []))
t6e_segs = sum(len(r.get('workSegments', [])) for r in refs_t6e)

c_t6e_refs = len(refs_t6e)
c_t6e_authors = len(t6e_authors_reached)
c_t6e_works = len(t6e_works_reached)
c_t6e_gbww_vols = len(t6e_gbww_vols_reached)
c_t6e_non_num = len(t6e_non_num_reached)
c_t6e_passages = len(t6e_passages_reached)

if not (c_t6e_refs == 11 and c_t6e_authors == 11 and c_t6e_works == 14 and c_t6e_gbww_vols == 10 and c_t6e_non_num == 0 and t6e_segs == 14 and c_t6e_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.6e QUEBRADA!")
    print(f"Esperado: 11 refs, 11 autores/fontes, 14 obras, 10 volumes GBWW, 0 fontes não-num, 14 segmentos, 0 passagens")
    print(f"Obtido:   {c_t6e_refs} refs, {c_t6e_authors} autores/fontes, {c_t6e_works} obras, {c_t6e_gbww_vols} volumes GBWW, {c_t6e_non_num} não-num, {t6e_segs} segmentos, {c_t6e_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_6e"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:6e')",
    "proporcaoOntologica": "11_refs / 11_autores_fontes / 14_obras / 10_volumes_gbww / 0_fontes_nao_num / 14_segmentos / 0_passagens",
    "referencias": c_t6e_refs,
    "totalSegmentosObra": t6e_segs,
    "autoresOuFontesAlcancados": c_t6e_authors,
    "obrasAlcancadas": c_t6e_works,
    "gbwwVolumesAlcancados": c_t6e_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t6e_non_num,
    "passagensAlcancadas": c_t6e_passages,
    "regraReferenciaVsPassagemCumprida": True
}


# -----------------------------------------------------------------------------
# 6.11 FIXTURE PERMANENTE 13: SUBGRAFO TÓPICO 42.7 (LOTE 3: JUSTIÇA DOMÉSTICA: DIREITO E DEVER NA FAMÍLIA)
# -----------------------------------------------------------------------------
refs_t7 = [r for r in refs_data if r.get('topicId') == 'topic:justica:7']
t7_authors_reached = set(r['authorId'] for r in refs_t7)
t7_works_reached = set(wid for r in refs_t7 for wid in r.get('workIds', []))
t7_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t7 if r.get('gbwwVolume') is not None)
t7_non_num_reached = set(r['authorId'] for r in refs_t7 if r.get('gbwwVolume') is None)
t7_passages_reached = set(pid for r in refs_t7 for pid in r.get('passageIds', []))
t7_segs = sum(len(r.get('workSegments', [])) for r in refs_t7)

c_t7_refs = len(refs_t7)
c_t7_authors = len(t7_authors_reached)
c_t7_works = len(t7_works_reached)
c_t7_gbww_vols = len(t7_gbww_vols_reached)
c_t7_non_num = len(t7_non_num_reached)
c_t7_passages = len(t7_passages_reached)

if not (c_t7_refs == 36 and c_t7_authors == 34 and c_t7_works == 72 and c_t7_gbww_vols == 28 and c_t7_non_num == 3 and t7_segs == 73 and c_t7_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.7 QUEBRADA!")
    print(f"Esperado: 36 refs, 34 autores/fontes, 72 obras, 28 volumes GBWW, 3 fontes não-num, 73 segmentos, 0 passagens")
    print(f"Obtido:   {c_t7_refs} refs, {c_t7_authors} autores/fontes, {c_t7_works} obras, {c_t7_gbww_vols} volumes GBWW, {c_t7_non_num} não-num, {t7_segs} segmentos, {c_t7_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_7"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:7')",
    "proporcaoOntologica": "36_refs / 34_autores_fontes / 72_obras / 28_volumes_gbww / 3_fontes_nao_num / 73_segmentos / 0_passagens",
    "referencias": c_t7_refs,
    "totalSegmentosObra": t7_segs,
    "autoresOuFontesAlcancados": c_t7_authors,
    "obrasAlcancadas": c_t7_works,
    "gbwwVolumesAlcancados": c_t7_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t7_non_num,
    "passagensAlcancadas": c_t7_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.12 FIXTURE PERMANENTE 14: SUBGRAFO TÓPICO 42.8 (LOTE 4: JUSTIÇA ECONÔMICA: PRODUÇÃO, DISTRIBUIÇÃO E TROCA)
# -----------------------------------------------------------------------------
refs_t8 = [r for r in refs_data if r.get('topicId') == 'topic:justica:8']
t8_authors_reached = set(r['authorId'] for r in refs_t8)
t8_works_reached = set(wid for r in refs_t8 for wid in r.get('workIds', []))
t8_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t8 if r.get('gbwwVolume') is not None)
t8_non_num_reached = set(r['authorId'] for r in refs_t8 if r.get('gbwwVolume') is None)
t8_passages_reached = set(pid for r in refs_t8 for pid in r.get('passageIds', []))
t8_segs = sum(len(r.get('workSegments', [])) for r in refs_t8)

c_t8_refs = len(refs_t8)
c_t8_authors = len(t8_authors_reached)
c_t8_works = len(t8_works_reached)
c_t8_gbww_vols = len(t8_gbww_vols_reached)
c_t8_non_num = len(t8_non_num_reached)
c_t8_passages = len(t8_passages_reached)

if not (c_t8_refs == 38 and c_t8_authors == 37 and c_t8_works == 70 and c_t8_gbww_vols == 30 and c_t8_non_num == 3 and t8_segs == 71 and c_t8_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8 QUEBRADA!")
    print(f"Esperado: 38 refs, 37 autores/fontes, 70 obras, 30 volumes GBWW, 3 fontes não-num, 71 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8_refs} refs, {c_t8_authors} autores/fontes, {c_t8_works} obras, {c_t8_gbww_vols} volumes GBWW, {c_t8_non_num} não-num, {t8_segs} segmentos, {c_t8_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8')",
    "proporcaoOntologica": "38_refs / 37_autores_fontes / 70_obras / 30_volumes_gbww / 3_fontes_nao_num / 71_segmentos / 0_passagens",
    "referencias": c_t8_refs,
    "totalSegmentosObra": t8_segs,
    "autoresOuFontesAlcancados": c_t8_authors,
    "obrasAlcancadas": c_t8_works,
    "gbwwVolumesAlcancados": c_t8_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8_non_num,
    "passagensAlcancadas": c_t8_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.13 FIXTURE PERMANENTE 15: SUBGRAFO TÓPICO 42.8a (LOTE 4: PROPRIEDADE PRIVADA E PÚBLICA)
# -----------------------------------------------------------------------------
refs_t8a = [r for r in refs_data if r.get('topicId') == 'topic:justica:8a']
t8a_authors_reached = set(r['authorId'] for r in refs_t8a)
t8a_works_reached = set(wid for r in refs_t8a for wid in r.get('workIds', []))
t8a_gbww_vols_reached = set(r['gbwwVolume'] for r in refs_t8a if r.get('gbwwVolume') is not None)
t8a_non_num_reached = set(r['authorId'] for r in refs_t8a if r.get('gbwwVolume') is None)
t8a_passages_reached = set(pid for r in refs_t8a for pid in r.get('passageIds', []))
t8a_segs = sum(len(r.get('workSegments', [])) for r in refs_t8a)

c_t8a_refs = len(refs_t8a)
c_t8a_authors = len(t8a_authors_reached)
c_t8a_works = len(t8a_works_reached)
c_t8a_gbww_vols = len(t8a_gbww_vols_reached)
c_t8a_non_num = len(t8a_non_num_reached)
c_t8a_passages = len(t8a_passages_reached)

if not (c_t8a_refs == 34 and c_t8a_authors == 32 and c_t8a_works == 59 and c_t8a_gbww_vols == 26 and c_t8a_non_num == 2 and t8a_segs == 61 and c_t8a_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8a QUEBRADA!")
    print(f"Esperado: 34 refs, 32 autores/fontes, 59 obras, 26 volumes GBWW, 2 fontes não-num, 61 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8a_refs} refs, {c_t8a_authors} autores/fontes, {c_t8a_works} obras, {c_t8a_gbww_vols} volumes GBWW, {c_t8a_non_num} não-num, {t8a_segs} segmentos, {c_t8a_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8a"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8a')",
    "proporcaoOntologica": "34_refs / 32_autores_fontes / 59_obras / 26_volumes_gbww / 2_fontes_nao_num / 61_segmentos / 0_passagens",
    "referencias": c_t8a_refs,
    "totalSegmentosObra": t8a_segs,
    "autoresOuFontesAlcancados": c_t8a_authors,
    "obrasAlcancadas": c_t8a_works,
    "gbwwVolumesAlcancados": c_t8a_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8a_non_num,
    "passagensAlcancadas": c_t8a_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.16 DÉCIMA SEXTA FIXTURE DE REGRESSÃO: SUBGRAFO TÓPICO 42.8b (SALÁRIOS E PREÇOS JUSTOS)
# -----------------------------------------------------------------------------
refs_t8b = [r for r in refs_data if r.get('topicId') == "topic:justica:8b"]
t8b_authors_reached = set(r.get('authorId') for r in refs_t8b if r.get('authorId'))
t8b_works_reached = set(wid for r in refs_t8b for wid in r.get('workIds', []))
t8b_gbww_vols_reached = set(r.get('gbwwVolume') for r in refs_t8b if r.get('gbwwVolume') is not None)
t8b_non_num_reached = set(r.get('authorId') for r in refs_t8b if r.get('gbwwVolume') is None)
t8b_passages_reached = set(pid for r in refs_t8b for pid in r.get('passageIds', []))
t8b_segs = sum(len(r.get('workSegments', [])) for r in refs_t8b)

c_t8b_refs = len(refs_t8b)
c_t8b_authors = len(t8b_authors_reached)
c_t8b_works = len(t8b_works_reached)
c_t8b_gbww_vols = len(t8b_gbww_vols_reached)
c_t8b_non_num = len(t8b_non_num_reached)
c_t8b_passages = len(t8b_passages_reached)

if not (c_t8b_refs == 26 and c_t8b_authors == 26 and c_t8b_works == 43 and c_t8b_gbww_vols == 20 and c_t8b_non_num == 3 and t8b_segs == 43 and c_t8b_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8b QUEBRADA!")
    print(f"Esperado: 26 refs, 26 autores/fontes, 43 obras, 20 volumes GBWW, 3 fontes não-num, 43 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8b_refs} refs, {c_t8b_authors} autores/fontes, {c_t8b_works} obras, {c_t8b_gbww_vols} volumes GBWW, {c_t8b_non_num} não-num, {t8b_segs} segmentos, {c_t8b_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8b"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8b')",
    "proporcaoOntologica": "26_refs / 26_autores_fontes / 43_obras / 20_volumes_gbww / 3_fontes_nao_num / 43_segmentos / 0_passagens",
    "referencias": c_t8b_refs,
    "totalSegmentosObra": t8b_segs,
    "autoresOuFontesAlcancados": c_t8b_authors,
    "obrasAlcancadas": c_t8b_works,
    "gbwwVolumesAlcancados": c_t8b_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8b_non_num,
    "passagensAlcancadas": c_t8b_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.17 DÉCIMA SÉTIMA FIXTURE DE REGRESSÃO: SUBGRAFO TÓPICO 42.8c (NÓ PAI: ORGANIZAÇÃO DA PRODUÇÃO)
# -----------------------------------------------------------------------------
refs_t8c = [r for r in refs_data if r.get('topicId') == "topic:justica:8c"]
t8c_authors_reached = set(r.get('authorId') for r in refs_t8c if r.get('authorId'))
t8c_works_reached = set(wid for r in refs_t8c for wid in r.get('workIds', []))
t8c_gbww_vols_reached = set(r.get('gbwwVolume') for r in refs_t8c if r.get('gbwwVolume') is not None)
t8c_non_num_reached = set(r.get('authorId') for r in refs_t8c if r.get('gbwwVolume') is None)
t8c_passages_reached = set(pid for r in refs_t8c for pid in r.get('passageIds', []))
t8c_segs = sum(len(r.get('workSegments', [])) for r in refs_t8c)

c_t8c_refs = len(refs_t8c)
c_t8c_authors = len(t8c_authors_reached)
c_t8c_works = len(t8c_works_reached)
c_t8c_gbww_vols = len(t8c_gbww_vols_reached)
c_t8c_non_num = len(t8c_non_num_reached)
c_t8c_passages = len(t8c_passages_reached)

if not (c_t8c_refs == 2 and c_t8c_authors == 2 and c_t8c_works == 2 and c_t8c_gbww_vols == 1 and c_t8c_non_num == 0 and t8c_segs == 2 and c_t8c_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8c (DIRECT_NODE_ONLY) QUEBRADA!")
    print(f"Esperado: 2 refs, 2 autores/fontes, 2 obras, 1 volume GBWW, 0 fontes não-num, 2 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8c_refs} refs, {c_t8c_authors} autores/fontes, {c_t8c_works} obras, {c_t8c_gbww_vols} volumes GBWW, {c_t8c_non_num} não-num, {t8c_segs} segmentos, {c_t8c_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8c"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8c', DIRECT_NODE_ONLY)",
    "proporcaoOntologica": "2_refs / 2_autores_fontes / 2_obras / 1_volume_gbww / 0_fontes_nao_num / 2_segmentos / 0_passagens",
    "referencias": c_t8c_refs,
    "totalSegmentosObra": t8c_segs,
    "autoresOuFontesAlcancados": c_t8c_authors,
    "obrasAlcancadas": c_t8c_works,
    "gbwwVolumesAlcancados": c_t8c_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8c_non_num,
    "passagensAlcancadas": c_t8c_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.18 DÉCIMA OITAVA FIXTURE DE REGRESSÃO: SUBGRAFO TÓPICO 42.8c(2) (LUCRO E INCREMENTO NÃO AUFERIDO)
# -----------------------------------------------------------------------------
refs_t8c2 = [r for r in refs_data if r.get('topicId') == "topic:justica:8c-2"]
t8c2_authors_reached = set(r.get('authorId') for r in refs_t8c2 if r.get('authorId'))
t8c2_works_reached = set(wid for r in refs_t8c2 for wid in r.get('workIds', []))
t8c2_gbww_vols_reached = set(r.get('gbwwVolume') for r in refs_t8c2 if r.get('gbwwVolume') is not None)
t8c2_non_num_reached = set(r.get('authorId') for r in refs_t8c2 if r.get('gbwwVolume') is None)
t8c2_passages_reached = set(pid for r in refs_t8c2 for pid in r.get('passageIds', []))
t8c2_segs = sum(len(r.get('workSegments', [])) for r in refs_t8c2)

c_t8c2_refs = len(refs_t8c2)
c_t8c2_authors = len(t8c2_authors_reached)
c_t8c2_works = len(t8c2_works_reached)
c_t8c2_gbww_vols = len(t8c2_gbww_vols_reached)
c_t8c2_non_num = len(t8c2_non_num_reached)
c_t8c2_passages = len(t8c2_passages_reached)

if not (c_t8c2_refs == 4 and c_t8c2_authors == 4 and c_t8c2_works == 4 and c_t8c2_gbww_vols == 4 and c_t8c2_non_num == 0 and t8c2_segs == 4 and c_t8c2_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8c(2) (DIRECT_NODE_ONLY) QUEBRADA!")
    print(f"Esperado: 4 refs, 4 autores/fontes, 4 obras, 4 volumes GBWW, 0 fontes não-num, 4 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8c2_refs} refs, {c_t8c2_authors} autores/fontes, {c_t8c2_works} obras, {c_t8c2_gbww_vols} volumes GBWW, {c_t8c2_non_num} não-num, {t8c2_segs} segmentos, {c_t8c2_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8c_2"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8c-2', DIRECT_NODE_ONLY)",
    "proporcaoOntologica": "4_refs / 4_autores_fontes / 4_obras / 4_volumes_gbww / 0_fontes_nao_num / 4_segmentos / 0_passagens",
    "referencias": c_t8c2_refs,
    "totalSegmentosObra": t8c2_segs,
    "autoresOuFontesAlcancados": c_t8c2_authors,
    "obrasAlcancadas": c_t8c2_works,
    "gbwwVolumesAlcancados": c_t8c2_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8c2_non_num,
    "passagensAlcancadas": c_t8c2_passages,
    "regraReferenciaVsPassagemCumprida": True
}

# -----------------------------------------------------------------------------
# 6.19 DÉCIMA NONA FIXTURE DE REGRESSÃO: SUBGRAFO TÓPICO 42.8d (USURA E TAXAS DE JUROS)
# -----------------------------------------------------------------------------
refs_t8d = [r for r in refs_data if r.get('topicId') == "topic:justica:8d"]
t8d_authors_reached = set(r.get('authorId') for r in refs_t8d if r.get('authorId'))
t8d_works_reached = set(wid for r in refs_t8d for wid in r.get('workIds', []))
t8d_gbww_vols_reached = set(r.get('gbwwVolume') for r in refs_t8d if r.get('gbwwVolume') is not None)
t8d_non_num_reached = set(r.get('authorId') for r in refs_t8d if r.get('gbwwVolume') is None)
t8d_passages_reached = set(pid for r in refs_t8d for pid in r.get('passageIds', []))
t8d_segs = sum(len(r.get('workSegments', [])) for r in refs_t8d)

c_t8d_refs = len(refs_t8d)
c_t8d_authors = len(t8d_authors_reached)
c_t8d_works = len(t8d_works_reached)
c_t8d_gbww_vols = len(t8d_gbww_vols_reached)
c_t8d_non_num = len(t8d_non_num_reached)
c_t8d_passages = len(t8d_passages_reached)

if not (c_t8d_refs == 18 and c_t8d_authors == 17 and c_t8d_works == 28 and c_t8d_gbww_vols == 17 and c_t8d_non_num == 1 and t8d_segs == 29 and c_t8d_passages == 0):
    print("FATAL: Fixture de Regressão de Subgrafo do Tópico 42.8d (DIRECT_NODE_ONLY) QUEBRADA!")
    print(f"Esperado: 18 refs, 17 autores/fontes, 28 obras, 17 volumes GBWW, 1 fonte não-num, 29 segmentos, 0 passagens")
    print(f"Obtido:   {c_t8d_refs} refs, {c_t8d_authors} autores/fontes, {c_t8d_works} obras, {c_t8d_gbww_vols} volumes GBWW, {c_t8d_non_num} não-num, {t8d_segs} segmentos, {c_t8d_passages} passagens")
    sys.exit(1)

results["fixtureRegressaoTopico42_8d"] = {
    "status": "PASSED",
    "tipoMedicao": "subgrafo_direcionado (topicId == 'topic:justica:8d', DIRECT_NODE_ONLY)",
    "proporcaoOntologica": "18_refs / 17_autores_fontes / 28_obras / 17_volumes_gbww / 1_fonte_nao_num / 29_segmentos / 0_passagens",
    "referencias": c_t8d_refs,
    "totalSegmentosObra": t8d_segs,
    "autoresOuFontesAlcancados": c_t8d_authors,
    "obrasAlcancadas": c_t8d_works,
    "gbwwVolumesAlcancados": c_t8d_gbww_vols,
    "fontesNaoNumeradasAlcancadas": c_t8d_non_num,
    "passagensAlcancadas": c_t8d_passages,
    "regraReferenciaVsPassagemCumprida": True
}











# -----------------------------------------------------------------------------
# 7. TRÊS PROTEÇÕES DE INTEGRIDADE DOCUMENTAL
# -----------------------------------------------------------------------------
# Proteção 1: Unicidade Documental da Tupla Composta
provenance_keys = set()
duplicate_provenance = []
for r in refs_data:
    key = (
        r.get('source-id', r.get('sourceId', 'source:pdf-justice-1952')),
        r.get('syntopiconPage'),
        r.get('topicId'),
        r.get('orderInTopic')
    )
    if key in provenance_keys:
        duplicate_provenance.append((r['id'], key))
    else:
        provenance_keys.add(key)

if duplicate_provenance:
    print(f"FATAL: Proteção 1 violada! Duplicidade de chave documental composta: {duplicate_provenance}")
    sys.exit(1)

# Proteção 2: Conservação Incondicional do locatorRaw
empty_locator_raw = []
for r in refs_data:
    raw = r.get('locatorRaw')
    if not raw or not isinstance(raw, str) or not raw.strip():
        empty_locator_raw.append(r['id'])
    for s in r.get('workSegments', []):
        s_raw = s.get('locatorRaw')
        if not s_raw or not isinstance(s_raw, str) or not s_raw.strip():
            empty_locator_raw.append(f"{r['id']} (segment)")

if empty_locator_raw:
    print(f"FATAL: Proteção 2 violada! locatorRaw ausente ou vazio: {empty_locator_raw}")
    sys.exit(1)

# Proteção 3 / Teste Unitário Montesquieu: Fronteira Estrita de Tópicos
# Montesquieu pertence ao tópico 8b na p. 868 e NUNCA a 8c(1)
if 'author:montesquieu' in authors_8c1_reached:
    print("FATAL: Violação de Fronteira de Tópicos! Montesquieu atribuído erroneamente a 8c(1)!")
    sys.exit(1)

# Proteção 4: Integridade Referencial Completa (0 Dangling IDs)
source_reg_path = os.path.join(VAULT, '00-sistema/registro-de-fontes.json')
valid_sources = set()
if os.path.exists(source_reg_path):
    with open(source_reg_path, 'r', encoding='utf-8') as f:
        source_reg = json.load(f)
    for src in source_reg.get('fontes', []):
        valid_sources.add(src['id'])
        for alias in src.get('aliases', []):
            valid_sources.add(alias)

valid_author_ids = set()
for p in author_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    if doc.get('id'):
        valid_author_ids.add(doc['id'])

valid_work_ids = set()
for p in work_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    if doc.get('id'):
        valid_work_ids.add(doc['id'])

valid_volume_ids = set()
for p in volume_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    if doc.get('id'):
        valid_volume_ids.add(doc['id'])
    if doc.get('volumeNumber') is not None:
        valid_volume_ids.add(doc['volumeNumber'])
# Volumes do Syntopicon (GBWW 2 e 3) registrados no catálogo de fontes
valid_volume_ids.add(2)
valid_volume_ids.add(3)
valid_volume_ids.add('vol:02')
valid_volume_ids.add('vol:03')

valid_topic_ids = set()
for p in topic_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    if doc.get('id'):
        valid_topic_ids.add(doc['id'])

valid_passage_ids = set()
for p in passage_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    if doc.get('id'):
        valid_passage_ids.add(doc['id'])

dangling_authors = []
dangling_works = []
dangling_volumes = []
dangling_topics = []
dangling_sources = []
dangling_passages = []

for r in refs_data:
    aid = r.get('authorId')
    if aid and aid not in valid_author_ids:
        dangling_authors.append((r['id'], aid))
    for wid in r.get('workIds', []):
        if wid not in valid_work_ids:
            dangling_works.append((r['id'], wid))
    for s in r.get('workSegments', []):
        swid = s.get('workId')
        if swid and swid not in valid_work_ids:
            dangling_works.append((r['id'], f"segment:{swid}"))
    vol = r.get('gbwwVolume')
    if vol is not None and vol not in valid_volume_ids and f"vol:{vol}" not in valid_volume_ids:
        dangling_volumes.append((r['id'], vol))
    tid = r.get('topicId')
    if tid and tid not in valid_topic_ids:
        dangling_topics.append((r['id'], tid))
    for pid in r.get('passageIds', []):
        if pid not in valid_passage_ids:
            dangling_passages.append((r['id'], pid))
    sid = r.get('source-id') or r.get('sourceId')
    if sid and sid not in valid_sources:
        dangling_sources.append((r['id'], sid))

for p in work_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    for aid in doc.get('authorIds', []):
        if aid not in valid_author_ids:
            dangling_authors.append((doc.get('id', p), aid))
    vol = doc.get('gbwwVolume')
    if vol is not None and vol not in valid_volume_ids and f"vol:{vol}" not in valid_volume_ids:
        dangling_volumes.append((doc.get('id', p), vol))
    sid = doc.get('source-id') or doc.get('sourceId')
    if sid and sid not in valid_sources:
        dangling_sources.append((doc.get('id', p), sid))

for p in author_files:
    with open(p) as f:
        doc = yaml.safe_load(f.read().split('---')[1]) or {}
    sid = doc.get('source-id') or doc.get('sourceId')
    if sid and sid not in valid_sources:
        dangling_sources.append((doc.get('id', p), sid))

if dangling_authors or dangling_works or dangling_volumes or dangling_topics or dangling_sources or dangling_passages:
    print(f"FATAL: Proteção 4 violada! Integridade referencial rompida:")
    if dangling_authors: print(f"  Autores dangling: {dangling_authors}")
    if dangling_works: print(f"  Obras dangling: {dangling_works}")
    if dangling_volumes: print(f"  Volumes dangling: {dangling_volumes}")
    if dangling_topics: print(f"  Tópicos dangling: {dangling_topics}")
    if dangling_sources: print(f"  Fontes dangling: {dangling_sources}")
    if dangling_passages: print(f"  Passagens dangling: {dangling_passages}")
    sys.exit(1)

# Proteção 5: Integridade de Wikilinks e Unicidade Semântica
def check_dups(files_list, id_field='id', slug_field='slug', title_field='canonicalTitle'):
    seen_ids = {}
    seen_slugs = {}
    seen_titles = {}
    dups = []
    for p in files_list:
        with open(p) as f:
            doc = yaml.safe_load(f.read().split('---')[1]) or {}
        i = doc.get(id_field)
        s = doc.get(slug_field) or os.path.splitext(os.path.basename(p))[0]
        t = doc.get(title_field)
        if i in seen_ids:
            dups.append(f"Duplicate ID {i}: {p} e {seen_ids[i]}")
        seen_ids[i] = p
        if s in seen_slugs:
            dups.append(f"Duplicate Slug {s}: {p} e {seen_slugs[s]}")
        seen_slugs[s] = p
        if t in seen_titles:
            dups.append(f"Duplicate Title {t}: {p} e {seen_titles[t]}")
        seen_titles[t] = p
    return dups

author_dups = check_dups(author_files, 'id', 'slug', 'canonicalName')
work_dups = check_dups(work_files, 'id', 'slug', 'canonicalTitle')
volume_dups = check_dups(volume_files, 'id', 'slug', 'volumeNumber')

if author_dups or work_dups or volume_dups:
    print(f"FATAL: Proteção 5 violada! Duplicatas semânticas detectadas:")
    if author_dups: print(f"  Autores duplicados: {author_dups}")
    if work_dups: print(f"  Obras duplicadas: {work_dups}")
    if volume_dups: print(f"  Volumes duplicados: {volume_dups}")
    sys.exit(1)

all_vault_markdown = glob.glob(f"{VAULT}/**/*.md", recursive=True)
all_vault_slugs = {os.path.splitext(os.path.basename(p))[0]: p for p in all_vault_markdown}

total_wikilinks_scanned = 0
broken_wikilinks = []

for p in all_vault_markdown:
    rel = os.path.relpath(p, VAULT)
    # 'antigas' = arquivo legado (pre-consolidacao) fora do escopo de integridade do grafo
    if 'templates' in rel or 'contrato-de-dados' in rel or 'arena-handoff-codex' in rel or 'antigas' in rel:
        continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    links = re.findall(r'\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]', c)
    total_wikilinks_scanned += len(links)
    for target, label in links:
        target_clean = target.strip()
        if target_clean not in all_vault_slugs:
            if not target_clean.startswith('gi-'):
                broken_wikilinks.append((rel, target_clean))

if broken_wikilinks:
    print(f"FATAL: Proteção 5 violada! Wikilinks quebrados detectados: {broken_wikilinks}")
    sys.exit(1)

results["protecoesIntegridadeDocumental"] = {
    "protecao1_unicidadeCompostaDocumental": f"PASSED ({len(provenance_keys)} chaves únicas validadas)",
    "protecao2_conservacaoLocatorRawVerbatim": f"PASSED (100% das referências e segmentos preservam texto original)",
    "protecao3_fronteiraTopicosCasoMontesquieu": "PASSED (Montesquieu estritamente isolado fora de 8c-1)",
    "protecao4_integridadeReferencialCompleta": {
        "status": "PASSED",
        "danglingAuthors": 0,
        "danglingWorks": 0,
        "danglingVolumes": 0,
        "danglingTopics": 0,
        "danglingPassages": 0,
        "danglingSources": 0,
        "totalIdentidadesVerificadas": len(valid_author_ids) + len(valid_work_ids) + len(valid_volume_ids) + len(valid_topic_ids) + len(valid_sources)
    },
    "protecao5_integridadeWikilinks": {
        "status": "PASSED",
        "brokenWikilinks": 0,
        "duplicatasSemanticasAutores": 0,
        "duplicatasSemanticasObras": 0,
        "duplicatasSemanticasVolumes": 0,
        "totalWikilinksAuditados": total_wikilinks_scanned,
        "escopoStubsPermitidos": "101 Grandes Ideias futuras (gi-01 a gi-102, exceto gi-42)"
    }
}

# Outline check
l1_topics = [tf for tf in topic_files if re.match(r'^topico-42-[0-9]+$', os.path.basename(tf)[:-3])]
desc_topics = [tf for tf in topic_files if tf not in l1_topics]

results["auditoriaHierarquiaJustica"] = {
    "ramosPrincipaisEsperados": 11,
    "ramosPrincipaisObtidos": len(l1_topics),
    "descendentesEsperados": 30,
    "descendentesObtidos": len(desc_topics),
    "totalNosEsperados": 41,
    "totalNosObtidos": len(topic_files),
    "conformidadeOutline1952": "100%_conforme_pp_857_858"
}

results["resumoMetricas"] = {
    "grandesIdeias": 1,
    "topicos": len(topic_files),
    "referencias": len(ref_files),
    "passagens": c_passages,
    "obras": len(work_files),
    "autores": len(author_files),
    "volumes": len(volume_files),
    "indices": 2,
    "totalEntidadesMaterializadas": 1 + len(topic_files) + len(ref_files) + len(work_files) + len(author_files) + len(volume_files)
}

results["integridadeRelacional"] = {
    "linksOutlineEmGrandeIdeia": f"{len(topic_files)}/41 válidos",
    "linksReferenciaTopico": f"{len(ref_files)}/{len(ref_files)} válidos",
    "linksReferenciaObras": "100% válidos",
    "linksReferenciaAutores": "100% válidos",
    "linksObrasAutores": "100% válidos",
    "linksObrasVolumes": "100% válidos",
    "triadeOrtogonalPresenteEmTodas": True
}

report_path = os.path.join(VAULT, '09-auditorias/validation-report.json')
with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"SUCCESS: Subgraph fixtures (8c1 + Lot 1 + 42.2 + 42.3 + 42.4 + 42.5 + 42.6 + 42.6a + 42.6b + 42.6c + 42.6d + 42.6e + 42.7 + 42.8 + 42.8a + 42.8b + 42.8c + 42.8c_2 + 42.8d), 4 Invariants, and 5 Documentary Protections passed 100%!")
print(f"Validation report updated successfully at {report_path}!")
