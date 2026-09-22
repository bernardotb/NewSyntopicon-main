---
tipo: obra
id: work:oedipus-at-colonus-sophocles
slug: obra-edipo-em-colono-sofocles
canonicalTitle: Oedipus at Colonus
displayTitlePtBr: Édipo em Colono
canonical-title: Oedipus at Colonus
display-title-ptbr: Édipo em Colono
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
- Édipo em Colono
- Oedipus at Colonus
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Édipo em Colono (*Oedipus at Colonus*)

> **Autor:** [[autor-sofocles|Sófocles]]  
> **Volume GBWW:** [[vol-05|GBWW Vol. 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tragédia de Sófocles que narra a velhice cega e o refúgio sagrado de Édipo em Colono sob a proteção de Teseu, bem como a amarga maldição proferida contra seus filhos traidores.

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
