import pandas as pd

dados = pd.read_csv("dados/vendas_lumina.csv")

dados["data"] = pd.to_datetime(dados["data"])

print(dados.head())

print(dados.dtypes)

dados["faturamento"] = dados["preco"] * dados["quantidade"]
faturamento_total = dados["faturamento"].sum()

print("Faturamento total da loja:")
print(faturamento_total)
print(dados.head())

faturamento_por_produto = dados.groupby("produto")["faturamento"].sum()

print("\nFaturamento por produto:")
print(faturamento_por_produto)