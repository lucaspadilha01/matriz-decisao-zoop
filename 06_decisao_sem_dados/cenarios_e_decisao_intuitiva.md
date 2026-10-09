# Aula 6.1 · Chat conselheiro: contexto, cenários e decisão intuitiva

**Papel:** consultor estratégico do diretor da Zoop Megastore, João Costa, em uma decisão **sem dados de mercado**. As respostas do diretor são as do Notion e estão marcadas como "resposta do diretor". O que for suposição está marcado como **[S]**; o que vem dos dados do projeto, como **[D]**.

---

## Prompt 1 · Reconhecimento do cenário e contexto

### A empresa

| Item | Informação |
|---|---|
| Fundação | 2005 |
| Propósito e missão | Transformar a experiência de compra de eletrônicos e eletrodomésticos, com produtos inovadores e serviço personalizado |
| Visão | Ser referência no varejo de eletrônicos na América Latina e expandir para o mercado internacional |
| Porte | US$ 5 bilhões de faturamento anual, 3.500 colaboradores, mais de 200 lojas físicas no Brasil e forte e-commerce |
| Portfólio | Eletrônicos (smartphones, computadores, tablets, wearables), eletrodomésticos e *smart home* |
| Concorrentes | Megatech (dispositivos móveis), Electro World (eletrodomésticos) e TechPro (automação residencial) |
| Diferenciais | Inovação constante, atendimento personalizado e experiência omnichannel |
| Desafios recentes | Concorrência internacional com preços mais baixos e migração dos consumidores para o e-commerce |
| Iniciativas | Sistema de recomendação online, novos layouts de loja, linha *eco-friendly* e reciclagem de eletrônicos |
| Planos | Expandir para a América Latina nos próximos 2 anos, investir em automação residencial e IA, adquirir startups e integrar mais os canais |

### O diretor

| Item | Informação |
|---|---|
| Cargo | CEO da Zoop desde 2010 |
| Formação | Administração na FGV, MBA em Gestão de Varejo na USP e pós em Marketing Estratégico no INSEAD |
| Trajetória | Mais de 20 anos no varejo: Diretor de Operações na Electra Brasil (2005 a 2010, reestruturação logística), Gerente de Marketing na TechWorld (2000 a 2005, marketing digital e +30% nas vendas de eletrônicos) |
| Perfil | Inovador, focado em eficiência e resultados, mentor de equipes; **prefere decidir com dados e usa inteligência de negócios** |
| Conquistas | Crescimento de mais de 200% em 10 anos, digitalização das operações e prêmio de inovação no varejo (2018) |
| Valores | Integridade, inovação e foco no cliente |

### A decisão

Duas decisões estratégicas que competem por caixa e atenção:
1. **Expansão internacional** da linha de eletrônicos, começando pela América Latina, sem histórico de vendas no exterior e com a logística internacional por construir.
2. **Reorganização do layout das lojas físicas** no Brasil, para vender mais produtos de maior valor (eletrodomésticos e automação residencial), sem pesquisa de mercado recente.

**Por que é urgente:** concorrentes expandem na América Latina, o tráfego das lojas físicas cai com a migração para o online, e a liderança e os acionistas pressionam por crescimento internacional. **Fatores internos:** equipe de vendas e atendimento muito eficiente no Brasil, mas sem experiência em logística internacional; caixa sólido, que precisa ser dividido entre as duas frentes. **Pressões externas:** TechPro e Electro World já operam na região, escassez de mão de obra para projetar lojas e complexidade de tarifas e normas de importação.

### O que os dados do projeto já dizem [D]

O projeto tem informação sobre o mercado doméstico, usada **só em proporções** porque a escala dos dados (cerca de R$ 16 milhões em três anos) não é a da empresa descrita (US$ 5 bilhões):

