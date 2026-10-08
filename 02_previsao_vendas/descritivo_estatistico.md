# Aula 2.2 · Análise dos dados históricos e descritivo estatístico

**Escopo:** os 11 produtos do case, período total da base `Zoop - Dados Vendas.xlsx` (01/01/2022 a 31/08/2024, 974 dias).
**Variáveis analisadas:** Total, Produto, Preço Unitário, Categoria, Canal de Venda, Quantidade Vendida, Campanhas e Dia da Semana.

## Método

- **Agrupamento por dia:** a base tem várias linhas por dia (36.000 registros). Somei a quantidade vendida por produto e por data antes de calcular as estatísticas diárias.
- **Média diária:** total vendido dividido pelos **974 dias do calendário**. Os dias sem nenhuma venda do produto (de 26 a 42 dias, conforme o produto) entram como zero, por isso o mínimo diário é 0.
- Valores com duas casas decimais e vírgula como separador.

## 1. Quantidade vendida por dia (descritivo por produto)

| Produto | Categoria | Total vendido (un.) | Média/dia | Mediana/dia | Desvio padrão | Mín. | Máx. |
|---|---|---:|---:|---:|---:|---:|---:|
| Aquecedor | Eletrodomésticos | 16.830 | 17,28 | 14,00 | 13,40 | 0 | 82 |
| Ar Condicionado | Eletrodomésticos | 16.323 | 16,76 | 12,00 | 14,88 | 0 | 101 |
| Cafeteira | Eletrodomésticos | 11.139 | 11,44 | 11,00 | 6,91 | 0 | 42 |
| Camera Fotográfica | Eletrônicos | 11.478 | 11,78 | 11,00 | 7,28 | 0 | 46 |
| Celular | Eletrônicos | 34.652 | 35,58 | 31,00 | 22,14 | 0 | 124 |
| Cobertor Elétrico | Eletrodomésticos | 11.829 | 12,14 | 11,00 | 8,57 | 0 | 63 |
| Notebook | Informática | 18.300 | 18,79 | 17,00 | 11,88 | 0 | 65 |
| Smart TV 55 | Eletrônicos | 18.138 | 18,62 | 18,00 | 11,36 | 0 | 63 |
| Smartphone | Eletrônicos | 34.813 | 35,74 | 33,00 | 22,14 | 0 | 171 |
| Smartwatch | Eletrônicos | 14.839 | 15,24 | 14,00 | 9,29 | 0 | 54 |
| Tablet | Informática | 14.673 | 15,06 | 14,00 | 9,03 | 0 | 47 |
| **Total Zoop** | – | **203.014** | **208,43** | **205,50** | **44,55** | **87** | **386** |

**Leitura:** Smartphone e Celular lideram em volume (cerca de 35 unidades por dia cada). A dispersão é alta: o desvio padrão é de 60% a 89% da média. Isso é maior em Ar Condicionado, Aquecedor e Cobertor Elétrico, os três com forte efeito sazonal (seção 5). A venda total diária da Zoop é bem mais estável (desvio de 44,55 sobre 208,43).

## 2. Preço unitário e receita

| Produto | Receita total (R$) | Preço médio (R$) | Mediana | Desvio padrão | Mín. | Máx. | Ticket/dia (R$) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Aquecedor | 42.823.839,13 | 2.543,21 | 2.541,94 | 82,51 | 2.375,04 | 2.729,92 | 43.966,98 |
| Ar Condicionado | 66.363.290,17 | 4.066,89 | 4.067,62 | 131,07 | 3.800,06 | 4.356,65 | 68.134,79 |
| Cafeteira | 3.440.039,28 | 308,82 | 308,39 | 11,87 | 285,05 | 335,99 | 3.531,87 |
| Camera Fotográfica | 11.735.564,67 | 1.022,44 | 1.021,29 | 35,37 | 950,20 | 1.102,44 | 12.048,83 |
| Celular | 35.429.554,11 | 1.022,13 | 1.021,89 | 35,34 | 950,03 | 1.102,31 | 36.375,31 |
| Cobertor Elétrico | 12.096.520,89 | 1.022,44 | 1.022,19 | 35,23 | 950,06 | 1.102,33 | 12.419,43 |
| Notebook | 83.873.296,50 | 4.584,15 | 4.583,12 | 154,69 | 4.275,66 | 4.934,84 | 86.112,21 |
| Smart TV 55 | 65.037.141,56 | 3.585,75 | 3.584,83 | 128,19 | 3.325,48 | 3.883,54 | 66.773,25 |
| Smartphone | 88.544.871,83 | 2.544,20 | 2.546,85 | 82,10 | 2.375,25 | 2.729,54 | 90.908,49 |
| Smartwatch | 22.893.887,59 | 1.543,82 | 1.542,69 | 59,11 | 1.425,09 | 1.679,69 | 23.505,02 |
| Tablet | 30.306.042,62 | 2.065,78 | 2.064,42 | 84,56 | 1.900,41 | 2.257,18 | 31.115,03 |

