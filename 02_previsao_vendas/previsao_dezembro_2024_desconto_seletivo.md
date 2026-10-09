# Aula 2.3 · Desconto seletivo de 10% em dezembro/2024 (versão revisada)

**Objetivo:** dar desconto só em produtos com bom potencial de venda em dezembro, para atrair público e **medir a elasticidade** de vendas.
**Restrições do negócio:** o **Aquecedor** fica de fora (a sazonalidade dele é de inverno, de junho a agosto) e o **Ar Condicionado** também (margem baixa).
**Base:** `Zoop - Dados Vendas.xlsx` (jan/2022 a ago/2024) e o modelo da Aula 2.2. A comparação com o desconto geral está em [previsao_dezembro_2024_desconto10.md](previsao_dezembro_2024_desconto10.md).

## 1. Escolha dos produtos

Com Aquecedor e Ar Condicionado fora, **só a Cafeteira** tem dezembro acima da média anual nos dois anos (índice de 1,22 em 2022 e 1,15 em 2023). Nenhum dos outros produtos tem pico sazonal em dezembro, então o critério passou a ser:

1. **Volume e potencial:** unidades e receita previstas para dezembro.
2. **Custo do desconto:** ticket menor significa menos receita sacrificada por 10% de desconto.
3. **Tendência de 2024:** produtos em queda são os que mais se beneficiam de uma promoção para atrair público.
4. **Confiabilidade da medição:** produtos de maior volume geram mais dados.

| Produto | Índice de dezembro (média 2022-23) | Dez/2022 | Dez/2023 | Unid. previstas (dez/2024) | Receita prevista (R$) | % da receita | Tendência 2024 | Decisão |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Ar Condicionado | 2,06 | 2,05 | 2,08 | 1078 | 4.473.512,01 | 27,34% | 7,44% | Fora: margem baixa |
| Smartphone | 0,98 | 0,95 | 1,01 | 1064 | 2.761.771,17 | 16,88% | -5,10% | Sem desconto |
| Celular | 1,00 | 0,95 | 1,05 | 1060 | 1.112.801,95 | 6,80% | -7,63% | **Desconto**: maior volume com ticket baixo; tendência de queda |
| Smart TV 55 | 1,02 | 0,96 | 1,09 | 567 | 2.096.668,45 | 12,82% | -2,73% | Sem desconto |
| Aquecedor | 1,12 | 1,13 | 1,10 | 567 | 1.471.822,52 | 9,00% | -2,46% | Fora: pico é no inverno (jun-ago) |
| Tablet | 1,01 | 0,98 | 1,03 | 447 | 962.035,38 | 5,88% | -8,49% | **Desconto**: item de presente; tendência de queda |
| Smartwatch | 0,88 | 0,87 | 0,89 | 421 | 673.026,89 | 4,11% | -4,20% | Sem desconto |
| Cafeteira | 1,19 | 1,22 | 1,15 | 408 | 130.707,65 | 0,80% | 9,56% | **Desconto**: único com dezembro acima da média nos 2 anos; item de presente |
| Notebook | 0,87 | 1,01 | 0,72 | 406 | 1.908.987,23 | 11,67% | 0,57% | Sem desconto |
| Cobertor Elétrico | 0,97 | 1,01 | 0,93 | 369 | 387.812,85 | 2,37% | 12,92% | Sem desconto |
| Camera Fotográfica | 0,97 | 0,89 | 1,05 | 362 | 380.966,83 | 2,33% | 3,73% | Sem desconto |

**Escolhidos:**
- **Cafeteira:** única com sazonalidade de dezembro nos dois anos, item de presente, ticket de cerca de R$ 320 (o desconto custa pouco) e tendência de alta em 2024.
- **Celular:** maior volume entre os produtos de ticket baixo (1.060 unidades previstas), tendência de queda de 7,63% em 2024 e dezembro/2023 acima da média (índice de 1,05).
- **Tablet:** item de presente de ticket médio, tendência de queda de 8,49% em 2024 e dezembro/2023 acima da média (índice de 1,03).

**Não escolhidos:** Smartphone e Smart TV 55 têm tickets altos (R$ 2.595 e R$ 3.695), então 10% de desconto sacrifica muita receita. Notebook, Smartwatch, Câmera e Cobertor Elétrico têm dezembro abaixo da média ou volume baixo.

Os três escolhidos somam **28,37% das unidades** e **13,48% da receita** prevista para dezembro.

## 2. Resultado do desconto seletivo (cenário base, elasticidade −1,0)

| Produto | Sem desconto (un.) | Com 10% (un.), base | Aumento | Preço normal (R$) | Preço promocional (R$) | Receita sem desconto (R$) | Receita com desconto (R$) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Cafeteira | 408 | 454 | 11,27% | 320,01 | 288,01 | 130.565,61 | 130.757,62 |
| Celular | 1060 | 1178 | 11,13% | 1.050,05 | 945,05 | 1.113.053,49 | 1.113.263,50 |
| Tablet | 447 | 497 | 11,19% | 2.152,84 | 1.937,56 | 962.320,90 | 962.966,75 |

