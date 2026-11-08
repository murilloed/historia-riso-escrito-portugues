"""Seleção cronológica de títulos inéditos; inventário codificado após conferência.

Uma ocorrência por obra/jornal/site. Não é censo das bases nem sorteio.
Datas de mensagens, edições, criação de comunidades e capturas ficam separadas.
"""
from pathlib import Path
from html.parser import HTMLParser
import csv,json,re,unicodedata,collections
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'data';GEN=ROOT/'artigo/generated'
downloads={x['id']:x for x in json.loads((DATA/'downloads.json').read_text(encoding='utf-8'))}
def norm(s):
 return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip()
def writecsv(name,rows):
 with (DATA/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def readcsv(name):
 with (DATA/name).open(encoding='utf-8') as f:return list(csv.DictReader(f))
class Meta(HTMLParser):
 def __init__(self):super().__init__();self.fields={}
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='meta' and 'name' in a:self.fields.setdefault(a['name'],[]).append(a.get('content',''))
def meta(id):
 p=Meta();p.feed((ROOT/f'sources/local/r4_bbm_{id}.html').read_text(encoding='utf-8'));return p.fields

# Baseline imutável desta rodada; já inclui títulos examinados sem ocorrência.
baseline=DATA/'revision4_exclusions.csv'
if not baseline.exists():
 prior=[]
 for r in readcsv('candidate_sources.csv'):
  title=r['description_from_input'].split(':')[0]
  prior.append(dict(label=title,normalized_title=norm(title),basis='roteiro já auditado',source='candidate_sources.csv'))
 for filename in ['attestations.csv','archive_decade_references.csv']:
  for r in readcsv(filename):
   if r.get('source_id','').startswith('r4_'):continue
   title=r.get('document',r.get('title',''))
   prior.append(dict(label=title,normalized_title=norm(title),basis='documento examinado anteriormente',source=filename))
 writecsv(baseline.name,prior)
prior=readcsv(baseline.name)

# id, ano do exemplar, localizador PDF, forma, categoria, chave de obra.
BOOKS=[
 (4678,1645,266,'risos (normalização do s longo)','lexical','chronica-companhia-iesv-portugal'),
 (5443,1720,353,'Riso; verbete, p. impressa 345','lexicográfica','vocabulario-portuguez-latino'),
 (5413,1789,354,'RISO; verbete','lexicográfica','diccionario-lingua-portugueza-morais'),
 (4347,1798,259,'Mostra em riso moderado','lexical','viola-de-lereno'),
 (6816,1813,25,'De riso menos digno','lexical','o-patriota'),
 (6941,1822,26,'isso merece risada','lexical','gazeta-pernambucana'),
 (6859,1836,140,'riso de alegria','lexical','nitheroy'),
 (3837,1837,22,'evitando sempre o rir-se a gargalhadas','lexical','reflexoes-dramaticas'),
 (4135,1846,51,'Da casa do guerreiro o riso, a dança','lexical','primeiros-cantos'),
 (7850,1866,12,'philosophia commodista dos risos','lexical','gennesco'),
 (2440,1902,12,'ás gargalhadas','lexical','a-fallencia'),
 (7845,1920,23,'torceram-se de riso','lexical','negrinha'),
 (1717,1980,35,'O riso tem lágrimas','lexical','poesia-1958-1978'),
 (7365,2017,146,'cujas poezias serviam de riso','lexical','rubens-borba-moraes-anotacoes-bibliofilo'),
]
rows=[]
for id,year,page,form,kind,key in BOOKS:
 m=meta(id);title=m['DC.title'][0];sid=f'r4_bbm_{id}_pdf'
 # Cada volume selecionado representa uma única obra/título, sem multiplicar a série.
 rows.append(dict(work_key=key,title=title,author='; '.join(m.get('DC.creator',[])),year=year,date=str(year),date_basis='ano do exemplar no catálogo; não primeira edição presumida',base='Brasiliana / BBM',source_id=sid,url=f'https://digital.bbm.usp.br/handle/bbm/{id}',file_url=downloads[sid]['url'],capture_date='',message_date='',locator=f'PDF p.{page}',form=form,kind=kind,evidence='imagem inspecionada',core=False,prior_overlap=False))
rows += [
 dict(work_key='kibe-loco',title='Kibe Loco: Uma chance (parte 2)',author='Kibe Loco',year=2007,date='2007-06-27',date_basis='data exibida na postagem; captura de 01/07/2007',base='Wayback / blog',source_id='r4_blog_page',url='https://web.archive.org/web/20070701184701/http://www.kibeloco.globolog.com.br/',file_url=downloads['r4_blog_page']['url'],capture_date='2007-07-01T18:47:01Z',message_date='2007-06-27',locator='postagem Uma chance (parte 2); parágrafo com não contendo o riso',form='não contendo o riso',kind='lexical',evidence='texto primário eletrônico preservado',core=False,prior_overlap=False),
 dict(work_key='forum-cifra-club',title='Cifra Club: como afinar meio tom abaixo',author='Participante identificado por pseudônimo',year=2010,date='2010-07-12',date_basis='data e hora exibidas na mensagem; captura de 15/09/2010; tópico iniciado em 2003',base='Wayback / fórum',source_id='r4_forum_capture',url='https://web.archive.org/web/20100915135414/http://forum.cifraclub.com.br/forum/3/19828/',file_url=downloads['r4_forum_capture']['url'],capture_date='2010-09-15T13:54:14Z',message_date='2010-07-12T15:21',locator='resposta Enviado: 12/jul/10 15:21; após boa!',form='kkkkkkkkkkkkk',kind='mimética',evidence='texto primário eletrônico preservado',core=True,prior_overlap=False),
 dict(work_key='orkut-comunidades',title='Orkut: comunidade Kiko Dança Psy-TRANCE',author='Descrição de comunidade pública',year=2014,date='2014-10-04',date_basis='data da captura, não data de redação; criação da comunidade em 2006 não data o trecho',base='Wayback / Orkut',source_id='r4_orkut_community',url='https://web.archive.org/web/20141004095823/http://orkut.google.com/c8965820.html',file_url=downloads['r4_orkut_community']['url'],capture_date='2014-10-04T09:58:23Z',message_date='',locator='descrição da comunidade, após sempre agitado',form='hehehe',kind='mimética',evidence='texto primário eletrônico preservado',core=True,prior_overlap=False),
]
rows.sort(key=lambda r:(r['year'],r['title']))
assert len({r['work_key'] for r in rows})==len(rows)
for i,r in enumerate(rows,1):r.update(id=f'N{i:02}',bib=f'r4{r["work_key"].replace("-","")}',checked_on='2026-11-08')
writecsv('revision4_new_titles.csv',rows)

from build_data import tex
b=[r'\small\begin{longtable}{>{\raggedright\arraybackslash}p{.09\textwidth}>{\raggedright\arraybackslash}p{.39\textwidth}>{\raggedright\arraybackslash}p{.20\textwidth}>{\raggedright\arraybackslash}p{.21\textwidth}}',r'\caption{Seleção cronológica de títulos inéditos no inventário anterior: uma referência por obra, periódico ou site. Datas de captura são explicitadas, sem retrodatação.}\\',r'\toprule Ano / ID & Título e localização & Forma / categoria & Base da data \\\midrule\endfirsthead',r'\toprule Ano / ID & Título e localização & Forma / categoria & Base da data \\\midrule\endhead']
for r in rows:b.append(tex(str(r['year'])+' / '+r['id'])+' & '+tex(r['title']+'; '+r['locator'])+r' \cite{'+r['bib']+'} & '+tex(r['form']+'; '+r['kind'])+' & '+tex(r['date_basis'])+r'\\')
b.append(r'\bottomrule\end{longtable}\normalsize')
(GEN/'new_titles_chronology.tex').write_text('\n'.join(b)+'\n',encoding='utf-8',newline='\n')

bibpath=ROOT/'artigo/references.bib';bib=bibpath.read_text(encoding='utf-8').split('% BEGIN REVISION4')[0].rstrip()+'\n\n% BEGIN REVISION4\n'
for r in rows:
 author=''
 if r['base']=='Brasiliana / BBM' and r['author']:
  # Datas biográficas do Dublin Core não integram o nome bibliográfico.
  authors=[re.sub(r',?\s*\d{4}(?:[-–][\d?]*)?\s*$', '',name).strip(' ,') for name in r['author'].split('; ')]
  author=' and '.join(name for name in authors if name)
 elif r['work_key']=='kibe-loco':author='{Kibe Loco}'
 author_field=('  author = {'+tex(author)+'},\n') if author else ('  key = {'+tex(r['title'])+'},\n')
 bib+='@misc{'+r['bib']+',\n'+author_field+'  title = {'+tex(r['title'])+'},\n  year = {'+str(r['year'])+'},\n  howpublished = {\\url{'+r['url']+'}},\n  note = {'+tex(r['locator']+'; '+r['date_basis'])+'; acesso em 8 nov. 2026}\n}\n\n'
bib+='@misc{r4orkutindex,\n title={Arquivo de Comunidades do Orkut: captura indicada pelo autor},\n year={2014},\n howpublished={\\url{https://web.archive.org/web/20141001005309/http://orkut.google.com/}},\n note={Página de entrada; não constitui transcrição de conversa de 2004. Acesso em 8 nov. 2026}\n}\n'
bibpath.write_text(bib.rstrip()+'\n',encoding='utf-8',newline='\n')

extra=json.loads((DATA/'extra_attestations.json').read_text(encoding='utf-8'));extra=[r for r in extra if not r['source_id'].startswith('r4_')]
for r in rows:
 if r['core']:extra.append(dict(year=r['year'],document=r['title'],source_id=r['source_id'],country='Brasil',medium='fórum preservado' if 'forum' in r['work_key'] else 'comunidade preservada',form=r['form'],locator=r['locator']+'; captura '+r['capture_date'],evidence='E2',bib=r['bib'],date_basis=r['date_basis']))
(DATA/'extra_attestations.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2),encoding='utf-8')
summary=dict(selection='dirigida; cronológica; uma referência por título inédito',new_titles=len(rows),bbm_titles=len(BOOKS),web_titles=3,kind_counts=dict(collections.Counter(r['kind'] for r in rows)),new_core_documents=2,oldest_selected=1645,newest_selected=2017,exhaustive=False,checked_on='2026-11-08')
(DATA/'revision4_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True))
