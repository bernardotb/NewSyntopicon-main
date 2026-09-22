---
tipo: obra
id: "work:paradise-lost-milton"
slug: "obra-paraiso-perdido-milton"
canonicalTitle: "Paradise Lost"
displayTitlePtBr: "Paraíso Perdido"
canonical-title: "Paradise Lost"
display-title-ptbr: "Paraíso Perdido"
authorIds: ["author:milton"]
author-ids: ["author:milton"]
autores:
  - "[[autor-john-milton|John Milton]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 32
gbww-volume: 32
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Paraíso Perdido"
  - "Paradise Lost"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Paraíso Perdido (*Paradise Lost*)

> **Autoria:** [[autor-john-milton|John Milton]]  
> **Volume GBWW:** 32 | **Idioma Original:** Inglês  
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
