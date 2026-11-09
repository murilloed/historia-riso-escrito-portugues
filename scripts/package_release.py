"""Empacota exclusivamente o projeto LaTeX e os dados públicos."""
from pathlib import Path
import zipfile,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'dist';out.mkdir(exist_ok=True)
sourcezip=out/'artigo-overleaf.zip'
with zipfile.ZipFile(sourcezip,'w',zipfile.ZIP_DEFLATED) as z:
 for p in (ROOT/'artigo').rglob('*'):
  if p.is_file() and (p.suffix in ['.tex','.bib']):z.write(p,p.relative_to(ROOT/'artigo'))
 z.writestr('LEIA-ME.txt','Autor único: Murillo Edson de Carvalho Souza.\nSelecione main.tex e pdfLaTeX no Overleaf.\nRepositório: https://github.com/murilloed/historia-riso-escrito-portugues\nAs tabelas geradas estão incluídas. Não é necessário executar Python para compilar.\n')
hashes={}
for p in [ROOT/'artigo/main.pdf',sourcezip,ROOT/'artigo/main.tex',ROOT/'artigo/references.bib',ROOT/'artigo/annual.bib']:
 hashes[str(p.relative_to(ROOT)).replace('\\','/')]=hashlib.sha256(p.read_bytes()).hexdigest()
(out/'SHA256.json').write_text(json.dumps(hashes,indent=2),encoding='utf-8')
print('Overleaf files:',len(zipfile.ZipFile(sourcezip).namelist()))
