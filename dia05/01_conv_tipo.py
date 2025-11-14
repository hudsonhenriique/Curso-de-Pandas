#%%
import pandas as pd

# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
df
# %%
# astype retorna uma série
df["qtdePontos"].astype(float).astype(str)

#%%
df["DtCriacao"]
# %%
df["DtCriacao"].replace({
    "0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000"})

# %%
pd.to_datetime(df["DtCriacao"])
# %%
replace = {"0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000"}
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))
# %%
df["DtCriacao"].dt.year
# %%
df["DtCriacao"].dt.month
# %%
df["DtCriacao"].dt.day
#%%

