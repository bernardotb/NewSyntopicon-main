---
tipo: volume
id: "volume:gbww-{{ano}}-{{numero-volume-pad}}"
slug: "volume-gbww-{{ano}}-{{numero-volume-pad}}"
numero-volume: {{numero-volume}}
edicao-ano: {{ano}}
colecao: "Great Books of the Western World"
editora: "Encyclopædia Britannica, Inc."
titulo-volume: "{{titulo-volume}}"
total-obras: {{total-obras}}
autores-inclusos: []
obras-inclusas: []
provenance: original-corpus
epistemology: canonical
verification: verified
source-id: "source:gbww-{{ano}}"
tags:
  - type/volume
  - type/bibliografia
aliases:
  - "GBWW Volume {{numero-volume}} ({{ano}})"
  - "Volume {{numero-volume}}"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Volume {{numero-volume}} — {{titulo-volume}} (GBWW {{ano}})

> **Coleção:** *Great Books of the Western World* ({{ano}})  
> **Identificador:** `volume:gbww-{{ano}}-{{numero-volume-pad}}`  
> **Total de Obras:** {{total-obras}}

---

## 📚 I. AUTORES E OBRAS PRESENTES NESTE VOLUME

```dataview
TABLE 
  author as "Autor(es)",
  displayTitlePtBr as "Título da Obra (PT)",
  canonicalTitle as "Título Original"
FROM "05-obras"
WHERE gbww-volume = this.numero-volume
SORT file.name ASC
```

---

## 🏛️ II. NOTAS DE CONSULTA E CONFERÊNCIA
*(Registro de notas sobre a tradução adotada na Britannica de 1952, numeração de páginas ou divisões internas).*
