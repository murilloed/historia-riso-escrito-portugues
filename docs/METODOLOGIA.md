# Método documental e estatístico

Autor: Murillo Edson de Carvalho Souza. Data da coleta: 8 de novembro de 2026.

## O que foi executado

Busca dirigida e auditoria exploratória. Os 15 registros não resultam de sorteio. O conjunto distingue 10 representações miméticas/marcadores e cinco rubricas descritivas. Documentos com exemplos reproduzidos em dissertações são classificados como interações reportadas, e não como logs originais obtidos.

Os 34 downloads bem-sucedidos incluem apoio bibliográfico e fontes sem ocorrência validada; não equivalem a 34 documentos positivos. O inventário também registra três falhas. A consulta web de Young não se confunde com aquisição local.

E1: imagem primária inspecionada. E2: transcrição eletrônica primária sem colação completa. E3: interação reproduzida em estudo com localizador. E4: alegação secundária ou não autenticada; os 22 alvos do roteiro não entram como dados positivos.

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
