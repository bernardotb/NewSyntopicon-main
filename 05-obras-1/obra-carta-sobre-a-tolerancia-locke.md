---
tipo: obra
id: "work:letter-concerning-toleration-locke"
slug: "obra-carta-sobre-a-tolerancia-locke"
canonicalTitle: "A Letter Concerning Toleration"
displayTitlePtBr: "Carta sobre a Tolerância"
canonical-title: "A Letter Concerning Toleration"
display-title-ptbr: "Carta sobre a Tolerância"
authorIds: ["author:locke"]
author-ids: ["author:locke"]
autores:
  - "[[autor-john-locke|John Locke]]"
originalLanguage: "Latim / Inglês"
original-language: "Latim / Inglês"
gbwwVolume: 35
gbww-volume: 35
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Carta sobre a Tolerância"
  - "A Letter Concerning Toleration"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Carta sobre a Tolerância (*A Letter Concerning Toleration*)

> **Autoria:** [[autor-john-locke|John Locke]]  
> **Volume GBWW:** [[vol-35|GBWW Vol. 35]] | **Idioma Original:** Latim / Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Ensaio clássico de John Locke sobre a separação entre as esferas civil e religiosa, fundamentando a inalienabilidade dos direitos de consciência contra a interferência coercitiva e tirânica do Estado.

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
