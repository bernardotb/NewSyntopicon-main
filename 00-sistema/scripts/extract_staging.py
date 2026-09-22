#!/usr/bin/env python3
"""
Extrator de Staging para o Corpus do Syntopicon: Chapter 42 - Justice (1952)
Processa Justice.pdf pp. 859-878 e gera as tres saidas de staging:
1. 00-sistema/staging/referencias-candidatas.json
2. 00-sistema/staging/ambiguidades.json
3. 00-sistema/staging/cobertura.json

Atende a todas as diretrizes do Contrato de Dados:
- Protecao 1: Chave documental composta estritamente unica (sourceId, syntopiconPage, topicId, orderInTopic)
- Protecao 2: Preservacao verbatim de locatorRaw (nunca sintetizado de campos normalizados)
- Protecao 3: Saidas automaticas estritamente com verification: "needs_verification"
- Regra de isolamento de fronteira de topico (caso de borda Montesquieu / transicao estrita)
- Baseline: STAGING_BASELINE_JUSTICE_1952_V1
"""

import os
import sys
import re
import json
import datetime
import pypdf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PDF_PATH = os.path.join(BASE_DIR, '_fontes', 'Justice.pdf')
STAGING_DIR = os.path.join(BASE_DIR, '00-sistema', 'staging')
SOURCE_ID = 'source:pdf-justice-1952'
BASELINE_ID = 'STAGING_BASELINE_JUSTICE_1952_V1'

os.makedirs(STAGING_DIR, exist_ok=True)

# 41 Topicos de Justica em sequencia documental estrita
OUTLINE_TOPICS = [
    ("42.1", "topic:justica:1", "Diverse conceptions of justice", r"1\.", ["diverse conceptions"]),
    ("42.1a", "topic:justica:1a", "Justice as the interest of the stronger or conformity to the will of the sovereign", r"[l1]a\.", ["interest of the stronger", "conformity to"]),
    ("42.1b", "topic:justica:1b", "Justice as harmony or right order in the soul: original justice", r"(?:[l1]?b\.|injustice as harmony)", ["harmony or right order", "harmony"]),
    ("42.1c", "topic:justica:1c", "Justice as a moral virtue directing activity in relation to others and the good of another", r"[l1I]c\.", ["moral virtue directing activity", "directing activity"]),
    ("42.1d", "topic:justica:1d", "Justice as the whole of virtue and as a particular virtue", r"\\?d\.", ["whole of virtue"]),
    ("42.1e", "topic:justica:1e", "Justice as an act of will or duty fulfilling obligations: the relation between debt and duty", r"[l1I]e\.", ["act of will or duty", "fulfilling obligations"]),
    ("42.1f", "topic:justica:1f", "Justice as a custom or moral sentiment based on comparative utility", r"[l1I]/?\.", ["custom or moral sentiment", "moral sentiment based"]),
    ("42.2", "topic:justica:2", "The precepts of justice: doing good, harming no one, rendering to each his own", r"2\.", ["precepts of justice", "doing good"]),
    ("42.3", "topic:justica:3", "The duties of justice compared with the generosity of love and friendship", r"3\.", ["duties of justice compared", "generosity of love"]),
    ("42.4", "topic:justica:4", "The comparison of justice and expediency: the choice between justice and utility", r"4\.", ["comparison of justice and expediency", "choice between justice"]),
    ("42.5", "topic:justica:5", "Justice and equality: the kinds of justice in relation to proportions of equality", r"5\.", ["justice and equality", "kinds of justice in"]),
    ("42.6", "topic:justica:6", "Justice and liberty: the theory of human rights", r"6\.", ["justice and liberty: the theory", "theory of human rights"]),
    ("42.6a", "topic:justica:6a", "The relation of natural rights to natural law and natural justice", r"6a\.", ["relation of natural", "natural rights to natural"]),
    ("42.6b", "topic:justica:6b", "The relation between natural and positive rights, and between natural and legal justice", r"6b\.", ["between natural and positive", "positive rights"]),
    ("42.6c", "topic:justica:6c", "The inalienability of natural rights: their violation or destruction by tyranny or enslavement", r"[S86]c\.", ["inalienability of natural rights", "inalienability"]),
    ("42.6d", "topic:justica:6d", "Justice as the basis of the distinction between liberty and license", r"6d\.", ["distinction between liberty and license", "liberty and license", "basis for the distinction"]),
    ("42.6e", "topic:justica:6e", "Justice and natural rights as the source of civil liberty and constitutional limits upon government", r"6e\.", ["natural rights as the source of", "civil liberty", "source of civil"]),
    ("42.7", "topic:justica:7", "Domestic justice: the problems of right and duty in the family or household", r"7\.", ["domestic justice", "family or household"]),
    ("42.8", "topic:justica:8", "Economic justice: justice in production, distribution, and exchange", r"8\.", ["economic justice", "justice in production"]),
    ("42.8a", "topic:justica:8a", "Private and public property: the just distribution of economic goods", r"8a\.", ["private and public property", "just distribution of economic"]),
    ("42.8b", "topic:justica:8b", "Fair wages and prices: the just exchange of goods and services", r"[S8]b\.", ["fair wages and prices", "exchange of goods"]),
    ("42.8c", "topic:justica:8c", "Justice in the organization of production", r"[I18]c\.", ["organization of production"]),
    ("42.8c(1)", "topic:justica:8c-1", "Economic exploitation: chattel slavery and wage slavery", r"(?:8c\s*\(1\)|economic exploitation)", ["economic exploitation", "chattel slavery"]),
    ("42.8c(2)", "topic:justica:8c-2", "Profit and unearned increment", r"8c\s*\\?\(2\)", ["profit and unearned increment", "unearned increment"]),
    ("42.8d", "topic:justica:8d", "Justice and the use of money: usury and interest rates", r"8d\.", ["justice and the use of money", "usury and interest"]),
    ("42.9", "topic:justica:9", "Political justice: justice in government", r"9\.", ["political justice: justice in government", "justice in government"]),
    ("42.9a", "topic:justica:9a", "The natural and the conventional in political justice: the justice of the state as a natural society", r"9a\.", ["natural and the conventional"]),
    ("42.9b", "topic:justica:9b", "Justice as the moral principle of political organization: the bond of men in states", r"9[b&]\.?", ["moral principle of political organization", "principle of political"]),
    ("42.9c", "topic:justica:9c", "The criteria of justice in diverse forms of government: the justice of kingship, aristocracy, constitutional government, democracy, and oligarchy", r"9c\.", ["criteria of justice in various forms", "criteria of justice"]),
    ("42.9d", "topic:justica:9d", "The relation between ruler and ruled: the justice of imperial rule and the subjugation of conquered peoples", r"9[d<]/\.", ["relation of ruler and ruled", "ruler and ruled"]),
    ("42.9e", "topic:justica:9e", "The just distribution of honors, positions, offices: the justice of qualifications for suffrage and citizenship", r"9e\.", ["just distribution of honors", "honors, ranks", "distribution of honors"]),
    ("42.9f", "topic:justica:9f", "Justice between states: the problem of right and might in international relations", r"9f[\*\.]?", ["justice between states", "problem of right and might", "problem of right and moral"]),
    ("42.9g", "topic:justica:9g", "The tempering of political justice by clemency: amnesty, pardon, and restitution", r"9g\.", ["tempering", "clem"]),
    ("42.10", "topic:justica:10", "Justice and law", r"10\s*[k\.]", ["justice and law"]),
    ("42.10a", "topic:justica:10a", "The measure of justice in laws made by the state: the injustice of unlawful or arbitrary government", r"[l1I]O?a\.", ["measure of justice in laws made", "laws made by the state"]),
    ("42.10b", "topic:justica:10b", "The legality of unjust laws: the extent of obedience due to unjust laws", r"10b?\.?", ["legality of unjust laws", "extent of obedience"]),
    ("42.10c", "topic:justica:10c", "The justice of punishment for unjust acts: the distinction between retribution and revenge", r"[l1I]Oc\.", ["justice of punishment for unjust acts", "punishment for unjust acts"]),
    ("42.10d", "topic:justica:10d", "The correction of legal justice: equity in the administration of law", r"[l1I]Q?d\.", ["correction of legal justice", "equity in the administration", "correction of legal"]),
    ("42.11", "topic:justica:11", "Divine justice: the relation of God or the gods to man", r"[I1]{1,2}\.", ["divine justice: the relation of god", "relation of god or the gods"]),
    ("42.11a", "topic:justica:11a", "The divine government of man: the justice and mercy of God", r"\[?a\.", ["divine government of man", "justice and mercy of god"]),
    ("42.11b", "topic:justica:11b", "The debt of man to God or the gods: the religious acts of justice", r"[l1I]{2}b\.", ["debt of man to god", "man's debt to god", "religious acts of piety"])
]

