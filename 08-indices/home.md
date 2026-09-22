---
tipo: dashboard
aliases:
  - Home
  - Início
  - Painel Central
tags:
  - type/home
  - type/dashboard
layer: editorial
provenance: derived-structure
epistemology: editorial
verification: verified
created: 2026-09-16
modified: 2026-09-17
---

# 🏛️ Syntopicon Vault: The Great Conversation

> *"A leitura sintópica não é um exercício mecânico de busca de termos, mas a arte de conduzir os maiores pensadores da história a um diálogo comum sobre as questões perenes da humanidade."*  
> — **Mortimer J. Adler**

---

## 🧭 Arquitetura Epistemológica do Vault

O cofre opera com separação estrita em camadas ontológicas e a tríade de validação (`provenance`, `epistemology`, `verification`):
- 🟢 **`canonical`:** Outline de tópicos, ensaios e taxonomia normativa de Mortimer J. Adler / *Syntopicon* (1952).
- 🔵 **`source`:** Obras e passagens catalogadas no corpus primário da coleção *Great Books of the Western World* (GBWW).
- 🟠 **`editorial`:** Reconstruções silogísticas, conexões conceituais e sínteses dialéticas (sempre demarcadas como `CAMADA EDITORIAL — NÃO CANÔNICA`).
- 🟣 **`contemporary-extension`:** Extensão contemporânea (Rawls, Nozick, Sandel, novos dilemas éticos).
- 🧠 **`personal`:** Anotações atômicas e síntese do estudante.

---

## 🗂️ Estrutura Semântica Canônica de Diretórios (Português sem Acentos)

| Diretório | Função Primária | Padrão de Nomenclatura |
| :--- | :--- | :--- |
| **`00-sistema/`** | Contratos, schemas JSON, registros de fontes, mapas e templates | `schema-entidades.json`, `contrato-de-dados.md` |
| **`01-grandes-ideias/`** | As 102 notas-mãe das Grandes Ideias | `gi-[numero]-[slug].md` |
| **`02-topicos/`** | Nós atômicos do Outline de tópicos (por ideia) | `topico-[gi]-[id].md` |
| **`03-referencias/`** | Entradas documentais de referências do Syntopicon | `ref-[gi]-[topico]-[ordem]-[autor].md` |
| **`04-passagens/`** | Passagens literais verificadas e traduzidas | `passagem-[id].md` |
| **`05-obras/`** | Fichas intelectuais das obras canônicas | `obra-[slug].md` |
| **`06-autores/`** | Fichas dos pensadores (GBWW e comentadores) | `autor-[slug].md` |
| **`07-volumes/`** | Fichas dos volumes físicos da coleção GBWW | `vol-[num].md` |
| **`08-indices/`** | Painéis de controle, índices e Mapas de Conteúdo (MOCs) | `home.md`, `moc-[slug].md` |
| **`09-auditorias/`** | Relatórios de conformidade e auditoria estrutural | `arena-handoff-codex.md`, `validation-report.json` |
| **`_fontes/`** | Arquivos brutos, PDFs originais e datasets | `Justice.pdf` |

---

## 🌟 Golden Idea de Referência (Benchmark)
- **[[gi-42-justica|GI-42: Justiça (Justice)]]** — A especificação oficial completa e auditada:
  - 11 ramos principais e 30 descendentes (**41 nós de tópicos gerados em `02-topicos/justica/`**).
  - 826 registros da ingestão estruturada do corpus de 1952 (classificados como `needs_verification` até auditoria página a página).
  - Golden Case 8c(1) reconciliado documentalmente: 18 entradas impressas no Syntopicon 1952 (p. 868), 17 entidades autorais, 20 obras distintas.

---

## 📊 Navegação Rápida por MOCs e Índices
- [[moc-102-ideias|MOC: As 102 Grandes Ideias]]
- [[gi-42-justica|Grande Ideia 42: Justiça]]
- [[topico-42-8c-1|Golden Case: Tópico 42.8c(1)]]
