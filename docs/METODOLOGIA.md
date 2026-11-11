# Método documental e estatístico

Autor único: Murillo Edson de Carvalho Souza.

## Balanço atualizado e dados vinculados

A coleta é dirigida, exploratória e não probabilística. O núcleo tem 121 testemunhos: E1=23, E2=95 e E3=3. O núcleo abrange 1872–2025: 110 registros estão entre 1900 e 2009, um em cada um dos 110 anos, e 11 ficam fora desse intervalo. O quadro de acompanhamento chega a 2026, sem atestação selecionada nesse ano. A ampliação por ano priorizou séries parlamentares brasileiras e portuguesas e periódicos brasileiros. As 66 indicações iniciais têm parecer individual; as 22 citações alegadas não foram autenticadas integralmente. O núcleo contém 96 rubricas descritivas e 25 representações miméticas ou marcadores digitais; as categorias não são intercambiáveis. O levantamento mais amplo inclui documentos desde 1645: são 40 identificadores de fonte anteriores a 1900 em 47 vínculos, sem cobertura anual contínua desse período.

Os 16 endereços indicados pelo autor estão no [inventário de bases](../data/base_registry.csv), com URL original, URL de acesso, sobreposições, quantidade selecionada e links para os dados. São 13 conjuntos operacionais de recursos de acesso, após agrupar portal/item do APESP, coleção/acervo geral da BBM e Orkut/Wayback. Essa definição se aplica aos endereços indicados, não ao universo de instituições ou fontes complementares; os domínios do manifesto não são contados como bases.

O [quadro quantitativo](../data/method_quantification.csv), também incluído na metodologia do artigo, reúne quantidades e unidades. O núcleo, as 135 referências por acervo/década e os 17 títulos inéditos se sobrepõem: não se somam como documentos independentes. Somente duas das 17 novas fontes ampliaram o núcleo. As 135 quotas por acervo e década têm referência selecionada, 70 em fontes alternativas; dois itens individuais têm conferência concluída sem ocorrência localizada, com duas alternativas de período registradas separadamente. Isso não equivale a confirmação nesses exemplares.

Os quatro inventários positivos têm 275 vínculos de registro e 258 identificadores de fonte distintos. As 135 seleções de quota correspondem a 129 fontes por source_id. A reconciliação e os vínculos estão em [consolidated_inventory.json](../data/consolidated_inventory.json) e [evidence_register.csv](../data/evidence_register.csv). Identidade de URL não prova independência textual.

O manifesto histórico contém 1635 entradas: 1482 com conteúdo, 2 respostas vazias e 151 falhas. Essas entradas incluem arquivos auxiliares, páginas de catálogo, imagens, PDFs, metadados e recursos técnicos; não são 1635 obras analisadas nem um contador de todas as tentativas realizadas. As 1484 entradas com estado `downloaded` incluem as respostas vazias. O histórico também conserva uma referência posteriormente retirada; preservação de proveniência não equivale a citação atual no artigo.

Todos os domínios presentes no manifesto constam em [source_domains.csv](../data/source_domains.csv). Eles não são contados como bases independentes. O [manifesto](../data/downloads.json) fornece URLs individuais, resultado de aquisição, tamanho e SHA-256. Os [testemunhos do núcleo](../data/attestations.csv), os [registros por acervo/década](../data/archive_decade_references.csv), a [matriz de pendências](../data/archive_decade_matrix.csv) e os [títulos inéditos](../data/revision4_new_titles.csv) têm arquivos próprios. A [busca anual suplementar](../data/annual_supplement.csv) conserva a fonte e o localizador de cada novo testemunho.

E1: imagem primária inspecionada. E2: texto/transcrição primária eletrônica, sem colação integral com o impresso. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada, excluída do núcleo positivo. E1–E3 são categorias de cadeia de evidência, não escores estatísticos.

