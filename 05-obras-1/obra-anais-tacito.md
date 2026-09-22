---
tipo: obra
id: work:annals-tacitus
slug: obra-anais-tacito
canonicalTitle: The Annals
displayTitlePtBr: Anais
canonical-title: The Annals
display-title-ptbr: Anais
authorIds:
- author:tacitus
author-ids:
- author:tacitus
autores:
- '[[autor-tacito|Cornélio Tácito]]'
originalLanguage: Latim
original-language: Latim
gbwwVolume: 15
gbww-volume: 15
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Anais
- The Annals
- Annals
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Anais (*The Annals*)

> **Autor:** [[autor-tacito|Cornélio Tácito]]  
> **Volume GBWW:** [[vol-15|GBWW Vol. 15]]  
> **Língua Original:** Latim  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra historiográfica romana monumental cobrindo os reinados dos imperadores Júlio-Claudio (Tibério, Calígula, Cláudio e Nero).

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
