---
tipo: obra
id: "work:leviathan-hobbes"
slug: "obra-leviata-hobbes"
canonicalTitle: "Leviathan"
displayTitlePtBr: "Leviatã"
canonical-title: "Leviathan"
display-title-ptbr: "Leviatã"
authorIds: ["author:hobbes"]
author-ids: ["author:hobbes"]
autores:
  - "[[autor-thomas-hobbes|Thomas Hobbes]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 23
gbww-volume: 23
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Leviatã"
  - "Leviathan"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Leviatã (*Leviathan*)

> **Autoria:** [[autor-thomas-hobbes|Thomas Hobbes]]  
> **Volume GBWW:** 23 | **Idioma Original:** Inglês  
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
