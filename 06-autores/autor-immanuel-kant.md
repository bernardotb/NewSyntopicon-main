---
tipo: autor
id: "author:kant"
slug: "autor-immanuel-kant"
canonicalName: "Immanuel Kant"
displayNamePtBr: "Immanuel Kant"
canonical-name: "Immanuel Kant"
display-name-ptbr: "Immanuel Kant"
period: "Iluminismo Alemão (1724–1804)"
periodo: "Iluminismo Alemão (1724–1804)"
tradition: "Filosofia Crítica / Deontologia"
tradicao: "Filosofia Crítica / Deontologia"
isGbwwCanonical: true
is-gbww-canonical: true
gbwwVolumes: [42]
volumes-gbww: [42]
provenance: original-corpus
epistemology: source
verification: verified
source-id: syntopicon-1952
tags:
  - type/autor
  - type/biografia
aliases:
  - "Immanuel Kant"
  - "Immanuel Kant"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Immanuel Kant (Immanuel Kant)

> **Período Histórico:** Iluminismo Alemão (1724–1804)  
> **Tradição / Escola:** Filosofia Crítica / Deontologia  
> **Status Canônico:** Autor integrante da coleção *Great Books of the Western World* (GBWW).

---

## 🏛️ I. CONTRIBUIÇÕES À GRANDE CONVERSA
Filósofo de Königsberg, formulou na Ciência do Direito a inviolabilidade da pessoa humana como fim em si mesma, vedando juridicamente a redução do homem a coisa ou mera mercadoria.

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
