from revision2_download import run,ROOT
import re,html
rows=[]
for p in (ROOT/'sources/local').glob('r2_*meta.html'):
 urls=sorted(set(html.unescape(x).replace('\\u002F','/').replace('\\/','/') for x in re.findall(r'https[^\s<>"\x27]+?\.pdf',p.read_text(encoding='utf-8'))))
 print(p.stem,urls)
 for i,u in enumerate(urls):
  if 'trecho' in u:rows.append((p.stem+'_preview'+str(i),u,'pdf','amostra disponibilizada pela editora; não redistribuir integral'))
if rows:run(rows)
