---
tipo: autor
id: "author:dostoevsky"
slug: "autor-fiodor-dostoievski"
canonicalName: "Fyodor Dostoevsky"
displayNamePtBr: "Fiódor Dostoiévski"
canonical-name: "Fyodor Dostoevsky"
display-name-ptbr: "Fiódor Dostoiévski"
period: "Realismo Psicológico Russo (1821–1881)"
periodo: "Realismo Psicológico Russo (1821–1881)"
tradition: "Filosofia da Existência / Cristianismo Ortodoxo"
tradicao: "Filosofia da Existência / Cristianismo Ortodoxo"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [52]
volumes-gbww: [52]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Fiódor Dostoiévski"
  - "Fyodor Dostoevsky"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Fiódor Dostoiévski (Fyodor Dostoevsky)

> **Período Histórico:** Realismo Psicológico Russo (1821–1881)  
> **Tradição / Escola:** Filosofia da Existência / Cristianismo Ortodoxo  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Escritor russo genial, analisou nos Irmãos Karamázov as raízes espirituais da exploração, o orgulho servil e a responsabilidade moral coletiva perante a dor dos desvalidos.

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
