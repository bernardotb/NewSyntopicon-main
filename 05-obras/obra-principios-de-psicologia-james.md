---
tipo: obra
id: "work:psychology-james"
slug: "obra-principios-de-psicologia-james"
canonicalTitle: "The Principles of Psychology"
displayTitlePtBr: "Princípios de Psicologia"
canonical-title: "The Principles of Psychology"
display-title-ptbr: "Princípios de Psicologia"
authorIds: ["author:william-james"]
author-ids: ["author:william-james"]
autores:
  - "[[autor-william-james]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 53
gbww-volume: 53
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Princípios de Psicologia"
  - "The Principles of Psychology"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Princípios de Psicologia (*The Principles of Psychology*)

> **Autoria:** [[autor-william-james]]  
> **Volume GBWW:** 53 | **Idioma Original:** Inglês  
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
