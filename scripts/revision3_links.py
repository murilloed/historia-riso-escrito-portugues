from pathlib import Path
from html.parser import HTMLParser
import re,json
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.rows=[];self.cur=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a':self.cur=[a.get('href',''),'']
 def handle_data(self,t):
  if self.cur:self.cur[1]+=t
 def handle_endtag(self,tag):
  if tag=='a' and self.cur:self.rows.append(self.cur);self.cur=None
for p in (ROOT/'sources/local').glob('r3_*.html'):
 encoding='latin1' if p.stem=='r3_h03' else 'utf-8'
 parser=Links();parser.feed(p.read_text(encoding=encoding,errors='replace'))
 (ROOT/'sources/local'/('links_'+p.stem+'.json')).write_text(json.dumps(parser.rows,ensure_ascii=False,indent=2),encoding='utf-8')
 if any(x in p.stem for x in ['cepe','apesp','bore_desc','bniframe','senado']):
  hits=[r for r in parser.rows if re.search('Acessar|pdf|Download|BAIXAR|Hemeroteca|recife|177|18[0-9][0-9]|2012',r[0]+' '+r[1],re.I)]
  print(p.stem,json.dumps(hits[:20],ensure_ascii=True))
