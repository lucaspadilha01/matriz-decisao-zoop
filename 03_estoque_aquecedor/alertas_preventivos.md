# Aula 3.3 · Alertas preventivos e ações proativas (estoque de aquecedores)

**Objetivo:** avisar a Zoop antes de um novo acúmulo de estoque de aquecedores, com uma ação proativa para cada alerta.
**Base:** indicadores e ata de 28/08/2024 (Notion), causas e ações das Aulas [3.1](analise_causas.md) e [3.2](acoes_corretivas.md), e as vendas diárias do aquecedor (jan/2022 a ago/2024) para calibrar os limites. O plano de execução está em [planejamento_aula_3_3.md](planejamento_aula_3_3.md) e o painel em [painel_alertas.csv](painel_alertas.csv).

## 1. Limites do Notion reconciliados (passo 1)

| Indicador | Conflito no Notion | Decisão adotada |
|---|---|---|
| Variação de vendas | A ata cita −10% contra o trimestre anterior e depois −15% contra o ano anterior | Média móvel de 3 meses contra o mesmo período do ano anterior: atenção em −10% e crítico em −15% |
| Lead time | Limite "superior a 90 dias", mas o valor atual já é 90; a ata fala em mais de 5 dias de atraso | Atenção a partir de 90 dias; crítico com atraso de mais de 5 dias sobre o prazo contratado |
| Capacidade de armazenagem | Limite de 85% sobre a capacidade, valor atual de "35% acima da capacidade ideal" (bases diferentes) | Ocupação sobre a capacidade total: atenção acima de 75%, crítico acima de 85%. Hoje consideramos o indicador crítico, supondo que "ideal" equivale a 100% |
| Conversão | Limite de 8% (absoluto), valor atual "12% abaixo da meta" (relativo) | Atenção abaixo de 10% e crítico abaixo de 8%. O valor atual fica "a validar", porque a meta não foi informada |

## 2. Etapa 1 · Tabela consolidada de indicadores

Cada indicador tem dois limites: **atenção** (amarelo) e **crítico** (vermelho).

| Indicador | Descrição | Valor atual | Atenção | Crítico | Origem e status hoje |
|---|---|---|---|---|---|
| Capacidade de armazenagem | % do armazém ocupado pelos aquecedores | 35% acima da capacidade ideal | > 75% | > 85% | Caso. **Crítico** |
| Lead time de fornecedores | Tempo de reposição | 90 dias | ≥ 90 dias | Atraso > 5 dias sobre o prazo | Caso. **Atenção** (no limite) |
| Conversão de campanhas | % de conversão das campanhas | 12% abaixo da meta | < 10% | < 8% | Caso. **A validar** |
| Rotatividade de estoque | % do estoque que sai por mês | Sem valor | < 20% ao mês | < 10% ao mês | Sem dado |
| Variação de vendas (3 meses) | Vendas contra o mesmo período do ano anterior | −3,3% (jun-ago/2024 contra 2023) | ≤ −10% | ≤ −15% | Dados de vendas. **Verde** |
| Erro de previsão (superestimativa, 3 meses) | Quanto a previsão passou das vendas | 25% de superestimativa | > 15% | > 20% | Caso. **Crítico** |
| Satisfação: reclamações por falta de produto | % de reclamações sobre ruptura | Sem valor | > 3% | > 5% | Sem dado |
| Custo de armazenagem | Aumento do custo por excesso de estoque | +20% em 3 meses | > 5% | > 10% | Caso. **Crítico** |
| **Cobertura de estoque** (novo) | Semanas de venda que o estoque sustenta | Sem valor | > 10 semanas | > 14 semanas | Sem dado |
| **Pedido para o pico vs demanda esperada** (novo) | Unidades pedidas para jun-ago contra a demanda esperada | Sem valor (pico de 2024: 2.378 un.) | > 105% | > 115% | Sem dado |
| **Participação do e-commerce** (novo) | Peso do online nas vendas do aquecedor | 55,3% (jun-ago/2024), +9 p.p. sobre 2023 | Queda ≥ 7 p.p. | Queda ≥ 12 p.p. | Dados de vendas. **Verde** |

**Leitura do estado de hoje:** três indicadores críticos vêm do caso (armazenagem, erro de previsão e custo de armazenagem) e o lead time está em atenção, no limite. **As vendas do aquecedor não caíram** (−3,3% no pico de 2024), o que confirma que o excesso vem de **compra acima da demanda**, e não de colapso de vendas.

