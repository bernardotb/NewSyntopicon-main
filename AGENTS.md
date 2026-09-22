# AGENTS.md — Instruções Operacionais para Agentes de IA

> **Escopo:** Este arquivo é o guia operacional para qualquer agente de IA (Codex/ChatGPT,
> Cursor, Copilot, Arena, Claude etc.) que trabalhe neste repositório.
> **Autoridade:** Em caso de conflito, a ordem de precedência é:
> 1. `00-sistema/contrato-de-dados.md` (normativo canônico, versão 3.3-consolidada)
> 2. `00-sistema/schema-entidades.json` (schemas formais Draft 2020-12)
> 3. Este arquivo (resumo operacional)
> 4. `09-auditorias/` (histórico de decisões e laudos)

---

## 1. O que é este projeto

Vault **Obsidian** de estudo do **Syntopicon (1952)** — capítulo 42: **Justiça**
(*Great Books of the Western World*, Vol. 2, pp. 857–878), com arquitetura pronta
para as 102 Grandes Ideias. É um **grafo de conhecimento** com entidades:

```
GrandeIdeia (gi-42-justica)
  └── Tópico (41 nós: 42.1 … 42.11b)
        └── Referência Syntopicon (apontamento do índice de Adler)
              └── Passagem (excerto verificado — hoje: ZERO no vault)
Referência → Autor (06-autores) → Obra (05-obras) → Volume GBWW (07-volumes)
```

A fonte de verdade é a **edição impressa de 1952** (arquivo de colação:
`_fontes/Justice.pdf` no vault local do dono do projeto). O PDF **não** está
neste repositório (excluído por tamanho).

## 2. Estrutura de diretórios canônica

**Nunca criar novas pastas de nível superior.** As pastas oficiais:

| Pasta | Conteúdo | Regra |
|---|---|---|
| `00-sistema/` | Contrato, schemas, scripts, templates, staging | Staging = baseline versionado (V1→V2→V3); não editar à mão sem emitir nova versão |
| `01-grandes-ideias/` | Notas-mãe das 102 ideias (hoje: só `gi-42-justica.md`) | 1 nota por ideia |
| `02-topicos/justica/` | 41 nós de tópicos (outline pp. 857–858) | Estrutura fixada pelo Syntopicon de 1952 |
| `03-referencias/justica/` | **Todas** as fichas de referência (uma ficha = 1 linha impressa do índice) | Localização canônica; consultas Dataview apontam para cá |
| `04-passagens/` | Passagens textuais verificadas (hoje: 0) | Só existe via transcrição conferida da edição |
| `05-obras/` | Fichas de obras GBWW (187) | 1 ficha por obra canônica |
| `06-autores/` | Fichas de autores/fontes (54) | Inclui fontes jurídicas (Constituição EUA etc.) |
| `07-volumes/` | Fichas dos volumes físicos GBWW (43) | |
| `08-indices/` | MOCs e home (`home.md`, `moc-102-ideias.md`) | |
| `09-auditorias/` | Laudos, handoffs, relatórios de validação | Laudos de auditoria: `audit-report-<AAAA-MM-DD>.json` |
| `antigas/` | **Arquivo legado pré-consolidação** | Somente leitura; fora do escopo dos checks de integridade |
| `Code/` | Wordbanks experimentais de lexical analysis | Fora do grafo |

## 3. Invariantes inegociáveis (violar = quebrar o pipeline)

1. **`Referência != Passagem`** (Invariante 5 do contrato). Uma referência diz
   *onde procurar*; ela **nunca** contém nem autoriza inventar o texto da obra.
   Passagens só existem quando o trecho foi localizado, conferido e traduzido.
2. **Níveis de verificação** (Invariante 4). `verification: verified` só é
   atribuída mediante **colação visual linha a linha** contra o PDF de 1952.
   Saídas de extração/staging entram estritamente como `needs_verification`.
   Agentes **não promovem** status sozinhos.
3. **`locatorRaw` é verbatim** (Proteção 2). Nunca sintetizar, reconstruir ou
   "corrigir" o localizador impresso a partir de campos normalizados. O texto
   tipográfico é a autoridade primária.
4. **Unicidade documental composta** (Proteção 1):
   `(source-id, syntopiconPage, topicId, orderInTopic)` é única por ficha.
5. **Fixtures de regressão** — contagens auditadas que o validador verifica.
   Exemplos atuais: Golden Case 8c(1) = `18 refs / 17 autores / 20 obras /
   16 volumes / 0 passagens`; Lote 1 (1a–1f) = 53 refs. Se um conteúdo
   canônico legítimo mudar, **contrato + validador + fixture mudam juntos**,
   com laudo em `09-auditorias/`.
