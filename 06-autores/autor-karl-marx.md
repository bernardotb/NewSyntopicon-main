---
tipo: autor
id: "author:marx"
slug: "autor-karl-marx"
canonicalName: "Karl Marx"
displayNamePtBr: "Karl Marx"
canonical-name: "Karl Marx"
display-name-ptbr: "Karl Marx"
period: "Século XIX (1818–1883)"
periodo: "Século XIX (1818–1883)"
tradition: "Materialismo Histórico / Crítica da Economia Política"
tradicao: "Materialismo Histórico / Crítica da Economia Política"
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
  - "Karl Marx"
  - "Karl Marx"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Karl Marx (Karl Marx)

> **Período Histórico:** Século XIX (1818–1883)  
> **Tradição / Escola:** Materialismo Histórico / Crítica da Economia Política  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Pensador revolucionário e economista alemão, dissecou em O Capital a escravidão assalariada, demonstrando que o contrato salarial formalmente livre mascara a apropriação compulsória da mais-valia.

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
