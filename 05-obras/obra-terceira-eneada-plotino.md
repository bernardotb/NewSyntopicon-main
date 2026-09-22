---
tipo: obra
id: "work:third-ennead-plotinus"
slug: "obra-terceira-eneada-plotino"
canonicalTitle: "Third Ennead"
displayTitlePtBr: "Terceira Enéada"
canonical-title: "Third Ennead"
display-title-ptbr: "Terceira Enéada"
authorIds: ["author:plotinus"]
author-ids: ["author:plotinus"]
autores:
  - "[[autor-plotino|Plotino]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 17
gbww-volume: 17
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Terceira Enéada"
  - "Third Ennead"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Terceira Enéada (*Third Ennead*)

> **Autoria:** [[autor-plotino|Plotino]]  
> **Volume GBWW:** 17 | **Idioma Original:** Grego Antigo  
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
