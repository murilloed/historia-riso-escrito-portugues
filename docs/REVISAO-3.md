# Ampliação por década em cada acervo

**Relatório histórico de etapa.** As contagens e pendências abaixo pertencem à etapa descrita. Para os resultados vigentes, consulte o [balanço reconciliado](../data/consolidated_inventory.json), a [matriz](../data/archive_decade_matrix.csv) e a [metodologia](METODOLOGIA.md).

Autor único: Murillo Edson de Carvalho Souza. Consulta em 8 de novembro de 2026.

## Escopo e andamento

A unidade de acompanhamento passou a ser o par **acervo × década**, conforme solicitado pelo autor. A coleta não foi concluída para todos os pares. `data/archive_summary.json` declara `scope_completed: false`; `data/archive_decade_matrix.csv` identifica as referências selecionadas e as quotas ainda pendentes. As linhas da matriz não são um universo exaustivo: alguns horizontes são editoriais, e os extremos gerais do portal APESP continuam indeterminados.

O núcleo de representações passa de 19 a **23 documentos**: 14 com imagem inspecionada, seis transcrições primárias eletrônicas e três interações reportadas. Os quatro documentos novos são:

- Imprensa Ytuana, 13/09/1879: `(Riso)`, rubrica em transcrição de discussão parlamentar, PDF p.2.
- A Cidade de Jardinópolis, 09/01/2016, p.3: `Hahaha...`, coluna Só Rindo.
- A Cidade de Jardinópolis, 29/01/2022, p.5: `kkkkk`, entrevista.
- Correio Braziliense, 07/04/2025, PDF p.22: `(risos)`, entrevista de Walter Lima Jr. por Ricardo Daehn.

A seleção cobre as onze décadas das pastas de Jardinópolis (1926–2022), com nove referências lexicais e duas grafias miméticas. No conjunto dos acervos, foram selecionadas 29 referências: 22 lexicais e sete rubricas ou grafias miméticas, incluindo três já presentes no núcleo anterior. As demais células permanecem pendentes.

O inventário complementar inclui referências lexicais a riso, sorriso e gargalhada. Elas não aumentam o núcleo de representações nem comprovam grafias onomatopaicas. As treze décadas com referência na BORE são 1870–1970, 2000 e 2010. Ausência de seleção em 1980 e 1990 não prova ausência no acervo.

## Limites verificados

- Jardinópolis: pastas com anos de 1926 a 2022; datas apenas de pasta são explicitamente identificadas. Busca por `quá` gera muitos falsos positivos, incluindo palavras comuns; seus resultados não são contagem de onomatopeias.
- BORE/USP: catálogo com extremos 1873 e 2012; 652 resultados para `risos`, 25 PDFs candidatos adquiridos e imagens selecionadas conferidas. Esses 652 resultados não são ocorrências autenticadas.
- Hemeroteca BN: a faixa inicial inclui Lisboa no século XVIII. O leitor desse item não carregou páginas úteis; não foi tratado como busca negativa. Um CAPTCHA apareceu e depois desapareceu sem submissão; não se declara que tenha sido resolvido. A autorização do autor para essa verificação foi recebida.
- Correio Braziliense: distingue-se o jornal de Brasília, iniciado em 1960, do título histórico de Hipólito da Costa.
- Google News / Jornal do Brasil: extremos informados pelo leitor, 08/04/1891–31/12/1999.
- Senado: Jornal do Senado, abril/1995–dezembro/2019; Em Discussão!, abril/2010–abril/2017. PDFs foram adquiridos e pesquisados; a ausência de OCR em parte dos arquivos limita o procedimento. Anais parlamentares de outros períodos não foram usados para simular cumprimento desta coleção.
- BBM, coleção 8427: a descrição menciona 1808–1821, mas o único PDF recuperado corresponde a 1817. Não se declara exame de todos os números da série.
- APESP, item D000071: Gazeta do Rio de Janeiro, n.48, 25/02/1809, quatro páginas. O registro informa original fora de circulação por conservação e não apresenta fac-símile na consulta. Identificação bibliográfica não autentica uma ocorrência.
- CEPE: o recorte de periódicos foi separado dos manuscritos. O leitor devolveu candidatos, ainda não autenticados por década.
- Globo, Folha e Diario de Pernambuco: portais e condições de entrada foram investigados, mas as quotas históricas continuam pendentes. Não houve contorno de assinatura nem substituição silenciosa por cópia de outra instituição.

## Método e reprodução

Uma referência por década é uma quota documental solicitada, e não tamanho de amostra calculado para estimar prevalência. Cumprimento de quota não mede frequência de uso; a seleção dirigida não admite intervalos de confiança populacionais. Cópias do mesmo jornal em instituições diferentes não são testemunhos históricos independentes.

Dados públicos: `archive_profiles.csv`, `archive_decade_references.csv`, `archive_decade_matrix.csv` e `archive_summary.json`. URLs, localizadores, base da data e categoria acompanham cada referência. Os fac-símiles permanecem locais quando não há licença de redistribuição verificada.

Os scripts `revision3_*.py` documentam aquisição e triagem. `revision3_build.py` gera o inventário codificado, as tabelas e o bloco BibTeX. Para reconstruí-lo são necessárias as aquisições locais indicadas no manifesto; a compilação do artigo usa as tabelas públicas já geradas. Buscas de rede podem mudar com a disponibilidade dos serviços.

A ampliação não identifica a primeira ocorrência absoluta de `kkkk` nem demonstra uma cadeia de transmissão desde `quiá`. As pendências de cobertura estão publicadas para evitar apresentar esta rodada como levantamento integral.
