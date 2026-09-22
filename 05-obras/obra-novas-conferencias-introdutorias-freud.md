---
tipo: obra
id: work:new-introductory-lectures-freud
slug: obra-novas-conferencias-introdutorias-freud
canonicalTitle: New Introductory Lectures on Psycho-Analysis
displayTitlePtBr: Novas Conferências Introdutórias sobre Psicanálise
canonical-title: New Introductory Lectures on Psycho-Analysis
display-title-ptbr: Novas Conferências Introdutórias sobre Psicanálise
authorIds:
- author:freud
author-ids:
- author:freud
autores:
- '[[autor-sigmund-freud|Sigmund Freud]]'
originalLanguage: Alemão
original-language: Alemão
gbwwVolume: 54
gbww-volume: 54
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Novas Conferências Introdutórias sobre Psicanálise
- New Introductory Lectures on Psycho-Analysis
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Novas Conferências Introdutórias sobre Psicanálise (*New Introductory Lectures on Psycho-Analysis*)

> **Autor:** [[autor-sigmund-freud|Sigmund Freud]]  
> **Volume GBWW:** [[vol-54|GBWW Vol. 54]]  
> **Língua Original:** Alemão  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Série de conferências psicanalíticas de Sigmund Freud aprofundando a dissecção da personalidade psíquica, a gênese do Superego a partir da autoridade e do amor paterno, e o papel da família na civilização.

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
