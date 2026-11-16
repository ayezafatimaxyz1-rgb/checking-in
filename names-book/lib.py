"""Shared helpers + CSS for the 99 Names book generator."""
import json, re, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
_QURAN = None
_QURAN_EN = None


def _load():
    global _QURAN, _QURAN_EN
    if _QURAN is None:
        base = os.path.join(HERE, "data")
        _QURAN = json.load(open(os.path.join(base, "quran.json"), encoding="utf-8"))
        _QURAN_EN = json.load(open(os.path.join(base, "quran_en.json"), encoding="utf-8"))


def verse(s, a):
    _load()
    ar = [x for x in _QURAN[s - 1]["verses"] if x["id"] == a][0]["text"]
    en = [x for x in _QURAN_EN[s - 1]["verses"] if x["id"] == a][0]["translation"]
    return ar, en


def clean_ar(t):
    # drop the sajda/hizb sign that precedes some verses and normalise alef wasla for display
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
    lines, trs = [], []
    for k in range(a, last + 1):
        ar, en = verse(s, k)
        ar = clean_ar(ar)
        if words:
            w = ar.split()
            ar = " ".join(w[words[0]:words[1]])
        lines.append(ar)
        trs.append(en.strip())
    en_all = clean_en(" ".join(trs)) if tr is None else tr
    ref = f"Qur'an {s}:{a}" + (f"–{b}" if b and b != a else "")
    return {"ar": lines, "en": en_all, "ref": ref}


ARABIC_RUN = re.compile(
    r"[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]+"
    r"(?:[  ]+[؀-ۿݐ-ݿࢠ-ࣿﭐ-﷿ﹰ-﻿]+)*")


def md(t):
    """Tiny inline markup: **bold**, *italic*, auto-wrap Arabic runs."""
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<i>\1</i>", t)
    t = t.replace("ﷺ", '<span class="pbuh">ﷺ</span>')
    t = ARABIC_RUN.sub(lambda m: f'<span class="a" dir="rtl">{m.group(0)}</span>', t)
    return t


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
    return f'<div class="relbox"><div class="relh">Related words</div><div>{md(t)}</div></div>'


def ayah_box(a):
    ar = "<br>".join(a["ar"])
    return (f'<div class="ayah"><div class="ayar" dir="rtl">{ar}</div>'
            f'<div class="aytr">{md(a["en"])}</div><div class="ref">{md(a["ref"])}</div></div>')


def hadith_box(ar, en, ref):
    arhtml = f'<div class="hdar" dir="rtl">{ar}</div>' if ar else ""
    return (f'<div class="hadith">{arhtml}<div class="hdtr">{md(en)}</div>'
            f'<div class="ref">{md(ref)}</div></div>')


def essence(en, ur=None):
    u = ""
    if ur:
        u = '<div class="essur" dir="rtl">' + "<br>".join(md(x) for x in ur) + "</div>"
    return f'<div class="essence"><div class="esslab">ESSENCE</div><div>{md(en)}</div>{u}</div>'


def question(t):
    return f'<p class="question">{md(t)}</p>'


def table(head, rows):
    h = "".join(f"<th>{md(x)}</th>" for x in head)
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
            f'<div class="rs">ROOT</div></div><div class="rtx">{hd}{ar}<div>{md(en_line)}</div></div></div>')


def pattern_head(name, pat):
    return f'<h3 class="pat">{md(name)} is on the pattern <span class="a" dir="rtl">{pat}</span></h3>'


def render_name(d):
    """Render one standard name chapter from a dict (see content files)."""
    n = d["n"]
    out = [chapter_open(f"NAME {n} OF 99", d["ar"], d["tr"], d["en"], d["ur"])]
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


