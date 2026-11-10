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

As [17 linhas pendentes](../data/archive_decade_matrix.csv) continuam abertas. A [revisão anterior](REVISAO-24.md) agrupa as rotas por acervo.
