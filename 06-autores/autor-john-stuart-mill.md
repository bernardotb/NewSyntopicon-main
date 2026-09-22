---
tipo: autor
id: "author:mill"
slug: "autor-john-stuart-mill"
canonicalName: "John Stuart Mill"
displayNamePtBr: "John Stuart Mill"
canonical-name: "John Stuart Mill"
display-name-ptbr: "John Stuart Mill"
period: "Século XIX (1806–1873)"
periodo: "Século XIX (1806–1873)"
tradition: "Utilitarismo / Liberalismo Político"
tradicao: "Utilitarismo / Liberalismo Político"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [43]
volumes-gbww: [43]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "John Stuart Mill"
  - "John Stuart Mill"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# John Stuart Mill (John Stuart Mill)

> **Período Histórico:** Século XIX (1806–1873)  
> **Tradição / Escola:** Utilitarismo / Liberalismo Político  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Filósofo e economista britânico, analisou em Considerações sobre o Governo Representativo a incompatibilidade da servidão humana com o progresso civilizatório e democrático.

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
