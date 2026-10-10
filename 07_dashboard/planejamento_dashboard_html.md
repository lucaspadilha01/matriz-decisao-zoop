# Planejamento · Dashboard interativo (HTML) com o resumo de todas as análises

**Objetivo:** reunir em uma única página interativa tudo o que descobrimos nos 6 módulos, para o público ver o resumo em um minuto e aprofundar onde quiser. A versão em HTML serve para **validar o caminho** (conteúdo, perguntas e visual) antes de construir a versão em Power BI.

**Público (suposição, a confirmar):** diretoria e equipe de análise, então uma página de resumo executivo no início e páginas de detalhe depois.

## 1. Formato técnico

| Item | Decisão |
|---|---|
| Entrega | **Uma página HTML única**, publicada como Artifact privado para revisão (nada é publicado sem a sua aprovação) |
| Dados | Tabelas agregadas **embutidas na página** (JSON). Os comentários dos feedbacks e os registros individuais não entram, para a página ficar leve e sem texto de clientes |
| Bibliotecas | Um gráfico em JavaScript (Chart.js ou Plotly) carregado de CDN com versão fixa; sem etapa de compilação |
| Interação | Filtros, abas, alternância de visões, *sliders* e tabelas ordenáveis; tudo calculado no navegador |
| Aparência | Modo claro e escuro, layout que funciona no celular, números no formato pt-BR (vírgula decimal, ponto de milhar), cores consistentes com os gráficos já feitos |
| Atualização | Um *script* em Python gera o JSON a partir dos CSVs do projeto, então a página pode ser refeita quando os dados mudarem |

## 2. Estrutura da página (7 abas)

| Aba | Pergunta que responde | Conteúdo interativo |
|---|---|---|
| **0 · Resumo executivo** | "O que eu preciso saber?" | 6 indicadores grandes, as 6 principais descobertas e as 5 recomendações mais prioritárias, cada uma com link para a aba de detalhe |
| **1 · Previsão de vendas** (módulo 2) | O que vai vender e quando? | Sazonalidade por produto (mapa de calor mês × produto), previsão de outubro e dezembro/2024, seletor de cenário de desconto (sem desconto, geral, seletivo, Cafeteira 20%) com receita e lucro bruto |
| **2 · Estoque de aquecedores** (módulo 3) | Por que o estoque encalhou e como evitar? | Curva sazonal e queda do pico, causas por categoria, painel de 11 alertas com semáforo e limites |
| **3 · Clientes e sentimento** (módulo 4) | Como os clientes avaliam os produtos? | Ranking de notas com intervalo de confiança, sentimento por produto, filtros por produto, plataforma e período, evolução trimestral, temas dos comentários, produtos em observação |
| **4 · Vendas e personalização** (módulo 5) | Onde e o que vender? | Matriz BCG (alternar unidades e receita), mapa de blocos do Brasil com a penetração por estado (alternar vendas e receita), tabela das recomendações GUT ordenável e filtrável por evidência |
| **5 · Decisão sem dados** (módulo 6) | Qual cenário escolher? | **Matriz multicritério com *sliders* de pesos** que recalculam as pontuações em tempo real, resultado da sensibilidade, resumo do SWOT e dos 3 cenários |
| **6 · Método e limites** | Quanto posso confiar? | Premissas, hipóteses marcadas, dados que faltam, fontes e glossário (BCG, RFM, GUT, penetração) |

### Indicadores do resumo executivo (valores já calculados nos módulos)

| Indicador | Valor | Origem |
|---|---|---|
| Feedbacks analisados e nota média | 10.000 e 3,88 | Módulo 4 |
| Sentimento dos comentários | 69,4% positivos, 15,3% neutros e 15,3% negativos | Módulo 4 |
| Produto fora do padrão | Batedeira, nota 3,62 (único significativo) | Módulo 4 |
| Oportunidade regional | Teto de +2.037 vendas, ou R$ 3,25 milhões, em estados sub-indexados | Módulo 5 |
| Cenário recomendado | Cenário 2 (piloto internacional + layout), 7,3 contra 7,0 e 6,2 | Módulo 6 |
| Desconto geral de dezembro | Receita igual e cerca de −26% de lucro bruto (margem ilustrativa de 30%) | Módulo 2 |

