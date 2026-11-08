from revision2_download import run
ROWS=[
('r3_apesp_jornais','https://atom.arquivoestado.sp.gov.br/br-spapesp-hemapesp-s001','html','descrição da série de jornais'),
('r3_cepe_reader_xix','http://200.238.101.22/docreader/docreader.aspx?bib=SECXIX','html','leitor público indicado pela CEPE'),
('r3_cepe_reader_jesuitas','http://200.238.101.22/docreader/docreader.aspx?bib=Livro_PDF','html','leitor público indicado pela CEPE'),
('r3_cepe_reader1927','http://200.238.101.22/docreader/docreader.aspx?bib=DM1927','html','leitor público indicado pela CEPE'),
('r3_cepe_reader1986','http://200.238.101.22/docreader/docreader.aspx?bib=SPFULL&pasta=1986','html','leitor público indicado pela CEPE'),
('r3_globo_historia','https://historia.globo.com/historia-grupo-globo/2005-2014/noticia/2013-lancamento-do-site-acervo-o-globo.ghtml','html','descrição institucional da cobertura'),
('r3_cb_memoria','https://www.correiobraziliense.com.br/historia-de-brasilia','html','descrição institucional do acervo'),
('r3_bn_recomposicao','https://www.gov.br/bn/pt-br/central-de-conteudos/noticias/aos-usuarios-da-hemeroteca-digital-brasileira-3','html','comunicado oficial sobre acesso e recomposição gradual'),
]
if __name__=='__main__':run(ROWS)
