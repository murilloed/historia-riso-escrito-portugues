"""Ampliação por acervo: quota documental, sem imputação de ocorrências ausentes.

Dados codificados após conferência; executar não faz nova consulta aos portais.
Datas provenientes somente da pasta são identificadas como tais.
"""
from pathlib import Path
import json,csv,re,hashlib,collections
from build_data import tex
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; GEN=ROOT/'artigo/generated'
manifest=json.loads((DATA/'downloads.json').read_text(encoding='utf-8'))
downloads={x['id']:x for x in manifest}

def writecsv(name,rows):
 with (DATA/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

PROFILES=[
 ('H01','DocVirt / Jardinópolis','r3_h01',1926,2022,'pastas do leitor; extremos do conjunto, não garantia de completude','Busca e imagens públicas; alguns resultados não confirmados'),
 ('H02','O Globo','r3_h02',1925,2026,'início editorial; extremo recente é horizonte de investigação','Portal consultado; fac-símiles históricos ainda pendentes de acesso e conferência'),
 ('H03','Folha','r3_h03',1921,2026,'início editorial das coleções; horizonte recente não integralmente conferido','Interface consultada; cobertura por década ainda pendente'),
 ('H04','BORE / USP, Jornais','r3_h04',1873,2012,'extremos dos itens no catálogo consultado','652 resultados para risos; 25 PDFs recuperados; 13 décadas com referência conferida'),
 ('H05','Hemeroteca / BN','r3_h05',1741,2026,'faixas do seletor e catálogo; inclui Lisboa, não apenas Brasil','Leitor antigo sem páginas carregadas; recomposição do serviço informada pela BN; PDFs públicos também consultados'),
 ('H06','Correio Braziliense','r3_h06',1960,2026,'jornal de Brasília; não o periódico de Hipólito da Costa','Edição de 2025 recuperada; demais décadas pendentes'),
 ('H07','Google News / Jornal do Brasil','r3_h07',1891,1999,'metadados do próprio leitor: 08/04/1891 a 31/12/1999','Catálogo consultado; ocorrências no fac-símile desta plataforma ainda pendentes'),
 ('H08','APESP / portal','r3_h08',None,None,'extremos do portal não determinados; não confundir documentos gerais com hemeroteca','Instrumentos de descrição consultados; inventário temporal e ocorrências pendentes'),
 ('H09','Senado / acervo de notícias','r3_h09',1995,2019,'Jornal: abril/1995 a dezembro/2019; revista: abril/2010 a abril/2017','PDFs de 1995, 2000 e 2015 e revista de 2017 adquiridos; busca textual sem ocorrência autenticada; parte dos arquivos sem OCR'),
 ('H10','Diario de Pernambuco / portal','r3_h10',1825,2026,'horizonte editorial; não equivale a cobertura digital demonstrada','Portal e destino da versão digital consultados; série histórica e ocorrências pendentes'),
 ('H11','CEPE / periódicos','r3_h11',1821,2006,'recorte documentado: século XIX, Diario da Manhã 1927–1985, suplemento 1986–2006','Busca devolve candidatos; autenticação por década pendente; manuscritos do portal fora deste recorte'),
 ('H12','BBM / Gazeta, coleção 8427','r3_h12',1817,1817,'único item recuperado: exemplar de 1817; descrição da série menciona 1808–1821','PDF de 28 páginas pesquisado; nenhuma representação autenticada; não se infere ausência histórica'),
 ('H13','APESP / item D000071','r3_apesp_d71',1809,1809,'item individual: Gazeta do Rio de Janeiro, n.48, 25/02/1809','Registro descritivo sem fac-símile; original fora de circulação para conservação'),
]
profiles=[]
coverage_sources={'H01':'r3_h01','H02':'r3_globo_historia','H03':'r3_h03','H04':'r3_bore_asc','H05':'r3_bniframe','H06':'r3_cb_memoria','H07':'r3_h07','H08':'r3_apesp_jornais','H09':'r3_senado_jornal','H10':'r3_h10','H11':'r3_cepe_xix','H12':'r3_bbm_item','H13':'r3_apesp_d71'}
for id,name,sid,start,end,basis,note in PROFILES:
 profiles.append(dict(archive=id,name=name,url=downloads[sid]['url'],coverage_url=downloads[coverage_sources[id]]['url'],start=start or '',end=end or '',date_basis=basis,access_finding=note,checked_on='2026-11-08'))
writecsv('archive_profiles.csv',profiles)

refs=[]
def add(archive,decade,sid,title,date,locator,form,kind,basis,url=None):
 refs.append(dict(id=f'D{len(refs)+1:03}',archive=archive,decade=decade,source_id=sid,title=title,date=date,locator=locator,form=form,kind=kind,date_basis=basis,url=url or downloads[sid]['url'],checked_on='2026-11-08',bib='r3doc'+str(len(refs)+1)))

# Um documento por década na coleção BORE; 1879 substitui o candidato lexical de 1877.
candidates=json.loads((DATA/'revision3_bore_candidates.json').read_text(encoding='utf-8'))
hits={x['id']:x for x in json.loads((DATA/'revision3_pdf_candidates.json').read_text(encoding='utf-8'))}
seen=set()
for c in sorted(candidates,key=lambda x:x['decade']):
 d=c['decade']
 if d in seen:continue
 seen.add(d);sid=f'r3_bore_item{d}_1_pdf';h=hits[sid]['candidates'][0]
 if d==1870:
  c=next(x for x in candidates if x['url'].endswith('/4951'));sid='r3_bore_item1870_2_pdf';h=dict(page=2,form='(Riso)')
 add('H04',d,sid,c['title'],c['date'],f'PDF p. {h["page"]}',h['form'],'rubrica' if d==1870 else 'lexical','data do catálogo; ocorrência inspecionada na imagem',c['url'])

selected=json.loads((DATA/'revision3_docvirt_selected.json').read_text(encoding='utf-8'))
for d,form in [(1920,'uma ironica gargalhada'),(1930,'O Sorriso dos Velhos'),(1960,'é de provocar o riso'),(2000,'Ele cai na gargalhada'),(2010,'Hahaha...'),(2020,'kkkkk')]:
 row=next((x for x in selected if x['decade']==d),None)
 if row is None:row=dict(folder=116,page=161,year_folder=1960,path='Correio - 1960',image_url='https://api.docvirt.com/v1/documents/dvd_ajhpmj/116/161')
 sid=f'r3_docvirt_{d}';path=ROOT/f'sources/local/{sid}.webp';raw=path.read_bytes()
 downloads[sid]=dict(id=sid,url=row['image_url'],resolved_url=row['image_url'],access_date='2026-11-08',rights='fac-símile; conservar local; licença de republicação não verificada',status='downloaded',path=str(path.relative_to(ROOT)).replace('\\','/'),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),public_copy=False)
 date={2010:'2016-01-09',2020:'2022-01-29'}.get(d,str(row['year_folder']))
 locator=f'pasta {row["folder"]}, página lógica {row["page"]}'
 if d==2010:locator+='; p. impressa 3; Só Rindo, Claudio Aguilhera'
 if d==2020:locator+='; p. impressa 5; Entrevista'
 add('H01',d,sid,'A Cidade de Jardinópolis' if d>=2000 else 'Correio da Semana',date,locator,form,'mimética' if d>=2010 else 'lexical','data impressa conferida' if d>=2010 else 'ano da pasta; dia não individualizado',f'https://app.docvirt.com/dvd_ajhpmj/folderid/{row["folder"]}/page/{row["page"]}')
