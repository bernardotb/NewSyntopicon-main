---
tipo: obra
id: "work:gullivers-travels"
slug: "obra-viagens-de-gulliver-swift"
canonicalTitle: "Gulliver's Travels"
displayTitlePtBr: "As Viagens de Gulliver"
canonical-title: "Gulliver's Travels"
display-title-ptbr: "As Viagens de Gulliver"
authorIds: ["author:swift"]
author-ids: ["author:swift"]
autores:
  - "[[autor-jonathan-swift|Jonathan Swift]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 36
gbww-volume: 36
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "As Viagens de Gulliver"
  - "Gulliver's Travels"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# As Viagens de Gulliver (*Gulliver's Travels*)

> **Autoria:** [[autor-jonathan-swift|Jonathan Swift]]  
> **Volume GBWW:** 36 | **Idioma Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra-prima satírica retratando viagens fabulosas para expor a cupidez, a exploração social e as fraquezas da natureza humana.

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
