---
tipo: obra
id: work:bible-colossians
slug: obra-colossenses-novo-testamento
canonicalTitle: Epistle to the Colossians
displayTitlePtBr: Epístola aos Colossenses
canonical-title: Epistle to the Colossians
display-title-ptbr: Epístola aos Colossenses
authorIds:
- author:bible-new-testament
author-ids:
- author:bible-new-testament
autores:
- '[[autor-novo-testamento|Novo Testamento]]'
originalLanguage: Grego Koiné
original-language: Grego Koiné
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
- Epístola aos Colossenses
- Epistle to the Colossians
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Epístola aos Colossenses (*Epistle to the Colossians*)

> **Autor:** [[autor-novo-testamento|Novo Testamento]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Grego Koiné  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Epístola paulina que estabelece as regras da ordem doméstica cristã, articulando as obrigações recíprocas entre esposos, pais, filhos e servos.

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
