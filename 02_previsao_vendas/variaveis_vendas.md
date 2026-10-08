# Aula 2.1: Variáveis que influenciam as vendas da Zoop Megastore

**Produtos:** Aquecedor, Ar Condicionado, Cafeteira, Câmera Fotográfica, Celular, Cobertor Elétrico, Notebook, Smart TV 55", Smartphone, Smartwatch, Tablet.
**Segmento:** varejo de eletroeletrônicos, eletrodomésticos e climatização, com sazonalidade climática e ciclo de lançamentos tecnológicos.

## Variáveis internas

| ID | Variável | Descrição | Como medir | Exemplos de métricas |
|---|---|---|---|---|
| 1 | **Preço dos produtos** | O preço define a demanda, e a sensibilidade varia por categoria: Smart TV, notebook e ar-condicionado são muito sensíveis; cafeteira e smartwatch, menos. | Compare variações de preço com variações de quantidade vendida no mesmo SKU. Calcule a elasticidade-preço: `E = (ΔQ/Q) / (ΔP/P)`. Ajuste uma regressão log-log `ln(Q) = a + b·ln(P)`; o coeficiente `b` é a elasticidade. | Elasticidade por SKU; margem de contribuição (preço − custos variáveis); preço médio praticado × preço de tabela. |
| 2 | **Promoções e descontos** | Campanhas elevam as vendas no curto prazo, mas podem antecipar compras e corroer a margem. | Marque os dias de campanha com uma variável *dummy* (1 = campanha) e compare com a linha de base (média das mesmas semanas sem campanha). | Lift = (vendas na campanha − baseline) / baseline; ROI da promoção; % de vendas com desconto; queda de vendas pós-campanha (*pull-forward*). |
| 3 | **Canais de venda** | Loja física, e-commerce, marketplace e app têm perfis de cliente, ticket e conversão diferentes. | Segmente as vendas por canal e compare a evolução ao longo do tempo. Use UTM e relatórios do ERP/PDV. | Participação (share) por canal; taxa de conversão por canal; ticket médio por canal; custo de aquisição por canal. |
| 4 | **Qualidade percebida do produto** | Notas e avaliações influenciam a decisão de compra e a taxa de devolução, principalmente em itens de alto valor. | Colete notas e comentários das redes sociais e dos marketplaces. Use análise de sentimento e correlacione com as vendas defasadas em 1 a 4 semanas. | Nota média; NPS; % de avaliações negativas; taxa de devolução e de acionamento de garantia. |
| 5 | **Disponibilidade de estoque** | Ruptura limita as vendas (venda perdida), e excesso gera custo de armazenagem e liquidação. | Cruze o estoque diário com a demanda. Conte os dias com estoque zero e estime a demanda não atendida. | Taxa de ruptura = dias sem estoque / dias totais; cobertura de estoque (dias); giro = CMV / estoque médio; venda perdida estimada. |
| 6 | **Mix e posicionamento de produto** | A presença de itens de entrada, intermediários e premium muda o ticket e o canibaliza entre modelos. | Analise a participação de cada SKU no faturamento (curva ABC) e a canibalização entre modelos semelhantes. | Curva ABC; ticket médio; margem por categoria; % de vendas por faixa de preço. |
| 7 | **Condições de pagamento e financiamento** | Parcelamento sem juros e crédito viabilizam a compra de itens de alto valor (notebook, TV, ar-condicionado). | Compare vendas por forma de pagamento e número de parcelas. Teste o efeito de mudar a oferta de parcelamento. | % de vendas parceladas; parcelas médias; taxa de aprovação de crédito; ticket médio por forma de pagamento. |
| 8 | **Engajamento de clientes** | Interações com a marca (redes sociais, e-mail, app, WhatsApp) geram tráfego e recompra. | Use relatórios das plataformas e do CRM e correlacione as interações com as vendas dos dias seguintes. | CTR de e-mail; engajamento em redes; tráfego do site; taxa de recompra; LTV = ticket médio × frequência × tempo de relacionamento. |
| 9 | **Investimento em marketing e mídia paga** | A verba e o mix de mídia explicam parte da demanda e do tráfego. | Atribua vendas às campanhas (Google Analytics, painel de mídia). Rode uma regressão do investimento defasado sobre as vendas. | CAC; ROAS = receita / investimento; custo por clique; custo por venda. |
| 10 | **Experiência de compra e atendimento** | Prazo de entrega, frete, atendimento e facilidade do site afetam a conversão e a recompra. | Monitore o funil (visita → carrinho → compra) e os prazos de entrega. | Taxa de conversão; abandono de carrinho; prazo médio de entrega; frete médio; CSAT; tempo de resposta. |

