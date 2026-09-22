---
tipo: obra
id: "work:utilitarianism-mill"
slug: "obra-utilitarismo-mill"
canonicalTitle: "Utilitarianism"
displayTitlePtBr: "Utilitarismo"
canonical-title: "Utilitarianism"
display-title-ptbr: "Utilitarismo"
authorIds: ["author:mill"]
author-ids: ["author:mill"]
autores:
  - "[[autor-john-stuart-mill|John Stuart Mill]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 43
gbww-volume: 43
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Utilitarismo"
  - "Utilitarianism"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Utilitarismo (*Utilitarianism*)

> **Autoria:** [[autor-john-stuart-mill|John Stuart Mill]]  
> **Volume GBWW:** 43 | **Idioma Original:** Inglês  
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