**Leitura:** o preço varia pouco dentro de cada produto (desvio padrão de cerca de 3% a 4% da média, e a amplitude entre mínimo e máximo fica em torno de ±7%). Por isso é difícil medir a elasticidade-preço com esta base. Notebook, Smartphone, Ar Condicionado e Smart TV concentram a maior receita.

## 3. Distribuição de frequência das variáveis categóricas

**Categoria do produto**

| Categoria | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Eletrônicos | 16.476 | 45,77% | 113.920 | 56,11% |
| Eletrodomésticos | 12.978 | 36,05% | 56.121 | 27,64% |
| Informática | 6.546 | 18,18% | 32.973 | 16,24% |

**Canal de venda**

| Canal de venda | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Loja | 18.043 | 50,12% | 101.705 | 50,10% |
| e-commerce | 17.957 | 49,88% | 101.309 | 49,90% |

**Origem da venda**

| Origem da venda | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Local | 18.043 | 50,12% | 101.705 | 50,10% |
| Google Ads | 6.081 | 16,89% | 33.991 | 16,74% |
| Instagram | 5.987 | 16,63% | 33.763 | 16,63% |
| Facebook | 5.889 | 16,36% | 33.555 | 16,53% |

**Método de pagamento**

| Pagamento | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Pix | 11.956 | 33,21% | 67.831 | 33,41% |
| Dinheiro | 12.004 | 33,34% | 67.771 | 33,38% |
| Cartão de crédito | 12.040 | 33,44% | 67.412 | 33,21% |

**Campanha**

| Campanha | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Nenhuma | 27.980 | 77,72% | 155.621 | 76,66% |
| Ano Novo | 3.421 | 9,50% | 21.101 | 10,39% |
| Natal | 2.307 | 6,41% | 14.018 | 6,90% |
| Black Friday | 2.292 | 6,37% | 12.274 | 6,05% |

**Dia da semana**

| Dia da semana | Registros | % registros | Unidades | % unidades |
|---|---:|---:|---:|---:|
| Quarta-feira | 5.248 | 14,58% | 29.854 | 14,71% |
| Sexta-feira | 5.175 | 14,37% | 29.130 | 14,35% |
| Segunda-feira | 5.199 | 14,44% | 29.105 | 14,34% |
| Terça-feira | 5.050 | 14,03% | 28.984 | 14,28% |
| Sábado | 5.076 | 14,10% | 28.768 | 14,17% |
| Domingo | 5.159 | 14,33% | 28.594 | 14,08% |
| Quinta-feira | 5.093 | 14,15% | 28.579 | 14,08% |

## 4. Vendas diárias totais por campanha e por dia da semana

Total de unidades da Zoop por dia, com vendas agrupadas por data.

| Campanha | Dias | Média/dia | Mediana | Desvio | Mín. | Máx. |
|---|---:|---:|---:|---:|---:|---:|
| Nenhuma | 759 | 205,03 | 201,00 | 44,16 | 87 | 375 |
| Ano Novo | 93 | 226,89 | 224,00 | 43,50 | 143 | 386 |
| Black Friday | 60 | 204,57 | 210,50 | 37,49 | 91 | 285 |
| Natal | 62 | 226,10 | 218,50 | 47,01 | 131 | 343 |

| Dia da semana | Dias | Média/dia | Mediana | Desvio | Mín. | Máx. |
|---|---:|---:|---:|---:|---:|---:|
| Segunda-feira | 139 | 209,39 | 204,00 | 45,68 | 101 | 312 |
| Terça-feira | 139 | 208,52 | 208,00 | 50,81 | 91 | 364 |
| Quarta-feira | 139 | 214,78 | 211,00 | 48,49 | 113 | 386 |
| Quinta-feira | 139 | 205,60 | 203,00 | 42,58 | 87 | 327 |
| Sexta-feira | 139 | 209,57 | 206,00 | 43,80 | 91 | 349 |
| Sábado | 140 | 205,49 | 204,00 | 39,11 | 110 | 321 |
| Domingo | 139 | 205,71 | 201,00 | 40,42 | 114 | 311 |

**Leitura:** Ano Novo e Natal vendem cerca de 10% acima dos dias sem campanha (226,89 e 226,10 contra 205,03). A Black Friday está no mesmo patamar dos dias normais (204,57). O dia da semana quase não afeta as vendas: a diferença entre o melhor dia (quarta, 214,78) e o pior (quinta, 205,60) é de cerca de 4%.

## 5. Sazonalidade mensal (média de unidades por dia)

