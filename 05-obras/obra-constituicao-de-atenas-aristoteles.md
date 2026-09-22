---
tipo: obra
id: "work:athenian-constitution"
slug: "obra-constituicao-de-atenas-aristoteles"
canonicalTitle: "Athenian Constitution"
displayTitlePtBr: "Constituição de Atenas"
canonical-title: "Athenian Constitution"
display-title-ptbr: "Constituição de Atenas"
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
  - "Constituição de Atenas"
  - "Athenian Constitution"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Constituição de Atenas (*Athenian Constitution*)

> **Autoria:** [[autor-aristoteles|Aristóteles]]  
> **Volume GBWW:** 9 | **Idioma Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
História institucional e política de Atenas, registrando a servidão por dívidas antes das reformas solonianas.

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
