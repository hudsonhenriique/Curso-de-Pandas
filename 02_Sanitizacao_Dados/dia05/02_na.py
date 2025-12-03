#%%
import pandas as pd
# %%
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes
# %%
# Primeira opção - ignorar todos os NAN
clientes.dropna()
#
# %%
# Segunda opção - a linha inteira é NAN
clientes.dropna(how="all")
# %%
df = pd.DataFrame(
    {
        "nome": ["Hudson",None,"Henrique","Marilaine"],
        "idade": [None,None,27,40],
        "salario": [3435,4324,None,5423]
        }
)

df
# %%
df.dropna()
# %%
df.dropna(how="all", subset=["idade","nome"])
# %%
# Fill NA
df["nome"] = df["nome"].fillna("Carla")
df
# %%
df.fillna(0)
# DROP NA SUBSTITU A LINHA E FILLNA SUBSTITUI A CELULA
#%%
medias = df[["idade","salario"]].mean()
df.fillna(medias)
# %%
