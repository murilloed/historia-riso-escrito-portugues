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
- [Condições de aquisição e distribuição](sources/README.md).
- [Validação executada](data/validation.json).

## Resultado e alcance

O inventário tem **15 atestações em documentos ou interações reportadas**, com ao menos um documento de cada década de 1900 a 2000. São seis testemunhos com imagem inspecionada (E1), seis transcrições primárias eletrônicas (E2) e três interações reportadas em pesquisas (E3).

Isso **não é cobertura de todos os anos nem uma amostra equilibrada de três livros e três jornais por período**. Também não representa frequência de uso da população. As lacunas anuais são publicadas explicitamente.

O levantamento documenta quiá em Til, cá em A segunda vida, ah em obras do início do século XX, quá em O Tico-Tico de 1935, ah no Diário Carioca de 1941 e em quadrinhos publicados em 1979. Inclui rubricas descritivas de 1925, 1955, 1965, 1985 e 1994 em categoria própria. Uma dissertação de 2008 reproduz kkkk em pesquisa desenvolvida em 2007.2.

**Não se identificou a primeira ocorrência absoluta de kkkk nem se demonstrou sua derivação de quiá.** Também não se demonstrou que as formas antigas fossem independentes ou tenham desaparecido da circulação. Onomatopeias podem ser transmitidas, emprestadas e modificadas historicamente.

As 22 transcrições do material inicial permanecem **não autenticadas nesta coleta**. Esse estatuto não significa prova de inexistência. As 66 sugestões são pistas para investigação; sua inclusão no apêndice não endossa datas ou descrições.

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

## Referências da UnB e literatura recente

A relação com a bibliografia da UnB se apoia no Anexo IV do Edital 04/2026 do PPGL, documento oficial identificado no inventário. Não se atribui uma preferência uniforme a todo o departamento. Estudos de 2024 e 2025 complementam os fundamentos em iconicidade e sinais digitais. Nenhuma afiliação, financiamento ou avaliação por pares foi presumida.

## Citação

SOUZA, Murillo Edson de Carvalho. Do riso impresso ao kkkk: mudança linguística, iconicidade e evidência documental na história das representações do riso em português. Manuscrito exploratório e repositório de pesquisa, 2026. Disponível em: https://github.com/murilloed/historia-riso-escrito-portugues. Identifique o commit ou release consultado.

Há metadados em CITATION.cff. O GitHub não fornece DOI automaticamente; nenhum DOI foi inventado.

## Direitos e autoria

Manuscrito e arquivos novos são identificados com a autoria de Murillo Edson de Carvalho Souza. A publicação pública não atribui automaticamente licença aberta ao manuscrito. Os textos e imagens de terceiros mantêm direitos e condições próprias, detalhados no inventário e nos cabeçalhos dos textos.

A elaboração utilizou assistência de IA para organização, redação, busca e programação, declarada no artigo. Essa assistência não configura coautoria e não substitui avaliação científica independente.
