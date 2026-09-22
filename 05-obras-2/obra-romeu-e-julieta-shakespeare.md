---
tipo: obra
id: work:romeo-and-juliet-shakespeare
slug: obra-romeu-e-julieta-shakespeare
canonicalTitle: Romeo and Juliet
displayTitlePtBr: Romeu e Julieta
canonical-title: Romeo and Juliet
display-title-ptbr: Romeu e Julieta
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
- Romeu e Julieta
- Romeo and Juliet
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Romeu e Julieta (*Romeo and Juliet*)

> **Autor:** [[autor-william-shakespeare|William Shakespeare]]  
> **Volume GBWW:** [[vol-26|GBWW Vol. 26]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Tragédia imortal sobre o amor juvenil frustrado pelo conflito geracional e pela rixa secular entre Capuletos e Montecchios, destacando o conflito entre dever filial e autonomia amorosa.

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
