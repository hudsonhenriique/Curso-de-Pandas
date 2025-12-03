# %%
import pandas as pd
brinquedo = pd.DataFrame(
    {
    "nome":["Hudson","Marilaine","Henrique"],
    "idade": [33,34,5],
    "uf":["Mg","Ba","Sp"],
    }
)
filtro = brinquedo["idade"] >=18
brinquedo[filtro]

# %%
df = pd.read_csv("../data/transacoes.csv",sep = ";")
df.head()
# %%
# Valores maiores que 50
filtro = df["QtdePontos"] >= 50
df[filtro]
# %%
#Valores entre 50 (inclusive) e 100
filtro = (df["QtdePontos"] >=50) & (df["QtdePontos"] < 100)
df[filtro]

# %%
# Valores que são 1 ou 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]
# %%
# Pontos entre 0 e 50 só em 2025
filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <50) & (df["DtCriacao"] >= "2025-01-01")
df[filtro]
# %%