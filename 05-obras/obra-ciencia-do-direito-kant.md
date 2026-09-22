---
tipo: obra
id: "work:science-of-right"
slug: "obra-ciencia-do-direito-kant"
canonicalTitle: "The Science of Right"
displayTitlePtBr: "A Ciência do Direito"
canonical-title: "The Science of Right"
display-title-ptbr: "A Ciência do Direito"
authorIds: ["author:kant"]
author-ids: ["author:kant"]
autores:
  - "[[autor-immanuel-kant|Immanuel Kant]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 42
gbww-volume: 42
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "A Ciência do Direito"
  - "The Science of Right"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# A Ciência do Direito (*The Science of Right*)

> **Autoria:** [[autor-immanuel-kant|Immanuel Kant]]  
> **Volume GBWW:** 42 | **Idioma Original:** Alemão  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Primeira parte da Metafísica dos Costumes, formulando os princípios universais do direito, a liberdade externa e a dignidade humana inalienável.

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