O gerador [build_method_inventory.py](../scripts/build_method_inventory.py) reconstrói o inventário e o balanço a partir dos dados públicos. Os links no PDF levam diretamente aos arquivos correspondentes no GitHub; o repositório e a versão/commit consultados devem acompanhar a reprodução.

## Unidade e denominador

Referência, documento, ocorrência e tipo gráfico são diferentes. Três passagens da mesma obra não são três fontes independentes. Comparações anuais exigem universo, seleção e extensão inspecionada. Frequência por milhão de palavras só pode ser calculada com denominadores confiáveis.

## Desenho efetivamente executado

O método combina **pesquisa documental histórica, auditoria de citações, seleção intencional por cobertura temporal, rastreamento de referências e conferência contextual**. A aplicação foi assistida por ferramentas de busca, scripts e inteligência artificial. A codificação não foi realizada por dois avaliadores independentes. Não houve sorteio dos documentos, revisão sistemática exaustiva, estimação de prevalência nem teste causal da origem de uma grafia.

A investigação responde a duas perguntas distintas: localizar representações ou menções ao riso em documentos datáveis; e avaliar se esses documentos sustentam uma relação histórica entre formas impressas e digitais. A primeira requer identificação e autenticação da passagem. A segunda requer elos de transmissão que não se deduzem apenas da semelhança gráfica.

### Frentes de seleção e tamanhos realizados

As frentes não são amostras independentes e não devem ser somadas como obras distintas:

1. **Auditoria do material recebido:** 66 indicações bibliográficas e 22 frases alegadas. O conjunto foi definido pelo material inicial, não por cálculo amostral. Cada indicação recebeu parecer; nenhuma das 22 transcrições foi autenticada integralmente. Ver [pareceres](../data/references_audit.csv) e [verificação das frases](../data/claims_verification.csv).
2. **Núcleo de representações:** 121 registros, sendo 23 E1, 95 E2 e três E3. Há 96 rubricas descritivas e 25 representações miméticas ou marcadores digitais. As menções exclusivamente lexicais não integram esse núcleo.
3. **Ampliação anual:** 96 registros adicionais ao conjunto de 25 já constituído, priorizando anos ainda sem testemunho entre 1900 e 2009. São 87 registros parlamentares e nove periódicos; 73 brasileiros e 23 portugueses. Os novos registros já integram os 121 do núcleo, e não são outros 96 documentos a acrescentar ao total atual. Ver [suplemento anual](../data/annual_supplement.csv).
4. **Seleção por acervo e década:** 137 linhas de acompanhamento, das quais 135 têm referência selecionada e duas correspondem a exemplares fixos conferidos sem ocorrência localizada. Os 135 vínculos usam 129 identificadores de fonte e compreendem 112 menções lexicais, 18 rubricas e cinco grafias miméticas. A confirmação é direta no acervo indicado em 65 vínculos e alternativa em 70. A quota de uma referência por década é uma regra de cobertura documental, não uma amostra probabilística.
5. **Seleção cronológica de títulos ainda não incluídos:** 17 registros — 14 da Brasiliana e três espaços digitais. A lista anterior foi usada para excluir títulos já examinados. Os registros incluem 13 menções lexicais, dois registros lexicográficos e duas grafias miméticas. Somente estas duas últimas foram incorporadas ao núcleo. Ver [exclusões por sobreposição](../data/revision4_exclusions.csv) e [seleção](../data/revision4_new_titles.csv).
6. **Alternativas literárias de período:** duas fontes, Bocage (1800) e Gonzaga (1812), selecionadas para documentar as décadas dos dois itens fixos sem ocorrência. Elas estão [registradas separadamente](../data/period_alternatives.csv), sem transformar a leitura negativa desses exemplares em atestação positiva.

