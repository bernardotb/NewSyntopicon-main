---
tipo: obra
id: work:taming-of-the-shrew-shakespeare
slug: obra-megera-domada-shakespeare
canonicalTitle: The Taming of the Shrew
displayTitlePtBr: A Megera Domada
canonical-title: The Taming of the Shrew
display-title-ptbr: A Megera Domada
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
- A Megera Domada
- The Taming of the Shrew
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: A Megera Domada (*The Taming of the Shrew*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Comédia de Shakespeare sobre a corte, casamento e harmonização de vontades entre Petrúquio e Catarina, culminando no célebre discurso de encerramento sobre os deveres das esposas e a paz doméstica.

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
