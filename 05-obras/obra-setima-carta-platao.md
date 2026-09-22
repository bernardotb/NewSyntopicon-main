---
tipo: obra
id: work:seventh-letter-plato
slug: obra-setima-carta-platao
canonicalTitle: Seventh Letter
displayTitlePtBr: Sétima Carta
canonical-title: Seventh Letter
display-title-ptbr: Sétima Carta
authorIds: &id001
- author:plato
author-ids: *id001
autores:
- '[[autor-platao|Platão]]'
originalLanguage: Grego Antigo
original-language: Grego Antigo
gbwwVolume: 7
gbww-volume: 7
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- Sétima Carta
- Seventh Letter
- Epistle VII
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Sétima Carta (*Seventh Letter*)

> **Autor:** [[autor-platao|Platão]]  
> **Volume GBWW:** [[vol-07|Volume 7]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (1952), volume 7.

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
