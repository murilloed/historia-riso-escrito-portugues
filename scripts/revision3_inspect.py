from pathlib import Path
import json,re,pymupdf
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'sources/local'
pat=re.compile(r'(?<!\w)(?:[aA][hH][!,.…\s-]+){2,}|(?<!\w)(?:[hH][aeiAEI][!,.…\s-]+){2,}|(?<!\w)(?:[qQ]u[iI]?[áaÁA][!,.…\s-]+){2,}|(?<!\w)(?:[cC][áaÁA][!,.…\s-]+){2,}|\([Rr]isos[^)]{0,50}\)')
lex=re.compile(r'\b(?:risos?|riu|rindo|gargalha\w*|sorriso\w*)\b',re.I)
out=[]
for p in sorted(D.glob('r3_*.pdf')):
 try:
  doc=pymupdf.open(p);pages=[(i+1,x.get_text()) for i,x in enumerate(doc)]
  p.with_suffix('.txt').write_text('\n'.join(f'\n=== PDF PAGE {n} ===\n{t}' for n,t in pages),encoding='utf-8')
  hits=[]
  for n,t in pages:
   for m in pat.finditer(t):hits.append(dict(page=n,kind='representacao_candidata',form=m.group(),context=t[max(0,m.start()-140):m.end()+220]))
  if not hits:
   for n,t in pages:
    for m in list(lex.finditer(t))[:1]:hits.append(dict(page=n,kind='lexical_candidato',form=m.group(),context=t[max(0,m.start()-140):m.end()+220]))
    if len(hits)>=3:break
  out.append(dict(id=p.stem,pages=len(doc),text_chars=sum(len(t) for n,t in pages),candidates=hits))
  print(p.stem,'p',len(doc),'chars',sum(len(t) for n,t in pages),json.dumps(hits[:2],ensure_ascii=True))
 except Exception as e:print(p.stem,str(e)[:100])
(ROOT/'data/revision3_pdf_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
