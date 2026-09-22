---
tipo: obra
id: work:birds-aristophanes
slug: obra-as-aves-aristofanes
canonicalTitle: The Birds
displayTitlePtBr: As Aves
canonical-title: The Birds
display-title-ptbr: As Aves
authorIds:
- author:aristophanes
author-ids:
- author:aristophanes
autores:
- '[[autor-aristofanes|Aristófanes]]'
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
- As Aves
- The Birds
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: As Aves (*The Birds*)

> **Autor:** [[autor-aristofanes|Aristófanes]]  
> **Volume GBWW:** [[vol-05|GBWW Vol. 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Comédia grega em que dois atenienses fundam uma cidade aérea utópica entre os deuses e os homens (Nefelococígia), com sátiras à dissolução moral da juventude e ao parricídio.

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
