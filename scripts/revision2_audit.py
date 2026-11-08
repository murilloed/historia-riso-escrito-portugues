"""Segunda auditoria: parecer individual; metadado não é atestação de grafia."""
from pathlib import Path
import csv,json,re,unicodedata,collections
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'data';G=ROOT/'artigo/generated'
def write(name,rows):
 with (D/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def esc(s):
 return str(s).replace('&',r'\&').replace('_',r'\_').replace('%',r'\%').replace('#',r'\#').replace('—','-').replace('–','-')
def norm(s):return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip()
manifest={r['id']:r for r in json.loads((D/'downloads.json').read_text(encoding='utf-8'))}
rows=list(csv.DictReader((D/'candidate_sources.csv').open(encoding='utf-8')))
# Os números correspondem à ordem imutável das 66 sugestões recebidas.
notes={
1:('I','r2_gazeta207','Exemplar de 25/07/1904, n. 207, recuperado; busca no OCR das quatro páginas não autenticou a frase do ovo. OCR degradado impede conclusão negativa definitiva.'),
2:('S','','Busca por título, década e riso não individualizou artigo, edição e página. A descrição genérica não comprova grafia.'),
3:('S','','Sem ano e edição do almanaque ou título da anedota. Busca não individualizou ocorrência; é necessário delimitar volume e seção.'),
4:('L','r2_canaa','Texto integral recuperado: expressão de riso, PDF p. 28. Referência lexical; não autentica o diálogo atribuído ao colono Maciel.'),
5:('L','r2_isaias1917','Exemplar consultado: segunda edição, 1917, PDF p. 26: Riu-se muito. Não datar a passagem de 1909 sem cotejo da primeira edição.'),
6:('L','r2_esfinge_VI','Oito capítulos consultados; capítulo VI contém risos casquinados. É descrição lexical, não uma sequência onomatopaica demonstrada.'),
7:('S','','A busca recuperou Quá em Quase doutor, Careta, 08/05/1915, via Vida urbana. Contexto de recusa, não riso: falso positivo excluído.'),
8:('I','r2_malho1912','Edição n. 526 de 12/10/1912 confirmada na capa. Busca nas 58 páginas do OCR não autenticou prefeito/carne barata; desenhos exigem revisão visual integral.'),
9:('S','','Pista alternativa: poema Epístola, A Cigarra, n. 16, 20/01/1915, p. 27, em reprodução externa. Não conferida no exemplar original; não incluída no corpus.'),
10:('L','policarpo1915','Texto de 1915 consultado. Terceira parte, cap. II, contém Você, Quaresma, é um visionario; sem Ah! ah! e sem a continuação sobre plantar. Citação recebida não é transcrição fiel.'),
11:('A','r2_urupes1919','Quinta edição de 1919: p. impressa 19, PDF p. 24: Quá, quá, quá!, com risos explícitos no contexto. Não retrodatado automaticamente a 1918.'),
12:('L','r2_eu','Monólogo de uma sombra: Chorando e rindo na ironia infausta. Confirma referência temática, não onomatopeia.'),
13:('S','r2_fon1925','Frase de 14/02/1925 não autenticada. Fon-Fon!, maio de 1925, p. 3, noticia retorno do Correio após suspensão; é indício de problema cronológico, não prova autônoma de que não existiu edição em fevereiro.'),
14:('A','r2_diario1928','17/06/1928, n. 290, p. 4: (risos, muito bem), em discurso de Mattos Pimenta. Rubrica descritiva, não grafia de gargalhada.'),
15:('S','','Busca por título, década e risos não individualizou reportagem verificável; faltam dia e página.'),
16:('A','r2_macunaima_uffs','Edição UFFS de 2019, p. 139: Quá! quá! quá quaquá!... e indicação de gargalhada. Obra original de 1928; a passagem não é a frase Ah! ah! enviada.'),
17:('L','r2_miramar1924','Exemplar de 1924, p. 114, PDF p. 116: morreu nos lábios de todos o sorriso. Referência lexical; não comprova onomatopeia.'),
18:('B','r2_meninabib','BBM-USP registra edição de 1954. A alegação de composição nos anos 1920 não foi demonstrada. Nenhuma passagem de riso autenticada.'),
19:('I','r2_fon1935','PDF identificado pelo acervo como n. 23 de 1935 recuperado; capa e OCR consultados. Data de 08/06 e frase sobre rei da Inglaterra não autenticadas; falta conferir expediente legível.'),
20:('S','r2_radical1935','Exemplar n. 1175 de 1935 recuperado e OCR pesquisado. Há candidatos lexicais, mas nenhuma grafia atribuída autenticada por imagem.'),
21:('S','r2_batalha1930','Exemplar n. 31 de 1930 recuperado e OCR pesquisado. Referências lexicais candidatas não autenticam a generalização sobre marcações de riso.'),
22:('B','r2_quinze_meta','Editora Record confirma estreia em 1930; aquisição automática recebeu HTTP 429. Não se confirmou passagem nem grafia.'),
23:('L','r2_saobernardo1938','Provas da segunda edição, 1938, recuperadas; PDF p. 63: sorrisos frios. A frase latim de missa não foi localizada no OCR; não retrodatado a 1934.'),
24:('S','','Reforma Agrária (1934), de Marquie: buscas por título, ano e variante do nome não identificaram registro bibliográfico suficiente. Não tratar como obra inexistente.'),
25:('I','r2_diario1944','Edição de 18/03/1944, n. 6564, confirmada no cabeçalho. Busca do OCR não autenticou ministro/boatos de racionamento; texto de baixa qualidade.'),
26:('S','','Busca por título, ano e rubrica não individualizou transmissão ou reportagem com página. Não demonstrada a descrição recebida.'),
27:('S','','Busca produziu falso positivo: Jornal de Notícias, de 02/03/1947, e não Folha da Manhã. Documento incluído separadamente; não substitui esta referência.'),
28:('B','r2_fogo_meta','Bibliografia da Academia Brasileira de Letras confirma Fogo morto, 1943. Texto e passagem sobre riso não conferidos.'),
29:('B','r2_continente_meta','Editora identifica O Continente na trilogia publicada entre 1949 e 1962. Metadado não autentica diálogo de caserna ou taberna.'),
30:('B','r2_sagarana_meta','Museu Casa Guimarães Rosa registra exemplar de Sagarana de 1946. Frase He! he! e mundo dá muitas voltas não autenticada.'),
31:('S','','Revista de 1950 e alegado Almanaque de 1953 não são a mesma referência. Faltam número, história e página para verificar moedas e Quá-quá-quá.'),
32:('S','','Busca de frase e jornal não localizou plano é honesto. Ano de 1955 sem dia, coluna e página não individualiza o documento.'),
33:('S','','Busca por jornal, década e risos não individualizou crônica. É necessária referência de edição.'),
34:('B','r2_grande_meta','Página editorial de Grande sertão: veredas consultada; primeira edição em 1956. Nenhuma passagem específica de riso foi autenticada.'),
35:('B','','Registro institucional sobre Vestido de noiva identifica escrita em 1943; estreia e publicação são eventos distintos. A edição em livro dos anos 1950 não foi individualizada.'),
36:('S','','Crônicas de Stanislaw Ponte Preta não designa título, edição ou crônica específica. Identidade do cronista não confirma data e grafia de passagem.'),
37:('S','r2_pasquim1969','Coleção identificada no dossiê da Biblioteca Nacional. URL tentada para n. 12 retornou 404; diálogo atribuído a Jaguar permanece não autenticado.'),
38:('S','','A reforma gráfica do jornal não demonstra uso de hahaha. Busca não localizou entrevista e página específicas na década de 1960.'),
39:('S','','Sem edição e entrevistado identificados. Busca por título, década e rubrica não autenticou onomatopeia corrida.'),
40:('B','r2_quarup_meta','Página editorial de Quarup localizada; download automático HTTP 429. Frase sobre jornais não autenticada e sem página.'),
41:('B','r2_paixao_meta','Registro museológico localizado para A paixão segundo G.H.; download retorna página sem conteúdo textual suficiente. Não confirma sorriso mental ou grafia.'),
42:('B','r2_zero_meta','ABL distingue edição italiana de 1974 e portuguesa de 1975. Alegada composição nos anos 1960 não autoriza contar publicação naquela década.'),
43:('S','','Menção genérica a gibis dos anos 1970. Busca não individualizou número e história com as formas atribuídas.'),
44:('S','','Busca por Opinião, década e risos não individualizou passagem verificável. A caracterização ideológica não prova grafia.'),
45:('S','','Busca por Movimento, década e risos não individualizou debate com localizador. Pendente identificação de edição.'),
46:('B','r2_meninas_meta','Página editorial de As meninas consultada. Frase sobre aposta e Ha-ha-ha! não autenticada; sem acesso integral conferido.'),
47:('B','r2_getulio_meta','Página editorial localizada na busca; aquisição automática falhou com 404. Data de obra não é prova de uma risada específica.'),
48:('B','r2_morte_meta','Coletânea de 1975 identificada também em pesquisa institucional UFRN; catálogo WorldCat bloqueou aquisição com 403. Nenhuma passagem de riso confirmada.'),
49:('S','','Busca da data 14/11/1986 e frase de congelamento não autenticou Rs. na seção Painel. Rubrica risos de outra publicação de 1994 não substitui esta alegação.'),
50:('S','','Busca por Zózimo, década e rs não individualizou nota. Não demonstrado uso comum de rs no jornal nos anos 1980.'),
51:('S','','Busca por jornal, década e rsrs não individualizou nota. Alegada economia da datilografia permanece explicação sem evidência específica.'),
52:('B','r2_viva_meta','Página editorial de Viva o povo brasileiro consultada. Descrição literária genérica não comprova forma particular de riso.'),
53:('B','r2_alquimista_meta','Página editorial de O Alquimista consultada. Sorriso e rir são itens lexicais; não devem ser classificados automaticamente como interjeições.'),
54:('B','r2_feliz_meta2','Página editorial de Feliz ano velho consultada. Frase burradas do colégio e sequência Ha ha ha não autenticadas.'),
55:('S','','Busca de Veja, 07/05/1993 e frase não fugirei da raia não individualizou entrevista. Data e entrevistado continuam sem autenticação.'),
56:('S','','Busca de Folhateen, junho de 1997, mIRC e grafias não identificou reportagem com dia e página. Não confirmada a frase recebida.'),
57:('S','','Busca de Bizz, década e hahaha não identificou entrevista específica. Sem edição, autoria e página.'),
58:('B','r2_chove_meta','Fonte institucional UEPA registra primeira publicação em 1941. Ano de 1998 pode designar edição; não é data de nascimento da obra nem da passagem.'),
59:('B','r2_budapeste_meta','Página editorial informa lançamento em 10/09/2003. Planejamento nos anos 1990 não demonstrado e não equivale a publicação.'),
60:('B','r2_estorvo_meta','Página editorial informa lançamento em 02/08/1991. Nenhuma passagem sobre riso foi conferida no texto integral.'),
61:('S','','Busca de Capricho, setembro de 2007 e frase quase quebrou a cara não individualizou reportagem. Não se sustenta afirmação de primeira impressão de kkkk.'),
62:('S','','Caderno de Informática de dois jornais é referência ambígua. Busca por internetês e kkkk não individualizou tabela de abreviações com data e página.'),
63:('S','','Busca por Meia Hora, 2005 e kkkk não identificou manchete. Fundação do veículo não demonstra adoção de grafia específica.'),
64:('S','','Título, autor e editora do alegado livro de 2005 não identificados. Resultado homônimo é postagem de blog de 2008, que não autentica o livro.'),
65:('S','','Manual do MSN Messenger sem autor, ISBN ou editora. Busca não individualizou obra e edição; não autentica convenções descritas.'),
66:('S','','Literatura de Blog é categoria, não referência bibliográfica individual. Cardosonline e Melhores do Mundo não podem ser convertidos em livro sem título, autor e edição.'),
}
audit=[]
for i,r in enumerate(rows,1):
 status,sid,note=notes[i];source=manifest.get(sid,{})
 audit.append(dict(id=f'R{i:02}',claimed_decade=r['claimed_decade'],type=r['type'],description_from_input=r['description_from_input'],status=status,source_id=sid,source_url=source.get('url',''),acquisition_status=source.get('status','não adquirido'),finding=note,scope='busca exploratória e documentos expressamente indicados; não exaustão de acervo',checked_on='2026-11-08'))
audit[34]['source_url']='https://consorciobdjur.stj.jus.br/vufind/Record/1947/Details'
audit[47]['source_url']='https://sigaa.ufrn.br/sigaa/public/programa/noticias_desc.jsf?id=65&lc=pt&noticia=136947610'
write('references_audit.csv',audit)
counts=dict(collections.Counter(x['status'] for x in audit))
(D/'revision2_summary.json').write_text(json.dumps(dict(total=66,status_counts=counts,legend={'A':'ocorrência de representação do riso autenticada','L':'referência lexical ou temática; não autentica grafia atribuída','B':'identificação bibliográfica; passagem não autenticada','I':'exemplar específico recuperado; citação atribuída não autenticada','S':'busca sem ocorrência autenticada ou referência insuficiente'}),ensure_ascii=False,indent=2),encoding='utf-8')
body=[r'\small\begin{longtable}{p{0.07\textwidth}p{0.08\textwidth}p{0.72\textwidth}}',r'\caption{Parecer individual sobre as 66 indicações. A: representação autenticada; L: referência lexical; B: identificação bibliográfica; I: exemplar específico; S: sem ocorrência autenticada.}\\',r'\toprule ID & Estado & Resultado e limites \\\midrule\endfirsthead',r'\toprule ID & Estado & Resultado e limites \\\midrule\endhead']
for r in audit:body.append(r['id']+' & '+r['status']+' & '+esc(r['finding'])+r'\\')
body.append(r'\bottomrule\end{longtable}\normalsize')
(G/'references-audit-table.tex').write_text('\n'.join(body),encoding='utf-8')
# Publicar metadados de busca, sem republicar excertos dos motores de busca.
for p in (D/'searches').glob('*.json'):
 r=json.loads(p.read_text(encoding='utf-8'))
 if 'response' in r:
  raw=str(r.pop('response'));r['result_urls']=sorted(set(re.findall(r'https?://[^\s<>\)"\\]+',raw)))
  r['interpretation']='Resultados de busca são pistas; não equivalem à inspeção do documento.'
  r['searched_on']='2026-11-08';p.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(counts))
