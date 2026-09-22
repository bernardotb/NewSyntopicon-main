---
tipo: obra
id: "work:communist-manifesto"
slug: "obra-manifesto-comunista-marx-engels"
canonicalTitle: "Manifesto of the Communist Party"
displayTitlePtBr: "Manifesto do Partido Comunista"
canonical-title: "Manifesto of the Communist Party"
display-title-ptbr: "Manifesto do Partido Comunista"
authorIds: ["author:marx-engels"]
author-ids: ["author:marx-engels"]
autores:
  - "[[autor-marx-engels|Karl Marx & Friedrich Engels]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 50
gbww-volume: 50
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Manifesto do Partido Comunista"
  - "Manifesto of the Communist Party"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Manifesto do Partido Comunista (*Manifesto of the Communist Party*)

> **Autoria:** [[autor-marx-engels|Karl Marx & Friedrich Engels]]  
> **Volume GBWW:** 50 | **Idioma Original:** Alemão  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Panfleto político e filosófico que proclamou a história de todas as sociedades como a história das lutas de classes entre exploradores e explorados.

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
