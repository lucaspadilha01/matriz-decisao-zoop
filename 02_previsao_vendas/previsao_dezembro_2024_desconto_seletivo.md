# Aula 2.3 · Desconto seletivo de 10% em dezembro/2024

**Mudança em relação ao cenário anterior:** em vez de 10% de desconto nos 11 produtos, o desconto vale só nos produtos com **maior potencial e maior sazonalidade em dezembro**, para atrair público e **medir a elasticidade** de vendas.
**Base:** `Zoop - Dados Vendas.xlsx` (jan/2022 a ago/2024) e o modelo da Aula 2.2. A comparação com o desconto geral está no arquivo [previsao_dezembro_2024_desconto10.md](previsao_dezembro_2024_desconto10.md).

## 1. Escolha dos produtos

Critérios: (a) **sazonalidade de dezembro** (índice = média diária de dezembro / média diária do ano, em 2022 e 2023), exigindo que o índice fique acima de 1,00 **nos dois anos**; (b) **potencial de venda** (unidades e receita previstas); (c) tendência de 2024 e custo do desconto.

| Produto | Índice de dezembro (média 2022-23) | Dez/2022 | Dez/2023 | Unid. previstas (dez/2024) | Receita prevista (R$) | % da receita | Tendência 2024 | Decisão |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Ar Condicionado | 2,06 | 2,05 | 2,08 | 1078 | 4.473.512,01 | 27,34% | 7,44% | **Desconto**: pico sazonal |
| Cafeteira | 1,19 | 1,22 | 1,15 | 408 | 130.707,65 | 0,80% | 9,56% | **Desconto**: item de presente, desconto de baixo custo |
| Aquecedor | 1,12 | 1,13 | 1,10 | 567 | 1.471.822,52 | 9,00% | -2,46% | **Desconto**: dezembro acima da média e estoque parado |
| Smart TV 55 | 1,02 | 0,96 | 1,09 | 567 | 2.096.668,45 | 12,82% | -2,73% | Sem desconto |
| Tablet | 1,01 | 0,98 | 1,03 | 447 | 962.035,38 | 5,88% | -8,49% | Sem desconto |
| Celular | 1,00 | 0,95 | 1,05 | 1060 | 1.112.801,95 | 6,80% | -7,63% | Sem desconto |
| Smartphone | 0,98 | 0,95 | 1,01 | 1064 | 2.761.771,17 | 16,88% | -5,10% | Sem desconto |
| Cobertor Elétrico | 0,97 | 1,01 | 0,93 | 369 | 387.812,85 | 2,37% | 12,92% | Sem desconto |
| Camera Fotográfica | 0,97 | 0,89 | 1,05 | 362 | 380.966,83 | 2,33% | 3,73% | Sem desconto |
| Smartwatch | 0,88 | 0,87 | 0,89 | 421 | 673.026,89 | 4,11% | -4,20% | Sem desconto |
| Notebook | 0,87 | 1,01 | 0,72 | 406 | 1.908.987,23 | 11,67% | 0,57% | Sem desconto |

**Resultado:** só três produtos têm dezembro acima da média nos dois anos.

- **Ar Condicionado:** é o maior pico sazonal da Zoop (índice de 2,06; dezembro é o melhor mês do ano) e representa 27,34% da receita prevista.
- **Cafeteira:** índice de 1,19 em dezembro, o melhor mês do ano para ela. É um item de presente de ticket baixo (cerca de R$ 320), então o desconto custa pouco.
- **Aquecedor:** índice de 1,12 (acima da média nos dois anos) e é o produto com estoque acumulado no case da Zoop. O desconto ajuda a escoar o estoque.

**Ficaram de fora:**
- Smart TV 55, Tablet e Celular: dezembro oscila em torno da média (índice entre 1,00 e 1,02), e Smart TV e Celular têm o índice abaixo de 1 em um dos anos.
- Smartphone: tem volume alto, mas sem pico em dezembro, então o desconto sairia caro sem ganho sazonal.
- Notebook, Smartwatch, Câmera e Cobertor Elétrico: dezembro é abaixo da média.

Os três escolhidos somam **30,42% das unidades** e **37,14% da receita** prevista para dezembro.

## 2. Resultado do desconto seletivo (cenário base, elasticidade −1,0)

| Produto | Sem desconto (un.) | Com 10% (un.), base | Aumento | Preço normal (R$) | Preço promocional (R$) | Receita sem desconto (R$) | Receita com desconto (R$) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ar Condicionado | 1078 | 1198 | 11,13% | 4.149,29 | 3.734,36 | 4.472.938,22 | 4.473.768,08 |
| Cafeteira | 408 | 454 | 11,27% | 320,01 | 288,01 | 130.565,61 | 130.757,62 |
| Aquecedor | 567 | 630 | 11,11% | 2.595,81 | 2.336,23 | 1.471.822,52 | 1.471.822,52 |

Os outros 8 produtos mantêm preço e previsão normais (a mesma previsão de referência da Aula 2.2, sem desconto).

## 3. Desconto seletivo contra desconto geral

Elasticidade assumida: −0,5 (conservador), −1,0 (base) e −1,5 (otimista). Lucro bruto calculado com uma **margem ilustrativa de 30%**, porque a base não traz custos.

