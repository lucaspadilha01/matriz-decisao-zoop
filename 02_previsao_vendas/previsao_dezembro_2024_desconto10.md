# Aula 2.3 · Cenário ajustado: dezembro de 2024 com campanha de final de ano e 10% de desconto

**Variáveis futuras informadas:** promoção de final de ano com **desconto de 10%**. Assumi que vale para os **11 produtos** e para o **mês inteiro** (01/12 a 31/12/2024, 31 dias).
**Base:** `Zoop - Dados Vendas.xlsx` (jan/2022 a ago/2024) e o modelo de previsão da Aula 2.2.

## Como o ajuste foi feito

1. **Previsão de referência para dezembro (sem desconto):** mesmo modelo da Aula 2.2 (nível dessazonalizado × índice sazonal de dezembro, com limite de crescimento). Total: **6749 unidades**, contra 6955 em dezembro/2022 e 7063 em dezembro/2023.
2. **A campanha de final de ano já está nessa referência.** Em 2022 e 2023 dezembro inteiro foi marcado como campanha "Natal", então o efeito histórico dela (cerca de +10%) já faz parte da sazonalidade. Não somei esse efeito de novo.
3. **O desconto de 10% é o efeito novo.** Nos anos anteriores o preço de dezembro foi igual ao do resto do ano (sem desconto), então a base **não permite medir** quanto o desconto aumenta as vendas. Por isso usei uma **elasticidade-preço assumida**: aumento de volume = (1 − 0,10)^E − 1.
4. **Três cenários:** conservador (E = −0,5), base (E = −1,0) e otimista (E = −1,5). A tabela diária usa o cenário base.
5. **Distribuição diária:** fator de dia da semana da Zoop, reduzido pela metade, com valores inteiros que preservam o total do mês.

## Resultado por produto (cenário base)

| Produto | Sem desconto (un.) | Com 10% (un.), cenário base | Variação | Preço normal (R$) | Preço com desconto (R$) | Receita sem desconto (R$) | Receita com desconto (R$) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Aquecedor | 567 | 630 | 11,11% | 2.595,81 | 2.336,23 | 1.471.822,52 | 1.471.822,52 |
| Ar Condicionado | 1078 | 1198 | 11,13% | 4.149,29 | 3.734,36 | 4.472.938,22 | 4.473.768,08 |
| Cafeteira | 408 | 454 | 11,27% | 320,01 | 288,01 | 130.565,61 | 130.757,62 |
| Camera Fotográfica | 362 | 403 | 11,33% | 1.051,18 | 946,07 | 380.528,97 | 381.264,79 |
| Celular | 1060 | 1178 | 11,13% | 1.050,05 | 945,05 | 1.113.053,49 | 1.113.263,50 |
| Cobertor Elétrico | 369 | 410 | 11,11% | 1.050,31 | 945,28 | 387.565,41 | 387.565,41 |
| Notebook | 406 | 451 | 11,08% | 4.698,44 | 4.228,59 | 1.907.565,42 | 1.907.095,58 |
| Smart TV 55 | 567 | 630 | 11,11% | 3.695,43 | 3.325,88 | 2.095.306,97 | 2.095.306,97 |
| Smartphone | 1064 | 1182 | 11,09% | 2.595,42 | 2.335,88 | 2.761.530,48 | 2.761.011,39 |
| Smartwatch | 421 | 467 | 10,93% | 1.600,46 | 1.440,41 | 673.794,09 | 672.673,76 |
| Tablet | 447 | 497 | 11,19% | 2.152,84 | 1.937,56 | 962.320,90 | 962.966,75 |
| **Total Zoop** | **6749** | **7500** | **11,13%** | – | – | **16.356.992,07** | **16.357.496,37** |

## Comparação dos cenários

| Cenário | Elasticidade | Aumento de volume | Unidades | Receita (R$) | Variação da receita |
|---|---:|---:|---:|---:|---:|
| Sem desconto (referência) | – | – | 6749 | 16.356.992,07 | – |
| Conservador | -0,5 | 5,41% | 7115 | 15.518.430,92 | -5,13% |
| Base | -1,0 | 11,11% | 7500 | 16.357.496,37 | 0,00% |
| Otimista | -1,5 | 17,12% | 7905 | 17.246.219,95 | 5,44% |

**Leitura:** com elasticidade −1,0 o volume sobe 11,11%, mas a receita **não cresce**: o preço cai 10% e a quantidade sobe quase o mesmo. A receita só aumenta se a elasticidade for maior que 1 em módulo, ou seja, se os clientes reagirem mais do que proporcionalmente ao desconto.

## O desconto compensa no lucro?

Mesmo que a receita se mantenha, o lucro cai, porque cada unidade vendida rende menos. Aumento de volume necessário para manter o lucro bruto, conforme a margem bruta atual:

| Margem bruta atual | Aumento mínimo de volume para manter o lucro bruto |
|---:|---:|
| 20% | +100% |
| 30% | +50% |
| 40% | +33% |
| 50% | +25% |