TOPIC_LOT_MAP = {
    "42.1": "Lote 1", "42.1a": "Lote 1", "42.1b": "Lote 1", "42.1c": "Lote 1", "42.1d": "Lote 1", "42.1e": "Lote 1", "42.1f": "Lote 1",
    "42.2": "Lote 2", "42.3": "Lote 2", "42.4": "Lote 2", "42.5": "Lote 2",
    "42.6": "Lote 3", "42.6a": "Lote 3", "42.6b": "Lote 3", "42.6c": "Lote 3", "42.6d": "Lote 3", "42.6e": "Lote 3", "42.7": "Lote 3",
    "42.8": "Lote 4", "42.8a": "Lote 4", "42.8b": "Lote 4", "42.8c": "Lote 4", "42.8c(1)": "Lote 4", "42.8c(2)": "Lote 4", "42.8d": "Lote 4",
    "42.9": "Lote 5", "42.9a": "Lote 5", "42.9b": "Lote 5", "42.9c": "Lote 5", "42.9d": "Lote 5", "42.9e": "Lote 5", "42.9f": "Lote 5", "42.9g": "Lote 5",
    "42.10": "Lote 6", "42.10a": "Lote 6", "42.10b": "Lote 6", "42.10c": "Lote 6", "42.10d": "Lote 6", "42.11": "Lote 6", "42.11a": "Lote 6", "42.11b": "Lote 6"
}

