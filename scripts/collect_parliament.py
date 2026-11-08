from collect import get,ROOT
import concurrent.futures,json
ROWS=[
('camara1955','https://imagem.camara.leg.br/Imagem/d/pdf/DCD10DEZ1955SUP.pdf','pdf','documento parlamentar público; conferir direitos de material inserido'),
('senado1965','https://www.senado.leg.br/publicacoes/anais/pdf-digitalizado/Anais_Republica/1965/1965%20Livro%201.pdf','pdf','documento parlamentar público; conferir direitos de material inserido'),
('camara1985','https://imagem.camara.leg.br/Imagem/d/pdf/DCD29MAR1985.pdf','pdf','documento parlamentar público; conferir direitos de material inserido'),
]
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:r=list(ex.map(get,ROWS))
 p=ROOT/'data/downloads.json';merged={x['id']:x for x in json.loads(p.read_text(encoding='utf-8'))}
 for x in r:merged[x['id']]=x;print(x['id'],x['status'],x.get('bytes'))
 p.write_text(json.dumps(list(merged.values()),ensure_ascii=False,indent=2),encoding='utf-8')
