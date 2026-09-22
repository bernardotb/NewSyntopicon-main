---
tipo: obra
id: work:new-atlantis
slug: obra-nova-atlantida-bacon
canonicalTitle: New Atlantis
displayTitlePtBr: Nova Atlântida
canonical-title: New Atlantis
display-title-ptbr: Nova Atlântida
authorIds:
- author:bacon
author-ids:
- author:bacon
autores:
- '[[autor-francis-bacon|Francis Bacon]]'
originalLanguage: Inglês
original-language: Inglês
gbwwVolume: 30
gbww-volume: 30
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Nova Atlântida
- New Atlantis
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Nova Atlântida (*New Atlantis*)

> **Autor:** [[autor-francis-bacon|Francis Bacon]]  
> **Volume GBWW:** [[vol-30|GBWW Vol. 30]]  
> **Língua Original:** Inglês  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Utopia científica e moral de Francis Bacon descrevendo a ilha de Bensalem e a célebre 'Festa da Família' (Feast of the Family), celebrando a veneração pública ao patriarca e à descendência fecunda.

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
