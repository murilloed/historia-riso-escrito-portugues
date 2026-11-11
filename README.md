# Do riso impresso ao kkkk

**Autor único: Murillo Edson de Carvalho Souza.**

Artigo científico exploratório sobre mudança linguística, iconicidade e evidência documental nas representações do riso em português. Projeto LaTeX adaptado do template fornecido pelo autor, com arquivo principal, seções e bibliografia BibTeX.

## Leitura e arquivos principais

- [Artigo em PDF](artigo/main.pdf).
- [Arquivo principal LaTeX](artigo/main.tex).
- [Bibliografia BibTeX](artigo/references.bib).
- [Dados de atestações](data/attestations.csv).
- [Auditoria dos 22 exemplos apresentados como citações](data/claims_audit.csv).
- [Catálogo das 66 pistas bibliográficas recebidas](data/candidate_sources.csv).
- [Cobertura de cada ano, 1872–2026](data/annual_coverage.csv).
- [Método e dimensionamento estatístico](docs/METODOLOGIA.md).
- [Inventário consolidado dos 16 endereços indicados](data/base_registry.csv).
- [Quadro quantitativo com unidades e links](data/method_quantification.csv).
- [Domínios e fontes complementares do manifesto](data/source_domains.csv).
- [Condições de aquisição e distribuição](sources/README.md).
- [Validação executada](data/validation.json).

## Resultado e alcance

O inventário tem **121 atestações** e cobre os **110 anos de 1900 a 2009**. A busca anual adicionou 96 testemunhos, sendo 87 registros parlamentares e nove periódicos. O conjunto contém 23 testemunhos E1, 95 E2 e três E3. Os novos testemunhos e respectivos localizadores constam no [suplemento anual](data/annual_supplement.csv).

Isso **não é cobertura de todos os anos nem uma amostra equilibrada de três livros e três jornais por período**. Também não representa frequência de uso da população. As lacunas anuais são publicadas explicitamente.

O levantamento documenta quiá em Til, cá em A segunda vida, ah em obras do início do século XX, quá em O Tico-Tico de 1935, ah no Diário Carioca de 1941 e em quadrinhos publicados em 1979. Inclui rubricas descritivas de 1925, 1955, 1965, 1985 e 1994 em categoria própria. Uma dissertação de 2008 reproduz kkkk em pesquisa desenvolvida em 2007.2.

**Não se identificou a primeira ocorrência absoluta de kkkk nem se demonstrou sua derivação de quiá.** Também não se demonstrou que as formas antigas fossem independentes ou tenham desaparecido da circulação. Onomatopeias podem ser transmitidas, emprestadas e modificadas historicamente.

As 22 transcrições do material inicial permanecem **sem autenticação integral**, após buscas literais e cotejo dos textos adquiridos. Em Policarpo Quaresma, há fala semelhante, mas a transcrição enviada acrescenta uma risada e altera a passagem. Esse estatuto não significa prova de inexistência das demais frases.

**Todas as 66 indicações têm parecer individual**, em [references_audit.csv](data/references_audit.csv) e no apêndice do artigo: 3 com representação autenticada, 7 com referência lexical/temática ou cotejo contextual, 19 com identificação bibliográfica, 4 com exemplar específico recuperado sem confirmação da frase e 33 sem ocorrência autenticada ou com identificação insuficiente. As categorias são exclusivas; não são frequências históricas.

A revisão acrescentou Quá em Urupês, edição de 1919, uma rubrica do Diário Nacional de 1928, uma rubrica do Jornal de Notícias de 1947 e uma passagem de Macunaíma na edição UFFS de 2019. O último não foi retrodatado a 1928 sem cotejo. Jornal de Notícias não foi confundido com Folha da Manhã. Foram corrigidas ou ressalvadas datas de A menina morta, Zero, Chove nos campos de Cachoeira e Budapeste. Ver [relatório da revisão](docs/REVISAO-2.md) e [parecer das 22 frases](data/claims_verification.csv).

