from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'artigo/main.tex';t=p.read_text(encoding='utf-8')
t=t.replace('A pesquisa recupera testemunhos literários e uma página de periódico, além de registros digitais reproduzidos em estudos acadêmicos, e oferece inventário de downloads, localizadores, códigos de evidência e scripts.','A pesquisa reúne dezenove atestações em textos literários, periódicos e registros de fala, além de interações digitais reproduzidas em estudos acadêmicos, e oferece inventário de downloads, localizadores, códigos de evidência e scripts. Todas as 66 indicações recebidas têm parecer individual; nenhuma das 22 frases alegadas foi autenticada integralmente. Identificação bibliográfica, ocorrência lexical e representação gráfica do riso são mantidas distintas.')
t=t.replace('Literary attestations and a 1935 periodical page are distinguished from digital interactions reproduced in academic studies.','Nineteen attestations in literary works, periodicals and reported speech are distinguished from lexical mentions and bibliographic identification. All 66 candidate references receive individual audit findings; none of the 22 alleged quotations was fully authenticated. Digital interactions reproduced in academic studies are coded separately.')
p.write_text(t,encoding='utf-8')
p=ROOT/'artigo/sections/06-conclusao.tex';t=p.read_text(encoding='utf-8');heading='\\section*{Disponibilidade de dados e materiais}'
start=t.index('A segunda auditoria acrescenta');end=t.index('\n\n',start);para=t[start:end]
t=t[:start]+t[end+2:];t=t.replace(heading,para+'\n\n'+heading);p.write_text(t,encoding='utf-8')
# Atualizar os dados auditáveis no dicionário do artigo.
p=ROOT/'artigo/sections/07-apendices.tex';t=p.read_text(encoding='utf-8')
t=t.replace('o repositório documenta comandos e versões.','o repositório documenta comandos e versões.')
t=t.replace('Regex localizam candidatos e não substituem anotação.','Regex localizam candidatos e não substituem anotação. A segunda rodada acrescenta os arquivos \\texttt{references\\_audit.csv}, \\texttt{claims\\_verification.csv} e \\texttt{extra\\_attestations.json}, além dos registros de buscas.');p.write_text(t,encoding='utf-8')