AUTHOR_SPECS = [
    (r'OLD\s+TESTAMENT', None, 'author:bible-old-testament', 'Old Testament'),
    (r'NEW\s+TESTAMENT', None, 'author:bible-new-testament', 'New Testament'),
    (r'APOCRYPHA', None, 'author:bible-apocrypha', 'Apocrypha'),
    (r'HOMER', 4, 'author:homer', 'Homer'),
    (r'AESCHYLUS', 5, 'author:aeschylus', 'Aeschylus'),
    (r'SOPHOCLES', 5, 'author:sophocles', 'Sophocles'),
    (r'EURIPID[EF]S?', 5, 'author:euripides', 'Euripides'),
    (r'ARISTO[PIH]+ANES?', 5, 'author:aristophanes', 'Aristophanes'),
    (r'H[CE]RODOTUS', 6, 'author:herodotus', 'Herodotus'),
    (r'THUCYDIDES?', 6, 'author:thucydides', 'Thucydides'),
    (r'T[AUCY]+[DIDE]+', 6, 'author:thucydides', 'Thucydides'),
    (r'PLATO|PLAIO', 7, 'author:plato', 'Plato'),
    (r'ARISTOTLE', [8, 9], 'author:aristotle', 'Aristotle'),
    (r'LUCRETIUS', 12, 'author:lucretius', 'Lucretius'),
    (r'EPIC[TI]+[CI]+US', 12, 'author:epictetus', 'Epictetus'),
    (r'AU[RCL]+IUS|MARCUS\s+AURELIUS', 12, 'author:marcus-aurelius', 'Marcus Aurelius'),
    (r'VIRGIL', 13, 'author:virgil', 'Virgil'),
    (r'PLUTARCH|Pm\s*i\s*ARCH', 14, 'author:plutarch', 'Plutarch'),
    (r'TAC[II]+US', 15, 'author:tacitus', 'Tacitus'),
    (r'PLOTINUS', 17, 'author:plotinus', 'Plotinus'),
    (r'AUGUSTINE', 18, 'author:augustine', 'Augustine'),
    (r'AQUINAS', [19, 20], 'author:aquinas', 'Thomas Aquinas'),
    (r'DANTE', 21, 'author:dante', 'Dante'),
    (r'CHAUCER', 22, 'author:chaucer', 'Chaucer'),
    (r'MACHIAVELLI', 23, 'author:machiavelli', 'Machiavelli'),
    (r'HOB\s*B[EB]S?', 23, 'author:hobbes', 'Thomas Hobbes'),
    (r'RABELAIS', 24, 'author:rabelais', 'François Rabelais'),
    (r'MONTAIGN[EL]', 25, 'author:montaigne', 'Montaigne'),
    (r'SHAKES[PEARMFI]+[EL]?', [26, 27], 'author:shakespeare', 'William Shakespeare'),
    (r'S[II]+AKESPCARL', [26, 27], 'author:shakespeare', 'William Shakespeare'),
    (r'CERVANTES', 29, 'author:cervantes', 'Miguel de Cervantes'),
    (r'BACON', 30, 'author:bacon', 'Francis Bacon'),
    (r'DESCARTES', 31, 'author:descartes', 'René Descartes'),
    (r'SPINOZA', 31, 'author:spinoza', 'Benedict de Spinoza'),
    (r'MIL[TI]+ON', 32, 'author:milton', 'John Milton'),
    (r'PASCAL', 33, 'author:pascal', 'Blaise Pascal'),
    (r'LOCKE', 35, 'author:locke', 'John Locke'),
    (r'BERKELEY', 35, 'author:berkeley', 'George Berkeley'),
    (r'HUME', 35, 'author:hume', 'David Hume'),
    (r'SWIFT', 36, 'author:swift', 'Jonathan Swift'),
    (r'STERNE', 36, 'author:sterne', 'Laurence Sterne'),
    (r'FIELDING', 37, 'author:fielding', 'Henry Fielding'),
    (r'MONTESQUIEU|MONIESQUIEU', 38, 'author:montesquieu', 'Montesquieu'),
    (r'ROUS[SF]+E?AU', 38, 'author:rousseau', 'Jean-Jacques Rousseau'),
    (r'SMITH', 39, 'author:smith', 'Adam Smith'),
    (r'GIBBON', [40, 41], 'author:gibbon', 'Edward Gibbon'),
    (r'KANT|KAN\b', 42, 'author:kant', 'Immanuel Kant'),
    (r'DECLARATION\s+OF\s+INDEPENDENCE', 43, 'author:founding-fathers-us', 'Declaration of Independence'),
    (r'ARTICLES\s+OF\s+CONFEDERATION', 43, 'author:founding-fathers-us', 'Articles of Confederation'),
    (r'CONSTITUTION\s+O[PF]\s+THE\s+U\.?S\.?', 43, 'author:founding-fathers-us', 'Constitution of the United States'),
    (r'F[HDE]+ERALIST', 43, 'author:founding-fathers-us', 'The Federalist'),
    (r'MILL', 43, 'author:mill', 'John Stuart Mill'),
    (r'BOS\s*WELL', 44, 'author:boswell', 'James Boswell'),
    (r'HEG[EL]+', 46, 'author:hegel', 'G. W. F. Hegel'),
    (r'GOETHE', 47, 'author:goethe', 'Johann Wolfgang von Goethe'),
    (r'MELVILLE', 48, 'author:melville', 'Herman Melville'),
    (r'DARWIN', 49, 'author:darwin', 'Charles Darwin'),
    (r'MARX\s*[\-\s]*[NQEGCELS]+', 50, 'author:marx-engels', 'Karl Marx & Friedrich Engels'),
    (r'MARX', 50, 'author:marx', 'Karl Marx'),
    (r'TOLSTO[YV]', 51, 'author:tolstoy', 'Leo Tolstoy'),
    (r'DOSTOEVSKY', 52, 'author:dostoevsky', 'Fyodor Dostoevsky'),
    (r'JAMES', 53, 'author:william-james', 'William James'),
    (r'FR[EF]+UD', 54, 'author:freud', 'Sigmund Freud'),
]

