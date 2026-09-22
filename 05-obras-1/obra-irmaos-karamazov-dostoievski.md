---
tipo: obra
id: "work:brothers-karamazov"
slug: "obra-irmaos-karamazov-dostoievski"
canonicalTitle: "The Brothers Karamazov"
displayTitlePtBr: "Os Irmãos Karamázov"
canonical-title: "The Brothers Karamazov"
display-title-ptbr: "Os Irmãos Karamázov"
authorIds: ["author:dostoevsky"]
author-ids: ["author:dostoevsky"]
autores:
  - "[[autor-fiodor-dostoievski|Fiódor Dostoiévski]]"
originalLanguage: "Russo"
original-language: "Russo"
gbwwVolume: 52
gbww-volume: 52
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "Os Irmãos Karamázov"
  - "The Brothers Karamazov"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Os Irmãos Karamázov (*The Brothers Karamazov*)

> **Autoria:** [[autor-fiodor-dostoievski|Fiódor Dostoiévski]]  
> **Volume GBWW:** 52 | **Idioma Original:** Russo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Romance existencial e filosófico sobre Deus, a liberdade, a culpa moral e a opressão espiritual e material na sociedade russa.

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
