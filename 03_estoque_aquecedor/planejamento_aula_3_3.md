# Planejamento · Aula 3.3: alertas preventivos e ações proativas

**Objetivo:** criar um sistema de alertas que avise a Zoop **antes** de um novo acúmulo de estoque de aquecedores, com uma ação proativa para cada alerta. Esta aula materializa a ação A9 (painel e alertas) e parte das ações A5 e A8 da [Aula 3.2](acoes_corretivas.md).

**Como a aula funciona (Notion):** dois prompts em sequência.
1. **Etapa 1, consolidação:** tabela com *Indicador, Descrição, Valor Atual, Limite de Alerta*.
2. **Etapa 2, alertas:** tabela com *Alerta, Ação Proativa, Impacto Estimado, Prioridade (Alta, Média, Baixa)*, usando Lean, Just-in-Time e análise preditiva.

## 1. Entradas já disponíveis

| Entrada | Origem |
|---|---|
| Ata de 28/08/2024 (limites discutidos) | Notion, Aula 3.3 |
| Tabela de 8 indicadores com limite de alerta | Notion, Aula 3.3 |
| Valores atuais (armazenagem +35%, lead time 90 dias, erro de previsão 25%, online −15%, conversão 12% abaixo da meta, custo +20%) | Notion, Aula 3.1 |
| Causas e ações corretivas (I1 a I7, E1 a E4, A1 a A10) | [analise_causas.md](analise_causas.md) e [acoes_corretivas.md](acoes_corretivas.md) |
| Vendas diárias do aquecedor (jan/2022 a ago/2024) | `Zoop - Dados Vendas.xlsx` |

## 2. Achados prévios que mudam o desenho dos alertas

1. **Limites do Notion são inconsistentes entre si:**
   - Vendas em queda: a ata cita "−10% contra o trimestre anterior" e depois "−15% contra o mesmo período do ano anterior", e a tabela só traz os −15%.
   - Lead time: o limite é "superior a 90 dias", mas o valor atual já é 90; a ata fala em "mais de 5 dias" acima do prazo.
   - Armazenagem: o limite é "acima de 85% da capacidade", mas o valor atual é "35% acima da capacidade ideal" (base de comparação diferente).
2. **Alerta mensal de −15% dispara muito:** aplicado ao histórico do aquecedor (20 meses comparáveis), **5 meses teriam alertado** (25%): ago/2023 (−17,8%), set/2023 (−19,6%), nov/2023 (−28,5%), jan/2024 (−19,4%) e jun/2024 (−21,4%). Com **média móvel de 3 meses** são 2 de 18 meses (11%). O alerta precisa ser calibrado para não perder credibilidade.
3. **Indicadores precisam ser sazonais:** "rotatividade menor que 10% ao mês" sempre dispararia no vale (set a mai). O limite deve variar com o índice sazonal do mês.
4. **O erro de previsão atual (25%) já está acima do limite (20%)**, então esse alerta nasce ligado.
5. **Divergência de canal:** o caso diz online −15%, a base mostra e-commerce +15,4% no aquecedor. O alerta de canal só vale depois da auditoria (A4).

## 3. Passos de execução

| # | Passo | Resultado |
|---|---|---|
| 1 | **Reconciliar os limites** (achado 1): definir um limite único por indicador e registrar a decisão | Tabela de limites oficial |
| 2 | **Etapa 1, consolidar indicadores:** montar a tabela com os 8 indicadores do Notion, preencher *Valor Atual* (caso ou dados) e marcar a origem de cada valor | Tabela consolidada |
| 3 | **Acrescentar indicadores novos** com valor verificável nos dados: cobertura de estoque em semanas, vendas contra o índice sazonal esperado, erro de previsão por mês (backtest) e participação do e-commerce | 4 a 5 indicadores adicionais |
| 4 | **Calibrar os limites com o histórico** (achados 2 e 3): simular cada regra nos 20 meses de dados, medir quantos alertas teria gerado e ajustar (média móvel, comparação com a mesma estação) | Limites com taxa de falso alarme conhecida |
| 5 | **Dois níveis de alerta:** atenção (amarelo) e crítico (vermelho), com dono e frequência de checagem | Escala de severidade |
| 6 | **Etapa 2, alertas e ações proativas:** para cada alerta, definir ação (Lean e Just-in-Time), impacto (financeiro, operacional, marketing) e prioridade, ligando às ações A1 a A10 | Tabela de alertas |
| 7 | **Calendário sazonal de monitoramento:** o que checar em mar-mai (compras), jun-ago (pico), set-nov (desova) e dez-fev (segunda janela) | Rotina anual |
| 8 | **Documentar, linkar no README e fazer commit** | `alertas_preventivos.md` |

## 4. Entregáveis

- `03_estoque_aquecedor/alertas_preventivos.md`: tabela consolidada, limites calibrados, tabela de alertas e ações, calendário sazonal e limites do método.
- (Opcional) `03_estoque_aquecedor/painel_alertas.csv`: indicadores com limites, para importar em Excel ou Power BI.
- README atualizado e commit local.

## 5. Decisões em aberto (com a minha sugestão)

| Decisão | Sugestão |
|---|---|
| Qual regra de queda de vendas vale? | Média móvel de 3 meses contra o mesmo período do ano anterior, alerta amarelo em −10% e vermelho em −15% |
| Lead time: qual limite? | Amarelo acima de 90 dias, vermelho com atraso de mais de 5 dias sobre o prazo contratado |
| Armazenagem: qual base? | Ocupação sobre a capacidade total: amarelo acima de 75% e vermelho acima de 85% |
| Limites sazonais? | Sim: rotatividade e cobertura de estoque ajustadas ao índice sazonal do mês |
| Incluir o painel em CSV? | Sim, é barato e permite uso no Power BI |

## 6. Riscos e limites

- **Sem dados de estoque, pedidos, conversão e custos**, só dá para calibrar com dados os alertas de **vendas, sazonalidade, previsão e canal**. Os demais usam os valores do caso e precisam ser alimentados por ERP ou logística.
- **Histórico curto** (2 anos e 8 meses): a calibração é indicativa.
- **Alerta demais vira ruído**, por isso a calibração com o histórico (passo 4) é obrigatória.

## 7. Critérios de aceite

- Todos os 8 indicadores do Notion estão na tabela, com valor atual e origem.
- Cada alerta tem ação proativa, impacto e prioridade.
- Todo limite calibrado tem o número de disparos no histórico.
- Conflitos de limite do Notion estão resolvidos e registrados.
