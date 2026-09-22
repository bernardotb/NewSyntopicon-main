---
tipo: obra
id: "work:statesman-plato"
slug: "obra-politico-platao"
canonicalTitle: "Statesman"
displayTitlePtBr: "O Político"
canonical-title: "Statesman"
display-title-ptbr: "O Político"
authorIds: ["author:plato"]
author-ids: ["author:plato"]
autores:
  - "[[autor-platao|Platão]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 7
gbww-volume: 7
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "O Político"
  - "Statesman"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# O Político (*Statesman*)

> **Autoria:** [[autor-platao|Platão]]  
> **Volume GBWW:** 7 | **Idioma Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (GBWW 1952), indexada tematicamente no *Syntopicon*.

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
