# Brasiliana, Orkut e Wayback: títulos inéditos

Autor único: Murillo Edson de Carvalho Souza. Consulta: 8 de novembro de 2026.

O autor delimitou uma **seleção cronológica de títulos inéditos, incluindo sites, fóruns e blogs**. A unidade desta rodada é a obra, o periódico ou o site. A antiga quota por acervo e década não foi substituída nem declarada concluída.

## Realizado

- Removido o edital da UnB da bibliografia, da introdução e da discussão. Removidas também as notas de recomendação institucional dos livros de Martelotta e de Seara, Nunes e Lazzarotto-Volcão. Os livros permanecem pela contribuição teórica; não há vínculo institucional com a UnB declarado no artigo.
- Selecionados **17 títulos novos**, em ordem de 1645 a 2017: 14 da Brasiliana, um blog (Kibe Loco), um fórum (Cifra Club) e uma comunidade pública do Orkut.
- Uma referência por título selecionado, sem multiplicação por volumes ou edições. Os títulos do inventário anterior foram mantidos na lista de exclusão, incluindo os examinados sem autenticação de ocorrência.
- Classificação: 13 referências lexicais, duas lexicográficas e duas grafias miméticas. Apenas estas duas últimas ampliam o núcleo, de 23 para **25 documentos** (E1=14, E2=8, E3=3).
- Corrigida a codificação das duas rubricas da rodada anterior (`jornal: rubrica`), que agora recebem explicitamente a categoria `rubrica descritiva` no CSV principal. Os testemunhos e as contagens não foram alterados por essa correção de categoria.

## Datas e leitura crítica

A Brasiliana foi acessada no domínio atual `digital.bbm.usp.br`, com o mesmo identificador de coleção `bbm/1`. O endereço antigo indicado retornou falha de certificado; não houve desativação da validação TLS. A consulta por `riso` retornou 1.078 itens. Esse número é de resultados de busca, não de referências autenticadas ou de ocorrências de uma grafia.

A seleção inclui Baltasar Teles (1645), Bluteau (1720), Moraes Silva (1789), Caldas Barbosa (1798), O Patriota (1813), Gazeta Pernambucana (1822), Nitheroy (1836), João Caetano (1837), Primeiros cantos (1846), Gennesco (1866), A fallencia (1902), Negrinha (1920), Poesia 1958/1978 (edição de 1980) e Anotações de um Bibliófilo (2017). Datas de catálogo identificam o exemplar, sem presumir primeira edição. O texto de 2017 remete a material antigo, que não foi automaticamente retrodatado.

O OCR de textos antigos pode confundir o **s longo** com `f`. Na Chronica de 1645, a ocorrência foi conferida na imagem e normalizada como `risos`; isso não representa uma transformação fonética de “rifos” em “risos”. Também foi rejeitado um falso candidato de OCR em outra página.

No Kibe Loco, uma postagem datada de 27/06/2007 contém referência lexical ao riso. A captura efetivamente recuperada é de **01/07/2007**, embora a consulta ao endereço de entrada tenha começado por uma captura de 10/06/2007. O manifesto preserva a URL solicitada e a resolvida.

No Cifra Club, `kkkkkkkkkkkkk` aparece numa resposta identificada como enviada em **12/07/2010 às 15h21**, preservada na captura de **15/09/2010**. O tópico começou em novembro de 2003; não se atribui a risada a 2003. Assim, o testemunho não antecipa a ocorrência reportada de 2007 já documentada no artigo.

No Orkut, o endereço indicado pelo autor é a entrada do arquivo de comunidades em outubro de 2014. Sua navegação levou à comunidade pública Kiko Dança Psy-TRANCE. `hehehe` está na descrição preservada em **04/10/2014**. A comunidade foi criada em 2006, mas a descrição podia ser editada. A ocorrência foi datada pela captura, não pela criação do espaço.

A triagem do Humor Tadela encontrou um caso de descontinuidade: um recurso incorporado a uma página de entrada capturada em 1998 foi servido por uma captura de 2002, com conteúdo sem ocorrência pertinente autenticada. Não foi incluído como referência positiva nem como prova de riso em 1998. Respostas HTTP vazias também não foram tratadas como documentos lidos.

## Dados e reprodução

- `data/revision4_exclusions.csv`: inventário de títulos anteriores usado na exclusão. Há linhas provenientes de fontes diferentes para o mesmo título; não são contagens de obras independentes.
- `data/revision4_new_titles.csv`: 17 referências, uma por chave de obra/site, com localizador, base da data, URL e categoria.
- `data/revision4_summary.json`: resultados e declaração de seleção não exaustiva.
- `scripts/revision4_acquire.py`: repetição das aquisições não vazias e bem-sucedidas registradas no manifesto.
- `scripts/revision4_build.py`: geração da seleção codificada, tabela LaTeX, bibliografia e dois acréscimos ao núcleo.

Reconstrução com os arquivos locais adquiridos: executar `revision4_build.py`, depois `build_appendices.py`, compilar `artigo/main.tex` e executar `validate.py`. A compilação direta usa as tabelas públicas já geradas e não depende dos PDFs locais. Os fac-símiles e o HTML integral permanecem locais; URLs, localizadores e SHA-256 são públicos.

O ano de 2017 é o extremo da seleção executada, não o limite de existência das bases. Não houve censo de toda a Brasiliana nem de toda a web preservada até 2026. A quantidade de títulos decorre desta seleção dirigida e não de uma fórmula de precisão estatística. Os exemplos não demonstram transmissão de `quiá` para `kkkk`, origem absoluta das grafias ou representatividade dos espaços digitais.
