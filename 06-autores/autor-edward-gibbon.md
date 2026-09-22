---
tipo: autor
id: "author:gibbon"
slug: "autor-edward-gibbon"
canonicalName: "Edward Gibbon"
displayNamePtBr: "Edward Gibbon"
canonical-name: "Edward Gibbon"
display-name-ptbr: "Edward Gibbon"
period: "Iluminismo Inglês (1737–1794)"
periodo: "Iluminismo Inglês (1737–1794)"
tradition: "Historiografia Moderna"
tradicao: "Historiografia Moderna"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [40, 41]
volumes-gbww: [40, 41]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Edward Gibbon"
  - "Edward Gibbon"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Edward Gibbon (Edward Gibbon)

> **Período Histórico:** Iluminismo Inglês (1737–1794)  
> **Tradição / Escola:** Historiografia Moderna  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Historiador britânico monumental, documentou a economia escravocrata do Império Romano e sua relação com a dissolução cívica e política em Declínio e Queda.

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
