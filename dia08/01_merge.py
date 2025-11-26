#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.rename(columns={'IdCliente': 'idCliente',
                           'QtdePontos':'qtdePontos'},
                           inplace=True)

transacoes.head()


#%%                
clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()
# %%

transacoes.merge(right=clientes,
                 how='left',
                 on=['idCliente'],
                 suffixes=('_Transação','_Cliente')).head()
# %%
df_1 = pd.DataFrame({
    "Transação":[1,2,3,4,5],
    "Nome":['t1','t2','t3','t4','t5'],
    "idCliente": [1,2,3,2,2],
    "Valor":[10,45,32,17,87],
})

df_2 = pd.DataFrame({
    "id":[1,2,3,4],
    "Nome":["Hudson","Marilaine","Henrique","Ana"],
})

df_1.merge(
    df_2,
    left_on=["idCliente"],
    right_on=["id"],
    how='left',
    suffixes=('_Transação','_Cliente')
)
# %%
