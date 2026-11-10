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

## Rastreio temático por Carnaval

- **H07/1920, incluída como D121.** O apêndice 1 da [dissertação sobre o Carnaval de Santa Cruz](https://pt.scribd.com/document/1023768675/O-ULTRA-ESPLENDIDO-CARNAVAL-NA-TERRA-DAS) identifica o Jornal do Brasil de 14 de fevereiro de 1926, p. 10, no começo da transcrição. O verso com “boa gargalhada” aparece na p. 281 do apêndice. A conferência no Google News segue pendente.
- **H02/1920, H02/1930 e H07/1940.** O mesmo apêndice remete a O Globo de 18 de fevereiro de 1928, p. 7, e de 25 de fevereiro de 1933, p. 2, e ao Jornal do Brasil de 4 de fevereiro de 1940, p. 10. Essas edições são pistas, com ocorrência ainda sem confirmação.

## Cruzamento por transcrições e republicações

- **H07/1890.** A consulta pelo nome do jornal, pelos anos de 1891 e 1892 e por referências a riso encontrou uma republicação contemporânea. [O Tempo de 30 de novembro de 1891](https://hemeroteca-pdf.bn.gov.br/218731/per218731_1891_00190.pdf) atribui ao Jornal do Brasil um telegrama do Recife publicado na véspera. A menção a riso está em outro texto da edição. O telegrama fica como localizador, sem inclusão na matriz.
- **H07/1940.** A consulta por Jornal do Brasil, sorriso e 1940 encontrou uma [dissertação da UFJF](https://repositorio.ufjf.br/jspui/bitstream/ufjf/14124/1/lucaseduardodesouzaferreira.pdf). O resultado aproxima um verso com sorriso de uma referência à edição de 19 de janeiro de 1940. A referência bibliográfica próxima não permite atribuir o verso à edição, que fica como pista.
- **H10/1980.** A consulta por Diario de Pernambuco, sorriso e 1988 encontrou os [anais da Constituinte](https://www.senado.leg.br/publicacoes/anais/constituinte/n020.pdf). Os anais mencionam um recorte de 30 de maio de 1988, p. A-10, sobre benefícios para aposentados. A menção a sorriso pertence a um discurso nos anais. O recorte segue como localizador.

## Busca por pasta anual no Suplemento Cultural

- **H11/1990, incluída como D122.** A busca cruzou cada pasta de 1990 a 1999 com sorriso, risos, gargalhada e riso. O leitor indicou páginas candidatas, e foram recuperadas cinco imagens. A [página física 795](http://200.238.101.22/docreader/docreader.aspx?bib=SPFULL&pesq=gargalhada&pasta=1990&pagfis=795) traz o cabeçalho JUN 90 e, na coluna central da p. impressa 16, a expressão “gargalhada que entra na hora certa”. A forma é lexical e ocorre numa crônica de José Cláudio.

## Busca por data de edição na BORE/USP

- **H04/1980 e H04/1990, incluídas como D123 e D124.** A [navegação por data](https://obrasraras.usp.br/xmlui/handle/123456789/4262/browse?type=dateissued&starts_with=1980) recuperou 14 itens de O Bisturi das duas décadas. A extração textual dos PDFs devolveu ocorrências em exemplares de 1983, 1985 e 1992. Foram selecionados “Envergonhou-se dos risos dos colegas” em setembro de 1985, PDF p. 7, e “tipo de risada” em janeiro/fevereiro de 1992, PDF p. 5. A navegação por data recuperou exemplares que a consulta por palavra não havia selecionado.

As [11 linhas pendentes](../data/archive_decade_matrix.csv) continuam abertas. A [revisão anterior](REVISAO-24.md) agrupa as rotas por acervo.
