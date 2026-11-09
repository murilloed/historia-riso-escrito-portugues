"""Síntese metodológica a partir dos dados públicos, sem confundir unidades.

Os 16 endereços indicados não são 16 bases independentes. O manifesto também
inclui fontes complementares e recursos técnicos; seus domínios não são bases.
"""
from pathlib import Path
from urllib.parse import urlsplit
import csv,json,collections,re
from build_data import ROOT,tex
DATA=ROOT/'data';GEN=ROOT/'artigo/generated'
REPO='https://github.com/murilloed/historia-riso-escrito-portugues'
def readcsv(name):
 with (DATA/name).open(encoding='utf-8') as f:return list(csv.DictReader(f))
def writecsv(name,rows):
 with (DATA/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def gh(path):return REPO+'/blob/main/'+path
manifest=json.loads((DATA/'downloads.json').read_text(encoding='utf-8'))
at=readcsv('attestations.csv');r3=readcsv('archive_decade_references.csv');r4=readcsv('revision4_new_titles.csv')
profiles=readcsv('archive_profiles.csv');registry=[]
for p in profiles:
 note='Portal/coleção; ver limitações de acesso e cobertura.'
 if p['archive']=='H08':note='Portal APESP; H13 é um item deste mesmo acervo.'
 if p['archive']=='H12':note='Coleção Gazeta na BBM; H14 é o acervo geral da mesma biblioteca.'
 if p['archive']=='H13':note='Item individual do APESP; não é outra base independente.'
 requested=p['url'] if p['archive']!='H13' else 'https://atom.arquivoestado.sp.gov.br/br-spapesp-hemapesp-s001-b000565-d000071;isad?sf_culture=fr'
 registry.append(dict(id=p['archive'],name=p['name'],requested_url=requested,access_url=p['url'],scope_note=note,selected_references=sum(x['archive']==p['archive'] for x in r3),count_scope='referências por acervo e década, rodada 3',data_url=gh('data/archive_decade_references.csv'),profile_url=gh('data/archive_profiles.csv'),bib='r3archive'+p['archive']))
registry += [
 dict(id='H14',name='Brasiliana / BBM: acervo geral',requested_url='https://www.brasiliana.usp.br/handle/bbm/1',access_url='https://digital.bbm.usp.br/handle/bbm/1',scope_note='Mesma biblioteca de H12; coleção geral, não outra instituição independente.',selected_references=sum(x['base']=='Brasiliana / BBM' for x in r4),count_scope='títulos inéditos selecionados, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='bbmAcervo2026'),
 dict(id='H15',name='Orkut preservado na Wayback',requested_url='https://web.archive.org/web/20141001005309/http://orkut.google.com/',access_url='https://web.archive.org/web/20141001005309/http://orkut.google.com/',scope_note='Conteúdo do Orkut preservado no serviço H16; não plataforma de preservação independente.',selected_references=sum(x['work_key']=='orkut-comunidades' for x in r4),count_scope='comunidade selecionada, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='r4orkutindex'),
 dict(id='H16',name='Wayback Machine: portal geral',requested_url='https://web.archive.org/',access_url='https://web.archive.org/',scope_note='Blog e fórum; Orkut contado separadamente em H15. O portal não foi pesquisado exaustivamente.',selected_references=sum(x['work_key'] in ['kibe-loco','forum-cifra-club'] for x in r4),count_scope='blog e fórum selecionados, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='waybackPortal2026'),
]
assert len(registry)==16 and len({x['id'] for x in registry})==16
writecsv('base_registry.csv',registry)

# Todos os domínios registrados, incluindo recursos técnicos e o histórico
# retirado. Não se transforma esse total em número de bases ou obras analisadas.
hosts=collections.defaultdict(list)
for x in manifest:hosts[urlsplit(x['url']).hostname].append(x)
domains=[]
for host,items in sorted(hosts.items()):
 domains.append(dict(domain=host,url=items[0]['url'],manifest_entries=len(items),downloaded_nonempty=sum(x['status']=='downloaded' and x.get('bytes',0)>0 for x in items),empty_responses=sum(x['status']=='downloaded' and x.get('bytes')==0 for x in items),failed=sum(x['status']=='failed' for x in items),scope='somente histórico de aquisição; referência retirada' if all(x['id']=='unb2026' for x in items) else 'fonte complementar, portal, documento ou serviço técnico; conferir URL individual no manifesto'))
writecsv('source_domains.csv',domains)

# Dois portais ainda não tinham entrada bibliográfica própria; reutilizar as
# treze entradas anteriores e a entrada do Orkut, sem duplicar referências.
bibpath=ROOT/'artigo/references.bib';bib=bibpath.read_text(encoding='utf-8').split('% BEGIN METHOD_INVENTORY')[0].rstrip()+'\n\n% BEGIN METHOD_INVENTORY\n'
bib+='''@misc{bbmAcervo2026,
 author={{Biblioteca Brasiliana Guita e José Mindlin}},
 title={Acervo Digital: coleção geral bbm/1},
 year={2026},
 howpublished={\\url{https://digital.bbm.usp.br/handle/bbm/1}},
 note={Portal de descoberta; não equivale à leitura integral do acervo. Acesso em 8 nov. 2026}
}
@misc{waybackPortal2026,
 author={{Internet Archive}},
 title={Wayback Machine: portal de preservação da web},
 year={2026},
 howpublished={\\url{https://web.archive.org/}},
 note={Capturas individuais e redirecionamentos documentados no manifesto. Acesso em 8 nov. 2026}
}
'''
bibpath.write_text(bib,encoding='utf-8',newline='\n')
bib_count=len(set(re.findall(r'@\w+\{([^,]+),',bib+'\n'+(ROOT/'artigo/annual.bib').read_text(encoding='utf-8'))))
evidence=collections.Counter(x['evidence'] for x in at)
metrics=[]
def metric(id,label,n,unit,scope,path):metrics.append(dict(id=id,indicator=label,value=str(n),unit=unit,scope=scope,data_url=gh(path)))
metric('M01','Endereços indicados pelo autor',len(registry),'endereços','Portais, coleções, item individual e captura; há sobreposições institucionais.','data/base_registry.csv')
metric('M02','Núcleo de representações autenticadas',len(at),'documentos/testemunhos','Inclui documentos primários e interações reportadas; exclui menções apenas lexicais.','data/attestations.csv')
metric('M03','Níveis do núcleo E1 / E2 / E3',f'{evidence["E1"]} / {evidence["E2"]} / {evidence["E3"]}','testemunhos',f'Imagem / texto primário eletrônico / interação reportada; partição dos {len(at)} registros.','data/attestations.csv')
metric('M04','Indicações iniciais com parecer',len(readcsv('references_audit.csv')),'indicações','Auditoria bibliográfica; não são 66 ocorrências positivas.','data/references_audit.csv')
metric('M05','Citações alegadas submetidas a verificação',len(readcsv('claims_verification.csv')),'alegações','Nenhuma autenticada integralmente; os resultados constam no parecer.','data/claims_verification.csv')
metric('M06','Referências por acervo e década',len(r3),'referências selecionadas','Rodada 3: inclui lexical, rubrica e mimética; parte já integra o núcleo.','data/archive_decade_references.csv')
metric('M07','Linhas de acompanhamento por acervo/década',len(readcsv('archive_decade_matrix.csv')),'linhas','Inclui quotas pendentes e uma linha com década indeterminada; não universo completo.','data/archive_decade_matrix.csv')
metric('M08','Títulos inéditos selecionados',len(r4),'títulos','Rodada 4: 14 Brasiliana e três espaços digitais; duas fontes já incorporadas ao núcleo.','data/revision4_new_titles.csv')
metric('M09','Anos no inventário anual do núcleo',len(readcsv('annual_coverage.csv')),'anos','1872–2026; anos sem testemunho não significam ausência histórica.','data/annual_coverage.csv')
metric('M10','Entradas no manifesto histórico',len(manifest),'entradas de aquisição','Inclui apoio, metadados, recursos técnicos, falhas e referências retiradas; não documentos lidos.','data/downloads.json')
metric('M11','Entradas com conteúdo baixado',sum(x['status']=='downloaded' and x.get('bytes',0)>0 for x in manifest),'entradas não vazias','Inclui HTML, PDF, imagem, JSON e código de interface; não equivale a leitura integral.','data/downloads.json')
metric('M12','Respostas vazias preservadas no manifesto',sum(x['status']=='downloaded' and x.get('bytes')==0 for x in manifest),'entradas vazias','Não contadas como documentos analisados ou resultados negativos.','data/downloads.json')
metric('M13','Entradas com falha de aquisição',sum(x['status']=='failed' for x in manifest),'entradas com falha','Estado registrado por identificador; não representa todas as tentativas históricas.','data/downloads.json')
metric('M14','Textos integrais com cópia pública',sum(bool(x.get('public_copy')) for x in manifest),'cópias públicas','Demais arquivos integrais ficam locais quando a redistribuição não foi verificada.','sources/README.md')
metric('M15','Referências bibliográficas',bib_count,'entradas BibTeX','Inclui teoria, documentos, catálogos e portais; não corresponde ao número de atestações.','artigo/references.bib')
annual_covered=sum(1900<=int(row['year'])<=2009 and int(row['confirmed_documents'])>0 for row in readcsv('annual_coverage.csv'))
metric('M16','Cobertura anual de 1900 a 2009',annual_covered,'anos com atestação','Intervalo de 110 anos. A busca dirigida incluiu rubricas e grafias miméticas.','data/annual_coverage.csv')
writecsv('method_quantification.csv',metrics)

def table(name,caption,columns,header,lines):
 out=[r'\small\begin{longtable}{'+columns+'}',r'\caption{'+caption+r'}\\',r'\toprule '+header+r'\\\midrule\endfirsthead',r'\toprule '+header+r'\\\midrule\endhead']+lines+[r'\bottomrule\end{longtable}\normalsize']
 (GEN/name).write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n')
col=lambda w:r'>{\raggedright\arraybackslash}p{'+w+r'\textwidth}'
table('method_quantification.tex','Balanço quantitativo do levantamento até 9 de novembro de 2026. As linhas têm unidades distintas e não devem ser somadas.',col('.31')+col('.13')+col('.45'),'Indicador & Quantidade & Unidade, escopo e dados',[tex(x['indicator'])+' & '+tex(x['value'])+' & '+tex(x['unit']+'. '+x['scope'])+r' \href{'+x['data_url']+r'}{Dados no GitHub} \\' for x in metrics])
table('base_registry.tex','Inventário consolidado dos 16 endereços indicados: portais, coleções, item e captura. Sobreposições não são novas bases independentes.',col('.29')+col('.38')+col('.22'),'ID / recurso & Relação entre os recursos & Seleção e rastreabilidade',[tex(x['id']+' '+x['name'])+r' \cite{'+x['bib']+'} & '+tex(x['scope_note'])+' & '+tex(str(x['selected_references'])+'; '+x['count_scope'])+r' \href{'+x['access_url']+r'}{Fonte}; \href{'+x['data_url']+r'}{GitHub} \\' for x in registry])

# Substitui apenas o balanço inicial desatualizado, preservando o plano
# estatístico e seus pressupostos, que continuam prospectivos.
doc=ROOT/'docs/METODOLOGIA.md';old=doc.read_text(encoding='utf-8');tail=old[old.index('## Unidade e denominador'):]
nonempty=sum(x['status']=='downloaded' and x.get('bytes',0)>0 for x in manifest)
empty=sum(x['status']=='downloaded' and x.get('bytes')==0 for x in manifest)
failed=sum(x['status']=='failed' for x in manifest)
downloaded=sum(x['status']=='downloaded' for x in manifest)
intro=f'''# Método documental e estatístico

Autor único: Murillo Edson de Carvalho Souza. Consulta: 8 e 9 de novembro de 2026.

## Balanço atualizado e dados vinculados

A coleta é dirigida, exploratória e não probabilística. O núcleo tem {len(at)} testemunhos: E1={evidence['E1']}, E2={evidence['E2']} e E3={evidence['E3']}. O núcleo cobre {annual_covered} dos 110 anos de 1900 a 2009. A ampliação por ano priorizou séries parlamentares brasileiras e portuguesas e periódicos brasileiros. As 66 indicações iniciais têm parecer individual; as 22 citações alegadas não foram autenticadas integralmente. Os números de 15 registros e 34 aquisições pertenciam à primeira versão e foram substituídos por este balanço consolidado.

Os 16 endereços indicados pelo autor estão no [inventário de bases](../data/base_registry.csv), com URL original, URL de acesso, sobreposições, quantidade selecionada e links para os dados. Não são 16 bases independentes: há portal e item do APESP, coleção e acervo geral da BBM e Orkut preservado no próprio Wayback.

O [quadro quantitativo](../data/method_quantification.csv), também incluído na metodologia do artigo, reúne quantidades e unidades. O núcleo, as {len(r3)} referências por acervo/década e os {len(r4)} títulos inéditos se sobrepõem: não se somam como documentos independentes. Somente duas das 17 novas fontes ampliaram o núcleo. As quotas da rodada 3 permanecem incompletas.

O manifesto histórico contém {len(manifest)} entradas: {nonempty} com conteúdo, {empty} respostas vazias e {failed} falhas. Essas entradas incluem arquivos auxiliares, páginas de catálogo, imagens, PDFs, metadados e recursos técnicos; não são {len(manifest)} obras analisadas nem um contador de todas as tentativas realizadas. As {downloaded} entradas com estado `downloaded` incluem as respostas vazias. O histórico também conserva uma referência posteriormente retirada; preservação de proveniência não equivale a citação atual no artigo.

Todos os domínios presentes no manifesto constam em [source_domains.csv](../data/source_domains.csv). Eles não são contados como bases independentes. O [manifesto](../data/downloads.json) fornece URLs individuais, resultado de aquisição, tamanho e SHA-256. Os [testemunhos do núcleo](../data/attestations.csv), os [registros por acervo/década](../data/archive_decade_references.csv), a [matriz de pendências](../data/archive_decade_matrix.csv) e os [títulos inéditos](../data/revision4_new_titles.csv) têm arquivos próprios. A [busca anual suplementar](../data/annual_supplement.csv) conserva a fonte e o localizador de cada novo testemunho.

E1: imagem primária inspecionada. E2: texto/transcrição primária eletrônica, sem colação integral com o impresso. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada, excluída do núcleo positivo. E1–E3 são categorias de cadeia de evidência, não escores estatísticos.

O gerador [build_method_inventory.py](../scripts/build_method_inventory.py) reconstrói o inventário e o balanço a partir dos dados públicos. Os links no PDF levam diretamente aos arquivos correspondentes no GitHub; o repositório e a versão/commit consultados devem acompanhar a reprodução.

'''
doc.write_text(intro+tail,encoding='utf-8',newline='\n')
summary=dict(requested_entry_points=len(registry),independent_bases_not_inferred=True,manifest_entries=len(manifest),nonempty_acquisitions=nonempty,empty_responses=empty,failed_entries=failed,technical_domains=len(domains),corpus_records=len(at),bibliographic_entries=bib_count,archive_decade_references=len(r3),new_titles=len(r4),counts_additive=False)
(DATA/'method_inventory_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary))
