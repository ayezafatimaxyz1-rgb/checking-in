"""Shared helpers + CSS for the 99 Names book generator (English and Urdu editions)."""
import json, re, html, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
LANG = "en"
COLLECT = None          # set() when collecting translatable strings
UR = {}                 # English key -> Urdu text
MISSING = {}

_Q = {}


def set_lang(l):
    global LANG, UR
    LANG = l
    if l == "ur" and not UR:
        for f in sorted(glob.glob(os.path.join(HERE, "ur", "ur_*.json"))):
            UR.update(json.load(open(f, encoding="utf-8")))


def _load():
    if not _Q:
        base = os.path.join(HERE, "data")
        for k, f in (("ar", "quran.json"), ("en", "quran_en.json"), ("ur", "quran_ur.json")):
            _Q[k] = json.load(open(os.path.join(base, f), encoding="utf-8"))


def verse(s, a, lang="en"):
    _load()
    ar = [x for x in _Q["ar"][s - 1]["verses"] if x["id"] == a][0]["text"]
    tr = [x for x in _Q[lang][s - 1]["verses"] if x["id"] == a][0]["translation"]
    return ar, tr


def surah_name(s):
    _load()
    return _Q["ar"][s - 1]["name"]


def clean_ar(t):
    for ch in ("۞", "۩"):
        t = t.replace(ch, "")
    return t.strip()


def clean_en(t):
    t = t.strip()
    if t.count('"') % 2 == 1:
        t = t + '."'
    elif not t.endswith(('.', '?', '!', '"')):
        t = t + '.'
    return t


def ayah(s, a, b=None, words=None, tr=None):
    """Arabic lines + translation from the verified Qur'an data. words=(i,j) slices Arabic words."""
    _load()
    last = b or a
    lines, trs, urs = [], [], []
    for k in range(a, last + 1):
        ar, en = verse(s, k)
        ar = clean_ar(ar)
        if words:
            w = ar.split()
            ar = " ".join(w[words[0]:words[1]])
        lines.append(ar)
        trs.append(en.strip())
        urs.append(verse(s, k, "ur")[1].strip())
    en_all = clean_en(" ".join(trs)) if tr is None else tr
    ref = f"Qur'an {s}:{a}" + (f"–{b}" if b and b != a else "")
    ref_ur = f"قرآن مجید، سورۃ {surah_name(s)}، \u2066{s}:{a}" + (f"\u2013{b}" if b and b != a else "") + "\u2069"
    ur_all = None if words else "«" + " ".join(urs) + "»"
    return {"ar": lines, "en": en_all, "ref": ref, "ref_ur": ref_ur, "ur": ur_all}


# ------------------------------------------------------------------ text cleaning
def deai(s):
    """Remove em-dash and arrow punctuation from prose."""
    if "—" not in s and "→" not in s:
        return s
    if s.startswith("— "):
        s = s[2:]
    out = []
    for seg in s.split("|"):
        seg = re.sub(r" — (?=(?:it|It|he|He|she|they|They|this|This|that|the|a|an|we|We|you|You|I|there|nothing|what|but|and|which|His|Allah|neither|every|each|no|not|only|both|all|one|both)\b)", "; ", seg)
        seg = seg.replace(" — ", ", ").replace("—", ", ")
        parts = seg.split(" → ")
        if len(parts) > 1:
            seg = parts[0] + ": " + ", ".join(parts[1:])
        out.append(seg)
    s = "|".join(out)
    s = s.replace(",  ", ", ").replace(", ,", ",").replace(", .", ".")
    return s


LATIN = re.compile(r"[A-Za-z]")
NAMEONLY = re.compile(r"(?:(?:Al|Ar|As|Ad|An|Ash|At|Az)-[A-Za-z'’]+(?:,? &?\s*)?)+")


def T(s):
    """Clean (and in Urdu mode, translate) an English string."""
    s = deai(s)
    if not LATIN.search(s):
        return s
    if COLLECT is not None and not NAMEONLY.fullmatch(s.strip()):
        COLLECT.setdefault(s, 1)
    if LANG == "ur":
        if s in UR:
            return UR[s]
        if NAMEONLY.fullmatch(s.strip()):
            return s
        MISSING.setdefault(s, 1)
        return s
    return s


