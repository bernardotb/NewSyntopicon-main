---
tipo: obra
id: "work:{{slug-obra}}"
slug: "obra-{{slug-obra}}"
canonical-title: "{{canonical-title}}"
display-title-ptbr: "{{display-title-ptbr}}"
author-ids:
  - "author:{{slug-autor}}"
autores:
  - "[[autor-{{slug-autor}}]]"
original-language: "{{original-language}}"
gbww-volume: {{gbww-volume}}
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/obra
  - type/canonico
aliases:
  - "{{display-title-ptbr}}"
  - "{{canonical-title}}"
status: em-desenvolvimento
created: 2026-09-17
modified: 2026-09-17
---

# {{display-title-ptbr}} (*{{canonical-title}}*)

> **Autoria:** [[autor-{{slug-autor}}|{{nome-autor}}]]  
> **Volume GBWW:** {{gbww-volume}} | **Idioma Original:** {{original-language}}  
> **Proveniência:** `provenance: original-corpus`

---

## 📖 I. VISÃO GERAL E CONTEXTO BIBLIOGRÁFICO
*(Apresentação da obra, data estimada de composição e sua relevância no cânone ocidental).*

---

## 🏛️ II. GRANDES IDEIAS DISCUTIDAS NA OBRA

```dataview
TABLE 
  topico as "Tópico Específico",
  locator as "Localizador (Locator Raw)",
  pagina as "Pág. Syntopicon"
FROM "03-referencias"
WHERE obra-id = this.id OR obra = this.file.link
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
