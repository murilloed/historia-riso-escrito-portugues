"""Aquisição rastreável; biblioteca padrão; não contorna controles de acesso."""
import urllib.request, json, hashlib, pathlib, concurrent.futures, re, html
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCES=[
 ('til1872','https://pt.wikisource.org/wiki/Til/II/VIII','html','dominio-publico-texto; interface CC-BY-SA'),
 ('machado1884','https://machado.byu.edu/text/a-segunda-vida/','html','dominio-publico-texto; interface institucional'),
 ('primo1878','https://www.gutenberg.org/ebooks/42942.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('policarpo1915','https://www.gutenberg.org/ebooks/67535.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('young2008','https://repositorio.ufc.br/bitstream/riufc/3309/1/2008_Dis_RSYOUNG.pdf','pdf','acesso-aberto; redistribuicao-nao-verificada'),
 ('unb2026','https://dpg.unb.br/wp-content/uploads/2026/03/Rev_Edital_N_C2_BA_04.2026_Selecao_Mestrado_2026.2__281_29_assinado.pdf','pdf','documento-oficial-publico'),
 ('iida2024','https://pmc.ncbi.nlm.nih.gov/articles/PMC11670811/','html','CC-BY-NC-ND-4.0'),
 ('missangas2025','https://revistas.uneb.br/missangas/article/download/24450/16407/90797','pdf','licenca-a-conferir'),
 ('cruz2015','https://profletras.ufrn.br/wp-content/uploads/2025/04/6a-Ana-Catia-Alves-da-Silva.pdf','pdf','acesso-aberto; redistribuicao-nao-verificada'),
 ('ufpe','https://attena.ufpe.br/bitstream/123456789/4072/1/arquivo2530_1.pdf','pdf','acesso-aberto; redistribuicao-nao-verificada'),
 ('ilari_catalog','https://www.editoracontexto.com.br/produto/linguistica-romanica/1496029','html','metadados; redistribuicao-nao-verificada'),
 ('portuguese_catalog','https://www.gutenberg.org/browse/languages/pt','html','catalogo'),
]
def get(row):
 id,url,ext,rights=row
 folder=ROOT/'sources'/'local';folder.mkdir(parents=True,exist_ok=True)
 result=dict(id=id,url=url,access_date='2026-11-08',rights=rights)
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'AcademicResearch/1.0 (documentary linguistic research)'})
  with urllib.request.urlopen(req,timeout=45) as r: data=r.read();result['resolved_url']=r.url
  p=folder/(id+'.'+ext);p.write_bytes(data)
  result.update(status='downloaded',path=str(p.relative_to(ROOT)).replace('\\','/'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  if ext=='html':
   text=html.unescape(re.sub('<[^>]+>',' ',re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',data.decode('utf-8','replace'),flags=re.S)))
   (folder/(id+'.txt')).write_text(text,encoding='utf-8')
 except Exception as e: result.update(status='failed',error=str(e))
 return result
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(get,SOURCES))
 (ROOT/'data').mkdir(exist_ok=True)
 (ROOT/'data'/'downloads.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
 for r in results: print(r['id'],r['status'],r.get('bytes',r.get('error')))
