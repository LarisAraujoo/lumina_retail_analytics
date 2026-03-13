import pandas as pd

dados = pd.read_csv("dados/vendas_lumina.csv")

dados["data"] = pd.to_datetime(dados["data"])

print(dados.head())

print(dados.dtypes)
