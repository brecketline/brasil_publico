### [2024-05] Arquivo de cursos vs arquivo de IES — Censo 2024

**Contexto:** O ZIP do Censo 2024 contém dois CSVs: um de instituições
(1MB) e um de cursos (453MB).

**Problema:** O código inicial apontava para `csvs[0]`, que era o arquivo
de IES. A análise de matrículas exige o arquivo de cursos.

**Decisão:** Inspecionar o tamanho dos arquivos antes de ler. O arquivo
de cursos é sempre o maior. Atualizado para `csvs[1]`.

**Impacto:** Crítico. Sem essa correção o DataFrame não teria nenhuma
coluna de matrícula.

---

### [2024-06] Nome da coluna de matrículas — Censo 2024

**Contexto:** Em anos anteriores a coluna se chamava `QT_MATRICULA_TOTAL`.
No Censo 2024 o nome é `QT_MAT`.

**Decisão:** Sempre inspecionar o cabeçalho antes de ler o arquivo
completo. Mapeamento documentado por ano.

**Impacto:** Sem essa verificação, o pandas ignoraria a coluna
silenciosamente e a análise retornaria zeros.

---

### [2024-07] Download manual do Censo 2014

**Contexto:** O servidor do INEP (`download.inep.gov.br`) não valida
corretamente o certificado SSL com o ambiente virtual Python no Mac.

**Problema:** `requests.get()` levantava `SSLCertVerificationError`.
O arquivo era criado mas vazio — corrompido.

**Decisão:** Download manual pelo navegador para o Censo 2014. O ZIP
foi extraído pelo macOS e os CSVs movidos para `data/raw/censo_2014/`
manualmente.

**Alternativa para automatizar futuramente:** `requests.get(url,
verify=False)` com `urllib3.disable_warnings()` — aceitável para
dados públicos em ambiente local.

**Impacto:** Não afeta a análise, os dados são idênticos
independente do método de download.

---

### [2024-08] Taxa de conclusão como proxy, não como evasão real

**Contexto:** O Censo não rastreia o estudante individualmente ao longo
do tempo, registra matrículas ativas por ano.

**Problema:** Calcular `QT_CONC / QT_MAT` não é taxa de evasão real.
Quem conclui em 2024 entrou ~4 anos antes, são populações diferentes.

**Decisão:** Usar a métrica como proxy comparativo entre modalidades,
com nota explícita de limitação em todo lugar que o número aparece.

**Impacto:** A diferença de 2,8 pontos percentuais entre EAD e
presencial é válida como sinal não como medida precisa de evasão.

---

### [2024-09] Viés de seleção na comparação 2014 vs 2024

**Contexto:** A taxa de conclusão do EAD caiu de 14,1% para 11,7%
entre 2014 e 2024.

**Problema:** Comparar as duas taxas diretamente ignora que a população
mudou. Em 2014 o EAD atendia 1,3 milhão de pessoas com perfil mais
homogêneo. Em 2024 atende 5,2 milhões, incluindo adultos trabalhadores,
pessoas de baixa renda e regiões com infraestrutura precária.

**Decisão:** Sempre contextualizar a queda de conclusão com os dados
de faixa etária que mostram que o EAD 2024 atende proporcionalmente
3x mais pessoas de 30-34 anos que o presencial.

**Impacto:** Evita a conclusão incorreta de que "o EAD piorou".
A queda pode refletir inclusão de população com mais barreiras,
não degradação do serviço.
