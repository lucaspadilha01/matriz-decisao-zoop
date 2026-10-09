# Aula 3.2 · Ações corretivas e priorização (estoque de aquecedores)

**Ponto de partida:** as causas mapeadas na [Aula 3.1](analise_causas.md). Aqui proponho ações para cada uma e priorizo com a **Matriz GUT** (Gravidade, Urgência e Tendência, notas de 1 a 5) e com **Esforço × Impacto**. As ações seguem princípios **Lean** (eliminar excesso) e **Just-in-Time** (comprar perto da demanda).

**Dados usados:** `Zoop - Dados Vendas.xlsx` (aquecedor, jan/2022 a ago/2024) e os indicadores do caso. A base não tem o tamanho do estoque, pedidos nem custos, então os impactos financeiros são **ordens de grandeza**, não previsões.

## 1. Fatos que orientam as ações

- **A janela de venda está fechando.** A média diária cai de 29,84 (ago/2022) para 12,77 (set/2022), e de 24,52 para 10,27 em 2023: **cerca de −57% de agosto para setembro**. Depois, de set a nov, o ritmo fica em cerca de 11,5 unidades por dia.
- **Há uma segunda janela de demanda de dez a fev:** cerca de 18,5 unidades por dia em jan e fev, e 18 a 20 em dezembro (índice de dezembro de 1,12), bem acima do vale de mar a mai (cerca de 10).
- **Tamanho do excesso (ordens de grandeza):** o pico de jun-ago/2024 vendeu 2.378 unidades. Se a superestimativa foi de 11,1% (limite sustentado pelos dados), o excesso é de cerca de **264 unidades, ou R$ 685 mil** ao preço de venda (R$ 2.596). Se foi de 25% (valor do caso), são cerca de **595 unidades, ou R$ 1,54 milhão**.
- **Quanto tempo o excesso leva para sair sozinho:** sem novos pedidos, ao ritmo de 11,5 unidades por dia (set a nov), 264 unidades levam cerca de 23 dias e 595 levam cerca de 52 dias. Ou seja, **parar de repor** já resolve boa parte do problema.

## 2. Ações corretivas propostas

| ID | Ação | Causa(s) atacada(s) | Prazo |
|---|---|---|---|
| A1 | **Congelar a reposição de aquecedores** até a cobertura de estoque cair ao nível-alvo (por exemplo, 8 a 10 semanas de venda no ritmo do período) | I1, I2, I7 | Imediato |
| A2 | **Campanha de desova de fim de temporada**, segmentada e focada no e-commerce (que cresce 15,4% no aquecedor), com desconto escalonado e limite de estoque | I3, I4, I7 | Imediato (a janela cai 57% em setembro) |
| A3 | **Redistribuir estoque** entre lojas e centros e, se necessário, renegociar o custo de armazenagem temporária | I7 | Curto prazo |
| A4 | **Auditar os indicadores de canal:** o caso diz online −15%, a base mostra e-commerce +15,4% e loja −19,3% no aquecedor. Reconciliar as fontes antes de decidir investimento por canal | E3 | Curto prazo |
| A5 | **Novo modelo de previsão sazonal por mês**, com histórico atualizado e tendência (a base mostra pico em queda de 10,02% em dois anos) | I1, I2, E2 | Médio prazo (antes do próximo ciclo de compras) |
| A6 | **Compras fracionadas e ancoradas no lead time de 90 dias:** lotes menores (por exemplo, março e maio) com a segunda parcela ajustada pelo ritmo real de mar a mai (Just-in-Time) | E1 | Médio prazo |
| A7 | **Calendário de marketing alinhado à sazonalidade:** campanhas de aquecedor em mai (pré-inverno) e jun a ago, com a verba de nov a jan reduzida para esse produto | I3, I4 | Médio prazo |
| A8 | **Rotina mensal Logística + Comercial (S&OP)** com uma única previsão de demanda e um único responsável por revisão | I5 | Médio prazo |
| A9 | **Painel de monitoramento em tempo real** (estoque, cobertura, vendas contra previsão), com alertas | I6 | Médio prazo (detalhado na Aula 3.3) |
| A10 | **Renegociar com fornecedores** prazo de entrega, lotes mínimos e flexibilidade de cancelamento | E1 | Médio a longo prazo |

## 3. Impactos esperados

| ID | Impacto financeiro | Impacto operacional | Impacto em marketing |
|---|---|---|---|
| A1 | Evita novo capital parado e custo de armazenagem; sem compra, o excesso de 264 a 595 unidades sai em cerca de 23 a 52 dias | Libera espaço (hoje 35% acima do ideal) | Neutro |
| A2 | Converte estoque parado (R$ 685 mil a R$ 1,54 milhão ao preço de venda) em caixa, ao custo do desconto | Libera espaço mais rápido | Alto: campanha direcionada recupera a conversão (12% abaixo da meta) |
| A3 | Reduz o custo de armazenagem (+20% em 3 meses) | Melhor uso dos pontos de venda | Neutro |
| A4 | Evita investir no canal errado | Decisões baseadas em dados consistentes | Médio: define onde concentrar campanha |
| A5 | Evita repetir a superestimativa de 11% a 25% (R$ 685 mil a R$ 1,54 milhão por ciclo) | Planejamento de compras mais estável | Neutro |
| A6 | Reduz o risco de excesso por pedido grande antecipado | Mais flexibilidade e menos estoque parado | Neutro |
| A7 | Aumenta venda no pico sem depender de desconto | Demanda alinhada ao estoque | Alto: campanhas no momento certo |
| A8 | Reduz erros de previsão entre áreas | Processo único, menos retrabalho | Médio |
| A9 | Detecta desvios cedo, antes do custo subir | Resposta mais rápida | Médio |
| A10 | Reduz risco e custo de estoque a longo prazo | Prazos mais curtos | Neutro |

