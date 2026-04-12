# Brasil Público — Escala 6x1

Você provavelmente já viu a manchete: se a jornada de trabalho cair de 44 horas para 40 horas por semana, o Brasil perderia **R$ 77 bilhões**. É um número grande, que soa definitivo. Mas de onde ele vem, exatamente?

Essa pergunta é o ponto de partida deste projeto.

A CNI (Confederação Nacional da Indústria) publicou em Abril de 2026 uma projeção apontando queda de **0,7% no PIB** com a redução da jornada. A estimativa é séria e merece atenção. O problema é que ela chegou sem metodologia publicada — sem explicar quais suposições foram feitas para chegar ali. E suposições, nesse tipo de cálculo, mudam tudo.

Este modelo, construído com dados públicos do IBGE, busca entender como esse impacto é calculado e o que acontece com o resultado quando variamos as premissas. O impacto não é um número fixo: é um intervalo que depende de hipóteses que raramente aparecem na manchete.

## O que este projeto faz

Usando microdados da **PNAD Contínua 2023** e as **Contas Nacionais Trimestrais do IBGE**, o projeto estima o impacto setorial da redução de jornada sob diferentes combinações de hipóteses:
* Quem seria afetado?
* Quanto as horas cairiam na prática?
* O que aconteceria com a produtividade por hora trabalhada?

O resultado é apresentado como um mapa: dependendo do que você assume, o impacto pode variar de **-0,627%** até próximo de zero (ou até positivo). A referência da CNI (-0,700%) está dentro desse espaço, a apenas **0,073 ponto percentual** do nosso cenário base.

## O que os dados mostram

Antes da simulação, é preciso olhar para a realidade do mercado:
* **34,6%** dos trabalhadores já cumprem exatamente 40h semanais (não seriam afetados).
* **19,4%** trabalham entre 41h e 44h (seriam os diretamente afetados). 

> **Conclusão:** Menos de 1 em cada 5 trabalhadores brasileiros seriam atingidos pela mudança. 

O efeito é concentrado e setorialmente assimétrico. **Comércio e Indústria** seriam os mais afetados em termos relativos, enquanto a **Administração Pública** seria a menos afetada proporcionalmente.

## Como o modelo funciona

O modelo parte de uma identidade contábil simples: o PIB é o produto entre horas trabalhadas e produtividade por hora. 

### Estrutura do Cálculo
Para cada setor incluído na simulação, o cálculo segue esta estrutura:

$$\Delta VAB_{setor} = VAB_{setor} \times parcela\_afetada \times (\Delta H + \Delta P_{setor})$$
$$\Delta PIB = \frac{\sum \Delta VAB_{setor}}{PIB_{total}}$$

Onde:
* **$\Delta H$**: Variação nas horas trabalhadas (calculada em **-5,82%** via média ponderada).
* **$\Delta P$**: Ganho de produtividade por hora.

## Resultados

| Hipótese sobre produtividade | $\Delta$ PIB estimado |
| :--- | :--- |
| Não muda (cenário base) | **-0,627%** |
| Sobe 3% por hora | **-0,290%** |
| Sobe 6% por hora | **+0,048%** |
| Sobe 9% por hora | **+0,386%** |

*A estimativa da CNI (-0,700%) está a 0,073 pp do nosso cenário base.*

## Limitações

* O modelo é de primeira ordem (não captura efeitos de demanda agregada ou preços).
* O setor informal está apenas parcialmente representado.
* Três setores foram excluídos por inconsistência de classificação entre PNAD e Contas Nacionais.

Documentação completa das decisões em: [`DECISIONS.md`](DECISIONS.md).

## Estrutura do Projeto

```text
escala-6x1/
├── data/
│   ├── raw/ibge/          # Dados brutos
│   └── processed/         # Dados processados
├── notebooks/
│   ├── 01_exploracao/     # Análise inicial
│   ├── 02_limpeza/        # Harmonização de bases
│   ├── 03_modelagem/      # Modelo e hipóteses
│   └── 05_storytelling/   # Comunicação
├── outputs/               # Figuras e tabelas exportadas
├── scripts/               # Automação de download
├── DECISIONS.md           # Metodologia detalhada
└── README.md
```
Este projeto faz parte do Brasil Público, um repositório de análises de dados sobre notícias veiculadas no Brasil.


