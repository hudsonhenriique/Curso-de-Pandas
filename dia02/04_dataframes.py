# %%
import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
#%%
# Amostras
df_clientes.head(10)
#%%
df_clientes.tail(10)
#%%
df_clientes.sample(10)
#%%
df_clientes.shape
#%%
df_clientes.columns
#%%
df_clientes.index
#%%
df_clientes.info(memory_usage="deep")
#%%
df_clientes.dtypes