Os outros 8 produtos mantêm preço e previsão normais (a previsão de referência da Aula 2.2).

## 3. Comparação das estratégias

Elasticidade assumida: −0,5 (conservador), −1,0 (base) e −1,5 (otimista). Lucro bruto calculado com uma **margem ilustrativa de 30% para todos os produtos**, porque a base não traz custos. Se a Zoop tiver margens reais por produto, vale recalcular.

| Estratégia | Cenário | Unidades | Receita (R$) | Var. receita | Var. lucro bruto (margem 30%) |
|---|---|---:|---:|---:|---:|
| Sem desconto (referência) | – | 6749 | 16.356.992,07 | – | – |
| Desconto geral (11 produtos) | Conservador (E = -0,5) | 7115 | 15.518.430,92 | -5,13% | -29,72% |
| Desconto geral (11 produtos) | Base (E = -1,0) | 7500 | 16.357.496,37 | 0,00% | -25,92% |
| Desconto geral (11 produtos) | Otimista (E = -1,5) | 7905 | 17.246.219,95 | 5,44% | -21,90% |
| Seleção anterior (Ar Condicionado, Cafeteira, Aquecedor) | Conservador (E = -0,5) | 6861 | 16.045.099,84 | -1,91% | -11,04% |
| Seleção anterior (Ar Condicionado, Cafeteira, Aquecedor) | Base (E = -1,0) | 6978 | 16.358.013,93 | 0,01% | -9,62% |
| Seleção anterior (Ar Condicionado, Cafeteira, Aquecedor) | Otimista (E = -1,5) | 7101 | 16.687.091,58 | 2,02% | -8,13% |
| Nova seleção (Cafeteira, Celular, Tablet) | Conservador (E = -0,5) | 6853 | 16.243.391,35 | -0,69% | -4,01% |
| Nova seleção (Cafeteira, Celular, Tablet) | Base (E = -1,0) | 6963 | 16.358.039,94 | 0,01% | -3,49% |
| Nova seleção (Cafeteira, Celular, Tablet) | Otimista (E = -1,5) | 7076 | 16.474.866,63 | 0,72% | -2,96% |

**Leitura:**
- **Receita:** igual à referência no cenário base. O desconto só eleva a receita se a elasticidade for maior que 1 em módulo.
- **Lucro bruto:** a perda cai de cerca de −26% (desconto geral) e −10% (seleção anterior, com Ar Condicionado e Aquecedor) para cerca de **−3,5%** na nova seleção. O ganho vem de descontar produtos de ticket menor.
- **Volume:** +214 unidades no mês (6.963 contra 6.749), cerca de +3,2%, o que ajuda a atrair público com custo baixo.

## 4. Como medir a elasticidade (e o limite dos dados)

1. **Controle:** os 8 produtos sem desconto e a divisão entre loja e e-commerce (cerca de 50% cada) servem de comparação. Uma opção é dar o desconto só no e-commerce e usar a loja como controle do mesmo produto.
2. **Ruído alto:** a razão entre e-commerce e loja varia cerca de ±25% por produto de um mês para outro (Cafeteira ±27%, Celular ±25%, Tablet ±22%). Juntando os 3 produtos o ruído cai para cerca de ±13%, próximo do efeito esperado de +11%. **Um mês com 10% provavelmente não dará uma elasticidade conclusiva.**
3. **Para melhorar a medição:**
   - dar 20% de desconto na Cafeteira (onde o custo é baixo) e manter 10% no Celular e no Tablet, para comparar duas intensidades de desconto;
   - repetir o teste na Black Friday e no Natal;
   - registrar o desconto real e o estoque na base a partir de agora.

## 5. Limites

- A elasticidade é uma hipótese: a base não tem descontos reais.
- A margem de 30% é ilustrativa e igual para todos os produtos.
- Não considerei canibalização (clientes trocando um produto sem desconto por um com desconto) nem o efeito halo (clientes que entram pela promoção e levam outros itens).
- Sem estoque, concorrência e temperatura na base, o modelo não captura rupturas nem a reação de concorrentes.

## 6. Previsão diária ajustada (cenário base; preço promocional apenas em Cafeteira, Celular e Tablet)

