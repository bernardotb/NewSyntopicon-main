---
tipo: obra
id: "work:decline-and-fall"
slug: "obra-declinio-e-queda-gibbon"
canonicalTitle: "The Decline and Fall of the Roman Empire"
displayTitlePtBr: "Declínio e Queda do Império Romano"
canonical-title: "The Decline and Fall of the Roman Empire"
display-title-ptbr: "Declínio e Queda do Império Romano"
authorIds: ["author:gibbon"]
author-ids: ["author:gibbon"]
autores:
  - "[[autor-edward-gibbon|Edward Gibbon]]"
originalLanguage: "Inglês"
original-language: "Inglês"
gbwwVolume: 40
gbww-volume: 40
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Declínio e Queda do Império Romano"
  - "The Decline and Fall of the Roman Empire"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Declínio e Queda do Império Romano (*The Decline and Fall of the Roman Empire*)

> **Autoria:** [[autor-edward-gibbon|Edward Gibbon]]  
> **Volume GBWW:** 40 | **Idioma Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
História monumental da civilização romana desde os Antoninos até a tomada de Constantinopla, dissecando sua estrutura social e servil.

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
