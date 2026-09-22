# CONTRATO DE DADOS E ONTOLOGIA DO ECOSSISTEMA SYNTOPICON

> **Status:** Documento Normativo Congelado (Baseline Canônico 1952)  
> **Versão:** 3.3-consolidada  
> **Escopo:** Padronização arquitetural única para o vault Obsidian e interoperabilidade com aplicações externas (TypeScript / SQLite / JSON).

---

## 1. Princípios Fundamentais e Invariantes Arquiteturais

1. **Invariante 1 — Identidade Canônica Autoritativa:**
   - O identificador lógico `id: "idea:justica"` é a única identidade autoritativa da Grande Ideia #42.
   - Os identificadores históricos (`idea:042`, `idea:justice`, `GI-42`) residem estritamente na propriedade `legacyIds: ["idea:042", "idea:justice", "GI-42"]` e **nunca devem gerar novas entidades no grafo**.
2. **Invariante 2 — Paridade Estrita dos Campos Numéricos:**
   - Por razões de retrocompatibilidade com diferentes scripts e templates, coexistem três chaves numéricas que devem satisfazer permanentemente a igualdade:
     `numeroCanonico == numero-canonico == numero == 42`
   - Qualquer divergência entre esses campos invalida o pipeline de CI/auditoria.
3. **Invariante 3 — Distinção Semântica entre `layer` e `camadas`:**
   - A propriedade `layer: canonical` define a natureza ontológica da entidade `GrandeIdeia` (ela própria é uma das 102 ideias canônicas de Mortimer J. Adler no Syntopicon de 1952).
   - A lista `camadas: [canonical, source, editorial, contemporary-extension, personal]` descreve a tipologia de conteúdos coexistentes no corpo do documento, garantindo que discussões pós-1952 (como Rawls, Nozick, Sandel e Sen) sejam prontamente identificadas como extensões editoriais e jamais confundidas com o corpus canônico da GBWW.
4. **Invariante 4 — Separação Estrita de Níveis de Verificação:**
   - A chave `verification: verified` atesta que a estrutura hierárquica e o outline da nota foram confrontados visualmente e conferidos contra as pp. 857–858 do Syntopicon de 1952.
   - A chave `corpus-ingestion-verification: needs_verification` atesta que a contagem global dos 826 registros (795 autorais + 31 bíblicos) provém de ingestão estruturada e requer auditoria independente linha por linha de todo o capítulo 42.
5. **Invariante 5 — Separação Ontológica Inegociável entre Referência e Passagem:**
   - **Referência Syntopicon (`SyntopiconReference`):** Apontamento remissivo do índice de Mortimer J. Adler (Autor, Obra, Volume GBWW, Página do Syntopicon, Localizador Bruto). **Uma referência diz onde procurar; ela não contém nem autoriza a invenção do texto da obra.**
   - **Passagem (`Passage`):** Excerto textual literal conferido, confrontado com edição comprovada e devidamente traduzido. Zero passagens são criadas de forma automatizada ou presumida.
6. **Princípio de Medição de Subgrafo para Fixtures de Regressão:**
   - As fixtures de regressão não medem o tamanho global das pastas (`06-autores/`, `05-obras/`, etc.), mas sim o **subgrafo de conhecimento alcançado a partir dos tópicos testados**.
   - **Subgrafo Golden Case 8c(1):**
     - Rastreamento a partir de `topic:justica:8c-1`:
     - `18 referências → 17 autores alcançados → 20 obras alcançadas → 16 volumes alcançados → 0 passagens`.
   - **Subgrafo Lote 1 (Tópico 1: 42.1 + 1a a 1f, pp. 859–860):**
     - Rastreamento a partir de `topic:justica:1a` a `topic:justica:1f`:
     - `53 referências → 82 segmentos de obra → 26 autores alcançados → 51 obras alcançadas → 28 volumes alcançados → 0 passagens`.
     - Distribuição por subtópico: `1a`: 18 refs (27 segs); `1b`: 8 refs (12 segs); `1c`: 11 refs (17 segs); `1d`: 8 refs (12 segs); `1e`: 3 refs (7 segs); `1f`: 5 refs (7 segs).
   - O validador falha imediatamente se qualquer subgrafo divergir dessas métricas documentais.

7. **Três Proteções Normativas de Integridade Documental:**
   - **Proteção 1 — Unicidade Documental Composta:** Cada nota de referência deve possuir unicidade estrita garantida pela tupla quádrupla `(source-id, syntopiconPage, topicId, orderInTopic)`. Nenhuma linha impressa pode ser ingerida duas vezes.
   - **Proteção 2 — Primazia Inegociável do `locatorRaw` Verbatim:** O parser pode decompor `locatorRaw → workSegments[] → locators[]`, mas é terminantemente vedado sintetizar ou reconstruir `locatorRaw` a partir de campos normalizados. O texto tipográfico é a autoridade primária; a estrutura é derivada dele.
   - **Proteção 3 — `needs_verification` como Único Status Automático:** O extrator emite saídas em staging estritamente sob `verification: needs_verification`. A promoção para `verification: verified` requer confronto visual linha por linha contra o PDF de 1952.
   - **Regra de Fronteira Documental de Tópicos (Caso Montesquieu):** Uma referência só pode pertencer a um subtópico depois que o cabeçalho documental desse subtópico for explicitamente reconhecido. A contiguidade espacial ou proximidade visual na página nunca autoriza a migração de topicId (evitando a absorção errônea de Montesquieu de 8b para 8c ou 8c-1).

---

## 2. A Tríade Ortogonal de Metadados

