import json,re,sys
C={}
for c in ['bukhari','muslim','tirmidhi','abudawud','nasai','ibnmajah','ahmad']:
    C[c]=json.load(open(f'DATA_DIR/{c}.json'))
def get(c,n):
    out=[]
    for r in C[c]:
        i=str(r['id'])
        if re.fullmatch(rf'{n}[a-z]?',i): out.append(r)
    return out
refs=[l.split() for l in sys.argv[1:]]
for c,n in [a.split(':') for a in sys.argv[1:]]:
    rs=get(c,n)
    print('=====',c,n,'found',len(rs))
    for r in rs[:2]:
        print(' id',r['id'],'|',r.get('grade'),'|',r['englishChapter'][:60])
        print(' EN:',re.sub(r'\s+',' ',r['content'])[:240])
        print(' AR:',re.sub(r'\s+',' ',r['arabicContent'])[-170:])
