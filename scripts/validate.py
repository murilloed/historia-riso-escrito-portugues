"""Verificações de integridade documental, cálculos e artefatos."""
from pathlib import Path
import re,json,csv,math,hashlib
ROOT=Path(__file__).resolve().parents[1]
def readcsv(name):
 with (ROOT/'data'/name).open(encoding='utf-8') as f:return list(csv.DictReader(f))
at=readcsv('attestations.csv');years=readcsv('annual_coverage.csv')
assert len({x['id'] for x in at})==len(at)==15
assert len(years)==155
assert all(any(int(x['year'])//10==d for x in at) for d in range(190,201))
assert len(readcsv('claims_audit.csv'))==22
assert len(readcsv('candidate_sources.csv'))==66
assert sum(int(x['confirmed_documents']) for x in years)==len(at)
assert math.ceil(math.log(.05)/math.log(.95))==59
assert math.ceil(math.log(.05)/math.log(.99))==299
assert math.ceil(1.96**2*.25/.1**2)==97
bib=(ROOT/'artigo/references.bib').read_text(encoding='utf-8')
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
text='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'artigo').rglob('*.tex'))
cites={k for m in re.finditer(r'\\cite\{([^}]+)\}',text) for k in m.group(1).split(',')}
assert not cites-keys, f'Chaves ausentes: {cites-keys}'
assert not keys-cites, f'Referências não citadas: {keys-cites}'
for x in at:assert x['bib'] in keys
log=(ROOT/'artigo/main.log').read_text(encoding='utf-8',errors='replace')
bad=[line for line in log.splitlines() if re.search(r'undefined|Missing character|Overfull|^!',line)]
assert not bad,bad
manifest=json.loads((ROOT/'data/downloads.json').read_text(encoding='utf-8'))
public=[]
for r in manifest:
 if r.get('public_copy'):
  p=ROOT/r['public_path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'];public.append(r['id'])
assert len(public)==8
report=dict(atestacoes=len(at),niveis=dict(__import__('collections').Counter(x['evidence'] for x in at)),referencias=len(keys),alvos_auditoria=22,pistas=66,anos_inventariados=155,decadas_nucleo_cobertas=11,downloads=sum(x['status']=='downloaded' for x in manifest),falhas_download=sum(x['status']=='failed' for x in manifest),textos_integrais_publicos=len(public),latex_sem_citacoes_indefinidas=True,latex_sem_glifos_ausentes=True,latex_sem_overfull=True)
try:
 import pymupdf
 d=pymupdf.open(ROOT/'artigo/main.pdf')
 report.update(paginas=len(d),palavras_pdf=sum(len(p.get_text().split()) for p in d))
 full='\n'.join(p.get_text() for p in d)
 assert 'Murillo Edson de Carvalho Souza' in full
 assert '[?]' not in full
except ImportError:pass
(ROOT/'data/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
