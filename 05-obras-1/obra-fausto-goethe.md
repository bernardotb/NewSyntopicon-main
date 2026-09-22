---
tipo: obra
id: "work:faust-goethe"
slug: "obra-fausto-goethe"
canonicalTitle: "Faust"
displayTitlePtBr: "Fausto"
canonical-title: "Faust"
display-title-ptbr: "Fausto"
authorIds: ["author:goethe"]
author-ids: ["author:goethe"]
autores:
  - "[[autor-johann-wolfgang-von-goethe|Johann Wolfgang von Goethe]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 47
gbww-volume: 47
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Fausto"
  - "Faust"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Fausto (*Faust*)

> **Autoria:** [[autor-johann-wolfgang-von-goethe|Johann Wolfgang von Goethe]]  
> **Volume GBWW:** 47 | **Idioma Original:** Alemão  
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
