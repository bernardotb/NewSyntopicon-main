---
tipo: obra
id: work:bible-2-thessalonians
slug: obra-2-tessalonicenses-novo-testamento
canonicalTitle: Second Epistle to the Thessalonians
displayTitlePtBr: Segunda Epístola aos Tessalonicenses
canonical-title: Second Epistle to the Thessalonians
display-title-ptbr: Segunda Epístola aos Tessalonicenses
authorIds: &id001
- author:bible-new-testament
author-ids: *id001
autores:
- '[[autor-novo-testamento|Novo Testamento]]'
originalLanguage: Grego Koiné
original-language: Grego Koiné
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
- II Tessalonicenses
- 2 Thessalonians
- Segunda Epístola aos Tessalonicenses
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Segunda Epístola aos Tessalonicenses (*Second Epistle to the Thessalonians*)

> **Autor:** [[autor-novo-testamento|Novo Testamento]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Grego Koiné  
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
