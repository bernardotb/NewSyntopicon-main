---
tipo: obra
id: work:othello-shakespeare
slug: obra-otelo-shakespeare
canonicalTitle: Othello, the Moor of Venice
displayTitlePtBr: Otelo, o Mouro de Veneza
canonical-title: Othello, the Moor of Venice
display-title-ptbr: Otelo, o Mouro de Veneza
authorIds:
- author:shakespeare
author-ids:
- author:shakespeare
autores:
- '[[autor-william-shakespeare|William Shakespeare]]'
originalLanguage: Inglês
original-language: Inglês
gbwwVolume: 27
gbww-volume: 27
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Otelo, o Mouro de Veneza
- Othello, the Moor of Venice
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Otelo, o Mouro de Veneza (*Othello, the Moor of Venice*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-27|GBWW Vol. 27]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tragédia em que a desconfiança inoculada por Iago destrói o vínculo matrimonial sagrado entre Otelo e Desdêmona, abordando os conceitos de honra, ciúme, fidelidade conjugal e falso julgamento doméstico.

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
