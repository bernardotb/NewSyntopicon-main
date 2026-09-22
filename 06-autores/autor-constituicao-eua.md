---
tipo: autor
id: "author:founding-fathers-us"
slug: "autor-constituicao-eua"
canonicalName: "Constitution of the United States"
displayNamePtBr: "Constituição dos Estados Unidos"
canonical-name: "Constitution of the United States"
display-name-ptbr: "Constituição dos Estados Unidos"
period: "Constitucionalismo Moderno (1787–1865)"
periodo: "Constitucionalismo Moderno (1787–1865)"
tradition: "Jusconstitucionalismo e Direitos Fundamentais"
tradicao: "Jusconstitucionalismo e Direitos Fundamentais"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [43]
volumes-gbww: [43]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Constituição dos Estados Unidos"
  - "Constitution of the United States"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Constituição dos Estados Unidos (Constitution of the United States)

> **Período Histórico:** Constitucionalismo Moderno (1787–1865)  
> **Tradição / Escola:** Jusconstitucionalismo e Direitos Fundamentais  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Texto normativo fundacional norte-americano, registrando as tensões e compromissos sobre a escravidão (Artigo I, Seção 9; Artigo IV, Seção 2) e sua abolição na XIII Emenda (1865).

---

## 📚 II. OBRAS DO AUTOR NO ECOSSISTEMA

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
