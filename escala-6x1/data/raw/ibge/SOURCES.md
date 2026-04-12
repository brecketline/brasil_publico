# Fontes de Dados

Este arquivo documenta de onde vêm os dados brutos do projeto
e como reconstruí-los do zero.

Os arquivos brutos **não estão versionados** por duas razões:
tamanho (>800MB no total) e restrições de redistribuição do IBGE.
Siga as instruções abaixo para reproduzir o pipeline completo.

---

## 1. PNAD Contínua 2023 — Microdados Trimestrais

**Fonte:** IBGE — FTP público  
**Versão utilizada:** atualização de 2025-08-15

### Arquivos de dados (salvar em `data/raw/ibge/`)

Acesse: https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/2023/

Baixar:
- `PNADC_012023.txt` (~196 MB)
- `PNADC_022023.txt` (~198 MB)
- `PNADC_032023.txt` (~202 MB)
- `PNADC_042023.txt` (~199 MB)

### Documentação (salvar em `data/raw/ibge/Dicionario_e_input_20221031/`)

Acesse: https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Trimestral/Microdados/Documentacao/

Baixar e descompactar a pasta `Dicionario_e_input_XXXXXXXX` mais recente.  
Arquivos necessários dentro dela:
- `input_PNADC_trimestral.txt` — layout das colunas (largura fixa)
- `dicionario_PNADC_microdados_trimestral.xls` — descrição das variáveis

---

## 2. Contas Nacionais Trimestrais — Tabelas Completas

**Fonte:** IBGE — FTP público  
**Versão utilizada:** Tab_Compl_CNT_4T25.xls (atualização 2026-03-03)

Acesse: https://ftp.ibge.gov.br/Contas_Nacionais/Contas_Nacionais_Trimestrais/Tabelas_Completas/

Baixar: `Tab_Compl_CNT.zip`  
Descompactar e salvar `Tab_Compl_CNT_4T25.xls` em `data/raw/ibge/`

**Aba utilizada:** `Valores Correntes`  
**Colunas utilizadas:** agropecuaria, ind_transformacao, construcao, comercio,
transporte, info_comunicacao, adm_publica_saude_educ, pib_total

---

## 3. Download automatizado

Para baixar os arquivos da PNAD automaticamente, execute:

```bash
python3 scripts/download_dados.py
```

O script baixa os quatro trimestres de 2023 e o arquivo da CNT,
verificando integridade pelo tamanho dos arquivos.

---

## 4. Ordem de execução dos notebooks

Após baixar os dados brutos, execute os notebooks na seguinte ordem:

```
1. notebooks/01_exploracao/construir_anual_2023.ipynb
   → lê os 4 trimestres e gera data/processed/pnadc_2023_anual.csv

2. notebooks/02_limpeza/recalcular_faixas_horas.ipynb
   → gera data/processed/horas_por_setor_2023_corrigido.csv

3. notebooks/02_limpeza/extrair_pib_setorial.ipynb
   → gera data/processed/pib_setorial_2012_2023.csv

4. notebooks/03_modelagem/base_analitica_setorial_v4.ipynb
   → gera data/processed/base_analitica_setorial_2023.csv
   → gera outputs/tables/cenario_base_setorial.csv

5. notebooks/03_modelagem/mapeamento_hipoteses.ipynb
   → gera outputs/tables/matriz_hipoteses_completa.csv
   → gera outputs/tables/normalizacao_setorial.csv
   → gera outputs/figures/12_mapeamento_hipoteses.png
   → gera outputs/figures/13_normalizacao_setorial.png

6. notebooks/04_validacao/pipeline_checklist.ipynb
   → verifica consistência de todo o pipeline

7. notebooks/04_validacao/validacao_outputs_graficos.ipynb
   → verifica que os valores dos gráficos são rastreáveis
```

---

## 5. Referência externa

**CNI (2026)** — projeção de impacto da redução de jornada  
Reportada por: PlatôBR, 07/04/2026  
URL: https://platobr.com.br/a-queda-no-pib-prevista-pela-cni-caso-a-jornada-de-trabalho-seja-reduzida  
Metodologia: não publicada — tratada como referência externa de comparação
