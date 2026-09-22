---
tipo: obra
id: work:bible-tobit
slug: obra-tobias-apocrifos
canonicalTitle: Tobit
displayTitlePtBr: Tobias
canonical-title: Tobit
display-title-ptbr: Tobias
authorIds:
- author:bible-apocrypha
author-ids:
- author:bible-apocrypha
autores:
- '[[autor-apocrifos|Apócrifos]]'
originalLanguage: Aramaico / Hebraico
original-language: Aramaico / Hebraico
gbwwVolume: null
gbww-volume: null
provenance: original-corpus
epistemology: source
verification: verified
source-id: source:pdf-justice-1952
tags:
- type/obra
- type/canonico
aliases:
- Tobias
- Tobit
- Book of Tobit
- Livro de Tobias
status: ativo
created: '2026-09-21'
modified: '2026-09-21'
---

# Obra: Tobias (*Tobit*)

> **Autor:** [[autor-apocrifos|Apócrifos]]  
> **Volume GBWW:** Corpus Bíblico Deuterocanônico  
> **Língua Original:** Aramaico / Hebraico  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
Narrativa moralizante e sapiencial do período intertestamentário, centrada na piedade de Tobit e seu filho Tobias, contendo preceitos sobre esmola, retribuição moral e o pagamento imediato e justo do salário ao trabalhador.

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
