---
tipo: obra
id: "work:civilization-and-its-discontents-freud"
slug: "obra-mal-estar-na-civilizacao-freud"
canonicalTitle: "Civilization and Its Discontents"
displayTitlePtBr: "O Mal-Estar na Civilização"
canonical-title: "Civilization and Its Discontents"
display-title-ptbr: "O Mal-Estar na Civilização"
authorIds: ["author:freud"]
author-ids: ["author:freud"]
autores:
  - "[[autor-sigmund-freud|Sigmund Freud]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 54
gbww-volume: 54
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "O Mal-Estar na Civilização"
  - "Civilization and Its Discontents"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# O Mal-Estar na Civilização (*Civilization and Its Discontents*)

> **Autoria:** [[autor-sigmund-freud|Sigmund Freud]]  
> **Volume GBWW:** 54 | **Idioma Original:** Alemão  
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
