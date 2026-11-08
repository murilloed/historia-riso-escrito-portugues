from collect import get,ROOT
import json,concurrent.futures
ROWS=[
('portugal1925','https://debates.parlamento.pt/catalogo/r1/cd/01/06/04/077/1925-06-11?sft=true','html','registro parlamentar público; transcrição automática'),
('folha1994','https://www1.folha.uol.com.br/fsp/1994/9/03/caderno_especial/2.html','html','copyright Folha; metadados e citação curta; íntegra apenas local'),
]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:r=list(ex.map(get,ROWS))
 p=ROOT/'data/downloads.json';merged={x['id']:x for x in json.loads(p.read_text(encoding='utf-8'))}
 for x in r:merged[x['id']]=x;print(x['id'],x['status'])
 p.write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2),encoding='utf-8')
