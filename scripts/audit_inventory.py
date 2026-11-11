"""Reconcilia registros públicos por identificador, sem inferir independência histórica."""
from pathlib import Path
import csv,json,collections
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'data'
def read(name):
 with (DATA/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
SETS=['attestations','archive_decade_references','revision4_new_titles','period_alternatives']
manifest={x['id']:x for x in json.loads((DATA/'downloads.json').read_text(encoding='utf-8'))}
register=[];per_set={}
for name in SETS:
 rows=read(name+'.csv')
 per_set[name]=dict(rows=len(rows),source_identifiers=len({x['source_id'] for x in rows}),bibliographic_keys=len({x['bib'] for x in rows}))
 for x in rows:
  assert x['source_id'] in manifest,x['source_id']
  m=manifest[x['source_id']]
  register.append(dict(dataset=name,record_id=x.get('id',x.get('work_key','')),source_id=x['source_id'],year=x.get('year',x.get('date',''))[:4],bib=x['bib'],url=m['url'],acquisition_status=m['status']))
with (DATA/'evidence_register.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(register[0]),lineterminator='\n');w.writeheader();w.writerows(register)
core=read('attestations.csv');refs=read('archive_decade_references.csv');matrix=read('archive_decade_matrix.csv')
ids={x['source_id'] for x in register}
summary=dict(datasets=per_set,combined_record_memberships=len(register),unique_selected_source_identifiers=len(ids),unique_selected_source_urls=len({x['url'] for x in register}),selected_source_acquisition_status=dict(collections.Counter(manifest[x]['status'] for x in ids)),core_representation_categories=dict(collections.Counter(x['representation'] for x in core)),core_countries=dict(collections.Counter(x['country'] for x in core)),archive_selection_categories=dict(collections.Counter(x['kind'] for x in refs)),archive_rows_with_reference=sum(bool(x['reference_id']) for x in matrix),archive_source_identifiers=len({x['source_id'] for x in refs}),identity_rule='source_id; URL identity checked; not a count of independent works, editions, witnesses or national usage',independence_not_inferred=True)
historical=[x for x in register if int(x['year'])<1900]
summary.update(earliest_selected_year=min(int(x['year']) for x in register),latest_selected_year=max(int(x['year']) for x in register),pre1900_record_memberships=len(historical),pre1900_source_identifiers=len({x['source_id'] for x in historical}),pre1900_continuous_annual_coverage_not_claimed=True)
(DATA/'consolidated_inventory.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(summary,ensure_ascii=False))

profiles=read('archive_profiles.csv');counts=[]
for profile in profiles:
 archive=profile['archive'];selected=[x for x in refs if x['archive']==archive];tracked=[x for x in matrix if x['archive']==archive]
 counts.append(dict(archive=archive,name=profile['name'],matrix_rows=len(tracked),reference_links=len(selected),source_identifiers=len({x['source_id'] for x in selected}),confirmed_in_indicated_archive=sum(bool(x['reference_id']) and x['status']!='confirmada em fonte alternativa' for x in tracked),confirmed_alternative=sum(x['status']=='confirmada em fonte alternativa' for x in tracked),reviewed_without_attestation=sum(x['status'].startswith('conferido: sem ocorrência localizada') for x in tracked),lexical=sum(x['kind']=='lexical' for x in selected),rubrica=sum(x['kind']=='rubrica' for x in selected),mimetica=sum(x['kind']=='mimética' for x in selected)))
with (DATA/'archive_selection_counts.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(counts[0]),lineterminator='\n');w.writeheader();w.writerows(counts)
assert sum(x['reference_links'] for x in counts)==len(refs)
assert sum(x['matrix_rows'] for x in counts)==len(matrix)
