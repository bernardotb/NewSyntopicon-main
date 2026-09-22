---
tipo: obra
id: work:agamemnon-aeschylus
slug: obra-agamemnon-esquilo
canonicalTitle: Agamemnon
displayTitlePtBr: Agamêmnon
canonical-title: Agamemnon
display-title-ptbr: Agamêmnon
authorIds:
- author:aeschylus
author-ids:
- author:aeschylus
autores:
- '[[autor-esquilo|Ésquilo]]'
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
- Agamêmnon
- Agamemnon
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Agamêmnon (*Agamemnon*)

> **Autor:** [[autor-esquilo|Ésquilo]]  
> **Volume GBWW:** [[vol-05|GBWW Vol. 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Primeira peça da trilogia Oresteia de Ésquilo, retratando o retorno triunfal e o assassinato de Agamêmnon por Clitemnestra, explorando a terrível cadeia de vingança e justiça de sangue no palácio de Argos.

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
