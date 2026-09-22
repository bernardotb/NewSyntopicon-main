---
tipo: autor
id: "author:rousseau"
slug: "autor-jean-jacques-rousseau"
canonicalName: "Jean-Jacques Rousseau"
displayNamePtBr: "Jean-Jacques Rousseau"
canonical-name: "Jean-Jacques Rousseau"
display-name-ptbr: "Jean-Jacques Rousseau"
period: "Iluminismo Francês (1712–1778)"
periodo: "Iluminismo Francês (1712–1778)"
tradition: "Contratualismo / Teoria Crítica"
tradicao: "Contratualismo / Teoria Crítica"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [38]
volumes-gbww: [38]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Jean-Jacques Rousseau"
  - "Jean-Jacques Rousseau"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Jean-Jacques Rousseau (Jean-Jacques Rousseau)

> **Período Histórico:** Iluminismo Francês (1712–1778)  
> **Tradição / Escola:** Contratualismo / Teoria Crítica  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Pensador genebrino fundamental, investigou no Discurso sobre a Desigualdade a gênese da escravidão e da submissão originadas com a apropriação da terra e a divisão do trabalho.

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
