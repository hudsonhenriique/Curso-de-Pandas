# %%
# 06.06 - Como podemos calcular as estatísticas descritivas
# dos pontos das transações de cada usuário?

import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=';')
transacoes.head()
# %%

(transacoes.groupby(by=['IdCliente'], as_index=False)['QtdePontos']
           .describe())
# %%