## 3. Dados necessários

| Aba | Fontes já prontas | A gerar |
|---|---|---|
| 0 | Documentos dos módulos | Tabela de indicadores e descobertas |
| 1 | `previsao_*.csv`, `descritivo_estatistico.md` | Sazonalidade mês × produto e totais dos cenários (a partir de `Zoop - Dados Vendas.xlsx`) |
| 2 | `painel_alertas.csv` | Série mensal do aquecedor |
| 3 | `todos_produtos/dados_dashboard/` (ag_produto, ag_produto_plataforma, ag_produto_trimestre, ag_variacao_recente, ag_produto_tema, ag_tempo_geral, de_para_produtos) | Nenhuma |
| 4 | `05_personalizacao/dados/` (bcg_produtos, rfm_regiao, rfm_uf, recomendacoes_gut) | Posições dos blocos do mapa do Brasil |
| 5 | `matriz_multicriterio.csv`, `sensibilidade_pesos.csv` | Notas por critério para o recálculo |

Estimativa de tamanho: menos de 1 MB de dados agregados, bem abaixo do limite de 16 MB.

## 4. Princípios de design

1. **Primeiro a resposta, depois o detalhe:** cada aba abre com a conclusão em uma frase.
2. **Honestidade estatística visível:** gráficos de ranking mostram o intervalo de confiança e o número de feedbacks, para não induzir leitura de diferença onde há só ruído.
3. **Hipóteses marcadas:** valores que são suposição (margem de 30%, elasticidade, metas do piloto) aparecem com selo de "hipótese".
4. **Poucas cores com significado:** azul para o padrão, vermelho para alerta, verde para positivo e cinza para o neutro, iguais aos gráficos dos documentos.
5. **Sem excesso:** no máximo 4 ou 5 gráficos por aba.

## 5. Etapas de construção

| # | Etapa | Resultado |
|---|---|---|
| 1 | Preparar o JSON de dados com um *script* e conferir cada número com os documentos | Dados validados |
| 2 | Montar o esqueleto: abas, estilo, modo escuro e filtros globais | Estrutura da página |
| 3 | **Versão 1 (MVP):** abas 0 (resumo), 3 (sentimento) e 5 (decisão com *sliders*) | Página para você avaliar o caminho |
| 4 | Revisão com você: conteúdo, perguntas e visual | Ajustes |
| 5 | **Versão 2:** abas 4 (personalização), 1 (previsão), 2 (estoque) e 6 (método) | Dashboard completo |
| 6 | Testes: números contra os documentos, filtros, celular, modo escuro e acessibilidade | Página validada |
| 7 | Publicar como Artifact privado e salvar o arquivo no repositório | Link e arquivo versionado |

## 6. Decisões em aberto (com a minha sugestão)

| Decisão | Sugestão |
|---|---|
| Qual MVP primeiro | Abas 0, 3 e 5: cobrem o resumo, os dados de clientes (os mais ricos) e a parte mais interativa (pesos da matriz) |
| Biblioteca de gráficos | Chart.js (simples e leve); Plotly só se precisarmos de gráficos mais complexos |
| Mapa do Brasil | Mapa de blocos (um quadrado por estado), sem arquivo de mapa externo |
| Onde publicar | Artifact privado para revisão; o link só é compartilhado por você |
| Tema | Claro e escuro automáticos, com a identidade de cores do projeto |
| Idioma | Português do Brasil em todos os textos e números |

## 7. Riscos

- **Excesso de conteúdo:** são 6 módulos, e a página pode ficar pesada. A aba de resumo e o limite de gráficos por aba mitigam isso.
- **Números divergentes dos documentos:** a conferência automática da etapa 1 e o teste da etapa 6 cuidam disso.
- **Mal-entendido sobre hipóteses:** selos de "hipótese" e a aba de método deixam claro o que é medição e o que é suposição.
- **Dados de clientes:** só entram agregados, sem comentários nem registros individuais.

## 8. Critérios de aceite

- Todos os números do resumo batem com os documentos.
- Os filtros e os *sliders* recalculam sem recarregar a página.
- Cada gráfico de ranking mostra o intervalo de confiança.
- Hipóteses e limites aparecem identificados.
- A página funciona no celular e nos modos claro e escuro.
