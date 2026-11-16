"""Assemble the full book: python3 make_book.py OUTPUT.pdf"""
import sys, os, re, subprocess, tempfile, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
import lib
import original, content_a, content_b, content_c, front
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
RENDER = os.path.join(HERE, "render_pdf.cjs")


def render(html_text, pdf_path, tmpdir, name):
    h = os.path.join(tmpdir, name + ".html")
    open(h, "w", encoding="utf-8").write(page(html_text))
    subprocess.run(["node", RENDER, h, pdf_path], check=True)
    return pdf_path


def name_pages():
    """Ordered list of (key, html) for the body, key used to find the page number."""
    A = {d["n"]: d for d in content_a.ALL}
    B = {d["n"]: d for d in content_b.ALL}
    C = {d["n"]: d for d in content_c.ALL}
    allnames = {**A, **B, **C}
    seq = [("N1", original.name1()), ("N2", original.name2()), ("T12", original.together12()), ("N3", original.name3())]
    for n in range(4, 14):
        seq.append((f"N{n}", render_name(allnames[n])))
    seq.append(("T1113", content_a.trio_1113()))
    for n in range(14, 26):
        seq.append((f"N{n}", render_name(allnames[n])))
    seq.append(("T2025", content_b.pairs_2025()))
    for n in range(26, 34):
        seq.append((f"N{n}", render_name(allnames[n])))
    return seq, allnames


TOC_ROWS = [  # key, label, title, arabic
    ("N1", "1", "Ar-Rahman", "الرَّحْمٰنُ"), ("N2", "2", "Ar-Raheem", "الرَّحِيمُ"),
    ("T12", "", "Ar-Rahman & Ar-Raheem — Together", ""),
    ("N3", "3", "Al-Malik", "الْمَلِكُ"),
    ("N4", "4", "Al-Quddus", "الْقُدُّوسُ"), ("N5", "5", "As-Salam", "السَّلَامُ"), ("N6", "6", "Al-Mu'min", "الْمُؤْمِنُ"),
    ("N7", "7", "Al-Muhaymin", "الْمُهَيْمِنُ"), ("N8", "8", "Al-'Aziz", "الْعَزِيزُ"), ("N9", "9", "Al-Jabbar", "الْجَبَّارُ"),
    ("N10", "10", "Al-Mutakabbir", "الْمُتَكَبِّرُ"), ("N11", "11", "Al-Khaliq", "الْخَالِقُ"), ("N12", "12", "Al-Bari'", "الْبَارِئُ"),
    ("N13", "13", "Al-Musawwir", "الْمُصَوِّرُ"), ("T1113", "", "Al-Khaliq, Al-Bari' & Al-Musawwir — Together", ""),
    ("N14", "14", "Al-Ghaffar", "الْغَفَّارُ"), ("N15", "15", "Al-Qahhar", "الْقَهَّارُ"), ("N16", "16", "Al-Wahhab", "الْوَهَّابُ"),
    ("N17", "17", "Ar-Razzaq", "الرَّزَّاقُ"), ("N18", "18", "Al-Fattah", "الْفَتَّاحُ"), ("N19", "19", "Al-'Alim", "الْعَلِيمُ"),
    ("N20", "20", "Al-Qabid", "الْقَابِضُ"), ("N21", "21", "Al-Basit", "الْبَاسِطُ"), ("N22", "22", "Al-Khafid", "الْخَافِضُ"),
    ("N23", "23", "Ar-Rafi'", "الرَّافِعُ"), ("N24", "24", "Al-Mu'izz", "الْمُعِزُّ"), ("N25", "25", "Al-Mudhill", "الْمُذِلُّ"),
    ("T2025", "", "The Names That Come in Pairs — Together", ""),
    ("N26", "26", "As-Sami'", "السَّمِيعُ"), ("N27", "27", "Al-Basir", "الْبَصِيرُ"), ("N28", "28", "Al-Hakam", "الْحَكَمُ"),
    ("N29", "29", "Al-'Adl", "الْعَدْلُ"), ("N30", "30", "Al-Latif", "اللَّطِيفُ"), ("N31", "31", "Al-Khabir", "الْخَبِيرُ"),
    ("N32", "32", "Al-Halim", "الْحَلِيمُ"), ("N33", "33", "Al-'Azim", "الْعَظِيمُ"),
]


SEARCH = {"N1": "The Vastly & Abundantly Merciful", "N2": "The Especially & Continually Merciful",
          "T12": "Differences, Equalities & What the Scholars Say", "N3": "The Absolute King & Sovereign",
          "T1113": "Three Names, One Ayah, One Complete Picture of Creation",
          "T2025": "Al-Qabid & Al-Basit \u00b7 Al-Khafid & Ar-Rafi' \u00b7 Al-Mu'izz & Al-Mudhill"}


def find_pages(body_pdf, allnames):
    """Sequential search of each chapter's cover line; returns {key: 1-based page in body}."""
    for n, d in allnames.items():
        SEARCH[f"N{n}"] = d["en"]
    order = [k for k, _, _, _ in TOC_ROWS]
    r = PdfReader(body_pdf)
    texts = [re.sub(r"\s+", "", (pg.extract_text() or "")) for pg in r.pages]
    found, i = {}, 0
    for k in order:
        key = re.sub(r"\s+", "", lib.deai(SEARCH[k]))
        while i < len(texts) and key not in texts[i]:
            i += 1
        if i >= len(texts):
            raise SystemExit("cover not found for " + k)
        found[k] = i + 1
        i += 1
    return found


