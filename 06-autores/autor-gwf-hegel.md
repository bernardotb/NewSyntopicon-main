---
tipo: autor
id: "author:hegel"
slug: "autor-gwf-hegel"
canonicalName: "Georg Wilhelm Friedrich Hegel"
displayNamePtBr: "G. W. F. Hegel"
canonical-name: "Georg Wilhelm Friedrich Hegel"
display-name-ptbr: "G. W. F. Hegel"
period: "Idealismo Alemão (1770–1831)"
periodo: "Idealismo Alemão (1770–1831)"
tradition: "Idealismo Dialético"
tradicao: "Idealismo Dialético"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [46]
volumes-gbww: [46]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "G. W. F. Hegel"
  - "Georg Wilhelm Friedrich Hegel"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# G. W. F. Hegel (Georg Wilhelm Friedrich Hegel)

> **Período Histórico:** Idealismo Alemão (1770–1831)  
> **Tradição / Escola:** Idealismo Dialético  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Filósofo de Berlim, abordou na Filosofia da História a dialética do senhor e do servo e a realização progressiva da consciência da liberdade no devir dos povos.

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