add('H05',1840,'r3_bn1845','Diario Novo, n. 63','1845-03-18','PDF p.1; Religião','os risos','lexical','cabeçalho impresso conferido')
add('H06',2020,'r3_cb2025','Correio Braziliense: Uma sintonia capital','2025-04-07','PDF p.22; Diversão & Arte; entrevista de Walter Lima Jr. por Ricardo Daehn','(risos)','rubrica','data impressa conferida')
# Exemplar anteriormente conferido na imagem integral; preservar o localizador próprio.
add('H01',1970,'r3_h01','A Cidade de Jardinópolis, n.24','1972-10-08','capa; pasta 4, página lógica 107; Divertindo-se às Margens do Rio Paraná','muitos risos, muitas alegrias','lexical','data impressa conferida','https://app.docvirt.com/dvd_ajhpmj/pageid/2527/search/risos')
alternatives=json.loads((DATA/'revision3_docvirt_alternatives.json').read_text(encoding='utf-8'))
for d,form in [(1940,'reinado do riso'),(1950,'se inspira lastima nem riso'),(1980,'provocar o riso ao assistente'),(1990,'romance e riso')]:
 row=next(x for x in alternatives if x['decade']==d);sid=f'r3_docvirt_alt{d}'
 path=ROOT/f'sources/local/{sid}.webp';raw=path.read_bytes();url=f'https://api.docvirt.com/v1/documents/dvd_ajhpmj/{row["folder"]}/{row["page"]}'
 downloads[sid]=dict(id=sid,url=url,resolved_url=url,access_date='2026-11-08',rights='fac-símile; conservar local; licença não verificada',status='downloaded',path=str(path.relative_to(ROOT)).replace('\\','/'),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),public_copy=False)
 add('H01',d,sid,'Correio da Semana' if d<1970 else 'A Cidade de Jardinópolis',str(row['year']),f'pasta {row["folder"]}, página lógica {row["page"]}',form,'lexical','ano da pasta; ocorrência inspecionada; dia não individualizado',f'https://app.docvirt.com/dvd_ajhpmj/folderid/{row["folder"]}/page/{row["page"]}')
