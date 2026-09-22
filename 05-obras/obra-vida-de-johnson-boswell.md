---
tipo: obra
id: "work:life-of-johnson"
slug: "obra-vida-de-johnson-boswell"
canonicalTitle: "The Life of Samuel Johnson, LL.D."
displayTitlePtBr: "A Vida de Samuel Johnson"
canonical-title: "The Life of Samuel Johnson, LL.D."
display-title-ptbr: "A Vida de Samuel Johnson"
authorIds: ["author:boswell"]
author-ids: ["author:boswell"]
autores:
  - "[[autor-james-boswell|James Boswell]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 44
gbww-volume: 44
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "A Vida de Samuel Johnson"
  - "The Life of Samuel Johnson, LL.D."
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# A Vida de Samuel Johnson (*The Life of Samuel Johnson, LL.D.*)

> **Autoria:** [[autor-james-boswell|James Boswell]]  
> **Volume GBWW:** 44 | **Idioma Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
A mais aclamada biografia da literatura inglesa, rica em diálogos vivos sobre filosofia moral, direito, escravidão e sociedade no Iluminismo.

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