| Dado | O que indica para a decisão |
|---|---|
| Lojas físicas respondem por 66,2% das vendas e o e-commerce por 33,8%, estável entre regiões e perfis | A loja física ainda é a maior parte das vendas, e o online já pesa um terço |
| Produtos acima de R$ 1.000 são 22,7% das vendas e **63,7% da receita** | Destacar produtos de maior valor no layout tem lógica |
| Não há linha de *smart home* na base; o mais próximo é Câmera de segurança (1,7% da receita, −6,8% de crescimento) | **Não há evidência de demanda** de automação residencial nos dados de vendas |
| Sul (índice de 0,52), Norte (0,68) e Nordeste (0,77) vendem abaixo do peso da população; teto teórico de +20,4% nas vendas | Há **crescimento doméstico com evidência**, que a expansão internacional não tem |
| A base não tem identificador de cliente | Limita sistemas de recomendação por cliente |

**Inconsistências do material:** o diretor aparece como João Costa (módulos 1 e 6) e como Carlos Souza (e-mail do módulo 4); trato como o mesmo cargo. O perfil do diretor (decisões baseadas em dados) contrasta com o enunciado "sem dados".

---

## Prompt 2 · Projeção de cenários e análise de risco

### Os três cenários

Cada cenário combina as **duas decisões**, do menor ao maior risco:

| | Cenário 1 · Brasil primeiro | Cenário 2 · Piloto internacional + layout em fases | Cenário 3 · Expansão simultânea |
|---|---|---|---|
| **Perfil** | Conservador: baixo risco, impacto moderado | Expansão moderada: risco calculado, alto potencial | Agressivo: alto risco, grande impacto |
| **Internacional** | Só estudo de mercado e conversas exploratórias; nenhuma operação por 12 meses | Piloto de e-commerce (*digital-first*) em **um** país da América Latina, com parceiro ou startup local e suporte técnico local | Entrada em vários países com e-commerce e lojas físicas próprias |
| **Lojas físicas** | Reorganização em fases, começando por lojas-piloto, com destaque a produtos de maior valor e automação residencial | Reorganização em fases (igual ao Cenário 1) | Reorganização de todas as 200+ lojas ao mesmo tempo |
| **Aquisições** | Nenhuma | Parceria com opção de compra futura [S] | Aquisição de startups de automação e IA |
| **Decisão seguinte** | Revisão em 12 meses | Ponto de decisão (go, ajustar ou parar) após o piloto | Sem ponto de revisão previsto |

O Cenário 2 **contém** o Cenário 1: a diferença entre eles é o piloto internacional. Essa estrutura em camadas será importante na decisão final (Aula 6.3).

### Cenário 1 · Brasil primeiro

**Vantagens**
1. Risco baixo: opera onde a Zoop já tem equipe, marca e logística.
2. Usa as mais de 200 lojas, que ainda são a maior parte das vendas [D].
3. Destaca produtos de maior valor, que concentram a receita [D].
4. Preserva caixa para inovação e para a compra de startups.
5. Resultados rápidos de medir (tráfego, conversão e ticket por loja).
6. O aprendizado de layout é replicável em todas as lojas.
7. Responde à queda de tráfego nas lojas físicas.
8. A base doméstica tem evidência de crescimento nas regiões sub-exploradas [D].
9. Menor exposição a regulação, câmbio e tarifas.
10. Dá tempo para montar equipe e logística internacional com calma.

**Desvantagens**
1. Não responde à pressão por crescimento internacional.
2. TechPro e Electro World já operam na região, e a janela pode fechar.
3. Mantém a dependência do mercado brasileiro.
4. O crescimento fica limitado ao Brasil.
5. Contraria a visão de ser referência na América Latina.
6. Pode passar imagem de inércia a acionistas e à equipe.
7. O novo layout é decidido sem pesquisa recente e pode errar o formato.
8. A escassez de profissionais de design de loja atrasa o cronograma.
9. Entrar mais tarde pode custar mais [S].
10. Sem aprendizado internacional enquanto não houver um piloto.

**Riscos e mitigação**

| Risco | Mitigação |
|---|---|
| Perder a janela de entrada para concorrentes | Manter o estudo de mercado ativo e definir o gatilho para antecipar o piloto |
| Layout errado, sem pesquisa | Testar em poucas lojas, medir vendas por loja antes e depois, e só então expandir |
| Falta de profissionais de design | Parcerias externas e padrão modular de layout |
| Pressão dos acionistas por crescimento | Apresentar um cronograma com datas e metas para a fase internacional |

