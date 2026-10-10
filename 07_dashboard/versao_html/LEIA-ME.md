# Painel Zoop Megastore (versão HTML, MVP)

Painel interativo publicado como Artifact privado no claude.ai (tipo "Dashboard"). Esta pasta guarda uma cópia para versionamento:

- `index.html`: página do painel (3 abas: resumo executivo, clientes e sentimento, decisão sem dados). Depende do ambiente do tipo "Dashboard" (objeto `dash` e `d3`), então não abre direto no navegador.
- `dados/*.json`: os 10 conjuntos de dados que a página lê.
- `gerar_dados.py`: script que gera os conjuntos de dados a partir das tabelas do projeto (ajuste os caminhos no início do arquivo).

Versão 2 prevista: abas de personalização (BCG e RFM), previsão de vendas, estoque de aquecedores e método e limites. Ver `../planejamento_dashboard_html.md`.
