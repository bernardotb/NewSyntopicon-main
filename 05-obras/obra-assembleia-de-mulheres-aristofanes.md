---
tipo: obra
id: work:ecclesiazusae-aristophanes
slug: obra-assembleia-de-mulheres-aristofanes
canonicalTitle: Ecclesiazusae
displayTitlePtBr: A Assembleia de Mulheres
canonical-title: Ecclesiazusae
display-title-ptbr: A Assembleia de Mulheres
authorIds: &id001
- author:aristophanes
author-ids: *id001
autores:
- '[[autor-aristofanes|Aristófanes]]'
originalLanguage: Grego Antigo
original-language: Grego Antigo
gbwwVolume: 5
gbww-volume: 5
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- A Assembleia de Mulheres
- Ecclesiazusae
- The Ecclesiazusae
- As Mulheres no Parlamento
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: A Assembleia de Mulheres (*Ecclesiazusae*)

> **Autor:** [[autor-aristofanes|Aristófanes]]  
> **Volume GBWW:** [[vol-05|Volume 5]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (1952), volume 5.

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
