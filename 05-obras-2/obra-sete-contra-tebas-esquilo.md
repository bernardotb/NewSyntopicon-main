---
tipo: obra
id: work:seven-against-thebes-aeschylus
slug: obra-sete-contra-tebas-esquilo
canonicalTitle: Seven Against Thebes
displayTitlePtBr: Sete contra Tebas
canonical-title: Seven Against Thebes
display-title-ptbr: Sete contra Tebas
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
- Sete contra Tebas
- Seven Against Thebes
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Sete contra Tebas (*Seven Against Thebes*)

> **Autor:** [[autor-esquilo|Ésquilo]]  
> **Volume GBWW:** [[vol-05|GBWW Vol. 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tragédia clássica de Ésquilo sobre o cerco de Tebas e a trágica fratricida disputa entre Polinices e Etéocles pelo trono paterno, culminando no dilema do dever de sepultamento.

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
