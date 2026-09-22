---
tipo: obra
id: "work:us-constitution"
slug: "obra-constituicao-dos-eua"
canonicalTitle: "Constitution of the United States"
displayTitlePtBr: "Constituição dos Estados Unidos da América"
canonical-title: "Constitution of the United States"
display-title-ptbr: "Constituição dos Estados Unidos da América"
authorIds: ["author:founding-fathers-us"]
author-ids: ["author:founding-fathers-us"]
autores:
  - "[[autor-constituicao-eua|Constituição dos EUA]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 43
gbww-volume: 43
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Constituição dos Estados Unidos da América"
  - "Constitution of the United States"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Constituição dos Estados Unidos da América (*Constitution of the United States*)

> **Autoria:** [[autor-constituicao-eua|Constituição dos EUA]]  
> **Volume GBWW:** 43 | **Idioma Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Documento jurídico fundamental que estabeleceu a república federativa norte-americana e seus artigos sobre a mão de obra servil e abolição.

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
