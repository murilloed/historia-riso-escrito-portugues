from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'artigo/main.tex';t=p.read_text(encoding='utf-8')
start=t.index('This paper examines');end=t.index('\n\\end{abstract}',start)
t=t[:start]+'''This paper examines whether historical written laughter can be linked to Brazilian digital \\textit{kkkk}. Historical linguistics and documentary criticism distinguish resemblance, chronology and demonstrated transmission. Nineteen attestations are documented. All 66 candidate references receive individual audit findings; none of the 22 alleged quotations was fully authenticated. Bibliographic identification and lexical mentions are distinguished from representations of laughter. A 2008 dissertation reports typed laughter collected in 2007. Neither an absolute first occurrence nor a transmission chain from nineteenth-century writing is established. Annual stratification, sample-size calculations and detection probabilities are prospective planning; the collection remains exploratory and non-probabilistic. Public data and scripts document evidence levels, acquisition failures and coverage gaps.'''+t[end:]
p.write_text(t,encoding='utf-8',newline='\n')
p=ROOT/'artigo/references.bib';p.write_text(p.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')
