---
tipo: obra
id: work:areopagitica-milton
slug: obra-areopagitica-milton
canonicalTitle: Areopagitica
displayTitlePtBr: Areopagítica
canonical-title: Areopagitica
display-title-ptbr: Areopagítica
authorIds:
- author:milton
author-ids:
- author:milton
autores:
- '[[autor-john-milton|John Milton]]'
originalLanguage: Inglês
original-language: Inglês
gbwwVolume: 32
gbww-volume: 32
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Areopagítica
- Areopagitica
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Areopagítica (*Areopagitica*)

> **Autor:** [[autor-john-milton|John Milton]]  
> **Volume GBWW:** [[vol-32|GBWW Vol. 32]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Discurso de John Milton dirigido ao Parlamento inglês em defesa intransigente da liberdade de imprensa e de expressão contra a censura prévia.

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
