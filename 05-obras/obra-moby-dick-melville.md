---
tipo: obra
id: "work:moby-dick-melville"
slug: "obra-moby-dick-melville"
canonicalTitle: "Moby Dick; or, The Whale"
displayTitlePtBr: "Moby Dick"
canonical-title: "Moby Dick; or, The Whale"
display-title-ptbr: "Moby Dick"
authorIds: ["author:melville"]
author-ids: ["author:melville"]
autores:
  - "[[autor-herman-melville|Herman Melville]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 48
gbww-volume: 48
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Moby Dick"
  - "Moby Dick; or, The Whale"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Moby Dick (*Moby Dick; or, The Whale*)

> **Autoria:** [[autor-herman-melville|Herman Melville]]  
> **Volume GBWW:** 48 | **Idioma Original:** Inglês  
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
