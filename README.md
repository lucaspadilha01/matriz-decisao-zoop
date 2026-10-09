# Uso de IA na Tomada de Decisões Estratégicas — Case Zoop Megastore

Projeto prático do curso da Alura sobre **IA aplicada a decisões estratégicas**. O case acompanha a **Zoop Megastore**, varejista de eletrônicos e eletrodomésticos, e o diretor **João Costa**, que precisa decidir sobre expansão, estoque, experiência do cliente e personalização usando o ChatGPT como apoio.

**Desafios da empresa:** expansão de mercado, gerenciamento de estoque, personalização de ofertas.
**Objetivo estratégico:** aumentar a participação de mercado e melhorar a eficiência operacional.

## Estrutura do repositório

```
.
├── README.md
├── 01_matriz_decisao/   # Matriz de decisão enriquecida com IA (Aula 1.3)
│   └── matriz_decisao.md
├── 02_previsao_vendas/  # Variáveis de vendas e validação nas bases (Aulas 2.1 a 2.3)
│   ├── variaveis_vendas.md
│   ├── validacao_dados.md
│   ├── descritivo_estatistico.md
│   ├── previsao_outubro_2024.md
│   ├── previsao_outubro_2024.csv
│   ├── previsao_dezembro_2024_desconto10.md
│   ├── previsao_dezembro_2024_desconto10.csv
│   ├── previsao_dezembro_2024_desconto_seletivo.md
│   ├── previsao_dezembro_2024_desconto_seletivo.csv
│   ├── previsao_dezembro_2024_variante_cafeteira20.md
│   ├── previsao_dezembro_2024_variante_cafeteira20.csv
│   └── estrategia_comercial_dezembro.md
├── 03_estoque_aquecedor/ # Causas do estoque elevado de aquecedores (Aulas 3.1 a 3.3)
│   ├── analise_causas.md
│   ├── acoes_corretivas.md
│   ├── planejamento_aula_3_3.md
│   ├── alertas_preventivos.md
│   ├── painel_alertas.csv
│   └── ishikawa_estoque_aquecedor.png
├── 04_sentimento_batedeiras/ # Sentimento dos clientes sobre a Batedeira (Aulas 4.1 a 4.3)
│   ├── planejamento_aula_4.md
│   ├── analise_feedbacks.md
│   └── graficos/        # 8 gráficos em PNG
├── dados/               # Bases usadas no case (vendas e feedbacks)
│   ├── Vendas Zopp.xlsx
│   ├── Zoop - Dados Vendas.xlsx
│   └── Feedbacks nas redes_sociais_zoop.xlsx
└── docs/
    └── notas.txt        # Links de referência (Notion e AI Canva)
```

## Os desafios do case (módulos do curso)

| Módulo | Desafio de negócio | Técnicas e frameworks |
|---|---|---|
| **1. IA na tomada de decisões** (Aula 1.3) | Criar uma matriz de decisão com decisões **Racionais, Intuitivas e Colaborativas** e mostrar como a IA apoia cada uma. | Prompt com persona, contexto e objetivo. Veja [a matriz](01_matriz_decisao/matriz_decisao.md). |
| **2. Previsão de vendas** (Aulas 2.1 a 2.3) | Mapear as variáveis que afetam as vendas, modelar previsões a partir do histórico e simular cenários futuros (campanhas e mudanças de preço) para os próximos 30 dias. | Sazonalidade, impacto de campanhas, modelo preditivo, simulação de cenários. Veja [as variáveis](02_previsao_vendas/variaveis_vendas.md), a [validação nos dados](02_previsao_vendas/validacao_dados.md) e o [descritivo estatístico](02_previsao_vendas/descritivo_estatistico.md), a [previsão de outubro/2024](02_previsao_vendas/previsao_outubro_2024.md) e o [cenário de dezembro/2024 com 10% de desconto](02_previsao_vendas/previsao_dezembro_2024_desconto10.md) e o [desconto seletivo](02_previsao_vendas/previsao_dezembro_2024_desconto_seletivo.md) e a [variante com Cafeteira a 20%](02_previsao_vendas/previsao_dezembro_2024_variante_cafeteira20.md). Conclusão: veja a [estratégia comercial para dezembro](02_previsao_vendas/estrategia_comercial_dezembro.md). |
| **3. Gestão de estoque** (Aulas 3.1 a 3.3) | Resolver o **acúmulo de estoque de aquecedores**: encontrar as causas, priorizar ações corretivas e criar alertas preventivos. | MECE, Diagrama de Ishikawa, Matriz GUT, Esforço × Impacto, Lean, Just-in-Time. Veja a [análise de causas](03_estoque_aquecedor/analise_causas.md) as [ações corretivas](03_estoque_aquecedor/acoes_corretivas.md) e os [alertas preventivos](03_estoque_aquecedor/alertas_preventivos.md). |
| **4. Sentimento do cliente** (Aulas 4.1 a 4.3) | Analisar os feedbacks de redes sociais sobre a linha de **Batedeiras**, classificar os sentimentos e propor melhorias. | Análise de sentimentos (positivo, neutro, negativo), 5W2H. Veja o [planejamento do módulo](04_sentimento_batedeiras/planejamento_aula_4.md) e a [análise dos feedbacks](04_sentimento_batedeiras/analise_feedbacks.md). |
| **5. Personalização** (Aulas 5.1 a 5.3) | Identificar padrões de compra por faixa etária, pagamento, gênero e região, mapear oportunidades e gerar recomendações personalizadas. | Segmentação de clientes, Matriz BCG, análise RFM, Matriz GUT. |
| **6. Decisão sem dados** (Aulas 6.1 a 6.3) | Decidir sobre a **expansão internacional** e a **reorganização do layout das lojas físicas** sem histórico nem avaliações. | IA como conselheiro estratégico, brainstorming, análise SWOT, cenários e heurísticas. |

## Bases de dados

| Arquivo | Uso no case |
|---|---|
| `dados/Vendas Zopp.xlsx` e `dados/Zoop - Dados Vendas.xlsx` | Previsão de vendas e padrões de compra (módulos 2 e 5) |
| `dados/Feedbacks nas redes_sociais_zoop.xlsx` | Análise de sentimentos das Batedeiras (módulo 4) |

## Referências

- Notion do curso: [Uso de IA na tomada de decisões estratégicas](https://grupoalura.notion.site/USO-DE-IA-NA-TOMADA-DE-DECIS-ES-ESTRAT-GICAS-fff379bdd09b811bb8b0e7fa947e2f8b)
- [AI Canva (StartSe)](https://ai-canva.startse.com/)

## Como usar a IA nas decisões (resumo)

- **Racional:** a IA analisa dados e prevê; a pessoa valida e decide.
- **Intuitiva:** a IA provoca, simula cenários e critica, sem virar análise de dados.
- **Colaborativa:** a IA facilita o consenso e a comunicação entre as áreas.
