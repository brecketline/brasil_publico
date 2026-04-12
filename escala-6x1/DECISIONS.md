# DECISIONS.md
**Projeto:** Brasil Público — Escala 6x1
**Última atualização:** 2026-04-10
**Responsável:** Brasil Público

Este arquivo documenta decisões metodológicas, fontes utilizadas, hipóteses assumidas e limitações conhecidas.

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

**Decisão:** usar exclusivamente a PNAD Contínua (2012–presente).

**Justificativa:** a PNAD anual foi descontinuada em 2015 e possui diferenças de cobertura, periodicidade e definição de variáveis incompatíveis com a PNAD Contínua.

**Impacto:** limita a série histórica a partir de 2012. Aceitável para o escopo.

**Referência:** IBGE, Nota técnica nov/2015.

---

## D02 — Dados: Trimestre inicial e cobertura temporal {#d02}

**Decisão:** usar os 4 trimestres de 2023 como base principal.

**Arquivos:** PNADC_012023 a PNADC_042023 — total 1.900.989 observações.

**Layout:** `input_PNADC_trimestral.txt` — IBGE, versão 2022-10-31.

---

## D03 — Dados: Variável de horas trabalhadas {#d03}

**Decisão:** usar `VD4031` (horas habituais em todos os trabalhos).

**Justificativa:** variável derivada pelo IBGE que consolida todos os vínculos. Mais representativa da carga total.

**Limitação:** autodeclarada, sujeita a viés de memória.

---

## D04 — Dados: Filtragem de ocupados {#d04}

**Decisão:** filtrar apenas `VD4002 == "1"` (ocupados na semana de referência).

**Resultado:** 815.737 observações (42,9% da amostra).

---

## D05 — Modelo: Identidade PIB = Horas × Produtividade {#d05}

**Identidade:**
```
PIB_i = N_i × H_i × P_i
Δ%PIB_i ≈ Δ%H_i + Δ%P_i  (N constante, aproximação 1ª ordem)
```

**Limitação:** não captura efeitos de demanda, preços, longo prazo ou heterogeneidade intrasetorial.

---

## D06 — Modelo: Abandono da âncora CNI {#d06}

**Decisão:** não usar o -0,7% da CNI como insumo. Tratar apenas como referência de comparação.

**Justificativa:** o -0,7% da CNI implica elasticidade implícita de ~0,077 com estrutura não documentada. Misturá-lo ao nosso modelo gera inconsistência metodológica.

---

## D07 — Modelo: Fontes dos ganhos de produtividade {#d07}

**Cenários de ganho definidos:**

| Cenário | Ganho P/hora | Referência principal |
|---|---|---|
| Base | 0% | — |
| A | +3% | Estimativa conservadora |
| B | +6% | Collewet & Sauermann (2017) |
| C | +9% | Pencavel (2015) — limite superior ⚠️ |

**Collewet & Sauermann (2017):** Labour Economics, 47, 96–106. Call center holandês, n=332, 6 anos.

**Pencavel (2015):** The Economic Journal, 125(589). Munições britânicas, 1914. ⚠️ Contexto muito diferente.

**Islândia (2015–2019):** setor público, sem queda de produtividade. Fonte: Autonomy/ALDA (2021).

---

## D08 — Modelo: Faixa afetada — correção da coluna {#d08}

**Correção (2026-04-10):** versão anterior usava `(VD4031 >= 40) & (VD4031 <= 44)`, incluindo trabalhadores em 40h exatas que não precisam reduzir jornada.

**Correto:** `(VD4031 > 40) & (VD4031 <= 44)`.

**Impacto:** redução expressiva nas parcelas afetadas. Exemplo: Adm. pública passou de 65,7% → 5,5%.

---

## D09 — Limitações conhecidas do modelo {#d09}

