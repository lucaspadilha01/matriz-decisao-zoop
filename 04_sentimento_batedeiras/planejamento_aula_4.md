# Planejamento · Módulo 4: sentimento dos clientes sobre a Batedeira

**Objetivo:** entender como os clientes avaliam a **Batedeira** da Zoop nas redes sociais, classificar os sentimentos dos comentários e propor um plano de melhoria em **5W2H** para os problemas apontados (durabilidade e ruído).

## 1. O que cada aula pede (Notion)

| Aula | Tarefa | Entregas pedidas |
|---|---|---|
| **4.1 · Entendendo o sentimento** | **Prompt 1:** visão geral dos feedbacks (total de registros, registros por ano e mês, média de avaliação por plataforma, produto, categoria e ano, média global). **Prompt 2:** aprofundar em uma variável escolhida (média, mediana, desvio padrão, distribuição de 1 a 5, padrões e anomalias) | Gráficos de linha temporal e de barras, um histograma ou equivalente para a variável escolhida |
| **4.2 · Identificando sentimentos** | Classificar os comentários da Batedeira em positivo, neutro e negativo com a tabela de palavras-chave, tratando negações e frases com dois sentidos | Contagem por sentimento, gráfico de pizza ou barras, gráfico por plataforma e **mapa de calor** plataforma × sentimento |
| **4.3 · Plano 5W2H** | Plano de ação para os comentários negativos, respondendo ao e-mail do diretor (Carlos Souza) e usando a tabela de informações da Batedeira | Tabela 5W2H: o quê, por quê, onde, quando, quem, como, quanto custa |

## 2. Entradas disponíveis

| Entrada | Conteúdo |
|---|---|
| `dados/Feedbacks nas redes_sociais_zoop.xlsx` | 10.000 feedbacks de 30 produtos, de 30/08/2021 a 15/10/2024, sem nulos nem duplicados. Colunas: ID, Data, Seguidores do Autor, Plataforma, Nome_produto, Categoria_produto, Avaliacao (1 a 5) e Comentario |
| `dados/Vendas Zopp.xlsx` | Inclui a Batedeira (307 vendas, 627 unidades), para medir o tamanho do negócio |
| E-mail do diretor e tabela da Batedeira (Notion, 4.3) | Problemas: durabilidade baixa e ruído elevado. Pontos fortes: design moderno e facilidade de uso. Soluções: reforço da estrutura (custo alto) e ajuste do motor (custo médio), em 3 meses |
| Tabela de palavras-chave de sentimento (Notion, 4.2) | Listas de palavras positivas, neutras e negativas, e regras para negações |

## 3. Achados prévios que orientam o plano

1. **A Batedeira tem 307 feedbacks**, de 19/09/2021 a 21/09/2024, com **nota média 3,62**, abaixo da média global de 3,88. 21,2% das notas são 1 ou 2 (contra 15,4% na base toda) e 61,6% são 4 ou 5.
2. **A piora recente é real:** a nota trimestral foi de cerca de 3,8 a 3,9 em 2023 e caiu para 3,38 no 2º trimestre e 3,29 no 3º trimestre de 2024. Desde abril/2024, 34% dos feedbacks têm nota 1 ou 2. Isso confirma o que o diretor relatou.
3. **Os problemas citados aparecem nos comentários:** "durabilidade" em 21 comentários, "ruído" em 10 e "quebrou" em 2. Os pontos fortes também aparecem: design (6) e facilidade de uso (8).
4. **Os 307 comentários são todos diferentes entre si** e usam frases curtas e padronizadas, com hashtags. Uma classificação por palavras-chave e regras de negação deve funcionar bem, mas precisa ser validada.
5. **A Batedeira é um produto pequeno:** nas vendas, são 627 unidades e cerca de R$ 124.773 em três anos (ticket médio de R$ 199). Isso importa para o 5W2H: o reforço estrutural, de custo alto, pode custar mais do que o negócio retorna.
6. **As plataformas têm tamanhos muito diferentes** (X/Twitter 128 feedbacks da Batedeira, Facebook 91, TikTok 45, Instagram 43), e as médias ficam entre 3,53 e 3,71. A diferença é pequena e precisa de teste antes de virar conclusão.

## 4. Passos de execução

