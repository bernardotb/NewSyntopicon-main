---
tipo: obra
id: work:provincial-letters-pascal
slug: obra-cartas-provinciais-pascal
canonicalTitle: The Provincial Letters
displayTitlePtBr: As Cartas Provinciais
canonical-title: The Provincial Letters
display-title-ptbr: As Cartas Provinciais
authorIds: &id001
- author:pascal
author-ids: *id001
autores:
- '[[autor-blaise-pascal|Blaise Pascal]]'
originalLanguage: Francês
original-language: Francês
gbwwVolume: 33
gbww-volume: 33
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- As Cartas Provinciais
- The Provincial Letters
- Lettres provinciales
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: As Cartas Provinciais (*The Provincial Letters*)

> **Autor:** [[autor-blaise-pascal|Blaise Pascal]]  
> **Volume GBWW:** [[vol-33|Volume 33]]  
> **Língua Original:** Francês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (1952), volume 33.

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