O [quadro por acervo](../data/archive_selection_counts.csv) discrimina linhas de acompanhamento, vínculos positivos, fontes por identificador, confirmação direta/alternativa e classes de ocorrência. O total de identificadores calculado separadamente em cada acervo não deve ser somado como total de fontes únicas, pois um documento pode atender a quotas diferentes. O [inventário de acesso](../data/base_registry.csv) mantém os 16 endereços e seus 13 grupos operacionais; os recursos complementares são rastreáveis no manifesto, sem confundir domínios com bases independentes.

### Elegibilidade, inclusão e exclusão

Uma passagem positiva precisa permitir identificar o documento, localizar o trecho e justificar sua data. O objeto é o uso em português; documentos portugueses participam da comparação, sem serem tratados como evidência exclusiva do português brasileiro. Traduções e edições posteriores conservam a data da versão consultada quando não houve cotejo de edição anterior.

As regras de classificação são:

- **Mimética ou marcador digital:** sequência que representa o riso ou funciona como marcador de humor no contexto, por exemplo `quiá`, `quá`, `ah! ah!` ou `kkkk`. A mera presença dessas letras não basta.
- **Rubrica descritiva:** indicação editorial de reação, como `(Risos.)`. Integra o núcleo em categoria própria; não é automaticamente uma onomatopeia.
- **Lexical/temática:** menção a `riso`, `sorriso`, `gargalhada` ou variantes pertinentes. Pode atender à seleção temática por década, mas não é incorporada ao núcleo como grafia sonora.
- **Lexicográfica:** definição ou comentário sobre a palavra, identificado separadamente na seleção de títulos.

Ficam fora do núcleo positivo: frases não autenticadas, dados só de catálogo, resultados de busca sem passagem conferida, nomes comerciais ou títulos de programa confundidos com risada, siglas ou palavras em que a sequência aparece acidentalmente e leituras espúrias de OCR. Uma mesma ocorrência duplicada pelo OCR não conta duas vezes. Documento sem acesso suficiente permanece com limitação explícita, sem inferência de ocorrência ou ausência.

Na seleção de títulos inéditos, volumes da mesma obra e números do mesmo periódico não foram multiplicados como novos títulos. Na seleção por quota, a mesma fonte pode aparecer em duas linhas justificadas; isso é vínculo de seleção, não nova fonte independente. Não houve comparação filológica completa de todas as edições, traduções ou reproduções.

### Como os candidatos foram localizados

A busca partiu das indicações recebidas, dos catálogos e dos recortes temporais da matriz. Foram combinados título, autor, ano, número de edição, página e termos temáticos ou variantes gráficas. Entre as pistas empregadas estão `riso`, `risos`, `rizo`, `sorriso`, `gargalhada`, `quiá`, `quia`, `quá`, `qua`, repetições de `ah`, `ha`, `k` e `rs`, com e sem acento e com pontuação variável. Essa lista descreve famílias de busca; **não é uma alegação de que toda combinação foi aplicada a todo acervo**.

O procedimento executado variou conforme o recurso:

1. Nos catálogos e acervos, identificaram-se título e recorte disponível; resultados ordenados por data foram usados quando o portal oferecia essa opção. Ordenar candidatos não significa inspecionar integralmente todos os itens retornados.
2. Em arquivos com texto, buscaram-se termos e variantes, recuperando a página e seu contexto. A camada textual e o OCR serviram à triagem, não à autenticação automática.
3. Diante de índice insuficiente, grafia histórica, texto sem OCR ou resultado ambíguo, utilizaram-se renderização, recortes e leitura visual das páginas selecionadas. Não se declara leitura integral de todas as obras adquiridas.
4. Para linhas sem resultado direto, buscaram-se estudos, transcrições e reproduções que citassem o jornal ou a obra. Seguiram-se referências até o número/página e confrontaram-se os metadados entre fontes. Os casos documentados estão em [RASTREIO.md](RASTREIO.md).
5. Quando a confirmação veio de outro portal, reprodução ou fonte secundária explícita, registrou-se essa procedência e manteve-se a ressalva sobre o cotejo no acervo inicialmente indicado. Transcrição secundária não foi promovida a fac-símile primário.

