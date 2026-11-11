"""Descriptive inventory and exploratory graphic clustering; no historical genealogy."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
from pathlib import Path
import csv, json, re, unicodedata, hashlib, platform, importlib.metadata
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.cluster.hierarchy import linkage, cut_tree, dendrogram
from scipy.spatial.distance import squareform
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score, adjusted_rand_score
from threadpoolctl import threadpool_limits

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; FIG=ROOT/'artigo/figures'; FIG.mkdir(exist_ok=True)
OUT=DATA/'analysis'; OUT.mkdir(exist_ok=True)
with (DATA/'attestations.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))

def writecsv(name, records):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]),lineterminator='\n');w.writeheader();w.writerows(records)

def normalize(s):
    return ''.join(c for c in unicodedata.normalize('NFKD',s.casefold()) if c.isalpha())

def edit(a,b):
    prev=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        curr=[i]
        for j,cb in enumerate(b,1):curr.append(min(curr[-1]+1,prev[j]+1,prev[j-1]+(ca!=cb)))
        prev=curr
    return prev[-1]/max(len(a),len(b))

def labels_at(z,k): return cut_tree(z,n_clusters=[k]).ravel()

variants=[]
for r in rows:
    if r['representation']=='rubrica descritiva':continue
    for i,v in enumerate(r['form'].split('/'),1):
        variants.append(dict(record_id=r['id'],source_id=r['source_id'],bib=r['bib'],year=r['year'],variant_index=i,original_form=v.strip(),normalized=normalize(v)))
forms=sorted({v['normalized'] for v in variants}); n=len(forms)
assert len(rows)==121 and len(variants)==26 and n==16
D=np.array([[edit(a,b) for b in forms] for a in forms])
assert np.allclose(D,D.T) and np.allclose(np.diag(D),0) and np.isfinite(D).all()
z=linkage(squareform(D),method='average',optimal_ordering=True)
z_complete=linkage(squareform(D),method='complete',optimal_ordering=True)
vectorizer=TfidfVectorizer(analyzer='char',ngram_range=(1,3),norm='l2',lowercase=False,use_idf=True,smooth_idf=True,sublinear_tf=False)
X=vectorizer.fit_transform(forms)
X_alt=TfidfVectorizer(analyzer='char',ngram_range=(1,2),norm='l2',lowercase=False).fit_transform(forms)
scores=[]; h_labels={}; k_labels={}; stable={}
with threadpool_limits(limits=1):
    for k in range(2,7):
        h=labels_at(z,k); h_labels[k]=h
        km=KMeans(n_clusters=k,n_init=50,random_state=0,max_iter=300,init='k-means++',algorithm='lloyd',tol=1e-4).fit(X)
        kl=km.labels_; k_labels[k]=kl
        trials=[adjusted_rand_score(kl,KMeans(n_clusters=k,n_init=1,random_state=s,max_iter=300,init='k-means++',algorithm='lloyd',tol=1e-4).fit_predict(X)) for s in range(20)]
        alt=KMeans(n_clusters=k,n_init=50,random_state=0,max_iter=300,init='k-means++',algorithm='lloyd',tol=1e-4).fit_predict(X_alt)
        scores.append(dict(k=k,hierarchical_silhouette_edit=float(silhouette_score(D,h,metric='precomputed')),kmeans_silhouette_cosine=float(silhouette_score(X,kl,metric='cosine')),kmeans_inertia=float(km.inertia_),kmeans_seed_ari_min=float(min(trials)),kmeans_seed_ari_median=float(np.median(trials)),kmeans_ngram_sensitivity_ari=float(adjusted_rand_score(kl,alt)),hierarchical_linkage_sensitivity_ari=float(adjusted_rand_score(h,labels_at(z_complete,k))),agreement_between_methods_ari=float(adjusted_rand_score(h,kl))))
        stable[k]=trials
best_h=max(scores,key=lambda v:(v['hierarchical_silhouette_edit'],-v['k']))['k']
best_k=max(scores,key=lambda v:(v['kmeans_silhouette_cosine'],-v['k']))['k']
units=[]
for i,form in enumerate(forms):
    linked=[v for v in variants if v['normalized']==form]
    units.append(dict(form_id=f'F{i+1:02}',normalized=form,record_links=len(linked),distinct_source_ids=len({v['source_id'] for v in linked}),first_selected_year=min(int(v['year']) for v in linked),last_selected_year=max(int(v['year']) for v in linked),hierarchical_cluster=int(h_labels[best_h][i])+1,kmeans_cluster=int(k_labels[best_k][i])+1))
by_form={u['normalized']:u for u in units}
for v in variants:v['form_id']=by_form[v['normalized']]['form_id']
writecsv('initialization_sensitivity.csv',[dict(k=k,seed=seed,ari_reference=value) for k,values in stable.items() for seed,value in enumerate(values)])
writecsv('partition_grid.csv',[dict(form_id=units[i]['form_id'],k=k,hierarchical_cluster=int(h_labels[k][i])+1,kmeans_cluster=int(k_labels[k][i])+1) for k in range(2,7) for i in range(n)])
writecsv('form_variants.csv',variants);writecsv('form_units.csv',units);writecsv('cluster_diagnostics.csv',scores)
writecsv('normalized_edit_distances.csv',[dict(form_id=units[i]['form_id'],**{units[j]['form_id']:float(D[i,j]) for j in range(n)}) for i in range(n)])
writecsv('tfidf_features.csv',[dict(form_id=u['form_id'],**{f'ngram:{term}':float(X[i,j]) for j,term in enumerate(vectorizer.get_feature_names_out())}) for i,u in enumerate(units)])
decades=list(range(1870,2030,10)); temporal=[]
for d in decades:
    group=[r for r in rows if int(r['year'])//10*10==d]
    temporal.append(dict(decade=d,records=len(group),rubrics=sum(r['representation']=='rubrica descritiva' for r in group),mimetic_or_digital=sum(r['representation']!='rubrica descritiva' for r in group)))
writecsv('core_by_decade.csv',temporal)
with (DATA/'evidence_register.csv').open(encoding='utf-8',newline='') as f: memberships=list(csv.DictReader(f))
selected_sources={}
for item in memberships:
    if item['source_id'] in selected_sources:assert selected_sources[item['source_id']]==int(item['year'])
    selected_sources[item['source_id']]=int(item['year'])
all_decades=range(min(selected_sources.values())//10*10,max(selected_sources.values())//10*10+1,10)
all_temporal=[dict(decade=d,source_identifiers=sum(y//10*10==d for y in selected_sources.values())) for d in all_decades]
writecsv('selected_sources_by_decade.csv',all_temporal)
summary=dict(scope='exploratory; graphic resemblance, not transmission, prevalence or phonetic distance',all_inventory_source_identifiers=len(selected_sources),all_inventory_earliest_year=min(selected_sources.values()),all_inventory_latest_year=max(selected_sources.values()),input_records=len(rows),rubrics=96,mimetic_digital_records=25,variant_links=len(variants),unique_normalized_forms=n,cluster_unit='distinct normalized graphic sequence; equal weight',normalization='casefold, Unicode NFKD, retain letters only; split slash-separated variants',excluded_features=['year','country','medium','evidence','representation label','archive'],k_range=list(range(2,7)),hierarchical=dict(distance='Levenshtein/max(lengths)',linkage='average',selected_k=best_h,selected_silhouette=next(s['hierarchical_silhouette_edit'] for s in scores if s['k']==best_h)),kmeans=dict(features='character TF-IDF 1–3 grams, L2',metric_for_silhouette='cosine; optimization uses squared Euclidean distance',selected_k=best_k,selected_silhouette=next(s['kmeans_silhouette_cosine'] for s in scores if s['k']==best_k),random_state=0,n_init=50,max_iter=300,init='k-means++',algorithm='lloyd',tol=1e-4,stability_seeds=list(range(20)),stability_n_init=1),selected_partitions_ari=float(adjusted_rand_score(h_labels[best_h],k_labels[best_k])),comparability_note='Silhouettes use distinct representations/distances; do not rank methods by their raw values.',seed_stability_note='Initialization sensitivity only; not population uncertainty or out-of-sample validation.',no_supervised_training=True,input_sha256=hashlib.sha256((DATA/'attestations.csv').read_bytes()).hexdigest(),packages={name:importlib.metadata.version(name) for name in ['numpy','scipy','scikit-learn','matplotlib','threadpoolctl']},python=platform.python_version())
(OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.bbox':'tight'})
BLUE='#285f86';ORANGE='#bd5b2a';GREEN='#47795b';GRAY='#606b78'
def save(fig,name):
    fig.savefig(FIG/(name+'.pdf'));fig.savefig(FIG/(name+'.png'),dpi=180);plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
for ax,labels,values,colors,title in [(axes[0],['Rubricas','Miméticas / digitais'],[96,25],[BLUE,ORANGE],'Núcleo: 121 registros'),(axes[1],['Lexicais','Rubricas','Miméticas'],[112,18,5],[GRAY,BLUE,ORANGE],'Seleção por quota: 135 vínculos')]:
    bars=ax.barh(labels,values,color=colors);ax.invert_yaxis();ax.bar_label(bars,padding=4);ax.set_xlim(0,max(values)*1.2);ax.set_title(title);ax.set_xlabel('Contagem no inventário selecionado')
save(fig,'analysis_composition')
fig,ax=plt.subplots(figsize=(10,4),layout='constrained');xx=np.arange(len(temporal));rr=[x['rubrics'] for x in temporal];mm=[x['mimetic_or_digital'] for x in temporal]
ax.bar(xx,rr,color=BLUE,label='Rubricas');ax.bar(xx,mm,bottom=rr,color=ORANGE,label='Miméticas / digitais');ax.set_xticks(xx,[str(d) for d in decades],rotation=45);ax.set_ylabel('Registros selecionados');ax.set_xlabel('Década do registro (sem interpolação de lacunas)');ax.set_title('Composição temporal do núcleo: perfil da coleta, não prevalência');ax.legend(frameon=False);save(fig,'analysis_decades')
fig,ax=plt.subplots(figsize=(11,4),layout='constrained')
xx=np.arange(len(all_temporal));ax.bar(xx,[x['source_identifiers'] for x in all_temporal],color=GREEN)
ax.set_xticks(xx,[str(x['decade']) for x in all_temporal],rotation=90,fontsize=8)
ax.set_xlabel('Década da data atribuída à fonte (1645–2025)');ax.set_ylabel('Identificadores de fonte distintos')
ax.set_title('Quatro inventários: 258 fontes por identificador, sem somar vínculos repetidos');ax.yaxis.set_major_locator(MaxNLocator(integer=True))
save(fig,'analysis_all_decades')
fig,ax=plt.subplots(figsize=(10,6),layout='constrained');dendrogram(z,labels=[u['form_id']+'  '+u['normalized'] for u in units],orientation='right',leaf_font_size=10,color_threshold=0,above_threshold_color=BLUE,ax=ax);ax.set_xlabel('Distância média de edição normalizada');ax.set_title('Semelhança gráfica de 16 formas distintas — não é árvore genealógica');save(fig,'analysis_dendrogram')
fig,axes=plt.subplots(1,3,figsize=(12,3.8),layout='constrained')
axes[0].plot([s['k'] for s in scores],[s['hierarchical_silhouette_edit'] for s in scores],'-o',color=BLUE)
axes[0].set_title('Hierárquico: distância de edição');axes[0].set_ylabel('Silhueta');axes[0].set_xlabel('Número de grupos');axes[0].set_xticks(range(2,7))
axes[1].plot([s['k'] for s in scores],[s['kmeans_silhouette_cosine'] for s in scores],'-s',color=ORANGE)
axes[1].set_title('K-means: cosseno em TF-IDF');axes[1].set_xlabel('Número de grupos');axes[1].set_xticks(range(2,7))
axes[2].boxplot([stable[k] for k in range(2,7)],tick_labels=list(range(2,7)));axes[2].set_xlabel('Número de grupos no K-means');axes[2].set_ylabel('ARI contra referência (50 reinícios)');axes[2].set_title('20 inicializações isoladas')
save(fig,'analysis_diagnostics')
fig,ax=plt.subplots(figsize=(8,7),layout='constrained');order=dendrogram(z,no_plot=True)['leaves'];im=ax.imshow(D[np.ix_(order,order)],cmap='Blues',vmin=0,vmax=1);labels=[units[i]['form_id'] for i in order];ax.set_xticks(range(n),labels,rotation=90);ax.set_yticks(range(n),[units[i]['form_id']+' '+forms[i] for i in order]);fig.colorbar(im,ax=ax,label='Edição normalizada (0: identidade)');ax.set_title('Distâncias gráficas; ordem derivada do agrupamento');save(fig,'analysis_distances')

def pt(v):return f'{v:.3f}'.replace('.',',')
bs=chr(92)
tex=bs+'newcommand{'+bs+'AnalysisForms}{'+str(n)+'}\n'+bs+'newcommand{'+bs+'AnalysisVariants}{'+str(len(variants))+'}\n'
tex+=bs+'newcommand{'+bs+'HierK}{'+str(best_h)+'}\n'+bs+'newcommand{'+bs+'KmeansK}{'+str(best_k)+'}\n'
tex+=bs+'newcommand{'+bs+'HierSil}{'+pt(summary['hierarchical']['selected_silhouette'])+'}\n'+bs+'newcommand{'+bs+'KmeansSil}{'+pt(summary['kmeans']['selected_silhouette'])+'}\n'+bs+'newcommand{'+bs+'MethodsARI}{'+pt(summary['selected_partitions_ari'])+'}\n'
(ROOT/'artigo/generated/analysis_counts.tex').write_text(tex,encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False))

# Tabela interpretável: datas apenas como metadados, nunca como entrada do agrupamento.
table=[r'\small\begin{longtable}{lp{.32\textwidth}rrl}',r'\caption{Formas normalizadas distintas e partições exploratórias. H: hierárquico com quatro grupos; K: K-means com seis. Datas são extremos selecionados, não origem ou duração de uso.}\label{tab:form-clusters}\\',r'\toprule ID & Sequência & H & K & Datas selecionadas \\ \midrule\endfirsthead',r'\toprule ID & Sequência & H & K & Datas selecionadas \\ \midrule\endhead']
for u in units:
 table.append(u['form_id']+' & '+r'\texttt{'+u['normalized']+'} & '+str(u['hierarchical_cluster'])+' & '+str(u['kmeans_cluster'])+' & '+str(u['first_selected_year'])+'--'+str(u['last_selected_year'])+r' \\')
table.append(r'\bottomrule\end{longtable}\normalsize')
(ROOT/'artigo/generated/form_clusters.tex').write_text('\n'.join(table)+'\n',encoding='utf-8')