Cada registro do ecossistema deve declarar três dimensões independentes de validação:

```yaml
provenance: original-corpus       # De qual artefato o dado se originou?
epistemology: canonical           # Qual é a natureza epistemológica do conteúdo?
verification: verified            # Qual é o grau de conferência humana/textual?
```

### 2.1 Valores Permitidos para `provenance`:
- `original-corpus`: Extraído diretamente do Syntopicon de 1952 ou da coleção *Great Books of the Western World* (GBWW).
- `derived-structure`: Estrutura hierárquica, numeração ou ordenação derivada por processamento automatizado auditado.
- `external-corpus`: Dados provenientes de projetos externos (ex: frequência lexical do NewSyntopicon).
- `contemporary-source`: Obras e fontes produzidas após o encerramento do corpus original de 1952.

### 2.2 Valores Permitidos para `epistemology`:
- `canonical`: Conteúdo autêntico e normativo de Mortimer J. Adler / Syntopicon 1952.
- `source`: Conteúdo original dos autores e obras canônicas da GBWW.
- `editorial`: Explicações, traduções de trabalho, sínteses silogísticas e contextualizações da equipe editorial (demarcadas como `CAMADA EDITORIAL — NÃO CANÔNICA`).
- `contemporary-extension`: Discussões contemporâneas (Rawls, Nozick, Sandel, Sen, etc.) claramente demarcadas para evitar anacronismo.
- `personal`: Reflexões, impressões e anotações pessoais do estudante (estritamente reservado).

### 2.3 Valores Permitidos para `verification`:
- `verified`: Registro confrontado visualmente página por página com a fonte primária documental (`_fontes/Justice.pdf`).
- `needs_verification`: Registro extraído por OCR ou pipeline digital preliminar pendente de conferência visual exaustiva.
- `unverified`: Dado provisório estruturado sem validação de edição.
- `ocr_error`: Erro documental de leitura detectado, preservado com anotação de correção.

---

## 3. Entidades Nucleares do Sistema e Modelagem Relacional

| Entidade | Prefixo do ID | Padrão do Slug | Função Arquitetural |
| :--- | :--- | :--- | :--- |
| **Grande Ideia** | `idea:` | `gi-[numero]-[slug].md` | Nota-mãe de navegação e síntese dialética de uma das 102 ideias. |
| **Tópico** | `topic:` | `topico-[gi]-[codigo].md` | Nó do outline hierárquico (11 ramos + 30 descendentes = 41 nós em Justiça). |
| **Referência** | `ref:` | `ref-[gi]-[topico]-[seq]-[autor].md` | Registro documental de um apontamento remissivo do Syntopicon 1952. |
| **Passagem** | `passage:` | `passagem-[id_estavel].md` | Citação literal verificada na obra correspondente (0 geradas sem conferência). |
| **Autor** | `author:` | `autor-[slug].md` | Agente histórico, pensador ou autoria coletiva. |
| **Obra** | `work:` | `obra-[slug].md` | Identidade intelectual de um texto (independente da edição física). |
| **Volume** | `vol:` | `vol-[num].md` | Volume físico de uma edição determinada da coleção GBWW. |
| **Fonte** | `source:` | `fonte-[slug].md` | Artefato bibliográfico ou arquivo físico/digital de consulta (ex: `Justice.pdf`). |
| **Índice / MOC** | `moc:` | `moc-[slug].md` / `home.md` | Instrumento de navegação transversal e painel central do vault. |

---

## 4. Estrutura Canônica de Diretórios (Português sem Acentos)

```text
vault-syntopicon/
├── 00-sistema/                # Contrato, schemas, registros, mapas, manifesto, scripts e templates canônicos
│   ├── scripts/               # Scripts de auditoria e utilitários de validação
│   ├── templates/             # Modelos padronizados de notas
│   ├── contrato-de-dados.md   # Este contrato normativo congelado
│   ├── schema-entidades.json  # Schemas JSON Draft 2020-12
│   ├── registro-de-fontes.json# Catálogo descritivo de fontes
│   ├── mapa-de-identidades.json# De-para de identificadores e legacyIds
│   └── manifesto-justica.json # Manifesto de auditoria e métricas de Justiça
├── 01-grandes-ideias/         # As 102 notas-mãe das Grandes Ideias (ex: gi-42-justica.md)
├── 02-topicos/                # Nós de tópicos organizados por ideia (ex: 02-topicos/justica/)
├── 03-referencias/            # Entradas documentais de referências do Syntopicon (ex: 03-referencias/justica/)
├── 04-passagens/              # Passagens literais confrontadas e verificadas (0 geradas sem prova textual)
├── 05-obras/                  # Fichas intelectuais das obras citadas
├── 06-autores/                # Fichas dos autores canônicos e comentadores
├── 07-volumes/                # Fichas dos volumes físicos da GBWW
├── 08-indices/                # Painéis centrais, Mapas de Conteúdo (MOCs) e inventários de termos
├── 09-auditorias/             # Relatórios de validação, codex handoff e relatórios de conformidade
└── _fontes/                   # Arquivos brutos, PDFs originais (Justice.pdf) e datasets brutos
```

---

## 5. Regra de Ouro dos Wikilinks

Todo link no Obsidian segue a sintaxe:
`[[slug-tecnico|Nome Exibido em Português]]`
- O alvo técnico é estritamente minúsculo, sem acentos, sem cedilha, sem espaços e separado por hífens (`autor-aristoteles`, `topico-42-8c-1`).
- O texto visível preserva a grafia vernácula em português com acentuação correta.
