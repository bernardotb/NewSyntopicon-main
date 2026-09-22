---
tipo: obra
id: "work:confessions-augustine"
slug: "obra-confissoes-agostinho"
canonicalTitle: "The Confessions of Saint Augustine"
displayTitlePtBr: "Confissões"
canonical-title: "The Confessions of Saint Augustine"
display-title-ptbr: "Confissões"
authorIds: ["author:augustine"]
author-ids: ["author:augustine"]
autores:
  - "[[autor-santo-agostinho|Santo Agostinho]]"
originalLanguage: "Latim"
original-language: "Latim"
gbwwVolume: 18
gbww-volume: 18
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Confissões"
  - "The Confessions of Saint Augustine"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Confissões (*The Confessions of Saint Augustine*)

> **Autoria:** [[autor-santo-agostinho|Santo Agostinho]]  
> **Volume GBWW:** 18 | **Idioma Original:** Latim  
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
