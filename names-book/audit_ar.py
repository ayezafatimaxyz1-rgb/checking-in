import sys, re, json, unicodedata, html
sys.path.insert(0,'.')
import lib
from lib import ARABIC_RUN
runs=[]
orig_md=lib.md
def logmd(t):
    for m in ARABIC_RUN.finditer(t): runs.append(m.group(0))
    return orig_md(t)
lib.md=logmd
import make_book
for n in ('p','h2','h3','bullets','box','related','ayah_box','hadith_box','essence','question','table','scholar','chapter_open','root_row','pattern_head'):
    pass
seq,_=make_book.name_pages()
# also raw arabic fields rendered without md
html_all="\n".join(h for _,h in seq)
raw=[m.group(0) for m in ARABIC_RUN.finditer(html.unescape(re.sub(r'<[^>]+>',' ',html_all)))]
def norm(s):
    s=unicodedata.normalize('NFC',s)
    s=re.sub(r'[ً-ٰٟۖ-ۭـ]','',s)
    s=s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ئ','ي').replace('ؤ','و').replace('ة','ه')
    return s
q=json.load(open('data/quran.json'))
corpus=" ".join(norm(v['text']) for s in q for v in s['verses'])
allr=sorted(set(raw))
nf=[]
for r in allr:
    n=norm(r).strip()
    if n and n not in corpus: nf.append(r)
print(len(allr),'unique runs;',len(nf),'not in Qur\'an text')
for r in nf: print(r)
