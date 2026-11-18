"""Draws pages in the same style as the adjective book: Letter size, Helvetica, same margins,
colours, font sizes and box geometry (measured from the original ReportLab content streams)."""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, KeepTogether, PageBreak, Flowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import Color
from reportlab.pdfbase.pdfmetrics import stringWidth
from xml.sax.saxutils import escape

NAVY = Color(.121569, .227451, .372549); GOLD = Color(.788235, .635294, .152941)
RED = Color(.752941, .223529, .168627); GREEN = Color(.117647, .443137, .270588)
PURPLE = Color(.482353, .247059, .627451); DARK = Color(.168627, .168627, .168627)
GREY = Color(.419608, .419608, .419608); GBOX = Color(.94902, .94902, .94902)
YBOX = Color(.992157, .952941, .85098); PFILL = Color(.960784, .929412, .980392)
FW = 477.6; CX = FW / 2          # frame width and its centre
H, HB, HO = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'

def _ps(name, font, size, lead, color, **kw): return ParagraphStyle(name, fontName=font, fontSize=size, leading=lead, textColor=color, **kw)
S_TITLE = _ps('t', HB, 22, 26, NAVY, alignment=TA_CENTER, spaceAfter=4)
S_SUB = _ps('s', HO, 11, 12, GOLD, alignment=TA_CENTER, spaceAfter=8)
S_WRONG = _ps('w', H, 10.5, 12, RED, leftIndent=12, spaceAfter=3)
S_RIGHT = _ps('r', HB, 10.5, 12, GREEN, leftIndent=12)
S_HRED = _ps('hr', HB, 10.5, 12, RED, spaceBefore=8, spaceAfter=4)
S_HGRN = _ps('hg', HB, 10.5, 12, GREEN, spaceBefore=10, spaceAfter=4)
S_GREY = _ps('g', HO, 9.5, 13.5, DARK)
S_YEL = _ps('y', HB, 9.8, 13.5, DARK)
S_VT = _ps('v', HB, 10.5, 12, NAVY, alignment=TA_CENTER, spaceBefore=10)
Z = lambda ch: f'<font name="ZapfDingbats">{ch}</font>'
X, OK = Z('7'), Z('3')
e = escape

class BoxPara(Flowable):
    def __init__(s, text, style, fill, border=None, indent=12, px=10, py=8):
        super().__init__(); s.text, s.style, s.fill, s.border, s.ind, s.px, s.py = text, style, fill, border, indent, px, py
    def wrap(s, aw, ah):
        s.p = Paragraph(s.text, s.style); _, ph = s.p.wrap(FW - 2 * s.ind - 2 * s.px, ah); s.h = ph + 2 * s.py; return FW, s.h
    def draw(s):
        c = s.canv; w = FW - 2 * s.ind
        c.setFillColor(s.fill); c.rect(s.ind, 0, w, s.h, stroke=0, fill=1)
        if s.border: c.setStrokeColor(s.border); c.setLineWidth(1); c.rect(s.ind, 0, w, s.h, stroke=1, fill=0)
        s.p.drawOn(c, s.ind + s.px, s.py)

class Viz(Flowable):
    def __init__(s, ops): super().__init__(); s.ops = ops
    def wrap(s, aw, ah): s.h = sum(h for h, _ in s.ops); return FW, s.h
    def draw(s):
        y = s.h
        for h, fn in s.ops:
            fn(s.canv, y); y -= h

