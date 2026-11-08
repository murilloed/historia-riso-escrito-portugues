from pathlib import Path
import pymupdf
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'tmp/qa/article';out.mkdir(parents=True,exist_ok=True)
d=pymupdf.open(ROOT/'artigo/main.pdf')
for i,p in enumerate(d):
 p.get_pixmap(matrix=pymupdf.Matrix(1.3,1.3)).save(out/f'page-{i+1:02}.png')
for start in range(0,len(d),9):
 sheet=Image.new('RGB',(900,1320),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j in range(start,min(start+9,len(d))):
  im=Image.open(out/f'page-{j+1:02}.png');im.thumbnail((282,400))
  x=(j-start)%3*300+9;y=(j-start)//3*440+26
  sheet.paste(im,(x,y));draw.text((x,y-18),f'Page {j+1}',fill='black')
 sheet.save(out/f'contact-{start//9+1}.png')
print('rendered',len(d),'pages')