COLL_NAMES = {
    "Sahih al-Bukhari": "صحیح بخاری", "Sahih Muslim": "صحیح مسلم", "Jami' at-Tirmidhi": "جامع ترمذی",
    "Sunan Abi Dawud": "سنن ابی داؤد", "Sunan an-Nasa'i": "سنن نسائی", "Sunan Ibn Majah": "سنن ابن ماجہ",
    "hasan sahih": "حسن صحیح", "hasan": "حسن"}


def ref_ur(ref):
    s = deai(ref)
    for k in sorted(COLL_NAMES, key=len, reverse=True):
        s = s.replace(k, COLL_NAMES[k])
    s = s.replace(";", "؛").replace(" and ", " اور ").replace("see also", "مزید دیکھیے")
    return s


ARABIC_RUN = re.compile(
    r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]+"
    r"(?:[  ]+[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]+)*")
_TOK = r"(?![\u0600-\u06FF]*[\u0679\u0688\u0691\u06BA\u06BE\u06C1\u06D2\u06A9\u06CC\u067E\u0686\u06AF])[\u0600-\u06FF]*[\u064B-\u0652\u0670][\u0600-\u06FF]*"
ARABIC_RUN_UR = re.compile(_TOK + r"(?:[  ]+" + _TOK + r")*")


def md(t):
    """Tiny inline markup: **bold**, *italic*, auto-wrap Arabic runs."""
    t = T(t)
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<i>\1</i>", t)
    t = t.replace("ﷺ", '<span class="pbuh">ﷺ</span>')
    rx = ARABIC_RUN_UR if LANG == "ur" else ARABIC_RUN
    t = rx.sub(lambda m: f'<span class="a" dir="rtl">{m.group(0)}</span>', t)
    return t


def raw(t):
    """Translate a short UI label that is inserted as-is (no markup)."""
    return T(t)


def p(t, cls=""):
    return f'<p class="{cls}">{md(t)}</p>' if cls else f"<p>{md(t)}</p>"


def h2(t):
    return f'<h2>{md(t)}</h2>'


def h3(t):
    return f'<h3>{md(t)}</h3>'


def bullets(items):
    return '<ul class="dash">' + "".join(f"<li>{md(i)}</li>" for i in items) + "</ul>"


def box(t):
    return f'<div class="defbox">{md(t)}</div>'


def related(t):
    parts = []
    for part in t.split(" · "):
        if " — " in part:
            a, b = part.split(" — ", 1)
            part = f"{a} ({b})"
        parts.append(part)
    t = " · ".join(parts)
    return f'<div class="relbox"><div class="relh">{raw("Related words")}</div><div>{md(t)}</div></div>'


def ayah_box(a):
    ar = "<br>".join(a["ar"])
    if LANG == "ur":
        tr = a["ur"] if a.get("ur") else T(a["en"])
        ref = a["ref_ur"] if a.get("ref_ur") else T(a["ref"]) if a["ref"] else ""
        tr_html = md(tr) if not a.get("ur") else html.escape(tr)
        ref_html = md(ref) if ref else ""
    else:
        global COLLECT
        saved = COLLECT
        if a.get("ur"):
            COLLECT = None
        tr_html = md(a["en"])
        COLLECT = None
        ref_html = md(a["ref"])
        COLLECT = saved
    return (f'<div class="ayah"><div class="ayar" dir="rtl">{ar}</div>'
            f'<div class="aytr">{tr_html}</div><div class="ref">{ref_html}</div></div>')


def hadith_box(ar, en, ref):
    arhtml = f'<div class="hdar" dir="rtl">{ar}</div>' if ar else ""
    global COLLECT
    saved = COLLECT
    COLLECT = None
    r = md(ref_ur(ref)) if LANG == "ur" else md(ref)
    COLLECT = saved
    return (f'<div class="hadith">{arhtml}<div class="hdtr">{md(en)}</div>'
            f'<div class="ref">{r}</div></div>')


def essence(en, ur=None):
    if LANG == "ur" and ur:
        body = " ".join(x.strip() for x in ur)
        body = fix_arabic_names(body)
        return f'<div class="essence"><div class="esslab">{raw("ESSENCE")}</div><div>{md(body)}</div></div>'
    return f'<div class="essence"><div class="esslab">{raw("ESSENCE")}</div><div>{md(en)}</div></div>'


def fix_arabic_names(s):
    """Inside words that carry Arabic vowel marks, use Arabic yeh/kaf (not Persian)."""
    def fix(m):
        w = m.group(0)
        return w.replace("ی", "ي").replace("ک", "ك")
    return re.sub(r"[؀-ۿ]*[ً-ْٰ][؀-ۿ]*", fix, s)