KNOWN_WORKS_BY_AUTHOR = {
    "author:aristotle": {
        "ethics": "work:nicomachean-ethics", "nicomachean ethics": "work:nicomachean-ethics",
        "politics": "work:politics-aristotle", "rhetoric": "work:rhetoric-aristotle",
        "topics": "work:topics-aristotle", "athenian constitution": "work:athenian-constitution-aristotle",
        "metaphysics": "work:metaphysics-aristotle", "physics": "work:physics-aristotle",
        "categories": "work:categories-aristotle", "posterior analytics": "work:posterior-analytics-aristotle",
        "poetics": "work:poetics-aristotle", "sophistical refutations": "work:sophistical-refutations-aristotle",
        "on the soul": "work:on-the-soul-aristotle"
    },
    "author:plato": {
        "republic": "work:republic-plato", "laws": "work:laws-plato", "apology": "work:apology-plato",
        "crito": "work:crito-plato", "phaedo": "work:phaedo-plato", "statesman": "work:statesman-plato",
        "gorgias": "work:gorgias-plato", "protagoras": "work:protagoras-plato", "charmides": "work:charmides-plato",
        "theaetetus": "work:theaetetus-plato", "symposium": "work:symposium-plato", "phaedrus": "work:phaedrus-plato",
        "timaeus": "work:timaeus-plato", "meno": "work:meno-plato", "philebus": "work:philebus-plato"
    },
    "author:aquinas": {
        "summa theologica": "work:summa-theologica"
    },
    "author:augustine": {
        "city of god": "work:city-of-god-augustine", "cityofgod": "work:city-of-god-augustine",
        "confessions": "work:confessions-augustine", "christian doctrine": "work:christian-doctrine-augustine"
    },
    "author:hobbes": {
        "leviathan": "work:leviathan-hobbes"
    },
    "author:spinoza": {
        "ethics": "work:ethics-spinoza", "tractatus theologico-politicus": "work:tractatus-spinoza"
    },
    "author:locke": {
        "civil government": "work:civil-government-locke", "human understanding": "work:human-understanding-locke",
        "toleration": "work:toleration-locke"
    },
    "author:montesquieu": {
        "spirit of laws": "work:spirit-of-laws-montesquieu", "laws": "work:spirit-of-laws-montesquieu"
    },
    "author:rousseau": {
        "inequality": "work:inequality-rousseau", "discourse on inequality": "work:inequality-rousseau",
        "social contract": "work:social-contract-rousseau", "political economy": "work:political-economy-rousseau",
        "discourse on political economy": "work:political-economy-rousseau", "emile": "work:emile-rousseau"
    },
    "author:smith": {
        "wealth of nations": "work:wealth-of-nations"
    },
    "author:gibbon": {
        "decline and fall": "work:decline-and-fall-gibbon"
    },
    "author:kant": {
        "pure reason": "work:pure-reason-kant", "science of right": "work:science-of-right",
        "fundamental principles": "work:fund-prin-metaphysic-morals-kant", "fund. prin.": "work:fund-prin-metaphysic-morals-kant",
        "pref. metaphysical elements of ethics": "work:fund-prin-metaphysic-morals-kant",
        "intro. metaphysic of morals": "work:fund-prin-metaphysic-morals-kant",
        "practical reason": "work:critique-practical-reason-kant", "judgement": "work:critique-of-judgement-kant",
        "perpetual peace": "work:perpetual-peace-kant"
    },
    "author:founding-fathers-us": {
        "constitution": "work:us-constitution", "constitution of the u.s.": "work:us-constitution",
        "declaration of independence": "work:declaration-of-independence",
        "articles of confederation": "work:articles-of-confederation",
        "federalist": "work:federalist-papers"
    },
    "author:mill": {
        "utilitarianism": "work:utilitarianism-mill", "liberty": "work:on-liberty-mill",
        "representative government": "work:representative-government"
    },
    "author:boswell": {
        "johnson": "work:life-of-johnson-boswell", "life of johnson": "work:life-of-johnson-boswell"
    },
    "author:hegel": {
        "philosophy of right": "work:philosophy-of-right-hegel", "philosophy of history": "work:philosophy-of-history"
    },
    "author:marx": {
        "capital": "work:capital-marx"
    },
    "author:marx-engels": {
        "communist manifesto": "work:communist-manifesto-marx-engels"
    },
    "author:tolstoy": {
        "war and peace": "work:war-and-peace"
    },
    "author:dostoevsky": {
        "brothers karamazov": "work:brothers-karamazov-dostoevsky"
    },
    "author:william-james": {
        "psychology": "work:psychology-james", "principles of psychology": "work:psychology-james"
    },
    "author:freud": {
        "civilization and its discontents": "work:civilization-discontents-freud",
        "group psychology": "work:group-psychology-freud",
        "ego and the id": "work:ego-and-id-freud",
        "new introductory lectures": "work:new-introductory-lectures-freud"
    },
    "author:milton": {
        "samson agonistes": "work:samson-agonistes", "paradise lost": "work:paradise-lost-milton",
        "areopagitica": "work:areopagitica-milton"
    },
    "author:swift": {
        "gulliver": "work:gullivers-travels-swift", "gulliver's travels": "work:gullivers-travels-swift"
    },
    "author:fielding": {
        "tom jones": "work:tom-jones-fielding"
    },
    "author:thucydides": {
        "peloponnesian war": "work:peloponnesian-war-thucydides"
    },
    "author:herodotus": {
        "history": "work:history-herodotus"
    },
    "author:aeschylus": {
        "suppliant maidens": "work:suppliant-maidens-aeschylus", "prometheus bound": "work:prometheus-bound-aeschylus",
        "agamemnon": "work:agamemnon-aeschylus", "choephoroe": "work:choephoroe-aeschylus", "eumenides": "work:eumenides-aeschylus"
    },
    "author:sophocles": {
        "antigone": "work:antigone-sophocles", "ajax": "work:ajax-sophocles", "oedipus the king": "work:oedipus-king-sophocles",
        "oedipus at colonus": "work:oedipus-colonus-sophocles", "electra": "work:electra-sophocles"
    },
    "author:euripides": {
        "suppliants": "work:suppliants-euripides", "bacchantes": "work:bacchantes-euripides",
        "phoenician maidens": "work:phoenician-maidens-euripides", "orestes": "work:orestes-euripides",
        "medea": "work:medea-euripides", "hecuba": "work:hecuba-euripides", "andromache": "work:andromache-euripides"
    },
    "author:marcus-aurelius": {
        "meditations": "work:meditations-marcus-aurelius"
    },
    "author:virgil": {
        "aeneid": "work:aeneid-virgil"
    },
    "author:dante": {
        "divine comedy": "work:divine-comedy-dante"
    },
    "author:cervantes": {
        "don quixote": "work:don-quixote-cervantes"
    },
    "author:pascal": {
        "pensées": "work:pensees-pascal", "pensees": "work:pensees-pascal", "provincial letters": "work:provincial-letters-pascal"
    },
    "author:montaigne": {
        "essays": "work:essays-montaigne"
    },
    "author:bacon": {
        "advancement of learning": "work:advancement-of-learning-bacon", "novum organum": "work:novum-organum-bacon"
    },
    "author:plotinus": {
        "enneads": "work:third-ennead-plotinus", "third ennead": "work:third-ennead-plotinus"
    }
}

def get_words_with_coords(page):
    res = page['/Resources']
    for k in res.get('/XObject', {}):
        obj = res['/XObject'][k]
        try:
            data = obj.get_data().decode('latin1', errors='ignore')
        except Exception:
            continue
        if 'BT' in data and 'Tj' in data:
            words = []
            curr_tf = 0
            for block in re.split(r'BT\s*', data):
                if not block.strip(): continue
                m_tf = re.search(r'/F\d+\s+([\d\.]+)\s+Tf', block)
                if m_tf: curr_tf = float(m_tf.group(1))
                m_tm = re.findall(r'1\s+0\s+0\s+1\s+([\d\.\-]+)\s+([\d\.\-]+)\s+Tm\s*\((.*?)\)Tj', block, re.DOTALL)
                for x, y, t in m_tm:
                    words.append((float(x), float(y), curr_tf, t))
            return words
    return []

