import pandas as pd
import matplotlib.pyplot as plt

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

faturamento_por_produto.plot(kind="bar")

plt.title("Faturamento por Produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento")

plt.savefig("grafico_faturamento_produto.png")
plt.show()

faturamento_por_categoria = dados.groupby("categoria")["faturamento"].sum()

print("\nFaturamento por categoria:")
print(faturamento_por_categoria)

faturamento_por_dia = dados.groupby('data')["faturamento"].sum()

print("\nFaturamento por dia:")
print(faturamento_por_dia)

melhor_dia = faturamento_por_dia.idxmax()
maior_faturamento = faturamento_por_dia.max()

print("\nMelhor dia de vendas:")
print(melhor_dia)

print("\nMaior faturamento em um dia:")
print(maior_faturamento)

quantidade_por_produto = dados.groupby("produto")["quantidade"].sum()

print("\nQuantidade vendida por produto:")
print(quantidade_por_produto)

produto_mais_vendido = quantidade_por_produto.idxmax()
maior_quantidade = quantidade_por_produto.max()

print("\nProduto mais vendido:")
print(produto_mais_vendido)

print("\nQuantidade vendida do produto mais vendido:")
print(maior_quantidade)

quantidade_vendas = len(dados)

ticket_medio = faturamento_total / quantidade_vendas

print("\nQuantidade de vendas:")
print(quantidade_vendas)

print("\nTicket médio:")
print(ticket_medio)