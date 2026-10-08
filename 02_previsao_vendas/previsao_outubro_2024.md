# Aula 2.2 · Previsão de vendas: outubro de 2024

**Escopo:** os 11 produtos da Zoop, de 01/10/2024 a 31/10/2024 (31 dias). **Eventos especiais:** nenhum confirmado, então o modelo é conservador (sem campanha e sem ajuste de preço).
**Base:** `Zoop - Dados Vendas.xlsx`, de 01/01/2022 a 31/08/2024.

## Modelo estatístico usado

Modelo de **nível dessazonalizado × índice sazonal**, com limite de crescimento (uma variante simples de suavização exponencial sazonal):

1. **Agrupamento:** somei as quantidades por produto e por dia (e completei os dias sem venda com zero).
2. **Suavização de picos:** limitei cada valor diário ao percentil 99 do produto, para picos anômalos sem campanha não distorcerem a previsão.
3. **Índice sazonal do mês:** razão entre a média diária do mês e a média do ano, calculada em 2022 e 2023. Aquecedor, Cobertor e Ar Condicionado usam o índice cheio. Nos outros 8 produtos o índice foi reduzido pela metade, porque a oscilação mensal deles é ruído, não sazonalidade real.
4. **Nível atual:** média diária de jan a ago de 2024 depois de retirar o efeito sazonal de cada mês. Isso mostra o ritmo "normal" de cada produto em 2024.
5. **Previsão de outubro:** nível × índice sazonal de outubro.
6. **Limite de crescimento:** a previsão não pode superar a média diária de outubro/2023 × (1 + crescimento de 2024 sobre 2023, quando positivo). Isso vale para Celular (de 32,28 para 28,90 por dia) e para Câmera Fotográfica (de 11,84 para 11,41 por dia).
7. **Distribuição diária:** o total do mês de cada produto é repartido pelos dias com um fator de dia da semana da Zoop, reduzido pela metade (o efeito real é de poucos pontos percentuais). Os valores foram arredondados para inteiros, preservando o total do mês.
8. **Preço previsto:** média de 2024 de cada produto. Na base o preço é estável dentro de cada ano e sobe cerca de 2% a 2,5% de um ano para o outro, então o preço de 2024 é o melhor estimador para outubro.

## Validação (backtest)

Previ junho, julho e agosto de 2024 usando só dados até maio de 2024, com o mesmo método:

| Teste | Erro médio por produto (MAPE) |
|---|---:|
| Este modelo | 8,80% |
| Repetir o mesmo mês do ano anterior | 13,20% |

O erro no total da Zoop ficou em +5,50% (junho), −5,50% (julho) e +2,00% (agosto). Os produtos com maior erro foram Ar Condicionado (16,30%) e Celular (15,20%).

## Resultado por produto

| Produto | Média/dia prevista | Total do mês (un.) | Preço previsto (R$) | Receita prevista (R$) | Out/2023 (média/dia) | Out/2022 (média/dia) | Variação vs. out/2023 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Aquecedor | 11,45 | 355 | 2.595,81 | 921.511,45 | 13,61 | 9,77 | -15,88% |
| Ar Condicionado | 10,42 | 323 | 4.149,29 | 1.340.221,75 | 11,29 | 9,29 | -7,71% |
| Cafeteira | 11,74 | 364 | 320,01 | 116.485,01 | 12,10 | 9,16 | -2,93% |
| Camera Fotográfica | 11,42 | 354 | 1.051,18 | 372.119,49 | 11,00 | 12,13 | 3,81% |
| Celular | 28,90 | 896 | 1.050,05 | 940.845,22 | 28,90 | 34,39 | 0,00% |
| Cobertor Elétrico | 11,23 | 348 | 1.050,31 | 365.508,84 | 12,26 | 8,03 | -8,42% |
| Notebook | 18,39 | 570 | 4.698,44 | 2.678.109,09 | 19,74 | 16,48 | -6,86% |
| Smart TV 55 | 18,19 | 564 | 3.695,43 | 2.084.220,69 | 20,13 | 17,65 | -9,62% |
| Smartphone | 35,42 | 1098 | 2.595,42 | 2.849.774,87 | 38,45 | 36,52 | -7,89% |
| Smartwatch | 14,23 | 441 | 1.600,46 | 705.803,31 | 17,42 | 12,61 | -18,33% |
| Tablet | 14,87 | 461 | 2.152,84 | 992.460,70 | 16,58 | 16,00 | -10,31% |
| **Total Zoop** | **186,26** | **5774** | – | **13.367.060,41** | **201,48** | **182,03** | **-7,56%** |

## Previsão diária (formato do prompt)