**Por que os indicadores novos:**
- **Cobertura de estoque:** mede o excesso em semanas de venda, o que o percentual de armazém não mostra. Com o ritmo de set a nov (cerca de 11,5 un./dia), 10 semanas são cerca de 800 unidades e 14 semanas cerca de 1.130. Em maio, a cobertura deve ser medida sobre os próximos 90 dias, para cobrir o pico.
- **Pedido vs demanda do pico:** age antes do problema, na hora de comprar. O pico caiu 10,02% em dois anos e a superestimativa verificável é de cerca de 11%.
- **Participação do e-commerce:** acompanha o canal que o caso e os dados contradizem (ação A4).

## 3. Calibração com o histórico (passo 4)

Cada regra foi simulada nos meses da base de vendas do aquecedor, para saber quantas vezes teria disparado:

| Regra testada | Meses avaliados | Disparos | Conclusão |
|---|---:|---:|---|
| Queda de vendas **mensal** contra o ano anterior ≤ −10% | 20 | 7 (35%) | Alerta demais |
| Queda de vendas **mensal** contra o ano anterior ≤ −15% | 20 | 5 (25%) | Alerta demais |
| Queda de vendas **3 meses** ≤ −10% | 18 | 3 (17%) | **Adotada** como atenção |
| Queda de vendas **3 meses** ≤ −15% | 18 | 2 (11%) | **Adotada** como crítico |
| Erro de previsão **mensal** acima de 20% (qualquer sentido) | 17 | 7 (41%) | Alerta demais |
| Superestimativa de **3 meses** > 15% | 15 | 3 (20%) | **Adotada** como atenção |
| Superestimativa de **3 meses** > 20% | 15 | 1 (7%) | **Adotada** como crítico (limite do Notion) |
| Queda da participação online ≥ 7 p.p. (3 meses, contra o ano anterior) | 18 | 1 (6%) | **Adotada** como atenção |
| Queda da participação online ≥ 12 p.p. | 18 | 0 | **Adotada** como crítico |

**Como a previsão foi simulada:** vendas do mesmo mês do ano anterior, ajustadas pela tendência dos 3 meses anteriores. É um método simples, só para medir o ruído da demanda mensal (erro mediano de 17,4% por mês e de 8,0% em 3 meses). **Não é o modelo de previsão da Zoop.**

**Conclusão da calibração:** a demanda mensal do aquecedor é muito ruidosa, então alertas baseados em um único mês perdem credibilidade. A média de 3 meses reduz os disparos para 7% a 20% dos meses e ainda captura os episódios relevantes (set/2023, jan/2024 e jun/2024).

Limites sem dado para calibrar (armazenagem, lead time, conversão, rotatividade, satisfação, custo, cobertura e pedido para o pico) seguem o Notion ou são propostas, e devem ser revisados após 2 a 3 meses de operação.

## 4. Etapa 2 · Alertas e ações proativas

Ações no estilo **Lean** (eliminar excesso) e **Just-in-Time** (comprar perto da demanda). A coluna de ação mostra primeiro a resposta ao nível de atenção e depois ao nível crítico.