def question(t):
    return f'<p class="question">{md(t)}</p>'


def table(head, rows):
    h = "".join(f"<th>{md(x) if x else ''}</th>" for x in head)
    r = ""
    for row in rows:
        r += "<tr>" + f"<td class='k'>{md(row[0])}</td>" + "".join(f"<td>{md(x)}</td>" for x in row[1:]) + "</tr>"
    return f'<table class="tbl"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table>'


def scholar(name, ar=None, en=None):
    a = f'<div class="scar" dir="rtl">{ar}</div>' if ar else ""
    e = f'<div class="scen">{md(en)}</div>' if en else ""
    return f'<div class="sch"><div class="schn">{md(name)}</div>{a}{e}</div>'


def chapter_open(label, ar, tr, en, ur):
    cls = "ar-title" if len(ar) <= 24 else ("ar-title s2" if len(ar) <= 40 else "ar-title s3")
    m = re.fullmatch(r"NAME (\d+) OF 99", label)
    if LANG == "ur":
        label = f"نام {m.group(1)} از 99" if m else raw(label)
        main = (f'<div class="en urmain">{html.escape(ur)}</div><div class="subm">{html.escape(deai(en))}</div>'
                if ur else f'<div class="en urmain">{md(en)}</div><div class="subm">{html.escape(deai(en))}</div>')
        return (f'<section class="chapter"><div class="eyebrow">{label}</div>'
                f'<div class="{cls}" dir="rtl">{ar}</div><div class="tr">{html.escape(deai(tr))}</div>'
                f'{main}<div class="rule"></div>')
    label = deai(label)
    return (f'<section class="chapter"><div class="eyebrow">{label}</div>'
            f'<div class="{cls}" dir="rtl">{ar}</div><div class="tr">{md(tr)}</div>'
            f'<div class="en">{md(en)}</div>' + (f'<div class="ur" dir="rtl">{ur}</div>' if ur else "") +
            '<div class="rule"></div>')


def chapter_close():
    return "</section>"


def root_row(letters, ar_line, en_line, head=None):
    hd = f'<div class="rtx-h">{md(head)}</div>' if head else ""
    ar = f'<div class="rtx-ar" dir="rtl">{ar_line}</div>' if ar_line else ""
    return (f'<div class="rootrow"><div class="rootbox"><div class="rl" dir="rtl">{letters}</div>'
            f'<div class="rs">{raw("ROOT")}</div></div><div class="rtx">{hd}{ar}<div>{md(en_line)}</div></div></div>')


def pattern_head(name, pat):
    if LANG == "ur":
        return f'<h3 class="pat"><span class="a" dir="rtl">{name}</span> کا وزن: <span class="a" dir="rtl">{pat}</span></h3>'
    return f'<h3 class="pat">{md(name)} is on the pattern <span class="a" dir="rtl">{pat}</span></h3>'


def label_name(n):
    return f"NAME {n} OF 99"


def render_name(d):
    """Render one standard name chapter from a dict (see content files)."""
    n = d["n"]
    if LANG == "ur":
        label = f"نام {n} از 99"
    else:
        label = label_name(n)
    # chapter_open translates `label` in Urdu mode; pass a ready label through a bypass
    if LANG == "ur":
        co = chapter_open_ur_ready(label, d["ar"], d["tr"], d["en"], d["ur"])
    else:
        co = chapter_open(label, d["ar"], d["tr"], d["en"], d["ur"])
    out = [co]
    out.append(h2("1. Root Word & Meaning"))
    out.append(root_row(d["root"], d.get("root_ar"), d["root_en"], d.get("root_head")))
    for x in d.get("intro", []):
        out.append(p(x))
    if d.get("table"):
        out.append(table(*d["table"]))
    if d.get("pattern"):
        pt = d["pattern"]
        out.append(pattern_head(d["name_ar"], pt["ar"]))
        out.append(bullets(pt["bullets"]))
    if d.get("defbox"):
        out.append(box(d["defbox"]))
    for x in d.get("after_def", []):
        out.append(p(x))
    for s in d.get("scholars", []):
        out.append(scholar(*s))
    if d.get("related"):
        out.append(related(d["related"]))
    out.append(h2("2. Qur'anic Connection"))
    for q in d["quran"]:
        out.append(ayah_box(q["ayah"]))
        for x in q.get("note", []):
            out.append(p(x))
    for hd in d.get("hadith", []):
        out.append(hadith_box(hd["ar"], hd["en"], hd["ref"]))
        for x in hd.get("note", []):
            out.append(p(x))
    out.append(h2("3. Essence of the Name"))
    out.append(essence(d["essence"], d.get("essence_ur")))
    out.append(h2("4. For You, the Servant"))
    for x in d["servant"]:
        out.append(p(x))
    out.append(question(d["question"]))
    out.append(chapter_close())
    return "\n".join(out)


