---
tipo: obra
id: work:comedy-of-errors-shakespeare
slug: obra-comedia-dos-erros-shakespeare
canonicalTitle: The Comedy of Errors
displayTitlePtBr: A Comédia dos Erros
canonical-title: The Comedy of Errors
display-title-ptbr: A Comédia dos Erros
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
- A Comédia dos Erros
- The Comedy of Errors
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: A Comédia dos Erros (*The Comedy of Errors*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Comédia de Shakespeare explorando equívocos de identidade entre pares de gêmeos idênticos, abordando simultaneamente a fidelidade conjugal, os direitos da esposa e os deveres domésticos.

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
