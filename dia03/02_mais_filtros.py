#%%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv",sep = ";")
df.head()
# %%
filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 11)
df[filtro]
# %%
filtro = df["IdProduto"].isin([5,11])
df[filtro]
# %%
clientes = pd.read_csv("../data/clientes.csv",sep = ";")
clientes.head()
#
# %%
# Somente clientes que a data de criação está completa, ainda que errada
filtro = clientes["DtCriacao"].notna()
clientes[filtro]
# %%
# As duas linhas abaixo têm o mesmo resultado: selecionar valores NÃO NULOS.
# A primeira (`~.isna()`) inverte a lógica de "é nulo", enquanto a segunda (`.notna()`) checa diretamente por "não é nulo".
# ~clientes["DtCriacao"].isna()
# clientes["DtCriacao"].notna()