def chapter_open_ur_ready(label, ar, tr, en, ur):
    cls = "ar-title" if len(ar) <= 24 else ("ar-title s2" if len(ar) <= 40 else "ar-title s3")
    return (f'<section class="chapter"><div class="eyebrow">{label}</div>'
            f'<div class="{cls}" dir="rtl">{ar}</div><div class="tr">{html.escape(tr)}</div>'
            f'<div class="en urmain">{html.escape(ur)}</div><div class="subm">{html.escape(deai(en))}</div>'
            '<div class="rule"></div>')


def font_css():
    f = os.path.join(HERE, "fonts")
    def ff(fam, file, w):
        return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{f}/{file}') format('woff2');}}"
    return (ff("Naskh", "noto-naskh-arabic-arabic-400-normal.woff2", 400) + ff("Naskh", "noto-naskh-arabic-arabic-700-normal.woff2", 700) +
            ff("Nastaliq", "noto-nastaliq-urdu-arabic-400-normal.woff2", 400) +
            ff("Nastaliq", "noto-nastaliq-urdu-arabic-700-normal.woff2", 700))


CSS = r"""
@page { size: 431.04pt 649.92pt; margin: 40pt 54pt 46pt 54pt; }
:root { --cream:#f5efe2; --maroon:#7a1f1f; --gold:#a3823a; --ink:#2b221c; --box:#ece3cf; --hbox:#efe2da; --ar:'Naskh','DejaVu Sans','FreeSerif',serif; }
* { box-sizing: border-box; }
html { background: var(--cream); }
body { margin:0; background: var(--cream); color: var(--ink);
  font-family: 'Liberation Serif','Times New Roman',serif; font-size: 10.1pt; line-height: 1.55; }
.a { font-family: var(--ar); font-size: 1.05em; line-height:1.6; }
.pbuh { font-family: 'Naskh','FreeSerif',serif; font-size: 1.05em; }
.chapter { break-before: page; }
.chapter:first-of-type { break-before: auto; }
p { margin: 0 0 8pt 0; text-align: justify; hyphens: manual; orphans: 2; widows: 2; }
b { font-weight: 700; }
.eyebrow { text-align:center; letter-spacing: 2.2pt; color: var(--maroon); font-size: 8.6pt; margin-top: 30pt; }
.ar-title { text-align:center; color: var(--maroon); font-family: var(--ar); font-size: 50pt; line-height: 1.5; margin-top: 8pt; }
.ar-title.s2 { font-size: 30pt; line-height:1.7; } .ar-title.s3 { font-size: 21pt; line-height:1.9; }
.tr { text-align:center; color: var(--maroon); font-style: italic; font-size: 17pt; margin-top: 2pt; direction: ltr; }
.en { text-align:center; font-weight: 700; font-size: 12.5pt; margin-top: 11pt; }
.ur { text-align:center; font-family: var(--ar); font-size: 13pt; margin-top: 10pt; color:#3b2f28; }
.rule { width: 84pt; height: 1.4pt; background: var(--gold); margin: 20pt auto 36pt auto; }
h2 { color: var(--maroon); font-size: 12.8pt; margin: 18pt 0 9pt 0; padding-bottom: 5pt; border-bottom: 1pt solid var(--gold); break-after: avoid; }
h3 { color: var(--maroon); font-size: 10.6pt; margin: 12pt 0 6pt 0; break-after: avoid; }
h3.pat { margin-top: 12pt; }
ul.dash { list-style: none; padding: 0; margin: 0 0 8pt 8pt; }
ul.dash li { position: relative; padding-left: 15pt; margin-bottom: 3pt; text-align: justify; }
ul.dash li::before { content: "\25C6"; font-size: 5.5pt; position:absolute; left:2pt; top: 0.55em; color: var(--gold); }
.rootrow { display:flex; gap: 14pt; align-items:center; margin: 0 0 10pt 0; break-inside: avoid; }
.rootbox { flex: 0 0 79pt; height: 63pt; background: var(--maroon); color: #f0dfc0; border-radius: 6pt; text-align:center; padding-top: 12pt; }
.rl { font-family: var(--ar); font-size: 17pt; letter-spacing: 3pt; line-height: 1.2; }
.rs { font-size: 6.5pt; letter-spacing: 1pt; color: #d9b977; margin-top: 8pt; }
.rtx { font-style: italic; line-height: 1.5; }
.rtx-ar { font-weight:700; font-family: var(--ar); font-size: 1.1em; }
.rtx-h { margin-bottom: 1pt; }
.defbox { border: 1pt solid var(--gold); background: var(--box); border-radius: 7pt; padding: 10pt 14pt; text-align:center; color: var(--maroon); font-weight:700; margin: 11pt 0 9pt 0; break-inside: avoid; }
.relbox { background: var(--box); border: 0.8pt solid #d9c9a4; border-radius: 7pt; padding: 9pt 13pt; margin: 10pt 0 6pt 0; font-size: 9.4pt; break-inside: avoid; }
.relh { color: var(--maroon); font-weight:700; margin-bottom: 3pt; }
.ayah { background: var(--box); border-right: 2.4pt solid var(--gold); padding: 10pt 12pt 8pt 14pt; margin: 9pt 0 10pt 0; break-inside: avoid; }
.ayar { text-align: right; color: var(--maroon); font-family: var(--ar); font-size: 15pt; line-height: 1.95; }
.aytr { font-style: italic; margin-top: 6pt; line-height: 1.5; }
.ref { color: var(--maroon); font-size: 8.5pt; margin-top: 4pt; }
.hadith { background: var(--hbox); border-left: 2.4pt solid var(--maroon); padding: 9pt 12pt 8pt 14pt; margin: 9pt 0 10pt 0; break-inside: avoid; }
.hdar { text-align:right; color: var(--maroon); font-family: var(--ar); font-size: 13.4pt; line-height: 1.95; }
.hdtr { margin-top: 5pt; line-height:1.5; }
.essence { background: var(--maroon); color: #f6ecd6; border-radius: 8pt; padding: 12pt 14pt; margin: 4pt 0 10pt 0; break-inside: avoid; }
.esslab { color: #d9b977; letter-spacing: 1.6pt; font-size: 8.4pt; margin-bottom: 6pt; }
.question { text-align:center; color: var(--maroon); font-style: italic; margin: 10pt 12pt 4pt 12pt; }
table.tbl { width:100%; border-collapse: collapse; margin: 8pt 0 10pt 0; font-size: 9.3pt; break-inside: avoid; }
.tbl th { background: var(--maroon); color:#f4e6c8; text-align:left; padding: 7pt 8pt; font-size: 9.3pt; }
.tbl td { padding: 7pt 8pt; border-bottom: 0.7pt solid #d9c9a4; vertical-align: top; line-height: 1.45; }
.tbl td.k { color: var(--maroon); font-weight:700; width: 24%; }
.sch { margin: 0 0 8pt 0; break-inside: avoid; }
.schn { color: var(--maroon); font-weight:700; font-size: 9.6pt; margin-bottom: 1pt; }
.scar { text-align:right; font-family: var(--ar); font-size: 12.4pt; line-height: 1.9; }
.scen { font-style: italic; line-height: 1.5; font-size: 9.6pt; }
.pair { display:flex; margin: 8pt 0 0 0; break-inside: avoid; }
.pair div { flex:1; text-align:center; padding: 9pt 8pt 8pt 8pt; color:#f6ecd6; }
.pair .m { background: var(--maroon); } .pair .g { background: var(--gold); }
.pair .pa { font-family: var(--ar); font-size: 14.5pt; } .pair .pl { letter-spacing: 1.2pt; font-size: 8pt; margin-top: 3pt; }
.card { background: var(--box); border: 0.8pt solid #d9c9a4; border-radius: 0 0 7pt 7pt; padding: 10pt 13pt 4pt 13pt; margin-bottom: 10pt; }
.title-page { text-align:center; padding-top: 96pt; }
.toc { margin: 0; padding:0; list-style:none; }
.toc li { display:flex; align-items:baseline; gap: 6pt; margin: 0 0 1.6pt 0; font-size: 9.4pt; line-height:1.15; }
.toc .a { line-height:1.1; }
.toc .tn { width: 16pt; color: var(--gold); text-align:right; }
.toc .tt { color: var(--ink); } .toc .ta { margin-left:auto; color:var(--maroon); font-family: var(--ar); font-size: 10.5pt; }
.toc .tp { width: 18pt; text-align:right; color: var(--maroon); }
.toc .dots { flex:1; border-bottom: 0.8pt dotted #b99a55; transform: translateY(-2pt); }
.note { font-size: 9.3pt; color:#4a3d34; }
.glance td, .glance th { padding: 2.4pt 6pt; font-size: 8.8pt; line-height:1.2; }
.glance .a { font-size: 10.5pt; }
table.tbl.glance { break-inside: auto; }
.glance tr { break-inside: avoid; }
.subm { text-align:center; font-style: italic; font-size: 9.6pt; color:#5a4a3f; margin-top: 3pt; direction:ltr; }
"""

