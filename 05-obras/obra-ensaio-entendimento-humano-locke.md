---
tipo: obra
id: "work:human-understanding-locke"
slug: "obra-ensaio-entendimento-humano-locke"
canonicalTitle: "An Essay Concerning Human Understanding"
displayTitlePtBr: "Ensaio sobre o Entendimento Humano"
canonical-title: "An Essay Concerning Human Understanding"
display-title-ptbr: "Ensaio sobre o Entendimento Humano"
authorIds: ["author:locke"]
author-ids: ["author:locke"]
autores:
  - "[[autor-john-locke|John Locke]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 35
gbww-volume: 35
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Ensaio sobre o Entendimento Humano"
  - "An Essay Concerning Human Understanding"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Ensaio sobre o Entendimento Humano (*An Essay Concerning Human Understanding*)

> **Autoria:** [[autor-john-locke|John Locke]]  
> **Volume GBWW:** 35 | **Idioma Original:** Inglês  
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
