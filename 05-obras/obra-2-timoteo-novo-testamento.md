---
tipo: obra
id: work:bible-2-timothy
slug: obra-2-timoteo-novo-testamento
canonicalTitle: Second Epistle to Timothy
displayTitlePtBr: Segunda Epístola a Timóteo
canonical-title: Second Epistle to Timothy
display-title-ptbr: Segunda Epístola a Timóteo
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
source-id: source:pdf-justice-1952
tags:
- type/obra
- type/canonico
aliases:
- Segunda Epístola a Timóteo
- Second Epistle to Timothy
- II Timóteo
- II Timothy
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Segunda Epístola a Timóteo (*Second Epistle to Timothy*)

> **Autor:** [[autor-novo-testamento|Novo Testamento]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Grego Koiné  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Segunda epístola pastoral paulina dirigida a Timóteo, destacando a perseverança apostólica e utilizando metáforas sobre o lavrador diligente que deve ser o primeiro a participar dos frutos do seu trabalho.

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
