---
tipo: obra
id: "work:pensees-pascal"
slug: "obra-pensamentos-pascal"
canonicalTitle: "Pensées"
displayTitlePtBr: "Pensamentos"
canonical-title: "Pensées"
display-title-ptbr: "Pensamentos"
authorIds: ["author:pascal"]
author-ids: ["author:pascal"]
autores:
  - "[[autor-blaise-pascal|Blaise Pascal]]"
originalLanguage: "Francês"
original-language: "Francês"
gbwwVolume: 33
gbww-volume: 33
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Pensamentos"
  - "Pensées"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Pensamentos (*Pensées*)

> **Autoria:** [[autor-blaise-pascal|Blaise Pascal]]  
> **Volume GBWW:** 33 | **Idioma Original:** Francês  
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
