---
tipo: obra
id: "work:war-and-peace"
slug: "obra-guerra-e-paz-tolstoi"
canonicalTitle: "War and Peace"
displayTitlePtBr: "Guerra e Paz"
canonical-title: "War and Peace"
display-title-ptbr: "Guerra e Paz"
authorIds: ["author:tolstoy"]
author-ids: ["author:tolstoy"]
autores:
  - "[[autor-liev-tolstoi|Liev Tolstói]]"
originalLanguage: "Russo"
original-language: "Russo"
gbwwVolume: 51
gbww-volume: 51
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Guerra e Paz"
  - "War and Peace"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Guerra e Paz (*War and Peace*)

> **Autoria:** [[autor-liev-tolstoi|Liev Tolstói]]  
> **Volume GBWW:** 51 | **Idioma Original:** Russo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Epopeia histórica sobre as guerras napoleônicas na Rússia, expondo as tensões humanas entre a nobreza proprietária e os servos camponeses.

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
