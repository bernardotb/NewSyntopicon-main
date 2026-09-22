---
tipo: obra
id: "work:bible-psalms"
slug: "obra-salmos-antigo-testamento"
canonicalTitle: "Psalms"
displayTitlePtBr: "Salmos"
canonical-title: "Psalms"
display-title-ptbr: "Salmos"
authorIds: ["author:bible-old-testament"]
author-ids: ["author:bible-old-testament"]
autores:
  - "[[autor-antigo-testamento|Antigo Testamento]]"
originalLanguage: "Hebraico"
original-language: "Hebraico"
gbwwVolume: null
gbww-volume: null
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Salmos"
  - "Psalms"
status: ativo
created: 2026-09-22
modified: 2026-09-22
---

# Salmos (*Psalms*)

> **Autoria:** [[autor-antigo-testamento|Antigo Testamento]]  
> **Volume GBWW:** Corpus Bíblico | **Idioma Original:** Hebraico  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Livro poético e litúrgico do Antigo Testamento contendo hinos, súplicas e meditações sapienciais sobre a retidão divina e as obrigações morais da comunidade.

---

## 🏛️ II. GRANDES IDEIAS DISCUTIDAS NA OBRA

```dataview
TABLE 
  topico as "Tópico Específico",
  locator-raw as "Localizador (Locator Raw)",
  syntopicon-pagina as "Pág. Syntopicon"
FROM "03-referencias/justica"
WHERE obra-id = this.id OR contains(workIds, this.id)
SORT topico ASC
LIMIT 30
```

---

## 📜 III. PASSAGENS LITERAIS VERIFICADAS

```dataview
TABLE 
  locator-exato as "Localizador",
  traducao as "Excerto em Português",
  verification as "Status"
FROM "04-passagens"
WHERE obra-id = this.id OR obra = this.file.link
SORT locator-exato ASC
```
