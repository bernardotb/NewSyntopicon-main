---
tipo: autor
id: "author:swift"
slug: "autor-jonathan-swift"
canonicalName: "Jonathan Swift"
displayNamePtBr: "Jonathan Swift"
canonical-name: "Jonathan Swift"
display-name-ptbr: "Jonathan Swift"
period: "Iluminismo Britânico (1667–1745)"
periodo: "Iluminismo Britânico (1667–1745)"
tradition: "Sátira Moral e Política"
tradicao: "Sátira Moral e Política"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [36]
volumes-gbww: [36]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Jonathan Swift"
  - "Jonathan Swift"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Jonathan Swift (Jonathan Swift)

> **Período Histórico:** Iluminismo Britânico (1667–1745)  
> **Tradição / Escola:** Sátira Moral e Política  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Escritor anglo-irlandês, utilizou a alegoria dos Houyhnhnms e Yahoos em As Viagens de Gulliver para fustigar a degradação e servidão moral humana.

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
