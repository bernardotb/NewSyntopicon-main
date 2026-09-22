---
tipo: obra
id: "work:liberty-mill"
slug: "obra-sobre-a-liberdade-mill"
canonicalTitle: "On Liberty"
displayTitlePtBr: "Sobre a Liberdade"
canonical-title: "On Liberty"
display-title-ptbr: "Sobre a Liberdade"
authorIds: ["author:mill"]
author-ids: ["author:mill"]
autores:
  - "[[autor-john-stuart-mill|John Stuart Mill]]"
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
  - "Sobre a Liberdade"
  - "On Liberty"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Sobre a Liberdade (*On Liberty*)

> **Autoria:** [[autor-john-stuart-mill|John Stuart Mill]]  
> **Volume GBWW:** 43 | **Idioma Original:** Inglês  
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
