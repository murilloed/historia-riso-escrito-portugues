from pathlib import Path
import re,csv,json,hashlib,os
from build_data import ROOT,GEN,DATA,tex
import revision2_audit
attachment=Path(os.environ['RISO_ROTEIRO_PATH']) if os.environ.get('RISO_ROTEIRO_PATH') else None
if attachment is not None and attachment.is_file():
 text=attachment.read_text(encoding='utf-8')
 block=text.split('quero para cada epoca que analisou',1)[1].split('Com todo esse aparato',1)[0]
 rows=[];decade=None;kind=None
 for line in block.splitlines():
  m=re.match(r'Década de (\d{4})',line.strip())
  if m:decade=int(m.group(1))
  if 'Jornais da Época:' in line or 'Jornais / Revistas da Época:' in line:kind='periódico'
  if 'Livros / Obras:' in line:kind='obra'
  if re.match(r'\s*\d+\.',line) and decade:
   desc=re.sub(r'^\s*\d+\.\s*','',line).strip()
   rows.append(dict(claimed_decade=decade,type=kind,description_from_input=desc,status='pista bibliográfica; ocorrência e data precisam de validação'))
 with (DATA/'candidate_sources.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
else:
 with (DATA/'candidate_sources.csv').open(encoding='utf-8') as f:rows=list(csv.DictReader(f))
body=[r'\small\begin{longtable}{p{0.09\textwidth}p{0.13\textwidth}p{0.66\textwidth}}',r'\caption{Pistas herdadas do roteiro, conservadas para auditoria. Descrições não constituem resultados verificados.}\\',r'\toprule Década alegada & Tipo & Descrição herdada (a verificar) \\\midrule\endfirsthead',r'\toprule Década alegada & Tipo & Descrição herdada (a verificar) \\\midrule\endhead']
for r in rows:
 body.append(str(r['claimed_decade'])+' & '+tex(r['type'])+' & '+tex(r['description_from_input'])+' '+r'\\')
body += [r'\bottomrule\end{longtable}\normalsize']
(GEN/'candidates-table.tex').write_text('\n'.join(body),encoding='utf-8')
with (DATA/'annual_coverage.csv').open(encoding='utf-8') as f:years=list(csv.DictReader(f))
body=[r'\small\begin{longtable}{rrp{0.65\textwidth}}',r'\caption{Cobertura anual do núcleo 1900--2009. Não é série de prevalência.}\\',r'\toprule Ano & Documentos & Interpretação \\\midrule\endfirsthead',r'\toprule Ano & Documentos & Interpretação \\\midrule\endhead']
for r in years:
 if 1900<=int(r['year'])<=2009:
  n=int(r['confirmed_documents'])
  body.append(r['year']+' & '+(str(n) if n else '--')+' & '+('Atestação confirmada; ver tabela documental.' if n else 'Sem atestação confirmada nesta coleta.')+' '+r'\\')
body += [r'\bottomrule\end{longtable}\normalsize']
(GEN/'annual-table.tex').write_text('\n'.join(body),encoding='utf-8')
print('candidate_sources',len(rows))
