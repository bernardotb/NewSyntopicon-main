---
tipo: obra
id: "work:intro-metaphysic-of-morals-kant"
slug: "obra-introducao-metafisica-costumes-kant"
canonicalTitle: "Introduction to the Metaphysic of Morals"
displayTitlePtBr: "Introdução à Metafísica dos Costumes"
canonical-title: "Introduction to the Metaphysic of Morals"
display-title-ptbr: "Introdução à Metafísica dos Costumes"
authorIds: ["author:kant"]
author-ids: ["author:kant"]
autores:
  - "[[autor-immanuel-kant|Immanuel Kant]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 42
gbww-volume: 42
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Introdução à Metafísica dos Costumes"
  - "Introduction to the Metaphysic of Morals"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Introdução à Metafísica dos Costumes (*Introduction to the Metaphysic of Morals*)

> **Autoria:** [[autor-immanuel-kant|Immanuel Kant]]  
> **Volume GBWW:** 42 | **Idioma Original:** Alemão  
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