### Aula 4.1
| # | Passo | Resultado |
|---|---|---|
| 1 | Perfil dos 10.000 feedbacks: registros por ano e mês (linha temporal), média por plataforma, produto, categoria, ano e média global | Gráficos e tabelas do Prompt 1 |
| 2 | Aprofundar a Batedeira por **plataforma** e por **trimestre**: média, mediana, desvio padrão, distribuição de 1 a 5, anomalias | Gráfico de distribuição e de evolução da nota |
| 3 | Testar se as diferenças entre plataformas e a queda de 2024 são maiores que o acaso | Indicação de quais diferenças são significativas |

### Aula 4.2
| # | Passo | Resultado |
|---|---|---|
| 4 | Implementar o classificador com as palavras-chave do Notion, tratando negações ("não recomendo", "nada bom") e frases com dois sentidos | Sentimento de cada comentário |
| 5 | **Validar** o classificador contra a nota (1 e 2 negativo, 3 neutro, 4 e 5 positivo) e revisar manualmente as divergências | Taxa de concordância e lista de erros |
| 6 | Contagem de sentimentos, gráfico de pizza ou barras, gráfico por plataforma e **mapa de calor** plataforma × sentimento | Gráficos do Prompt de 4.2 |
| 7 | Extrair os **temas** dos negativos (durabilidade, ruído, expectativa/descrição, outros) e dos positivos (design, facilidade, qualidade) | Tabela de temas com contagem |

### Aula 4.3
| # | Passo | Resultado |
|---|---|---|
| 8 | Dimensionar o negócio (vendas da Batedeira) e relacionar o peso de cada tema negativo | Base para custo-benefício |
| 9 | Montar o **5W2H** para as soluções do Notion (reforço da estrutura e ajuste do motor) e acrescentar ações de baixo custo (comunicação, garantia, atendimento) | Tabela 5W2H |
| 10 | Redigir a **resposta ao diretor** (resumo de uma página, prazo até o fim da semana) | Texto para o diretor |
| 11 | Documentar, atualizar o README e fazer commit | Arquivos do módulo |

## 5. Entregáveis

Pasta `04_sentimento_batedeiras/`:
- `analise_feedbacks.md` (Aula 4.1) com gráficos em PNG;
- `analise_sentimentos.md` (Aula 4.2) com gráficos e mapa de calor em PNG;
- `plano_5w2h_batedeira.md` (Aula 4.3), incluindo o resumo para o diretor;
- `batedeira_sentimentos.csv`: cada comentário da Batedeira com o sentimento e o tema atribuídos;
- README atualizado e commit local.

## 6. Decisões em aberto (com a minha sugestão)

| Decisão | Sugestão |
|---|---|
| Variável para aprofundar na Aula 4.1 | **Plataforma**, com o recorte por **trimestre** para mostrar a queda recente (liga com o mapa de calor da 4.2) |
| Regra de sentimento | Palavras-chave do Notion com negações; validar contra a nota |
| Neutros | Notas 3 e comentários com palavras neutras do Notion; frases mistas seguem a regra do Notion (vale o lado predominante) |
| Custos do 5W2H | Manter a escala do Notion (alto e médio) e comparar com o tamanho do negócio; deixar campo para o valor em R$ se a Zoop tiver |
| Prazo e responsáveis | Usar os do e-mail: Gerente de Produto (João), Operações (Lucas) e Finanças (Carolina), com 3 meses para as mudanças no produto |
| Gráficos | PNG gerados em Python e inseridos nos arquivos de análise |

## 7. Riscos e limites

- **Classificador por palavras-chave** erra ironia e frases fora do vocabulário. A validação contra a nota mede isso.
- **Poucos dados por plataforma** (43 a 128 feedbacks da Batedeira): diferenças pequenas podem ser acaso.
- **Sem custos em R$** para as soluções: o 5W2H usa a escala do caso e o tamanho do negócio como referência.
- **Retorno do reforço estrutural incerto:** com receita de cerca de R$ 124.773 em três anos, o custo "alto" pode superar o ganho. O plano deve dizer isso com clareza.

## 8. Critérios de aceite

- Todos os itens do Prompt 1 (total, por ano e mês, por plataforma, produto, categoria e ano, média global) estão com gráfico.
- Cada comentário da Batedeira tem sentimento, e a taxa de concordância com a nota está informada.
- O mapa de calor plataforma × sentimento está feito.
- O 5W2H responde às sete perguntas para cada ação e responde ao e-mail do diretor.
