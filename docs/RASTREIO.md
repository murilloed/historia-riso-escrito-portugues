# Rastreio de ocorrências por edição

O procedimento adapta [TARCiS](https://www.bmj.com/content/385/bmj-2023-078384) para seguir citações e [PRISMA-S](https://pmc.ncbi.nlm.nih.gov/articles/PMC8270366/) para registrar a busca. A aplicação é exploratória.

1. Fixar a linha da matriz e identificar o título, o ano e o número no catálogo.
2. Escolher pesquisas que tenham usado o periódico. Seguir suas notas para trás até a edição. Procurar também trabalhos posteriores e reproduções que remetam à mesma edição.
3. Cruzar título, data, número e página em acervos diferentes. Agrupar cópias do mesmo documento, mantendo a procedência de cada uma.
4. Triar as páginas e conferir a atribuição do trecho à edição. Uma transcrição explícita pode sustentar confirmação em fonte alternativa.
5. Registrar consulta, fonte de partida, edição candidata, página, trecho, URL e decisão. Distinguir falha de acesso, edição não localizada e ocorrência descartada.

## Triagem local

Com Python e PyMuPDF instalados, rode **python -X utf8 scripts/trace_laughter.py caminho.pdf**. A saída JSONL traz arquivo, página, termo e contexto. O script recompõe palavras hifenizadas na quebra de linha e usa a camada textual do PDF. Páginas sem texto exigem OCR externo ou leitura direta.

## Aplicação

- **H07/1920.** A busca por Jornal do Brasil, Palcos e Telas e gargalhadas levou à [dissertação da UFF](https://www.historia.uff.br/stricto/td/1992.pdf). A nota 192 indica a edição 244, de 9 de setembro de 1921, p. 10. A expressão “estrepitosas gargalhadas”, encontrada em outro trecho do estudo, pertence ao jornal A Noite. A linha continua pendente.
- **H10/1980.** A busca pelo Diario de Pernambuco em estudos sobre cinema Super-8 levou à [dissertação de Gabriel Bandeira Alexandre](https://pt.scribd.com/document/1028640152/Super-8-e-Resistencia-Micropolitica-No-Recife-1973-1983-Gabriel-Bandeira-Alexandre). A bibliografia identifica a edição de 17 de maio de 1982, seção B, p. B-3. As menções a sorriso verificadas no estudo descrevem um filme de 1979. A linha continua pendente.
- **Controle.** A triagem recuperou “gargalhadas” na p. 2 do Jornal Pequeno de 21 de julho de 1910, já documentado como D117. O OCR duplicou a passagem na mesma página, o que impede usar a contagem bruta de resultados como contagem documental.

## Nova aplicação

- **H10/1960, incluída como D119.** A consulta por Diario de Pernambuco, gargalhadas e anos de atuação de Barreto Júnior levou ao [estudo de Leidson Ferraz](https://leidsonferraz.com.br/assets/pdfs/artigos/a26.pdf#page=19). A busca dentro do PDF passou de gargalhadas a riso e localizou a transcrição “provocar o riso franco”. A referência identifica Adeth Leite, Diario de Pernambuco, 17 de setembro de 1968, p. 5. A conferência no portal do jornal segue pendente.
- **H07/1920, ocorrência descartada.** A consulta por Jornal do Brasil, 1921, gargalhadas e teatro levou a [A Noite de 5 de dezembro de 1921](https://hemeroteca-pdf.bn.gov.br/348970/per348970_1921_03591.pdf#page=6). A edição reúne citações de vários jornais. A ocorrência de gargalhadas recuperada na busca estava fora do bloco introduzido por “Diz o Jornal do Brasil”.

## Rastreio temático por esporte e imprensa

- **H02/1950, incluída como D120.** A consulta por O Globo e formas flexionadas de sorrir encontrou a [tese sobre a cobertura da Copa de 1950](https://cev.org.br/media/biblioteca/4035746.pdf). Na p. 97, a transcrição atribui a O Globo de 5 de julho de 1950, p. 3, a expressão “Flávio sorriu e esclareceu”. A consulta ao portal original segue pendente.
- **H02/1930, mantida como pista.** O [Blog do Acervo](https://blogs.oglobo.globo.com/blog-do-acervo/post/como-os-cariocas-viraram-noite-nas-ruas-para-ver-chegada-do-dirigivel-graf-zeppelin-ha-90-anos.html) identifica a edição de 26 de maio de 1930. A expressão “cair na gargalhada” está no texto de 2020, fora do trecho explicitamente transcrito. A ocorrência histórica exige confirmação.
- **H02/1940, mantida como pista.** Uma [dissertação da UFF](https://www.historia.uff.br/stricto/td/2053.pdf) indica um recorte de O Globo de 1948, mas o trecho sobre sorriso remete ao Correio da Manhã.

As [15 linhas pendentes](../data/archive_decade_matrix.csv) continuam abertas. A [revisão anterior](REVISAO-24.md) agrupa as rotas por acervo.