O rastreio foi inspirado em recomendações de busca por citações e documentação de buscas mencionadas em [RASTREIO.md](RASTREIO.md). Não se declara cumprimento integral de PRISMA-S ou TARCiS, nem se reconstrói retrospectivamente um protocolo prospectivo que não foi registrado. Os exemplos do rastreio são históricos; o estado atual de cada linha é o da matriz.

A prioridade de fontes foi documental: buscar o original quando acessível e, se necessário, registrar a confirmação alternativa com sua limitação. Isso não equivale a um algoritmo determinístico aplicado uniformemente. A seleção teve como critérios a pertinência, a datação disponível, a novidade em relação ao inventário pertinente e a possibilidade de verificar o trecho. Não foi adotada uma regra universal de “primeiro resultado do buscador” ou “documento mais antigo de toda a base”.

### Avaliação e codificação de cada passagem

Para reproduzir uma decisão já registrada, o leitor deve:

1. Localizar o registro pelo `id`, `source_id` ou `bib` no inventário correspondente e no [registro consolidado](../data/evidence_register.csv).
2. Conferir título, autoria quando disponível, número, edição e data no catálogo e no próprio documento; registrar divergências sem completar metadados por suposição.
3. Abrir o localizador indicado. Distinguir a página impressa da posição no PDF e, para conteúdo web, usar a captura ou o texto referido.
4. Ler o trecho com contexto suficiente para decidir se há risada representada, rubrica, menção lexical, uso lexicográfico ou falso positivo. A forma normalizada para busca não substitui a transcrição da fonte.
5. Conferir a imagem quando essa é a base alegada da evidência. Se houver apenas texto eletrônico ou interação reportada, preservar a classificação correspondente, sem declarar inspeção visual inexistente.
6. Registrar a base de datação. Não transferir a abertura de um tópico à data de uma resposta, nem a criação de uma comunidade à data da captura que preserva sua descrição.
7. Verificar se o documento já foi incluído e se a nova linha representa uma fonte nova ou outro vínculo com a mesma fonte.
8. Comparar a classificação com o registro publicado. Uma divergência deve trazer localizador, leitura alternativa e justificativa; os scripts não resolvem automaticamente a interpretação histórica.

**E1, E2 e E3** registram imagem primária inspecionada, texto/transcrição primária eletrônica e interação reproduzida em estudo, respectivamente. Não são notas de qualidade comparáveis numericamente. Fontes alternativas da matriz podem ser secundárias e não herdam automaticamente um desses níveis do núcleo. Os pareceres da auditoria inicial têm categorias próprias: autenticação de representação, referência lexical/contextual, identificação bibliográfica, exemplar recuperado sem confirmação e caso sem autenticação suficiente.

A busca não recuperada não é tratada como frequência zero. Nos dois itens fixos, o estado “conferido: sem ocorrência localizada” documenta o exame realizado e seus limites, sem afirmar inexistência em toda a série. Não foi calculado acordo entre avaliadores, pois não houve dupla codificação independente.

### Técnicas e ferramentas: funções e limites

- **Busca textual e variantes:** localização de candidatos, inclusive diferenças de acento, pontuação, repetição e grafia histórica.
- **Extração de texto de PDF:** triagem por página e contexto com PyMuPDF. O script [trace_laughter.py](../scripts/trace_laughter.py) recompõe hifenização de linha e exporta candidatos em JSONL; não autentica a passagem.
- **OCR e inspeção visual:** apoio à leitura de fac-símiles. Leituras automáticas suspeitas são cotejadas com a imagem; texto espúrio em folha em branco é descartado. OCR não foi aplicado de forma uniforme a todos os arquivos.
- **Rastreio de citações e cruzamento de acervos:** identificação de edição, número e página em estudos, referências e reproduções. O procedimento não garante que fontes secundárias sejam independentes entre si.
- **Consulta estruturada de índice público:** no caso de O Globo de 1925, usou-se a consulta documentada em [RASTREIO.md](RASTREIO.md), seguida da recuperação e leitura da imagem. O índice orientou a descoberta, sem substituir a conferência.
- **Manifesto de aquisição e SHA-256:** rastreabilidade do arquivo efetivamente obtido. Hash idêntico comprova identidade dos bytes, não autenticidade histórica ou independência textual.
- **Reconciliação por identificador e URL:** controle das sobreposições entre inventários. Não elimina automaticamente reedições ou conteúdo reproduzido em URLs diferentes.
- **Validação por scripts:** conferência de contagens, vínculos, chaves bibliográficas, fórmulas de planejamento e aspectos do PDF. A validação técnica não substitui a crítica documental.

