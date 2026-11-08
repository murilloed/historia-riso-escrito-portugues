from revision3_docvirt import read,ROOT,LOCAL
import json,re,concurrent.futures
def flatten(items,path=''):
 out=[]
 for row in items:
  name=path+'\\'+row['Name'];out.append(dict(row,path=name));out.extend(flatten(row.get('SubFolders') or [],name))
 return out
def main():
 raw=read('https://api.docvirt.com/v1/folders/dvd_ajhpmj');(LOCAL/'r3_docvirt_folders.json').write_bytes(raw)
 body=json.loads(raw);folders=flatten(json.loads(body['data']) if isinstance(body['data'],str) else body['data'])
 (ROOT/'data/revision3_docvirt_folders.json').write_text(json.dumps([dict(id=x['Id'],path=x['path'],pages=x.get('Pages',0)) for x in folders],ensure_ascii=False,indent=2),encoding='utf-8')
 actual_years=[int(y) for x in folders for y in re.findall(r'- ((?:18|19|20)\d{2})\b',x['path']) if int(y)<=2026]
 print('years',min(actual_years),max(actual_years))
 fmap={x['Id']:x for x in folders};chosen={};candidates=[]
 for term in ['kkkk','hahaha','gargalhada','risos','riso']:
  if not (LOCAL/('r3_docvirt_search_'+term+'.json')).exists():continue
  r=json.loads((LOCAL/('r3_docvirt_search_'+term+'.json')).read_text(encoding='utf-8'))['data']
  for hit in r['matchs']:
   f=fmap.get(hit['folderID'],{});years=re.findall(r'- ((?:18|19|20)\d{2})\b',f.get('path',''))
   if not years:continue
   year=int(years[0]);d=year//10*10
   row=dict(term=term,decade=d,year_folder=year,folder=hit['folderID'],page=hit['page'],path=f['path'],image_url=f'https://api.docvirt.com/v1/documents/dvd_ajhpmj/{hit["folderID"]}/{hit["page"]}')
   candidates.append(row)
   if d not in chosen:chosen[d]=row
 (ROOT/'data/revision3_docvirt_candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2),encoding='utf-8')
 def fetch(row):
  raw=read(row['image_url']);name=f'r3_docvirt_{row["decade"]}';p=LOCAL/(name+'.webp');p.write_bytes(raw)
  row['local_image']=str(p.relative_to(ROOT)).replace('\\','/');print(row['decade'],row['term'],row['path'],row['page'],len(raw))
  return row
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:result=list(ex.map(fetch,chosen.values()))
 (ROOT/'data/revision3_docvirt_selected.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':main()
