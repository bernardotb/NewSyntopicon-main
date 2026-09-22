import os

section_1_31 = """

---

## 1.31 Reconciliação e Auditoria Física Estrita do Tópico 42.8d (*Justice and the use of money: usury and interest rates*) e Fechamento do Subtree 42.8

### 📅 Data da Auditoria: 2026-09-22
**Artefato Primário Auditado:** `_fontes/Justice.pdf` (GBWW Vol. 2, pág. 868, col. 2, linha 102 a pág. 869, col. 1, linha 15).  
**Status da Auditoria:** `verification: verified` | `epistemology: canonical` | `provenance: original-corpus`  
**Escopo do Nó:** `topic:justica:8d` (*Justice and the use of money: usury and interest rates* / *A justiça e o uso do dinheiro: usura e taxas de juros*), nó folha de nível 2 subordinado ao nó pai [[topico-42-8|42.8]].

---

### 🔍 I. Delimitação Física Documental e Resolução Filológica
1. **Fronteira Superior:** `8d. Justice and the use ofmoney: usury and in- / terest rates` na pág. 868, coluna direita, linhas 102–103 (imediatamente após a citação final de Marx em 8c(2)).
2. **Fronteira Inferior (Exclusiva):** `9. Political justice: justice in government` na pág. 869, coluna esquerda, linha 16. O censo foi estritamente interrompido antes do início do ramo 9.
3. **Censo Físico Soberano (DIRECT_NODE_ONLY):** O espaço tipográfico contém exatamente **18 blocos físicos de citação**:
   - **Entrada 1:** `OLD TESTAMENT: Exodus, 22:25 / Leviticus, 25:35-37 / Deuteronomy, 23:19-20; 24:10-13 / Nehemiah, 5 (D) II Esdras, 5 / Psalms, 15:5 (D) Psalms, 14:5 / Proverbs, 28:8 / Jeremiah, 15:10 (D) Jeremias, 15:10 / Ezekiel, 18:4-21 esp 18:8, 18:13, 18:17, 22:12 (D) Ezechiel, 18:4-21 esp 18:8, 18:13, 18:17; 22:12` (`author:bible-old-testament`, 8 workSegments correspondentes a 8 livros bíblicos veterotestamentários distintos).
   - **Entrada 2:** `7 PLATO: Republic, BK viii, 408c-d / Laws, BK v, 694c-d; BK xi, 775c-d` (`author:plato`, GBWW Vol. 7, 2 workSegments: *República* e *Leis*).
   - **Entrada 3:** `9 ARISTOTLE: Ethics, BK v, CH 2 [1130b13-b8] 377c-378a; CH 5 [1133a5-b29] 380d-381c; BK ix, CH 2 [1164b10-1165a11] 417d-418a / Politics, BK i, CH 9-10 450d-452d esp CH 10 [1258b8] 452d / Athenian Constitution, CH 12, par 4 557d-558a` (`author:aristotle`, GBWW Vol. 9, 3 workSegments: *Ética a Nicômaco*, *Política* e *Constituição de Atenas*).
   - **Entrada 4:** `14 PLUTARCH: Marcus Cato, 287c-d / Lucullus, 409b-d` (`author:plutarch`, GBWW Vol. 14, 2 workSegments: *Marco Catão* e *Lúculo*).
   - **Entrada 5:** `15 TACITUS: Annals, BK vi, 90a-c` (`author:tacitus`, GBWW Vol. 15, 1 workSegment). Retificado erro de OCR que listava Vol. 6.
   - **Entrada 6:** `20 AQUINAS: Summa Theologica, PART I-II, Q 105, A 2, REP 4 309d-316a` (`author:aquinas`, GBWW Vol. 20, 1 workSegment). Retificado erro de OCR `PART MI` para `PART I-II`.
   - **Entrada 7:** `21 DANTE: Divine Comedy, HELL, xi [91-111] 16a-b; xvii [31-75] 24a-c` (`author:dante`, GBWW Vol. 21, 1 workSegment).
   - **Entrada 8:** `24 RABELAIS: Gargantua and Pantagruel, BK iii, 133b-140b` (`author:rabelais`, GBWW Vol. 24, 1 workSegment).
   - **Entrada 9:** `26 SHAKESPEARE: Merchant of Venice, ACT i, sc iii 409c-411b` (`author:shakespeare`, GBWW Vol. 26, 1 workSegment).
   - **Entrada 10:** `33 PASCAL: Provincial Letters, 55a-57a` (`author:pascal`, GBWW Vol. 33, 1 workSegment). Retificado OCR `55a*57a`.
   - **Entrada 11:** `38 MONTESQUIEU: Spirit of Laws, BK v, 29c; BK xii, 92d-93c; BK xxi, 169a-170b; BK xxii, 175d-176a; 184b-187a,c` (`author:montesquieu`, GBWW Vol. 38, 1 workSegment).
   - **Entrada 12:** `39 SMITH: Wealth of Nations, BK i, 37b-41d; BK ii, 140b; 154c-155a` (`author:smith`, GBWW Vol. 39, 1 workSegment).
   - **Entrada 13:** `40 GIBBON: Decline and Fall, 498c` (`author:gibbon`, GBWW Vol. 40, 1 workSegment).
   - **Entrada 14:** `41 GIBBON: Decline and Fall, 90d-91a` (`author:gibbon`, GBWW Vol. 41, 1 workSegment).
   - **Entrada 15:** `42 KANT: Science of Right, 424a-425b` (`author:kant`, GBWW Vol. 42, 1 workSegment).
   - **Entrada 16:** `44 BOSWELL: Johnson, 304b-c, 409a-b` (`author:boswell`, GBWW Vol. 44, 1 workSegment).
   - **Entrada 17:** `46 HEGEL: Philosophy of History, PART iv, 353b-c` (`author:hegel`, GBWW Vol. 46, 1 workSegment).
   - **Entrada 18:** `50 MARX: Capital, 77c-78b; 252b; 293a-d [fn 1]; 371c-372c` (`author:marx`, GBWW Vol. 50, 1 workSegment). Restaurada a ordem verbatim do título `Capital` no início do localizador.
4. **Resolução de Anomalia de Segmentação e Criação do Baseline V9:** O staging preliminar colapsara os livros de *Provérbios* e *Jeremias* em um único segmento por corrupção de OCR (`28:87 Jeremiah`). A recuperação do segmento independente de *Jeremias* elevou o censo de workSegments de 42.8d de 28 para 29 (`workSegmentDelta = +1`), acionando a promoção compulsória para o **`STAGING_BASELINE_JUSTICE_1952_V9`** (814 refs / 1.351 workSegments).

---

### ⚖️ II. Promoção Canônica para o Baseline V9 (`STAGING_BASELINE_JUSTICE_1952_V9`)
- **Total Físico Canônico:** 814 referências físicas (`referenceDelta = 0`);
- **Total de WorkSegments:** 1.351 segmentos (`workSegmentDelta = +1`);
- **Causa-raiz:** Separação documental de *Provérbios* e *Jeremias* em `ref:justica:8d:01-antigo-testamento`;
- **Status:** Ativo e soberano.

---

### 🏛️ III. Materialização Canônica de Obras e Referências
1. **Obras Novas Criadas em `05-obras/`:**
   - `obra-salmos-antigo-testamento.md` (`work:bible-psalms`, Salmos);
   - `obra-luculo-plutarco.md` (`work:lucullus-plutarch`, Lúculo, GBWW Vol. 14).
2. **Referências Canônicas Materializadas em `03-referencias/justica/`:**
   - 18 notas canônicas geradas (`ref-42-8d-01-antigo-testamento.md` até `ref-42-8d-18-karl-marx.md`), cobrindo 29 workSegments e 17 volumes da GBWW.
3. **Atualização do Tópico 42.8d:**
   - Seção IV de `topico-42-8d.md` integralmente populada com a tabela das 18 referências auditadas.

---

### 🛡️ IV. Validação Sistêmica e Décima Nona Fixture de Regressão
Implementada a **Fixture Permanente 19** (`fixtureRegressaoTopico42_8d`, escopo `DIRECT_NODE_ONLY`) em `00-sistema/scripts/validate_vault.py`:
- **18 referências** auditadas e materializadas;
- **29 segmentos de obra** verificados;
- **17 autores/fontes canônicos**;
- **28 obras canônicas distintas**;
- **17 volumes numerados da GBWW**;
- **1 fonte não-numerada** (`author:bible-old-testament`);
- **0 passagens literais** transcritas (`Referência != Passagem` incondicionalmente preservada).

**Resultado Geral da Suíte de Testes:**
- 19 Fixtures de Regressão: **100% PASS**;
- 4 Invariantes Arquiteturais: **100% PASS**;
- 5 Proteções de Integridade Documental: **100% PASS** (441 chaves compostas únicas, 0 dangling IDs em 381 identidades canônicas, 0 wikilinks quebrados);
- Golden Case 8c(1): **100% PASS** (inalterado em 18 refs / 21 segments).

---

### 🌳 V. Fechamento Consolidado do Subtree 42.8 (A Ordem Econômica)

Com a auditoria de 42.8d, todos os nós do ramo 8 estão plenamente verificados:

```text
42.8 (A ordem econômica: 38 refs / 71 segs)
├── 42.8a (Propriedade privada: 34 refs / 61 segs)
├── 42.8b (Salários e preços justos: 26 refs / 43 segs)
├── 42.8c (Organização da produção: 2 refs / 2 segs)
│   ├── 42.8c(1) (Exploração econômica [Golden Case]: 18 refs / 21 segs)
│   └── 42.8c(2) (Lucro e incremento não auferido: 4 refs / 4 segs)
└── 42.8d (Usura e taxas de juros: 18 refs / 29 segs)
```

**Métricas Agregadas do Subtree 8:**
- **Total de Referências Físicas Diretas:** 140 referências;
- **Total de WorkSegments Diretos:** 231 segmentos;
- **Autores Distintos no Subtree 8:** 43 autores/fontes;
- **Obras Distintas no Subtree 8:** 88 obras;
- **Volumes GBWW Alcançados:** 37 volumes;
- **Duplicação de Referências:** 0 duplicatas (`duplicateReferenceIds = 0`, `duplicatePhysicalOwnership = 0`);
- **Isolamento de 8c(1):** `golden8c1DuplicatedInto8c = False`.

**Status Oficial:** `SUBTREE_42_8_STATUS = FULLY_VERIFIED`.

---

### 📊 VI. Tabela Acumulada de Progresso do Cofre (Pós-42.8d)

| Métrica | Estado Anterior (42.8c-2) | Delta 42.8d | Estado Atual (42.8d) |
| :--- | :---: | :---: | :---: |
| **Baseline Ativo** | V8 (814 refs / 1.350 segs) | `0 ref / +1 seg` | **V9 (814 refs / 1.351 segs)** |
| **Referências Físicas Verificadas** | 423 | +18 | **441** (54,18% do corpus) |
| **WorkSegments Verificados** | 677 | +29 | **706** (52,26% do corpus) |
| **Referências Pendentes em Staging** | 391 | -18 | **373** |
| **WorkSegments Pendentes em Staging** | 673 | -28 | **645** |
| **Obras Canônicas no Vault** | 185 | +2 | **187** |
| **Autores e Fontes Canônicas** | 54 | 0 | **54** |
| **Volumes GBWW no Vault** | 43 | 0 | **43** |
| **Passagens Literais** | 0 | 0 | **0** |
| **Fixtures de Regressão Permanentes** | 18 | +1 | **19** |
| **Total de Entidades Primárias** | 747 | +20 | **767** |
| **Total de Entidades com Índices** | 749 | +20 | **769** |
"""

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
codex_path = os.path.join(base_dir, '09-auditorias', 'arena-handoff-codex.md')

with open(codex_path, 'a', encoding='utf-8') as f:
    f.write(section_1_31)

print("Successfully appended Section 1.31 to arena-handoff-codex.md")
