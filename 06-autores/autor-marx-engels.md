---
tipo: autor
id: "author:marx-engels"
slug: "autor-marx-engels"
canonicalName: "Karl Marx & Friedrich Engels"
displayNamePtBr: "Karl Marx & Friedrich Engels"
canonical-name: "Karl Marx & Friedrich Engels"
display-name-ptbr: "Karl Marx & Friedrich Engels"
period: "Século XIX (1818–1895)"
periodo: "Século XIX (1818–1895)"
tradition: "Socialismo Científico"
tradicao: "Socialismo Científico"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [50]
volumes-gbww: [50]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Karl Marx & Friedrich Engels"
  - "Karl Marx & Friedrich Engels"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Karl Marx & Friedrich Engels (Karl Marx & Friedrich Engels)

> **Período Histórico:** Século XIX (1818–1895)  
> **Tradição / Escola:** Socialismo Científico  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Autoria conjunta fundacional da teoria revolucionária, proclamou no Manifesto Comunista a luta de classes e a necessidade de superação de todas as formas de exploração do homem pelo homem.

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
