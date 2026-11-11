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
import audit_inventory
reconciled=json.loads((DATA/'consolidated_inventory.json').read_text(encoding='utf-8'))
for p in profiles:
 note='Portal/coleção; ver limitações de acesso e cobertura.'
 if p['archive']=='H08':note='Portal APESP; H13 é um item deste mesmo acervo.'
 if p['archive']=='H12':note='Coleção Gazeta na BBM; H14 é o acervo geral da mesma biblioteca.'
 if p['archive']=='H13':note='Item individual do APESP; não é outra base independente.'
 requested=p['url'] if p['archive']!='H13' else 'https://atom.arquivoestado.sp.gov.br/br-spapesp-hemapesp-s001-b000565-d000071;isad?sf_culture=fr'
 registry.append(dict(id=p['archive'],name=p['name'],requested_url=requested,access_url=p['url'],scope_note=note,selected_references=sum(x['archive']==p['archive'] for x in r3),count_scope='referências por acervo e década',data_url=gh('data/archive_decade_references.csv'),profile_url=gh('data/archive_profiles.csv'),bib='r3archive'+p['archive']))
registry += [
 dict(id='H14',name='Brasiliana / BBM: acervo geral',requested_url='https://www.brasiliana.usp.br/handle/bbm/1',access_url='https://digital.bbm.usp.br/handle/bbm/1',scope_note='Mesma biblioteca de H12; coleção geral, não outra instituição independente.',selected_references=sum(x['base']=='Brasiliana / BBM' for x in r4),count_scope='títulos inéditos selecionados, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='bbmAcervo2026'),
 dict(id='H15',name='Orkut preservado na Wayback',requested_url='https://web.archive.org/web/20141001005309/http://orkut.google.com/',access_url='https://web.archive.org/web/20141001005309/http://orkut.google.com/',scope_note='Conteúdo do Orkut preservado no serviço H16; não plataforma de preservação independente.',selected_references=sum(x['work_key']=='orkut-comunidades' for x in r4),count_scope='comunidade selecionada, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='r4orkutindex'),
 dict(id='H16',name='Wayback Machine: portal geral',requested_url='https://web.archive.org/',access_url='https://web.archive.org/',scope_note='Blog e fórum; Orkut contado separadamente em H15. O portal não foi pesquisado exaustivamente.',selected_references=sum(x['work_key'] in ['kibe-loco','forum-cifra-club'] for x in r4),count_scope='blog e fórum selecionados, rodada 4',data_url=gh('data/revision4_new_titles.csv'),profile_url=gh('docs/REVISAO-4.md'),bib='waybackPortal2026'),
]
assert len(registry)==16 and len({x['id'] for x in registry})==16
group_map={'H13':'H08','H14':'H12','H15':'H16'}
for entry in registry:
 entry['resource_group']=group_map.get(entry['id'],entry['id'])
resource_groups=len({x['resource_group'] for x in registry})
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
 note={Portal de descoberta; não equivale à leitura integral do acervo. Consulta documental registrada no inventário}
}
@misc{waybackPortal2026,
 author={{Internet Archive}},
 title={Wayback Machine: portal de preservação da web},
 year={2026},
 howpublished={\\url{https://web.archive.org/}},
 note={Capturas individuais e redirecionamentos documentados no manifesto. Consulta documental registrada no inventário}
}
'''
for row in {r['bib']: r for r in reversed(r3)}.values():
 if row['bib'].startswith('acervoD'):
  title=tex(row['title'])
  note=tex(row['locator']+'. '+row['date_basis'])
  bib+=f"@misc{{{row['bib']},\n key={{{title}}},\n title={{{title}}},\n year={{{row['date'][:4]}}},\n howpublished={{\\url{{{row['url']}}}}},\n note={{{note}}}\n}}\n"
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
metric('M06','Referências por acervo e década',len(r3),'referências selecionadas','Inclui menções lexicais, rubricas e grafias miméticas, com fontes alternativas identificadas na matriz.','data/archive_decade_references.csv')
metric('M07','Linhas de acompanhamento por acervo/década',len(readcsv('archive_decade_matrix.csv')),'linhas','135 linhas com referência e dois itens conferidos sem ocorrência; não é o universo de documentos.','data/archive_decade_matrix.csv')
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
metric('M17','Conjuntos de recursos de acesso indicados',resource_groups,'grupos operacionais','16 endereços agrupados: APESP portal/item, BBM coleção/acervo geral e Wayback/Orkut; não instituições independentes.','data/base_registry.csv')
metric('M18','Fontes da seleção por acervo/década',reconciled['archive_source_identifiers'],'identificadores de fonte','As 135 seleções reutilizam documentos entre quotas; 129 source_id distintos.','data/evidence_register.csv')
metric('M19','Fontes selecionadas nos quatro inventários',reconciled['unique_selected_source_identifiers'],'identificadores de fonte','Reconciliação por source_id e URL; não independência de obras, edições ou testemunhos.','data/consolidated_inventory.json')
metric('M20','Rubricas / marcadores miméticos e digitais do núcleo',str(reconciled['core_representation_categories']['rubrica descritiva'])+' / '+str(reconciled['core_representation_categories']['representação mimética ou marcador digital']),'registros','Partição do núcleo; rubricas descrevem reações, sem transcrever necessariamente o som.','data/consolidated_inventory.json')
metric('M21','Alternativas literárias de período',len(readcsv('period_alternatives.csv')),'fontes','Bocage 1800 e Gonzaga 1812; não ocorrências nos exemplares fixos da Gazeta.','data/period_alternatives.csv')
metric('M22','Itens conferidos sem ocorrência localizada',sum(x['status'].startswith('conferido:') for x in readcsv('archive_decade_matrix.csv')),'itens','Leitura concluída; não prova de ausência na série nem quota positiva.','data/archive_decade_matrix.csv')
metric('M23','Confirmação no acervo indicado / fonte alternativa',str(sum(bool(x['reference_id']) and x['status']!='confirmada em fonte alternativa' for x in readcsv('archive_decade_matrix.csv')))+' / '+str(sum(x['status']=='confirmada em fonte alternativa' for x in readcsv('archive_decade_matrix.csv'))),'linhas de quota','Partição das 135 seleções; confirmação alternativa não equivale a cotejo no portal original.','data/archive_decade_matrix.csv')
metric('M24','Classes lexicais / rubricas / miméticas da seleção', ' / '.join(str(reconciled['archive_selection_categories'][k]) for k in ['lexical','rubrica','mimética']),'seleções','Partição das 135 linhas; não prevalência histórica nem fontes distintas.','data/consolidated_inventory.json')
metric('M25','Domínios registrados no manifesto',len(domains),'hosts','Inclui subdomínios, serviços técnicos e aquisições falhas; não equivale a bases consultadas integralmente.','data/source_domains.csv')
metric('M26','Fontes anteriores a 1900',reconciled['pre1900_source_identifiers'],'identificadores de fonte','47 vínculos nos quatro inventários; inclui documentos desde 1645. Não é cobertura anual contínua.','data/consolidated_inventory.json')
metric('M27','Registros do núcleo dentro / fora de 1900–2009',str(reconciled['core_records_within_1900_2009'])+' / '+str(reconciled['core_records_outside_1900_2009']),'registros','Partição dos 121 registros; fora do intervalo há três anteriores a 1900 e oito posteriores a 2009.','data/consolidated_inventory.json')
writecsv('method_quantification.csv',metrics)

def table(name,caption,columns,header,lines):
 out=[r'\small\begin{longtable}{'+columns+'}',r'\caption{'+caption+r'}\\',r'\toprule '+header+r'\\\midrule\endfirsthead',r'\toprule '+header+r'\\\midrule\endhead']+lines+[r'\bottomrule\end{longtable}\normalsize']
 (GEN/name).write_text('\n'.join(out)+'\n',encoding='utf-8',newline='\n')
col=lambda w:r'>{\raggedright\arraybackslash}p{'+w+r'\textwidth}'
table('method_quantification.tex','Balanço quantitativo consolidado do levantamento. As linhas têm unidades distintas e não devem ser somadas.',col('.31')+col('.13')+col('.45'),'Indicador & Quantidade & Unidade, escopo e dados',[tex(x['indicator'])+' & '+tex(x['value'])+' & '+tex(x['unit']+'. '+x['scope'])+r' \href{'+x['data_url']+r'}{Dados no GitHub} \\' for x in metrics])
table('base_registry.tex','Inventário consolidado dos 16 endereços indicados: portais, coleções, item e captura. Sobreposições não são novas bases independentes.',col('.29')+col('.38')+col('.22'),'ID / recurso & Relação entre os recursos & Seleção e rastreabilidade',[tex(x['id']+' '+x['name'])+r' \cite{'+x['bib']+'} & '+tex(x['scope_note'])+' & '+tex(str(x['selected_references'])+'; '+x['count_scope'])+r' \href{'+x['access_url']+r'}{Fonte}; \href{'+x['data_url']+r'}{GitHub} \\' for x in registry])

matrix=readcsv('archive_decade_matrix.csv')
alternative=sum(x['status']=='confirmada em fonte alternativa' for x in matrix)
direct=sum(bool(x['reference_id']) for x in matrix)-alternative
archive_summary=dict(archive_addresses=len(profiles),matrix_rows=len(matrix),
                     confirmed_archive_decade_cells=direct,alternative_source_cells=alternative,
                     pending_quota_cells=sum(x['status'].startswith('pendente:') for x in matrix),
                     selected_references=len(r3),new_core_documents_round3=4,
                     scope_completed=all(bool(x['reference_id']) for x in matrix),
                     quota_completed=not any(x['status'].startswith('pendente:') for x in matrix),
                     items_without_attestation=sum(x['status'].startswith('conferido: sem ocorrência localizada') for x in matrix),
                     fixed_item_reviews_completed=sum(x['status'].startswith('conferido:') for x in matrix),
                     fixed_item_reviews_pending=sum(not x['reference_id'] and not x['status'].startswith('conferido:') for x in matrix),
                     period_alternatives=len(readcsv('period_alternatives.csv')),checked_on='2026-11-11')
# Valores usados no texto do artigo e na síntese pública, derivados dos CSV.
counts=dict(CoreEOne=evidence['E1'],CoreETwo=evidence['E2'],CoreEThree=evidence['E3'],CoreRubrics=reconciled['core_representation_categories']['rubrica descritiva'],CoreMimetic=reconciled['core_representation_categories']['representação mimética ou marcador digital'],CoreWithin=reconciled['core_records_within_1900_2009'],CoreOutside=reconciled['core_records_outside_1900_2009'],CoreMinYear=reconciled['core_earliest_year'],CoreMaxYear=reconciled['core_latest_year'],SelectedMinYear=reconciled['earliest_selected_year'],SelectedMaxYear=reconciled['latest_selected_year'],PreNineteenSources=reconciled['pre1900_source_identifiers'],PreNineteenLinks=reconciled['pre1900_record_memberships'],ArchiveLinkCount=len(r3),ArchiveSourceCount=reconciled['archive_source_identifiers'],ArchiveDirect=direct,ArchiveAlternative=alternative,MatrixRowCount=len(matrix),EvidenceSources=reconciled['unique_selected_source_identifiers'],EvidenceMemberships=reconciled['combined_record_memberships'],RequestedAddresses=len(registry),ResourceGroups=resource_groups,BibEntryCount=bib_count)
slash=chr(92)
(GEN/'inventory_counts.tex').write_text(''.join(slash+'newcommand{'+slash+k+'}{'+str(v)+'}'+chr(10) for k,v in counts.items()),encoding='utf-8',newline='\n')
state=f"""O núcleo reúne **{len(at)} registros**, classificados em **{evidence['E1']} E1, {evidence['E2']} E2 e {evidence['E3']} E3**, com datas de **{reconciled['core_earliest_year']} a {reconciled['core_latest_year']}**. Há **{reconciled['core_records_within_1900_2009']} registros no intervalo de 1900–2009**, um em cada um dos **{annual_covered} anos**, e **{reconciled['core_records_outside_1900_2009']} fora dele**. São **{counts['CoreRubrics']} rubricas descritivas** e **{counts['CoreMimetic']} representações miméticas ou marcadores digitais**, portanto não {len(at)} exemplos de onomatopeia. A ampliação anual incorporou 96 registros — 87 parlamentares e nove da imprensa periódica — já incluídos no total. Há documentos brasileiros e portugueses; a seleção não é amostra representativa de uso nacional. **Os quatro inventários positivos incluem fontes de {reconciled['earliest_selected_year']} a {reconciled['latest_selected_year']}, com {reconciled['pre1900_source_identifiers']} identificadores anteriores a 1900, sem cobertura anual contínua desse período.** O quadro anual estende-se até 2026, ano sem atestação selecionada no núcleo."""
readme=ROOT/'README.md';current=readme.read_text(encoding='utf-8');start='<!-- BEGIN CURRENT_CORE_SUMMARY -->';end='<!-- END CURRENT_CORE_SUMMARY -->'
if start in current:
 left=current.index(start)+len(start);right=current.index(end,left);current=current[:left]+'\n'+state+'\n'+current[right:];readme.write_text(current,encoding='utf-8',newline='\n')
(DATA/'current_state.json').write_text(json.dumps(dict(text=state,counts=counts,source='CSV versionados; scripts/build_method_inventory.py'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
(DATA/'archive_summary.json').write_text(json.dumps(archive_summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
table('archive_profiles.tex','Recortes e condições de acesso dos 13 endereços consultados.',
      col('.20')+col('.32')+col('.37'),'ID / acervo & Recorte e fundamento & Situação',
      [tex(p['archive']+' '+p['name'])+' & '+tex(p['start']+'--'+p['end']+'. '+p['date_basis'])+' & '+
       tex(p['access_finding'])+r' \cite{r3archive'+p['archive']+r'} \\' for p in profiles])
table('archive_references.tex','Referências selecionadas por década e acervo, com fontes alternativas identificadas na matriz.',
      col('.13')+col('.53')+col('.23'),'Acervo / década & Documento e localização & Ocorrência / categoria',
      [tex(r['archive']+' / '+r['decade'])+' & '+tex(r['title']+'; '+r['date']+'; '+r['locator'])+
       ' & '+tex(r['form']+'; '+r['kind'])+r' \cite{'+r['bib']+r'} \\' for r in r3])
table('archive_matrix.tex','Matriz por acervo e década. A confirmação em fonte alternativa conserva a pendência de conferência na plataforma indicada.',
      col('.10')+col('.13')+col('.66'),'Acervo & Década & Resultado',
      [' & '.join(map(tex,[r['archive'],'n/d' if r['decade']=='indeterminada' else r['decade'],
       r['status']+(' ('+r['reference_id']+')' if r['reference_id'] else '')]))+r' \\' for r in matrix])

# Substitui apenas o balanço inicial desatualizado, preservando o plano
# estatístico e seus pressupostos, que continuam prospectivos.
doc=ROOT/'docs/METODOLOGIA.md';old=doc.read_text(encoding='utf-8');tail=old[old.index('## Unidade e denominador'):]
nonempty=sum(x['status']=='downloaded' and x.get('bytes',0)>0 for x in manifest)
empty=sum(x['status']=='downloaded' and x.get('bytes')==0 for x in manifest)
failed=sum(x['status']=='failed' for x in manifest)
downloaded=sum(x['status']=='downloaded' for x in manifest)
intro=f'''# Método documental e estatístico

Autor único: Murillo Edson de Carvalho Souza.

## Balanço atualizado e dados vinculados

A coleta é dirigida, exploratória e não probabilística. O núcleo tem {len(at)} testemunhos: E1={evidence['E1']}, E2={evidence['E2']} e E3={evidence['E3']}. O núcleo abrange {reconciled["core_earliest_year"]}–{reconciled["core_latest_year"]}: {reconciled["core_records_within_1900_2009"]} registros estão entre 1900 e 2009, um em cada um dos {annual_covered} anos, e {reconciled["core_records_outside_1900_2009"]} ficam fora desse intervalo. O quadro de acompanhamento chega a 2026, sem atestação selecionada nesse ano. A ampliação por ano priorizou séries parlamentares brasileiras e portuguesas e periódicos brasileiros. As 66 indicações iniciais têm parecer individual; as 22 citações alegadas não foram autenticadas integralmente. O núcleo contém 96 rubricas descritivas e 25 representações miméticas ou marcadores digitais; as categorias não são intercambiáveis. O levantamento mais amplo inclui documentos desde 1645: são {reconciled["pre1900_source_identifiers"]} identificadores de fonte anteriores a 1900 em {reconciled["pre1900_record_memberships"]} vínculos, sem cobertura anual contínua desse período.

Os 16 endereços indicados pelo autor estão no [inventário de bases](../data/base_registry.csv), com URL original, URL de acesso, sobreposições, quantidade selecionada e links para os dados. São {resource_groups} conjuntos operacionais de recursos de acesso, após agrupar portal/item do APESP, coleção/acervo geral da BBM e Orkut/Wayback. Essa definição se aplica aos endereços indicados, não ao universo de instituições ou fontes complementares; os domínios do manifesto não são contados como bases.

O [quadro quantitativo](../data/method_quantification.csv), também incluído na metodologia do artigo, reúne quantidades e unidades. O núcleo, as {len(r3)} referências por acervo/década e os {len(r4)} títulos inéditos se sobrepõem: não se somam como documentos independentes. Somente duas das 17 novas fontes ampliaram o núcleo. As 135 quotas por acervo e década têm referência selecionada, 70 em fontes alternativas; dois itens individuais têm conferência concluída sem ocorrência localizada, com duas alternativas de período registradas separadamente. Isso não equivale a confirmação nesses exemplares.

Os quatro inventários positivos têm {reconciled['combined_record_memberships']} vínculos de registro e {reconciled['unique_selected_source_identifiers']} identificadores de fonte distintos. As {len(r3)} seleções de quota correspondem a {reconciled['archive_source_identifiers']} fontes por source_id. A reconciliação e os vínculos estão em [consolidated_inventory.json](../data/consolidated_inventory.json) e [evidence_register.csv](../data/evidence_register.csv). Identidade de URL não prova independência textual.

O manifesto histórico contém {len(manifest)} entradas: {nonempty} com conteúdo, {empty} respostas vazias e {failed} falhas. Essas entradas incluem arquivos auxiliares, páginas de catálogo, imagens, PDFs, metadados e recursos técnicos; não são {len(manifest)} obras analisadas nem um contador de todas as tentativas realizadas. As {downloaded} entradas com estado `downloaded` incluem as respostas vazias. O histórico também conserva uma referência posteriormente retirada; preservação de proveniência não equivale a citação atual no artigo.

Todos os domínios presentes no manifesto constam em [source_domains.csv](../data/source_domains.csv). Eles não são contados como bases independentes. O [manifesto](../data/downloads.json) fornece URLs individuais, resultado de aquisição, tamanho e SHA-256. Os [testemunhos do núcleo](../data/attestations.csv), os [registros por acervo/década](../data/archive_decade_references.csv), a [matriz de pendências](../data/archive_decade_matrix.csv) e os [títulos inéditos](../data/revision4_new_titles.csv) têm arquivos próprios. A [busca anual suplementar](../data/annual_supplement.csv) conserva a fonte e o localizador de cada novo testemunho.

E1: imagem primária inspecionada. E2: texto/transcrição primária eletrônica, sem colação integral com o impresso. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada, excluída do núcleo positivo. E1–E3 são categorias de cadeia de evidência, não escores estatísticos.

O gerador [build_method_inventory.py](../scripts/build_method_inventory.py) reconstrói o inventário e o balanço a partir dos dados públicos. Os links no PDF levam diretamente aos arquivos correspondentes no GitHub; o repositório e a versão/commit consultados devem acompanhar a reprodução.

'''
doc.write_text(intro+tail,encoding='utf-8',newline='\n')
summary=dict(requested_entry_points=len(registry),requested_resource_groups=resource_groups,independent_bases_not_inferred=True,manifest_entries=len(manifest),nonempty_acquisitions=nonempty,empty_responses=empty,failed_entries=failed,technical_domains=len(domains),corpus_records=len(at),bibliographic_entries=bib_count,archive_decade_references=len(r3),new_titles=len(r4),counts_additive=False)
(DATA/'method_inventory_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary))
