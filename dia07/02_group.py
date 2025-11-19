#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
transacoes.head()
#
# %%
transacoes.groupby(by=["IdCliente"]).count()
# %%
# Executando assim ele retorna uma série
transacoes.groupby(by=["IdCliente"])["IdTransacao"].count()
# %%
# Executando assim ele retorna um dataframe
# as_index=False, cria um index para o nosso data frame, nos deixando o IdCliente como coluna no nosso DataFrame
transacoes.groupby(by=["IdCliente"],as_index=False)[["IdTransacao"]].count()
# %%
# Calculando mais de uma estatistica
summary = (transacoes.groupby(by=["IdCliente"],as_index=False)
          .agg({"IdTransacao":['count'],
                "QtdePontos":['sum','mean']}))
summary
# %%
# Nosso pequeno DataFrame se tornou MultiIndex
summary.columns
#MultiIndex([(  'IdCliente',      ''),
#            ('IdTransacao', 'count'),
#            ( 'QtdePontos',   'sum'),
#            ( 'QtdePontos',  'mean')],
#           )
# %%
# Trabalhando com MultiIndex
summary["QtdePontos"] #Retorna uma DataFrame
# %%
summary[("QtdePontos","mean")] # Retorna uma série

# %%
# Como nós definimos nossas colunas com MultiIndex
summary.columns = ['IdCliente',"QtdeTransacao","totalPontos","mediaPontos"]
summary
# %%
