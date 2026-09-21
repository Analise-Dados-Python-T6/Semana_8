import pandas as pd

pedidos = pd.read_csv("pedidos_sabor_caseiro.csv")

clientes = pedidos[["cliente"]].drop_duplicates().reset_index(drop=True)
clientes["id_cliente"] = clientes.index + 1

tabela_pedidos = pedidos.merge(clientes, on="cliente")

print(clientes)
print(tabela_pedidos.head())
