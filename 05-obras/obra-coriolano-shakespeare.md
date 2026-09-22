---
tipo: obra
id: work:coriolanus-shakespeare
slug: obra-coriolano-shakespeare
canonicalTitle: The Tragedy of Coriolanus
displayTitlePtBr: Coriolano
canonical-title: The Tragedy of Coriolanus
display-title-ptbr: Coriolano
authorIds: &id001
- author:shakespeare
author-ids: *id001
autores:
- '[[autor-william-shakespeare|William Shakespeare]]'
originalLanguage: Inglês Moderno
original-language: Inglês Moderno
gbwwVolume: 27
gbww-volume: 27
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- Coriolano
- Coriolanus
- The Tragedy of Coriolanus
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Coriolano (*The Tragedy of Coriolanus*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-27|Volume 27]]  
> **Língua Original:** Inglês Moderno  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (1952), volume 27.

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
