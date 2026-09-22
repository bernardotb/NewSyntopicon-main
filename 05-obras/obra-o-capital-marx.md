---
tipo: obra
id: "work:capital-marx"
slug: "obra-o-capital-marx"
canonicalTitle: "Capital"
displayTitlePtBr: "O Capital"
canonical-title: "Capital"
display-title-ptbr: "O Capital"
authorIds: ["author:marx"]
author-ids: ["author:marx"]
autores:
  - "[[autor-karl-marx|Karl Marx]]"
originalLanguage: "Alemão"
original-language: "Alemão"
gbwwVolume: 50
gbww-volume: 50
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "O Capital"
  - "Capital"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# O Capital (*Capital*)

> **Autoria:** [[autor-karl-marx|Karl Marx]]  
> **Volume GBWW:** 50 | **Idioma Original:** Alemão  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Crítica monumental da economia política, contendo a fundamentação teórica da mais-valia, do processo de acumulação e da escravidão assalariada.

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
