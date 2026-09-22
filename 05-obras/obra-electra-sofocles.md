---
tipo: obra
id: work:electra-sophocles
slug: obra-electra-sofocles
canonicalTitle: Electra
displayTitlePtBr: Electra
canonical-title: Electra
display-title-ptbr: Electra
authorIds:
- author:sophocles
author-ids:
- author:sophocles
autores:
- '[[autor-sofocles|Sófocles]]'
originalLanguage: Grego Antigo
original-language: Grego Antigo
gbwwVolume: 5
gbww-volume: 5
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Electra
- Electra
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Electra (*Electra*)

> **Autor:** [[autor-sofocles|Sófocles]]  
> **Volume GBWW:** [[vol-05|GBWW Vol. 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Dramatização sofocliana do luto inquebrantável de Electra e da consumação da vingança filial de Orestes contra a mãe e Egisto pelo assassinato do pai.

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
