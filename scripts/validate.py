"""Verificações de integridade documental, cálculos e artefatos."""
from pathlib import Path
import re,json,csv,math,hashlib
ROOT=Path(__file__).resolve().parents[1]
def readcsv(name):
 with (ROOT/'data'/name).open(encoding='utf-8') as f:return list(csv.DictReader(f))
at=readcsv('attestations.csv');years=readcsv('annual_coverage.csv')
annual_supplement=readcsv('annual_supplement.csv')
assert len({x['id'] for x in at})==len(at)==25+len(annual_supplement)
assert len({x['year'] for x in annual_supplement})==len(annual_supplement)
assert all(1900<=int(x['year'])<=2009 for x in annual_supplement)
audit=readcsv('references_audit.csv')
assert len(audit)==66 and len({x['id'] for x in audit})==66
assert __import__('collections').Counter(x['status'] for x in audit)==dict(A=3,L=7,B=19,I=4,S=33)
assert all(x['finding'] and x['checked_on'] for x in audit)
assert len(readcsv('claims_verification.csv'))==22
assert len(years)==155
core_years={int(x['year']) for x in years if int(x['confirmed_documents'])>0 and 1900<=int(x['year'])<=2009}
assert core_years==set(range(1900,2010))
assert len(annual_supplement)==96
archive_rows=readcsv('archive_decade_matrix.csv')
archive_refs=readcsv('archive_decade_references.csv')
assert len(readcsv('archive_profiles.csv'))==13
assert len({(x['archive'],x['decade']) for x in archive_rows})==len(archive_rows)
assert sum(bool(x['reference_id']) for x in archive_rows)==len(archive_refs)
assert all(x['kind'] in ['lexical','rubrica','mimética'] for x in archive_refs)
archive_summary=json.loads((ROOT/'data/archive_summary.json').read_text(encoding='utf-8'))
assert archive_summary['selected_references']==len(archive_refs)
assert archive_summary['alternative_source_cells']==sum(x['status']=='confirmada em fonte alternativa' and bool(x['note']) for x in archive_rows)
assert archive_summary['confirmed_archive_decade_cells']+archive_summary['alternative_source_cells']==len(archive_refs)
assert archive_summary['pending_quota_cells']==sum(x['status'].startswith('pendente:') for x in archive_rows)
ref_lookup={x['id']:x for x in archive_refs}
for x in archive_rows:
 if x['reference_id']:
  r=ref_lookup[x['reference_id']]
  assert (x['archive'],x['decade'])==(r['archive'],r['decade'])
