# DECISIONS.md
**Projeto:** Brasil Público — Escala 6x1  
**Última atualização:** 2026-04-12  
**Responsável:** Brasil Público  

Este documento reúne as principais decisões metodológicas do projeto incluindo escolhas de dados, hipóteses adotadas e limitações já identificadas. A ideia é deixar claro não só *o que foi feito*, mas *por que foi feito assim* e onde o modelo ainda pode falhar.

---

## Índice
- [D01 — Dados: PNAD Contínua vs PNAD antiga](#d01)
- [D02 — Dados: Trimestre inicial e cobertura temporal](#d02)
- [D03 — Dados: Variável de horas trabalhadas](#d03)
- [D04 — Dados: Filtragem de ocupados](#d04)
- [D05 — Modelo: Identidade PIB = Horas × Produtividade](#d05)
- [D06 — Modelo: Abandono da âncora CNI](#d06)
- [D07 — Modelo: Fontes dos ganhos de produtividade](#d07)
- [D08 — Modelo: Faixa afetada — correção da coluna](#d08)
- [D09 — Limitações conhecidas do modelo agregado](#d09)
- [D10 — Modelo: Correspondência setorial PNAD × CNT](#d10)
- [D11 — Modelo: Hipótese forte da faixa 41–44h](#d11)
- [D12 — Modelo: Nomenclatura dos cenários](#d12)
- [D13 — Modelo: Cobertura diferencial PNAD × Contas Nacionais](#d13)
- [D14 — Modelo: Setores excluídos e subestimação](#d14)
- [D15 — Modelo: Interpretação da diferença em relação à CNI](#d15)

---

## D01 — Dados: PNAD Contínua vs PNAD antiga {#d01}

**Decisão:** trabalhar exclusivamente com a PNAD Contínua (2012–presente).

**Por quê:** a PNAD anual foi encerrada em 2015 e não é diretamente comparável com a versão contínua — há diferenças relevantes de metodologia, cobertura e definição de variáveis.

**Consequência:** abrimos mão de séries mais longas, mas ganhamos consistência. Para o objetivo do projeto, isso é mais importante.

**Referência:** IBGE, nota técnica (nov/2015).

---

## D02 — Dados: Trimestre inicial e cobertura temporal {#d02}

Optamos por usar os quatro trimestres de 2023 como base principal.

Isso nos dá uma fotografia recente, com boa representatividade e sem distorções de períodos atípicos (como pandemia).

**Arquivos utilizados:** PNADC_012023 a PNADC_042023  
**Total:** 1.900.989 observações  

**Layout:** `input_PNADC_trimestral.txt` (IBGE, versão 2022-10-31)

---

## D03 — Dados: Variável de horas trabalhadas {#d03}

**Escolha:** usar `VD4031` (horas habituais em todos os trabalhos).

Essa variável já vem consolidada pelo IBGE, somando múltiplos vínculos quando existem. Na prática, é a melhor aproximação da carga total de trabalho de cada pessoa.

**Ponto de atenção:** como é autodeclarada, pode carregar algum erro de memória ou arredondamento.

---

## D04 — Dados: Filtragem de ocupados {#d04}

Aqui não tem muito mistério: filtramos apenas quem estava efetivamente ocupado na semana de referência (`VD4002 == "1"`).

Depois do filtro, ficamos com:

- **815.737 observações**
- cerca de **42,9% da amostra original**

---

## D05 — Modelo: Identidade PIB = Horas × Produtividade {#d05}

A base do modelo é simples e conhecida:
PIB_i = N_i × H_i × P_i
Δ%PIB_i ≈ Δ%H_i + Δ%P_i


Assumimos o número de trabalhadores constante no curto prazo, o que permite essa aproximação de primeira ordem.

**Importante:** isso é um modelo *deliberadamente simplificado*. Ele não captura efeitos de demanda, preços ou mudanças estruturais mais profundas.

---

## D06 — Modelo: Abandono da âncora CNI {#d06}

**Decisão:** não usar o -0,7% da CNI como input do modelo.

A estimativa da CNI até pode ser útil como referência externa, mas não sabemos exatamente como ela foi construída. Incorporar esse número diretamente criaria uma inconsistência metodológica.

Em outras palavras: preferimos errar com transparência do que acertar sem saber por quê.

---

## D07 — Modelo: Fontes dos ganhos de produtividade {#d07}

Os cenários de produtividade foram definidos com base em literatura empírica:

| Cenário | Ganho por hora | Interpretação |
|---|---|---|
| Base | 0% | Nenhum ajuste |
| A | +3% | Conservador |
| B | +6% | Valor central |
| C | +9% | Limite otimista |

**Referências principais:**
- Collewet & Sauermann (2017) — call center holandês  
- Pencavel (2015) — indústria de guerra britânica contexto extremo  
- Experimentos na Islândia (2015–2019)

O cenário C existe mais como limite teórico do que como expectativa realista.

---

## D08 — Modelo: Faixa afetada — correção da coluna {#d08}

Uma correção importante foi feita em 2026-04-10.

Antes, estávamos incluindo trabalhadores com exatamente 40h — o que não faz sentido, já que eles não teriam redução.

**Antes:**
VD4031 >= 40 & VD4031 <= 44

**Agora:**
VD4031 > 40 & VD4031 <= 44


O impacto foi grande. Em alguns setores, a parcela afetada caiu drasticamente (ex: administração pública).

---

## D09 — Limitações conhecidas do modelo {#d09}

Nenhuma surpresa aqui — o modelo tem várias limitações, e é melhor deixá-las explícitas:

| Limitação | Gravidade | Tendência |
|---|---|---|
| Curto prazo / estático | Alta | Subestima médio prazo |
| Sem demanda agregada | Alta | Subestima ganhos |
| Uso de evidência internacional | Média | Incerto |
| Informalidade elevada | Média | Subestima impacto |
| Dados históricos (Pencavel) | Alta | Baixa validade externa |

---

## D10 — Modelo: Correspondência PNAD × CNT {#d10}

Um dos pontos mais 'chatos' do trabalho foi alinhar PNAD com Contas Nacionais.

As classificações simplesmente não batem.

O que fizemos foi construir uma correspondência prática:

| Setor PNAD | CNT | Observação |
|---|---|---|
| Agropecuária | agropecuaria | Direto |
| Indústria | ind_transformacao | Parcial |
| Construção | construcao | Direto |
| Comércio | comercio | Direto |
| Transporte | transporte | Direto |
| Informação | info_comunicacao | Parcial |
| Adm. pública | adm_publica_saude_educ | Amplo |

Alguns setores ficaram de fora.

**Resumo:** os valores absolutos pedem cautela mas a direção dos efeitos é robusta.

---

## D11 — Modelo: Hipótese da faixa 41–44h {#d11}

Aqui está uma das hipóteses mais fortes do modelo.

Assumimos que apenas trabalhadores entre **41h e 44h** seriam diretamente afetados.

Isso ignora três coisas importantes:
1. Quem trabalha acima de 44h  
2. Ajustes generalizados das empresas  
3. Informalidade  

A redução média assumida foi:

de 42h para 40h (**-4,76%**)

**Leitura correta:** isso puxa o resultado para baixo. O modelo tende a subestimar o impacto total.

---

## D12 — Modelo: Nomenclatura dos cenários {#d12}

Troca simples, mas necessária.

“Hipótese nula” foi substituído por **cenário base** que é um termo mais adequado fora de testes estatísticos formais.

---

## D13 — Modelo: PNAD vs Contas Nacionais {#d13}

As bases não medem exatamente a mesma coisa.

| Aspecto | PNAD | CNT |
|---|---|---|
| Cobertura | Parcial | Total |
| Informalidade | Subcaptada | Estimada |

Isso gera um efeito importante:

produtividade por hora tende a ser **superestimada** em setores informais

Decidimos não corrigir isso artificialmente apenas documentar.

---

## D14 — Modelo: Setores excluídos {#d14}

Alguns setores ficaram de fora por limitações de dados:

- Alojamento e alimentação  
- Saúde  
- Serviços domésticos  

Estimativa do impacto não capturado: **~R$ -28,2 bi**

Isso leva a uma faixa mais realista:

- Resultado mínimo: **-0,513%**
- Resultado provável: até **~ -0,77%**

---

## D15 — Modelo: Comparação com a CNI {#d15}

Evitamos uma leitura simplista do tipo:

> “nosso modelo é melhor” ou “mais otimista”

A forma mais honesta de colocar é:

> Sob hipóteses mais restritas e explícitas, estimamos -0,513%.  
> A CNI chega a -0,70% com uma metodologia não divulgada.

Ou seja: a diferença vem das hipóteses, não necessariamente da qualidade.

---

## D16 — Modelo: Adoção da Formulação C {#d16}

**Data:** 2026-04-11  

Aqui foi uma mudança relevante.

Testamos duas formas de calcular a redução de horas:

| Métrica | A | C |
|---|---|---|
| ΔH | -4,76% | -5,82% |
| ΔPIB | -0,513% | -0,627% |

A diferença não é pequena — ~18%.

Como isso ultrapassa o limite definido no próprio projeto, adotamos a **Formulação C como padrão**.

**Intuição:**  
reduções percentuais não são lineares. A média simples subestima o efeito real.

**Limitação que sobra:**  
não sabemos a distribuição exata dentro da faixa 41–44h. Se houver concentração em 44h, ainda podemos estar subestimando.

---

### Conclusão geral

O modelo não pretende ser definitivo.

Ele é, antes de tudo, **explícito**:
- deixa claro onde simplifica
- onde pode errar
- e em que direção tende a errar

Isso, no fim, é mais útil do que um número “fechado” sem contexto.

---

*Próxima atualização: inclusão completa dos cenários A, B e C (D16).*