CSS = r"""
@page { size: 431.04pt 649.92pt; margin: 40pt 54pt 46pt 54pt; }
:root { --cream:#f5efe2; --maroon:#7a1f1f; --gold:#a3823a; --ink:#2b221c; --box:#ece3cf; --hbox:#efe2da; }
* { box-sizing: border-box; }
html { background: var(--cream); }
body { margin:0; background: var(--cream); color: var(--ink);
  font-family: 'Liberation Serif','Times New Roman',serif; font-size: 10.1pt; line-height: 1.55; }
.a { font-family: 'DejaVu Sans','FreeSerif',sans-serif; font-size: 0.95em; line-height:1.4; }
.pbuh { font-family: 'FreeSerif','DejaVu Sans',serif; font-size: 1.1em; }
.chapter { break-before: page; }
.chapter:first-of-type { break-before: auto; }
p { margin: 0 0 8pt 0; text-align: justify; hyphens: manual; orphans: 2; widows: 2; }
b { font-weight: 700; }
.eyebrow { text-align:center; letter-spacing: 2.2pt; color: var(--maroon); font-size: 8.6pt; margin-top: 30pt; }
.ar-title { text-align:center; color: var(--maroon); font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 44pt; line-height: 1.5; margin-top: 8pt; }
.ar-title.s2 { font-size: 27pt; line-height:1.7; } .ar-title.s3 { font-size: 19pt; line-height:1.9; }
.tr { text-align:center; color: var(--maroon); font-style: italic; font-size: 17pt; margin-top: 2pt; }
.en { text-align:center; font-weight: 700; font-size: 12.5pt; margin-top: 11pt; }
.ur { text-align:center; font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 11.5pt; margin-top: 10pt; color:#3b2f28; }
.rule { width: 84pt; height: 1.4pt; background: var(--gold); margin: 20pt auto 36pt auto; }
h2 { color: var(--maroon); font-size: 12.8pt; margin: 18pt 0 9pt 0; padding-bottom: 5pt; border-bottom: 1pt solid var(--gold); break-after: avoid; }
h3 { color: var(--maroon); font-size: 10.6pt; margin: 12pt 0 6pt 0; break-after: avoid; }
h3.pat { margin-top: 12pt; }
ul.dash { list-style: none; padding: 0; margin: 0 0 8pt 8pt; }
ul.dash li { position: relative; padding-left: 15pt; margin-bottom: 3pt; text-align: justify; }
ul.dash li::before { content: "\2014"; position:absolute; left:0; color: var(--gold); }
.rootrow { display:flex; gap: 14pt; align-items:center; margin: 0 0 10pt 0; break-inside: avoid; }
.rootbox { flex: 0 0 79pt; height: 63pt; background: var(--maroon); color: #f0dfc0; border-radius: 6pt; text-align:center; padding-top: 12pt; }
.rl { font-family:'DejaVu Sans',sans-serif; font-size: 15pt; letter-spacing: 3pt; line-height: 1.2; }
.rs { font-size: 6.5pt; letter-spacing: 1pt; color: #d9b977; margin-top: 8pt; }
.rtx { font-style: italic; line-height: 1.5; }
.rtx-ar { font-weight:700; }
.rtx-h { margin-bottom: 1pt; }
.defbox { border: 1pt solid var(--gold); background: var(--box); border-radius: 7pt; padding: 10pt 14pt; text-align:center; color: var(--maroon); font-weight:700; margin: 11pt 0 9pt 0; break-inside: avoid; }
.relbox { background: var(--box); border: 0.8pt solid #d9c9a4; border-radius: 7pt; padding: 9pt 13pt; margin: 10pt 0 6pt 0; font-size: 9.4pt; break-inside: avoid; }
.relh { color: var(--maroon); font-weight:700; margin-bottom: 3pt; }
.ayah { background: var(--box); border-right: 2.4pt solid var(--gold); padding: 10pt 12pt 8pt 14pt; margin: 9pt 0 10pt 0; break-inside: avoid; }
.ayar { text-align: right; color: var(--maroon); font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 13.2pt; line-height: 1.85; }
.aytr { font-style: italic; margin-top: 6pt; line-height: 1.5; }
.ref { color: var(--maroon); font-size: 8.5pt; margin-top: 4pt; }
.hadith { background: var(--hbox); border-left: 2.4pt solid var(--maroon); padding: 9pt 12pt 8pt 14pt; margin: 9pt 0 10pt 0; break-inside: avoid; }
.hdar { text-align:right; color: var(--maroon); font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 11.6pt; line-height: 1.85; }
.hdtr { margin-top: 5pt; line-height:1.5; }
.essence { background: var(--maroon); color: #f6ecd6; border-radius: 8pt; padding: 12pt 14pt; margin: 4pt 0 10pt 0; break-inside: avoid; }
.esslab { color: #d9b977; letter-spacing: 1.6pt; font-size: 8.4pt; margin-bottom: 6pt; }
.essur { margin-top: 7pt; font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 9.8pt; line-height: 1.7; }
.essur .a { font-size: 1em; }
.question { text-align:center; color: var(--maroon); font-style: italic; margin: 10pt 12pt 4pt 12pt; }
table.tbl { width:100%; border-collapse: collapse; margin: 8pt 0 10pt 0; font-size: 9.3pt; break-inside: avoid; }
.tbl th { background: var(--maroon); color:#f4e6c8; text-align:left; padding: 7pt 8pt; font-size: 9.3pt; }
.tbl td { padding: 7pt 8pt; border-bottom: 0.7pt solid #d9c9a4; vertical-align: top; line-height: 1.45; }
.tbl td.k { color: var(--maroon); font-weight:700; width: 24%; }
.sch { margin: 0 0 8pt 0; break-inside: avoid; }
.schn { color: var(--maroon); font-weight:700; font-size: 9.6pt; margin-bottom: 1pt; }
.scar { text-align:right; font-family:'DejaVu Sans','FreeSerif',sans-serif; font-size: 10.6pt; line-height: 1.8; }
.scen { font-style: italic; line-height: 1.5; font-size: 9.6pt; }
.pair { display:flex; margin: 8pt 0 0 0; break-inside: avoid; }
.pair div { flex:1; text-align:center; padding: 9pt 8pt 8pt 8pt; color:#f6ecd6; }
.pair .m { background: var(--maroon); } .pair .g { background: var(--gold); }
.pair .pa { font-family:'DejaVu Sans',sans-serif; font-size: 12.5pt; } .pair .pl { letter-spacing: 1.2pt; font-size: 8pt; margin-top: 3pt; }
.card { background: var(--box); border: 0.8pt solid #d9c9a4; border-radius: 0 0 7pt 7pt; padding: 10pt 13pt 4pt 13pt; margin-bottom: 10pt; }
.title-page { text-align:center; padding-top: 96pt; }
.toc { margin: 0; padding:0; list-style:none; }
.toc li { display:flex; align-items:baseline; gap: 6pt; margin: 0 0 1.6pt 0; font-size: 9.4pt; line-height:1.15; }
.toc .a { line-height:1.1; }
.toc .tn { width: 16pt; color: var(--gold); text-align:right; }
.toc .tt { color: var(--ink); } .toc .ta { margin-left:auto; color:var(--maroon); font-family:'DejaVu Sans',sans-serif; font-size: 9.4pt; }
.toc .tp { width: 18pt; text-align:right; color: var(--maroon); }
.toc .dots { flex:1; border-bottom: 0.8pt dotted #b99a55; transform: translateY(-2pt); }
.note { font-size: 9.3pt; color:#4a3d34; }
"""


def page(body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>The 99 Names of Allah, Part One: Names 1 to 33</title><style>{CSS}</style></head><body>{body}</body></html>"""


CSS += """
.glance td, .glance th { padding: 2.4pt 6pt; font-size: 8.8pt; line-height:1.2; }
.glance .a { font-size: 10pt; }
"""

CSS += """
table.tbl.glance { break-inside: auto; }
.glance tr { break-inside: avoid; }
"""
