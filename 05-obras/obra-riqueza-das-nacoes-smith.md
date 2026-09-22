---
tipo: obra
id: "work:wealth-of-nations"
slug: "obra-riqueza-das-nacoes-smith"
canonicalTitle: "The Wealth of Nations"
displayTitlePtBr: "A Riqueza das Nações"
canonical-title: "The Wealth of Nations"
display-title-ptbr: "A Riqueza das Nações"
authorIds: ["author:smith"]
author-ids: ["author:smith"]
autores:
  - "[[autor-adam-smith|Adam Smith]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 39
gbww-volume: 39
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "A Riqueza das Nações"
  - "The Wealth of Nations"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# A Riqueza das Nações (*The Wealth of Nations*)

> **Autoria:** [[autor-adam-smith|Adam Smith]]  
> **Volume GBWW:** 39 | **Idioma Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Texto fundador da ciência econômica moderna, demonstrando o funcionamento dos mercados, salários e a ineficiência do trabalho compulsório.

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
