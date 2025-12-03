#%%
import pandas as pd

df = pd.read_csv("../../exercicios/case_homicidios/Homidicios_consolidados.csv",sep=";")
df.head()
# %%
df_stack =(df.set_index(["nome","período"])
             .stack()
             .reset_index())
df_stack.columns = ["nome","período","metrica","valor"]
df_stack.head()
# %%
(df_stack.pivot_table(values="valor",
                     index=["nome","período"],
                     columns="metrica")
         .reset_index())

# %%
df_stack.pivot_table(values="valor",
                     index=["nome"],
                     columns="metrica",
                     aggfunc="mean",)
# %%
