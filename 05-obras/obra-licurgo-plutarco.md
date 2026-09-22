---
tipo: obra
id: "work:lycurgus-plutarch"
slug: "obra-licurgo-plutarco"
canonicalTitle: "Lycurgus"
displayTitlePtBr: "Licurgo"
canonical-title: "Lycurgus"
display-title-ptbr: "Licurgo"
authorIds: ["author:plutarch"]
author-ids: ["author:plutarch"]
autores:
  - "[[autor-plutarco|Plutarco]]"
originalLanguage: "Grego Antigo"
original-language: "Grego Antigo"
gbwwVolume: 14
gbww-volume: 14
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Licurgo"
  - "Lycurgus"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Licurgo (*Lycurgus*)

> **Autoria:** [[autor-plutarco|Plutarco]]  
> **Volume GBWW:** 14 | **Idioma Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Biografia do mítico legislador espartano, detalhando as instituições da Lacônia e a submissão militarizada dos hilotas.

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
