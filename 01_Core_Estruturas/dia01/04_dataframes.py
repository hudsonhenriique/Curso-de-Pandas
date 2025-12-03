#%%
import pandas as pd

idades = [32,38,30,30,31,35,25,29,31,37,27,23,36,33,36]

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela",
         "Heitor", "Isabela", "João", "Laura", "Miguel", "Natália", "Otávio", "Patrícia"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
#%%
df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df
#%%
print(df.iloc[0])
print(df.iloc[3]["idades"])
print(df.iloc[-1]["nomes"])