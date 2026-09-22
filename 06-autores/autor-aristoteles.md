---
tipo: autor
id: "author:aristotle"
slug: "autor-aristoteles"
canonicalName: "Aristotle"
displayNamePtBr: "Aristóteles"
canonical-name: "Aristotle"
display-name-ptbr: "Aristóteles"
period: "Antiguidade Clássica (384–322 a.C.)"
periodo: "Antiguidade Clássica (384–322 a.C.)"
tradition: "Filosofia Grega Antiga / Peripatética"
tradicao: "Filosofia Grega Antiga / Peripatética"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [8, 9]
volumes-gbww: [8, 9]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Aristóteles"
  - "Aristotle"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Aristóteles (Aristotle)

> **Período Histórico:** Antiguidade Clássica (384–322 a.C.)  
> **Tradição / Escola:** Filosofia Grega Antiga / Peripatética  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Filósofo grego cujas investigações em ética e política formularam a teoria clássica da justiça distributiva e comutativa, bem como a defesa e os limites da escravidão natural.

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