## 4. Priorização com a Matriz GUT

GUT = Gravidade × Urgência × Tendência (cada nota de 1 a 5, máximo de 125).

| ID | Gravidade | Urgência | Tendência | **GUT** | Justificativa das notas |
|---|---:|---:|---:|---:|---|
| A1 | 5 | 5 | 4 | **100** | O estoque e o custo crescem enquanto houver reposição; a janela de venda cai |
| A5 | 5 | 4 | 5 | **100** | Sem previsão sazonal o erro se repete em todo ciclo, e o pico segue em queda |
| A2 | 4 | 5 | 4 | **80** | A demanda cai cerca de 57% em setembro; cada semana de espera custa |
| A8 | 4 | 3 | 5 | **60** | Sem integração, as previsões voltam a divergir |
| A9 | 4 | 3 | 5 | **60** | Sem alertas, o problema volta a aparecer tarde |
| A6 | 4 | 3 | 4 | **48** | Lead time alto é permanente, mas só pesa no próximo ciclo |
| A7 | 4 | 3 | 4 | **48** | Efeito no próximo inverno |
| A3 | 3 | 4 | 3 | **36** | Alivia o custo, mas não ataca a causa |
| A4 | 3 | 4 | 3 | **36** | Evita decisão errada de canal; ajuda a calibrar A2 |
| A10 | 4 | 2 | 4 | **32** | Efeito lento, dependente do fornecedor |

## 5. Matriz Esforço × Impacto

| Quadrante | Ações | Observação |
|---|---|---|
| **Ganhos rápidos** (baixo esforço, alto impacto) | A1, A2, A4 | Executar já |
| **Projetos estratégicos** (alto esforço, alto impacto) | A5, A6, A7, A9 | Planejar antes do próximo ciclo de compras |
| **Apoio** (baixo esforço, impacto médio) | A3, A8 | Fazer em paralelo |
| **Longo prazo** (alto esforço, impacto médio) | A10 | Iniciar a conversa agora |

## 6. Lista final de ações priorizadas

| Ação proposta | Impacto financeiro | Impacto operacional | Impacto de marketing | GUT | Quadrante | **Prioridade** |
|---|---|---|---|---:|---|---|
| A1 · Congelar reposição de aquecedores | Evita novo capital parado e custo de armazenagem | Libera espaço | Neutro | 100 | Ganho rápido | **Alta** |
| A5 · Modelo de previsão sazonal por mês | Evita R$ 685 mil a R$ 1,54 milhão por ciclo | Planejamento estável | Neutro | 100 | Estratégico | **Alta** |
| A2 · Campanha de desova de fim de temporada (e-commerce) | Converte estoque em caixa | Libera espaço | Alto | 80 | Ganho rápido | **Alta** |
| A8 · S&OP mensal Logística + Comercial | Menos erro de previsão | Processo único | Médio | 60 | Apoio | **Média** |
| A9 · Painel e alertas em tempo real | Detecta desvios cedo | Resposta rápida | Médio | 60 | Estratégico | **Média** |
| A4 · Auditar indicadores de canal | Evita investir no canal errado | Dados consistentes | Médio | 36 | Ganho rápido | **Média** (subiu por ser barata e calibrar a A2) |
| A6 · Compras fracionadas (JIT) | Menos risco de excesso | Mais flexibilidade | Neutro | 48 | Estratégico | **Média** |
| A7 · Calendário de marketing sazonal | Mais venda no pico | Demanda alinhada | Alto | 48 | Estratégico | **Média** |
| A3 · Redistribuir estoque | Reduz custo de armazenagem | Melhor uso das lojas | Neutro | 36 | Apoio | **Baixa** |
| A10 · Renegociar com fornecedores | Menor risco a longo prazo | Prazos mais curtos | Neutro | 32 | Longo prazo | **Baixa** |

## 7. Observações e limites

- **A desova (A2) e a decisão de dezembro:** a segunda janela de demanda (dez a fev) existe nos dados, mas, na análise de dezembro, decidimos **não** dar desconto no aquecedor. Aqui a lógica é outra: desova de excesso, e não atrair público. Se preferirem manter o aquecedor fora de promoções em dezembro, a campanha deve ficar em **fim de agosto e setembro**, no e-commerce.
- **Estoque real:** os cálculos de 264 e 595 unidades são hipóteses a partir do erro de previsão. O volume real em estoque precisa vir do ERP para dimensionar A1 e A2.
- **Custos:** a base não traz margem nem custo de armazenagem, então os impactos financeiros usam o preço de venda e são ordens de grandeza.
- **Notas GUT** são julgamento técnico e devem ser revisadas com as áreas envolvidas.

> **Próximo passo (Aula 3.3):** transformar o monitoramento (A9) em um sistema de alertas preventivos com limites e ações proativas.
