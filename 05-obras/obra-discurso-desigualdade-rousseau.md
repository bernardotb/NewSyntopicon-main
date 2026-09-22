---
tipo: obra
id: "work:discourse-on-inequality"
slug: "obra-discurso-desigualdade-rousseau"
canonicalTitle: "Discourse on the Origin and Basis of Inequality Among Men"
displayTitlePtBr: "Discurso sobre a Origem da Desigualdade"
canonical-title: "Discourse on the Origin and Basis of Inequality Among Men"
display-title-ptbr: "Discurso sobre a Origem da Desigualdade"
authorIds: ["author:rousseau"]
author-ids: ["author:rousseau"]
autores:
  - "[[autor-jean-jacques-rousseau|Jean-Jacques Rousseau]]"
originalLanguage: "Francês"
original-language: "Francês"
gbwwVolume: 38
gbww-volume: 38
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Discurso sobre a Origem da Desigualdade"
  - "Discourse on the Origin and Basis of Inequality Among Men"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Discurso sobre a Origem da Desigualdade (*Discourse on the Origin and Basis of Inequality Among Men*)

> **Autoria:** [[autor-jean-jacques-rousseau|Jean-Jacques Rousseau]]  
> **Volume GBWW:** 38 | **Idioma Original:** Francês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Ensaio filosófico seminal sobre o estado de natureza, o surgimento da propriedade e a institucionalização da servidão social.

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
