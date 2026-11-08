import urllib.request,json,zipfile,io,pathlib
import truststore
truststore.inject_into_ssl()
root=pathlib.Path(__file__).resolve().parents[1]
headers={'User-Agent':'academic-article-builder'}
req=urllib.request.Request('https://api.github.com/repos/tectonic-typesetting/tectonic/releases/latest',headers=headers)
with urllib.request.urlopen(req,timeout=30) as f:r=json.load(f)
a=next(a for a in r['assets'] if 'x86_64-pc-windows-msvc.zip' in a['name'])
with urllib.request.urlopen(urllib.request.Request(a['browser_download_url'],headers=headers),timeout=90) as f:data=f.read()
p=root/'tools/tectonic';p.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(io.BytesIO(data)) as z:
 for n in z.namelist():
  if n.endswith('tectonic.exe'): (p/'tectonic.exe').write_bytes(z.read(n))
print(r['tag_name'],a['name'],len(data))