class VB:
    """Builds a visualisation top to bottom. Every op has a height and a draw function."""
    def __init__(s): s.ops = []
    def add(s, h, fn): s.ops.append((h, fn)); return s
    def gap(s, h): return s.add(h, lambda c, y: None)
    def build(s): return Viz(list(s.ops))
    def text(s, t, size=9.5, color=DARK, font=HB, h=None, x=CX):
        h = h or size * 1.25 + 3
        def fn(c, y): c.setFillColor(color); c.setFont(font, size); c.drawCentredString(x, y - h / 2 - size * .33, t)
        return s.add(h, fn)
    def cap(s, t, size=8.3, color=GREY, font=HO, x=CX): return s.text(t, size, color, font, h=size * 1.2 + 3, x=x)
    def head(s, t): return s.text(t, 10.5, GOLD, HB, h=20)
    def sub(s, t): return s.text(t, 9.5, NAVY, HB, h=16)
    def sep(s):
        def fn(c, y): c.setStrokeColor(GOLD); c.setLineWidth(1); c.line(19.2, y - 23.6, 458.4, y - 23.6)
        return s.add(35, fn)
    def arrow(s, xs=(CX,), ln=14, color=DARK, w=1.2):
        def fn(c, y):
            c.setStrokeColor(color); c.setLineWidth(w)
            for x in xs:
                c.line(x, y - 7.6, x, y - 7.6 - ln); c.line(x, y - 7.6 - ln, x - 4, y - 7.6 - ln + 7); c.line(x, y - 7.6 - ln, x + 4, y - 7.6 - ln + 7)
        return s.add(ln + 11, fn)
    def split(s, xs, color=DARK, ln=12):
        def fn(c, y):
            c.setStrokeColor(color); c.setLineWidth(1.2); c.line(CX, y - 2, CX, y - 8); c.line(min(xs), y - 8, max(xs), y - 8)
            for x in xs:
                c.line(x, y - 8, x, y - 8 - ln); c.line(x, y - 8 - ln, x - 4, y - 8 - ln + 7); c.line(x, y - 8 - ln, x + 4, y - 8 - ln + 7)
        return s.add(ln + 12, fn)
    def pill(s, t, size=10.5, color=PURPLE):
        w = stringWidth(t, HB, size) + 62
        def fn(c, y):
            c.setStrokeColor(color); c.setFillColor(PFILL); c.setLineWidth(1.3)
            c.roundRect(CX - w / 2, y - 32, w, 30, 6.6, stroke=1, fill=1)
            c.setFillColor(color); c.setFont(HB, size); c.drawCentredString(CX, y - 21.5, t)
        return s.add(36, fn)
    def result(s, t, color=GREEN, glyph='3', size=10.5):
        def fn(c, y):
            wz = stringWidth(glyph, 'ZapfDingbats', size); wt = stringWidth('  ' + t, HB, size); x0 = CX - (wz + wt) / 2
            c.setFillColor(color); c.setFont('ZapfDingbats', size); c.drawString(x0, y - 15, glyph)
            c.setFont(HB, size); c.drawString(x0 + wz, y - 15, '  ' + t)
        return s.add(22, fn)
    def bad(s, t, size=10): return s.result(t, RED, '7', size)
    def row(s, items, h=24, size=10.5, frame=None, links=None):
        """items: dict(t, w, x, c, size, cap, capc, k='txt' for plain text, hl=fill colour)"""
        gap = 14; ws = []
        for it in items:
            sz = it.get('size', size); it['_sz'] = sz
            ws.append(it.get('w') or max(it.get('minw', 56), stringWidth(it['t'], HB, sz) + 24) if it.get('k') != 'txt' else (it.get('w') or stringWidth(it['t'], HB, sz) + 8))
        tot = sum(ws) + gap * (len(items) - 1); x0 = CX - tot / 2; xs = []
        for w in ws: xs.append(x0 + w / 2); x0 += w + gap
        for i, it in enumerate(items):
            if 'x' in it: xs[i] = CX + it['x']
        capn = max([len(it['cap']) if isinstance(it.get('cap'), list) else (1 if it.get('cap') else 0) for it in items] + [0])
        frt, frb = (16, 8) if frame else (0, 0)
        lk = 12 if links else 0
        total = h + 6 + frt + frb + (capn * 11 + 11.4 if capn else 0) + lk
        def fn(c, y):
            top = y - 3 - frt - lk
            if frame:
                i0, i1, lab = frame; xa = xs[i0] - ws[i0] / 2 - 8; xb = xs[i1] + ws[i1] / 2 + 8
                c.setStrokeColor(GOLD); c.setLineWidth(1.3); c.roundRect(xa, top - h - 6, xb - xa, h + 12, 6, stroke=1, fill=0)
                c.setFillColor(GOLD); c.setFont(HB, 8.5); c.drawCentredString((xa + xb) / 2, top + 10, lab)
            for it, x, w in zip(items, xs, ws):
                col = it.get('c', NAVY); sz = it['_sz']
                if it.get('k') == 'txt':
                    c.setFillColor(it.get('c', DARK)); c.setFont(HB, sz); c.drawCentredString(x, top - h / 2 - sz * .33, it['t'])
                else:
                    c.setLineWidth(1.3); c.setStrokeColor(col)
                    if it.get('hl'): c.setFillColor(it['hl']); c.rect(x - w / 2, top - h, w, h, stroke=1, fill=1)
                    else: c.rect(x - w / 2, top - h, w, h, stroke=1, fill=0)
                    c.setFillColor(col); c.setFont(HB, sz); c.drawCentredString(x, top - h / 2 - sz * .33, it['t'])
                cp = it.get('cap')
                if cp:
                    for k, line in enumerate(cp if isinstance(cp, list) else [cp]):
                        c.setFillColor(it.get('capc', GREY)); c.setFont(it.get('capf', HO), it.get('caps', 8.3)); c.drawCentredString(x, top - h - 12 - (8 if frame else 0) - k * 11, line)
            for (i, j, lab) in (links or []):
                xa = xs[i] + ws[i] / 2 + 3; xb = xs[j] - ws[j] / 2 - 3; ym = top - h / 2
                c.setStrokeColor(GREY); c.setLineWidth(.8); c.line(xa, ym, xb, ym)
                if lab: c.setFillColor(GREY); c.setFont(HO, 8); c.drawCentredString((xa + xb) / 2, top + 2, lab)
        return s.add(total, fn)
    def cmp(s, l, r, ok, color, size=9.3, h=16):
        sym = '=' if ok else '\u2260'
        def fn(c, y):
            wl = stringWidth(l, HB, size); wr = stringWidth(r, HB, size); sw = stringWidth(sym, 'Symbol', size); g = 9
            x0 = CX - (wl + wr + sw + 2 * g) / 2; yb = y - h / 2 - size * .33
            c.setFillColor(color); c.setFont(HB, size); c.drawString(x0, yb, l)
            c.setFont('Symbol', size); c.drawString(x0 + wl + g, yb, sym)
            c.setFont(HB, size); c.drawString(x0 + wl + sw + 2 * g, yb, r)
        return s.add(h, fn)
    def texts(s, items, h=16):
        def fn(c, y):
            for t, x, size, color, font in items:
                c.setFillColor(color); c.setFont(font, size); c.drawCentredString(x, y - h / 2 - size * .33, t)
        return s.add(h, fn)

