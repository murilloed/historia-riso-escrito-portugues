from collect import get, ROOT
import concurrent.futures,json
ROWS=[
 ('ticotico1935','https://hemeroteca-pdf.bn.gov.br/153079/per153079_1935_01569.pdf','pdf','Acervo Fundacao Biblioteca Nacional; direitos de terceiros'),
 ('momento1953','https://hemeroteca-pdf.bn.gov.br/118699/per118699_1948_00593.pdf','pdf','Acervo Fundacao Biblioteca Nacional; direitos de terceiros'),
 ('riounu1910','https://hemeroteca-pdf.bn.gov.br/706736/per706736_1910_01275.pdf','pdf','Acervo Fundacao Biblioteca Nacional; texto historico'),
 ('noticias1946','https://hemeroteca-pdf.bn.gov.br/583138/per583138_1946_00177.pdf','pdf','Acervo Fundacao Biblioteca Nacional; direitos de terceiros'),
 ('intervalo1965','https://hemeroteca-pdf.bn.gov.br/109835/per109835_1965_00128.pdf','pdf','Acervo Fundacao Biblioteca Nacional; direitos de terceiros'),
 ('lopesduarte','https://laborhistorico.letras.ufrj.br/producao/Lopes%20%26%20Duarte%20PHPB.pdf','pdf','acesso-aberto; redistribuicao-nao-verificada'),
]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:r=list(ex.map(get,ROWS))
 p=ROOT/'data/downloads.json';old=json.loads(p.read_text(encoding='utf-8'));merged={x['id']:x for x in old}
 for x in r: merged[x['id']]=x; print(x['id'],x['status'],x.get('bytes',x.get('error')))
 p.write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2),encoding='utf-8')
