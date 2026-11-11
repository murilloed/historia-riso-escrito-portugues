# Método documental e estatístico

Autor único: Murillo Edson de Carvalho Souza.

## Balanço atualizado e dados vinculados

A coleta é dirigida, exploratória e não probabilística. O núcleo tem 121 testemunhos: E1=23, E2=95 e E3=3. O núcleo cobre 110 dos 110 anos de 1900 a 2009. A ampliação por ano priorizou séries parlamentares brasileiras e portuguesas e periódicos brasileiros. As 66 indicações iniciais têm parecer individual; as 22 citações alegadas não foram autenticadas integralmente. O núcleo contém 96 rubricas descritivas e 25 representações miméticas ou marcadores digitais; as categorias não são intercambiáveis.

Os 16 endereços indicados pelo autor estão no [inventário de bases](../data/base_registry.csv), com URL original, URL de acesso, sobreposições, quantidade selecionada e links para os dados. São 13 conjuntos operacionais de recursos de acesso, após agrupar portal/item do APESP, coleção/acervo geral da BBM e Orkut/Wayback. Essa definição se aplica aos endereços indicados, não ao universo de instituições ou fontes complementares; os domínios do manifesto não são contados como bases.

O [quadro quantitativo](../data/method_quantification.csv), também incluído na metodologia do artigo, reúne quantidades e unidades. O núcleo, as 135 referências por acervo/década e os 17 títulos inéditos se sobrepõem: não se somam como documentos independentes. Somente duas das 17 novas fontes ampliaram o núcleo. As 135 quotas por acervo e década têm referência selecionada, 70 em fontes alternativas; dois itens individuais têm conferência concluída sem ocorrência localizada, com duas alternativas de período registradas separadamente. Isso não equivale a confirmação nesses exemplares.

Os quatro inventários positivos têm 275 vínculos de registro e 258 identificadores de fonte distintos. As 135 seleções de quota correspondem a 129 fontes por source_id. A reconciliação e os vínculos estão em [consolidated_inventory.json](../data/consolidated_inventory.json) e [evidence_register.csv](../data/evidence_register.csv). Identidade de URL não prova independência textual.

O manifesto histórico contém 1635 entradas: 1482 com conteúdo, 2 respostas vazias e 151 falhas. Essas entradas incluem arquivos auxiliares, páginas de catálogo, imagens, PDFs, metadados e recursos técnicos; não são 1635 obras analisadas nem um contador de todas as tentativas realizadas. As 1484 entradas com estado `downloaded` incluem as respostas vazias. O histórico também conserva uma referência posteriormente retirada; preservação de proveniência não equivale a citação atual no artigo.

Todos os domínios presentes no manifesto constam em [source_domains.csv](../data/source_domains.csv). Eles não são contados como bases independentes. O [manifesto](../data/downloads.json) fornece URLs individuais, resultado de aquisição, tamanho e SHA-256. Os [testemunhos do núcleo](../data/attestations.csv), os [registros por acervo/década](../data/archive_decade_references.csv), a [matriz de pendências](../data/archive_decade_matrix.csv) e os [títulos inéditos](../data/revision4_new_titles.csv) têm arquivos próprios. A [busca anual suplementar](../data/annual_supplement.csv) conserva a fonte e o localizador de cada novo testemunho.

E1: imagem primária inspecionada. E2: texto/transcrição primária eletrônica, sem colação integral com o impresso. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada, excluída do núcleo positivo. E1–E3 são categorias de cadeia de evidência, não escores estatísticos.

O gerador [build_method_inventory.py](../scripts/build_method_inventory.py) reconstrói o inventário e o balanço a partir dos dados públicos. Os links no PDF levam diretamente aos arquivos correspondentes no GitHub; o repositório e a versão/commit consultados devem acompanhar a reprodução.

## Unidade e denominador

Referência, documento, ocorrência e tipo gráfico são diferentes. Três passagens da mesma obra não são três fontes independentes. Comparações anuais exigem universo, seleção e extensão inspecionada. Frequência por milhão de palavras só pode ser calculada com denominadores confiáveis.

## Plano de amostragem

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