def numbers_pdf(total, first_numbered, tmp):
    css = "@page{size:431.04pt 649.92pt;margin:0}html,body{margin:0;background:transparent}.pg{width:431.04pt;height:649.92pt;position:relative;break-after:page;overflow:hidden}.n{position:absolute;bottom:22pt;left:0;right:0;text-align:center;font-family:'Liberation Serif',serif;font-size:9pt;color:#a3823a;letter-spacing:1pt}"
    body = "".join(f'<div class="pg"><div class="n">{i if i >= first_numbered else ""}</div></div>' for i in range(1, total + 1))
    h = os.path.join(tmp, "nums.html")
    open(h, "w").write(f"<!doctype html><meta charset=utf-8><style>{css}</style><body>{body}</body>")
    out = os.path.join(tmp, "nums.pdf")
    subprocess.run(["node", RENDER, h, out], check=True)
    return out


def bg_pdf(tmp):
    h = os.path.join(tmp, "bg.html")
    open(h, "w").write("<!doctype html><meta charset=utf-8><style>@page{size:431.04pt 649.92pt;margin:0}html,body{margin:0;background:#f5efe2;width:431.04pt;height:649.92pt}</style><body></body>")
    out = os.path.join(tmp, "bg.pdf")
    subprocess.run(["node", RENDER, h, out], check=True)
    return out


def main(out_pdf, lang="en"):
    global TITLE
    lib.set_lang(lang)
    TITLE = "اسماءُ اللہ الحسنیٰ، حصہ اول: نام 1 تا 33" if lang == "ur" else "The 99 Names of Allah, Part One: Names 1 to 33"
    tmp = tempfile.mkdtemp(prefix="book_")
    seq, allnames = name_pages()
    body_html = "\n".join(h for _, h in seq)
    body_pdf = render(body_html, os.path.join(tmp, "body.pdf"), tmp, "body")
    pages = find_pages(body_pdf, allnames)
    nbody = len(PdfReader(body_pdf).pages)

    # build glance rows
    rows = [("1", "الرَّحْمٰنُ", "Ar-Rahman", "The Vastly & Abundantly Merciful"),
            ("2", "الرَّحِيمُ", "Ar-Raheem", "The Especially & Continually Merciful"),
            ("3", "الْمَلِكُ", "Al-Malik", "The Absolute King & Sovereign")]
    for n in range(4, 34):
        d = allnames[n]
        rows.append((str(n), d["ar"], d["tr"], d["en"]))

    def front_html(offset):
        toc = [(num, title, ar, (str(pages[k] + offset) if k in pages else "")) for k, num, title, ar in TOC_ROWS]
        toc.append(("", "The First 33 at a Glance", "", str(nbody + offset + 1)))
        toc.append(("", "Sources & Notes", "", str(nbody + offset + 2 + 1)))
        return front.title_page() + front.intro_page() + front.contents_page(toc)

    f_pdf = render(front_html(0), os.path.join(tmp, "front.pdf"), tmp, "front")
    nf = len(PdfReader(f_pdf).pages)
    # glance may take >1 page: measure the tail first
    tail_html = front.glance_page(rows) + front.sources_page()
    tail_pdf = render(tail_html, os.path.join(tmp, "tail.pdf"), tmp, "tail")
    tr_ = PdfReader(tail_pdf)
    glance_pages = 0
    for pg in tr_.pages:
        t = re.sub(r"\s+", "", pg.extract_text() or "")
        if "SOURCES&NOTES" in t.upper() and "NOTES" in t:
            break
        glance_pages += 1
    # second pass with real offsets (glance starts after body; sources after glance)
    def front_html2(offset):
        toc = [(num, title, ar, str(pages[k] + offset)) for k, num, title, ar in TOC_ROWS]
        toc.append(("", "The First 33 at a Glance", "", str(offset + nbody + 1)))
        toc.append(("", "Sources & Notes", "", str(offset + nbody + glance_pages + 1)))
        return front.title_page() + front.intro_page() + front.contents_page(toc)
    f_pdf = render(front_html2(nf), os.path.join(tmp, "front.pdf"), tmp, "front")
    assert len(PdfReader(f_pdf).pages) == nf

    parts = [f_pdf, body_pdf, tail_pdf]
    total = nf + nbody + len(tr_.pages)
    bgp = bg_pdf(tmp)
    nump = numbers_pdf(total, 2, tmp)
    nr = PdfReader(nump)
    w = PdfWriter()
    idx = 0
    for part in parts:
        for pg in PdfReader(part).pages:
            base = PdfReader(bgp).pages[0]
            base.merge_page(pg)
            base.merge_page(nr.pages[idx])
            w.add_page(base)
            idx += 1
    w.add_metadata({"/Title": TITLE, "/Author": "", "/Producer": "", "/Creator": ""})
    w.write(out_pdf)
    print("pages:", idx, "front:", nf, "body:", nbody, "tail:", len(tr_.pages), "glance:", glance_pages)
    for k in lib.MISSING: print("MISSING:", k[:120])
    print("toc keys found:", len(pages), "of", len(TOC_ROWS))
    return tmp


if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "en"))
