"""Copia somente textos cuja publicação integral foi selecionada para o acervo público."""
from pathlib import Path
import json,shutil,hashlib
ROOT=Path(__file__).resolve().parents[1]
PUBLIC=ROOT/'sources/public';PUBLIC.mkdir(parents=True,exist_ok=True)
ids=['primo1878','policarpo1915','falencia1901','intrusa1908','serras1901','ramires1900','humus1917','lucio1914']
manifest=json.loads((ROOT/'data/downloads.json').read_text(encoding='utf-8'))
for r in manifest:
 r['public_copy']=False
 if r['id'] in ids and r['status']=='downloaded':
  src=ROOT/r['path'];dst=PUBLIC/src.name;shutil.copyfile(src,dst)
  assert hashlib.sha256(dst.read_bytes()).hexdigest()==r['sha256']
  r['public_copy']=True;r['public_path']=str(dst.relative_to(ROOT)).replace('\\','/')
(ROOT/'data/downloads.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('public_texts',sum(r['public_copy'] for r in manifest),'downloaded',sum(r['status']=='downloaded' for r in manifest),'failed',sum(r['status']=='failed' for r in manifest))
