---
tipo: obra
id: "work:philosophy-of-history"
slug: "obra-filosofia-da-historia-hegel"
canonicalTitle: "The Philosophy of History"
displayTitlePtBr: "A Filosofia da História"
canonical-title: "The Philosophy of History"
display-title-ptbr: "A Filosofia da História"
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
  - "A Filosofia da História"
  - "The Philosophy of History"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# A Filosofia da História (*The Philosophy of History*)

> **Autoria:** [[autor-gwf-hegel|G. W. F. Hegel]]  
> **Volume GBWW:** 46 | **Idioma Original:** Alemão  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Lições de Hegel sobre o desenvolvimento histórico universal como desdobramento dialético da consciência da liberdade.

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
