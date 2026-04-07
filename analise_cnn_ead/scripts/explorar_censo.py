import pandas as pd

CAMINHO = "data/raw/censo_exemplo.csv"

try:
    df = pd.read_csv(CAMINHO, sep=";", encoding="latin-1")
except FileNotFoundError:
    print(f"Arquivo não encontrado: {CAMINHO}")
    print("Isso é esperado por enquanto — no Módulo 2 fazemos o download real.")
    exit()

print("=" * 50)
print("INSPEÇÃO INICIAL DOS DADOS")
print("=" * 50)

linhas, colunas = df.shape
print(f"\nTamanho: {linhas:,} linhas × {colunas} colunas")
print("\nColunas e tipos de dado:")
print(df.dtypes)
print("\nValores faltando por coluna:")
faltando = df.isnull().sum()
if faltando_relevante.empty:
    print("Nenhum valor faltando.")
else:
    print(faltando_relevante)
print("\nPrimeiras 3 linhas dos dados:")
print(df.head(3))