| Data Futura | Produto | Preço Aplicado | Quantidade Prevista |
|---|---|---:|---:|
| 2024-12-01 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-02 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-03 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-04 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-05 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-06 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-07 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-08 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-09 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-10 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-11 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-12 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-13 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-14 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-15 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-16 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-17 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-18 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-19 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-20 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-21 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-22 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-23 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-24 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-25 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-26 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-27 | Aquecedor | R$ 2.595,81 | 19 unidades |
| 2024-12-28 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-29 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-30 | Aquecedor | R$ 2.595,81 | 18 unidades |
| 2024-12-31 | Aquecedor | R$ 2.595,81 | 18 unidades |
| **Total do mês** | **Aquecedor** | – | **567 unidades** |
| 2024-12-01 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-02 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-03 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-04 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-05 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-06 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-07 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-08 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-09 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-10 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-11 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-12 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-13 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-14 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-15 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-16 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-17 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-18 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-19 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-20 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-21 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-22 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-23 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-24 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-25 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-26 | Ar Condicionado | R$ 4.149,29 | 34 unidades |
| 2024-12-27 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-28 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-29 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-30 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| 2024-12-31 | Ar Condicionado | R$ 4.149,29 | 35 unidades |
| **Total do mês** | **Ar Condicionado** | – | **1078 unidades** |
| 2024-12-01 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-02 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-03 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-04 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-05 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-06 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-07 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-08 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-09 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-10 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-11 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-12 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-13 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-14 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-15 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-16 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-17 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-18 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-19 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-20 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-21 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-22 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-23 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-24 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-25 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-26 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-27 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-28 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-29 | Cafeteira | R$ 288,01 | 14 unidades |
| 2024-12-30 | Cafeteira | R$ 288,01 | 15 unidades |
| 2024-12-31 | Cafeteira | R$ 288,01 | 15 unidades |
| **Total do mês** | **Cafeteira** | – | **454 unidades** |
| 2024-12-01 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-02 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-03 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-04 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-05 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-06 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-07 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-08 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-09 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-10 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-11 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-12 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-13 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-14 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-15 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-16 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-17 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-18 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-19 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-20 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-21 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-22 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-23 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-24 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-25 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-26 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-27 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-28 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-29 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-12-30 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-12-31 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| **Total do mês** | **Camera Fotográfica** | – | **362 unidades** |
| 2024-12-01 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-02 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-03 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-04 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-05 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-06 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-07 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-08 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-09 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-10 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-11 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-12 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-13 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-14 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-15 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-16 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-17 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-18 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-19 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-20 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-21 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-22 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-23 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-24 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-25 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-26 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-27 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-28 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-29 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-30 | Celular | R$ 945,05 | 38 unidades |
| 2024-12-31 | Celular | R$ 945,05 | 38 unidades |
| **Total do mês** | **Celular** | – | **1178 unidades** |
| 2024-12-01 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-02 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-03 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-04 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-05 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-12-06 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-07 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-08 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-09 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-10 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-11 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-12 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-13 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-14 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-15 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-16 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-17 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-18 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-19 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-12-20 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-21 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-22 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-23 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-24 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-25 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-26 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-12-27 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-28 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-29 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-30 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-12-31 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| **Total do mês** | **Cobertor Elétrico** | – | **369 unidades** |
| 2024-12-01 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-02 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-03 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-04 | Notebook | R$ 4.698,44 | 14 unidades |
| 2024-12-05 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-06 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-07 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-08 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-09 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-10 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-11 | Notebook | R$ 4.698,44 | 14 unidades |
| 2024-12-12 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-13 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-14 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-15 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-16 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-17 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-18 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-19 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-20 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-21 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-22 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-23 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-24 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-25 | Notebook | R$ 4.698,44 | 14 unidades |
| 2024-12-26 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-27 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-28 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-29 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-30 | Notebook | R$ 4.698,44 | 13 unidades |
| 2024-12-31 | Notebook | R$ 4.698,44 | 13 unidades |
| **Total do mês** | **Notebook** | – | **406 unidades** |
| 2024-12-01 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-02 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-03 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-04 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-05 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-06 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-07 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-08 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-09 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-10 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-11 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-12 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-13 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-14 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-15 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-16 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-17 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-18 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-19 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-20 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-21 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-22 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-23 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-24 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-25 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-26 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-27 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-12-28 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-29 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-30 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-12-31 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| **Total do mês** | **Smart TV 55** | – | **567 unidades** |
| 2024-12-01 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-02 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-03 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-04 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-05 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-06 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-07 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-08 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-09 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-10 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-11 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-12 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-13 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-14 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-15 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-16 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-17 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-18 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-19 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-20 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-21 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-22 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-23 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-24 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-25 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-26 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-27 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-12-28 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-29 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-30 | Smartphone | R$ 2.595,42 | 34 unidades |
| 2024-12-31 | Smartphone | R$ 2.595,42 | 34 unidades |
| **Total do mês** | **Smartphone** | – | **1064 unidades** |
| 2024-12-01 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-02 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-03 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-04 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-05 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-06 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-07 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-08 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-09 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-10 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-11 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-12 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-13 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-14 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-15 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-16 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-17 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-18 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-19 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-20 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-21 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-22 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-23 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-24 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-25 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-26 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-27 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-28 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-29 | Smartwatch | R$ 1.600,46 | 13 unidades |
| 2024-12-30 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-12-31 | Smartwatch | R$ 1.600,46 | 14 unidades |
| **Total do mês** | **Smartwatch** | – | **421 unidades** |
| 2024-12-01 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-02 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-03 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-04 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-05 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-06 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-07 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-08 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-09 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-10 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-11 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-12 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-13 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-14 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-15 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-16 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-17 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-18 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-19 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-20 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-21 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-22 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-23 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-24 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-25 | Tablet | R$ 1.937,56 | 17 unidades |
| 2024-12-26 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-27 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-28 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-29 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-30 | Tablet | R$ 1.937,56 | 16 unidades |
| 2024-12-31 | Tablet | R$ 1.937,56 | 16 unidades |
| **Total do mês** | **Tablet** | – | **497 unidades** |
