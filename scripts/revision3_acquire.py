"""Aquisição incremental dos 13 endereços indicados pelo autor."""
from revision2_download import run
ARCHIVES=[
('H01','DocVirt AJHPMJ','https://app.docvirt.com/dvd_ajhpmj/pageid/1'),
('H02','O Globo','https://oglobo.globo.com/acervo/'),
('H03','Folha','https://acervo.folha.com.br/index.do'),
('H04','BORE-USP Jornais','https://obrasraras.usp.br/xmlui/handle/123456789/4262'),
('H05','Hemeroteca Digital Brasileira','https://memoria.bn.gov.br/hdb/periodico.aspx'),
('H06','Correio Braziliense','https://www.correiobraziliense.com.br/acervo'),
('H07','Google News Jornal do Brasil','https://news.google.com/newspapers?nid=0qX8s2k1IRwC'),
('H08','Arquivo Público do Estado de São Paulo','https://atom.arquivoestado.sp.gov.br/'),
('H09','Senado Notícias Acervo Histórico','https://www12.senado.leg.br/noticias/acervo-historico'),
('H10','Diario de Pernambuco','https://www.diariodepernambuco.com.br/acervo'),
('H11','CEPE','https://acervo.cepe.com.br/'),
('H12','BBM-USP Gazeta do Rio de Janeiro','https://digital.bbm.usp.br/handle/bbm/8427'),
('H13','APESP item indicado','https://atom.arquivoestado.sp.gov.br/br-spapesp-hemapesp-s001-b000565-d000071;isad?sf_culture=fr'),
]
if __name__=='__main__':run([('r3_'+id.lower(),url,'html','consulta institucional; direitos por documento e coleção') for id,name,url in ARCHIVES])
