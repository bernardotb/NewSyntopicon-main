---
tipo: obra
id: "work:king-lear-shakespeare"
slug: "obra-rei-lear-shakespeare"
canonicalTitle: "King Lear"
displayTitlePtBr: "Rei Lear"
canonical-title: "King Lear"
display-title-ptbr: "Rei Lear"
authorIds: ["author:shakespeare"]
author-ids: ["author:shakespeare"]
autores:
  - "[[autor-william-shakespeare|William Shakespeare]]"
originalLanguage: "Inglês"
original-language: "Inglês"
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
  - "Rei Lear"
  - "King Lear"
status: ativo
created: "2026-09-17"
modified: "2026-09-17"
---
# Obra: Rei Lear (*King Lear*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-27|GBWW Vol. 27]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Uma das tragédias magnas de Shakespeare sobre a divisão injusta de um reino, a ingratidão filial, a loucura e a descoberta dilacerante da lei natural e da justiça elementar perante os elementos cósmicos.

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
