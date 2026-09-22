import os

topics = [
    {
        "id": "topico-42-1",
        "numero": "42.1",
        "en": "Diverse conceptions of justice",
        "pt": "Concepções diversas da justiça",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 1,
        "desc": "Panorama geral das definições concorrentes de justiça na tradição ocidental: da força ao dever moral e à utilidade."
    },
    {
        "id": "topico-42-1a",
        "numero": "42.1a",
        "en": "Justice as the interest of the stronger or conformity to the will of the sovereign",
        "pt": "Justiça como interesse do mais forte ou conformidade à vontade do soberano",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 2,
        "desc": "A tese cínica/realista e a ruptura juspositivista: Trasímaco, Hobbes e Spinoza."
    },
    {
        "id": "topico-42-1b",
        "numero": "42.1b",
        "en": "Justice as harmony or right order in the soul: original justice",
        "pt": "Justiça como harmonia ou ordem correta na alma: justiça original",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 3,
        "desc": "A justiça como ordem interior das faculdades da alma (Platão) e o conceito teológico de justiça original."
    },
    {
        "id": "topico-42-1c",
        "numero": "42.1c",
        "en": "Justice as a moral virtue directing activity in relation to others and to the community: the distinction between the just man and the just act",
        "pt": "Justiça como virtude moral que dirige a atividade em relação aos outros e à comunidade: distinção entre o homem justo e o ato justo",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 4,
        "desc": "A justiça como virtude cardeal relacional (ad alterum) em Aristóteles e Tomás de Aquino."
    },
    {
        "id": "topico-42-1d",
        "numero": "42.1d",
        "en": "Justice as the whole of virtue and as a particular virtue: the distinction between the lawful and the fair",
        "pt": "Justiça como a totalidade da virtude e como uma virtude particular: distinção entre o legal e o equitativo",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 5,
        "desc": "A clássica distinção aristotélica entre justiça geral/universal (obediência à lei) e justiça particular (o equitativo/justo)."
    },
    {
        "id": "topico-42-1e",
        "numero": "42.1e",
        "en": "Justice as an act of will or duty fulfilling obligations to the common good: the harmonious action of individual wills under a universal law of freedom",
        "pt": "Justiça como ato da vontade ou dever que cumpre obrigações para com o bem comum: ação harmoniosa das vontades individuais sob uma lei universal de liberdade",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 6,
        "desc": "A concepção deontológica da justiça e do direito em Kant e na tradição do dever moral."
    },
    {
        "id": "topico-42-1f",
        "numero": "42.1f",
        "en": "Justice as a custom or moral sentiment based on considerations of utility",
        "pt": "Justiça como costume ou sentimento moral baseado em considerações de utilidade",
        "pai": "topico-42-1", "raiz": "topico-42-1", "nivel": 2, "ordem": 7,
        "desc": "A fundamentação empírica e utilitarista da justiça: virtude artificial em Hume e utilidade social em Mill."
    },
    {
        "id": "topico-42-2",
        "numero": "42.2",
        "en": "The precepts of justice: doing good, harming no one, rendering to each his own, treating equals equally",
        "pt": "Os preceitos da justiça: fazer o bem, não prejudicar ninguém, dar a cada um o que lhe pertence, tratar igualmente os iguais",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 8,
        "desc": "As fórmulas e mandamentos axiais do direito e da moral clássica (neminem laedere, suum cuique tribuere)."
    },
    {
        "id": "topico-42-3",
        "numero": "42.3",
        "en": "The duties of justice compared with the generosity of love and friendship",
        "pt": "Os deveres da justiça comparados à generosidade do amor e da amizade",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 9,
        "desc": "O estritamente devido versus o dom imerecido: as fronteiras entre justiça, caritas, philia e misericórdia."
    },
    {
        "id": "topico-42-4",
        "numero": "42.4",
        "en": "The comparison of justice and expediency: the choice between doing and suffering injustice; the relation of justice to happiness",
        "pt": "A comparação entre justiça e conveniência: a escolha entre cometer e sofrer injustiça; a relação da justiça com a felicidade",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 10,
        "desc": "O paradoxo socrático do Górgias e da República: a integridade moral do agente versus o dano material sofrido."
    },
    {
        "id": "topico-42-5",
        "numero": "42.5",
        "en": "Justice and equality: the kinds of justice in relation to the measure and modes of equality and inequality",
        "pt": "Justiça e igualdade: os tipos de justiça em relação à medida e aos modos de igualdade e desigualdade",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 11,
        "desc": "A igualdade como critério da justiça: igualdade aritmética nas trocas/reparações versus proporção geométrica ao mérito na distribuição."
    },
    {
        "id": "topico-42-6",
        "numero": "42.6",
        "en": "Justice and liberty: the theory of human rights",
        "pt": "Justiça e liberdade: a teoria dos direitos humanos",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 12,
        "desc": "O ramo canônico do Syntopicon que articula a justiça com a doutrina dos direitos naturais e da liberdade civil."
    },
    {
        "id": "topico-42-6a",
        "numero": "42.6a",
        "en": "The relation of natural rights to natural law and natural justice",
        "pt": "A relação dos direitos naturais com a lei natural e a justiça natural",
        "pai": "topico-42-6", "raiz": "topico-42-6", "nivel": 2, "ordem": 13,
        "desc": "Fundamentação dos direitos subjetivos na lei moral natural anterior à ordem positiva estatal."
    },
    {
        "id": "topico-42-6b",
        "numero": "42.6b",
        "en": "The relation between natural and positive rights, innate and acquired rights, private and public rights: their correlative duties",
        "pt": "A relação entre direitos naturais e positivos, direitos inatos e adquiridos, direitos privados e públicos: seus deveres correlativos",
        "pai": "topico-42-6", "raiz": "topico-42-6", "nivel": 2, "ordem": 14,
        "desc": "Classificação jurídica e filosófica das categorias de direitos e sua correspondência com obrigações morais e civis."
    },
    {
        "id": "topico-42-6c",
        "numero": "42.6c",
        "en": "The inalienability of natural rights: their violation by tyranny and despotism",
        "pt": "A inalienabilidade dos direitos naturais: sua violação pela tirania e pelo despotismo",
        "pai": "topico-42-6", "raiz": "topico-42-6", "nivel": 2, "ordem": 15,
        "desc": "Limites morais do poder político: direitos que o indivíduo não pode alienar e que o soberano não pode violar."
    },
    {
        "id": "topico-42-6d",
        "numero": "42.6d",
        "en": "Justice as the basis of the distinction between liberty and license",
        "pt": "A justiça como base da distinção entre liberdade e licença",
        "pai": "topico-42-6", "raiz": "topico-42-6", "nivel": 2, "ordem": 16,
        "desc": "O critério da justiça impedindo que a liberdade degenere em arbítrio destrutivo ou lesão a terceiros."
    },
    {
        "id": "topico-42-6e",
        "numero": "42.6e",
        "en": "Justice and natural rights as the source of civil liberty",
        "pt": "Justiça e direitos naturais como fonte da liberdade civil",
        "pai": "topico-42-6", "raiz": "topico-42-6", "nivel": 2, "ordem": 17,
        "desc": "A passagem da liberdade natural à liberdade civil assegurada sob a constituição política justa."
    },
    {
        "id": "topico-42-7",
        "numero": "42.7",
        "en": "Domestic justice: the problems of right and duty in the family",
        "pt": "Justiça doméstica: os problemas de direito e dever na família",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 18,
        "desc": "Relações de autoridade, reciprocidade e dever entre cônjuges, pais e filhos na comunidade doméstica."
    },
    {
        "id": "topico-42-8",
        "numero": "42.8",
        "en": "Economic justice: justice in production, distribution, and exchange",
        "pt": "Justiça econômica: justiça na produção, distribuição e troca",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 19,
        "desc": "O grande ramo da filosofia prática que examina a ordem econômica sob a medida da justiça."
    },
    {
        "id": "topico-42-8a",
        "numero": "42.8a",
        "en": "Private and public property: the just distribution of economic goods",
        "pt": "Propriedade privada e pública: a distribuição justa dos bens econômicos",
        "pai": "topico-42-8", "raiz": "topico-42-8", "nivel": 2, "ordem": 20,
        "desc": "A legitimidade moral da apropriação privada, seus limites pelo bem comum e critérios distributivos."
    },
    {
        "id": "topico-42-8b",
        "numero": "42.8b",
        "en": "Fair wages and prices: the just exchange of goods and services",
        "pt": "Salários e preços justos: a troca justa de bens e serviços",
        "pai": "topico-42-8", "raiz": "topico-42-8", "nivel": 2, "ordem": 21,
        "desc": "A comutação econômica: do justo preço e salário medieval aos debates sobre remuneração do trabalho no mercado."
    },
    {
        "id": "topico-42-8c",
        "numero": "42.8c",
        "en": "Justice in the organization of production",
        "pt": "Justiça na organização da produção",
        "pai": "topico-42-8", "raiz": "topico-42-8", "nivel": 2, "ordem": 22,
        "desc": "Estruturas produtivas e relações sociais de trabalho: exploração versus cooperação livre."
    },
    {
        "id": "topico-42-8c-1",
        "numero": "42.8c(1)",
        "en": "Economic exploitation: chattel slavery and wage slavery",
        "pt": "Exploração econômica: escravidão como propriedade e escravidão assalariada",
        "pai": "topico-42-8c", "raiz": "topico-42-8", "nivel": 3, "ordem": 23,
        "desc": "GOLDEN CASE: A genealogia crítica da exploração do trabalho humano, de Aristóteles a Marx."
    },
    {
        "id": "topico-42-8c-2",
        "numero": "42.8c(2)",
        "en": "Profit and unearned increment",
        "pt": "Lucro e incremento não auferido",
        "pai": "topico-42-8c", "raiz": "topico-42-8", "nivel": 3, "ordem": 24,
        "desc": "A moralidade do ganho mercantil, renda da terra e apropriação de excedentes sem trabalho direto."
    },
    {
        "id": "topico-42-8d",
        "numero": "42.8d",
        "en": "Justice and the use of money: usury and interest rates",
        "pt": "Justiça e o uso do dinheiro: usura e taxas de juros",
        "pai": "topico-42-8", "raiz": "topico-42-8", "nivel": 2, "ordem": 25,
        "desc": "A controvérsia histórica sobre a esterilidade da moeda, a proibição escolástica da usura e a justificação moderna do crédito."
    },
    {
        "id": "topico-42-9",
        "numero": "42.9",
        "en": "Political justice: justice in government",
        "pt": "Justiça política: justiça no governo",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 26,
        "desc": "O ramo dedicado à justiça na constituição, no exercício do poder estatal e nas relações entre governantes e governados."
    },
    {
        "id": "topico-42-9a",
        "numero": "42.9a",
        "en": "The natural and the conventional in political justice: natural law and general will",
        "pt": "O natural e o convencional na justiça política: lei natural e vontade geral",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 27,
        "desc": "A tensão entre os padrões imutáveis da lei natural e as convenções políticas da soberania popular (Rousseau)."
    },
    {
        "id": "topico-42-9b",
        "numero": "42.9b",
        "en": "Justice as the moral principle of political organization: the bond of men in states",
        "pt": "Justiça como princípio moral da organização política: o vínculo dos homens nos Estados",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 28,
        "desc": "A justiça como argamassa da concórdia civil e condição para que o Estado não degenere em bando de salteadores."
    },
    {
        "id": "topico-42-9c",
        "numero": "42.9c",
        "en": "The criteria of justice in diverse forms of government and constitutions",
        "pt": "Os critérios de justiça nas diversas formas de governo e constituições",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 29,
        "desc": "Como monarquias, aristocracias, repúblicas e democracias justificam a legitimidade distributiva de suas ordens."
    },
    {
        "id": "topico-42-9d",
        "numero": "42.9d",
        "en": "The relation between ruler and ruled: the justice of the prince or statesman and of the subject or citizen",
        "pt": "A relação entre governante e governado: a justiça do príncipe ou estadista e do súdito ou cidadão",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 30,
        "desc": "Deveres de justiça do magistrado público e virtudes cívicas de obediência ou resistência do cidadão."
    },
    {
        "id": "topico-42-9e",
        "numero": "42.9e",
        "en": "The just distribution of honors, positions, offices, and suffrage",
        "pt": "A distribuição justa de honras, posições, cargos e sufrágio",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 31,
        "desc": "Justiça distributiva aplicada aos direitos políticos: quem tem direito a votar, governar e ser honrado."
    },
    {
        "id": "topico-42-9f",
        "numero": "42.9f",
        "en": "Justice between states: the problem of right and might in the making of war and peace",
        "pt": "Justiça entre Estados: o problema do direito e da força na realização da guerra e da paz",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 32,
        "desc": "Relações internacionais, teoria da guerra justa (ius ad bellum, ius in bello) e a ordem da paz."
    },
    {
        "id": "topico-42-9g",
        "numero": "42.9g",
        "en": "The tempering of political justice by clemency: amnesty, asylum, and pardon",
        "pt": "A moderação da justiça política pela clemência: anistia, asilo e perdão",
        "pai": "topico-42-9", "raiz": "topico-42-9", "nivel": 2, "ordem": 33,
        "desc": "A faculdade soberana de suspender o rigor punitivo estatal em benefício da reconciliação cívica e da humanidade."
    },
    {
        "id": "topico-42-10",
        "numero": "42.10",
        "en": "Justice and law",
        "pt": "Justiça e lei",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 34,
        "desc": "O nó fundamental da filosofia do direito: a relação entre a justiça substantiva e a norma positiva do Estado."
    },
    {
        "id": "topico-42-10a",
        "numero": "42.10a",
        "en": "The measure of justice in laws made by the state: natural and constitutional standards",
        "pt": "A medida da justiça nas leis feitas pelo Estado: padrões naturais e constitucionais",
        "pai": "topico-42-10", "raiz": "topico-42-10", "nivel": 2, "ordem": 35,
        "desc": "Os limites substanciais e constitucionais que impedem que a legislação positiva seja arbitrária."
    },
    {
        "id": "topico-42-10b",
        "numero": "42.10b",
        "en": "The legality of unjust laws: the extent of obedience required of the just man in the unjust society",
        "pt": "A legalidade das leis injustas: a extensão da obediência exigida do homem justo na sociedade injusta",
        "pai": "topico-42-10", "raiz": "topico-42-10", "nivel": 2, "ordem": 36,
        "desc": "O dilema moral e cívico: uma lei injusta obriga em consciência? Limites do dever de obediência e desobediência civil."
    },
    {
        "id": "topico-42-10c",
        "numero": "42.10c",
        "en": "The justice of punishment for unjust acts: the distinction between retribution and vengeance",
        "pt": "A justiça da punição por atos injustos: a distinção entre retribuição e vingança",
        "pai": "topico-42-10", "raiz": "topico-42-10", "nivel": 2, "ordem": 37,
        "desc": "Fundamentos da pena penal: retribuição moral proporcional versus vingança passional arbitrária."
    },
    {
        "id": "topico-42-10d",
        "numero": "42.10d",
        "en": "The correction of legal justice: equity in the administration of human law",
        "pt": "A correção da justiça legal: equidade na aplicação da lei humana",
        "pai": "topico-42-10", "raiz": "topico-42-10", "nivel": 2, "ordem": 38,
        "desc": "A equidade (epieikeia / aequitas) como corretivo essencial à imperfeição da lei universal diante do caso particular."
    },
    {
        "id": "topico-42-11",
        "numero": "42.11",
        "en": "Divine justice: the relation of God or the gods to man",
        "pt": "Justiça divina: a relação de Deus ou dos deuses com o homem",
        "pai": None, "raiz": None, "nivel": 1, "ordem": 39,
        "desc": "A dimensão teológica da justiça: providência cósmica, teodiceia e o mistério da retribuição transcendental."
    },
    {
        "id": "topico-42-11a",
        "numero": "42.11a",
        "en": "The divine government of man: the justice and mercy of God or the gods",
        "pt": "O governo divino do homem: a justiça e a misericórdia de Deus ou dos deuses",
        "pai": "topico-42-11", "raiz": "topico-42-11", "nivel": 2, "ordem": 40,
        "desc": "A conciliação entre a infalível justiça retributiva de Deus e a abundância de Sua misericórdia e graça salvífica."
    },
    {
        "id": "topico-42-11b",
        "numero": "42.11b",
        "en": "The debt of man to God or the gods: the religious acts of piety and worship",
        "pt": "A dívida do homem para com Deus ou os deuses: os atos religiosos de piedade e culto",
        "pai": "topico-42-11", "raiz": "topico-42-11", "nivel": 2, "ordem": 41,
        "desc": "A religião e a piedade como atos da virtude da justiça em relação ao Princípio Supremo a quem tudo se deve."
    }
]

