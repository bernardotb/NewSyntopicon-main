---
tipo: obra
id: "work:eclogues-virgil"
slug: "obra-bucolicas-virgilio"
canonicalTitle: "Eclogues"
displayTitlePtBr: "Bucólicas (Éclogas)"
canonical-title: "Eclogues"
display-title-ptbr: "Bucólicas (Éclogas)"
authorIds: ["author:virgil"]
author-ids: ["author:virgil"]
autores:
  - "[[autor-virgilio|Virgílio]]"
originalLanguage: "Latim"
original-language: "Latim"
gbwwVolume: 13
gbww-volume: 13
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Bucólicas (Éclogas)"
  - "Eclogues"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Bucólicas (Éclogas) (*Eclogues*)

> **Autoria:** [[autor-virgilio|Virgílio]]  
> **Volume GBWW:** 13 | **Idioma Original:** Latim  
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
