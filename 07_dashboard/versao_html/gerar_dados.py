import json, os
import numpy as np, pandas as pd

P = "C:/Users/lucas/OneDrive/Área de Trabalho/Analise_dados_google_MD/Projeto_Alura/"
DD = P + "04_sentimento_batedeiras/todos_produtos/dados_dashboard/"
OUT = "C:/Users/lucas/AppData/Local/Temp/claude/C--Users-lucas-OneDrive--rea-de-Trabalho-Analise-dados-google-MD-Projeto-People-Analytics/8ef2f882-99e6-4c76-84a5-3ef23498a798/scratchpad/dash/"
os.makedirs(OUT, exist_ok=True)


def rd(f):
    return pd.read_csv(f, sep=";", decimal=",", encoding="utf-8-sig")


def clean(v):
    if isinstance(v, (np.integer,)): return int(v)
    if isinstance(v, (np.floating, float)): return None if pd.isna(v) else round(float(v), 4)
    if pd.isna(v) if not isinstance(v, str) else False: return None
    return v


def save(name, rows):
    rows = [{k: clean(v) for k, v in r.items()} for r in rows]
    json.dump(rows, open(OUT + name + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(name, len(rows), "linhas,", os.path.getsize(OUT + name + ".json") // 1024, "KB")


TODOS = "Todos os produtos"
fato = rd(DD + "fato_feedbacks.csv")
fato["Neg"] = (fato.Sentimento == "Negativo")

# ---------------- produtos (+ variação recente)
ap = rd(DD + "ag_produto.csv"); av = rd(DD + "ag_variacao_recente.csv")
m = ap.merge(av, on="Produto", how="left")
rows = []
for _, r in m.iterrows():
    rows.append(dict(Produto=r.Produto, Categoria=r.Categoria, Feedbacks=r.Feedbacks, Nota_media=r.Nota_media, IC95_inf=r.IC95_inf, IC95_sup=r.IC95_sup,
                     Pct_nota_1_2=r.Pct_nota_1_2, Pct_positivo=r.Pct_positivo, Pct_neutro=r.Pct_neutro, Pct_negativo=r.Pct_negativo,
                     p_ajustado=r.p_ajustado_BH_x, Destaque="Sim" if r.Significativo_5pct == "Sim" else "Não", Posicao_nota=r.Rank_nota,
                     Nota_antes=r.Nota_ref, Nota_recente=r.Nota_rec, Variacao_nota=r.Delta_nota, Neg_antes=r.Pct_neg_ref, Neg_recente=r.Pct_neg_rec,
                     p_variacao=r.p_valor, p_variacao_ajustado=r.p_ajustado_BH_y))
n = len(fato); a = fato.Avaliacao; se = a.std() / np.sqrt(n)
ref = fato[(fato.Data >= "2023-01-01") & (fato.Data < "2024-04-01")]; rec = fato[fato.Data >= "2024-04-01"]
rows.insert(0, dict(Produto=TODOS, Categoria="Todas", Feedbacks=n, Nota_media=a.mean(), IC95_inf=a.mean() - 1.96 * se, IC95_sup=a.mean() + 1.96 * se,
                    Pct_nota_1_2=(a <= 2).mean() * 100, Pct_positivo=(fato.Sentimento == "Positivo").mean() * 100, Pct_neutro=(fato.Sentimento == "Neutro").mean() * 100,
                    Pct_negativo=fato.Neg.mean() * 100, p_ajustado=None, Destaque="Não", Posicao_nota=None, Nota_antes=ref.Avaliacao.mean(), Nota_recente=rec.Avaliacao.mean(),
                    Variacao_nota=rec.Avaliacao.mean() - ref.Avaliacao.mean(), Neg_antes=ref.Neg.mean() * 100, Neg_recente=rec.Neg.mean() * 100, p_variacao=0.7027, p_variacao_ajustado=None))
save("produtos", rows)
prod = pd.DataFrame(rows)

# ---------------- trimestres
pt = rd(DD + "ag_produto_trimestre.csv"); pt = pt[pt.Feedbacks >= 5]
tg = fato.groupby("Trimestre").agg(Feedbacks=("Avaliacao", "size"), Nota_media=("Avaliacao", "mean"), Pct_negativo=("Neg", lambda s: s.mean() * 100)).reset_index()
tg = tg[tg.Feedbacks >= 50]; tg.insert(0, "Produto", TODOS)
tri = pd.concat([tg, pt[["Produto", "Trimestre", "Feedbacks", "Nota_media", "Pct_negativo"]]])
save("trimestres", tri.to_dict("records"))

# ---------------- plataformas
pp = rd(DD + "ag_produto_plataforma.csv")
gp = fato.groupby("Plataforma").agg(Feedbacks=("Avaliacao", "size"), Nota_media=("Avaliacao", "mean"), Pct_negativo=("Neg", lambda s: s.mean() * 100)).reset_index(); gp.insert(0, "Produto", TODOS)
save("plataformas", pd.concat([gp, pp[["Produto", "Plataforma", "Feedbacks", "Nota_media", "Pct_negativo"]]]).to_dict("records"))

# ---------------- temas
tm = rd(DD + "ag_produto_tema.csv")
GT = pd.read_pickle("GT_all.pkl")
g = GT[GT.n > 0].rename(columns={"n": "Comentarios", "pct": "Pct_do_sentimento", "Tema": "Tema", "Sentimento": "Sentimento"}); g.insert(0, "Produto", TODOS)
REN = {"Expectativa e descrição": "Descrição e expectativa"}
allt = pd.concat([g[["Produto", "Sentimento", "Tema", "Comentarios", "Pct_do_sentimento"]], tm[["Produto", "Sentimento", "Tema", "Comentarios", "Pct_do_sentimento"]]])
allt["Tema"] = allt.Tema.replace(REN)
save("temas", allt.to_dict("records"))

# ---------------- recomendações (GUT)
gut = rd(P + "05_personalizacao/dados/recomendacoes_gut.csv")
SEG = {"R11": "Base de clientes", "R1": "Sul (SC, RS, PR)", "R6": "Quem compra Batedeira", "R2": "Norte, Nordeste e Mato Grosso", "R5": "Todos os grupos", "R3": "MG, BA e PE",
       "R4": "Estados de alta fidelidade", "R7": "Compradores de Notebook, Tablet e TV Box", "R10": "Cidades sem compra há mais de 80 dias", "R9": "Mulheres de 18 a 25 anos", "R8": "Compradores de eletrônicos"}
gut["Segmento"] = gut.ID.map(SEG)
gut = gut.sort_values(["GUT", "Urgencia"], ascending=False)
save("recomendacoes", gut[["ID", "Segmento", "Recomendacao", "Gravidade", "Urgencia", "Tendencia", "GUT", "Prioridade", "Evidencia"]].to_dict("records"))

# ---------------- resumo (KPIs e descobertas)
resumo = [
    dict(tipo="kpi", id="k1", rotulo="Feedbacks analisados", valor=10000, formato="int", detalhe="30 produtos, de 30/08/2021 a 15/10/2024", modulo="Módulo 4", aba="", evidencia="", origem="Base de feedbacks"),
    dict(tipo="kpi", id="k2", rotulo="Nota média dos clientes", valor=3.88, formato="dec2", detalhe="Escala de 1 a 5; mediana 4; sem diferença entre plataformas, categorias e anos", modulo="Módulo 4", aba="sentimento", evidencia="", origem="Base de feedbacks"),
    dict(tipo="kpi", id="k3", rotulo="Comentários positivos", valor=69.39, formato="pct1", detalhe="15,3% neutros e 15,3% negativos", modulo="Módulo 4", aba="sentimento", evidencia="", origem="Classificador de sentimento"),
    dict(tipo="kpi", id="k4", rotulo="Nota da Batedeira", valor=3.62, formato="dec2", detalhe="Último de 30 produtos; único fora do padrão (p ajustado 0,001)", modulo="Módulo 4", aba="sentimento", evidencia="", origem="Base de feedbacks"),
    dict(tipo="kpi", id="k5", rotulo="Oportunidade regional (teto teórico)", valor=3.248878, formato="brl_mi", detalhe="2.037 vendas a mais se os estados sub-indexados chegassem à penetração média", modulo="Módulo 5", aba="", evidencia="", origem="Vendas e Censo 2022"),
    dict(tipo="kpi", id="k6", rotulo="Nota do cenário recomendado", valor=7.3, formato="dec1", detalhe="Cenário 2 (piloto internacional e layout em fases); Cenário 1: 7,0; Cenário 3: 6,2", modulo="Módulo 6", aba="decisao", evidencia="", origem="Matriz multicritério"),
    dict(tipo="descoberta", id="d1", rotulo="Batedeira é o único produto fora do padrão", valor=None, formato="",
         detalhe="Nota de 3,62 contra 3,88 na média, com 21,2% de notas 1 e 2. Os outros 29 produtos não se distinguem entre si. Em abril a setembro de 2024 a nota caiu para 3,34 (p = 0,054), no limite da significância, e as vendas seguem estáveis: é um sinal para acompanhar, não uma conclusão.",
         modulo="Módulo 4", aba="sentimento", evidencia="Forte", origem="Base de feedbacks"),
    dict(tipo="descoberta", id="d2", rotulo="A oportunidade está na geografia, não no perfil do cliente", valor=None, formato="",
         detalhe="Idade, gênero e pagamento não mudam o que se compra (todos os testes com p ≥ 0,29). Sul (índice de penetração 0,52), Norte (0,68) e Nordeste (0,77) vendem abaixo do peso da população; Santa Catarina tem índice de 0,10.",
         modulo="Módulo 5", aba="", evidencia="Forte", origem="Vendas e Censo 2022"),
    dict(tipo="descoberta", id="d3", rotulo="Produtos estrela por receita: cinco itens de ticket alto", valor=None, formato="",
         detalhe="Notebook, Smartphone, Câmera digital, Tablet e Relógio inteligente somam 34,2% da receita. O crescimento dos produtos é instável (correlação de −0,46 entre 2023 e 2024), então a Matriz BCG vale por receita e deve ser reavaliada a cada trimestre.",
         modulo="Módulo 5", aba="", evidencia="Moderada", origem="Vendas"),
    dict(tipo="descoberta", id="d4", rotulo="Desconto geral em dezembro não compensa no lucro", valor=None, formato="",
         detalhe="Com 10% de desconto nos 11 produtos a receita fica igual e o lucro bruto cai cerca de 26% (margem ilustrativa de 30%). Descontar só Cafeteira, Celular e Tablet reduz a perda para cerca de 3,5%. A elasticidade é uma hipótese: a base quase não tem variação de preço.",
         modulo="Módulo 2", aba="", evidencia="Hipótese", origem="Vendas e simulação"),
    dict(tipo="descoberta", id="d5", rotulo="O estoque de aquecedores veio de compra acima da demanda", valor=None, formato="",
         detalhe="A demanda de junho a agosto é de 2,4 a 2,7 vezes a dos meses fracos, o pico caiu 10,0% em dois anos e não há nenhuma campanha no inverno. As vendas não colapsaram; o planejamento ignorou a sazonalidade.",
         modulo="Módulo 3", aba="", evidencia="Moderada", origem="Vendas e ata do caso"),
    dict(tipo="descoberta", id="d6", rotulo="Cenário 2 vence por pouco e depende dos pesos", valor=None, formato="",
         detalhe="Piloto internacional com layout em fases soma 7,3 contra 7,0 do Cenário 1 e 6,2 do Cenário 3. Com pesos avessos a risco, o Cenário 1 vence. Em 20 mil simulações, o Cenário 2 é o melhor em 59,4% dos casos. A decisão final espera a confirmação do diretor.",
         modulo="Módulo 6", aba="decisao", evidencia="Julgamento", origem="Matriz multicritério"),
]
save("resumo", resumo)

# ---------------- matriz multicritério
CEN = {"Cenário 1": "Brasil primeiro", "Cenário 2": "Piloto internacional + layout em fases", "Cenário 3": "Expansão simultânea"}
CRIT = ["Impacto no crescimento", "Risco de implementação", "Viabilidade operacional", "Urgência de aplicação"]
PESO = {"Impacto no crescimento": 40, "Risco de implementação": 20, "Viabilidade operacional": 30, "Urgência de aplicação": 10}
NOTAS = {"Cenário 1": [5, 9, 9, 5], "Cenário 2": [8, 6, 7, 8], "Cenário 3": [10, 2, 3, 9]}
JUST = {
    "Cenário 1": ["Só cresce no Brasil; os dados mostram espaço doméstico, mas o efeito do novo layout não foi medido", "Opera onde a Zoop já tem equipe, marca e logística", "Executável com os recursos atuais", "Trata a queda de tráfego das lojas, mas não a pressão por expansão"],
    "Cenário 2": ["Abre o mercado internacional e mantém o ganho do layout; o piloto sozinho tem efeito pequeno no curto prazo", "Risco limitado e reversível, mas exige parceiro e logística novos", "Duas frentes exigem coordenação, mas o caixa existe", "Responde à pressão de concorrentes e acionistas já no primeiro ano"],
    "Cenário 3": ["Maior alcance e velocidade", "Compromete caixa, opera em vários países e não tem ponto de saída", "Falta logística internacional e mão de obra para fazer tudo ao mesmo tempo", "Máxima resposta à pressão de tempo"]}
mat = []
for c, nome in CEN.items():
    for j, k in enumerate(CRIT):
        mat.append(dict(Cenario=c, Nome=nome, Criterio=k, Peso_pct=PESO[k], Nota=NOTAS[c][j], Justificativa=JUST[c][j]))
save("matriz", mat)

sens = [("Pesos do diretor", 40, 20, 30, 10, 7.0, 7.3, 6.2, "Cenário 2"), ("Pesos iguais", 25, 25, 25, 25, 7.0, 7.25, 6.0, "Cenário 2"), ("Avesso a risco", 20, 40, 30, 10, 7.8, 6.9, 4.6, "Cenário 1"),
        ("Foco em crescimento", 60, 10, 20, 10, 6.2, 7.6, 7.7, "Cenário 3"), ("Foco em execução", 30, 20, 40, 10, 7.4, 7.2, 5.5, "Cenário 1"), ("Foco em urgência", 30, 15, 25, 30, 6.6, 7.45, 6.75, "Cenário 2")]
save("sensibilidade", [dict(Perfil=s[0], Peso_impacto=s[1], Peso_risco=s[2], Peso_viabilidade=s[3], Peso_urgencia=s[4], Cenario_1=s[5], Cenario_2=s[6], Cenario_3=s[7], Vencedor=s[8]) for s in sens])

cen = [
    dict(Cenario="Cenário 1", Nome="Brasil primeiro", Perfil="Conservador: baixo risco, impacto moderado", Internacional="Só estudo de mercado e conversas; nenhuma operação por 12 meses",
         Lojas="Reorganização em fases, começando por lojas-piloto", Decisao_seguinte="Revisão em 12 meses", Prob_melhor_pct=35.6),
    dict(Cenario="Cenário 2", Nome="Piloto internacional + layout em fases", Perfil="Expansão moderada: risco calculado, alto potencial", Internacional="Piloto de e-commerce em um país da América Latina, com parceiro e suporte técnico local",
         Lojas="Reorganização em fases (igual ao Cenário 1)", Decisao_seguinte="Ponto de decisão (ampliar, ajustar ou parar) após o piloto", Prob_melhor_pct=59.4),
    dict(Cenario="Cenário 3", Nome="Expansão simultânea", Perfil="Agressivo: alto risco, grande impacto", Internacional="Vários países com e-commerce e lojas físicas, mais aquisição de startups",
         Lojas="Reorganização das mais de 200 lojas ao mesmo tempo", Decisao_seguinte="Sem ponto de revisão previsto", Prob_melhor_pct=5.1)]
save("cenarios", cen)

swot = []
def add(q, items, fonte):
    for it, f in zip(items, fonte): swot.append(dict(Quadrante=q, Item=it, Fonte=f))
add("Forças", ["Inovação constante e histórico de lançar tecnologia no varejo", "Experiência omnichannel e atendimento personalizado", "Porte: US$ 5 bilhões, 3.500 colaboradores e mais de 200 lojas", "Caixa sólido para investir",
               "Equipe de vendas e atendimento muito eficiente no Brasil", "Liderança com histórico de expansão e de transformação digital", "Lojas físicas ainda respondem por 66,2% das vendas", "Receita concentrada em produtos de maior valor, que combinam com o novo layout"],
    ["Notion"] * 6 + ["Dados do projeto"] * 2)
add("Fraquezas", ["Falta de experiência em mercados e logística internacionais", "Tráfego das lojas físicas em queda", "Dependência do mercado doméstico", "Escassez de mão de obra para projetar e gerir lojas",
                  "Decisões sem pesquisa de mercado recente", "Preços mais altos que concorrentes globais", "Sem dados por cliente para personalizar", "Sem linha de automação residencial nos dados de vendas"],
    ["Notion"] * 5 + ["Notion e suposição", "Dados do projeto", "Dados do projeto"])
add("Oportunidades", ["Crescimento do e-commerce de eletrônicos na América Latina", "Automação residencial, IA e IoT em alta", "Demanda por produtos sustentáveis", "Startups locais para parceria ou aquisição",
                      "Omnichannel avançado", "Regiões brasileiras abaixo do potencial (Sul, Norte e Nordeste)", "Marketing digital local com influenciadores regionais"],
    ["Notion"] * 5 + ["Dados do projeto", "Notion"])
add("Ameaças", ["Concorrentes internacionais com preços mais baixos", "TechPro e Electro World já operam na região", "Tarifas e normas de produto diferentes por país", "Consumidor cada vez mais online",
                "Escassez de profissionais especializados", "Câmbio e ambiente político da região", "Clientes testam na loja e compram em outro site"],
    ["Notion"] * 5 + ["Suposição"] * 2)
save("swot", swot)
