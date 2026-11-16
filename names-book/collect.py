import sys, json
sys.path.insert(0,'.')
import lib, make_book, front
lib.set_lang('en'); lib.COLLECT={}
seq,allnames=make_book.name_pages()
front.title_page(); front.intro_page()
front.contents_page([("","The First 33 at a Glance","","")]); front.contents_page([("","Sources & Notes","","")])
for k,num,title,ar in make_book.TOC_ROWS: lib.T(title)
rows=[(str(n),d["ar"],d["tr"],d["en"]) for n,d in allnames.items()]
front.glance_page(rows); front.sources_page()
lib.T("Name"); lib.T("Meaning")
keys=list(lib.COLLECT)
json.dump(keys,open('ur/todo.json','w'),ensure_ascii=False,indent=0)
print(len(keys), sum(len(k.split()) for k in keys))
