# Segunda auditoria documental — 8 de novembro de 2026

**Relatório histórico de etapa.** As contagens e pendências abaixo pertencem à etapa descrita. Para os resultados vigentes, consulte o [balanço reconciliado](../data/consolidated_inventory.json), a [matriz](../data/archive_decade_matrix.csv) e a [metodologia](METODOLOGIA.md).

Autor único do artigo: Murillo Edson de Carvalho Souza.

Esta rodada examinou individualmente as 66 indicações e buscou âncoras das 22 citações recebidas. Concluir o parecer sobre uma indicação não significa confirmar sua alegação. Nenhuma das 22 frases foi autenticada integralmente. Não houve leitura visual integral de todas as páginas de todos os volumes. A pesquisa combinou buscas web literais, identificação em catálogos, aquisição de exemplares, pesquisa do texto/OCR e inspeção visual de passagens e cabeçalhos selecionados.

## Novos testemunhos no corpus

- Urupês, quinta edição de 1919: Quá, quá, quá!, conto O engraçado arrependido, página 19, PDF 24. A primeira edição de 1918 não foi cotejada para essa passagem.
- Diário Nacional, 17/06/1928, n. 290, página 4: (risos, muito bem), discurso de Mattos Pimenta.
- Jornal de Notícias, 02/03/1947, n. 267, página 1: (Risos dos presentes), notícia sobre Bidault. Não é Folha da Manhã.
- Macunaíma, edição UFFS de 2019, página 139: Quá! quá! quá quaquá!... A ficha catalográfica está no PDF 205. O inventário usa 2019, sem retrodatação automática ao lançamento da obra em 1928.

O inventário passou de 15 para 19 testemunhos: E1=10, E2=6, E3=3. As rubricas descritivas são separadas das grafias miméticas. Referências lexicais ou temáticas não são somadas automaticamente como atestações de grafias.

## Resultado sobre as 66 indicações

A=3: representação de riso autenticada. L=7: referência lexical, temática ou cotejo contextual, sem autenticar a grafia atribuída. B=19: identificação bibliográfica; passagem não autenticada. I=4: exemplar específico recuperado; frase não autenticada. S=33: sem ocorrência autenticada ou referência insuficiente. O CSV references_audit.csv contém um parecer para cada indicação, fonte quando disponível, estado de aquisição e limites. A legenda e as contagens estão em revision2_summary.json.

O arquivo candidate_sources.csv conserva as descrições recebidas para comparação; elas não foram reescritas como resultados. O artigo contém tanto o catálogo original quanto a matriz de pareceres. claims_verification.csv relaciona C01–C22 aos registros R01–R66. Os registros de busca em data/searches/ publicam consultas quando disponíveis e endereços recuperados, sem republicar os excertos dos motores. Uma URL em resultado de busca não significa que a passagem foi lida ou confirmada.

## Correções e restrições

A menina morta foi identificada em edição de 1954; composição nos anos 1920 não demonstrada. Zero tem edição italiana de 1974 e portuguesa de 1975; preparação anterior não equivale a publicação. Chove nos campos de Cachoeira tem primeira publicação em 1941; 1998 precisa ser identificado como edição. Budapeste foi lançado em 2003; planejamento anterior não demonstrado.

Em Policarpo Quaresma, a fala de Floriano foi localizada no capítulo II da terceira parte, mas difere da transcrição enviada e não contém a risada alegada. Em Macunaíma, a passagem positiva encontrada também é diferente da citação recebida. Encontrar outra passagem não autentica uma frase atribuída à mesma obra.

Foram recuperadas as edições específicas de Gazeta de Notícias de 25/07/1904, O Malho de 12/10/1912 e Diário de Notícias de 18/03/1944. A busca no OCR não autenticou as frases atribuídas. OCR degradado e imagens não reconhecidas limitam essa conclusão. Fon-Fon! de maio de 1925 noticia retorno do Correio da Manhã após suspensão: é indício para revisar a data de fevereiro, não delimitação suficiente de todo o período sem circulação.

HTTP 403, 404, 429, erro de DNS e timeout constam no manifesto; não foram contornados. O PDF de provas de São Bernardo tem mais de 100 MB e permanece local, assim como materiais cuja republicação integral não foi verificada. URLs e SHA-256 dos downloads permitem nova aquisição. Os oito textos públicos da primeira versão foram preservados byte a byte.

## Método estatístico

As contagens acima descrevem a auditoria, não a frequência de uso de risadas na população. A seleção continua dirigida e não probabilística. O planejamento estratificado por ano e suporte permanece prospectivo: n=97 para precisão nominal de dez pontos percentuais, n=385 para cinco, sob os pressupostos descritos no artigo; detecção de ocorrência com probabilidade hipotética de 5% requer n=59 para chance de 95% de ao menos um achado. Esses números não justificam retrospectivamente quantidades desiguais de referências encontradas por ano.

## Reprodução

Execute python scripts/build_appendices.py para gerar as tabelas e pareceres a partir dos dados codificados. O script importa build_data e revision2_audit. extra_attestations.json contém os quatro acréscimos; claims_verification.csv contém os pareceres das frases. Os scripts revision2_download.py, revision2_periodicals.py, revision2_acquire_extra.py, revision2_focus.py e revision2_more_newspapers.py fazem aquisição incremental; não é necessário baixar os PDFs novamente para compilar o artigo. revision2_inspect.py localiza candidatos e produz extrações locais; seus resultados precisam de julgamento humano e conferência visual. revision2_integrate.py registra as decisões da rodada e acrescenta as referências idempotentemente.

A conclusão desta rodada é um corpus ampliado e um parecer explícito para cada indicação. Confirmar todas as frases recebidas continua sem suporte documental e não é anunciado como resultado alcançado.
