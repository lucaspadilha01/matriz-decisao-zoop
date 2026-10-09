# Aula 2.3 · Variante de teste: Cafeteira 20%, Celular 10% e Tablet 10% (dezembro/2024)

**Objetivo:** comparar duas intensidades de desconto para ter mais chance de medir a elasticidade.
**Desenho:** Cafeteira com **20%** de desconto (ticket baixo, custo pequeno) e Celular e Tablet com **10%**, durante todo dezembro/2024. Os outros 8 produtos mantêm preço e previsão de referência.
**Base:** `Zoop - Dados Vendas.xlsx` e o modelo da Aula 2.2. Parte da seleção revisada em [previsao_dezembro_2024_desconto_seletivo.md](previsao_dezembro_2024_desconto_seletivo.md).

## 1. Efeito esperado no volume, por elasticidade assumida

Aumento de volume = (1 − desconto)^E − 1.

| Elasticidade | Cafeteira (20%) | Celular e Tablet (10%) |
|---|---:|---:|
| Conservador (-0,5) | +11,80% | +5,41% |
| Base (-1,0) | +25,00% | +11,11% |
| Otimista (-1,5) | +39,75% | +17,12% |

## 2. Previsão por produto

| Produto | Desconto | Preço normal → promocional (R$) | Sem desconto (un.) | Conservador | Base | Otimista |
|---|---:|---|---:|---:|---:|---:|
| Cafeteira | 20% | 320,01 → 256,01 | 408 | 457 (12,01%) | 511 (25,25%) | 571 (39,95%) |
| Celular | 10% | 1.050,05 → 945,05 | 1060 | 1117 (5,38%) | 1178 (11,13%) | 1241 (17,08%) |
| Tablet | 10% | 2.152,84 → 1.937,56 | 447 | 471 (5,37%) | 497 (11,19%) | 523 (17,00%) |

## 3. Comparação com o desconto de 10% nos três produtos

Lucro bruto com **margem ilustrativa de 30%** para todos os produtos (a base não traz custos).

| Desenho | Cenário | Unidades | Receita (R$) | Var. receita | Var. lucro bruto (margem 30%) |
|---|---|---:|---:|---:|---:|
| Sem desconto (referência) | – | 6749 | 16.356.992,07 | – | – |
| 10% nos 3 produtos | Conservador (E = -0,5) | 6853 | 16.243.391,35 | -0,69% | -4,01% |
| 10% nos 3 produtos | Base (E = -1,0) | 6963 | 16.358.039,94 | 0,01% | -3,49% |
| 10% nos 3 produtos | Otimista (E = -1,5) | 7076 | 16.474.866,63 | 0,72% | -2,96% |
| **Variante: Cafeteira 20%, Celular 10%, Tablet 10%** | Conservador (E = -0,5) | 6879 | 16.236.255,04 | -0,74% | -4,27% |
| **Variante: Cafeteira 20%, Celular 10%, Tablet 10%** | Base (E = -1,0) | 7020 | 16.358.103,94 | 0,01% | -3,75% |
| **Variante: Cafeteira 20%, Celular 10%, Tablet 10%** | Otimista (E = -1,5) | 7169 | 16.483.378,99 | 0,77% | -3,21% |

**Leitura:**
- **Custo extra da variante:** muito pequeno. Dobrar o desconto da Cafeteira soma só cerca de 0,26 ponto percentual de perda de lucro (de −3,49% para −3,75% no cenário base), porque a Cafeteira pesa apenas 0,80% da receita de dezembro.
- **Ganho de volume:** +57 unidades a mais que o desenho de 10% (7.020 contra 6.963 no cenário base).
- **Atenção à margem:** com margem de 30%, um desconto de 20% só mantém o lucro da Cafeteira se o volume subir 200%. A variante é um **teste de custo baixo**, não uma promoção que se paga sozinha.

## 4. Como ler o resultado do teste

O teste só é útil se o resultado observado for comparado com o esperado. Compare o volume real de dezembro com a previsão de referência (sem desconto), por produto:

| Aumento observado na Cafeteira (20%) | Leitura da elasticidade |
|---|---|
| Até +12% | Pouco sensível a preço (E próximo de −0,5 ou menos): não vale descontar |
| Cerca de +25% | Elasticidade unitária (E próximo de −1,0): a receita se mantém, o lucro cai |
| Acima de +40% | Muito sensível a preço (E próximo de −1,5 ou mais): o desconto tende a compensar |

Para Celular e Tablet (10%), os pontos de corte equivalentes são +5%, +11% e +17%.

**Limite de confiança:** a variação de um mês para outro é de cerca de ±25% por produto (±13% se juntar os três). Por isso:
- Resultados na faixa de +25% (Cafeteira) ou +11% (Celular e Tablet) **não permitem concluir** muita coisa sozinhos.
- Só o cenário otimista (Cafeteira acima de +40%) se destaca com clareza do ruído.
- O ideal é cruzar os dois: se a Cafeteira (20%) subir muito mais que o Celular e o Tablet (10%), isso sugere sensibilidade a preço. Se subirem parecido, o desconto maior não está rendendo.
- Para reforçar, dar o desconto apenas no e-commerce e usar a loja como controle do mesmo produto, e repetir na Black Friday.

## 5. Limites

- A elasticidade é uma hipótese: a base não tem descontos reais.
- A margem de 30% é ilustrativa e igual para todos.
- Não considerei canibalização nem efeito halo.
- Sem estoque, concorrência e temperatura na base, o modelo não captura rupturas nem a reação de concorrentes.

## 6. Previsão diária ajustada (cenário base)

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
| 2024-12-01 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-02 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-03 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-04 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-05 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-06 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-07 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-08 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-09 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-10 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-11 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-12 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-13 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-14 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-15 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-16 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-17 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-18 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-19 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-20 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-21 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-22 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-23 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-24 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-25 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-26 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-27 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-28 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-29 | Cafeteira | R$ 256,01 | 16 unidades |
| 2024-12-30 | Cafeteira | R$ 256,01 | 17 unidades |
| 2024-12-31 | Cafeteira | R$ 256,01 | 16 unidades |
| **Total do mês** | **Cafeteira** | – | **511 unidades** |
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