Não houve treinamento de modelo específico para recuperar o riso, classificação automática validada por amostra de referência, mensuração de precisão/recall ou aplicação de aprendizado ativo. O uso de ferramentas e IA não deve ser descrito como um algoritmo que autentica sozinho as fontes.

## Reprodução dos resultados publicados

### Fixar a versão e o ambiente

Clone o repositório e substitua `<COMMIT>` pelo identificador da versão que deseja reproduzir:

```sh
git clone https://github.com/murilloed/historia-riso-escrito-portugues.git
cd historia-riso-escrito-portugues
git checkout <COMMIT>
```

Os arquivos de dados públicos são a entrada para a reprodução das tabelas. O [ambiente local registrado](../data/reproduction_environment.json) informa Python 3.12.14, Tectonic 0.17.0 e as versões das bibliotecas de inspeção. A geração dos inventários usa a biblioteca padrão de Python; PyMuPDF é necessário para a triagem de PDF e para as verificações de conteúdo e hiperlinks do PDF. O validador pode executar sem PyMuPDF, mas nesse caso pula essas verificações: a ausência da biblioteca não deve ser interpretada como validação completa do PDF.

As versões registradas descrevem o ambiente usado, não garantem resultado binário idêntico em qualquer sistema. Fontes tipográficas, distribuição TeX, dependências e metadados de geração podem alterar os bytes do PDF sem alterar os dados.

### Reconstruir inventários e tabelas

Na raiz do projeto, execute:

```sh
python scripts/build_appendices.py
```

Esse comando reconstrói os dados derivados e as tabelas, usando os registros codificados no código e nos CSV versionados. Importa, entre outros, `build_data.py`, `build_method_inventory.py` e `audit_inventory.py`. Ele **não realiza novamente a pesquisa nos acervos** nem descobre ocorrências novas. Na ausência dos anexos privados, utiliza o catálogo público já versionado. Execute em cópia de trabalho própria, pois arquivos derivados são regravados.

As saídas de interesse são [quantificação](../data/method_quantification.csv), [inventário de recursos](../data/base_registry.csv), [quantidades por acervo](../data/archive_selection_counts.csv), [vínculos de evidência](../data/evidence_register.csv), [balanço reconciliado](../data/consolidated_inventory.json) e tabelas LaTeX em `artigo/generated/`.

Para reconstruir apenas a reconciliação dos inventários existentes:

```sh
python scripts/audit_inventory.py
```

Verifique que os quatro inventários totalizam 275 vínculos, 258 identificadores e 258 URLs, que o núcleo soma 121 registros e que a seleção por acervo contém 135 vínculos, 129 fontes e 137 linhas acompanhadas. Esses são resultados desta versão; revisões posteriores podem legitimamente alterá-los.

### Conferir uma fonte e refazer a triagem

Escolha um `source_id` no inventário e encontre a entrada correspondente em [downloads.json](../data/downloads.json). Ela informa URL, resultado histórico de aquisição, tamanho e SHA-256 quando o arquivo foi obtido. Obtenha o documento em uma pasta separada de trabalho, preservando o manifesto publicado. Compare o hash quando a aquisição atual permitir: em PowerShell, `Get-FileHash -Algorithm SHA256 caminho.pdf`; em sistemas com a ferramenta disponível, `sha256sum caminho.pdf`.

