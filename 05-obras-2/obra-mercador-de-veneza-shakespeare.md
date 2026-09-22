---
tipo: obra
id: work:merchant-of-venice-shakespeare
slug: obra-mercador-de-veneza-shakespeare
canonicalTitle: The Merchant of Venice
displayTitlePtBr: O Mercador de Veneza
canonical-title: The Merchant of Venice
display-title-ptbr: O Mercador de Veneza
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
- O Mercador de Veneza
- The Merchant of Venice
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: O Mercador de Veneza (*The Merchant of Venice*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Peça de Shakespeare que articula o drama da dívida de Shylock e Pórcia com a fuga de Jéssica da autoridade paterna judaica e as obrigações do testamento paternal dos três cofres.

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
