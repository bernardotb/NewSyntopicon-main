---
tipo: obra
id: work:bible-nehemiah
slug: obra-neemias-antigo-testamento
canonicalTitle: Nehemiah (II Esdras)
displayTitlePtBr: Neemias (II Esdras)
canonical-title: Nehemiah (II Esdras)
display-title-ptbr: Neemias (II Esdras)
authorIds: &id001
- author:bible-old-testament
author-ids: *id001
autores:
- '[[autor-antigo-testamento|Antigo Testamento]]'
originalLanguage: Hebraico
original-language: Hebraico
gbwwVolume: null
gbww-volume: null
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- Neemias
- Nehemiah
- II Esdras
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Neemias (II Esdras) (*Nehemiah (II Esdras)*)

> **Autor:** [[autor-antigo-testamento|Antigo Testamento]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Hebraico  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Livro integrante do corpus bíblico canônico indexado no *Syntopicon* (1952).

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