| Estratégia | Cenário | Unidades | Receita (R$) | Var. receita | Var. lucro bruto (margem 30%) |
|---|---|---:|---:|---:|---:|
| Sem desconto (referência) | – | 6749 | 16.356.992,07 | – | – |
| Desconto geral (11 produtos) | Conservador (E = -0,5) | 7115 | 15.518.430,92 | -5,13% | -29,72% |
| Desconto geral (11 produtos) | Base (E = -1,0) | 7500 | 16.357.496,37 | 0,00% | -25,92% |
| Desconto geral (11 produtos) | Otimista (E = -1,5) | 7905 | 17.246.219,95 | 5,44% | -21,90% |
| Desconto seletivo (3 produtos) | Conservador (E = -0,5) | 6861 | 16.045.099,84 | -1,91% | -11,04% |
| Desconto seletivo (3 produtos) | Base (E = -1,0) | 6978 | 16.358.013,93 | 0,01% | -9,62% |
| Desconto seletivo (3 produtos) | Otimista (E = -1,5) | 7101 | 16.687.091,58 | 2,02% | -8,13% |

**Leitura:**
- **Receita:** nos dois desenhos fica praticamente igual à referência no cenário base. O desconto só aumenta a receita se a elasticidade for maior que 1 em módulo.
- **Lucro bruto:** o desconto seletivo reduz a perda de lucro de cerca de −26% (desconto geral) para cerca de −10% no cenário base, porque o desconto incide em 37,14% da receita e não em toda ela.
- **Volume:** o ganho de unidades é menor (6.978 contra 7.500), porque só três produtos recebem a promoção.
- O Ar Condicionado concentra a maior parte do custo do desconto. Se a margem dele for baixa, vale testar o desconto com Cafeteira e Aquecedor primeiro.

## 4. Como medir a elasticidade (e o limite dos dados)

O objetivo do desconto é medir a elasticidade real. Duas observações da própria base:

1. **Comparar com um grupo de controle:** os 8 produtos sem desconto, e também o canal. A divisão entre loja e e-commerce é estável (cerca de 50% cada), então dá para dar o desconto só no e-commerce e usar a loja como controle do mesmo produto, o que elimina a sazonalidade da comparação.
2. **Ruído alto:** a razão entre e-commerce e loja varia, mês a mês, cerca de ±21% a ±28% por produto. Mesmo juntando os 3 produtos, o ruído (cerca de ±14%) é parecido com o efeito esperado de um desconto de 10% (+11% no cenário base). **Um mês com 10% de desconto provavelmente não permitirá concluir a elasticidade com segurança.**

**Para a medição ser conclusiva**, qualquer uma destas ajudaria:
- aumentar o desconto de um dos produtos (por exemplo, 20% na Cafeteira, onde o custo é baixo), para o efeito passar de cerca de +25%;
- repetir o teste em mais de um mês (Black Friday e Natal);
- registrar o desconto e o estoque na base a partir de agora (campo de desconto real e de ruptura).

## 5. Limites

- A elasticidade é uma hipótese: a base não tem descontos reais.
- Não considerei canibalização (clientes migrando de um produto sem desconto para um com desconto) nem o efeito halo (clientes que entram pela promoção e levam outros itens). Ambos mudam o resultado.
- Ar Condicionado em pico pode ter demanda menos sensível a preço; por isso o cenário conservador é relevante para ele.
- Sem estoque, concorrência e temperatura, o modelo não captura rupturas nem a reação de concorrentes.

## 6. Previsão diária ajustada (cenário base; preço promocional apenas em Ar Condicionado, Cafeteira e Aquecedor)

| Data Futura | Produto | Preço Aplicado | Quantidade Prevista |
|---|---|---:|---:|
| 2024-12-01 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-02 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-03 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-04 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-05 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-06 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-07 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-08 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-09 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-10 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-11 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-12 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-13 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-14 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-15 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-16 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-17 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-18 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-19 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-20 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-21 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-22 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-23 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-24 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-25 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-26 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-27 | Aquecedor | R$ 2.336,23 | 21 unidades |
| 2024-12-28 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-29 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-30 | Aquecedor | R$ 2.336,23 | 20 unidades |
| 2024-12-31 | Aquecedor | R$ 2.336,23 | 20 unidades |
| **Total do mês** | **Aquecedor** | – | **630 unidades** |
| 2024-12-01 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-02 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-03 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-04 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-05 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-06 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-07 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-08 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-09 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-10 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-11 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-12 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-13 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-14 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-15 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-16 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-17 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-18 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-19 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-20 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-21 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-22 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-23 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-24 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-25 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-26 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-27 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-28 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-29 | Ar Condicionado | R$ 3.734,36 | 38 unidades |
| 2024-12-30 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| 2024-12-31 | Ar Condicionado | R$ 3.734,36 | 39 unidades |
| **Total do mês** | **Ar Condicionado** | – | **1198 unidades** |
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
| 2024-12-01 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-02 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-03 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-04 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-05 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-06 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-07 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-08 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-09 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-10 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-11 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-12 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-13 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-14 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-15 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-16 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-17 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-18 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-19 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-20 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-21 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-22 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-23 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-24 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-25 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-26 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-27 | Celular | R$ 1.050,05 | 35 unidades |
| 2024-12-28 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-29 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-30 | Celular | R$ 1.050,05 | 34 unidades |
| 2024-12-31 | Celular | R$ 1.050,05 | 34 unidades |
| **Total do mês** | **Celular** | – | **1060 unidades** |
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
| 2024-12-01 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-02 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-03 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-04 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-05 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-06 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-07 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-08 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-09 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-10 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-11 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-12 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-13 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-14 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-15 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-16 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-17 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-18 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-19 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-20 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-21 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-22 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-23 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-24 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-25 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-26 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-27 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-28 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-29 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-12-30 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-12-31 | Tablet | R$ 2.152,84 | 14 unidades |
| **Total do mês** | **Tablet** | – | **447 unidades** |
