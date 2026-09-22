---
tipo: obra
id: work:bible-mark
slug: obra-marcos-novo-testamento
canonicalTitle: Gospel According to Mark
displayTitlePtBr: Evangelho segundo Marcos
canonical-title: Gospel According to Mark
display-title-ptbr: Evangelho segundo Marcos
authorIds:
- author:bible-new-testament
author-ids:
- author:bible-new-testament
autores:
- '[[autor-novo-testamento|Novo Testamento]]'
originalLanguage: Grego Koiné
original-language: Grego Koiné
gbwwVolume: null
gbww-volume: null
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Evangelho segundo Marcos
- Gospel According to Mark
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Evangelho segundo Marcos (*Gospel According to Mark*)

> **Autor:** [[autor-novo-testamento|Novo Testamento]]  
> **Volume GBWW:** Corpus Bíblico  
> **Língua Original:** Grego Koiné  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Segundo evangelho sinótico canônico, relatando os ensinamentos e o ministério de Jesus Cristo, com passagens fundamentais sobre a honra aos pais e o mandamento moral divino.

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