## Estrutura

- artigo/: projeto completo; main.tex, references.bib, sections/ e tabelas generated/.
- data/: CSV, JSON, inventários e relatório de validação.
- scripts/: aquisição, geração das tabelas, inspeção e validação.
- sources/public/: oito textos integrais com condições de uso preservadas.
- docs/: método, proveniência e limites.
- .github/workflows/: compilação automática.

O acervo de downloads integrais de trabalho fica em sources/local/ e é ignorado pelo Git quando os direitos de republicação não foram verificados. O inventário público fornece links, status, tamanho e SHA-256.

## Reproduzir as tabelas

Python 3.12 ou posterior. A geração das tabelas utiliza somente a biblioteca padrão:

    python scripts/build_appendices.py

Esse comando importa build_data.py, gera as estatísticas de planejamento e as tabelas de atestações e auditoria, e depois gera os apêndices. Na ausência dos anexos privados do autor, o catálogo usa o CSV já versionado. Os registros codificados são decisões documentais explícitas; o programa não descobre nem autentica citações automaticamente.

## Compilar

No Overleaf: envie o conteúdo do pacote de fontes, selecione main.tex como documento principal e pdfLaTeX como compilador. As tabelas geradas já estão incluídas.

Localmente, com TeX Live:

    cd artigo
    pdflatex -interaction=nonstopmode main.tex
    bibtex main
    pdflatex -interaction=nonstopmode main.tex
    pdflatex -interaction=nonstopmode main.tex

Alternativa, com Tectonic 0.17:

    tectonic -X compile artigo/main.tex --keep-logs --keep-intermediates

A compilação local desta versão usou Tectonic. O fluxo do GitHub também compila com TeX Live/pdfLaTeX. O template é da classe article, 11pt, A4, margens de uma polegada; foram conservados o estilo de cabeçalho e as citações numéricas. Adaptaram-se idioma, título, autoria, seções, suporte a tabelas longas e bibliografia. O texto de exemplo e sua coautoria não integram o novo manuscrito.

## Adquirir novamente os documentos

Os scripts não contornam autenticação, paywalls ou controles de acesso. Execute:

    python scripts/collect.py
    python scripts/collect_more.py
    python scripts/collect_periodicals.py
    python scripts/collect_final.py
    python scripts/collect_parliament.py
    python scripts/collect_rubrics.py
    python scripts/package_sources.py

collect.py inicia o inventário; os demais o complementam. Falhas permanecem registradas. Uma nova execução pode produzir resultados diferentes por alterações de URL, conteúdo ou disponibilidade. Ela atualiza o inventário de trabalho: preserve o commit antigo para comparar os checksums.

O download direto do PDF de Young falhou localmente; a leitura da fonte acadêmica e do registro institucional ocorreu por serviço de consulta web. O registro diz isso explicitamente. Não se publica como baixado um arquivo que não foi obtido.

## Verificação

Para inspeção de PDFs, instale as dependências opcionais:

    python -m pip install -r requirements.txt
    python scripts/validate.py
    python scripts/render_qa.py

validate.py confere contagens, cobertura, cálculos, chaves de citação, ausência de glifos faltantes e de caixas excedentes no log Tectonic, e checksums dos textos públicos. Para uma compilação TeX Live que escreva avisos diferentes, revise o log correspondente. render_qa.py gera imagens locais para revisão de diagramação; elas não são incluídas como fontes históricas.

A inspeção visual não substitui a validação histórica da citação. O relatório de execução fica em data/validation.json.

## Quantidade de fontes por ano

Três livros e três jornais constituem uma quota editorial, não um tamanho amostral estatisticamente demonstrado. O artigo oferece:

