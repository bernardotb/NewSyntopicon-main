---
tipo: passagem
id: "passage:{{id-estavel}}"
slug: "passagem-{{id-estavel}}"
obra-id: "work:{{slug-obra}}"
obra: "[[obra-{{slug-obra}}]]"
autor-id: "author:{{slug-autor}}"
autor: "[[autor-{{slug-autor}}]]"
topicos: []
referencias-origem-ids: []
referencias: []
edicao-consultada: "{{edicao-consultada}}"
volume-gbww: {{volume-gbww}}
locator-exato: "{{locator-exato}}"
idioma-original: "{{idioma-original}}"
idioma-traducao: "pt-BR"
tradutor: "{{tradutor}}"
evidencia-conferida: "{{evidencia-conferida}}"
provenance: original-corpus
epistemology: source
verification: verified
tags:
  - type/passagem
  - type/evidencia-textual
aliases:
  - "Passagem {{nome-autor}} - {{nome-obra}} ({{locator-exato}})"
status: verificado
created: 2026-09-17
modified: 2026-09-17
---

# Passagem: [[autor-{{slug-autor}}|{{nome-autor}}]] — *[[obra-{{slug-obra}}|{{nome-obra}}]]* (`{{locator-exato}}`)

> **Obra:** [[obra-{{slug-obra}}|{{nome-obra}}]] | **Autor:** [[autor-{{slug-autor}}|{{nome-autor}}]]  
> **Edição de Referência:** {{edicao-consultada}} | **Localização Exata:** `{{locator-exato}}`  
> **Status de Verificação:** `verification: verified` (Conferido contra a fonte primária)

---

## 📜 I. TEXTO ORIGINAL ({{idioma-original}})

> "{{texto-original}}"

---

## 🇧🇷 II. TRADUÇÃO CONFERIDA (PT-BR)

> "{{texto-traducao}}"
> — *Tradutor:* {{tradutor}} (*{{edicao-consultada}}*)

---

## 🔍 III. EVIDÊNCIA DE VERIFICAÇÃO DOCUMENTAL

- **Critério de Conferência:** {{evidencia-conferida}}
- **Referências do Syntopicon Correspondentes:**
```dataview
LIST
FROM "03-referencias"
WHERE contains(passagens-verificadas, this.id) OR id = this.referencias-origem-ids
```

---

## 🟠 IV. ANÁLISE FILOSÓFICA & CONTEXTO SINTÓPICO
*(Comentário da equipe editorial sobre o valor desta passagem para os tópicos do Syntopicon vinculados).*
