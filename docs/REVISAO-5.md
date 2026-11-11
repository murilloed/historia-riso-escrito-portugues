# Consolidação metodológica e inventário de bases

**Relatório histórico de etapa.** As contagens e pendências abaixo pertencem à etapa descrita. Para os resultados vigentes, consulte o [balanço reconciliado](../data/consolidated_inventory.json), a [matriz](../data/archive_decade_matrix.csv) e a [metodologia](METODOLOGIA.md).

Autor único: Murillo Edson de Carvalho Souza. Data: 8 de novembro de 2026.

A conferência identificou que as fontes estavam registradas de maneira dispersa e que `docs/METODOLOGIA.md` ainda descrevia a primeira versão, com 15 registros e 34 aquisições. O documento foi atualizado, e a metodologia do artigo ganhou dois quadros com hiperlinks diretos para os arquivos no GitHub.

## Instrumentos novos

- [base_registry.csv](../data/base_registry.csv): todos os 16 endereços indicados pelo autor, com URL indicada, URL de acesso, vínculos entre portais/coleções/itens, quantidade selecionada e arquivo de dados correspondente.
- [method_quantification.csv](../data/method_quantification.csv): 15 indicadores com quantidade, unidade, escopo e hiperlink para os dados.
- [source_domains.csv](../data/source_domains.csv): todos os 53 domínios encontrados nas 293 entradas do manifesto histórico. Domínios técnicos não são apresentados como bases independentes. A referência retirada permanece apenas no histórico de aquisição, sem voltar à bibliografia do artigo.
- [method_inventory_summary.json](../data/method_inventory_summary.json): contagens consolidadas, com a declaração de que não são aditivas.
- [build_method_inventory.py](../scripts/build_method_inventory.py): geração a partir dos dados públicos; incluída na reconstrução das tabelas e na compilação automática.

## Unidades que não se confundem

O núcleo tem 25 testemunhos (E1=14, E2=8, E3=3). A auditoria inicial abrange 66 indicações e 22 citações alegadas. A seleção por acervo/década contém 29 referências; a seleção de títulos inéditos contém 17. Parte dessas fontes também está no núcleo. Não se anuncia a soma desses conjuntos como total de obras independentes.

O manifesto tem 293 entradas: 276 com conteúdo, duas respostas vazias e 15 falhas. Inclui PDFs, imagens, HTML, JSON, código de interface e apoio bibliográfico. O estado `downloaded` aparece em 278 entradas porque inclui as duas vazias. Nenhuma dessas contagens equivale à leitura integral de todas as obras, a resultados positivos de riso ou ao total de requisições realizadas em toda a pesquisa.

Os 16 endereços também não são 16 bases independentes. H08/H13 são portal e item do APESP; H12/H14 são coleção e acervo geral da BBM; H15 é conteúdo do Orkut preservado no serviço Wayback, H16. O quadro explicita essas sobreposições e preserva as pendências documentais.

Foram acrescentadas entradas bibliográficas próprias para o acervo geral da BBM e o portal Wayback. Os demais recursos reutilizam as referências já existentes, sem duplicação. O plano estatístico continua prospectivo, e a coleta continua dirigida e não probabilística.

## Validação

A validação verifica a presença dos 16 identificadores, a reconciliação das entradas do manifesto, os arquivos de destino dos hiperlinks e as anotações de hiperlink no PDF. O inventário usa links para a versão corrente do repositório; a reprodução histórica deve identificar a versão ou o commit consultado.