| Alerta (atenção → crítico) | Ação proativa | Impacto estimado | Prioridade |
|---|---|---|---|
| **Armazenagem** > 75% → > 85% | Atenção: suspender novos pedidos do item. Crítico: redistribuir estoque entre lojas e centros e acionar a campanha de desova (A1, A3, A2) | Financeiro: reduz o custo de armazenagem (+20% em 3 meses). Operacional: libera espaço, hoje 35% acima do ideal | **Alta** |
| **Lead time** ≥ 90 dias → atraso > 5 dias | Atenção: antecipar a data do pedido do próximo lote. Crítico: ajustar ou fracionar os pedidos e acionar fornecedor alternativo (A6, A10) | Operacional: flexibilidade do inventário. Financeiro: menos risco de pedido grande antecipado | **Alta** |
| **Erro de previsão** (superestimativa) > 15% → > 20% | Atenção: revisar a previsão e reduzir o próximo lote. Crítico: congelar a reposição até a cobertura voltar ao alvo e reunir Logística e Comercial (A1, A5, A8) | Financeiro: evita R$ 685 mil a R$ 1,54 milhão de estoque excedente por ciclo (ao preço de venda) | **Alta** |
| **Pedido para o pico** > 105% → > 115% | Atenção: rever o pedido com a previsão sazonal. Crítico: cortar o pedido ao nível da demanda esperada antes de fechar (A5, A6) | Financeiro: age antes de o estoque existir, evitando o custo de armazenagem | **Alta** |
| **Cobertura de estoque** > 10 → > 14 semanas | Atenção: suspender reposição. Crítico: campanha de desova no e-commerce e redistribuição (A1, A2, A3) | Operacional: reduz o capital parado; marketing: campanha direcionada | **Alta** |
| **Rotatividade** < 20% → < 10% ao mês | Atenção: ajustar compras ao ritmo real. Crítico: desova com desconto escalonado e limite de estoque (A2) | Financeiro: converte estoque parado em caixa | **Alta** |
| **Custo de armazenagem** > 5% → > 10% | Atenção: renegociar custo ou mover produtos entre armazéns. Crítico: desova e revisão do contrato (A3, A2) | Financeiro: a ata projeta até +15% de custo nos próximos dois trimestres sem ação (projeção do caso, não verificável) | **Alta** |
| **Variação de vendas (3 meses)** ≤ −10% → ≤ −15% | Atenção: checar se é sazonalidade ou mudança real. Crítico: reduzir pedidos e revisar campanhas (A5, A7) | Marketing: campanhas ajustadas; financeiro: evita compra acima da demanda | **Alta** |
| **Conversão de campanhas** < 10% → < 8% | Atenção: rever o público-alvo. Crítico: mover a verba para o período certo do produto (jun-ago) (A7) | Marketing: eleva a taxa de conversão (12% abaixo da meta) | **Média** |
| **Participação do e-commerce** queda ≥ 7 p.p. → ≥ 12 p.p. | Atenção: auditar o canal (A4). Crítico: reforçar a campanha online e revisar preço | Marketing: protege o canal que mais cresce no aquecedor | **Média** |
| **Reclamações por falta de produto** > 3% → > 5% | Atenção: revisar a cobertura mínima. Crítico: priorizar a reposição dos itens em falta | Marketing: protege a satisfação; evita o excesso oposto (ruptura) | **Média** |

A ata prevê redução de até 10% nos custos de armazenagem no curto prazo e de até 30% no tempo de resposta com IA. São estimativas do caso e não foram verificadas.

## 5. Calendário sazonal de monitoramento

Média diária de venda do aquecedor por mês (média de 2022 e 2023), para dimensionar a cobertura e ler os alertas:

| Período | Ritmo esperado (un./dia) | Foco do monitoramento |
|---|---:|---|
| **Mar a mai** (vale, fase de compras) | 10,42 (mar), 9,83 (abr), 10,13 (mai) | **Pedido para o pico**, lead time e previsão. Em maio, cobertura medida sobre os próximos 90 dias |
| **Jun a ago** (pico) | 28,73 (jun), 27,29 (jul), 27,18 (ago) | Vendas contra o esperado, ruptura (reclamações) e conversão das campanhas |
| **Set a nov** (vale, fase de desova) | 11,52 (set), 11,69 (out), 11,32 (nov) | **Cobertura, rotatividade, armazenagem e custo**; desova |
| **Dez a fev** (segunda janela) | 18,90 (dez), 18,24 (jan), 18,73 (fev) | Cobertura e erro de previsão; segunda janela de venda |

**Frequência:** indicadores de estoque e cobertura, semanais; vendas, previsão, custo e canal, mensais; lead time, a cada pedido.

## 6. Como alimentar o sistema

| Dado | Fonte necessária | Quem fornece |
|---|---|---|
| Estoque diário e ocupação do armazém | ERP e Logística | Logística |
| Pedidos e prazos efetivos de entrega | Compras | Logística |
| Conversão e meta das campanhas | Ferramentas de marketing | Marketing |
| Custo de armazenagem | Financeiro | Finanças |
| Reclamações por ruptura | Atendimento | Atendimento |
| Vendas diárias por canal | Base de vendas (já disponível) | Comercial / TI |

**Limites:** com apenas 2 anos e 8 meses de histórico, a calibração é indicativa. Sem estoque, pedidos, conversão e custos na base, nove dos onze indicadores ainda dependem de dados de fora. Revisar os limites depois de 2 a 3 meses de uso.
