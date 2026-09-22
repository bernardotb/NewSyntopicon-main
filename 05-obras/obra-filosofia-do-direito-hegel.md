---
tipo: obra
id: "work:philosophy-of-right-hegel"
slug: "obra-filosofia-do-direito-hegel"
canonicalTitle: "Philosophy of Right"
displayTitlePtBr: "Filosofia do Direito"
canonical-title: "Philosophy of Right"
display-title-ptbr: "Filosofia do Direito"
authorIds: ["author:hegel"]
author-ids: ["author:hegel"]
autores:
  - "[[autor-gwf-hegel|G. W. F. Hegel]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 46
gbww-volume: 46
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Filosofia do Direito"
  - "Philosophy of Right"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Filosofia do Direito (*Philosophy of Right*)

> **Autoria:** [[autor-gwf-hegel|G. W. F. Hegel]]  
> **Volume GBWW:** 46 | **Idioma Original:** Alemão  
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
