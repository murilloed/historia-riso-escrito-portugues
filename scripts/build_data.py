"""Gera tabelas de registros com estatuto explícito; não inventa dados."""
from pathlib import Path
import csv,json,math,collections
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; GEN=ROOT/'artigo/generated';GEN.mkdir(parents=True,exist_ok=True)
def csvwrite(name,rows):
 with (DATA/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def tex(s):
 return str(s).replace('–','-').replace('—','-').translate(str.maketrans({'&':r'\&','%':r'\%','_':r'\_','#':r'\#','$':r'\$'}))
AT=[
 (1872,'Til','til1872','Brasil','livro','Quiá!... quiá!... quiá!...','Volume II, capítulo VIII; âncora: Ai, menina!','E2','alencar1872','ano da obra; transcrição eletrônica'),
 (1884,'A segunda vida','machado1884','Brasil','conto','cá, cá, cá, cá, cá...','Âncora: Era uma gargalhada assim','E2','assis1884','ano do conto; corpus eletrônico'),
 (1901,'A cidade e as serras','serras1901','Portugal','livro','Ah! ah! ah!','Âncora: Então tambem eu rio!; PG 18220','E2','queiros1901','edição de 1901 transcrita'),
 (1917,'A engomadeira','engomadeira1917','Portugal','livro','Ah! Ah! Ah!...',"Âncora: E 'inda o confessa!; PG 23879",'E2','almada1917','edição de 1917 transcrita'),
 (1935,'O Tico-Tico, n. 1569','ticotico1935','Brasil','periódico','Quá quá quá...','30/10/1935; capa, último quadro; PDF p. 1','E1','ticotico1935','data impressa inspecionada'),
 (1941,'Diário Carioca, n. 3902','carioca1941','Brasil','periódico','Ah! ah!','08/03/1941; p. 13; folhetim As memórias de Sherlock Holmes','E1','carioca1941','data da tradução publicada, não da composição original'),
 (1979,'Correio do Povo','correio1979','Brasil','periódico','AH, AH, AH','28/04/1979; p. 5; tira Bidu, quadros finais','E1','correio1979','data impressa inspecionada'),
 (2007,'Chat reproduzido por Young (2008)','young2008','Brasil','chat reportado','kkkk','Dissertação p. 93; contexto: semestre 2007.2','E3','young2008','período da pesquisa; mensagem sem dia validado'),
 (2010,'Leão (2010)','ufpe','Brasil','chat reportado','kkkkkkkk / rsrsrsrs','PDF pp. 90-92; fragmentos 97, 101 e 103 e análise','E3','leao2010','ano da dissertação; não data individual da mensagem'),
 (2015,'Silva (2015)','cruz2015','Brasil','comentário reportado','Kkkk','p. impressa 86, PDF p. 87; CA7 P2','E3','silva2015','ano da dissertação; não data individual da mensagem'),
 (1925,'Diário da Câmara dos Deputados, n. 77','portugal1925','Portugal','registro parlamentar','Risos.','11/06/1925; p. 14; intervenção de Cunha Leal','E2','portugal1925','data da sessão; transcrição automática oficial'),
 (1955,'Diário do Congresso Nacional, suplemento','camara1955','Brasil','registro parlamentar','(Risos)','10/12/1955; p. 13; intervenção de Alberto Torres','E1','camara1955','data do diário; imagem inspecionada'),
 (1965,'Anais do Senado, livro 1','senado1965','Brasil','registro parlamentar','(Risos.)','p. impressa 162; PDF p. 185; intervenção de Edmundo Levi','E1','senado1965','ano do volume; dia da sessão não individualizado'),
 (1985,'Diário do Congresso Nacional, seção I','camara1985','Brasil','registro parlamentar','(risos e aplausos.)','29/03/1985; p. impressa 2107; PDF p. 55','E1','camara1985','data do diário; material transcrito inserido'),
 (1994,'Folha de S.Paulo','folha1994','Brasil','jornal: transcrição','(risos)','03/09/1994; Veja íntegra da conversa de Ricupero com Monforte','E2','folha1994','data da publicação; versão eletrônica do jornal'),
]
keys=['year','document','source_id','country','medium','form','locator','evidence','bib','date_basis']
AT=[dict(id=f'A{i:02}',**dict(zip(keys,row))) for i,row in enumerate(AT,1)]
extra=DATA/'extra_attestations.json'
if extra.exists():AT.extend(json.loads(extra.read_text(encoding='utf-8')))
supp=DATA/'annual_supplement.csv'
added=[]
if supp.exists():
 with supp.open(encoding='utf-8') as f:added=list(csv.DictReader(f))
 for r in added:AT.append(dict((k,int(r[k]) if k=='year' else r[k]) for k in keys))
annual_bib=[]
for r in added:
 annual_bib.append('@misc{'+r['bib']+',\n  title={'+tex(r['document'])+'},\n  key={'+r['bib']+'},\n  year={'+r['year']+'},\n  howpublished={\\url{'+r['url']+'}},\n  note={'+tex(r['locator']+'; '+r['date_basis'])+'}\n}')
(ROOT/'artigo/annual.bib').write_text('\n\n'.join(annual_bib)+'\n',encoding='utf-8',newline='\n')
AT.sort(key=lambda r:r['year'])
for i,r in enumerate(AT,1):
 r['id']=f'A{i:02}'
 r['representation']='rubrica descritiva' if r['medium'] in ['registro parlamentar','jornal: transcrição','jornal: rubrica'] else 'representação mimética ou marcador digital'
csvwrite('attestations.csv',AT)
counts=collections.Counter(r['year'] for r in AT)
covered=sum(counts[y]>0 for y in range(1900,2010))
(GEN/'annual_counts.tex').write_text('\n'.join('\\newcommand{\\'+k+'}{'+str(v)+'}' for k,v in dict(CorpusSize=len(AT),AnnualAdded=len(added),AnnualCovered=covered,AnnualMissing=110-covered).items())+'\n',encoding='utf-8',newline='\n')
annual=[dict(year=y,confirmed_documents=counts[y],scope='recorte anual 1900–2009' if 1900<=y<=2009 else 'fora do recorte anual',interpretation='atestação no inventário' if counts[y] else 'sem atestação confirmada nesta coleta; não é ausência histórica') for y in range(1872,2027)]
csvwrite('annual_coverage.csv',annual)
det=[dict(n=n,p005=1-(1-.05)**n,p001=1-(1-.01)**n) for n in [3,6,30,59,97,299]]
csvwrite('detection_sensitivity.csv',det)
body=[r'\begin{table}[htbp]\centering\small',r'\caption{Probabilidade de ao menos uma detecção em cenários hipotéticos independentes. Não são resultados observados.}',r'\begin{tabular}{rrr}\toprule',r'Documentos ($n$) & $p=0{,}05$ & $p=0{,}01$ \\\midrule']
for r in det:
 body.append(f"{r['n']} & {100*r['p005']:.1f}\\% & {100*r['p001']:.1f}\\% ".replace('.',',')+r'\\')
body += [r'\bottomrule\end{tabular}',r'\end{table}']
(GEN/'detection-table.tex').write_text('\n'.join(body),encoding='utf-8')
body=[r'\small',r'\begin{longtable}{p{0.07\textwidth}p{0.24\textwidth}p{0.17\textwidth}p{0.37\textwidth}}',r'\caption{Atestações selecionadas: ano de referência, grafia e localizador. E1: imagem; E2: transcrição primária; E3: interação reportada.}\label{tab:attestations}\\',r'\toprule Ano & Documento & Grafia & Localizador / evidência \\\midrule\endfirsthead',r'\toprule Ano & Documento & Grafia & Localizador / evidência \\\midrule\endhead']
for r in AT:
 body.append(f"{r['year']} & {tex(r['document'])} "+r'\cite{'+r['bib']+'} & '+tex(r['form'])+' & '+tex(r['locator'])+' ('+r['evidence']+'). '+r'\\')
body += [r'\bottomrule\end{longtable}\normalsize']
(GEN/'attestations-table.tex').write_text('\n'.join(body),encoding='utf-8')
CLAIMS=[
(1902,'Canaã','Livro','Ah! Ah! Ah!','colono Maciel, batendo no joelho','Sem edição e página'),
(1904,'Gazeta de Notícias, 25/07','Jornal','Ah! Ah! Ah!','ovo na barriga da galinha','Sem página e autoria da crônica'),
(1911,'Triste fim de Policarpo Quaresma','Livro','Ah! ah!','Quaresma, você é um visionário','Sem edição e página; separar folhetim de 1911 e livro de 1915'),
(1912,'O Malho, 12/10','Revista','Quá! Quá! Quá!','O prefeito promete carne barata','Sem página e número'),
(1928,'Macunaíma','Livro','Ah! ah! ah!','assim você me mata de rir','Sem página e edição'),
(1925,'Correio da Manhã, 14/02','Jornal','Ah! ah! ah!','baronesa e leque de plumas','Sem página e autoria'),
(1934,'São Bernardo','Livro','Ah, ah!','latim de missa','Sem página e edição'),
(1935,'Fon-Fon!, 08/06','Revista','Quá! quá! quá!','rei da Inglaterra','Sem página'),
(1946,'Sagarana','Livro','He! he! he!','O mundo dá muitas voltas','Sem conto, página e edição'),
(1944,'Diário de Notícias, 18/03','Jornal','(Risos na assistência)','boatos de racionamento','Sem página e identificação do ministro'),
(1953,'Almanaque do Pato Donald','Quadrinhos','Quá-quá-quá!','escondeu as moedas','Sem número, história e página'),
(1955,'Tribuna da Imprensa','Jornal','He-he-he','o plano é honesto','Sem dia, página e título da coluna'),
(1967,'Quarup','Livro','Ha, ha, ha','o que os jornais publicam','Sem página e edição'),
(1969,'O Pasquim, n. 12','Jornal','(hahaha)','Jaguar e desenho horrível','Sem página e entrevista'),
(1973,'As meninas','Livro','Ha-ha-ha!','Você perdeu a aposta','Sem página e edição'),
(1975,'Revista do Cebolinha','Quadrinhos','Hi-hi-hi!','encontrar o Sansão','Sem número, história e página'),
(1982,'Feliz ano velho','Livro','Ha ha ha','burradas do colégio','Sem página e edição'),
(1986,'Folha de S.Paulo, Painel, 14/11','Jornal','Rs.','congelar a inflação para sempre','Sem página'),
(1993,'Veja, Páginas Amarelas, 07/05','Revista','(Risos)','não fugirei da raia','Entrevistado não identificado'),
(1997,'Folhateen, junho','Jornal','rsrsrs / hahaha','sala de chat do mIRC','Sem dia, página e reportagem'),
(2005,'Os segredos do Orkut','Livro','kakakaka','Adoro passar as tardes','Sem autor, editora e edição identificados'),
(2007,'Capricho, setembro','Revista','KKKKKKKKKK','quase quebrou a cara','Sem número, página e reportagem'),
]
rows=[dict(id=f'C{i:02}',claimed_year=y,claimed_source=s,medium=m,claimed_form=f,anchor=a,missing=st,status='literal não autenticado nesta coleta') for i,(y,s,m,f,a,st) in enumerate(CLAIMS,1)]
verification=DATA/'claims_verification.csv'
if verification.exists():
 with verification.open(encoding='utf-8') as f:details={r['id']:r for r in csv.DictReader(f)}
 for r in rows:
  r['status']=details[r['id']]['status']
  r['missing']=details[r['id']]['finding']
csvwrite('claims_audit.csv',rows)
body=[r'\small\begin{longtable}{p{0.07\textwidth}p{0.21\textwidth}p{0.14\textwidth}p{0.42\textwidth}}',r'\caption{Os 22 alvos da série enviada: grafias alegadas e parecer após a segunda auditoria.}\\',r'\toprule Ano & Fonte alegada & Grafia alegada & Verificação e limites \\\midrule\endfirsthead',r'\toprule Ano & Fonte alegada & Grafia alegada & Verificação e limites \\\midrule\endhead']
for r in rows:
 form=tex(r['claimed_form']).replace('KKKKKKKKKK',r'KKKKK\allowbreak KKKKK')
 body.append(str(r['claimed_year'])+' & '+tex(r['claimed_source'])+' & '+form+' & '+tex(r['missing']).rstrip('.')+'. '+r'\\')
body+=[r'\bottomrule\end{longtable}\normalsize']
(GEN/'claims-table.tex').write_text('\n'.join(body),encoding='utf-8')
summary=dict(attestations=len(AT),years_with_attestations=len(counts),by_evidence=dict(collections.Counter(x['evidence'] for x in AT)),claims_audited=len(rows),design='exploratory_non_probability',n0_10=math.ceil(1.96**2*.25/.1**2),n0_05=math.ceil(1.96**2*.25/.05**2),detection_005=math.ceil(math.log(.05)/math.log(.95)),detection_001=math.ceil(math.log(.05)/math.log(.99)))
(DATA/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=True))
