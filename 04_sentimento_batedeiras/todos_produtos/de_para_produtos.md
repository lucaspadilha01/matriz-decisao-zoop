# De-para de produtos entre as bases

Para cruzar a nota dos feedbacks com as vendas no dashboard, comparei os nomes de produtos nas três bases do projeto. Arquivos gerados em [dados_dashboard/](dados_dashboard/):

- [de_para_produtos.csv](dados_dashboard/de_para_produtos.csv): tabela de correspondência, com uma chave padrão `Chave_Produto` (P01 a P34).
- [cruzamento_nota_vendas.csv](dados_dashboard/cruzamento_nota_vendas.csv): nota dos feedbacks e vendas lado a lado, por produto.

## 1. Resumo

| Base | Produtos | Período | Cruza com os feedbacks? |
|---|---:|---|---|
| `Feedbacks nas redes_sociais_zoop.xlsx` | 30 | 30/08/2021 a 15/10/2024 | Base de referência |
| `Vendas Zopp.xlsx` | 30 | 20/08/2021 a 19/08/2024 | **Sim, sem de-para:** os 30 nomes são idênticos, e o `ID_produto` (0 a 29) é único por produto |
| `Zoop - Dados Vendas.xlsx` | 11 | 01/01/2022 a 31/08/2024 | **Parcialmente:** 7 dos 11 produtos têm correspondência |

**Correção importante:** a limitação que eu havia anotado (só Cafeteira, Smartphone, Notebook e Tablet coincidem) vale **apenas para o `Zoop - Dados Vendas.xlsx`**. Com o `Vendas Zopp.xlsx` os 30 produtos coincidem.

## 2. Correspondência com o `Zoop - Dados Vendas.xlsx`

| Produto em Dados Vendas | Produto nos feedbacks | Tipo de correspondência | Observação |
|---|---|---|---|
| Cafeteira | Cafeteira | Exata | |
| Notebook | Notebook | Exata | Categoria diferente: Informática × Eletrônicos |
| Smartphone | Smartphone | Exata | |
| Tablet | Tablet | Exata | Categoria diferente: Informática × Eletrônicos |
| Smart TV 55 | Smart TV 55" | Equivalente (formatação) | Muda só a aspa de polegadas |
| Smartwatch | Relógio inteligente | Equivalente (mesmo tipo de produto) | Confirmar com a área de produto |
| Camera Fotográfica | Câmera digital | **Provável (confirmar)** | Não há "Câmera fotográfica" nos feedbacks |
| Aquecedor | – | Sem correspondência | Não há feedbacks do produto |
| Ar Condicionado | – | Sem correspondência | Não há feedbacks do produto |
| Celular | – | Sem correspondência | Não há feedbacks do produto |
| Cobertor Elétrico | – | Sem correspondência | Não há feedbacks do produto |

**Resultado:** 4 correspondências exatas, 2 equivalentes e 1 provável, que dependem de confirmação do negócio. Os outros 23 produtos dos feedbacks não existem no `Zoop - Dados Vendas.xlsx`. No arquivo `de_para_produtos.csv` há 34 linhas: os 30 produtos dos feedbacks e os 4 produtos que só existem em Dados Vendas.

## 3. Cuidados ao cruzar

- **As duas bases de vendas são catálogos diferentes.** Os preços diferem muito para o mesmo nome: Smartphone R$ 1.499 (Vendas Zopp) contra R$ 2.544 (Dados Vendas); Notebook R$ 3.499 contra R$ 4.584; Tablet R$ 1.199 contra R$ 2.066; Cafeteira R$ 199 contra R$ 309. **Não somar nem comparar valores entre as duas bases.** Uma coluna no cruzamento traz os dados de Dados Vendas só para os 7 produtos com correspondência, para consulta.
- **Categorias:** Notebook e Tablet são "Informática" em Dados Vendas e "Eletrônicos" nos feedbacks. O dashboard deve usar uma só classificação.
- **Períodos diferentes:** Vendas Zopp cobre ago/2021 a ago/2024; Dados Vendas, jan/2022 a ago/2024.

## 4. O que o cruzamento (feedbacks × Vendas Zopp) já mostra

- **A nota nas vendas é praticamente a mesma dos feedbacks.** A coluna de avaliação do `Vendas Zopp.xlsx` coincide com a nota dos feedbacks em quase todos os produtos (diferença média de 0,004; correlação de 0,974). A exceção é a **Batedeira**: 3,73 nas vendas contra 3,62 nos feedbacks. Por isso, não usar a avaliação das vendas como confirmação independente.
- **Nota e volume de vendas não têm relação:** correlação de 0,03 com as unidades (de 588 a 740 por produto). Os produtos mais bem avaliados não vendem mais unidades.
- **Nota e receita:** correlação de −0,20, explicada pelo preço (produtos caros têm receita maior, independentemente da nota).
- **Batedeira:** 627 unidades e R$ 124.773 em três anos, ou 0,78% da receita total de R$ 15,9 milhões da base. Não é o menor faturamento (Ferro de passar roupa, Chuveiro elétrico, Ventilador de mesa e Liquidificador faturam menos), mas é um produto de baixo ticket (R$ 199).

## 5. Como usar no dashboard

1. Usar `Chave_Produto` como chave do modelo e `Produto_Padrao` como nome de exibição.
2. Ligar feedbacks e `Vendas Zopp.xlsx` por `Produto` (ou `ID_Produto_Vendas_Zopp`).
3. Se o `Zoop - Dados Vendas.xlsx` entrar no dashboard, usar apenas as linhas de correspondência exata ou equivalente, e **confirmar com o negócio** o par Câmera fotográfica e Câmera digital antes de publicar.