Com margem de 30%, por exemplo, o volume teria de subir **50%**, e o cenário otimista entrega apenas 17,12%. Sem os custos da Zoop não consigo afirmar o resultado, mas o desconto geral de 10% só compensa em produtos com margem alta ou muito elásticos.

## Limites desta simulação

- A elasticidade é uma hipótese, não um valor medido: a base quase não tem variação de preço.
- O limite de crescimento da Aula 2.2 continua valendo na referência: onde dezembro/2023 foi menor que dezembro/2022, a previsão não passa do nível de 2023 (caso do Notebook, que ficou em 13,11 unidades por dia, bem abaixo das 19,58 de dezembro/2022).
- Sem estoque, concorrência e temperatura na base, o modelo não captura rupturas nem a reação de concorrentes.
- Sugestão: aplicar o desconto só em produtos de margem alta e estoque parado (por exemplo, o Aquecedor) e acompanhar as vendas diárias para estimar a elasticidade real.

## Previsão diária ajustada (cenário base)

| Data Futura | Produto | Preço Aplicado | Quantidade Prevista (com campanha de final de ano e 10% de desconto) |
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
| 2024-12-01 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-02 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-03 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-04 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-05 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-06 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-07 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-08 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-09 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-10 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-11 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-12 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-13 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-14 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-15 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-16 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-17 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-18 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-19 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-20 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-21 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-22 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-23 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-24 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-25 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-26 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-27 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-28 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-29 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-30 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| 2024-12-31 | Camera Fotográfica | R$ 946,07 | 13 unidades |
| **Total do mês** | **Camera Fotográfica** | – | **403 unidades** |
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
| 2024-12-01 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-02 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-03 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-04 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-05 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-06 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-07 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-08 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-09 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-10 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-11 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-12 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-13 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-14 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-15 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-16 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-17 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-18 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-19 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-20 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-21 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-22 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-23 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-24 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-25 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-26 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-27 | Cobertor Elétrico | R$ 945,28 | 14 unidades |
| 2024-12-28 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-29 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-30 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| 2024-12-31 | Cobertor Elétrico | R$ 945,28 | 13 unidades |
| **Total do mês** | **Cobertor Elétrico** | – | **410 unidades** |
| 2024-12-01 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-02 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-03 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-04 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-05 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-06 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-07 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-08 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-09 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-10 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-11 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-12 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-13 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-14 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-15 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-16 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-17 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-18 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-19 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-20 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-21 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-22 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-23 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-24 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-25 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-26 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-27 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-28 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-29 | Notebook | R$ 4.228,59 | 14 unidades |
| 2024-12-30 | Notebook | R$ 4.228,59 | 15 unidades |
| 2024-12-31 | Notebook | R$ 4.228,59 | 15 unidades |
| **Total do mês** | **Notebook** | – | **451 unidades** |
| 2024-12-01 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-02 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-03 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-04 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-05 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-06 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-07 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-08 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-09 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-10 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-11 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-12 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-13 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-14 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-15 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-16 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-17 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-18 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-19 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-20 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-21 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-22 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-23 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-24 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-25 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-26 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-27 | Smart TV 55 | R$ 3.325,88 | 21 unidades |
| 2024-12-28 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-29 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-30 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| 2024-12-31 | Smart TV 55 | R$ 3.325,88 | 20 unidades |
| **Total do mês** | **Smart TV 55** | – | **630 unidades** |
| 2024-12-01 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-02 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-03 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-04 | Smartphone | R$ 2.335,88 | 39 unidades |
| 2024-12-05 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-06 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-07 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-08 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-09 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-10 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-11 | Smartphone | R$ 2.335,88 | 39 unidades |
| 2024-12-12 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-13 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-14 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-15 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-16 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-17 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-18 | Smartphone | R$ 2.335,88 | 39 unidades |
| 2024-12-19 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-20 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-21 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-22 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-23 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-24 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-25 | Smartphone | R$ 2.335,88 | 39 unidades |
| 2024-12-26 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-27 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-28 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-29 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-30 | Smartphone | R$ 2.335,88 | 38 unidades |
| 2024-12-31 | Smartphone | R$ 2.335,88 | 38 unidades |
| **Total do mês** | **Smartphone** | – | **1182 unidades** |
| 2024-12-01 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-02 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-03 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-04 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-05 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-06 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-07 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-08 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-09 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-10 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-11 | Smartwatch | R$ 1.440,41 | 16 unidades |
| 2024-12-12 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-13 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-14 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-15 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-16 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-17 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-18 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-19 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-20 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-21 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-22 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-23 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-24 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-25 | Smartwatch | R$ 1.440,41 | 16 unidades |
| 2024-12-26 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-27 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-28 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-29 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-30 | Smartwatch | R$ 1.440,41 | 15 unidades |
| 2024-12-31 | Smartwatch | R$ 1.440,41 | 15 unidades |
| **Total do mês** | **Smartwatch** | – | **467 unidades** |
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