| Limitação | Nível | Direção do viés |
|---|---|---|
| Modelo estático, curto prazo | Alto | Neutro/subestima médio prazo |
| Sem demanda agregada | Alto | Subestima ganhos |
| Ganhos de produtividade internacionais | Médio | Incerto |
| Informalidade (~39% dos ocupados) | Médio | Subestima parcela afetada |
| Pencavel (2015) = dados de 1914 | Alto | Não generalizável |

---

## D10 — Modelo: Correspondência setorial PNAD × CNT {#d10}

**Problema:** PNAD usa ~11 grupamentos (VD4010); CNT usa ~12 atividades econômicas. Não há mapeamento oficial direto.

**Tabela de correspondência adotada:**

| Setor PNAD | Coluna CNT | Qualidade |
|---|---|---|
| Agropecuária | agropecuaria |  Direta |
| Indústria geral | ind_transformacao | Parcial (~60% do VA industrial) |
| Construção | construcao | Direta |
| Comércio e rep. | comercio | Direta |
| Transp. e armaz. | transporte | Direta |
| Inf. e serv. prof. | info_comunicacao | Parcial |
| Adm. públ. e educação | adm_publica_saude_educ | Ampla — agrega saúde e educação públicas |
| Alojamento e alim. | outros_servicos | Excluída |
| Saúde | adm_publica_saude_educ | Excluída |
| Serv. domésticos | outros_servicos | Excluída |

**Consequência:** magnitude dos setores deve ser interpretada com cautela. Direção do impacto é confiável.

---

## D11 — Modelo: Hipótese forte da faixa 41–44h {#d11}

**Hipótese:** apenas trabalhadores com 41h < VD4031 ≤ 44h são diretamente afetados.

**O que essa hipótese ignora:**
1. Trabalhadores acima de 44h que também reduziriam
2. Efeito de contágio: empregadores podem uniformizar jornada para todos
3. Trabalhadores informais nessa faixa sem proteção legal

**Redução assumida:** de 42h (média da faixa) para 40h = **-4,76%**.

**Direção do viés:** o modelo subestima o impacto total. O resultado de -0,513% é um **limite inferior**.

---

## D12 — Modelo: Nomenclatura dos cenários {#d12}

**Decisão:** substituir "hipótese nula" por "cenário base".

**Justificativa:** "hipótese nula" tem conotação estatística específica. O correto é "cenário base" — produtividade por hora constante após redução de jornada.

**Nomenclatura adotada:**

| Nome | Δ produtividade/hora | Interpretação |
|---|---|---|
| Cenário base | 0% | Sem ajuste de eficiência. Impacto máximo esperado. |
| Cenário A | +3% | Compensação parcial conservadora |
| Cenário B | +6% | Linha central da literatura |
| Cenário C | +9% | Limite superior otimista |

---

## D13 — Modelo: Cobertura diferencial PNAD × Contas Nacionais {#d13}

**Problema:** as bases têm coberturas diferentes.

| Dimensão | PNAD | CNT |
|---|---|---|
| Trabalhadores | Formal + informal (parcial) | Toda a economia (inclui estimativas informais) |
| Setor informal | Parcialmente captado | Estimado por métodos indiretos |

**Consequência:** produtividade por hora é **superestimada** em setores com alta informalidade (Agropecuária, Construção) porque o denominador (horas da PNAD) subestima o total real de horas.

**Postura:** usar os dados como estão e documentar a limitação. Sem correções ad hoc.

---

## D14 — Modelo: Setores excluídos e subestimação {#d14}

**Setores excluídos:**

| Setor | Motivo | Impacto potencial não capturado |
|---|---|---|
| Alojamento e alim. | Coluna CNT muito agregada | ~R$ -13,6 bi |
| Saúde | VAB não separável da Adm. pública | ~R$ -7,1 bi |
| Serv. domésticos | VAB formal irrisório | ~R$ -7,5 bi |

**Total potencialmente subestimado:** ~R$ -28,2 bi

**Faixa de incerteza do modelo:**
- **Resultado reportado (setores incluídos):** -0,513%
- **Resultado com todos os setores (proxies imperfeitas):** ~-0,77%
- **Referência CNI:** -0,70%

