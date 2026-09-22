---
tipo: autor
id: "author:{{slug-autor}}"
slug: "autor-{{slug-autor}}"
canonical-name: "{{canonical-name}}"
display-name-ptbr: "{{display-name-ptbr}}"
periodo: "{{periodo}}"
tradicao: "{{tradicao}}"
is-gbww-canonical: true
volumes-gbww: []
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "{{display-name-ptbr}}"
  - "{{canonical-name}}"
status: em-desenvolvimento
created: 2026-09-17
modified: 2026-09-17
---

# {{display-name-ptbr}} ({{canonical-name}})

> **Período Histórico:** {{periodo}}  
> **Tradição / Escola:** {{tradicao}}  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 📚 I. OBRAS DO AUTOR NO ECOSSISTEMA

```dataview
TABLE 
  displayTitlePtBr as "Título da Obra",
  gbwwVolume as "Volume GBWW",
  originalLanguage as "Idioma Original"
FROM "05-obras"
WHERE contains(authorIds, this.id) OR author = this.file.link
SORT gbwwVolume ASC
```

---

## 🏛️ II. CONTRIBUIÇÕES À GRANDE CONVERSA
*(Contextualização da posição do pensador nas 102 Grandes Ideias do Ocidente).*

---

## 📌 III. PASSAGENS CITADAS (DATAVIEW)

```dataview
TABLE 
  obra as "Obra",
  locator-exato as "Localização",
  traducao as "Excerto"
FROM "04-passagens"
WHERE autor-id = this.id OR autor = this.file.link
SORT obra ASC
LIMIT 20
```
