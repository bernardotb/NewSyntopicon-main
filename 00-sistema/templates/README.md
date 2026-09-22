# Guia dos Templates do Ecossistema Syntopicon

> **Aviso de Transição Arquitetural (Fase 2):**  
> Este repositório está adotando o **Contrato de Dados da Fase 2**, localizado em `00-sistema/contrato-de-dados.md`. Os templates oficiais e canônicos para materialização de notas encontram-se exclusivamente em `00-sistema/templates/`.

---

## 1. Templates Canônicos Oficiais (Fase 2)

Localizados na pasta `00-sistema/templates/`:

| Template | Função | Entidade / Schema Correspondente |
| :--- | :--- | :--- |
| **`template-grande-ideia.md`** | Nota-mãe de uma das 102 Grandes Ideias | `idea:` (ex: `gi-42-justica.md`) |
| **`template-topico.md`** | Nó do Outline de tópicos | `topic:` (ex: `topico-42-8c-1.md`) |
| **`template-referencia.md`** | Entrada remissiva do índice de Adler (*não contém o texto*) | `ref:` (ex: `ref-42-001.md`) |
| **`template-passagem.md`** | Excerto textual verificado e confrontado na obra | `passage:` (ex: `passagem-001.md`) |
| **`template-autor.md`** | Ficha bio-bibliográfica do pensador | `author:` (ex: `autor-platao.md`) |
| **`template-obra.md`** | Ficha intelectual da obra canônica | `work:` (ex: `obra-republica-platao.md`) |
| **`template-volume.md`** | Ficha do volume físico da coleção GBWW | `volume:` (ex: `volume-gbww-1952-02.md`) |

---

## 2. A Distinção Vital: Referência Syntopicon ≠ Passagem / Citação

Um dos erros corrigidos na auditoria da Fase 2 foi a confusão entre o apontamento do índice e o texto do livro:
1. **`template-referencia.md`:** Modela o ponteiro bibliográfico de Mortimer J. Adler (Autor, Obra, Volume GBWW, Página do Syntopicon e *Locator Raw*). Uma referência **não finge ter o texto da obra**.
2. **`template-passagem.md`:** Modela a evidência textual concreta. Só é criada quando o trecho do livro foi efetivamente localizado, conferido e traduzido. Uma referência pode ter zero, uma ou mais passagens associadas.

---

## 3. Depreciação dos Templates Legados

Os modelos anteriores (sem extensão ou contendo prefixos como `*tipo:`, listas colapsadas em linha única e caminhos obsoletos como `05-Topicos` e `06-Citacoes`) estão formalmente **depreciados**:
- Não devem ser utilizados para novas notas;
- O resolvedor de metadados agora exige a tríade de validação:
  ```yaml
  provenance: original-corpus
  epistemology: canonical
  verification: verified
  ```
- Todas as consultas Dataview foram migradas para a hierarquia semântica oficial (`02-topicos/`, `03-referencias/`, `04-passagens/`, `05-obras/`, `06-autores/`).

---

## 4. Regra de Ouro dos Wikilinks

Todo link no cofre deve seguir a sintaxe:
`[[slug-tecnico|Nome Exibido]]`
- Alvo técnico: minúsculo, sem acentos, sem pontuação, separado por hífens (`autor-tomas-de-aquino`, `gi-42-justica`).
- Texto visível: grafia elegante em português com acentuação correta.
