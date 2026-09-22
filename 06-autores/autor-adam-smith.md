---
tipo: autor
id: "author:smith"
slug: "autor-adam-smith"
canonicalName: "Adam Smith"
displayNamePtBr: "Adam Smith"
canonical-name: "Adam Smith"
display-name-ptbr: "Adam Smith"
period: "Iluminismo Escocês (1723–1790)"
periodo: "Iluminismo Escocês (1723–1790)"
tradition: "Economia Política Clássica / Filosofia Moral"
tradicao: "Economia Política Clássica / Filosofia Moral"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [39]
volumes-gbww: [39]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Adam Smith"
  - "Adam Smith"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Adam Smith (Adam Smith)

> **Período Histórico:** Iluminismo Escocês (1723–1790)  
> **Tradição / Escola:** Economia Política Clássica / Filosofia Moral  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Pioneiro da economia política clássica, demonstrou em A Riqueza das Nações a ineficiência econômica e a crueldade da escravidão, analisando as condições do trabalho assalariado.

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
