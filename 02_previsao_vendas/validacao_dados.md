# Validação das variáveis nas bases (Aula 2.1 → 2.2)

Base principal: `dados/Zoop - Dados Vendas.xlsx` (36.000 linhas, 01/01/2022 a 31/08/2024, sem nulos nem duplicados). Contém exatamente os 11 produtos do case.

## Cobertura das variáveis

| ID | Variável | Cobertura na base | Coluna(s) |
|---|---|---|---|
| 1 | Preço | Parcial: o preço varia só cerca de ±7% em torno da média de cada produto | `Preço Unitario` |
| 2 | Promoções e campanhas | Parcial: só 3 campanhas (Ano Novo, Natal, Black Friday), sem % de desconto | `campanhas` |
| 3 | Canais de venda | Sim | `Canal de venda`, `Origem da Venda` |
| 7 | Pagamento | Parcial: só crédito, dinheiro e Pix, sem parcelamento | `Método de pagamento` |
| 11 | Sazonalidade e calendário | Sim | `Data`, `Ano`, `Mês`, `Dia`, `Dia da Semana` |
| 12 | Clima e temperatura | **Não está na base.** Pode ser inferido pelo mês | externo (INMET) |
| 4, 8, 9, 10 | Qualidade, engajamento, mídia, experiência | Parcial: nota e comentários só na base de feedbacks (outros produtos) | `Feedbacks nas redes_sociais_zoop.xlsx` |
| 5 | Estoque | **Não está na base** | falta |
| 13 a 18 | Concorrência, lançamentos, macro, região, tendências, eventos | **Não estão na base** | externos |

A base `Vendas Zopp.xlsx` (10.000 linhas) tem região, gênero, idade e avaliação, mas outros produtos e um período diferente. Ela serve ao módulo 5 (personalização).

## O que os dados mostram

**1. Sazonalidade climática, a variável mais forte.** Índice = vendas do mês / média mensal do produto (2022 e 2023):

| Produto | Pico | Vale |
|---|---|---|
| Aquecedor | jun a ago: 1,63 a 1,67 | mar a mai: 0,57 a 0,62 |
| Cobertor Elétrico | jun a ago: 1,37 a 1,63 | demais meses: 0,76 a 0,98 |
| Ar Condicionado | dez e jan: 2,12 e 2,00 | abr a set: 0,54 a 0,66 |

Os demais produtos oscilam pouco, entre 0,8 e 1,25, sem padrão climático.

**2. Campanhas.** Ficam em janeiro (Ano Novo), novembro (Black Friday) e dezembro (Natal). Média de unidades por dia de campanha contra dias sem campanha:

| Período | Unidades por dia |
|---|---|
| Ano Novo | 227 |
| Natal | 226 |
| Black Friday | 205 |
| Sem campanha | 205 |

A Black Friday **não mostra aumento**, e o ticket nas campanhas (cerca de R$ 2.150 a R$ 2.240) é igual ao dos dias sem campanha. Como a campanha coincide com o mês, o efeito dela se mistura com a sazonalidade: pela base, não dá para separar os dois.

**3. Preço.** A correlação entre preço e quantidade (em logaritmo) é próxima de zero em todos os produtos (de −0,04 a +0,03), porque o preço quase não varia. **Não é possível estimar elasticidade-preço** com esta base. Para isso seriam necessários descontos reais ou testes de preço.

**4. Canais.** Loja e e-commerce vendem o mesmo volume (cerca de 50% cada). No e-commerce, Google Ads, Instagram e Facebook se dividem em partes iguais.

**5. Dia da semana.** Sem padrão relevante: de 28,6 mil a 29,9 mil unidades por dia da semana.

**6. Tendência.** Volume anual estável (13,5 mil linhas em 2022 e 13,6 mil em 2023). Os meses de 2024 seguem o ritmo de 2023.

## Implicações para o modelo (Aula 2.2)

- Aquecedor, cobertor e ar-condicionado: modelar com **sazonalidade mensal**, que explica a maior parte da variação.
- Demais produtos: um modelo simples de média e tendência já é adequado.
- Não prometer efeito de preço ou de Black Friday: os dados não sustentam essas conclusões.
- Para um modelo mais completo, incluir temperatura (INMET), estoque e dados de concorrência.
