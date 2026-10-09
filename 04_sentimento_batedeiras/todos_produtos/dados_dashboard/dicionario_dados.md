# Dicionário de dados · base para o dashboard de feedbacks

Tabelas geradas a partir de `Feedbacks nas redes_sociais_zoop.xlsx` (10.000 feedbacks, 30 produtos, 30/08/2021 a 15/10/2024), com o sentimento e os temas da análise em [analise_todos_produtos.md](../analise_todos_produtos.md). **O dashboard ainda não foi construído**; este documento só descreve o que está pronto para usar.

**Formato dos arquivos:** CSV em UTF-8 com BOM, separador `;`, decimal `,` (padrão pt-BR). Datas no formato `AAAA-MM-DD`.

## 1. Tabelas fato e dimensões

| Arquivo | Linhas | Conteúdo |
|---|---:|---|
| `fato_feedbacks.csv` | 10.000 | Uma linha por feedback, com sentimento e temas |
| `fato_feedback_temas.csv` | 12.748 | Um tema por linha de feedback (relação muitos para muitos) |
| `dim_produto.csv` | 30 | Produto e categoria |
| `dim_plataforma.csv` | 4 | Plataformas |

### `fato_feedbacks.csv`

| Coluna | Tipo | Descrição |
|---|---|---|
| `ID_social` | inteiro | Identificador do feedback (único) |
| `Data` | data | Data do feedback |
| `Ano` | inteiro | Ano |
| `Trimestre` | texto | Formato `2024T3` |
| `AnoMes` | texto | Formato `2024-09` |
| `Plataforma` | texto | X (Twitter), Facebook, Instagram ou TikTok |
| `Produto` | texto | Nome do produto (30 valores) |
| `Categoria` | texto | Eletrodomésticos ou Eletrônicos |
| `Seguidores` | inteiro | Seguidores do autor |
| `Avaliacao` | inteiro | Nota de 1 a 5 |
| `Sentimento` | texto | Positivo, Neutro ou Negativo (classificador da Aula 4.2) |
| `Temas` | texto | Temas do comentário, separados por `; ` |
| `Comentario` | texto | Texto original |

### `fato_feedback_temas.csv`

| Coluna | Descrição |
|---|---|
| `ID_social` | Liga ao `fato_feedbacks` |
| `Tema` | Um dos 17 temas: Durabilidade, Arrependimento, Concorrência e alternativas, Não recomenda, Qualidade, Ruído, Defeitos, Expectativa e descrição, Preço e valor, Marca, Desempenho e eficiência, Facilidade de uso, Design, Uso diário e praticidade, Entrega, Recomendação, Produto básico ou comum |

(Os temas "Expectativa e descrição" nos negativos significam "abaixo do esperado ou diferente do descrito", e nos positivos, "atendeu ou superou a expectativa".)

## 2. Tabelas agregadas (pré-calculadas)

Podem ser recalculadas por medidas no dashboard. Estão prontas para uso imediato e para conferir os números.

| Arquivo | Linhas | Granularidade | Colunas principais |
|---|---:|---|---|
| `ag_produto.csv` | 30 | Produto | Feedbacks, nota média, mediana, desvio, IC 95%, % de notas 1 e 2, 3, 4 e 5, contagem e % de sentimentos, diferença para a média geral, p contra os demais, p ajustado (BH), destaque estatístico, posição por nota e por % de negativos |
| `ag_produto_plataforma.csv` | 120 | Produto × plataforma | Feedbacks, nota média, % negativos |
| `ag_produto_trimestre.csv` | 407 | Produto × trimestre | Feedbacks, nota média, % negativos |
| `ag_variacao_recente.csv` | 30 | Produto | Nota e % de negativos antes (jan/2023 a mar/2024) e recente (abr a set/2024), variação, p e p ajustado |
| `ag_produto_tema.csv` | 572 | Produto × sentimento × tema | Comentários e % dentro do sentimento do produto |
| `ag_tempo_geral.csv` | 14 | Trimestre (todos os produtos) | Feedbacks, nota média, % de cada sentimento |

Os períodos de `ag_variacao_recente.csv` e os p-valores são **fixos** (calculados uma vez); não se recalculam com filtros.

## 3. Relacionamentos sugeridos (modelo em estrela)

```
dim_produto[Produto]     1 ──► * fato_feedbacks[Produto]
dim_plataforma[Plataforma] 1 ──► * fato_feedbacks[Plataforma]
fato_feedbacks[ID_social]  1 ──► * fato_feedback_temas[ID_social]
Calendário[Data]           1 ──► * fato_feedbacks[Data]   (tabela calendário a criar)
```

## 4. Medidas sugeridas (a criar quando o dashboard for montado)

| Medida | Definição |
|---|---|
| Feedbacks | Contagem de `ID_social` |
| Nota média | Média de `Avaliacao` |
| % Positivo, % Neutro, % Negativo | Contagem do sentimento / total filtrado |
| % Notas 1 e 2 | Feedbacks com `Avaliacao` ≤ 2 / total |
| Intervalo de confiança 95% | Nota média ± 1,96 × desvio / √feedbacks |
| Variação da nota | Nota média do período recente − nota média do período anterior |
| % do tema entre negativos | Negativos que citam o tema / total de negativos |

## 5. Pontos de atenção

- **Nomes de produtos diferem da base de vendas.** Iguais nas duas: Cafeteira, Smartphone, Notebook e Tablet. Aparecem com nome diferente: "Smart TV 55\"" (feedbacks) e "Smart TV 55" (vendas), "Relógio inteligente" e "Smartwatch", "Câmera digital" e "Camera Fotográfica". Os demais produtos de feedback não existem na base de vendas de `Zoop - Dados Vendas.xlsx`. Para cruzar nota e vendas, será preciso um de-para.
- **Meses parciais:** ago/2021, set/2021 e out/2024. Trimestres 2021T3 e 2024T4 têm poucos feedbacks.
- **Poucos feedbacks por célula:** cruzamentos produto × plataforma têm de 37 a 156, e produto × trimestre menos ainda. Usar mínimo de 30 feedbacks para exibir médias.
- **Temas:** só a Batedeira tem temas específicos (ruído, design, facilidade de uso). Nos outros 29 produtos os comentários são genéricos.
- **Sentimento:** classificação por palavras-chave, com 99,89% de concordância com a nota. Pode errar em textos reais mais variados.
