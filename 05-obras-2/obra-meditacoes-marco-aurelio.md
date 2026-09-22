---
tipo: obra
id: "work:meditations-aurelius"
slug: "obra-meditacoes-marco-aurelio"
canonicalTitle: "The Meditations of Marcus Aurelius"
displayTitlePtBr: "Meditações"
canonical-title: "The Meditations of Marcus Aurelius"
display-title-ptbr: "Meditações"
authorIds: ["author:marcus-aurelius"]
author-ids: ["author:marcus-aurelius"]
autores:
  - "[[autor-marco-aurelio|Marco Aurélio]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 12
gbww-volume: 12
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Meditações"
  - "The Meditations of Marcus Aurelius"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Meditações (*The Meditations of Marcus Aurelius*)

> **Autoria:** [[autor-marco-aurelio|Marco Aurélio]]  
> **Volume GBWW:** 12 | **Idioma Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (GBWW 1952), indexada tematicamente no *Syntopicon*.

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
