from revision2_download import run,ROOT
import urllib.parse,re,html,json
BASE='https://obrasraras.usp.br'
def discover():
 rows=[]
 for page in range(7):
  args={'query':'risos','rpp':'100','page':str(page+1)}
  rows.append((f'r3_bore_results{page}',BASE+'/xmlui/handle/123456789/4262/discover?'+urllib.parse.urlencode(args),'html','resultados de busca; classificar por data do item; não é autenticação'))
 run(rows)
def extract():
 out=[];rows=[]
 for p in (ROOT/'sources/local').glob('r3_bore_results*.html'):
  text=p.read_text(encoding='utf-8',errors='replace')
  for block in re.split(r'<li class="ds-artifact-item[^>]*>',text)[1:]:
   m=re.search(r'<div class="artifact-title">\s*<a href="([^"]+)">([^<]+)</a>',block)
   date=re.search(r'<span class="date">([^<]+)',block)
   if m and date:
    decade=int(date[1][:4])//10*10
    if any(x['url']==BASE+m[1] for x in out):continue
    out.append(dict(decade=decade,url=BASE+m[1],title=html.unescape(m[2]),date=date[1]))
    # Amostra dirigida: até dois candidatos por década para conferência.
    if sum(x['decade']==decade for x in out)<=2:rows.append((f'r3_bore_item{decade}_{sum(x["decade"]==decade for x in out)}',BASE+m[1],'html','metadados e links de exemplar candidato'))
 (ROOT/'data/revision3_bore_candidates.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
 print('candidatos',len(out),'décadas',sorted(set(x['decade'] for x in out)))
 if rows:run(rows)
def files():
 rows=[]
 for p in (ROOT/'sources/local').glob('r3_bore_item*.html'):
  urls=sorted(set(html.unescape(x) for x in re.findall(r'href="([^"]+\.pdf(?:\?[^"]*)?)"',p.read_text(encoding='utf-8',errors='replace'))))
  if urls:
   url=urls[0];url=url if url.startswith('http') else BASE+url
   rows.append((p.stem+'_pdf',url,'pdf','exemplar institucional; conservar local; licença integral a verificar'))
 print('pdfs',len(rows))
 if rows:run(rows)
if __name__=='__main__':discover();extract();files()
