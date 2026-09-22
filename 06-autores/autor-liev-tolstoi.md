---
tipo: autor
id: "author:tolstoy"
slug: "autor-liev-tolstoi"
canonicalName: "Leo Tolstoy"
displayNamePtBr: "Liev Tolstói"
canonical-name: "Leo Tolstoy"
display-name-ptbr: "Liev Tolstói"
period: "Realismo Russo (1828–1910)"
periodo: "Realismo Russo (1828–1910)"
tradition: "Romance Histórico / Anarquismo Cristão"
tradicao: "Romance Histórico / Anarquismo Cristão"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [51]
volumes-gbww: [51]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Liev Tolstói"
  - "Leo Tolstoy"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Liev Tolstói (Leo Tolstoy)

> **Período Histórico:** Realismo Russo (1828–1910)  
> **Tradição / Escola:** Romance Histórico / Anarquismo Cristão  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Romancista russo, expôs em Guerra e Paz a estrutura feudal da servidão russa e a inquietação moral da nobreza diante da posse de outros seres humanos.

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