**Ganhos potenciais:** aumento do ticket médio e das vendas de produtos de maior valor; base para a expansão posterior. **Risco iminente:** perder espaço na América Latina para concorrentes enquanto a Zoop espera.

### Cenário 2 · Piloto internacional + layout em fases

**Vantagens**
1. Aprende com baixo custo: e-commerce em um país, sem lojas.
2. Responde à pressão por crescimento sem comprometer toda a operação.
3. O parceiro ou startup local supre a falta de experiência e logística.
4. Reorganiza as lojas em fases, ajustando a cada etapa.
5. Cria um ponto de decisão baseado em resultados reais do piloto.
6. Aproveita o crescimento do e-commerce e da automação residencial na região.
7. O suporte técnico local pode diferenciar a Zoop de importadores de preço baixo.
8. Combina inovação (IA e realidade aumentada) com a experiência na loja.
9. Preserva o caixa para ampliar apenas o que funcionar.
10. É reversível: o piloto pode ser encerrado com perda limitada.

**Desvantagens**
1. Duas frentes ao mesmo tempo dividem a atenção da liderança.
2. O piloto em um país pode não representar os demais mercados.
3. O resultado leva tempo, e a concorrência continua avançando.
4. O parceiro local cria dependência e risco de desalinhamento.
5. Logística e regulação internacional ainda precisam ser construídas do zero.
6. O custo das duas frentes pressiona o caixa.
7. Sem dados de mercado, a escolha do país é feita por julgamento.
8. Não há evidência de demanda por automação residencial nos dados de vendas [D].
9. O piloto pode ser pequeno demais para gerar um sinal confiável.
10. Pode criar a expectativa de expansão rápida que o piloto não sustenta.

**Riscos e mitigação**

| Risco | Mitigação |
|---|---|
| Escolher o país errado | Critérios de seleção definidos antes (tamanho do e-commerce, regulação, logística, concorrência) e comparação de 2 ou 3 países em um estudo curto |
| Dependência do parceiro | Contrato com cláusulas de saída, metas e acesso aos dados de clientes |
| Piloto pequeno demais | Definir antes o volume mínimo para uma conclusão confiável |
| Sobrecarga da equipe | Equipes dedicadas para o piloto e para o layout, e cronograma escalonado |
| Falha de suporte técnico em automação | Rede local de assistência antes de vender automação no piloto |

**Ganhos potenciais:** acesso a um novo mercado com perda limitada, dados reais para decidir a expansão e vantagem inicial em suporte técnico. **Risco iminente:** o piloto "dar certo" por razões locais que não se repetem em outros países.

### Cenário 3 · Expansão simultânea

**Vantagens**
1. Maior potencial de crescimento e de receita.
2. Posição de pioneira em automação residencial na região.
3. Resposta máxima à pressão de acionistas e concorrentes.
4. A aquisição de startups traz tecnologia, talentos e conhecimento local de uma vez.
5. Ganho de escala em compras e na marca regional.
6. Layout padronizado em todas as lojas reforça uma mensagem única de marca.
7. Ocupa espaço que concorrentes poderiam tomar.
8. Reduz mais cedo a dependência do mercado brasileiro.
9. Sinaliza ambição e atrai parcerias e investidores.
10. Se der certo, cria uma vantagem difícil de copiar.

**Desvantagens**
1. Risco muito alto, sem aprendizado prévio.
2. Compromete grande parte do caixa antes de validar o modelo.
3. Falta de logística internacional em vários países ao mesmo tempo.
4. Cada país tem regulação, tarifas e hábitos de consumo diferentes.
5. Lojas físicas no exterior exigem investimento fixo alto e são difíceis de reverter.
6. Reorganizar mais de 200 lojas de uma vez interrompe a operação e as vendas.
7. A escassez de mão de obra impede executar tudo em paralelo.
8. Integrar várias aquisições é complexo e caro.
9. Um erro de estratégia se repete em todos os mercados.
10. Se falhar, prejudica a reputação e o foco no Brasil.

