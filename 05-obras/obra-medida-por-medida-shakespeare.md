---
tipo: obra
id: work:measure-for-measure-shakespeare
slug: obra-medida-por-medida-shakespeare
canonicalTitle: Measure for Measure
displayTitlePtBr: Medida por Medida
canonical-title: Measure for Measure
display-title-ptbr: Medida por Medida
authorIds:
- author:shakespeare
author-ids:
- author:shakespeare
autores:
- '[[autor-william-shakespeare|William Shakespeare]]'
originalLanguage: Inglês
original-language: Inglês
gbwwVolume: 27
gbww-volume: 27
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Medida por Medida
- Measure for Measure
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Medida por Medida (*Measure for Measure*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-27|GBWW Vol. 27]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Peça teatral de Shakespeare que examina profundamente a relação entre justiça, clemência, estrita legalidade e a corrupção da liberdade em licença desmedida.

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
