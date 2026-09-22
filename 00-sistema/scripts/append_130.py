import os

section_1_30 = """

---

## 1.30 Reconciliação e Auditoria Física Estrita do Tópico 42.8c(2) (*Profit and unearned increment*)

### 📅 Data da Auditoria: 2026-09-22
**Artefato Primário Auditado:** `_fontes/Justice.pdf` (GBWW Vol. 2, pág. 868, coluna 2, linhas 91–101).  
**Status da Auditoria:** `verification: verified` | `epistemology: canonical` | `provenance: original-corpus`  
**Escopo do Nó:** `topic:justica:8c-2` (*Profit and unearned increment* / *Lucro e incremento não auferido*), nó folha de nível 3 subordinado ao nó pai [[topico-42-8c|42.8c]].

---

### 🔍 I. Delimitação Física Documental e Resolução Filológica
1. **Fronteira Superior:** `8c(2) Profit and unearned increment` na pág. 868, coluna direita, linha 91 (imediatamente após a citação final de Dostoievski em 8c(1)).
2. **Fronteira Inferior (Exclusiva):** `8d. Justice and the use ofmoney: usury and in-` na pág. 868, coluna direita, linha 102.
3. **Censo Físico Soberano (DIRECT_NODE_ONLY):** O espaço tipográfico estrito contém exatamente **4 blocos físicos de citação**:
   - **Entrada 1:** `14 PLUTARCH: Marcus Cato, 287c-d` (`author:plutarch`, `work:marcus-cato-plutarch`, GBWW Vol. 14, 1 workSegment).
   - **Entrada 2:** `39 SMITH: Wealth of Nations, BK i, 20b-23b passim, esp 21a-c; 27b-28a; 109d-110d` (`author:smith`, `work:wealth-of-nations`, GBWW Vol. 39, 1 workSegment). Resolvida a quebra de linha do OCR (`pas- sim`).
   - **Entrada 3:** `46 HEGEL: Philosophy of Right, PART iii, par 243, 77b-c` (`author:hegel`, `work:philosophy-of-right-hegel`, GBWW Vol. 46, 1 workSegment). Retificado erro de OCR `PART in` para numeral romano `PART iii`.
   - **Entrada 4:** `50 MARX: Capital, 71d-72c; 85a-263d esp 92c-94a, 100a-101b, 104b-105c, 112c, 154d-156d, 198c-199b, 254c-255a, 263c-d; 267b; 267d-275c passim, esp 271b-c; 286a-301b passim, esp 288b-289c, 295a-d, 301a-b, 327b` (`author:marx`, `work:capital-marx`, GBWW Vol. 50, 1 workSegment). Corrigido OCR `lOOa-lOlb` para `100a-101b` e restaurada a ordem verbatim do título `Capital` no início do localizador.
4. **Paridade com Staging:** O staging congelado em V8 já previa 4 referências e 4 workSegments. O confronto físico resultou em:
   - `referenceDelta = 0` (4 staging -> 4 físico);
   - `workSegmentDelta = 0` (4 staging -> 4 físico);
   - `candidatesMisassignedFrom8c = 0`;
   - `duplicatesMaterialized = 0`.

---

### ⚖️ II. Manutenção do Baseline V8 (`STAGING_BASELINE_JUSTICE_1952_V8`)
Como não houve alteração no censo físico global de referências nem de workSegments (`referenceDelta == 0` e `workSegmentDelta == 0`), o **`STAGING_BASELINE_JUSTICE_1952_V8`** permanece plenamente ativo e normativo:
- **Total Físico Canônico:** 814 referências físicas;
- **Total de WorkSegments:** 1.350 segmentos;
- **Status:** Ativo e soberano.

---

### 🏛️ III. Materialização Canônica (`03-referencias/justica/`)
Foram materializadas com 100% de conformidade ao schema `SyntopiconReference`:
1. `ref-42-8c-2-01-plutarco.md` (`ref:justica:8c-2:01-plutarch`, Plutarco, *Marco Catão*, Vol. 14, p. 868)
2. `ref-42-8c-2-02-adam-smith.md` (`ref:justica:8c-2:02-smith`, Adam Smith, *A Riqueza das Nações*, Vol. 39, p. 868)
3. `ref-42-8c-2-03-gwf-hegel.md` (`ref:justica:8c-2:03-hegel`, G. W. F. Hegel, *Filosofia do Direito*, Vol. 46, p. 868)
4. `ref-42-8c-2-04-karl-marx.md` (`ref:justica:8c-2:04-karl-marx`, Karl Marx, *O Capital*, Vol. 50, p. 868)
A Seção IV de `topico-42-8c-2.md` foi atualizada com a tabela documental correspondente.

---

### 🛡️ IV. Validação Sistêmica e Décima Oitava Fixture de Regressão
Implementada a **Fixture Permanente 18** (`fixtureRegressaoTopico42_8c_2`, escopo `DIRECT_NODE_ONLY`) em `00-sistema/scripts/validate_vault.py`:
- **4 referências** auditadas e materializadas;
- **4 segmentos de obra** verificados;
- **4 autores canônicos** (Plutarco, Adam Smith, G. W. F. Hegel, Karl Marx);
- **4 obras canônicas** (*Marco Catão*, *A Riqueza das Nações*, *Filosofia do Direito*, *O Capital*);
- **4 volumes numerados da GBWW** (Vols. 14, 39, 46, 50);
- **0 fontes documentais não-numeradas**;
- **0 passagens literais** transcritas (`Referência != Passagem` incondicionalmente preservada).

**Resultado Geral da Suíte de Testes:**
- 18 Fixtures de Regressão: **100% PASS**;
- 4 Invariantes Arquiteturais: **100% PASS**;
- 5 Proteções de Integridade Documental: **100% PASS** (423 chaves compostas únicas, 0 dangling IDs em 379 identidades canônicas, 0 wikilinks quebrados);
- Golden Case 8c(1): **100% PASS** (inalterado).

---

### 📊 V. Tabela Acumulada de Progresso do Cofre (Pós-42.8c(2))

| Métrica | Estado Anterior (42.8c) | Delta 42.8c(2) | Estado Atual (42.8c(2)) |
| :--- | :---: | :---: | :---: |
| **Baseline Ativo** | V8 (814 refs / 1.350 segs) | `0 ref / 0 segs` | **V8 (814 refs / 1.350 segs)** |
| **Referências Físicas Verificadas** | 419 | +4 | **423** (51,97% do corpus) |
| **WorkSegments Verificados** | 673 | +4 | **677** (50,15% do corpus) |
| **Referências Pendentes em Staging** | 395 | -4 | **391** |
| **Obras Canônicas no Vault** | 185 | 0 | **185** |
| **Autores e Fontes Canônicas** | 54 | 0 | **54** |
| **Volumes GBWW no Vault** | 43 | 0 | **43** |
| **Passagens Literais** | 0 | 0 | **0** |
| **Fixtures de Regressão Permanentes** | 17 | +1 | **18** |
| **Total de Entidades Primárias** | 743 | +4 | **747** |
| **Total de Entidades com Índices** | 745 | +4 | **749** |
"""

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
codex_path = os.path.join(base_dir, '09-auditorias', 'arena-handoff-codex.md')

with open(codex_path, 'a', encoding='utf-8') as f:
    f.write(section_1_30)

print("Successfully appended Section 1.30 to arena-handoff-codex.md")
