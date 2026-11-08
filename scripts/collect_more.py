from collect import get, ROOT
import concurrent.futures,json
ROWS=[
 ('falencia1901','https://www.gutenberg.org/ebooks/69229.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('intrusa1908','https://www.gutenberg.org/ebooks/67594.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('serras1901','https://www.gutenberg.org/ebooks/18220.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('ramires1900','https://www.gutenberg.org/ebooks/23145.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('humus1917','https://www.gutenberg.org/ebooks/39618.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('lucio1914','https://www.gutenberg.org/ebooks/68807.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('engomadeira1917','https://www.gutenberg.org/ebooks/23879.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('orpheu1915','https://www.gutenberg.org/ebooks/23620.txt.utf-8','txt','dominio-publico; observar cabecalho Gutenberg'),
 ('young2008','https://repositorio.ufc.br/bitstream/riufc/3309/1/2008_Dis_RSYOUNG.pdf','pdf','acesso-aberto; redistribuicao-nao-verificada'),
 ('kempe2025','https://rke.abertay.ac.uk/files/88146020/Kempe_NoEvidenceForGenerationalDifferences_Published_2025.pdf','pdf','licenca-a-conferir'),
 ('malho1920_914','https://hemeroteca-pdf.bn.gov.br/116300/per116300_1920_00914.pdf','pdf','Acervo Fundacao Biblioteca Nacional; texto historico'),
 ('malho1920_919','https://hemeroteca-pdf.bn.gov.br/116300/per116300_1920_00919.pdf','pdf','Acervo Fundacao Biblioteca Nacional; texto historico'),
 ('malho1920_943','https://hemeroteca-pdf.bn.gov.br/116300/per116300_1920_00943.pdf','pdf','Acervo Fundacao Biblioteca Nacional; texto historico'),
]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:r=list(ex.map(get,ROWS))
 p=ROOT/'data/downloads.json';old=json.loads(p.read_text(encoding='utf-8'));merged={x['id']:x for x in old}
 for x in r: merged[x['id']]=x; print(x['id'],x['status'],x.get('bytes',x.get('error')))
 p.write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2),encoding='utf-8')
