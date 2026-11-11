"""Check exported analysis against source membership, distances and diagnostics."""
from pathlib import Path
import csv, json, hashlib, math
from collections import Counter
import numpy as np
from sklearn.metrics import silhouette_score, adjusted_rand_score

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'data/analysis'
def read(path):
    with path.open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
s=json.loads((OUT/'summary.json').read_text(encoding='utf-8'))
core=read(ROOT/'data/attestations.csv');units=read(OUT/'form_units.csv');variants=read(OUT/'form_variants.csv')
eligible={x['id']:x for x in core if x['representation']!='rubrica descritiva'}
assert s['input_sha256']==hashlib.sha256((ROOT/'data/attestations.csv').read_bytes()).hexdigest()
assert len(core)==s['input_records']==121
assert len(eligible)==s['mimetic_digital_records']==25
assert len(variants)==s['variant_links']==26
assert len(units)==s['unique_normalized_forms']==16
assert {v['record_id'] for v in variants}==set(eligible)
for v in variants:
    r=eligible[v['record_id']]
    assert v['original_form'] in [z.strip() for z in r['form'].split('/')]
    assert v['source_id']==r['source_id'] and v['year']==r['year']
assert sum(int(u['record_links']) for u in units)==len(variants)
assert len({u['normalized'] for u in units})==len(units)
dist=read(OUT/'normalized_edit_distances.csv')
D=np.array([[float(row[u['form_id']]) for u in units] for row in dist])
assert np.isfinite(D).all() and np.all((0<=D)&(D<=1))
assert np.allclose(D,D.T) and np.allclose(D.diagonal(),0)
lookup={u['normalized']:i for i,u in enumerate(units)}
assert math.isclose(D[lookup['kkkk'],lookup['kkkkkkkk']],0.5)
assert math.isclose(D[lookup['quiaquiaquia'],lookup['quaquaqua']],0.25)
h=np.array([int(u['hierarchical_cluster']) for u in units]);k=np.array([int(u['kmeans_cluster']) for u in units])
assert len(set(h))==s['hierarchical']['selected_k']
assert len(set(k))==s['kmeans']['selected_k']
assert math.isclose(silhouette_score(D,h,metric='precomputed'),s['hierarchical']['selected_silhouette'],abs_tol=1e-10)
features=read(OUT/'tfidf_features.csv');cols=[x for x in features[0] if x!='form_id']
assert all(x.startswith('ngram:') for x in cols)
X=np.array([[float(row[c]) for c in cols] for row in features])
assert np.allclose(np.linalg.norm(X,axis=1),1)
assert math.isclose(silhouette_score(X,k,metric='cosine'),s['kmeans']['selected_silhouette'],abs_tol=1e-10)
assert math.isclose(adjusted_rand_score(h,k),s['selected_partitions_ari'],abs_tol=1e-10)
diag=read(OUT/'cluster_diagnostics.csv')
assert [int(x['k']) for x in diag]==s['k_range']==list(range(2,7))
for method,col in [('hierarchical','hierarchical_silhouette_edit'),('kmeans','kmeans_silhouette_cosine')]:
    best=max(diag,key=lambda x:(float(x[col]),-int(x['k'])))
    assert int(best['k'])==s[method]['selected_k']
for r in diag:
    assert float(r['kmeans_seed_ari_min'])<=float(r['kmeans_seed_ari_median'])<=1
temporal=read(OUT/'core_by_decade.csv')
assert sum(int(x['records']) for x in temporal)==len(core)
assert sum(int(x['rubrics']) for x in temporal)==96
assert sum(int(x['mimetic_or_digital']) for x in temporal)==25
source_temporal=read(OUT/'selected_sources_by_decade.csv')
assert sum(int(x['source_identifiers']) for x in source_temporal)==s['all_inventory_source_identifiers']==258
assert s['all_inventory_earliest_year']==1645 and s['all_inventory_latest_year']==2025
assert s['no_supervised_training'] is True
for name in ['composition','decades','all_decades','dendrogram','diagnostics','distances']:
    for ext in ['png','pdf']:
        p=ROOT/f'artigo/figures/analysis_{name}.{ext}'
        assert p.is_file() and p.stat().st_size>1000
report=dict(core_records=len(core),eligible_records=len(eligible),variant_links=len(variants),normalized_forms=len(units),hierarchical_k=len(set(h)),kmeans_k=len(set(k)),distance_checks=True,metric_recalculation=True,temporal_totals=True,figures=6,input_hash_verified=True)
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report))
