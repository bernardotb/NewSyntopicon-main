---
tipo: obra
id: work:1st-henry-iv-shakespeare
slug: obra-1-henrique-iv-shakespeare
canonicalTitle: The First Part of King Henry the Fourth
displayTitlePtBr: Henrique IV, Parte 1
canonical-title: The First Part of King Henry the Fourth
display-title-ptbr: Henrique IV, Parte 1
authorIds:
- author:shakespeare
author-ids:
- author:shakespeare
autores:
- '[[autor-william-shakespeare|William Shakespeare]]'
originalLanguage: Inglês
original-language: Inglês
gbwwVolume: 26
gbww-volume: 26
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Henrique IV, Parte 1
- The First Part of King Henry the Fourth
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Henrique IV, Parte 1 (*The First Part of King Henry the Fourth*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Drama histórico que dramatiza a rebelião contra Henrique IV e o comovente confronto entre o rei e o Príncipe Hal sobre a dignidade do herdeiro e as responsabilidades filiais perante a coroa.

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