1. estratos por ano e suporte;
2. estimando de proporção de documentos com riso;
3. dimensionamento inicial de 97 documentos por estrato para erro de 10 pontos percentuais e 95% nominal, sob amostragem aleatória simples e p=0,5;
4. correção para população finita;
5. detecção de forma rara: 59 documentos para p=0,05 ou 299 para p=0,01, com 95% de chance de ao menos uma ocorrência;
6. análise de sensibilidade e limites da dependência entre documentos.

Esses números são **planejamento prospectivo**, não o desenho retrospectivo da coleta dirigida. Não se calculam intervalos populacionais para os 15 exemplos.

## Fundamentos linguísticos e literatura recente

Os livros de linguística e de fonética e fonologia são citados pela pertinência teórica. Estudos de 2024 e 2025 complementam os fundamentos em iconicidade e sinais digitais. O artigo não declara afiliação institucional, financiamento ou avaliação por pares inexistentes.

## Citação

SOUZA, Murillo Edson de Carvalho. Do riso impresso ao kkkk: mudança linguística, iconicidade e evidência documental na história das representações do riso em português. Manuscrito exploratório e repositório de pesquisa, 2026. Disponível em: https://github.com/murilloed/historia-riso-escrito-portugues. Identifique o commit ou release consultado.

Há metadados em CITATION.cff. O GitHub não fornece DOI automaticamente; nenhum DOI foi inventado.

## Direitos e autoria

Manuscrito e arquivos novos são identificados com a autoria de Murillo Edson de Carvalho Souza. A publicação pública não atribui automaticamente licença aberta ao manuscrito. Os textos e imagens de terceiros mantêm direitos e condições próprias, detalhados no inventário e nos cabeçalhos dos textos.

A elaboração utilizou assistência de IA para organização, redação, busca e programação, declarada no artigo. Essa assistência não configura coautoria e não substitui avaliação científica independente.

## Ampliação por acervo e década

A terceira rodada acrescenta quatro documentos ao núcleo e um inventário complementar de menções lexicais. A meta de uma referência em cada década de cada acervo **permanece parcialmente atendida**. Veja o [relatório da terceira revisão](docs/REVISAO-3.md), os [perfis dos 13 endereços](data/archive_profiles.csv), as [referências selecionadas](data/archive_decade_references.csv) e a [matriz com pendências](data/archive_decade_matrix.csv). O balanço atual registra 63 células confirmadas no acervo indicado, 69 em fonte alternativa e 3 linhas com quota pendente. Veja o [relatório da vigésima quarta revisão](docs/REVISAO-24.md). O estado de conclusão consta em [archive_summary.json](data/archive_summary.json).

## Títulos inéditos: Brasiliana e Wayback

A quarta rodada seleciona **17 títulos novos**, uma referência por obra, periódico ou site: 14 da Brasiliana, Kibe Loco, Cifra Club e uma comunidade do Orkut. O intervalo selecionado é 1645–2017; a consulta foi feita em 2026 e não constitui censo das bases. O fórum preserva `kkkkkkkkkkkkk` numa resposta de 2010 e o Orkut preserva `hehehe` numa descrição capturada em 2014. Essas duas fontes elevam o núcleo a 25 documentos. A data do tópico e a criação da comunidade não foram transferidas às ocorrências. O edital da UnB foi retirado do artigo e da bibliografia.

Veja [títulos selecionados](data/revision4_new_titles.csv), [exclusões de títulos anteriores](data/revision4_exclusions.csv) e [relatório da quarta rodada](docs/REVISAO-4.md).

## Balanço metodológico consolidado

A metodologia do artigo e o [documento metodológico](docs/METODOLOGIA.md) vinculam o [inventário de bases](data/base_registry.csv), o [quadro quantitativo](data/method_quantification.csv), o [manifesto de aquisição](data/downloads.json) e a [cobertura anual](data/annual_coverage.csv). A busca de 8 e 9 de novembro de 2026 priorizou séries parlamentares do Brasil e de Portugal e periódicos brasileiros. Os registros estão separados por fonte e nível de evidência. Consulte o [relatório da sexta revisão](docs/REVISAO-6.md).
