# Método documental e estatístico

Autor único: Murillo Edson de Carvalho Souza. Consulta: 8 e 9 de novembro de 2026.

## Balanço atualizado e dados vinculados

A coleta é dirigida, exploratória e não probabilística. O núcleo tem 121 testemunhos: E1=23, E2=95 e E3=3. O núcleo cobre 110 dos 110 anos de 1900 a 2009. A ampliação por ano priorizou séries parlamentares brasileiras e portuguesas e periódicos brasileiros. As 66 indicações iniciais têm parecer individual; as 22 citações alegadas não foram autenticadas integralmente. Os números de 15 registros e 34 aquisições pertenciam à primeira versão e foram substituídos por este balanço consolidado.

Os 16 endereços indicados pelo autor estão no [inventário de bases](../data/base_registry.csv), com URL original, URL de acesso, sobreposições, quantidade selecionada e links para os dados. Não são 16 bases independentes: há portal e item do APESP, coleção e acervo geral da BBM e Orkut preservado no próprio Wayback.

O [quadro quantitativo](../data/method_quantification.csv), também incluído na metodologia do artigo, reúne quantidades e unidades. O núcleo, as 117 referências por acervo/década e os 17 títulos inéditos se sobrepõem: não se somam como documentos independentes. Somente duas das 17 novas fontes ampliaram o núcleo. As quotas da rodada 3 permanecem incompletas.

O manifesto histórico contém 1608 entradas: 1458 com conteúdo, 2 respostas vazias e 148 falhas. Essas entradas incluem arquivos auxiliares, páginas de catálogo, imagens, PDFs, metadados e recursos técnicos; não são 1608 obras analisadas nem um contador de todas as tentativas realizadas. As 1460 entradas com estado `downloaded` incluem as respostas vazias. O histórico também conserva uma referência posteriormente retirada; preservação de proveniência não equivale a citação atual no artigo.

Todos os domínios presentes no manifesto constam em [source_domains.csv](../data/source_domains.csv). Eles não são contados como bases independentes. O [manifesto](../data/downloads.json) fornece URLs individuais, resultado de aquisição, tamanho e SHA-256. Os [testemunhos do núcleo](../data/attestations.csv), os [registros por acervo/década](../data/archive_decade_references.csv), a [matriz de pendências](../data/archive_decade_matrix.csv) e os [títulos inéditos](../data/revision4_new_titles.csv) têm arquivos próprios. A [busca anual suplementar](../data/annual_supplement.csv) conserva a fonte e o localizador de cada novo testemunho.

E1: imagem primária inspecionada. E2: texto/transcrição primária eletrônica, sem colação integral com o impresso. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada, excluída do núcleo positivo. E1–E3 são categorias de cadeia de evidência, não escores estatísticos.

O gerador [build_method_inventory.py](../scripts/build_method_inventory.py) reconstrói o inventário e o balanço a partir dos dados públicos. Os links no PDF levam diretamente aos arquivos correspondentes no GitHub; o repositório e a versão/commit consultados devem acompanhar a reprodução.

## Unidade e denominador

Referência, documento, ocorrência e tipo gráfico são diferentes. Três passagens da mesma obra não são três fontes independentes. Comparações anuais exigem universo, seleção e extensão inspecionada. Frequência por milhão de palavras só pode ser calculada com denominadores confiáveis.

## Plano de amostragem

Moldura de documentos por h=(ano,suporte). Registrar N_h, país, gênero, edição, acervo e extensão. Censo dos estratos pequenos; sorteio sem reposição nos demais. Materiais digitais exigem unidades próprias (sessão, usuário, mensagem), com tratamento da dependência.

Para proporção binomial e população grande, n0=z²p(1-p)/e². Com z=1,96, p=0,5 e e=0,10: 96,04, arredondado para 97 por estrato. Com e=0,05: 385. A exigência de 97 em cada ano e em cada um de dois suportes ao longo de 110 anos produz até 21.340 documentos. Não é uma quota universal ou necessária a todo estudo.

População finita: n=ceil(N*n0/(N+n0-1)); usar n0 não arredondado. Exemplo com N=20: 17; N=100: 50; N=1000: 88.

Detecção: P(ao menos uma)=1-(1-p)^n. Para q=0,95: n=ceil(log(1-q)/log(1-p)). Resultados: n=59 para p=0,05; n=299 para p=0,01. Supõem-se oportunidades independentes e p constante. Esses p são cenários, não estimativas do corpus.

Alocação ótima com custos distintos: n_h proporcional a N_h*S_h/sqrt(c_h), se variâncias e custos forem conhecidos. Não foram estimados nesta coleta.

## O que não se pode inferir

- A primeira ocorrência encontrada não é necessariamente a origem.
- Uma lacuna anual não representa zero histórico.
- Semelhança não demonstra genealogia; ausência de elos não demonstra independência.
- Intervalos binomiais não corrigem a seleção por conveniência.
- Um registro por década não sustenta predomínio ou substituição.
- Mudança de suporte não exclui mudança linguística.

O artigo apresenta Wilson como método aplicável a um desenho probabilístico futuro. Não fornece IC populacional para os exemplos atuais.

## Referências metodológicas

Cochran (1977), Sampling Techniques, 3ª ed.; Wilson (1927), DOI 10.1080/01621459.1927.10502953; Wilkinson et al. (2016), DOI 10.1038/sdata.2016.18. Os dados, fórmulas e cenários estão no artigo e em scripts/build_data.py.
