

## Análise 01 — EAD está substituindo universidades?

**Contexto:** Em setembro de 2025, a CNN Brasil reportou que o EAD
cresceu 286,7% em dez anos e que o ensino presencial caiu 22,3%
no mesmo período, sugerindo substituição de modalidade.
Fonte: https://www.cnnbrasil.com.br/educacao/ead-cresce-quase-300-em-dez-anos-diz-inep/

**O que investigamos:** A narrativa de substituição é verdadeira?
Ou o EAD expandiu o acesso para quem antes não estudava?

**Fonte dos dados:**
- INEP, Censo da Educação Superior 2014
- INEP, Censo da Educação Superior 2024
- Acesso: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior

**O que encontramos:**

| Indicador | 2014 | 2024 | Variação |
|-----------|------|------|----------|
| Total de matrículas | 7,8M | 10,2M | +30,5% |
| Matrículas presenciais | 6,5M | 5,0M | -22,5% |
| Matrículas EAD | 1,3M | 5,2M | +286,7% |
| Share EAD | 17,1% | 50,7% | +33,6 p.p. |
| Conclusão presencial | 12,9% | 14,5% | +1,6 p.p. |
| Conclusão EAD | 14,1% | 11,7% | -2,4 p.p. |

**O dado que a CNN não mostrou:**

O EAD ganhou 3,8 milhões de estudantes. O presencial perdeu 1,4 milhão.
A diferença: 2,4 milhões de pessoas, são estudantes que não
existiam no sistema antes. Não migraram do presencial, entraram
pela primeira vez no ensino superior.

Isso é consistente com os dados de faixa etária: 26% dos alunos
EAD têm entre 30 e 34 anos, contra 8% no presencial. Esse perfil
é de adultos que trabalham, não de jovens migrando de modalidade.

**O dado honesto que não escondemos:**


A taxa de conclusão do EAD caiu 2,4 pontos percentuais no período. Parte dessa queda pode refletir o fato de que o EAD passou a incluir pessoas com mais barreiras reais para concluir um curso: quem trabalha, quem tem filho, quem depende de internet instável. Mas o dado existe e está aqui.

**Notebooks:**
- `notebooks/modulo2_download_inep.ipynb` — ingestão e análise 2024
- `notebooks/modulo3_serie_temporal.ipynb` — comparação 2014 vs 2024
- `notebooks/modulo4_visualizacao.ipynb` — gráficos

**Decisões analíticas:** ver `DECISIONS.md`

---

## Como reproduzir
```bash
git clone https://github.com/brecketline/brasil_publico.git
cd brasil_publico
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Os arquivos de dados brutos não são versionados (`.gitignore`).
> Baixe os microdados do INEP pelo link acima e coloque em `data/raw/`.

---

## Estrutura
```
brasil_publico/
├── data/
│   ├── raw/          ← dados originais (não versionados)
│   └── clean/        ← dados processados
├── notebooks/        ← análises por módulo
├── visuals/          ← gráficos gerados
├── posts/            ← roteiros dos posts do Instagram
├── DECISIONS.md      ← diário de decisões analíticas
└── requirements.txt
```

---

## Licença

MIT — scripts e análises livres para uso com atribuição.
Dados originais: INEP/MEC.