**Riscos e mitigação**

| Risco | Mitigação |
|---|---|
| Falha de execução em vários países | Limitar a quantidade de frentes simultâneas |
| Perda de caixa sem retorno | Teto de investimento por etapa e liberação condicionada a metas |
| Interrupção das lojas durante a reorganização | Fazer em ondas, mesmo neste cenário |
| Integração das aquisições | Equipe dedicada e integração gradual |

**Ganhos potenciais:** maior retorno possível se tudo funcionar. **Riscos iminentes:** perda de caixa, ruptura de operação e dano à marca, sem ponto de saída.

### Recomendação

**O Cenário 2 oferece a melhor combinação de riscos controláveis e oportunidade estratégica.** Ele responde à pressão por crescimento, mantém o risco limitado, é reversível e gera dados reais, que é o que falta. O Cenário 1 é a alternativa se o diretor priorizar segurança, e o Cenário 3 só se justifica com muito mais evidência. A comparação numérica está na [Aula 6.3](matriz_multicriterio_e_decisao_final.md).

---

## Prompt 3 · Exploração de decisões intuitivas

### Rodada 1: perguntas adaptadas ao diretor

**Expansão internacional**
1. Quais desafios específicos você enxerga ao entrar na América Latina?
2. Que experiência passada pode ser aplicada?
3. A presença inicial deve ser digital, física ou uma combinação?

**Reorganização das lojas**
4. Como o novo layout deve mudar a experiência do cliente?
5. Como a loja deve se complementar com o e-commerce?

**Validação da intuição**
6. Que experiência acumulada pesa mais nesta decisão?
7. Que lições práticas de decisões anteriores se aplicam?
8. Como integrar inovação à experiência física?

**Plano intuitivo**
9. O que o motiva a escolher um caminho?
10. Que pressões internas e externas pesam?
11. Quais são as prioridades de curto prazo?

**Riscos e oportunidades**
12. Que risco oculto você teme?
13. Que oportunidade emergente enxerga?
14. Como pretende mitigar os riscos?

### Respostas do diretor (Notion)

| Tema | Resposta do diretor |
|---|---|
| Desafios da expansão | Logística e cultura: cada país tem particularidades que exigem adaptar o portfólio, a entrega e as regulações |
| Experiência aplicável | A expansão logística no Brasil (Electra) e a criação de uma cadeia eficiente; parcerias com empresas locais |
| Presença | Começar pelo **e-commerce**, com presença física planejada onde a cultura local valoriza a compra presencial |
| Lojas e experiência | Lojas mais interativas, com demonstrações, realidade aumentada e autoatendimento; a loja como complemento do online |
| Experiência acumulada | Na migração para o e-commerce, agilidade e capacidade de adaptação foram essenciais para reduzir o risco |
| Lições práticas | Inovação e antecipação de tendências foram decisivas; considera comprar startups locais para acelerar |
| Motivação | Manter a Zoop na vanguarda da inovação e ser pioneira em automação residencial em grande escala |
| Pressões | Equipe e acionistas esperam crescer e inovar; a concorrência internacional pressiona; quer crescer de forma sustentável e reforçar o Brasil |
| Prioridades | Testar novos conceitos de loja física **em mercados internacionais**, acelerar a digitalização no Brasil e fazer um piloto internacional |
| Risco oculto | Adaptação cultural; mitigar com testes-piloto em mercados menores |
| Oportunidade | Automação residencial com suporte técnico local |
| Mitigação | Entrada gradual com um país-piloto e teste de integração digital e físico em localidades diferentes |

### Validação da intuição

**Onde a experiência do diretor sustenta a intuição:**
- **Entrada gradual com país-piloto:** coerente com a lição da migração para o e-commerce (agilidade com flexibilidade) e com a restrição de falta de dados. É o que o Cenário 2 faz.
- **E-commerce primeiro:** reduz custo e exposição, e é onde a Zoop tem competência digital.
- **Parcerias locais:** replicam a lógica de adaptar a operação por região que ele aplicou no Brasil.
- **Loja como complemento do online:** os dados mostram que as lojas físicas ainda são 66,2% das vendas [D], então o papel de vitrine e experiência é plausível.

