from pathlib import Path
import re,json,pymupdf
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'sources/local'
pat=re.compile(r'(?<!\w)(?:[aA][hH][!,.…\s-]+){2,}|(?<!\w)(?:[hH][aeiAEI][!,.…\s-]+){2,}|(?<!\w)(?:[qQ]u[iI]?[áaÁA][!,.…\s-]+){2,}|(?<!\w)(?:[cC][áaÁA][!,.…\s-]+){2,}')
lex=re.compile(r'\b(?:risos?|riu|rindo|gargalha\w*|sorriso\w*)\b',re.I)
out=[]
for p in sorted(D.glob('r2_*')):
 if p.suffix not in ['.pdf','.txt']:continue
 if p.suffix=='.txt' and p.with_suffix('.pdf').exists():continue
 try:
  if p.suffix=='.pdf':
   doc=pymupdf.open(p);pages=[(i+1,x.get_text()) for i,x in enumerate(doc)]
   p.with_suffix('.txt').write_text('\n'.join(f'\n=== PDF PAGE {n} ===\n{t}' for n,t in pages),encoding='utf-8')
  else:pages=[(None,p.read_text(encoding='utf-8'))]
  rows=[]
  for n,t in pages:
   for m in pat.finditer(t):rows.append(dict(page=n,kind='onomatopeia_candidata',form=m.group(),context=t[max(0,m.start()-100):m.end()+140]))
  if not rows:
   for n,t in pages:
    for m in list(lex.finditer(t))[:1]:
     rows.append(dict(page=n,kind='lexical_candidato',form=m.group(),context=t[max(0,m.start()-90):m.end()+130]))
    if len(rows)>=3:break
  out.append(dict(id=p.stem,pages=len(pages),candidates=rows))
  print(p.stem,'pages',len(pages),'candidates',len(rows),json.dumps(rows[:3],ensure_ascii=True))
 except Exception as e:print(p.stem,type(e).__name__,str(e)[:100])
(ROOT/'data/revision2_text_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
