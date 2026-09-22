---
tipo: obra
id: work:coriolanus-plutarch
slug: obra-coriolano-plutarco
canonicalTitle: Coriolanus
displayTitlePtBr: Coriolano
canonical-title: Coriolanus
display-title-ptbr: Coriolano
authorIds:
- author:plutarch
author-ids:
- author:plutarch
autores:
- '[[autor-plutarco|Plutarco]]'
originalLanguage: Grego Antigo
original-language: Grego Antigo
gbwwVolume: 14
gbww-volume: 14
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
- type/obra
- type/canonico
aliases:
- Coriolano
- Coriolanus
status: ativo
created: '2026-09-20'
modified: '2026-09-20'
---

# Obra: Coriolano (*Coriolanus*)

> **Autor:** [[autor-plutarco|Plutarco]]  
> **Volume GBWW:** [[vol-14|GBWW Vol. 14]]  
> **Língua Original:** Grego Antigo  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Vida de Caio Márcio Coriolano em Plutarco, examinando a trágica colisão entre o orgulho aristocrático, a fidelidade patrícia e a súplica filial irresistível de sua mãe Volúmnia.

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