# Documentos já auditados: reutilização não aumenta o núcleo nem o número de documentos independentes.
old=json.loads((DATA/'extra_attestations.json').read_text(encoding='utf-8'))
import csv as _csv
with (DATA/'attestations.csv').open(encoding='utf-8') as f:at=list(_csv.DictReader(f))
for sid in ['r2_diario1928','ticotico1935','carioca1941']:
 a=next(x for x in at if x['source_id']==sid)
 if any(r['archive']=='H05' and r['decade']==int(a['year'])//10*10 for r in refs):continue
 add('H05',int(a['year'])//10*10,sid,a['document'],a['year'],a['locator'],a['form'],'rubrica' if 'risos' in a['form'].lower() else 'mimética',a['date_basis'])
writecsv('archive_decade_references.csv',refs)

matrix=[]
for p in profiles:
 if not p['start']:ds=['indeterminada']
 elif p['archive']=='H05':ds=[1740,1760]+list(range(1800,2030,10))
 else:ds=list(range(int(p['start'])//10*10,int(p['end'])//10*10+1,10))
 for d in ds:
  found=next((x for x in refs if x['archive']==p['archive'] and x['decade']==d),None)
  status='confirmada: '+found['kind'] if found else 'pendente: quota não satisfeita'
  if p['archive'] in ['H12','H13']:status='sem ocorrência autenticada no item' if p['archive']=='H12' else 'somente metadados; fac-símile indisponível nesta coleta'
  matrix.append(dict(archive=p['archive'],decade=d,status=status,reference_id=found['id'] if found else '',note='' if found else p['access_finding']))
writecsv('archive_decade_matrix.csv',matrix)
(DATA/'downloads.json').write_text(json.dumps(list(downloads.values()),ensure_ascii=False,indent=2),encoding='utf-8')

def table(filename,caption,headers,rows,widths):
 b=[r'\small\begin{longtable}{'+''.join('p{'+str(w)+r'\textwidth}' for w in widths)+'}',r'\caption{'+caption+r'}\\',r'\toprule '+' & '.join(headers)+r'\\\midrule\endfirsthead',r'\toprule '+' & '.join(headers)+r'\\\midrule\endhead']
 b+=[' & '.join(tex(c) for c in row)+r'\\' for row in rows];b+=[r'\bottomrule\end{longtable}\normalsize']
 (GEN/filename).write_text('\n'.join(b)+'\n',encoding='utf-8',newline='\n')
table('archive_profiles.tex','Delimitação dos 13 endereços solicitados. Extremo editorial não equivale a disponibilidade integral.',['ID / acervo','Recorte e fundamento','Situação'],[(p['archive']+' '+p['name'],str(p['start'])+'--'+str(p['end'])+'. '+p['date_basis'],p['access_finding']+r' \cite{r3archive'+p['archive']+'}') for p in profiles],[.20,.32,.37])
# Citações incorporadas após escape dos campos; tex() preserva os comandos.
table('archive_references.tex','Referências selecionadas por década e acervo. Lexical não significa grafia mimética.',['Acervo / década','Documento e localização','Ocorrência / categoria'],[(r['archive']+' / '+str(r['decade']),r['title']+'; '+r['date']+'; '+r['locator'],r['form']+'; '+r['kind']+r' \cite{'+r['bib']+'}') for r in refs],[.13,.53,.23])
table('archive_matrix.tex','Matriz por acervo e década: cumprimento observado da quota, sem imputação de exemplos.',['Acervo','Década','Resultado'],[(r['archive'],'n/d' if r['decade']=='indeterminada' else r['decade'],r['status']+(' ('+r['reference_id']+')' if r['reference_id'] else '')) for r in matrix],[.10,.13,.66])

# Bloco idempotente de bibliografia.
bibpath=ROOT/'artigo/references.bib';bib=bibpath.read_text(encoding='utf-8').split('% BEGIN REVISION3')[0].rstrip()+'\n\n% BEGIN REVISION3\n'
def entry(key,title,url,year,note):
 return '@misc{'+key+',\n  title = {'+tex(title)+'},\n  howpublished = {\\url{'+url+'}},\n  year = {'+str(year)+'},\n  note = {'+tex(note)+'; acesso em 8 nov. 2026}\n}\n\n'
for p in profiles:bib+=entry('r3archive'+p['archive'],p['name']+': catálogo e condições de acesso',p['coverage_url'],2026,p['date_basis'])
for r in refs:bib+=entry(r['bib'],r['title'],r['url'],r['date'][:4],r['locator']+'; '+r['date_basis'])
bibpath.write_text(bib.rstrip()+'\n',encoding='utf-8',newline='\n')

# Somente quatro documentos novos entram no núcleo de representações.
new=[next(r for r in refs if r['source_id']==sid) for sid in ['r3_bore_item1870_2_pdf','r3_docvirt_2010','r3_docvirt_2020','r3_cb2025']]
old=[x for x in old if not x['source_id'].startswith('r3_')]
for r in new:
 old.append(dict(year=int(r['date'][:4]),document=r['title'],source_id=r['source_id'],country='Brasil',medium='jornal: rubrica' if r['kind']=='rubrica' else 'jornal: grafia mimética',form=r['form'],locator=r['date']+'; '+r['locator'],evidence='E1',bib=r['bib'],date_basis=r['date_basis']))
(DATA/'extra_attestations.json').write_text(json.dumps(old,ensure_ascii=False,indent=2),encoding='utf-8')
summary=dict(archive_addresses=len(profiles),matrix_rows=len(matrix),confirmed_archive_decade_cells=sum(bool(x['reference_id']) for x in matrix),selected_references=len(refs),new_core_documents=4,scope_completed=False,checked_on='2026-11-08')
(DATA/'archive_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary))
