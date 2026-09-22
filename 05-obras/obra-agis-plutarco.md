---
tipo: obra
id: work:agis-plutarch
slug: obra-agis-plutarco
canonicalTitle: Agis
displayTitlePtBr: Ágis
canonical-title: Agis
display-title-ptbr: Ágis
authorIds: &id001
- author:plutarch
author-ids: *id001
autores:
- '[[autor-plutarco|Plutarco]]'
originalLanguage: Grego Antigo
original-language: Grego Antigo
gbwwVolume: 14
gbww-volume: 14
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:gbww-1952
tags:
- type/obra
- type/canonico
aliases:
- Ágis
- Agis
- Vida de Ágis
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Ágis (*Agis*)

> **Autor:** [[autor-plutarco|Plutarco]]  
> **Volume GBWW:** [[vol-14|Volume 14]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Obra canônica integrante da coleção *Great Books of the Western World* (1952), volume 14.

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