Para a triagem textual de um PDF local:

```sh
python -X utf8 scripts/trace_laughter.py caminho.pdf > candidatos.jsonl
```

O padrão atual de `trace_laughter.py` procura as famílias lexicais `riso/risos`, `risada/risadas`, `gargal...`, `sorri...`, `rindo` e `riu`, após normalizar acentos e recompor hifenização. Ele não cobre sozinho todas as grafias miméticas nem todas as variantes históricas, como `rizo`: essas exigem buscas adicionais ou adaptação explícita do padrão, com a versão registrada.

Os candidatos precisam ser conferidos na página. Uma página sem texto extraível exige leitura visual ou OCR adicional; um arquivo sem candidato não é automaticamente um documento sem riso. Não existe comando único que reproduza a totalidade das decisões manuais.

Os scripts de aquisição em `scripts/` preservam procedimentos de diferentes etapas; não devem ser executados indiscriminadamente sobre o manifesto publicado. Alguns regravam estados históricos ou dependem de endpoints e arquivos locais. Uma nova aquisição deve ser registrada como nova consulta, sem apagar a anterior. Falhas, bloqueios, alterações do portal e restrições de acesso devem ser relatados, sem contornar controles.

### Compilar e validar os artefatos

Com Tectonic instalado, execute a partir da raiz:

```sh
tectonic -X compile artigo/main.tex --keep-logs --keep-intermediates
python scripts/validate.py
python scripts/package_release.py
```