| Mês | Aquecedor | Cobertor Elétrico | Ar Condicionado | Smartphone | Celular | Notebook |
|---|---:|---:|---:|---:|---:|---:|
| Jan | 17,19 | 9,81 | 34,12 | 36,90 | 37,87 | 18,90 |
| Fev | 19,51 | 10,32 | 28,54 | 36,92 | 33,05 | 20,20 |
| Mar | 10,60 | 9,62 | 17,94 | 39,87 | 34,92 | 19,52 |
| Abr | 9,86 | 9,17 | 9,98 | 33,91 | 36,20 | 19,41 |
| Mai | 10,26 | 9,95 | 9,53 | 35,70 | 35,80 | 19,73 |
| Jun | 27,18 | 17,82 | 9,60 | 33,66 | 35,52 | 16,98 |
| Jul | 27,48 | 18,58 | 10,57 | 37,29 | 37,77 | 18,62 |
| Ago | 26,63 | 17,42 | 9,71 | 32,42 | 35,73 | 21,43 |
| Set | 11,52 | 9,72 | 9,18 | 34,43 | 34,73 | 15,27 |
| Out | 11,69 | 10,15 | 10,29 | 37,48 | 31,65 | 18,11 |
| Nov | 11,32 | 8,92 | 19,45 | 34,38 | 35,70 | 18,75 |
| Dez | 18,90 | 11,23 | 34,94 | 35,45 | 36,53 | 16,31 |

**Leitura:** Aquecedor e Cobertor Elétrico sobem de junho a agosto (inverno). O Ar Condicionado sobe de dezembro a fevereiro (verão). Smartphone, Celular e Notebook ficam estáveis o ano todo.

## 6. Mapa de variáveis que influenciam as vendas

| ID | Variável | Descrição | Como medir | Exemplo prático (dados da Zoop) |
|---|---|---|---|---|
| 1 | **Mês / sazonalidade climática** | Define a demanda dos produtos de clima. É a variável de maior efeito. | Média diária por mês de cada produto, em relação à média anual. | Aquecedor vende 26,63 a 27,48 un./dia de junho a agosto, contra 9,86 a 11,69 nos outros meses. Ar Condicionado vende 34,94 em dezembro e 9,18 em setembro. |
| 2 | **Produto e categoria** | O produto define o volume e o ticket. | Total e média diária por produto, e % por categoria. | Smartphone e Celular somam 69.465 unidades. Eletrônicos concentram 56,11% das unidades. |
| 3 | **Campanhas promocionais** | Ano Novo e Natal elevam o volume. A Black Friday, no período analisado, não elevou. | Média diária nos dias de campanha contra a média dos dias sem campanha. | Ano Novo vende 226,89 un./dia contra 205,03 sem campanha (cerca de +10,66%). Black Friday, 204,57 (cerca de −0,22%). |
| 4 | **Preço unitário** | Afeta a demanda e a receita. Na base varia pouco (cerca de ±7%). | Elasticidade-preço `(ΔQ/Q)/(ΔP/P)` por produto. Exige variação real de preço. | A faixa de preço do Aquecedor vai de R$ 2.375,04 a R$ 2.729,92 sem relação clara com a quantidade vendida. |
| 5 | **Canal de venda** | Define a origem das vendas (loja ou e-commerce). | Participação de cada canal nas unidades e na receita. | Loja 50,10% e e-commerce 49,90% das unidades. |
| 6 | **Origem da venda (mídia)** | Mostra o retorno de cada fonte de tráfego digital. | Unidades e receita por origem, e CAC/ROAS quando houver custo de mídia. | Google Ads 16,74%, Instagram 16,63%, Facebook 16,53%. |
| 7 | **Dia da semana** | Pode concentrar as compras em certos dias. | Média diária por dia da semana. | Quarta tem 214,78 un./dia e quinta 205,60 (diferença de cerca de 4%). |
| 8 | **Método de pagamento** | Facilita a compra, principalmente em itens caros. | Participação por forma de pagamento. A base não tem parcelamento. | Pix 33,41%, dinheiro 33,38%, crédito 33,21%. |
| 9 | **Tendência (ano contra ano)** | Mostra o crescimento ou a queda de longo prazo. | Compare o mesmo mês em anos diferentes (YoY). | O volume anual de 2022 e 2023 é semelhante (cerca de 13,5 mil registros por ano). |
| 10 | **Variáveis ausentes na base** | Temperatura, estoque, concorrência, câmbio, desconto real e região. | Obter fontes externas (INMET, ERP, pesquisa de preços). | Sem temperatura e estoque, o modelo usa o mês como substituto do clima. |

## 7. Conclusões para o modelo preditivo

1. **Aquecedor, Cobertor Elétrico e Ar Condicionado:** usar o mês (sazonalidade) como variável principal.
2. **Smartphone, Celular, Notebook, Tablet, Smartwatch, Smart TV, Cafeteira e Câmera:** volume estável, bem descrito pela média e pela tendência.
3. **Campanhas:** incluir Ano Novo e Natal como variáveis (cerca de +10%). Não considerar a Black Friday como fator de aumento com base nestes dados.
4. **Preço, canal, pagamento e dia da semana:** efeito pequeno ou não mensurável, de baixa prioridade no modelo.
5. **Próximo passo (Aula 2.2, prompt 2):** definir o produto e o mês de previsão e construir o modelo.