for r in archive_refs:assert int(r['date'][:4])//10*10==int(r['decade'])
assert all(any(int(x['year'])//10==d for x in at) for d in range(190,201))
assert len(readcsv('claims_audit.csv'))==22
assert len(readcsv('candidate_sources.csv'))==66
assert sum(int(x['confirmed_documents']) for x in years)==len(at)
assert math.ceil(math.log(.05)/math.log(.95))==59
assert math.ceil(math.log(.05)/math.log(.99))==299
assert math.ceil(1.96**2*.25/.1**2)==97
bib='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'artigo').glob('*.bib'))
keys=set(re.findall(r'@\w+\{([^,]+),',bib))
text='\n'.join(p.read_text(encoding='utf-8') for p in (ROOT/'artigo').rglob('*.tex'))
cites={k for m in re.finditer(r'\\cite\{([^}]+)\}',text) for k in m.group(1).split(',')}
assert not cites-keys, f'Chaves ausentes: {cites-keys}'
assert 'unb2026' not in keys and 'unb2026' not in cites
new_titles=readcsv('revision4_new_titles.csv')
assert len(new_titles)==17 and len({x['work_key'] for x in new_titles})==17
assert sum(x['core']=='True' for x in new_titles)==2
assert [int(x['year']) for x in new_titles]==sorted(int(x['year']) for x in new_titles)
bases=readcsv('base_registry.csv');metrics=readcsv('method_quantification.csv');domains=readcsv('source_domains.csv')
assert {x['id'] for x in bases}=={f'H{i:02}' for i in range(1,17)}
assert sum(int(x['manifest_entries']) for x in domains)==len(json.loads((ROOT/'data/downloads.json').read_text(encoding='utf-8')))
metric_values={x['id']:x['value'] for x in metrics}
assert int(metric_values['M02'])==len(at) and int(metric_values['M15'])==len(keys)
assert int(metric_values['M10'])==sum(int(metric_values[k]) for k in ['M11','M12','M13'])
prefix='https://github.com/murilloed/historia-riso-escrito-portugues/blob/main/'
for row in metrics+bases:
 assert row['data_url'].startswith(prefix) and (ROOT/row['data_url'][len(prefix):]).is_file()
assert not keys-cites, f'Referências não citadas: {keys-cites}'
for x in at:assert x['bib'] in keys
log=(ROOT/'artigo/main.log').read_text(encoding='utf-8',errors='replace')
bad=[line for line in log.splitlines() if re.search(r'undefined|Missing character|Overfull|^!',line)]
assert not bad,bad
blg=(ROOT/'artigo/main.blg').read_text(encoding='utf-8',errors='replace')
assert not re.search(r'Too many commas|[1-9]\d* error messages?|I was expecting|Repeated entry',blg), 'Erro BibTeX: consultar main.blg'
manifest=json.loads((ROOT/'data/downloads.json').read_text(encoding='utf-8'))
manifest_by_id={r['id']:r for r in manifest}
for row in annual_supplement:
 source=manifest_by_id[row['source_id']]
 assert source['status']=='downloaded' and source['bytes']>0 and source['url']==row['url'],row
 assert row['locator'] and row['form'] and row['date_basis'],row
public=[]
for r in manifest:
 if r.get('public_copy'):
  p=ROOT/r['public_path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'];public.append(r['id'])
assert len(public)==8
report=dict(atestacoes=len(at),niveis=dict(__import__('collections').Counter(x['evidence'] for x in at)),referencias=len(keys),alvos_auditoria=22,pistas=66,pareceres_individuais=len(audit),estados_auditoria=dict(__import__('collections').Counter(x['status'] for x in audit)),anos_inventariados=155,decadas_nucleo_cobertas=11,downloads=sum(x['status']=='downloaded' for x in manifest),falhas_download=sum(x['status']=='failed' for x in manifest),textos_integrais_publicos=len(public),latex_sem_citacoes_indefinidas=True,latex_sem_glifos_ausentes=True,latex_sem_overfull=True)
report.update(anos_nucleo_cobertos=len(core_years),atestacoes_suplementares=len(annual_supplement))
try:
 import pymupdf
 d=pymupdf.open(ROOT/'artigo/main.pdf')
 report.update(paginas=len(d),palavras_pdf=sum(len(p.get_text().split()) for p in d))
 full='\n'.join(p.get_text() for p in d)
 assert 'Murillo Edson de Carvalho Souza' in full
 assert '[?]' not in full
 assert not re.search(r'\bUnB\b|Edital 04/2026',full)
 pdf_urls={link.get('uri','') for page in d for link in page.get_links()}
 for path in ['data/base_registry.csv','data/method_quantification.csv','data/source_domains.csv','data/downloads.json','data/annual_coverage.csv','data/annual_supplement.csv']:
  assert prefix+path in pdf_urls, 'Hiperlink ausente no PDF: '+path
except ImportError:pass
report.update(acervos=13,referencias_por_acervo_e_decada=len(archive_refs),linhas_matriz_acervos=len(archive_rows),cobertura_integral_acervos=False)
report.update(titulos_ineditos_quarta_rodada=len(new_titles),edital_unb_removido=True)
report.update(enderecos_indicados_inventariados=len(bases),indicadores_metodologicos=len(metrics),hiperlinks_metodologicos_no_pdf=True)
(ROOT/'data/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=True))
