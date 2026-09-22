---
tipo: obra
id: "work:peloponnesian-war-thucydides"
slug: "obra-guerra-do-peloponeso-tucidides"
canonicalTitle: "The History of the Peloponnesian War"
displayTitlePtBr: "História da Guerra do Peloponeso"
canonical-title: "The History of the Peloponnesian War"
display-title-ptbr: "História da Guerra do Peloponeso"
authorIds: ["author:thucydides"]
author-ids: ["author:thucydides"]
autores:
  - "[[autor-tucidides|Tucídides]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 6
gbww-volume: 6
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "História da Guerra do Peloponeso"
  - "The History of the Peloponnesian War"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# História da Guerra do Peloponeso (*The History of the Peloponnesian War*)

> **Autoria:** [[autor-tucidides|Tucídides]]  
> **Volume GBWW:** 6 | **Idioma Original:** Grego Antigo  
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
