---
tipo: autor
id: "author:plutarch"
slug: "autor-plutarco"
canonicalName: "Plutarch"
displayNamePtBr: "Plutarco"
canonical-name: "Plutarch"
display-name-ptbr: "Plutarco"
period: "Antiguidade Greco-Romana (c. 46–119 d.C.)"
periodo: "Antiguidade Greco-Romana (c. 46–119 d.C.)"
tradition: "Platonismo Médio / Historiografia Moral"
tradicao: "Platonismo Médio / Historiografia Moral"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [14]
volumes-gbww: [14]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Plutarco"
  - "Plutarch"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Plutarco (Plutarch)

> **Período Histórico:** Antiguidade Greco-Romana (c. 46–119 d.C.)  
> **Tradição / Escola:** Platonismo Médio / Historiografia Moral  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Biógrafo e moralista grego, autor das Vidas Paralelas, retratou a sociedade espartana, a opressão dos hilotas e a gestão escravista no modelo agrário de Catão.

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
