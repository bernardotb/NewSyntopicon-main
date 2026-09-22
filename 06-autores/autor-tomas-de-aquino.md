---
tipo: autor
id: "author:aquinas"
slug: "autor-tomas-de-aquino"
canonicalName: "Thomas Aquinas"
displayNamePtBr: "Tomás de Aquino"
canonical-name: "Thomas Aquinas"
display-name-ptbr: "Tomás de Aquino"
period: "Escolástica Medieval (1225–1274)"
periodo: "Escolástica Medieval (1225–1274)"
tradition: "Filosofia Escolástica / Tomismo"
tradicao: "Filosofia Escolástica / Tomismo"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [19, 20]
volumes-gbww: [19, 20]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Tomás de Aquino"
  - "Thomas Aquinas"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Tomás de Aquino (Thomas Aquinas)

> **Período Histórico:** Escolástica Medieval (1225–1274)  
> **Tradição / Escola:** Filosofia Escolástica / Tomismo  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Doutor da Igreja e teólogo dominicano, sistematizou o conceito de lei natural, a justiça comutativa e a legitimidade jurídica e moral da servidão no direito das gentes.

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
