"""Integra decisões codificadas da revisão documental de 08/11/2026."""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'data'
extra=[
dict(year=1919,document='Urupês, quinta edição',source_id='r2_urupes1919',country='Brasil',medium='livro',form='Quá, quá, quá!',locator='p. impressa 19; PDF p. 24; conto O engraçado arrependido',evidence='E1',bib='lobato1919',date_basis='ano do exemplar consultado, não da primeira edição'),
dict(year=1928,document='Diário Nacional, n. 290',source_id='r2_diario1928',country='Brasil',medium='jornal: transcrição',form='(risos, muito bem)',locator='17/06/1928; p. 4; discurso de Mattos Pimenta',evidence='E1',bib='diarionacional1928',date_basis='data impressa e passagem inspecionadas'),
dict(year=1947,document='Jornal de Notícias, n. 267',source_id='r2_folhamanha1947',country='Brasil',medium='jornal: transcrição',form='(Risos dos presentes)',locator='02/03/1947; p. 1; fala de Bidault; não é Folha da Manhã',evidence='E1',bib='jornalnoticias1947',date_basis='data impressa; texto traduzido de discurso francês'),
dict(year=2019,document='Macunaíma, edição UFFS',source_id='r2_macunaima_uffs',country='Brasil',medium='livro',form='Quá! quá! quá quaquá!...',locator='p. impressa e PDF 139; ficha catalográfica PDF 205',evidence='E1',bib='andrade2019',date_basis='edição consultada de 2019; obra original de 1928 sem cotejo daquela passagem'),
]
(D/'extra_attestations.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={r['id']:r for r in json.loads((D/'downloads.json').read_text(encoding='utf-8'))}
entries=[
('lobato1919','Monteiro Lobato','Urupês: quinta edição','r2_urupes1919','1919','p. 19; PDF p. 24; edição da Revista do Brasil; imagem conferida'),
('diarionacional1928','{Diário Nacional}','O anniversario da Secção Universitaria do Partido Democratico do Districto Federal','r2_diario1928','1928','17 jun.; n. 290; p. 4; rubrica conferida por imagem'),
('jornalnoticias1947','{Jornal de Notícias}','Bidault apresenta a questão da Espanha à Conferência das quatro potências em Moscou','r2_folhamanha1947','1947','2 mar.; n. 267; p. 1; grafia da rubrica conferida'),
('andrade2019','Mário de Andrade','Macunaíma: o herói sem nenhum caráter','r2_macunaima_uffs','2019','Editora UFFS; organização de Miguel Sanches Neto e Silvana Oliveira; p. 139'),
('r2canaa','Graça Aranha','Canaã: edição digital consultada','r2_canaa','','Fundação Darcy Ribeiro; PDF p. 28; referência lexical'),
('r2isaias','Lima Barreto','Recordações do escrivão Isaías Caminha: segunda edição','r2_isaias1917','1917','BBM-USP; PDF p. 26; referência lexical'),
('r2esfinge','Coelho Neto','Esfinge: capítulo VI','r2_esfinge_VI','1908','Wikisource; transcrição consultada; referência lexical'),
('r2eu','Augusto dos Anjos','Eu: Monólogo de uma sombra','r2_eu','1912','Edição eletrônica na Biblioteca Virtual Miguel de Cervantes; referência temática'),
('r2miramar','Oswald de Andrade','Memorias sentimentaes de João Miramar','r2_miramar1924','1924','BBM-USP; p. 114, PDF p. 116; referência lexical'),
('r2saobernardo','Graciliano Ramos','São Bernardo: provas da segunda edição','r2_saobernardo1938','1938','BBM-USP; PDF p. 63; referência lexical'),
('r2policarpo','Lima Barreto','Triste fim de Policarpo Quaresma','policarpo1915','1915','Project Gutenberg, e-book 67535; terceira parte, capítulo II; cotejo da fala atribuída'),
('r2meninamorta','{Biblioteca Brasiliana Guita e José Mindlin}','A menina morta: registro de edição de 1954','r2_meninabib','1954','Metadados bibliográficos; não atesta passagem de riso'),
('r2quinze','{Editora Record}','O quinze: página editorial','r2_quinze_meta','','Metadados de primeira publicação, 1930; leitura web; download HTTP 429'),
('r2fogo','{Academia Brasileira de Letras}','José Lins do Rego: bibliografia','r2_fogo_meta','','Metadados: Fogo morto, 1943; não atesta passagem'),
('r2continente','{Companhia das Letras}','O continente, volume 1: página editorial','r2_continente_meta','','Metadados da trilogia; não atesta passagem'),
('r2sagarana','{Museu Casa Guimarães Rosa}','Sagarana: sem edição e segunda edição','r2_sagarana_meta','1946','Registro museológico do exemplar; não atesta passagem'),
('r2grande','{Companhia das Letras}','Grande sertão: veredas: página editorial','r2_grande_meta','','Metadados editoriais; não atesta passagem'),
('r2quarup','{Editora Record}','Quarup: página editorial','r2_quarup_meta','','Metadados editoriais; leitura web; download HTTP 429; não atesta passagem'),
('r2paixao','{Museu da Língua Portuguesa}','A paixão segundo G.H.: registro de acervo','r2_paixao_meta','','Identificação bibliográfica; não atesta passagem'),
('r2zero','{Academia Brasileira de Letras}','Ignácio de Loyola Brandão: bibliografia','r2_zero_meta','','Edição italiana de 1974 e portuguesa de 1975; não atesta passagem'),
('r2meninas','{Companhia das Letras}','As meninas: página editorial','r2_meninas_meta','','Metadados editoriais; não atesta passagem'),
('r2getulio','{Companhia das Letras}','Sargento Getúlio: página editorial','r2_getulio_meta','','Identificação pela busca editorial; aquisição automática HTTP 404; não atesta passagem'),
('r2viva','{Companhia das Letras}','Viva o povo brasileiro: página editorial','r2_viva_meta','','Metadados editoriais; não atesta passagem'),
('r2alquimista','{Companhia das Letras}','O Alquimista: página editorial','r2_alquimista_meta','','Metadados editoriais; não atesta passagem'),
('r2feliz','{Companhia das Letras}','Feliz ano velho: página editorial','r2_feliz_meta2','','Metadados editoriais; não atesta passagem'),
('r2chove','{Universidade do Estado do Pará}','Programação ressalta vida e obra de Dalcídio Jurandir','r2_chove_meta','','Informa primeira publicação de Chove nos campos de Cachoeira em 1941; não atesta passagem'),
('r2budapeste','{Companhia das Letras}','Budapeste: página editorial','r2_budapeste_meta','','Data editorial: 10 set. 2003; não atesta passagem'),
('r2estorvo','{Companhia das Letras}','Estorvo: página editorial','r2_estorvo_meta','','Data editorial: 2 ago. 1991; não atesta passagem'),
('r2fon1925','{Fon-Fon!}','Commentarios da Semana: O Correio da Manhã','r2_fon1925','1925','Maio, p. 3; notícia do retorno após suspensão; imagem consultada'),
('r2gazeta1904','{Gazeta de Notícias}','Edição n. 207 de 25 de julho de 1904','r2_gazeta207','1904','Exemplar recuperado; frase atribuída não autenticada'),
('r2malho1912','{O Malho}','Edição n. 526 de 12 de outubro de 1912','r2_malho1912','1912','Exemplar recuperado; frase atribuída não autenticada'),
('r2diario1944','{Diário de Notícias}','Edição n. 6564 de 18 de março de 1944','r2_diario1944','1944','Exemplar recuperado; frase atribuída não autenticada'),
]
manual=[
('r2vestido','{Consórcio BDJur}','Vestido de noiva: registro bibliográfico','https://consorciobdjur.stj.jus.br/vufind/Record/1947/Details','Registro sobre escrita em 1943; não individualiza edição dos anos 1950'),
('r2morte','{Universidade Federal do Rio Grande do Norte}','Notícia acadêmica sobre A morte de D.J. em Paris','https://sigaa.ufrn.br/sigaa/public/programa/noticias_desc.jsf?id=65&lc=pt&noticia=136947610','Identificação da coletânea de 1975; não atesta passagem'),
]
bib=ROOT/'artigo/references.bib';text=bib.read_text(encoding='utf-8')
for key,author,title,sid,year,note in entries:
 if '@misc{'+key+',' in text:continue
 url=manifest[sid]['url'];text+='\n@misc{'+key+',\n  author = {'+author+'},\n  title = {'+title+'},\n'+('  year = {'+year+'},\n' if year else '')+'  howpublished = {\\url{'+url+'}},\n  note = {'+note+'. Acesso em 8 nov. 2026}\n}\n'
for key,author,title,url,note in manual:
 if '@misc{'+key+',' in text:continue
 text+='\n@misc{'+key+',\n  author = {'+author+'},\n  title = {'+title+'},\n  howpublished = {\\url{'+url+'}},\n  note = {'+note+'. Acesso em 8 nov. 2026}\n}\n'
bib.write_text(text,encoding='utf-8')
mapping=[4,1,10,8,16,13,23,19,30,25,31,32,40,37,46,43,54,49,55,56,64,61]
audit=list(csv.DictReader((D/'references_audit.csv').open(encoding='utf-8')))
checks=[dict(id=f'C{i:02}',reference_id=f'R{n:02}',status='citação integral não autenticada',finding=audit[n-1]['finding'],method='busca literal web; exame do texto/OCR quando adquirido; sem leitura visual integral de todos os volumes') for i,n in enumerate(mapping,1)]
with (D/'claims_verification.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(checks[0]));w.writeheader();w.writerows(checks)