## Variáveis externas

| ID | Variável | Descrição | Como medir | Exemplos de métricas |
|---|---|---|---|---|
| 11 | **Sazonalidade e calendário** | Datas comerciais (Black Friday, Natal, Dia das Mães, Dia dos Pais, Dia do Consumidor), pagamento de salários e dia da semana mudam o volume. | Decomponha a série histórica (tendência, sazonalidade, ruído) e calcule índices sazonais por mês e por dia da semana. | Índice sazonal = média do mês / média anual; vendas por dia da semana; crescimento ano contra ano (YoY). |
| 12 | **Clima e temperatura** | É a variável mais forte para aquecedor, cobertor elétrico e ar-condicionado: frio puxa os dois primeiros, calor puxa o terceiro. | Cruze a temperatura média e mínima regional (INMET) com as vendas diárias, em regressão com defasagem de 0 a 7 dias. | Correlação temperatura × vendas; vendas por faixa de temperatura; vendas após a primeira frente fria ou onda de calor. |
| 13 | **Concorrência** | Preço, promoções e lançamentos de concorrentes e de marketplaces deslocam a demanda. | Monitore preços (*web scraping* ou ferramentas de comparação) e calcule a diferença de preço em relação aos concorrentes. | Índice de preço relativo = nosso preço / preço do concorrente; share of shelf; participação de mercado. |
| 14 | **Lançamentos e ciclo tecnológico** | Novos modelos de smartphone, notebook, smartwatch e TV tornam os anteriores obsoletos e geram picos de demanda e liquidação. | Mapeie o calendário de lançamentos e acompanhe a curva de vida do produto. | Dias desde o lançamento do modelo; queda de vendas do modelo anterior; tempo de desvalorização do estoque. |
| 15 | **Macroeconomia** | Renda, desemprego, juros, inflação e câmbio afetam o poder de compra e o custo de itens importados (celular, notebook, câmera). | Use séries do IBGE e do Banco Central (Selic, IPCA, câmbio) e inclua-as na regressão com defasagem. | Correlação vendas × renda e Selic; variação cambial × preço de custo; confiança do consumidor. |
| 16 | **Localização e demografia** | O perfil da região (população, renda, faixa etária, clima) define o mix e o volume das vendas. | Compare as vendas por região, cidade e loja com dados demográficos. | Vendas per capita; ticket por região; densidade de lojas; perfil etário e de gênero dos compradores. |
| 17 | **Tendências e comportamento do consumidor** | Busca online, trabalho híbrido, compras mobile, *social commerce* e a pesquisa antes da compra mudam o que e onde se compra. | Acompanhe o Google Trends e as buscas internas do site, e correlacione com as vendas futuras. | Volume de buscas por produto; tráfego orgânico; participação de vendas mobile; tempo entre a pesquisa e a compra. |
| 18 | **Eventos extremos e imprevistos** | Greves, crises logísticas, mudança tributária ou de regulação e variações climáticas incomuns causam choques de oferta ou demanda. | Registre os eventos como variáveis *dummy* para isolar seu efeito nos modelos. | Variação de vendas nos dias do evento; atraso médio de entrega; custo do frete. |

## Como usar estas variáveis na previsão

1. **Regressão múltipla:** `Vendas = β0 + β1·Preço + β2·Promoção + β3·Temperatura + β4·Sazonalidade + β5·Estoque + ε`.
2. **Elasticidade de preço:** calcule por SKU antes de definir descontos.
3. **KPIs de acompanhamento:** ticket médio, taxa de conversão, LTV, CAC, giro e taxa de ruptura.
4. **Priorização por produto:**
   - Aquecedor e cobertor elétrico: clima e sazonalidade (inverno).
   - Ar-condicionado: temperatura, crédito e renda.
   - Smartphone, celular, notebook, tablet e smartwatch: lançamentos, câmbio, preço relativo e promoções.
   - Smart TV: datas comerciais (Black Friday, grandes eventos) e parcelamento.
   - Cafeteira e câmera fotográfica: qualidade percebida, mix e engajamento.

> **Próximo passo (Aula 2.2):** validar estas variáveis nas bases em `dados/` e construir o modelo preditivo.
