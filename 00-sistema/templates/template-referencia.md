---
tipo: referencia
id: "ref:{{slug-ideia}}:{{id-estavel}}"
slug: "ref-{{numero-ideia}}-{{id-estavel}}"
ideia-id: "idea:{{slug-ideia}}"
topico-id: "topic:{{slug-ideia}}:{{codigo-topico}}"
topico: "[[topico-{{numero-ideia}}-{{codigo-topico}}]]"
autor-id: "author:{{slug-autor}}"
autor: "[[autor-{{slug-autor}}]]"
obra-id: "work:{{slug-obra}}"
obra: "[[obra-{{slug-obra}}]]"
gbww-volume: {{volume-gbww}}
pagina-syntopicon: {{pagina-syntopicon}}
locator-raw: "{{locator-raw}}"
ordem-no-topico: {{ordem}}
passagens-verificadas: []
provenance: original-corpus
epistemology: canonical
verification: needs_verification
source-id: syntopicon-1952
tags:
  - type/referencia
  - type/documental
aliases:
  - "Ref {{numero-ideia}}.{{codigo-topico}} - {{nome-autor}} ({{nome-obra}})"
status: em-desenvolvimento
created: 2026-09-17
modified: 2026-09-17
---

# Referência: [[autor-{{slug-autor}}|{{nome-autor}}]], *[[obra-{{slug-obra}}|{{nome-obra}}]]*

> **Tópico Canônico:** [[topico-{{numero-ideia}}-{{codigo-topico}}|Tópico {{codigo-topico}}]]  
> **Volume GBWW:** {{volume-gbww}} | **Página no Syntopicon (1952):** {{pagina-syntopicon}}  
> **Localizador Bruto (*Locator Raw*):** `{{locator-raw}}`

---

## 🟢 I. APONTAMENTO DOCUMENTAL DO SYNTOPICON (1952)

> **Entrada Impressa:**  
> `{{nome-autor}}: {{nome-obra}}, {{locator-raw}}`

---

## 🔵 II. PASSAGENS LITERAIS VINCULADAS

```dataview
TABLE 
  locator-exato as "Localizador Exato",
  traducao as "Texto em Português",
  verification as "Status de Conferência"
FROM "04-passagens"
WHERE contains(referencia-origem-id, this.id) OR contains(referencias, this.file.link)
```

---

## 🟠 III. NOTAS CONTEXTUAIS E FILOLÓGICAS
*(Espaço para registrar variantes de tradução, problemas de OCR na leitura do locator ou correspondência entre capítulos da obra).*
