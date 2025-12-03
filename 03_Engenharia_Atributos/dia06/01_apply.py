#%%
import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()


# %%
idCliente = "001749bd-37b5-4b1e-8111-f9fbba90f530"

def get_last_id(x):
    return x.split("-")[-1]

# %%
get_last_id("001749bd-37b5-4b1e-8111-f9fbba90f530")

# %%
# Essa forma é arcaica
id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%
# Outra forma de fazer utilizando o Apply, uma forma mais simples e direta
df["idCliente"].apply(get_last_id)

# %%)