VAULT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
out_dir = os.path.join(VAULT, "02-topicos/justica")
os.makedirs(out_dir, exist_ok=True)

# Build linear prev/next mapping
n = len(topics)
for i, t in enumerate(topics):
    prev_id = topics[i-1]["id"] if i > 0 else None
    next_id = topics[i+1]["id"] if i < n - 1 else None
    
    pai_link = f"[[{t['pai']}]]" if t['pai'] else "null"
    raiz_link = f"[[{t['raiz']}]]" if t['raiz'] else "null"
    
    prev_link = f"[[{prev_id}]]" if prev_id else "*(Primeiro nó do Outline)*"
    next_link = f"[[{next_id}]]" if next_id else "*(Último nó do Outline)*"
    
    content = f"""---
tipo: topico
numero-topico: "{t['numero']}"
ideia-mae: "[[gi-42-justica]]"
topico-pai: {pai_link}
topico-raiz: {raiz_link}
ordem: {t['ordem']}
nivel: {t['nivel']}
nome-en: "{t['en']}"
nome-pt: "{t['pt']}"
layer: canonical
tags:
  - type/structure
  - type/topico
  - theme/justica
aliases:
  - "{t['pt']}"
  - "{t['en']}"
  - "Tópico {t['numero']}"
status: em-desenvolvimento
created: 2026-09-16
modified: 2026-09-16
---

# Tópico {t['numero']}: {t['pt']}

> **Nome Original (EN):** *{t['en']}*  
> **Grande Ideia Mãe:** [[gi-42-justica|GI-42 Justiça]]  
> **Hierarquia:** Tópico Pai: {pai_link} | **Nível:** {t['nivel']} | **Camada:** `layer: canonical`

---

## 🟢 I. ENUNCIADO CANÔNICO (SYNTOPICON 1952)

> **Original (Mortimer J. Adler, *GBWW* Vol. 2, pp. 857–858):**  
> *"{t['en']}"*

> **Tradução Oficial de Trabalho:**  
> *"{t['pt']}"*

---

## 🟠 II. DELIMITAÇÃO CONCEITUAL & ESCOPO DIALÉTICO

{t['desc']}

---
"""

    # If golden case 8c(1), add rich content
    if t["id"] == "topico-42-8c-1":
        content += """## 🔵 III. REFERÊNCIAS CANÔNICAS DO GOLDEN CASE (1952)

O tópico **8c(1) — Exploração econômica** reúne 10 referências estruturadas de autoridade no corpus de 1952, articulando uma linhagem crítica sobre escravidão civil e servidão assalariada:

| Autor | Obra | Localizador (*Locator Raw*) | Vol. GBWW |
| :--- | :--- | :--- | :---: |
| [[autor-aristoteles\|Aristóteles]] | *Ética*, *Política*, *Constituição de Atenas* | Passagens sobre a escravidão natural e o trabalho servil | 9 |
| [[autor-plutarco\|Plutarco]] | *Vidas Paralelas* (*Licurgo*, *Marco Catão*) | O tratamento espartano aos hilotas e a economia escravista romana | 14 |
| [[autor-tomas-de-aquino\|Tomás de Aquino]] | *Suma Teológica* | II-II, questões econômicas sobre servidão e justiça comutativa | 20 |
| [[autor-john-milton\|John Milton]] | *Sansão Agonista* | O cativeiro forçado e a dignidade humana | 32 |
| [[autor-jean-jacques-rousseau\|Rousseau]] | *Discurso sobre a Origem da Desigualdade* | A gênese da propriedade privada e a sujeição dos despossuídos | 38 |
| [[autor-montesquieu\|Montesquieu]] | *Do Espírito das Leis* | Crítica das razões civis e políticas da escravidão | 38 |
| [[autor-adam-smith\|Adam Smith]] | *A Riqueza das Nações* | Ineficiência e crueldade do trabalho cativo; remuneração do assalariado | 39 |
| [[autor-immanuel-kant\|Immanuel Kant]] | *A Ciência do Direito* | A pessoa humana como fim em si mesma; repúdio à instrumentalização | 42 |
| [[autor-gwf-hegel\|G. W. F. Hegel]] | *Filosofia da História* | A dialética histórica da servidão e emancipação do espírito | 46 |
| [[autor-karl-marx\|Karl Marx]] | *O Capital* | A mais-valia, extração do trabalho excedente e escravidão assalariada | 50 |

---

## 🟠 IV. ESTRUTURAÇÃO SILOGÍSTICA DO DEBATE

### 🔵 [[autor-karl-marx|Karl Marx]]: [A Escravidão Assalariada no Modo de Produção Capitalista]
- **Tese Central:** A exploração econômica não é uma falha moral acidental do patrão, mas a condição estrutural objetiva sob a qual a mais-valia é extraída do trabalhador desprovido de meios de produção.
- **Estrutura Silogística:**
  1. *Premissa 1:* O valor de toda mercadoria é determinado pela quantidade de tempo de trabalho socialmente necessário para produzi-la.
  2. *Premissa 2:* Sob o contrato assalariado, o operário é remunerado apenas pelo valor necessário à sua subsistência (trabalho necessário), enquanto a jornada excedente (mais-trabalho) é apropriada pelo capitalista como mais-valia.
  3. *Conclusão:* Portanto, o contrato de trabalho formalmente "livre" oculta uma relação de exploração substantiva análoga à escravidão, na qual o excedente do trabalho é expropriado sem contraprestação equivalente.
"""
    elif t["id"] == "topico-42-1b":
        content += """## 🟠 III. ESTRUTURAÇÃO SILOGÍSTICA DO DEBATE

### 🔵 [[autor-platao|Platão]]: [A Justiça como Harmonia Funcional da Alma]
- **Tese Central:** A justiça não consiste na vantagem do mais forte ou em retaliação cega, mas na harmonia interior da alma — onde a faculdade racional governa o ânimo e modera o apetite.
- **Estrutura Silogística:**
  1. *Premissa 1:* Uma realidade composta atinge a saúde e a virtude quando cada uma de suas partes opera segundo sua excelência própria em concordância harmoniosa com o todo.
  2. *Premissa 2:* A alma humana é tripartite, dotada de razão, ânimo e apetites concupiscíveis.
  3. *Conclusão:* Portanto, a justiça é a virtude pela qual a razão dirige as potências inferiores, gerando a ordem espiritual interior que impede o agente de cometer atos iníquos.
"""
    elif t["id"] == "topico-42-1a":
        content += """## 🟠 III. ESTRUTURAÇÃO SILOGÍSTICA DO DEBATE

### 🔵 [[autor-thomas-hobbes|Thomas Hobbes]]: [A Justiça Fundada no Pacto Soberano]
- **Tese Central:** No estado de natureza inexiste justiça ou injustiça; a justiça nasce com a espada do Estado e consiste no cumprimento dos pactos válidos.
- **Estrutura Silogística:**
  1. *Premissa 1:* Onde não há lei civil pública e poder comum coercitivo que constranja a todos, todos os homens têm direito a todas as coisas, vigorando a guerra de todos contra todos.
  2. *Premissa 2:* A injustiça define-se estritamente como a ruptura culposa de um pacto civil válido.
  3. *Conclusão:* Portanto, a autoridade soberana civil é o fundamento da propriedade e da distinção pública entre o justo e o injusto.
"""
    else:
        content += """## 🟠 III. TESES E ARGUMENTOS DOS AUTORES (SILOGISMOS)
*(Espaço para os esquemas de Premissa 1, Premissa 2 e Conclusão das posições autorais específicas deste nó).*

---

## 🔵 IV. REFERÊNCIAS CANÔNICAS CATALOGADAS (CORPUS GBWW)

| Autor | Obra | Localizador (*Locator Raw*) | Vol. GBWW |
| :--- | :--- | :--- | :---: |
| *(A tabular a partir da ingestão do corpus)* | | | |
"""

    content += f"""---

## 📌 V. EXCERTOS E CITAÇÕES FICHADAS

```dataview
TABLE 
  autor as "Autor",
  obra as "Obra",
  locator as "Localizador",
  citacao as "Excerto"
FROM "05-citacoes"
WHERE contains(topico, this.file.link)
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
FROM "02-topicos/justica"
WHERE topico-pai = this.file.link
SORT ordem ASC
```

### Navegação Linear
← {prev_link} | **[[gi-42-justica|Ideia Central: Justiça]]** | {next_link} →
"""

    filepath = os.path.join(out_dir, f"{t['id']}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Sucesso: gerados todos os {len(topics)} nós de tópicos em {out_dir}")
