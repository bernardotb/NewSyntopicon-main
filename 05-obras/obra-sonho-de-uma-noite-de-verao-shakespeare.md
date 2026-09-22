---
tipo: obra
id: work:midsummer-nights-dream-shakespeare
slug: obra-sonho-de-uma-noite-de-verao-shakespeare
canonicalTitle: A Midsummer Night's Dream
displayTitlePtBr: Sonho de uma Noite de Verão
canonical-title: A Midsummer Night's Dream
display-title-ptbr: Sonho de uma Noite de Verão
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
- Sonho de uma Noite de Verão
- A Midsummer Night's Dream
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Sonho de uma Noite de Verão (*A Midsummer Night's Dream*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Comédia poética que se abre com o rígido conflito legal em Atenas entre a autoridade patriarcal de Egeu sobre a filha Hérmia e a liberdade de escolha do casamento matrimonial.

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