def pairs(pp):
    out = []
    for i, (w, r) in enumerate(pp):
        out += [Paragraph(f'{X} {e(w)}', S_WRONG), Paragraph(f'{OK} {e(r)}', S_RIGHT)]
        if i < len(pp) - 1: out.append(Spacer(0, 7))
    return out

def error(n, subtitle, pp, old, logic, viz_flow):
    """One error: title block, old-school-rule box, logic box, then the visualisation flowables."""
    out = [Paragraph(f'ERROR {n}', S_TITLE), Paragraph(e(subtitle), S_SUB)]
    out += pairs(pp)
    out += [Spacer(0, 8), Paragraph(f'{X} OLD SCHOOL RULE: SKIP THIS', S_HRED), BoxPara(e(old), S_GREY, GBOX),
            Paragraph(f'{OK} THE LOGIC', S_HGRN), BoxPara(e(logic), S_YEL, YBOX, border=GOLD), Spacer(0, 4),
            Paragraph('LOGIC VISUALIZATION', S_VT), Spacer(0, 6)]
    return out + viz_flow

def build(path, story):
    doc = BaseDocTemplate(path, pagesize=letter, leftMargin=67.2, rightMargin=67.2, topMargin=56.4, bottomMargin=48, title='Adjective errors', author='')
    doc.addPageTemplates([PageTemplate(id='p', frames=[Frame(67.2, 48, FW, 792 - 56.4 - 48, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)])])
    doc.build(story)
