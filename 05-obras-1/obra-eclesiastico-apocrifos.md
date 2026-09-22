---
tipo: obra
id: work:bible-ecclesiasticus
slug: obra-eclesiastico-apocrifos
canonicalTitle: Ecclesiasticus
displayTitlePtBr: Eclesiástico (Sirácida)
canonical-title: Ecclesiasticus
display-title-ptbr: Eclesiástico (Sirácida)
authorIds:
- author:bible-apocrypha
author-ids:
- author:bible-apocrypha
autores:
- '[[autor-apocrifos|Apócrifos]]'
originalLanguage: Hebraico / Grego
original-language: Hebraico / Grego
gbwwVolume: null
gbww-volume: null
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Eclesiástico (Sirácida)
- Ecclesiasticus
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Eclesiástico (Sirácida) (*Ecclesiasticus*)

> **Autor:** [[autor-apocrifos|Apócrifos]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Hebraico / Grego  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Livro sapiencial do período intertestamentário, atribuído a Jesus Ben Sirá, contendo extensas instruções morais e preceitos sobre honra aos pais, piedade filial e disciplina familiar.

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