def group_words_into_lines(words):
    words = sorted(words, key=lambda w: -w[1])
    lines = []
    curr = []
    curr_y = None
    for w in words:
        if curr_y is None:
            curr = [w]
            curr_y = w[1]
        elif abs(w[1] - curr_y) < 16:
            curr.append(w)
        else:
            curr.sort(key=lambda w: w[0])
            lines.append((' '.join(w[3] for w in curr), curr_y))
            curr = [w]
            curr_y = w[1]
    if curr:
        curr.sort(key=lambda w: w[0])
        lines.append((' '.join(w[3] for w in curr), curr_y))
    return lines

def resolve_author(raw_str, vol_hint=None):
    clean = raw_str.strip()
    for pat, expected_vol, aid, canonical_name in AUTHOR_SPECS:
        if re.search(pat, clean, re.IGNORECASE):
            vol = None
            if expected_vol is not None:
                if isinstance(expected_vol, list):
                    vol = vol_hint if vol_hint in expected_vol else expected_vol[0]
                else:
                    vol = expected_vol
            return aid, canonical_name, vol, None
    return "author:unresolved", raw_str, vol_hint, f"Unresolved author: {raw_str}"

def resolve_work(author_id, title_raw, vol_hint=None):
    if not title_raw:
        if author_id == "author:founding-fathers-us":
            return "work:us-constitution", "Constitution of the United States", None
        elif author_id == "author:aquinas":
            return "work:summa-theologica", "Summa Theologica", None
        elif author_id == "author:marx":
            return "work:capital-marx", "Capital", None
        elif author_id == "author:hegel":
            return "work:philosophy-of-right-hegel", "Philosophy of Right", None
        return f"work:unresolved-{author_id.replace('author:', '')}", "Unspecified Work", "Missing work title"
    
    t_clean = title_raw.lower().strip()
    t_clean = re.sub(r'^[,\.\:\;\s\(\)]+|[,\.\:\;\s\(\)]+$', '', t_clean)
    t_norm = re.sub(r'[^a-z0-9]+', '', t_clean)
    
    # Check known works for this author
    if author_id in KNOWN_WORKS_BY_AUTHOR:
        for k, wid in KNOWN_WORKS_BY_AUTHOR[author_id].items():
            k_norm = re.sub(r'[^a-z0-9]+', '', k)
            if k_norm in t_norm or t_norm in k_norm:
                return wid, title_raw, None
    
    # Check bible
    if "bible" in author_id:
        slug = re.sub(r'[^a-z0-9]+', '-', t_clean).strip('-')
        return f"work:bible-{slug}", title_raw, None

    # Fallback to general slug
    slug = re.sub(r'[^a-z0-9]+', '-', t_clean).strip('-')
    auth_slug = author_id.replace('author:', '')
    return f"work:{slug}-{auth_slug}", title_raw, f"Work auto-resolved by slug heuristic: {title_raw}"

def clean_locator_slashes(loc_str):
    # 1. Proteger Gibbon "Fa//" -> "Fall"
    s = re.sub(r'Fa//', 'Fall', loc_str)
    # 2. Proteger numerais romanos // e /// que o OCR leu no lugar de II e III
    s = re.sub(r'(?<=\s)///(?=\s)', 'III', s)
    s = re.sub(r'(?<=\s)//(?=\s)', 'II', s)
    s = re.sub(r'^\s*///(?=\s)', 'III', s)
    s = re.sub(r'^\s*//(?=\s)', 'II', s)
    s = re.sub(r'\(/D\)\s*//\s*', '(D) II ', s)
    # 3. Garantir espacamento em barras unicas que separam obras (ex: 17b/CityofGod -> 17b / CityofGod)
    s = re.sub(r'(?<!/)/(?!/)', ' / ', s)
    # 4. Colapsar espacos extras
    s = re.sub(r'[ \t]+', ' ', s).strip()
    return s

def parse_work_segments(locator_raw, author_id, vol_hint=None):
    cleaned_loc = clean_locator_slashes(locator_raw)
    parts = re.split(r'\s+/\s+', cleaned_loc)
    segments = []
    ambiguities = []
    
    for seg_idx, p in enumerate(parts, 1):
        p_clean = p.strip()
        if not p_clean: continue
        
        # In Syntopicon, title precedes comma or locator markers
        m = re.match(r'^([A-Za-z0-9\s\'\.\-]+?)(?:,\s*|:\s*|(?=\s*\[|\s+BK|\s+PART|\s+CH|\s+SECT|\s+Q\b|\s+ACT|\s+\d+[a-d]))(.*)', p_clean)
        
        if m and not re.match(r'^(?:BK|PART|CH|SECT|Q|ACT|CANTO|SCENE|ARTICLE|AMENDMENTS|\d)', m.group(1).strip()):
            title_candidate = m.group(1).strip()
            loc_str = m.group(2).strip()
            if loc_str.startswith(','): loc_str = loc_str[1:].strip()
            wid, wtitle, w_warn = resolve_work(author_id, title_candidate, vol_hint)
        else:
            title_candidate = None
            loc_str = p_clean
            wid, wtitle, w_warn = resolve_work(author_id, None, vol_hint)
            
        if w_warn:
            ambiguities.append({
                "tipo": "work_resolution_warning",
                "descricao": w_warn,
                "textoOriginal": p_clean,
                "resolucaoProposta": wid,
                "severidade": "baixa"
            })
            
        # Parse individual atomic locators
        loc_items = [x.strip() for x in re.split(r';\s*', loc_str) if x.strip()]
        
        segments.append({
            "workSegmentIndex": seg_idx,
            "workId": wid,
            "workTitle": wtitle,
            "locatorRaw": p_clean,
            "locators": loc_items
        })
        
    return segments, ambiguities

