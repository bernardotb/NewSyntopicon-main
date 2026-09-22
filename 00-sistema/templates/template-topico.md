---
tipo: topico
id: "topic:{{slug-ideia}}:{{codigo-slug}}"
slug: "topico-{{numero-ideia}}-{{codigo-slug}}"
ideia-id: "idea:{{slug-ideia}}"
ideia-mae: "[[gi-{{numero-ideia}}-{{slug-ideia}}]]"
topico-pai: "{{topico-pai}}"
topico-raiz: "{{topico-raiz}}"
codigo-original: "{{codigo-original}}"
ordem: {{ordem}}
nivel: {{nivel}}
nome-en: "{{nome-en}}"
nome-pt: "{{nome-pt}}"
provenance: original-corpus
epistemology: canonical
verification: verified
source-id: syntopicon-1952
tags:
  - type/structure
  - type/topico
  - theme/{{slug-ideia}}
aliases:
  - "{{nome-pt}}"
  - "{{nome-en}}"
  - "Tópico {{codigo-original}}"
status: em-desenvolvimento
created: 2026-09-17
modified: 2026-09-17
---

# Tópico {{codigo-original}}: {{nome-pt}}

> **Nome Original (EN):** *{{nome-en}}*  
> **Grande Ideia Mãe:** [[gi-{{numero-ideia}}-{{slug-ideia}}|GI-{{numero-ideia}} {{nome-pt-ideia}}]]  
> **Hierarquia:** Tópico Pai: {{topico-pai}} | **Nível:** {{nivel}} | **Ordem:** {{ordem}}

---

## 🟢 I. ENUNCIADO CANÔNICO (SYNTOPICON 1952)

> **Original (Mortimer J. Adler, *GBWW* Vol. [X], pp. [Y–Z]):**  
> *"{{nome-en}}"*

> **Tradução Oficial de Trabalho:**  
> *"{{nome-pt}}"*

---

## 🟠 II. DELIMITAÇÃO CONCEITUAL & ESCOPO DIALÉTICO
*(Espaço para delimitação do problema específico investigado por este nó e sua distinção analítica em relação aos tópicos irmãos).*

---

## 🟠 III. TESES E ARGUMENTOS DOS AUTORES (SILOGISMOS)

### 🔵 [[autor-nome]]: [Posição no Tópico]
- **Tese Central:** 
- **Estrutura Silogística:**
  1. *Premissa 1:* 
  2. *Premissa 2:* 
  3. *Conclusão:* 
- **Significado Histórico / Dialético:**

---

## 🔵 IV. REFERÊNCIAS CANÔNICAS DO SYNTOPICON (CORPUS GBWW)

```dataview
TABLE 
  autor as "Autor",
  obra as "Obra",
  locator as "Localizador (Locator Raw)",
  pagina as "Pág. Syntopicon"
FROM "03-referencias"
WHERE contains(topico, this.file.link) OR topico-id = this.id
SORT ordem ASC
```

---

## 📌 V. PASSAGENS LITERAIS VERIFICADAS

```dataview
TABLE 
  autor as "Autor",
  obra as "Obra",
  locator-exato as "Localização Exata",
  traducao as "Excerto (PT-BR)"
FROM "04-passagens"
WHERE contains(topicos, this.file.link)
SORT autor ASC
```

---

## 🧠 VI. NOTAS DE ESTUDO & OBSERVAÇÕES PESSOAIS
*(Espaço reservado para as reflexões e anotações atômicas do estudante).*

---

## 🔗 VII. NAVEGAÇÃO HIERÁRQUICA

### Tópicos Descendentes
```dataview
LIST
FROM "02-topicos"
WHERE topico-pai = this.file.link
SORT ordem ASC
```

### Navegação Linear
← [[topico-anterior|Tópico Anterior]] | **[[gi-{{numero-ideia}}-{{slug-ideia}}|Ideia Central]]** | [[topico-seguinte|Tópico Seguinte]] →