6. **Identidade canônica**: `id: "idea:justica"` é a identidade única da GI-42;
   `idea:042`/`idea:justice`/`GI-42` vivem só em `legacyIds`.
   Paridade numérica permanente: `numeroCanonico == numero-canonico == numero == 42`.
7. **Fronteiras de tópico** (Caso Montesquieu): a contiguidade visual na página
   nunca autoriza mover uma referência de `topicId`. O cabeçalho do subtópico é
   o único critério.
8. **Tríade ortogonal** presente em TODAS as notas:
   `provenance` / `epistemology` / `verification`
   (valores permitidos: ver `contrato-de-dados.md` §2).
9. **Wikilinks**: `[[slug-tecnico|Nome Exibido]]` — slug minúsculo, sem acento,
   hífens. O Obsidian resolve por slug (não por pasta), mas a pasta canônica
   acima permanece obrigatória para os queries Dataview.
10. **Templates obrigatórios** (`00-sistema/templates/`): `template-grande-ideia`,
    `template-topico`, `template-referencia`, `template-passagem`,
    `template-autor`, `template-obra`, `template-volume`.
11. **Schemas** (`00-sistema/schema-entidades.json`, Draft 2020-12):
    `GreatIdea`, `Topic`, `SyntopiconReference`, `Passage`, `Author`, `Work`,
    `Volume`, `Source`. Fichas novas devem validar contra o schema correspondente.

## 4. Pipeline de validação

Ambiente (Python 3): `pyyaml`, `jsonschema`.

```bash
python3 -m venv /tmp/vvault && /tmp/vvault/bin/pip install pyyaml jsonschema

# CI canônico — para na PRIMEIRA falha (FATAL) e grava
# 09-auditorias/validation-report.json apenas se tudo passar
/tmp/vvault/bin/python 00-sistema/scripts/validate_vault.py

# Laudo completo (contínuo; grava 09-auditorias/audit-report-<data>.json)
/tmp/vvault/bin/python 00-sistema/scripts/audit_report.py
```

Regras do agente:
- **Nunca sobrescrever** `09-auditorias/validation-report.json` (relatório
  histórico do vault completo) salvo execução canônico 100% verde.
- Estado atual do repositório: sempre o **mais recente** `audit-report-*.json`.
- Os scripts resolvem o vault pelo caminho relativo a si próprios — rode-os
  a partir da raiz do repositório.

## 5. Workflow padrão para trabalho de conteúdo

1. **Ler** o laudo de auditoria mais recente em `09-auditorias/` e o contrato.
2. **Materializar** fichas apenas a partir do staging
   (`00-sistema/staging/referencias-candidatas.json`), preservando o
   `verification` do candidato (nunca "upgrading" para `verified`).
3. **Ids/slugs** seguem o padrão existente:
   - id: `ref:justica:<tópico>:<ordem-2dígitos>-<autor>` (ex.: `ref:justica:8c-1:01-aristoteles`)
   - slug/nome de arquivo: `ref-42-<tópico>-<ordem>-<autor>.md` (ex.: `ref-42-8c-1-01-aristoteles.md`)
   - destino: `03-referencias/justica/<slug>.md`
4. **Rodar** `validate_vault.py` (ou `audit_report.py` para o quadro completo).
5. **Gravar laudo** em `09-auditorias/` quando houver auditoria relevante.
6. **Commit** em português, mensagem descritiva, com o escopo das mudanças.

## 6. Proibições rápidas

- ❌ Criar passagens ou citações sem conferência na edição (zero tolerância).
- ❌ "Corrigir" conteúdo canônico 1952 por inferência ou conhecimento externo.
- ❌ Renomear slugs/ids de entidades existentes (migrações só via `legacyIds`).
- ❌ Editar o baseline de staging à mão sem versionar (Vn → Vn+1).
- ❌ Quebrar fixtures sem atualizar contrato + validador + laudo.
- ❌ Adicionar pastas de nível superior fora da tabela da seção 2.
- ❌ Tratar `antigas/` como conteúdo ativo (arquivo; somente leitura).
- ❌ Push direto em `main` sem revisão humana — trabalhar em branch e abrir PR.

## 7. Contexto para o agente

- Idioma de trabalho: **português (BR)** — notas, commits, laudos.
- O vault local do dono (fora do GitHub) pode estar à frente deste repositório;
  divergências de conteúdo devem ser reportadas, não "resolvidas" por
  recriação a partir do staging.
- Decisões arquiteturais passadas estão documentadas em
  `09-auditorias/arena-handoff-codex.md` (consolidação de 2026-09-17).
- Este arquivo deve ser **mantido junto com o contrato**: mudanças de
  estrutura ou invariantes atualizam os dois, no mesmo commit.