O compilador deve estar no PATH; no ambiente Windows registrado também existe o executável local `tools/tectonic/tectonic.exe`. A alternativa com pdfLaTeX/BibTeX está no [README](../README.md#compilar). A validação requer os arquivos auxiliares produzidos na compilação. O empacotamento produz `dist/artigo-overleaf.zip` e o arquivo de hashes, sem autenticar o conteúdo histórico do manuscrito.

Confira o relatório em [validation.json](../data/validation.json), as contagens e os links. Renderize e inspecione as páginas alteradas: o validador detecta problemas específicos, mas não substitui a revisão visual de diagramação. O fluxo de GitHub Actions reconstrói tabelas e compila o artigo; não deve ser confundido com uma nova auditoria humana das fontes.

### O que é e o que não é reproduzível com os registros disponíveis

São reconstruíveis a partir dos arquivos públicos: composição dos inventários codificados, sobreposições por identificador, tabelas, cálculos de cenários, chaves bibliográficas e arquivos LaTeX. As interpretações podem ser auditadas pelos localizadores, fontes disponíveis e critérios acima.

A busca histórica completa não é reproduzível como uma sequência exata de requisições: não há log exaustivo de todos os termos, filtros, horários, resultados recuperados, candidatos descartados e páginas examinadas. Não se dispõe de denominador confiável de todas as obras ou páginas triadas; os 1.635 registros de aquisição não substituem esse denominador. Direitos, disponibilidade de portais e arquivos mantidos locais também limitam a repetição. Esses limites impedem inventar um fluxo de revisão sistemática ou calcular rendimento de busca e recall a partir do manifesto.

Para **novas buscas**, recomenda-se registrar: identificador da consulta, linha-alvo, recurso, data/hora, termo exato, filtros, ordenação, URL ou endpoint, fonte candidata, localizador, transcrição, tipo de evidência, decisão e justificativa. Trata-se de uma especificação para ampliar o registro daqui em diante, não de dados retrospectivos que já existiriam para toda a coleta.

<a id="plano-de-amostragem"></a>

## Plano de amostragem: finalidade prospectiva

**Estatuto dos cálculos.** As fórmulas abaixo foram calculadas como cenários interpretativos e de planejamento. O desenho probabilístico correspondente **não foi aplicado à seleção do corpus**: os cálculos não fixaram o número de documentos por ano, não orientaram sorteio de unidades e não determinaram uma regra de encerramento por tamanho amostral.

O trabalho executado foi direcionado pela pergunta de pesquisa, pelas indicações bibliográficas, pelas metas de cobertura anual ou decenal, pela disponibilidade dos documentos e pela verificação das passagens. As quantidades efetivamente encontradas decorrem dessa seleção intencional. Elas descrevem os inventários, sem estimar prevalências ou conferir representatividade à coleta. Os níveis de confiança e margens de erro dos exemplos não são propriedades dos resultados empíricos publicados.

A utilidade das fórmulas é explicitar, sob hipóteses declaradas, os limites de uma busca com poucos documentos e planejar uma ampliação futura com moldura documental e seleção probabilística. A probabilidade de detecção dos exemplos é condicional aos valores pressupostos de ocorrência e independência; não foi estimada para os acervos examinados. Os cálculos não justificam retrospectivamente a quantidade de referências selecionada em cada ano.


O estrato combina ano e suporte, $h=(y,s)$. Para cada estrato, registram-se o tamanho da população $N_h$, o país, o gênero, a edição, o acervo e a extensão. Prevê-se censo dos estratos pequenos e sorteio sem reposição nos demais. Materiais digitais exigem unidades próprias — sessão, usuário ou mensagem — e tratamento de sua dependência.

### Dimensionamento para uma proporção

Para uma proporção binomial em população grande:

$$
n_0 = \frac{z^2 p(1-p)}{e^2}
$$

Nessa expressão, $z$ é o quantil normal associado ao nível de confiança, $p$ é a proporção pressuposta no planejamento e $e$ é a margem de erro absoluta desejada.

Com $z=1{,}96$, $p=0{,}5$ e $e=0{,}10$:

$$
n_0 = \frac{1{,}96^2 \times 0{,}5 \times (1-0{,}5)}{0{,}10^2}
= 96{,}04
\qquad\Rightarrow\qquad n=97
$$

O resultado é arredondado para cima. Com $e=0{,}05$, são necessários 385 documentos por estrato, sob os mesmos pressupostos. Aplicar 97 documentos a cada ano e a cada um de dois suportes, ao longo de 110 anos, produziria:

$$
97 \times 2 \times 110 = 21\,340
$$

Esse total é um cenário de planejamento, não uma quota universal ou uma exigência para este estudo.

### Correção para população finita

Para uma população conhecida de tamanho $N_h$, com sorteio sem reposição:

$$
n_h = \left\lceil \frac{N_h n_0}{N_h+n_0-1} \right\rceil
$$

O símbolo $\lceil x\rceil$ indica arredondamento para cima. Usa-se o valor **não arredondado** de $n_0$ na correção. No cenário $n_0=96{,}04$, obtêm-se 17 documentos para $N_h=20$, 50 para $N_h=100$ e 88 para $N_h=1000$.

### Detecção de pelo menos uma ocorrência

Sob oportunidades independentes e probabilidade constante $p$ de ocorrência por documento:

$$
P(\text{pelo menos uma ocorrência}\mid n,p)=1-(1-p)^n
$$

Para alcançar uma probabilidade de detecção de pelo menos $q$, com $0<p<1$ e $0<q<1$:

$$
n \geq \left\lceil \frac{\log(1-q)}{\log(1-p)} \right\rceil
$$

Com $q=0{,}95$, o mínimo é 59 documentos para $p=0{,}05$ e 299 para $p=0{,}01$. Esses valores de $p$ são **cenários**, não estimativas obtidas do corpus.

### Alocação com custos distintos

Se os desvios-padrão $S_h$ e os custos por unidade $c_h$ forem conhecidos, a alocação ótima sob restrição de custo segue:

$$
n_h \propto \frac{N_h S_h}{\sqrt{c_h}}
$$

O símbolo $\propto$ significa “proporcional a”. As variâncias e os custos necessários a essa alocação **não foram estimados nesta coleta**.

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
