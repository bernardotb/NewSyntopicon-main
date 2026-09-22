---
tipo: obra
id: "work:nicomachean-ethics"
slug: "obra-etica-a-nicomaco-aristoteles"
canonicalTitle: "Nicomachean Ethics"
displayTitlePtBr: "Ética a Nicômaco"
canonical-title: "Nicomachean Ethics"
display-title-ptbr: "Ética a Nicômaco"
authorIds: ["author:aristotle"]
author-ids: ["author:aristotle"]
autores:
  - "[[autor-aristoteles|Aristóteles]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 9
gbww-volume: 9
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Ética a Nicômaco"
  - "Nicomachean Ethics"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Ética a Nicômaco (*Nicomachean Ethics*)

> **Autoria:** [[autor-aristoteles|Aristóteles]]  
> **Volume GBWW:** 9 | **Idioma Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tratado ético magistral de Aristóteles que estabelece a justiça como virtude cardeal, distinguindo suas modalidades universais e particulares.

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
