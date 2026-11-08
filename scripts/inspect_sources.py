from pathlib import Path
from pypdf import PdfReader
import re
root=Path(__file__).resolve().parents[1]
for p in (root/'sources/local').glob('*.pdf'):
 try:
  reader=PdfReader(p);out=[]
  for i,page in enumerate(reader.pages,1):
   t=page.extract_text() or '';out.append(f'\n=== PDF PAGE {i} ===\n'+t)
  text='\n'.join(out);p.with_suffix('.txt').write_text(text,encoding='utf-8')
  print('\nSOURCE',p.name,'PAGES',len(reader.pages));print(text[:1800].encode('ascii','backslashreplace').decode())
  for m in list(re.finditer(r'k{3,}|rsrs|Qu[iáa]+',text,re.I))[:6]: print(repr(text[max(0,m.start()-70):m.end()+130]).encode('ascii','backslashreplace').decode())
 except Exception as e:print(type(e).__name__,str(e)[:100])
for name in ['machado1884','primo1878','policarpo1915']:
 text=(root/'sources/local'/f'{name}.txt').read_text(encoding='utf-8')
 print('\nTEXT',name)
 for m in list(re.finditer(r'(?:[Cc][áa][,! .-]+){2,}|(?:[Qq]ui[áa][,! .-]+){2,}|(?:[AaHh][hHaAeEiI][!, .-]+){3,}',text))[:8]:print(repr(text[max(0,m.start()-100):m.end()+130]).encode('ascii','backslashreplace').decode())
