"""Segunda rodada: aquisição incremental, com manifesto e falhas explícitas."""
from collect import get,ROOT
import json,concurrent.futures,urllib.parse
try:
 import truststore
 truststore.inject_into_ssl()
except ImportError:pass
ROWS=[
('r2_canaa','https://fundar.org.br/wp-content/uploads/2021/06/canaa.pdf','pdf','edição institucional; manter íntegra local até revisão de direitos editoriais'),
('r2_isaias1917','https://digital.bbm.usp.br/bitstream/bbm/4808/1/001228_COMPLETO.pdf','pdf','BBM-USP; domínio público declarado'),
('r2_miramar1924','https://digital.bbm.usp.br/bitstream/bbm/8828/1/45000019398_Output.o.pdf','pdf','BBM-USP; texto histórico; direitos de ilustrações a verificar'),
('r2_urupes1919','https://libsysdigi.library.uiuc.edu/OCA/Books2010-12/3394502/3394502.pdf','pdf','biblioteca universitária; digitalização histórica'),
('r2_eu','https://www.letrasgalegas.org/obra-visor/eu--0/html/ffc942a2-82b1-11df-acc7-002185ce6064_3.html','html','edição eletrônica de texto histórico; atribuir provedor'),
('r2_saobernardo1938','https://digital.bbm.usp.br/bitstream/bbm/8418/1/45000003127_Output.o.pdf','pdf','BBM-USP; provas de edição de 1938; não confundir com primeira edição'),
('r2_quinze_portal','https://docente.ifrn.edu.br/paulomartins/livros-classicos-de-literatura/o-quinze-rachel-de-queiroz/view','html','portal docente; acesso não equivale a licença de republicação'),
('r2_meninabib','https://digital.bbm.usp.br/handle/bbm/2873','html','metadados institucionais'),
('r2_isaiasbib','https://digital.bbm.usp.br/handle/bbm/4808','html','metadados institucionais'),
('r2_miramarbib','https://digital.bbm.usp.br/handle/bbm/8828','html','metadados institucionais'),
]
ROWS += [('r2_esfinge_'+c,'https://pt.wikisource.org/wiki/Esfinge_(Coelho_Neto)/'+c,'html','transcrição eletrônica de edição de 1908; Wikisource') for c in ['I','II','III','IV','V','VI','VII','VIII']]
def acquire(row):
 row=(row[0],urllib.parse.quote(row[1],safe=':/?=&%#'),row[2],row[3])
 return get(row)
def run(rows):
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(acquire,rows))
 p=ROOT/'data/downloads.json';manifest={x['id']:x for x in json.loads(p.read_text(encoding='utf-8'))}
 for r in results:manifest[r['id']]=r;print(r['id'],r['status'],r.get('bytes',r.get('error','')))
 p.write_text(json.dumps(list(manifest.values()),ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':run(ROWS)