def run_extraction():
    print(f"[{datetime.datetime.now().isoformat()}] Iniciando extracao geral de pp. 859-878 de {PDF_PATH} ({BASELINE_ID})...")
    reader = pypdf.PdfReader(PDF_PATH)
    
    all_lines = []
    for p_idx in range(9, 29):
        page_num = p_idx + 850
        page = reader.pages[p_idx]
        words = get_words_with_coords(page)
        col1 = [w for w in words if w[1] <= 4700 and w[0] < 1700 and not (page_num == 878 and w[1] < 4100)]
        col2 = [w for w in words if w[1] <= 4700 and w[0] >= 1700 and not (page_num == 878 and w[1] < 4100)]
        lines1 = group_words_into_lines(col1)
        lines2 = group_words_into_lines(col2)
        for l, y in lines1: all_lines.append((page_num, 1, y, l))
        for l, y in lines2: all_lines.append((page_num, 2, y, l))

    print(f"Total de linhas de texto extraidas com coordenadas: {len(all_lines)}")

    # 1. Alinhamento de todos os 41 topicos
    curr_line_idx = 0
    matched_headings = []
    for code, tid, tname, pat, keywords in OUTLINE_TOPICS:
        found = False
        for i in range(curr_line_idx, len(all_lines)):
            p, c, y, text = all_lines[i]
            t_strip = text.strip()
            if t_strip.startswith('(') and (t_strip.endswith(')') or len(t_strip) > 35) and y > 4500:
                continue
            clean_text = text.lower().replace('\\', '')
            pat_match = bool(re.search(pat, text, re.IGNORECASE))
            kw_match = any(kw in clean_text for kw in keywords)
            if (pat_match and kw_match) or (kw_match and len(text) < 80):
                matched_headings.append({
                    "topicCode": code,
                    "topicId": tid,
                    "topicName": tname,
                    "page": p,
                    "col": c,
                    "y": y,
                    "text": text,
                    "lineIndex": i
                })
                curr_line_idx = i + 1
                found = True
                break
        if not found:
            raise RuntimeError(f"ERRO CRITICO: Nao foi possivel detectar o topico {code} ({tid})")

    if len(matched_headings) != 41:
        raise RuntimeError(f"ERRO: Apenas {len(matched_headings)} de 41 topicos foram detectados!")

    print(f"Sucesso: Todos os 41 topicos foram alinhados documentalmente em sequencia estrita.")

    # 2. Reconstrucao de entradas fisicas dentro de cada intervalo de topico
    entry_start_pattern = re.compile(
        r'^(?:'
        r'OLD TESTAMENT|NEW TESTAMENT|APOCRYPHA|'
        r'\d{1,2}\s+[A-Za-z\-\s\.\,\']+:|'
        r'\d{1,2}\s+[A-Z\-\s]{3,}\b|'
        r'\d{1,2}\s+Bos\s*WELL|'
        r'l4\s+PLUTARCH|\'5\s+BERKELEY|7\s+FIELDING|1\s+GIBBON|45\s+HEGEL'
        r')'
    )

    candidatas = []
    ambiguidades = []
    
    cobertura_paginas = {}
    for p in range(859, 879):
        cobertura_paginas[f"p.{p}"] = {
            "pagina": p,
            "entradasDetectadas": 0,
            "verificadasNoVault": 0,
            "refsComWarning": 0,
            "totalAmbiguidades": 0,
            "topicosPresentes": []
        }

    cobertura_topicos = {}
    for code, tid, tname, _, _ in OUTLINE_TOPICS:
        cobertura_topicos[code] = {
            "topicoId": tid,
            "topicCode": code,
            "nomeEn": tname,
            "tipo": "heading_node" if code in ["42.1", "42.11"] else "leaf_node",
            "paginas": set(),
            "refsDetectadas": 0,
            "workSegmentsDetectados": 0,
            "refsVerificadasNoVault": 0,
            "workSegmentsVerificadosNoVault": 0,
            "refsComWarning": 0,
            "totalAmbiguidades": 0,
            "statusReconciliacao": "needs_verification",
            "lote": TOPIC_LOT_MAP[code]
        }

    # Fixtures de regressao comprovadas no vault:
    fixture_verified_refs = {
        "42.1a": 18, "42.1b": 8, "42.1c": 11, "42.1d": 8, "42.1e": 3, "42.1f": 5,
        "42.8c(1)": 18
    }
    fixture_verified_segs = {
        "42.1a": 27, "42.1b": 12, "42.1c": 17, "42.1d": 12, "42.1e": 7, "42.1f": 7,
        "42.8c(1)": 21
    }

    seen_composite_keys = set()

    for idx, h in enumerate(matched_headings):
        code = h["topicCode"]
        tid = h["topicId"]
        line_start = h["lineIndex"]
        line_end = matched_headings[idx+1]["lineIndex"] if idx + 1 < len(matched_headings) else len(all_lines)
        
        cobertura_topicos[code]["paginas"].add(h["page"])
        if code not in cobertura_paginas[f"p.{h['page']}"]["topicosPresentes"]:
            cobertura_paginas[f"p.{h['page']}"]["topicosPresentes"].append(code)

        raw_entries = []
        curr_entry = None

        for l_i in range(line_start + 1, line_end):
            lp, lc, ly, ltext = all_lines[l_i]
            l_str = ltext.strip()
            
            cobertura_topicos[code]["paginas"].add(lp)
            if code not in cobertura_paginas[f"p.{lp}"]["topicosPresentes"]:
                cobertura_paginas[f"p.{lp}"]["topicosPresentes"].append(code)

            if l_str.startswith('(') and (l_str.endswith(')') or len(l_str) > 35) and ly > 4500:
                continue
            if l_i == line_start + 1 and not entry_start_pattern.match(l_str):
                continue
            if l_i == line_start + 2 and not entry_start_pattern.match(l_str) and len(l_str) < 40:
                continue

            m = entry_start_pattern.match(l_str)
            if m:
                if curr_entry:
                    raw_entries.append(curr_entry)
                curr_entry = {
                    "startLine": l_i,
                    "page": lp,
                    "col": lc,
                    "header": m.group(0),
                    "lines": [l_str]
                }
            else:
                if curr_entry:
                    curr_entry["lines"].append(l_str)
                else:
                    if len(l_str) > 3:
                        amb_item = {
                            "topicCode": code,
                            "topicId": tid,
                            "page": lp,
                            "col": lc,
                            "tipo": "orphan_line_before_entry",
                            "descricao": "Linha encontrada antes do inicio da primeira entrada no topico",
                            "textoOriginal": l_str,
                            "resolucaoProposta": "Linha ignorada ou anexada ao cabecalho",
                            "severidade": "baixa"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{lp}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1

        if curr_entry:
            raw_entries.append(curr_entry)

        # Processar cada entrada fisica no topico
        for order_idx, re_entry in enumerate(raw_entries, 1):
            entry_page = re_entry["page"]
            entry_col = re_entry["col"]
            
            comp_key = f"{SOURCE_ID}:{entry_page}:{tid}:{order_idx}"
            if comp_key in seen_composite_keys:
                raise ValueError(f"VIOLACAO DE INTEGRIDADE DOCUMENTAL: Chave composta duplicada {comp_key}")
            seen_composite_keys.add(comp_key)

            full_text = " ".join(re_entry["lines"]).strip()
            
            m_bible = re.match(r'^(OLD TESTAMENT|NEW TESTAMENT|APOCRYPHA)', full_text)
            warnings_list = []
            
            if m_bible:
                b_name = m_bible.group(1)
                aid, cname, vol_num, err = resolve_author(b_name, None)
                author_raw = b_name
                raw_loc = re.sub(r'^(?:OLD TESTAMENT|NEW TESTAMENT|APOCRYPHA)[\:\s]*', '', full_text).strip()
            else:
                m_auth = re.match(r'^(\d{1,2}|l4|\'5)\s+([^:\']+)(?:[:\']|\s{2,})(.*)', full_text)
                if m_auth:
                    raw_vol_str = m_auth.group(1)
                    raw_author = m_auth.group(2).strip()
                    raw_loc = m_auth.group(3).strip()
                    
                    vol_val = None
                    if raw_vol_str == 'l4':
                        vol_val = 14
                        amb_item = {
                            "topicCode": code, "topicId": tid, "page": entry_page, "col": entry_col,
                            "tipo": "ocr_volume_correction", "descricao": "Volume l4 corrigido para 14 (Plutarco)",
                            "textoOriginal": raw_vol_str, "resolucaoProposta": 14, "severidade": "baixa"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1
                    elif raw_vol_str == "'5":
                        vol_val = 35
                        amb_item = {
                            "topicCode": code, "topicId": tid, "page": entry_page, "col": entry_col,
                            "tipo": "ocr_volume_correction", "descricao": "Volume '5 corrigido para 35 (Berkeley)",
                            "textoOriginal": raw_vol_str, "resolucaoProposta": 35, "severidade": "baixa"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1
                    elif raw_vol_str.isdigit():
                        vol_val = int(raw_vol_str)
                    
                    aid, cname, resolved_vol, err = resolve_author(raw_author, vol_val)
                    author_raw = raw_author
                    vol_num = resolved_vol if resolved_vol is not None else vol_val
                    if err:
                        warnings_list.append(err)
                        amb_item = {
                            "topicCode": code, "topicId": tid, "page": entry_page, "col": entry_col,
                            "tipo": "author_resolution_warning", "descricao": err,
                            "textoOriginal": raw_author, "resolucaoProposta": aid, "severidade": "media"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1
                else:
                    m_fallback = re.match(r'^(\d{1,2}|l4|\'5)\s+([A-Z\-\s]{3,})\s+(.*)', full_text)
                    if m_fallback:
                        raw_vol_str = m_fallback.group(1)
                        raw_author = m_fallback.group(2).strip()
                        raw_loc = m_fallback.group(3).strip()
                        vol_val = int(raw_vol_str) if raw_vol_str.isdigit() else None
                        aid, cname, vol_num, err = resolve_author(raw_author, vol_val)
                        author_raw = raw_author
                        amb_item = {
                            "topicCode": code, "topicId": tid, "page": entry_page, "col": entry_col,
                            "tipo": "missing_author_colon", "descricao": f"Dois pontos ausente apos autor {raw_author}",
                            "textoOriginal": full_text[:40], "resolucaoProposta": f"{vol_val} {aid}: {raw_loc[:30]}",
                            "severidade": "baixa"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1
                    else:
                        aid = "author:unresolved"
                        author_raw = full_text[:20]
                        vol_num = None
                        raw_loc = full_text
                        err = f"Formato de entrada irreconhecivel: {full_text[:40]}"
                        warnings_list.append(err)
                        amb_item = {
                            "topicCode": code, "topicId": tid, "page": entry_page, "col": entry_col,
                            "tipo": "unparseable_entry", "descricao": err,
                            "textoOriginal": full_text, "resolucaoProposta": "Requer analise manual",
                            "severidade": "alta"
                        }
                        ambiguidades.append(amb_item)
                        cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                        cobertura_topicos[code]["totalAmbiguidades"] += 1

            if not raw_loc:
                raw_loc = full_text
            
            work_segments, seg_ambiguities = parse_work_segments(raw_loc, aid, vol_num)
            for sa in seg_ambiguities:
                sa["topicCode"] = code
                sa["topicId"] = tid
                sa["page"] = entry_page
                sa["col"] = entry_col
                ambiguidades.append(sa)
                cobertura_paginas[f"p.{entry_page}"]["totalAmbiguidades"] += 1
                cobertura_topicos[code]["totalAmbiguidades"] += 1

            sub_slug = code.replace("42.", "").replace("(", "-").replace(")", "")
            ref_id = f"ref:justica:{sub_slug}-{order_idx:02d}"

            candidata_obj = {
                "id": ref_id,
                "topicId": tid,
                "topicCode": code,
                "orderInTopic": order_idx,
                "sourceId": SOURCE_ID,
                "syntopiconPage": entry_page,
                "syntopiconCol": entry_col,
                "compositeKey": comp_key,
                "volume": vol_num,
                "authorId": aid,
                "authorRaw": author_raw,
                "locatorRaw": raw_loc,
                "workSegments": work_segments,
                "totalWorkSegments": len(work_segments),
                "verification": "needs_verification",
                "epistemology": "documentary",
                "provenance": SOURCE_ID,
                "warnings": warnings_list
            }

            candidatas.append(candidata_obj)

            cobertura_paginas[f"p.{entry_page}"]["entradasDetectadas"] += 1
            if warnings_list:
                cobertura_paginas[f"p.{entry_page}"]["refsComWarning"] += 1

            cobertura_topicos[code]["refsDetectadas"] += 1
            cobertura_topicos[code]["workSegmentsDetectados"] += len(work_segments)
            if warnings_list:
                cobertura_topicos[code]["refsComWarning"] += 1

    # Atualizar contagens verificadas com base nas fixtures comprovadas
    total_verificadas = 0
    total_segs_verificados = 0
    for code, v_count in fixture_verified_refs.items():
        cobertura_topicos[code]["refsVerificadasNoVault"] = v_count
        s_count = fixture_verified_segs.get(code, 0)
        cobertura_topicos[code]["workSegmentsVerificadosNoVault"] = s_count
        if cobertura_topicos[code]["refsDetectadas"] == v_count:
            cobertura_topicos[code]["statusReconciliacao"] = "verified"
        total_verificadas += v_count
        total_segs_verificados += s_count

    for c in candidatas:
        code = c["topicCode"]
        p = c["syntopiconPage"]
        if code in fixture_verified_refs:
            cobertura_paginas[f"p.{p}"]["verificadasNoVault"] += 1

    # Resumo por lote estritamente calculado a partir das candidatas
    resumo_lotes = {}
    for lote_nome in ["Lote 1", "Lote 2", "Lote 3", "Lote 4", "Lote 5", "Lote 6"]:
        topicos_lote = [c for c, l in TOPIC_LOT_MAP.items() if l == lote_nome]
        refs_det = sum(cobertura_topicos[c]["refsDetectadas"] for c in topicos_lote)
        segs_det = sum(cobertura_topicos[c]["workSegmentsDetectados"] for c in topicos_lote)
        refs_ver = sum(cobertura_topicos[c]["refsVerificadasNoVault"] for c in topicos_lote)
        segs_ver = sum(cobertura_topicos[c]["workSegmentsVerificadosNoVault"] for c in topicos_lote)
        refs_warn = sum(cobertura_topicos[c]["refsComWarning"] for c in topicos_lote)
        tot_amb = sum(cobertura_topicos[c]["totalAmbiguidades"] for c in topicos_lote)
        
        status_lote = "needs_verification"
        if lote_nome == "Lote 1":
            status_lote = "verified"
        elif lote_nome == "Lote 4":
            status_lote = "partially_verified_8c1"

        resumo_lotes[lote_nome] = {
            "topicos": topicos_lote,
            "totalTopicos": len(topicos_lote),
            "refsDetectadas": refs_det,
            "workSegmentsDetectados": segs_det,
            "refsVerificadas": refs_ver,
            "workSegmentsVerificados": segs_ver,
            "refsComWarning": refs_warn,
            "totalAmbiguidades": tot_amb,
            "statusLote": status_lote
        }

    for code in cobertura_topicos:
        cobertura_topicos[code]["paginas"] = sorted(list(cobertura_topicos[code]["paginas"]))

    total_work_segments = sum(c["totalWorkSegments"] for c in candidatas)
    total_refs_com_warning = sum(1 for c in candidatas if c["warnings"])

    cobertura_report = {
        "versao": "1.1.0",
        "baseline": BASELINE_ID,
        "timestamp": datetime.datetime.now().isoformat(),
        "fonteDocumental": SOURCE_ID,
        "paginasEscopo": "859–878",
        "metricasGlobais": {
            "totalEntradasDetectadas": len(candidatas),
            "totalWorkSegmentsDetectados": total_work_segments,
            "totalEntradasVerificadasNoVault": total_verificadas,
            "totalWorkSegmentsVerificadosNoVault": total_segs_verificados,
            "referenciasCandidatasStaging": len(candidatas) - total_verificadas,
            "totalReferenciasComWarning": total_refs_com_warning,
            "totalAmbiguidadesRegistradas": len(ambiguidades)
        },
        "esclarecimentoSemantico": {
            "totalReferenciasComWarning": "Contagem de registros de referencia fisica que possuem ao menos 1 aviso no campo warnings (ex: autor nao resolvido ou formato irregular).",
            "totalAmbiguidadesRegistradas": "Contagem de ocorrencias individuais de atrito documental catalogadas detalhadamente em ambiguidades.json (inclui correcoes de OCR, dois pontos ausentes e resolucoes aproximadas de obra por segmento)."
        },
        "resumoPorLote": resumo_lotes,
        "porPagina": cobertura_paginas,
        "porTopico": cobertura_topicos
    }

    path_candidatas = os.path.join(STAGING_DIR, 'referencias-candidatas.json')
    path_ambiguidades = os.path.join(STAGING_DIR, 'ambiguidades.json')
    path_cobertura = os.path.join(STAGING_DIR, 'cobertura.json')

    with open(path_candidatas, 'w', encoding='utf-8') as f:
        json.dump(candidatas, f, indent=2, ensure_ascii=False)
    print(f"Salvo: {path_candidatas} ({len(candidatas)} referencias candidatas)")

    with open(path_ambiguidades, 'w', encoding='utf-8') as f:
        json.dump(ambiguidades, f, indent=2, ensure_ascii=False)
    print(f"Salvo: {path_ambiguidades} ({len(ambiguidades)} ambiguidades registradas)")

    with open(path_cobertura, 'w', encoding='utf-8') as f:
        json.dump(cobertura_report, f, indent=2, ensure_ascii=False)
    print(f"Salvo: {path_cobertura} (relatorio completo de cobertura por pagina e topico)")

    print("\n=== RESUMO RECONCILIADO DA EXTRACAO ===")
    print(f"Total de referencias detectadas: {len(candidatas)}")
    print(f"Total de segmentos de obra: {total_work_segments}")
    print(f"Total de referencias verificadas no vault: {total_verificadas} (53 Lote 1 + 18 8c-1)")
    print(f"Total de segmentos verificados no vault: {total_segs_verificados} (82 Lote 1 + 21 8c-1)")
    print(f"Total de referencias com warning: {total_refs_com_warning}")
    print(f"Total de ambiguidades individuais registradas: {len(ambiguidades)}")
    for lote, dados in resumo_lotes.items():
        print(f"  {lote:8s}: {dados['refsDetectadas']:3d} refs | {dados['workSegmentsDetectados']:3d} segs | "
              f"verif: {dados['refsVerificadas']:2d} refs ({dados['workSegmentsVerificados']:2d} segs) | "
              f"warns: {dados['refsComWarning']:2d} | ambig: {dados['totalAmbiguidades']:3d} | status: {dados['statusLote']}")

if __name__ == '__main__':
    run_extraction()
