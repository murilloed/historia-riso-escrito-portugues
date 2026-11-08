from revision2_download import run
ROWS=[
('r3_bniframe','https://memoria.bn.gov.br/hdb/DefaultNew.aspx','html','interface pública de pesquisa'),
('r3_bore_asc','https://obrasraras.usp.br/xmlui/handle/123456789/4262/browse?type=dateissued','html','índice cronológico institucional'),
('r3_bore_desc','https://obrasraras.usp.br/xmlui/handle/123456789/4262/browse?type=dateissued&order=DESC','html','índice cronológico institucional'),
('r3_bbm_item','https://digital.bbm.usp.br/handle/bbm/8426','html','metadados de item; distinguir datas da série e exemplar'),
('r3_bbm1817','https://digital.bbm.usp.br/bitstream/bbm/8426/1/45000010974_Output.o.pdf','pdf','texto histórico; digitalização BBM-USP'),
('r3_cepe_xix','https://acervo.cepe.com.br/colecao-jornais-seculo-xix-recife','html','descrição de coleção'),
('r3_cepe_manha','https://acervo.cepe.com.br/colecao-do-jornal-diario-da-manha-1927-1985','html','descrição de coleção'),
('r3_cepe_suplemento','https://acervo.cepe.com.br/coletanea-do-suplemento-cultural-1986-2006','html','descrição de coleção'),
('r3_cepe_jesuitas','https://acervo.cepe.com.br/bens-dos-jesuitas','html','coleção de manuscritos e transcrição'),
('r3_senado_jornal','https://www12.senado.leg.br/noticias/acervo-historico/jornal-do-senado','html','índice institucional de 1995-2019'),
('r3_senado_revista','https://www12.senado.leg.br/noticias/acervo-historico/revista-em-discussao','html','índice institucional; endereço a validar'),
('r3_apesp_hemeroteca','https://atom.arquivoestado.sp.gov.br/hemeroteca-apesp','html','descrição arquivística; endereço a validar'),
]
if __name__=='__main__':run(ROWS)
