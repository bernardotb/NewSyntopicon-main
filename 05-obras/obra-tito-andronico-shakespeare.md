---
tipo: obra
id: work:titus-andronicus-shakespeare
slug: obra-tito-andronico-shakespeare
canonicalTitle: Titus Andronicus
displayTitlePtBr: Tito Andrônico
canonical-title: Titus Andronicus
display-title-ptbr: Tito Andrônico
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
- Tito Andrônico
- Titus Andronicus
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Tito Andrônico (*Titus Andronicus*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tragédia de vingança romana de Shakespeare em que a honra familiar, a crueldade atroz e a destruição da linhagem de Tito desembocam em justiça sangrenta no banquete final.

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
