"""
Script: download_dados.py
Projeto: Brasil Público — Escala 6x1

Baixa os arquivos de dados brutos necessários para reproduzir o projeto.
Execução: python3 scripts/download_dados.py
          (rodar da raiz do projeto)
"""

import urllib.request
import os
from pathlib import Path

BASE = next(p for p in [Path().resolve()] + list(Path().resolve().parents)
            if (p / "DECISIONS.md").exists())
DIR_RAW = BASE / "data/raw/ibge"
DIR_RAW.mkdir(parents=True, exist_ok=True)

ARQUIVOS = [
    # (url, nome_local, tamanho_esperado_mb)
    (
        "https://ftp.ibge.gov.br/Trabalho_e_Rendimento/"
        "Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/"
        "Trimestral/Microdados/2023/PNADC_012023.txt",
        "PNADC_012023.txt", 196
    ),
    (
        "https://ftp.ibge.gov.br/Trabalho_e_Rendimento/"
        "Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/"
        "Trimestral/Microdados/2023/PNADC_022023.txt",
        "PNADC_022023.txt", 198
    ),
    (
        "https://ftp.ibge.gov.br/Trabalho_e_Rendimento/"
        "Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/"
        "Trimestral/Microdados/2023/PNADC_032023.txt",
        "PNADC_032023.txt", 202
    ),
    (
        "https://ftp.ibge.gov.br/Trabalho_e_Rendimento/"
        "Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/"
        "Trimestral/Microdados/2023/PNADC_042023.txt",
        "PNADC_042023.txt", 199
    ),
    (
        "https://ftp.ibge.gov.br/Contas_Nacionais/"
        "Contas_Nacionais_Trimestrais/Tabelas_Completas/"
        "Tab_Compl_CNT.zip",
        "Tab_Compl_CNT.zip", 350
    ),
]


def baixar(url, destino, tamanho_mb):
    if destino.exists():
        tamanho_atual = destino.stat().st_size / 1024 / 1024
        if tamanho_atual > tamanho_mb * 0.9:
            print(f"  Já existe: {destino.name} ({tamanho_atual:.0f} MB)")
            return
        else:
            print(
                f"  Arquivo incompleto ({tamanho_atual:.0f} MB), baixando novamente...")

    print(f"  Baixando {destino.name} (~{tamanho_mb} MB)...",
          end=" ", flush=True)

    def progresso(count, block_size, total_size):
        if total_size > 0:
            pct = min(count * block_size / total_size * 100, 100)
            print(f"\r  Baixando {destino.name} (~{tamanho_mb} MB)... {pct:.0f}%",
                  end="", flush=True)

    try:
        urllib.request.urlretrieve(url, destino, reporthook=progresso)
        tamanho = destino.stat().st_size / 1024 / 1024
        print(f"\r  {destino.name} ({tamanho:.0f} MB)")
    except Exception as e:
        print(f"\r  Erro ao baixar {destino.name}: {e}")


print("Brasil Público — Download de dados brutos")
print(f"Destino: {DIR_RAW}")
print()

for url, nome, tamanho in ARQUIVOS:
    baixar(url, DIR_RAW / nome, tamanho)

print()
print("Próximo passo:")
print("  Se baixou Tab_Compl_CNT.zip, descompacte em data/raw/ibge/")
print("  e renomeie o .xls para Tab_Compl_CNT_4T25.xls se necessário.")
print()
print("  Depois siga a ordem de execução dos notebooks em data/raw/ibge/SOURCES.md")
