---
tipo: autor
id: "author:milton"
slug: "autor-john-milton"
canonicalName: "John Milton"
displayNamePtBr: "John Milton"
canonical-name: "John Milton"
display-name-ptbr: "John Milton"
period: "Idade Moderna / Renascimento Inglês (1608–1674)"
periodo: "Idade Moderna / Renascimento Inglês (1608–1674)"
tradition: "Humanismo Cristão / Republicanismo"
tradicao: "Humanismo Cristão / Republicanismo"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [32]
volumes-gbww: [32]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "John Milton"
  - "John Milton"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# John Milton (John Milton)

> **Período Histórico:** Idade Moderna / Renascimento Inglês (1608–1674)  
> **Tradição / Escola:** Humanismo Cristão / Republicanismo  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Poeta e polemista republicano inglês, retratou em Samson Agonistes a tragédia do cativeiro forçado, a dignidade violada do cativo e a libertação da servidão.

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