| Data Futura | Produto | Preço Previsto | Quantidade Prevista |
|---|---|---:|---:|
| 2024-10-01 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-02 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-03 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-04 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-05 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-06 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-07 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-08 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-09 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-10 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-11 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-12 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-13 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-14 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-15 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-16 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-17 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-18 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-19 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-20 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-21 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-22 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-23 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-24 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-25 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-26 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-27 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-28 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-29 | Aquecedor | R$ 2.595,81 | 11 unidades |
| 2024-10-30 | Aquecedor | R$ 2.595,81 | 12 unidades |
| 2024-10-31 | Aquecedor | R$ 2.595,81 | 11 unidades |
| **Total do mês** | **Aquecedor** | – | **355 unidades** |
| 2024-10-01 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-02 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-03 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-04 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-05 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-06 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-07 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-08 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-09 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-10 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-11 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-12 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-13 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-14 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-15 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-16 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-17 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-18 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-19 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-20 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-21 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-22 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-23 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-24 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-25 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-26 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-27 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-28 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-29 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| 2024-10-30 | Ar Condicionado | R$ 4.149,29 | 11 unidades |
| 2024-10-31 | Ar Condicionado | R$ 4.149,29 | 10 unidades |
| **Total do mês** | **Ar Condicionado** | – | **323 unidades** |
| 2024-10-01 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-02 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-03 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-04 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-05 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-06 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-07 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-08 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-09 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-10 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-11 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-12 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-13 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-14 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-15 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-16 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-17 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-18 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-19 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-20 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-21 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-22 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-23 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-24 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-25 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-26 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-27 | Cafeteira | R$ 320,01 | 11 unidades |
| 2024-10-28 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-29 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-30 | Cafeteira | R$ 320,01 | 12 unidades |
| 2024-10-31 | Cafeteira | R$ 320,01 | 11 unidades |
| **Total do mês** | **Cafeteira** | – | **364 unidades** |
| 2024-10-01 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-02 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-03 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-04 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-05 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-06 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-07 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-08 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-09 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-10 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-11 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-12 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-13 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-14 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-15 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-16 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-17 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-18 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-19 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-20 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-21 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-22 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-23 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-24 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-25 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-26 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-27 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-28 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-29 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| 2024-10-30 | Camera Fotográfica | R$ 1.051,18 | 12 unidades |
| 2024-10-31 | Camera Fotográfica | R$ 1.051,18 | 11 unidades |
| **Total do mês** | **Camera Fotográfica** | – | **354 unidades** |
| 2024-10-01 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-02 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-03 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-04 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-05 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-06 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-07 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-08 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-09 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-10 | Celular | R$ 1.050,05 | 28 unidades |
| 2024-10-11 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-12 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-13 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-14 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-15 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-16 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-17 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-18 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-19 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-20 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-21 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-22 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-23 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-24 | Celular | R$ 1.050,05 | 28 unidades |
| 2024-10-25 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-26 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-27 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-28 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-29 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-30 | Celular | R$ 1.050,05 | 29 unidades |
| 2024-10-31 | Celular | R$ 1.050,05 | 28 unidades |
| **Total do mês** | **Celular** | – | **896 unidades** |
| 2024-10-01 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-02 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-03 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-04 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-05 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-06 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-07 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-08 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-09 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-10 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-11 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-12 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-13 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-14 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-15 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-16 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-17 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-18 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-19 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-20 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-21 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-22 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-23 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-24 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-25 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-26 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-27 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-28 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-29 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| 2024-10-30 | Cobertor Elétrico | R$ 1.050,31 | 12 unidades |
| 2024-10-31 | Cobertor Elétrico | R$ 1.050,31 | 11 unidades |
| **Total do mês** | **Cobertor Elétrico** | – | **348 unidades** |
| 2024-10-01 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-02 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-03 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-04 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-05 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-06 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-07 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-08 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-09 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-10 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-11 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-12 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-13 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-14 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-15 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-16 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-17 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-18 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-19 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-20 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-21 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-22 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-23 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-24 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-25 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-26 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-27 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-28 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-29 | Notebook | R$ 4.698,44 | 18 unidades |
| 2024-10-30 | Notebook | R$ 4.698,44 | 19 unidades |
| 2024-10-31 | Notebook | R$ 4.698,44 | 18 unidades |
| **Total do mês** | **Notebook** | – | **570 unidades** |
| 2024-10-01 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-02 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-03 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-04 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-05 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-06 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-07 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-08 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-09 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-10 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-11 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-12 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-13 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-14 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-15 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-16 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-17 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-18 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-19 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-20 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-21 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-22 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-23 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-24 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-25 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-26 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-27 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-28 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-29 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| 2024-10-30 | Smart TV 55 | R$ 3.695,43 | 19 unidades |
| 2024-10-31 | Smart TV 55 | R$ 3.695,43 | 18 unidades |
| **Total do mês** | **Smart TV 55** | – | **564 unidades** |
| 2024-10-01 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-02 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-03 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-04 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-05 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-06 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-07 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-08 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-09 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-10 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-11 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-12 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-13 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-14 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-15 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-16 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-17 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-18 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-19 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-20 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-21 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-22 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-23 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-24 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-25 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-26 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-27 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-28 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-29 | Smartphone | R$ 2.595,42 | 35 unidades |
| 2024-10-30 | Smartphone | R$ 2.595,42 | 36 unidades |
| 2024-10-31 | Smartphone | R$ 2.595,42 | 35 unidades |
| **Total do mês** | **Smartphone** | – | **1098 unidades** |
| 2024-10-01 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-02 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-03 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-04 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-05 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-06 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-07 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-08 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-09 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-10 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-11 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-12 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-13 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-14 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-15 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-16 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-17 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-18 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-19 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-20 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-21 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-22 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-23 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-24 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-25 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-26 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-27 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-28 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-29 | Smartwatch | R$ 1.600,46 | 14 unidades |
| 2024-10-30 | Smartwatch | R$ 1.600,46 | 15 unidades |
| 2024-10-31 | Smartwatch | R$ 1.600,46 | 14 unidades |
| **Total do mês** | **Smartwatch** | – | **441 unidades** |
| 2024-10-01 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-02 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-03 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-04 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-05 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-06 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-07 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-08 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-09 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-10 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-10-11 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-12 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-13 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-14 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-15 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-16 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-17 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-10-18 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-19 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-20 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-21 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-22 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-23 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-24 | Tablet | R$ 2.152,84 | 14 unidades |
| 2024-10-25 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-26 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-27 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-28 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-29 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-30 | Tablet | R$ 2.152,84 | 15 unidades |
| 2024-10-31 | Tablet | R$ 2.152,84 | 14 unidades |
| **Total do mês** | **Tablet** | – | **461 unidades** |
