from collect import get,ROOT
import json,concurrent.futures
ROWS=[
('carioca1941','https://hemeroteca-pdf.bn.gov.br/093092/per093092_1941_03902.pdf','pdf','Acervo Fundacao Biblioteca Nacional; direitos de terceiros'),
('correio1979','https://hemeroteca.ciasc.sc.gov.br/correiodopovo/1979/CDP19793035.pdf','pdf','Acervo Hemeroteca Digital Catarinense; direitos de terceiros'),
]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(get,ROWS))
 p=ROOT/'data/downloads.json';merged={x['id']:x for x in json.loads(p.read_text(encoding='utf-8'))}
 for x in r:merged[x['id']]=x;print(x['id'],x['status'])
 p.write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2),encoding='utf-8')
