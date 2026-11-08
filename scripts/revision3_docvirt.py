"""Cliente de leitura das interfaces públicas anunciadas pelo próprio leitor."""
from pathlib import Path
import urllib.request,urllib.parse,json,re,hashlib
import truststore
truststore.inject_into_ssl()
ROOT=Path(__file__).resolve().parents[1];LOCAL=ROOT/'sources/local'
def read(url):
 with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AcademicResearch/1.0'}),timeout=45) as f:return f.read()
def run():
 config=json.loads(read('https://app.docvirt.com/appsettings.txt'))
 search=config['REACT_APP_DOCSEARCHAPI'].replace('localhost','app.docvirt.com')
 reader=config['REACT_APP_DOCREADERAPI'].replace('localhost','app.docvirt.com')
 print('search',search,'reader',reader)
 for term in ['risos','quá','hahaha','kkkk','gargalhada']:
  url=search+'/search/dvd_ajhpmj/'+urllib.parse.quote(term)+'?matchslist=2'
  raw=read(url);p=LOCAL/('r3_docvirt_search_'+re.sub(r'[^a-z]','',term)+'.json');p.write_bytes(raw)
  r=json.loads(raw);data=r.get('data');print(term,'success',r.get('sucesso'),'keys',list(data) if isinstance(data,dict) else type(data).__name__)
  if isinstance(data,dict):print(json.dumps({k:v for k,v in data.items() if not isinstance(v,(list,dict))},ensure_ascii=True)[:800])
if __name__=='__main__':run()
