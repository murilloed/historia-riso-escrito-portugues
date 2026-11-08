from revision2_download import run
ROWS=[
('r3_cepe_risos_xix','http://200.238.101.22/docreader/docreader.aspx?bib=SECXIX&pesq=risos','html','busca pública no acervo'),
('r3_cepe_risos1927','http://200.238.101.22/docreader/docreader.aspx?bib=DM1927&pesq=risos','html','busca pública no acervo'),
('r3_cepe_risos1986','http://200.238.101.22/docreader/docreader.aspx?bib=SPFULL&pesq=risos','html','busca pública no acervo'),
('r3_cepe_lib','http://200.238.101.22/docreader/lib/DocReader.js','js','código público do leitor; apenas inspeção dos meios de consulta'),
('r3_bore_risos','https://obrasraras.usp.br/xmlui/handle/123456789/4262/discover?query=risos','html','busca pública no repositório'),
('r3_apesp_risos','https://atom.arquivoestado.sp.gov.br/informationobject/browse?query=risos&topLod=0','html','busca pública no catálogo'),
('r3_apesp_item_search','https://atom.arquivoestado.sp.gov.br/informationobject/browse?query=b000565&topLod=0','html','busca por identificador informado'),
]
if __name__=='__main__':run(ROWS)
