"""Repete aquisições válidas da rodada 4 usando as URLs públicas do manifesto.

Não contorna certificados inválidos nem trata resposta vazia como documento.
Capturas Wayback podem redirecionar; conferir sempre resolved_url depois.
"""
from pathlib import Path
import json
from revision2_download import run
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
 manifest=json.loads((ROOT/'data/downloads.json').read_text(encoding='utf-8'))
 rows=[(r['id'],r['url'],Path(r['path']).suffix.lstrip('.'),r.get('rights','fonte pública; licença a conferir')) for r in manifest if r['id'].startswith('r4_') and r['status']=='downloaded' and r.get('bytes',0)>0]
 run(rows)