**Onde a intuição merece teste:**
1. **A experiência logística no Brasil pode não se transferir:** no exterior entram alfândega, tarifas, câmbio e normas de produto, que não existiam na operação doméstica.
2. **"Pioneira em grande escala" e "entrada gradual" puxam em sentidos opostos.** É preciso decidir qual vem primeiro.
3. **Lojas físicas internacionais como teste:** é a parte mais cara e menos reversível. Testar o novo conceito de loja **no Brasil**, onde a Zoop já tem lojas, é mais barato e depois exporta o que funcionou.
4. **Comprar startups locais** é bem menos reversível do que uma parceria. Uma parceria com opção de compra preserva a flexibilidade [S].
5. **Automação residencial é a aposta central, mas a base de vendas não mostra demanda** [D]. É preciso validar com uma pesquisa curta ou um teste de vendas antes de transformar a automação em eixo.
6. **O perfil do diretor prefere dados:** alguns dados baratos (pesquisa de mercado, teste de anúncios, análise de regulação) reduziriam a dependência de intuição.

### Plano de ação intuitivo (versão 1)

| Caminho | O que fazer | Quando [S] |
|---|---|---|
| **A · Brasil** | Reorganizar as lojas em fases com foco em automação, demonstração interativa e agendamento, e acelerar a digitalização | Fase 1 em 3 a 6 meses; ondas seguintes conforme resultados |
| **B · País-piloto** | E-commerce em um país da América Latina com parceiro local e suporte técnico local | Preparação em 3 meses; operação de 6 meses |
| **C · Revisão** | Avaliar os resultados do piloto antes de ampliar a expansão ou comprar startups | Ponto de decisão após o piloto |

### Riscos ocultos e oportunidades emergentes

**Riscos que ainda não estavam na mesa:**
- **Efeito vitrine:** o cliente experimenta na loja e compra no site de um concorrente.
- **Dependência do parceiro local:** acesso aos clientes, qualidade do atendimento e alinhamento de metas.
- **Sobrecarga da equipe** com duas frentes simultâneas.
- **Logística reversa e garantia no exterior:** trocas, devoluções e assistência técnica.
- **Medição omnichannel:** atribuir corretamente a venda entre loja e online.
- **Câmbio e preços** frente a importados baratos [S].

**Oportunidades emergentes:** suporte técnico local como diferencial em automação; pontos de retirada e de devolução nas lojas; dados do piloto como ativo para decidir aquisições; marketing local com influenciadores regionais.

**Mitigações:** critérios de escolha do país definidos antes; contrato de parceria com cláusulas de saída; teto de investimento e metas para o piloto; testar o novo layout no Brasil antes de exportá-lo; equipes separadas para cada frente.

### Rodada 2: processo refeito com as respostas

Com as respostas do diretor incorporadas, o plano fica assim:

1. **Meses 0 a 3 (preparação):** escolher os critérios e o país-piloto; selecionar o parceiro; mapear a regulação; escolher de 3 a 5 lojas brasileiras para a fase 1 do layout; definir as métricas do piloto.
2. **Meses 3 a 9 (execução):** lançar o e-commerce no país-piloto; reorganizar as lojas da fase 1; medir vendas por loja e o desempenho do piloto.
3. **Meses 9 a 12 (decisão):** ponto de decisão com três saídas: ampliar, ajustar ou parar.

**Perguntas para a próxima rodada (pendentes do diretor):**
1. Qual é a **perda máxima** que a Zoop aceita no piloto?
2. Que **critérios** definem o país-piloto (tamanho do e-commerce, regulação, proximidade logística)?
3. Qual será a **métrica de sucesso** do piloto, e quando ela deve ser atingida?
4. Em que condições a Zoop **compraria** uma startup, em vez de manter a parceria?
5. Quais lojas brasileiras entram na fase 1 do novo layout, e com que critério?

> **Próximo passo (Aula 6.2):** organizar a análise SWOT e o brainstorming colaborativo.
