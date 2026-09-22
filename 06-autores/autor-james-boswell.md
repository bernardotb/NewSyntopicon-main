---
tipo: autor
id: "author:boswell"
slug: "autor-james-boswell"
canonicalName: "James Boswell"
displayNamePtBr: "James Boswell"
canonical-name: "James Boswell"
display-name-ptbr: "James Boswell"
period: "Século XVIII (1740–1795)"
periodo: "Século XVIII (1740–1795)"
tradition: "Biografia Literária Britânica"
tradicao: "Biografia Literária Britânica"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [44]
volumes-gbww: [44]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "James Boswell"
  - "James Boswell"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# James Boswell (James Boswell)

> **Período Histórico:** Século XVIII (1740–1795)  
> **Tradição / Escola:** Biografia Literária Britânica  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Autor escocês, retratou a vida e os diálogos de Samuel Johnson, documentando os debates éticos e jurídicos do século XVIII contra o tráfico de escravos.

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