URDU_CSS = r"""
html { direction: rtl; }
body.u { direction: rtl; font-family: 'Nastaliq','Naskh',serif; font-size: 10.3pt; line-height: 2.3; }
body.u p { text-align: justify; margin-bottom: 7pt; }
body.u .eyebrow { letter-spacing: 0; font-size: 10pt; margin-top: 26pt; }
body.u .tr { direction: ltr; }
body.u .urmain { font-family: 'Nastaliq',serif; font-size: 13.5pt; line-height: 2.1; font-weight: 700; margin-top: 8pt; }
body.u h2 { font-size: 13.5pt; line-height: 2; padding-bottom: 2pt; }
body.u h3 { font-size: 11pt; line-height: 2; }
body.u ul.dash { margin: 0 8pt 8pt 0; }
body.u ul.dash li { padding-left: 0; padding-right: 15pt; }
body.u ul.dash li::before { left: auto; right: 2pt; top: 1.1em; }
body.u .rtx { font-style: normal; line-height: 2; }
body.u .rtx-ar { margin-bottom: 2pt; }
body.u .rl { direction: rtl; }
body.u .rs { font-family: 'Nastaliq'; letter-spacing: 0; font-size: 8pt; }
body.u .esslab { font-family: 'Nastaliq'; letter-spacing: 0; font-size: 9pt; }
body.u .essence { line-height: 2.3; }
body.u .defbox { font-size: 10pt; line-height: 2.3; }
body.u .aytr { font-style: normal; font-size: 9.6pt; line-height: 2.2; text-align: justify; }
body.u .ref { font-size: 8.5pt; line-height: 1.8; }
body.u .hadith { border-left: 0; border-right: 2.4pt solid var(--maroon); padding: 9pt 14pt 8pt 12pt; }
body.u .hdtr { line-height: 2.2; }
body.u .question { font-style: normal; line-height: 2.3; }
body.u .relbox { font-size: 9.2pt; line-height: 2; }
body.u .tbl th { text-align: right; font-family: 'Nastaliq'; }
body.u .tbl td { line-height: 2; font-size: 9pt; }
body.u .scen, body.u .note { font-style: normal; line-height: 2.2; }
body.u .sch .schn { line-height: 2; }
body.u .subm { font-family: 'Liberation Serif'; }
body.u .toc li { line-height: 1.3; }
body.u .toc .tn { text-align: left; }
body.u .toc .ta { margin-left: 0; margin-right: auto; }
body.u .toc .tp { text-align: left; }
body.u .glance td { line-height: 1.35; padding: 1.6pt 6pt; }
body.u .glance .urc { font-size: 9pt; line-height: 1.7; }
body.u .title-page .tr { direction: ltr; }
body.u .pair .pl { font-family: 'Nastaliq'; letter-spacing: 0; font-size: 8.5pt; }
body.u .card p { line-height: 2.25; }
"""


def page(body):
    lang = LANG
    extra = URDU_CSS if lang == "ur" else ""
    cls = ' class="u"' if lang == "ur" else ""
    title = ("اسماءُ اللہ الحسنیٰ، حصہ اول: نام 1 تا 33" if lang == "ur"
             else "The 99 Names of Allah, Part One: Names 1 to 33")
    return f"""<!doctype html><html lang="{lang}" dir="{'rtl' if lang == 'ur' else 'ltr'}"><head><meta charset="utf-8">
<title>{title}</title><style>{font_css()}{CSS}{extra}</style></head><body{cls}>{body}</body></html>"""
