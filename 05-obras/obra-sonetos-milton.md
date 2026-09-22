---
tipo: obra
id: work:sonnets-milton
slug: obra-sonetos-milton
canonicalTitle: Sonnets
displayTitlePtBr: Sonetos
canonical-title: Sonnets
display-title-ptbr: Sonetos
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
- Sonetos
- Sonnets
- Sonnets of John Milton
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Sonetos (*Sonnets*)

> **Autor:** [[autor-john-milton|John Milton]]  
> **Volume GBWW:** [[vol-32|GBWW Vol. 32]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Coletânea poética de John Milton contendo os sonetos de maturidade cívica, moral e política, notadamente o Soneto XII, que estabelece a clássica distinção: 'Licence they mean when they cry Liberty'.

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
