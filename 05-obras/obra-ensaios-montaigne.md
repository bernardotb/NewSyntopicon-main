---
tipo: obra
id: "work:essays-montaigne"
slug: "obra-ensaios-montaigne"
canonicalTitle: "The Essays of Michel de Montaigne"
displayTitlePtBr: "Ensaios"
canonical-title: "The Essays of Michel de Montaigne"
display-title-ptbr: "Ensaios"
authorIds: ["author:montaigne"]
author-ids: ["author:montaigne"]
autores:
  - "[[autor-michel-de-montaigne|Michel de Montaigne]]"
originalLanguage: "Francês"
original-language: "Francês"
gbwwVolume: 25
gbww-volume: 25
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Ensaios"
  - "The Essays of Michel de Montaigne"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Ensaios (*The Essays of Michel de Montaigne*)

> **Autoria:** [[autor-michel-de-montaigne|Michel de Montaigne]]  
> **Volume GBWW:** 25 | **Idioma Original:** Francês  
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
