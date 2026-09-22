#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT MODE — Laudo Completo do Estado do Vault (sem parar na primeira FATAL)
============================================================================

Executa o `validate_vault.py` REAL de forma iterativa: cada vez que um check
falha (FATAL), o laudo registra a falha com todos os detalhes impressos,
neutraliza APENAS esse check (if -> if False:) e reexecuta, até o validador
terminar limpo. Assim o laudo contém TODOS os checks (passados e falhos) sem
qualquer divergência da lógica canônica de validação.

Garantias:
  - O `validation-report.json` canônico NUNCA é sobrescrito (o nome do
    relatório é redirecionado em modo auditoria);
  - A lógica de validação é a do validador original, sem reimplementação.

Uso:
    python3 00-sistema/scripts/audit_report.py
Exit code: 0 = 100% verde, 1 = há falhas (laudo gravado em ambos os casos).
"""
import os, io, re, sys, json, datetime, glob
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.abspath(os.path.join(HERE, '..', '..'))
VALIDATOR = os.path.join(HERE, 'validate_vault.py')

SRC = open(VALIDATOR, encoding='utf-8').read()
# proteção: nunca sobrescrever o relatório canônico histórico
SRC = SRC.replace("'09-auditorias/validation-report.json'",
                  "'09-auditorias/audit-report-internal.json'")

# ordem importa: âncoras mais específicas antes das genéricas
# (as âncoras são substratos EXATOS das mensagens FATAL impressas pelo validador)
ANCHOR_KEY_MAP = [
    ('Subgrafo 8c(1) QUEBRADA', 'fixtureRegressaoGoldenCase8c1'),
    ('Lote 1 QUEBRADA', 'fixtureRegressaoLote1'),
    ('Tópico 42.8c(2)', 'fixtureRegressaoTopico42_8c_2'),
    ('Tópico 42.8c (DIRECT_NODE_ONLY)', 'fixtureRegressaoTopico42_8c'),
    ('Tópico 42.8d', 'fixtureRegressaoTopico42_8d'),
    ('Tópico 42.8a', 'fixtureRegressaoTopico42_8a'),
    ('Tópico 42.8b', 'fixtureRegressaoTopico42_8b'),
    ('Tópico 42.8 QUEBRADA', 'fixtureRegressaoTopico42_8'),
    ('Tópico 42.7', 'fixtureRegressaoTopico42_7'),
    ('Tópico 42.6a', 'fixtureRegressaoTopico42_6a'),
    ('Tópico 42.6b', 'fixtureRegressaoTopico42_6b'),
    ('Tópico 42.6c', 'fixtureRegressaoTopico42_6c'),
    ('Tópico 42.6d', 'fixtureRegressaoTopico42_6d'),
    ('Tópico 42.6e', 'fixtureRegressaoTopico42_6e'),
    ('Tópico 42.6 QUEBRADA', 'fixtureRegressaoTopico42_6'),
    ('Tópico 42.5', 'fixtureRegressaoTopico42_5'),
    ('Tópico 42.4', 'fixtureRegressaoTopico42_4'),
    ('Tópico 42.3', 'fixtureRegressaoTopico42_3'),
    ('Tópico 42.2', 'fixtureRegressaoTopico42_2'),
    ('Proteção 1', 'protecoesIntegridadeDocumental'),
    ('Proteção 2', 'protecoesIntegridadeDocumental'),
    ('Fronteira de Tópicos', 'protecoesIntegridadeDocumental'),
    ('Proteção 4', 'protecoesIntegridadeDocumental'),
    ('Proteção 5 violada! Duplicatas', 'protecoesIntegridadeDocumental'),
    ('Proteção 5 violada! Wikilinks', 'protecoesIntegridadeDocumental'),
    ('Invariante 1', 'invariantesArquiteturais'),
    ('Invariante 2', 'invariantesArquiteturais'),
    ('Invariante 3', 'invariantesArquiteturais'),
    ('Invariante 4', 'invariantesArquiteturais'),
]


def find_fatal_anchor(line):
    """Retorna (âncora, chave_results) correspondente à linha FATAL."""
    for anchor, key in ANCHOR_KEY_MAP:
        if anchor in line:
            return anchor, key
    return None, None


def neutralize_check(src, anchor):
    """Neutraliza o BLOCO if..sys.exit(1) inteiro do check que falhou.

    Substitui a faixa [linha do if .. linha do sys.exit(1)] por `if False:` +
    `pass`, preservando a indentação original. Isso é sintaticamente seguro
    mesmo quando a condição do if ocupa múltiplas linhas (que é o caso das
    fixtures de subgrafo).
    """
    # 1) localiza a linha do print FATAL que contém a âncora
    idx = None
    for m in re.finditer(r'print\((f?)"[^"]*' + re.escape(anchor), src):
        idx = m.start()
        break
    if idx is None:
        pos = src.find(anchor)
        if pos == -1:
            raise RuntimeError(f'âncora não encontrada no validador: {anchor!r}')
        idx = pos
    print_line_start = src.rfind('\n', 0, idx) + 1

    # 2) sobe até a linha `if` que abre o bloco (condição pode ser multi-linha)
    before = src[:print_line_start]
    lines = before.splitlines(keepends=True)
    if_start = None
    if_indent = ''
    for i in range(len(lines) - 1, -1, -1):
        stripped = lines[i].lstrip()
        if stripped.startswith('if ') or stripped.startswith('if('):
            if_start = sum(len(l) for l in lines[:i])
            if_indent = lines[i][:len(lines[i]) - len(stripped)]
            break
    if if_start is None:
        raise RuntimeError(f'if de encerramento não encontrado para: {anchor!r}')
    # indentação do corpo = indentação da própria linha do print FATAL
    print_line_end = src.find('\n', print_line_start)
    print_line = src[print_line_start:print_line_end if print_line_end != -1 else len(src)]
    body_indent = print_line[:len(print_line) - len(print_line.lstrip())] or '    '

    # 3) desce até o sys.exit(1) que fecha o bloco
    exit_pos = src.find('sys.exit(1)', if_start)
    if exit_pos == -1:
        raise RuntimeError(f'sys.exit(1) não encontrado após o if de: {anchor!r}')
    exit_line_end = src.find('\n', exit_pos)
    if exit_line_end == -1:
        exit_line_end = len(src)

    replacement = (f'{if_indent}if False:  # AUDIT_MODE: check neutralizado\n'
                   f'{body_indent}pass')
    return src[:if_start] + replacement + src[exit_line_end:]


def run_validator(src):
    g = {'__name__': '__audit__', '__file__': VALIDATOR}
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            exec(compile(src, VALIDATOR, 'exec'), g)
        except SystemExit:
            pass  # check falhou no meio do script; stdout já capturado
    return g.get('results', {}), buf.getvalue()


# -----------------------------------------------------------------------------
# Loop iterativo: executa, captura a 1ª FATAL, neutraliza, repete
# -----------------------------------------------------------------------------
failures = []
src2 = SRC
for _ in range(40):
    results, out = run_validator(src2)
    cur = None
    for line in out.splitlines():
        ls = line.rstrip()
        if not ls.strip():
            continue
        if ls.startswith('FATAL'):
            if cur:
                failures.append(cur)
            anchor, key = find_fatal_anchor(ls)
            cur = {'check': key or 'desconhecido', 'veredito': ls.strip(), 'detalhes': []}
        elif cur is not None:
            cur['detalhes'].append(ls.strip())
    if cur:
        failures.append(cur)
    if cur is None:
        break  # run limpo (nenhum FATAL nesta execução)
    first_fatal = next(l for l in out.splitlines() if l.strip().startswith('FATAL'))
    anchor, _ = find_fatal_anchor(first_fatal)
    if anchor is None:
        raise RuntimeError(f'FATAL sem mapeamento conhecido: {first_fatal!r}')
    src2 = neutralize_check(src2, anchor)
else:
    raise RuntimeError('limite de iterações excedido — há falha cíclica?')

# -----------------------------------------------------------------------------
# Remove de `results` os checks que falharam (em modo auditoria o exec os
# gravaria como PASSED após o if False: — o veredito real vai em checksFalhos)
# -----------------------------------------------------------------------------
failed_keys = {f['check'] for f in failures if f['check'] != 'desconhecido'}
for k in [k for k in results if k in failed_keys]:
    results.pop(k)

# -----------------------------------------------------------------------------
# Resumo de gap: staging x materializado (o que falta, tópico a tópico)
# -----------------------------------------------------------------------------
staging_path = os.path.join(VAULT, '00-sistema/staging/referencias-candidatas.json')
if os.path.exists(staging_path):
    cands = json.load(open(staging_path, encoding='utf-8'))
    mat_ids = set()
    mat_keys = set()  # (topicId, orderInTopic) — a chave documental estavel
    for f in glob.glob(os.path.join(VAULT, '03-referencias/justica/*.md')):
        head = open(f, encoding='utf-8').read(4000)
        mi = re.search(r'^id:\s*"?([^\n"]+)', head, re.M)
        mt = re.search(r'^topicId:\s*"?([^\n"]+)', head, re.M)
        mo = re.search(r'^orderInTopic:\s*"?(\d+)', head, re.M)
        if mi:
            mat_ids.add(mi.group(1).strip())
        if mt and mo:
            mat_keys.add((mt.group(1).strip(), int(mo.group(1))))
    # uma ficha ja esta materializada se o id OU a chave documental batem
    # (o pipeline normaliza ids na materializacao, ex.: ref:justica:8d-01 ->
    #  ref:justica:8d:01-antigo-testamento; a chave estavel e topicId+orderInTopic)
    def materialized(c):
        if c.get('id') in mat_ids:
            return True
        return (c.get('topicId'), c.get('orderInTopic')) in mat_keys
    missing = [c for c in cands if not materialized(c)]
    by_topic = {}
    for c in missing:
        t = c.get('topicId', '?')
        e = by_topic.setdefault(t, {'candidatos': 0, 'ids': []})
        e['candidatos'] += 1
        e['ids'].append(c['id'])
    results['resumoGapStaging'] = {
        'candidatosNoStaging': len(cands),
        'fichasMaterializadas': len(mat_ids),
        'candidatosAindaNaoMaterializados': len(missing),
        'porTopico': {t: by_topic[t] for t in sorted(by_topic, key=lambda x: (len(x), x))},
        'nota': ('Fichas presentes no staging mas ausentes em 03-referencias/justica/. '
                 'Familias 1-8: status "verified" no staging (auditadas visualmente); '
                 'familias 9-11: "needs_verification" (pendentes de colacao).')
    }

# -----------------------------------------------------------------------------
# Veredito global + laudo
# -----------------------------------------------------------------------------
results['timestamp'] = datetime.datetime.now().astimezone().isoformat()
results['suite'] = 'Audit Mode (contínuo) — Laudo de Estado do Repositorio'
results['status'] = 'PASSED' if not failures else f'FAILED ({len(failures)} check(s) falharam)'
if failures:
    results['checksFalhos'] = failures

today = datetime.date.today().isoformat()
audit_path = os.path.join(VAULT, '09-auditorias/audit-report-' + today + '.json')
with open(audit_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
internal = os.path.join(VAULT, '09-auditorias/audit-report-internal.json')
if os.path.exists(internal):
    os.remove(internal)

# -----------------------------------------------------------------------------
# Resumo legível
# -----------------------------------------------------------------------------
passed = sorted(k for k, v in results.items()
                if isinstance(v, dict) and v.get('status') == 'PASSED')
print(f"=== AUDIT MODE — {results['status']} ===")
print(f"Checks PASSED: {len(passed)} | Checks FALHOS: {len(failures)}")
for k in passed:
    print(f"  [PASS] {k}")
for fl in failures:
    print(f"  [FAIL] {fl['check']}")
    print('        ', fl['veredito'])
    for d in fl.get('detalhes', []):
        print('        ', d)
gs = results.get('resumoGapStaging')
if gs:
    print()
    print("=== GAP STAGING -> 03-referencias/justica ===")
    print(f"Staging: {gs['candidatosNoStaging']} | Materializadas: {gs['fichasMaterializadas']} | Faltando: {gs['candidatosAindaNaoMaterializados']}")
    for t, e in gs['porTopico'].items():
        print(f"  {t:24s} faltam {e['candidatos']:3d}")
print()
print(f"Laudo completo: {audit_path}")
sys.exit(0 if not failures else 1)
