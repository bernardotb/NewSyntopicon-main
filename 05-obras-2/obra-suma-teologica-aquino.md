---
tipo: obra
id: "work:summa-theologica"
slug: "obra-suma-teologica-aquino"
canonicalTitle: "Summa Theologica"
displayTitlePtBr: "Suma Teológica"
canonical-title: "Summa Theologica"
display-title-ptbr: "Suma Teológica"
authorIds: ["author:aquinas"]
author-ids: ["author:aquinas"]
autores:
  - "[[autor-tomas-de-aquino|Tomás de Aquino]]"
originalLanguage: "Latim"
original-language: "Latim"
gbwwVolume: 20
gbww-volume: 20
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Suma Teológica"
  - "Summa Theologica"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Suma Teológica (*Summa Theologica*)

> **Autoria:** [[autor-tomas-de-aquino|Tomás de Aquino]]  
> **Volume GBWW:** 20 | **Idioma Original:** Latim  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra magna do pensamento escolástico, examinando na Segunda Parte a justiça, o direito, a propriedade e a servidão humana.

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
