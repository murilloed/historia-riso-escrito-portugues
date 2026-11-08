"""OCR auxiliar: saída local; toda citação exige inspeção posterior da imagem."""
from pathlib import Path
import json,re
from rapidocr_onnxruntime import RapidOCR
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'sources/local'
engine=RapidOCR(intra_op_num_threads=4,inter_op_num_threads=2,det_limit_side_len=2600)
for p in D.glob('r3_docvirt_*.webp'):
 # Excluir nomes legados incompatíveis com o corte temporal da pesquisa.
 year=re.search(r'(\d{4})$',p.stem)
 if year and int(year[1])>2026:continue
 dest=p.with_suffix('.ocr.json')
 if dest.exists():continue
 result,timing=engine(str(p),use_cls=False)
 rows=[dict(box=r[0],text=r[1],confidence=float(r[2])) for r in (result or [])]
 dest.write_text(json.dumps(rows,ensure_ascii=False),encoding='utf-8')
 p.with_suffix('.ocr.txt').write_text('\n'.join(r['text'] for r in rows),encoding='utf-8')
 hits=[(i,r['text']) for i,r in enumerate(rows) if re.search(r'ri[sz]o|gargalh|ha.?ha|kkkk',r['text'],re.I)]
 print(p.stem,'lines',len(rows),'hits',json.dumps(hits,ensure_ascii=True),flush=True)