O resultado de -0,513% é o **limite inferior conservador**. O resultado real provavelmente está entre -0,513% e -0,77%.

---

## D15 — Modelo: Interpretação da diferença em relação à CNI {#d15}

**Formulação incorreta:**
> "Nosso modelo é menos pessimista que a CNI."

**Formulação correta:**
> "Sob hipóteses mais restritas e transparentes — faixa 41–44h apenas, sem efeitos de segunda ordem — o modelo estima -0,513% no PIB. A CNI estima -0,70% com metodologia não publicada, possivelmente incluindo efeitos de custos trabalhistas e perda de competitividade não capturados aqui."

**Comparação dos modelos:**

| Elemento | Nosso modelo | CNI |
|---|---|---|
| Faixa afetada | 41–44h apenas | Não documentado |
| Efeitos de segunda ordem | Não incluídos | Possivelmente incluídos |
| Transparência | Total — código aberto | Não publicada |
| Resultado (cenário base) | -0,513% | -0,70% |

**Conclusão:** a diferença de 0,187 pp não indica que um modelo está certo e o outro errado. Indica hipóteses diferentes. A contribuição do projeto é tornar as hipóteses explícitas e auditáveis.

---

*Próxima atualização: após implementação dos cenários A, B e C (D16).*

---

## D16 — Modelo: Adoção da Formulação C como padrão de ΔH {#d16}

**Data da decisão:** 2026-04-11

**Contexto:** o modelo utilizava Formulação A (ΔH = redução da média da faixa 41–44h = -4,76%) como estimativa da intensidade de redução de horas para trabalhadores afetados.

**Teste de robustez realizado:** comparação com Formulação C (média ponderada das reduções individuais dentro da faixa 41–44h, assumindo distribuição uniforme) com escopo idêntico.

**Resultado do teste:**

| Métrica | Formulação A | Formulação C |
|---|---|---|
| ΔH assumido | -4,7619% | -5,8171% |
| ΔPIB agregado | -0,5134% | -0,6272% |
| Viés relativo | 18,14% | — (referência) |

**Critério de decisão (definido a priori no notebook):**
- Viés < 5%: A adequada
- Viés 5–15%: viés moderado
- Viés > 15%: A inadequada, adotar C

**Resultado:** viés de 18,14% → acima do limiar. **Formulação C adotada como padrão.**

**Justificativa matemática:**
A Formulação A usa a média da faixa (42h) como referência, aplicando ΔH = (40-42)/42 = -4,76% uniformemente. A Formulação C calcula a média ponderada das reduções individuais:

```
ΔH_C = média[ (40-41)/41, (40-42)/42, (40-43)/43, (40-44)/44 ]
     = média[ -2,44%, -4,76%, -6,98%, -9,09% ]
     = -5,82%
```

A diferença ocorre porque a função ΔH(h) = (40-h)/h é côncava — a média das reduções individuais é maior (em módulo) do que a redução da média. A Formulação A subestima sistematicamente o ΔH médio da faixa.

**Limitação remanescente da Formulação C:**
A distribuição real dentro da faixa 41–44h provavelmente não é uniforme. Há provável concentração em 44h exatas (por convenção coletiva e contratos padronizados). Se a distribuição for mais concentrada em 44h, a Formulação C subestima o ΔH real; se mais concentrada em 41h, superestima. Sem microdados por hora exata dentro da faixa, não é possível calcular a distribuição real.

**Impacto na faixa de incerteza do modelo:**

| Versão | Cenário base | Limite superior |
|---|---|---|
| Com Formulação A | -0,513% | -0,770% |
| Com Formulação C | -0,627% | ~-0,940% |

**Impacto interpretativo:** com Formulação C, o cenário base (-0,627%) converge para a mesma ordem de grandeza da referência CNI (-0,700%). Isso não implica validação cruzada — as metodologias ainda são distintas — mas reduz a distância entre os modelos e torna as comparações mais cautelosas.

---
